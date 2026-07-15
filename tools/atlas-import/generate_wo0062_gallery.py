#!/usr/bin/env python3
"""Build the WO-0062 ten-seed candidate gallery and quality reports."""

from __future__ import annotations

import json
import shutil
import sys
import textwrap
from argparse import Namespace
from pathlib import Path

from PIL import Image, ImageDraw

from mapplan_candidate_compiler import compile_candidate


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
STUDIO = WORKSPACE / "AtlasStudio"
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
COMPILER = STUDIO / "atlas-tools/mapgen/compiler"
sys.path.insert(0, str(COMPILER))
from quality_auditor import QualityAuditor  # noqa: E402

OUTPUT = REPO / "reports/atlas-import/wo0062"
CONTACTS = COMPILER / "style_study/wo0060/contact_sheets"
RENDERER = COMPILER / "style_study/wo0060/render_map.py"
SHARED = COMPILER / "contract/examples/shared"
PALETTES = {
    "temperate": (HERE / "tile-palettes/temperate-village-interior.palette.json", SHARED / "style_pack_ashford_cozy_interior.json"),
    "coastal": (HERE / "tile-palettes/coastal-settlement-interior.palette.json", SHARED / "style_pack_coastal_settlement_interior.json"),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    plans = [path for path in sorted((COMPILER / "prototypes/wo0059").glob("*.map_plan.json"))
             if path.name.startswith(("house-", "shop-"))][:10]
    if len(plans) < 10:
        raise SystemExit("WO-0062 requires at least ten structural fixtures")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    auditor = QualityAuditor()
    records = []
    for index, plan_path in enumerate(plans, start=1):
        style_name = "temperate" if index % 2 else "coastal"
        palette_path, style_path = PALETTES[style_name]
        slug = f"{index:02d}-{plan_path.stem.replace('.map_plan', '')}-{style_name}"
        candidate_dir = OUTPUT / "candidates" / slug
        project = candidate_dir / "fixture-project"
        (project / "data").mkdir(parents=True)
        (project / "map_ownership.json").write_text(json.dumps({
            "schema_version": "1.0", "maps": {"1": {"state": "generated", "atlas_screen": None, "name": slug}}
        }, indent=2) + "\n", encoding="utf-8")
        result = compile_candidate(Namespace(
            map_plan=plan_path, palette=palette_path, style_pack=style_path, source_project=GAME,
            target_project=project, map_id=1, output_dir=candidate_dir, contact_root=CONTACTS, renderer=RENDERER,
        ))
        plan, palette = load(plan_path), load(palette_path)
        quality = auditor.audit_generated_candidate(
            plan=plan, map_json=load(result["map"]), manifest=load(result["manifest"]),
            diagnostics=load(result["diagnostics"]), palette=palette,
        )
        quality_path = candidate_dir / "quality.json"
        quality_path.write_text(json.dumps(quality, indent=2) + "\n", encoding="utf-8")
        intent = plan["map_intent"]
        records.append({
            "candidate_id": slug, "seed": intent.get("generation_seed"), "archetype": intent.get("archetype_ref"),
            "layout_family": intent.get("layout_family_ref"), "variant": intent.get("variant_id"),
            "style_pack": palette["style_pack_ref"], "palette_version": palette["version"],
            "hard_passed": quality["hard_passed"], "advisory_score": quality["advisory"]["score"],
            "rejection_reasons": [item["code"] for item in quality["hard_findings"]],
            "human_review": quality["human_review"], "promotion": "not_applied",
            "render": str(result["render"]), "quality_report": str(quality_path),
        })
    build_contact_sheet(records, OUTPUT / "seed-gallery.png")
    payload = {"schema_version": "0.1", "candidate_count": len(records), "hard_pass_count": sum(item["hard_passed"] for item in records),
               "human_review_boundary": "Scores never accept, reject, or promote candidates. Record human decisions separately.", "candidates": records}
    (OUTPUT / "index.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(records)} candidates and {OUTPUT / 'seed-gallery.png'}")


def build_contact_sheet(records: list[dict], path: Path) -> None:
    thumb_w, thumb_h, label_h = 264, 336, 112
    sheet = Image.new("RGB", (thumb_w * 5, (thumb_h + label_h) * 2), (22, 25, 32))
    draw = ImageDraw.Draw(sheet)
    for index, record in enumerate(records):
        image = Image.open(record["render"]).convert("RGB").resize((thumb_w, thumb_h))
        x, y = (index % 5) * thumb_w, (index // 5) * (thumb_h + label_h)
        sheet.paste(image, (x, y))
        label_lines = [record["candidate_id"], f"seed {record['seed']}"]
        label_lines += textwrap.wrap(str(record["archetype"]), width=40)
        label_lines += textwrap.wrap(str(record["layout_family"]), width=40)
        label_lines += textwrap.wrap(f"{record['style_pack']} v{record['palette_version']}", width=40)
        label_lines.append(f"HARD {'PASS' if record['hard_passed'] else 'FAIL'} | ADV {record['advisory_score']}")
        label = "\n".join(label_lines)
        draw.multiline_text((x + 5, y + thumb_h + 4), label, fill=(240, 235, 220), spacing=2)
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(path)


if __name__ == "__main__":
    main()
