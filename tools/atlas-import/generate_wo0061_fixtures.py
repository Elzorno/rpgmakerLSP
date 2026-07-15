#!/usr/bin/env python3
"""Generate disposable temperate/coastal WO-0061 candidate projects."""

from __future__ import annotations

import json
import shutil
from argparse import Namespace
from pathlib import Path

from mapplan_candidate_compiler import compile_candidate


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
STUDIO = WORKSPACE / "AtlasStudio"
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
REPORT = REPO / "reports/atlas-import/wo0061"
PLAN = STUDIO / "atlas-tools/mapgen/compiler/prototypes/wo0059/shop-compact-seed-1.map_plan.json"
CONTACTS = STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/contact_sheets"
RENDERER = STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/render_map.py"
SHARED = STUDIO / "atlas-tools/mapgen/compiler/contract/examples/shared"


STYLES = {
    "temperate": (
        HERE / "tile-palettes/temperate-village-interior.palette.json",
        SHARED / "style_pack_ashford_cozy_interior.json",
    ),
    "coastal": (
        HERE / "tile-palettes/coastal-settlement-interior.palette.json",
        SHARED / "style_pack_coastal_settlement_interior.json",
    ),
}


def main() -> None:
    if REPORT.exists():
        shutil.rmtree(REPORT)
    summary = {"schema_version": "0.1", "source_map_plan": str(PLAN), "candidates": []}
    for name, (palette, style) in STYLES.items():
        root = REPORT / name / "fixture-project"
        (root / "data").mkdir(parents=True)
        (root / "map_ownership.json").write_text(json.dumps({
            "schema_version": "1.0", "maps": {"1": {"state": "generated", "atlas_screen": None, "name": f"WO-0061 {name} candidate"}}
        }, indent=2) + "\n", encoding="utf-8")
        result = compile_candidate(Namespace(
            map_plan=PLAN, palette=palette, style_pack=style, source_project=GAME,
            target_project=root, map_id=1, output_dir=REPORT / name,
            contact_root=CONTACTS, renderer=RENDERER,
        ))
        summary["candidates"].append({
            "style": name, "map": str(result["map"]), "render": str(result["render"]),
            "dimensions": result["dimensions"], "events": result["events"],
            "data_length": result["data_length"], "route_audit": result["route_audit"],
        })
    (REPORT / "index.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(summary['candidates'])} guarded candidates from one MapPlan in {REPORT}")


if __name__ == "__main__":
    main()
