#!/usr/bin/env python3
"""Generate the disposable, non-canon WO-0063 settlement vertical slice."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw

from autotile import paint_region
from mapplan_candidate_compiler import atomic_json, event_page


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
STUDIO = WORKSPACE / "AtlasStudio"
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
COMPILER = STUDIO / "atlas-tools/mapgen/compiler"
sys.path.insert(0, str(COMPILER))
from map_plan import MapPlan  # noqa: E402
from quality_auditor import QualityAuditor  # noqa: E402
from structural_preview import render_ascii, render_svg  # noqa: E402

OUTPUT = REPO / "reports/atlas-import/wo0063"
CONTACTS = OUTPUT / "contact_sheets"
RENDERER = COMPILER / "style_study/wo0060/render_map.py"
SEEDS = (6301, 6302, 6303)
WIDTH, HEIGHT = 40, 30


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rect(x: int, y: int, w: int, h: int) -> dict:
    return {"shape": "rect", "x": x, "y": y, "w": w, "h": h}


def build_plan(seed: int) -> dict:
    mirrored = seed % 2 == 0
    left, right = ("inn", "shop") if mirrored else ("shop", "inn")
    zones = {
        "entry": (18, 27, 4, 3, "entry_threshold"),
        "civic_spine": (18, 9, 4, 18, "civic_spine"),
        "landmark_plaza": (16, 4, 8, 6, "landmark_plaza"),
        f"{left}_plot": (5, 7, 9, 7, f"{left}_plot"),
        f"{right}_plot": (26, 7, 9, 7, f"{right}_plot"),
        "house_plot": (5 if not mirrored else 26, 18, 9, 7, "house_plot"),
        "curiosity_garden": (26 if not mirrored else 5, 18, 9, 7, "curiosity_garden"),
    }
    terrain = [{"terrain_id": f"ZONE-{key}", "terrain_type": role, "area": rect(x, y, w, h), "movement": "walkable"}
               for key, (x, y, w, h, role) in zones.items()]
    edges = [
        ("entry", "civic_spine", True), ("civic_spine", "landmark_plaza", True),
        ("civic_spine", "shop_plot", True), ("civic_spine", "inn_plot", True),
        ("civic_spine", "house_plot", True), ("civic_spine", "curiosity_garden", False),
    ]
    obstacles, anchors = [], []
    for building in ("shop", "inn", "house"):
        zx, zy, zw, zh, _ = zones[f"{building}_plot"]
        footprint = rect(zx + 1, zy + 1, zw - 2, 4)
        obstacles.append({"obstacle_id": f"BLDG-{building.upper()}", "name": f"building_{building}", "area": footprint,
                          "blocking": True, "parent_zone": f"{building}_plot", "clearance": 1})
        anchors.append({"local_anchor_id": f"DOOR-{building.upper()}", "anchor": {"shape": "point", "x": zx + zw // 2, "y": zy + 5},
                        "trigger_intent": f"exterior_door_{building}"})
    anchors.append({"local_anchor_id": "CURIOSITY-GARDEN", "anchor": {"shape": "point", "x": zones["curiosity_garden"][0] + 4, "y": 21},
                    "trigger_intent": "optional_curiosity_hook"})
    payload = {
        "schema_version": "0.1", "blueprint_id": f"BP-WO0063-SETTLEMENT-{seed}", "atlas_screen_id": None,
        "title": f"Disposable Generated Settlement Seed {seed}",
        "source_documents": ["atlas/workorders/WO-0063-first-generated-settlement-vertical-slice.md"],
        "map_intent": {"purpose": "Non-canon reusable settlement vertical-slice fixture", "layout_mode": "procedural",
                       "generation_seed": seed, "critical_path_role": "disposable_fixture",
                       "archetype_ref": "ARCH-SETTLEMENT-VERTICAL-SLICE@0.1", "layout_family_ref": "LAY-SETTLEMENT-CIVIC-SPINE@0.1",
                       "variant_id": "mirrored" if mirrored else "standard"},
        "dimensions": {"width": WIDTH, "height": HEIGHT, "unit": "tile", "coordinate_system": "atlas_tile", "origin": "top_left"},
        "terrain": terrain,
        "traversable_areas": [{"area_id": f"ROAD-{i+1}", "from_zone": a, "to_zone": b, "connector_type": "road_connection", "required": required}
                              for i, (a, b, required) in enumerate(edges)],
        "obstacles": obstacles,
        "transfer_points": [{"transfer_id": "SETTLEMENT-ENTRY-EXIT", "anchor": {"shape": "point", "x": 19, "y": 28}, "placement_intent": "fixture_entry_exit"}],
        "event_anchors": anchors,
        "landmark_slots": [{"landmark_tag": "civic_well_landmark", "zone_role": "landmark_plaza", "zone_id": "landmark_plaza",
                            "required": True, "dominant": True, "anchor": {"shape": "point", "x": 19, "y": 6}}],
        "validation": {"entry_zone": "entry", "must_reach": ["landmark_plaza", "shop_plot", "inn_plot", "house_plot"],
                       "assembly_order": ["primary_landmark", "entry_and_civic_spine", "plots", "structures", "secondary_paths", "dressing"]},
        "generation_manifest_ref": f"GEN-WO0063-{seed}",
    }
    return MapPlan.from_dict(payload).to_dict()


def binding(tag: str, sheet: str, addressing: str, index: int, role: str, notes: str) -> dict:
    base = {"Outside_A5": 1536, "Outside_B": 0, "Outside_C": 256}.get(sheet, 0)
    tile_id = 2048 + index * 48 if addressing == "autotile_kind" else base + index
    return {"visual_tag": tag, "asset_sheet": sheet, "source_index": {"addressing": addressing, "index": index},
            "tile_id": tile_id, "role": role, "provenance": {"contact_sheet": f"{sheet.lower()}_{'kinds' if addressing == 'autotile_kind' else 'tiles'}.png", "notes": notes}}


def build_palette(style: str, flags: list[int]) -> dict:
    base_kind, road_kind = (16, 19) if style == "temperate" else (17, 42)
    entries = [
        binding("settlement_ground", "Outside_A2", "autotile_kind", base_kind, "ground", "Labeled Outside_A2 contact sheet; accepted project tileset."),
        binding("civic_road", "Outside_A2", "autotile_kind", road_kind, "road", "Labeled Outside_A2 contact sheet; accepted project tileset."),
        binding("roof_left", "Outside_B", "normal_tile", 13, "building", "Roof left segment on labeled Outside_B sheet."),
        binding("roof_middle", "Outside_B", "normal_tile", 14, "building", "Roof middle segment on labeled Outside_B sheet."),
        binding("roof_right", "Outside_B", "normal_tile", 15, "building", "Roof right segment on labeled Outside_B sheet."),
        binding("wall_left", "Outside_B", "normal_tile", 82, "building", "Exterior wall left segment on labeled Outside_B sheet."),
        binding("wall_middle", "Outside_B", "normal_tile", 83, "building", "Exterior wall middle segment on labeled Outside_B sheet."),
        binding("wall_right", "Outside_B", "normal_tile", 84, "building", "Exterior wall right segment on labeled Outside_B sheet."),
        binding("window", "Outside_B", "normal_tile", 96, "building", "Window tile on labeled Outside_B sheet."),
        binding("door", "Outside_B", "normal_tile", 114, "threshold", "Exterior door tile on labeled Outside_B sheet."),
        binding("shop_sign", "Outside_B", "normal_tile", 66, "service", "Shop sign on labeled Outside_B sheet."),
        binding("inn_sign", "Outside_B", "normal_tile", 70, "service", "Inn sign on labeled Outside_B sheet."),
        binding("civic_well_landmark", "Outside_B", "normal_tile", 139, "landmark", "Stone well on labeled Outside_B sheet."),
        binding("tree_top", "Outside_B", "normal_tile", 184, "dressing", "Tree canopy on labeled Outside_B sheet."),
        binding("tree_base", "Outside_B", "normal_tile", 200, "dressing", "Tree trunk/base on labeled Outside_B sheet."),
        binding("flower_patch", "Outside_B", "normal_tile", 160, "dressing", "Flower patch on labeled Outside_B sheet."),
    ]
    tileset_pngs = {path.stem: sha256(path) for path in (GAME / "img/tilesets").glob("Outside_*.png")}
    for item in entries:
        item["flags"] = int(flags[item["tile_id"]])
        item["passage"] = "passable" if not (item["flags"] & 15) else "blocked" if (item["flags"] & 15) == 15 else "directional"
        item["layer"] = "base" if item["asset_sheet"].startswith("Outside_A") else "object"
        item["adjacency"] = "autotile_48" if item["source_index"]["addressing"] == "autotile_kind" else "none"
        item["source_sha256"] = tileset_pngs[item["asset_sheet"]]
    return {"schema_version": "0.1", "tile_palette_id": f"PAL-WO0063-{style.upper()}-EXTERIOR", "version": "0.1",
            "style_pack_ref": f"STY-WO0063-{style.upper()}-SETTLEMENT", "target_engine": "rpg_maker_mz", "tileset_id": 2,
            "tileset_name": "Outside", "status": "generated_pending_live_review", "bindings": entries, "owner_repo": "rpgmakerLSP",
            "provenance": {"target_tilesets_sha256": sha256(GAME / "data/Tilesets.json"), "contact_sheet_root": str(CONTACTS),
                           "notes": "Disposable WO-0063 exterior palette grounded in labeled Outside contact sheets and accepted clean-project tileset flags."},
            "human_review": {"rpg_maker_live_confirmed": False}}


def compile_map(plan: dict, palette: dict, style: str) -> tuple[dict, dict]:
    width, height = WIDTH, HEIGHT
    data = [0] * (width * height * 6)
    flags = json.loads((GAME / "data/Tilesets.json").read_text(encoding="utf-8"))[2]["flags"]
    by_tag = {item["visual_tag"]: item for item in palette["bindings"]}
    def set_tile(x, y, layer, value): data[(layer * height + y) * width + x] = value
    ground = {(x, y) for y in range(height) for x in range(width)}
    paint_region(set_tile, ground, by_tag["settlement_ground"]["source_index"]["index"], 0)
    roads = {(x, y) for y in range(9, 30) for x in range(18, 22)} | {(x, y) for y in range(14, 17) for x in range(5, 35)} | {(x, y) for y in range(4, 10) for x in range(16, 24)}
    for anchor in plan["event_anchors"]:
        if anchor["local_anchor_id"].startswith("DOOR-"):
            ax, ay = anchor["anchor"]["x"], anchor["anchor"]["y"]
            roads |= {(ax, y) for y in range(min(ay, 15), max(ay, 15) + 1)}
    paint_region(set_tile, roads, by_tag["civic_road"]["source_index"]["index"], 0)
    collision = set()
    for obstacle in plan["obstacles"]:
        area = obstacle["area"]; x0, y0, w, h = area["x"], area["y"], area["w"], area["h"]
        door_x, door_y = x0 + w // 2, y0 + h - 1
        for x in range(x0, x0 + w):
            set_tile(x, y0, 2, by_tag["roof_left" if x == x0 else "roof_right" if x == x0 + w - 1 else "roof_middle"]["tile_id"])
        for y in range(y0 + 1, y0 + h):
            for x in range(x0, x0 + w):
                set_tile(x, y, 1, by_tag["wall_left" if x == x0 else "wall_right" if x == x0 + w - 1 else "wall_middle"]["tile_id"])
                collision.add((x, y))
        set_tile(door_x, door_y, 2, by_tag["door"]["tile_id"])
        set_tile(x0 + 1, door_y, 2, by_tag["window"]["tile_id"]); set_tile(x0 + w - 2, door_y, 2, by_tag["window"]["tile_id"])
        sign = "shop_sign" if "SHOP" in obstacle["obstacle_id"] else "inn_sign" if "INN" in obstacle["obstacle_id"] else None
        if sign: set_tile(door_x, y0 + 1, 3, by_tag[sign]["tile_id"])
    well = plan["landmark_slots"][0]["anchor"]; set_tile(well["x"], well["y"], 2, by_tag["civic_well_landmark"]["tile_id"]); collision.add((well["x"], well["y"]))
    garden = next(item for item in plan["terrain"] if item["terrain_type"] == "curiosity_garden")["area"]
    for dx, dy in ((1, 1), (3, 2), (5, 1), (6, 4)): set_tile(garden["x"] + dx, garden["y"] + dy, 2, by_tag["flower_patch"]["tile_id"])
    if style == "temperate":
        for x, y in ((2, 4), (37, 5), (2, 23), (37, 22)):
            set_tile(x, y, 2, by_tag["tree_top"]["tile_id"]); set_tile(x, y + 1, 2, by_tag["tree_base"]["tile_id"]); collision |= {(x, y), (x, y + 1)}
    events = [None]
    semantic = plan["transfer_points"] + plan["event_anchors"]
    for item in semantic:
        identity = item.get("transfer_id") or item.get("local_anchor_id"); anchor = item["anchor"]
        comments = [{"code": 108, "indent": 0, "parameters": [f"WO-0063 semantic identity: {identity}; no unsupported destination/dialogue authored."]}]
        events.append({"id": len(events), "name": identity, "note": "WO-0063 semantic candidate anchor", "pages": [event_page(comments, trigger=0, priority=0)], "x": anchor["x"], "y": anchor["y"]})
    for x, y in sorted(collision):
        events.append({"id": len(events), "name": f"ADAPTER-COLLISION-{x}-{y}", "note": "Adapter building/landmark collision blocker",
                       "pages": [event_page([], trigger=0)], "x": x, "y": y})
    region_ids = {item["terrain_type"]: i + 1 for i, item in enumerate(plan["terrain"])}
    for item in plan["terrain"]:
        a = item["area"]
        for y in range(a["y"], a["y"] + a["h"]):
            for x in range(a["x"], a["x"] + a["w"]): set_tile(x, y, 5, region_ids[item["terrain_type"]])
    map_json = {"autoplayBgm": False, "autoplayBgs": False, "battleback1Name": "", "battleback2Name": "",
                "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90}, "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
                "disableDashing": False, "displayName": plan["title"], "encounterList": [], "encounterStep": 30, "height": height,
                "note": f"WO-0063 disposable settlement candidate; {palette['tile_palette_id']}", "parallaxLoopX": False, "parallaxLoopY": False,
                "parallaxName": "", "parallaxShow": True, "parallaxSx": 0, "parallaxSy": 0, "scrollType": 0, "specifyBattleback": False,
                "tilesetId": 2, "width": width, "data": data, "events": events}
    start = (19, 28); reached = bfs(width, height, start, collision)
    failures = []
    for item in semantic:
        p = (item["anchor"]["x"], item["anchor"]["y"]); ring = {(p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)}
        if p not in reached and not ring & reached: failures.append(item.get("transfer_id") or item.get("local_anchor_id"))
    if failures: raise RuntimeError(f"unreachable settlement anchors: {failures}")
    return map_json, {"result": "pass", "origin": list(start), "reachable_cells": len(reached), "interaction_ring_failures": []}


def bfs(width: int, height: int, start: tuple[int, int], blocked: set[tuple[int, int]]) -> set[tuple[int, int]]:
    seen, queue = {start}, deque([start])
    while queue:
        x, y = queue.popleft()
        for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= p[0] < width and 0 <= p[1] < height and p not in seen and p not in blocked:
                seen.add(p); queue.append(p)
    return seen


def render(map_path: Path, output: Path) -> None:
    spec = importlib.util.spec_from_file_location("wo0063_renderer", RENDERER); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    module.GAME = str(GAME); module.render_map(str(map_path), str(GAME / "data/Tilesets.json"), str(output))


def main() -> None:
    if OUTPUT.exists():
        contacts_tmp = {p.name: p.read_bytes() for p in CONTACTS.glob("*.png")} if CONTACTS.exists() else {}
        shutil.rmtree(OUTPUT); CONTACTS.mkdir(parents=True)
        for name, body in contacts_tmp.items(): (CONTACTS / name).write_bytes(body)
    else: OUTPUT.mkdir(parents=True)
    tilesets = json.loads((GAME / "data/Tilesets.json").read_text(encoding="utf-8")); flags = tilesets[2]["flags"]
    records, auditor = [], QualityAuditor()
    for style in ("temperate", "coastal"):
        palette = build_palette(style, flags); palette_path = OUTPUT / f"{style}.exterior.palette.json"; atomic_json(palette_path, palette)
        for seed in SEEDS:
            plan = build_plan(seed); slug = f"{style}-seed-{seed}"; root = OUTPUT / "candidates" / slug; project = root / "fixture-project"
            (project / "data").mkdir(parents=True); atomic_json(project / "map_ownership.json", {"schema_version": "1.0", "maps": {"1": {"state": "generated", "name": slug}}})
            plan_path = root / "settlement.map_plan.json"; atomic_json(plan_path, plan)
            plan_model = MapPlan.from_dict(plan)
            (root / "settlement.structural.txt").write_text(render_ascii(plan_model), encoding="utf-8")
            (root / "settlement.structural.svg").write_text(render_svg(plan_model), encoding="utf-8")
            map_json, route = compile_map(plan, palette, style); map_path = project / "data/Map001.json"; atomic_json(map_path, map_json)
            diagnostics_path = root / "candidate.diagnostics.json"; atomic_json(diagnostics_path, {"schema_version": "0.1", "route_audit": route, "errors": [], "warnings": []})
            render_path = root / "candidate.render.png"; render(map_path, render_path)
            manifest = {"schema_version": "0.1", "status": "generated_pending_review", "map_plan": str(plan_path), "palette": str(palette_path),
                        "style_pack": palette["style_pack_ref"], "candidate_map": str(map_path), "render": str(render_path), "promotion": "not_applied",
                        "ownership_state": "generated", "round_trip_contract": "fixture_unbound_safe",
                        "human_review": {"status": "pending", "decision": None, "reviewer": None, "reviewed_at": None, "notes": None},
                        "provenance": {"map_plan_sha256": sha256(plan_path), "palette_sha256": sha256(palette_path), "style_pack_sha256": hashlib.sha256(palette["style_pack_ref"].encode()).hexdigest(),
                                       "candidate_map_sha256": sha256(map_path), "render_sha256": sha256(render_path), "tilesets_sha256": sha256(GAME / "data/Tilesets.json")}}
            manifest_path = root / "candidate.manifest.json"; atomic_json(manifest_path, manifest)
            quality = auditor.audit_generated_candidate(plan=plan, map_json=map_json, manifest=manifest, diagnostics={"route_audit": route}, palette=palette)
            atomic_json(root / "quality.json", quality)
            records.append({"candidate_id": slug, "seed": seed, "style": style, "archetype": "ARCH-SETTLEMENT-VERTICAL-SLICE@0.1",
                            "layout_family": "LAY-SETTLEMENT-CIVIC-SPINE@0.1", "palette": palette["tile_palette_id"], "hard_passed": quality["hard_passed"],
                            "advisory_score": quality["advisory"]["score"], "render": str(render_path), "human_review": manifest["human_review"], "promotion": "not_applied"})
    gallery(records, OUTPUT / "settlement-gallery.png"); atomic_json(OUTPUT / "index.json", {"schema_version": "0.1", "candidate_count": len(records), "candidates": records})
    print(f"Generated {len(records)} WO-0063 settlement candidates")


def gallery(records: list[dict], path: Path) -> None:
    tw, th, lh = 360, 270, 80; image = Image.new("RGB", (tw * 3, (th + lh) * 2), (20, 23, 29)); draw = ImageDraw.Draw(image)
    for i, record in enumerate(records):
        source = Image.open(record["render"]).convert("RGB"); source.thumbnail((tw, th)); x, y = (i % 3) * tw, (i // 3) * (th + lh)
        image.paste(source, (x + (tw-source.width)//2, y)); draw.multiline_text((x+5,y+th+3), f"{record['candidate_id']}\n{record['archetype']}\n{record['layout_family']}\nHARD {'PASS' if record['hard_passed'] else 'FAIL'} | ADV {record['advisory_score']}", fill=(240,235,220))
    image.save(path)


if __name__ == "__main__": main()
