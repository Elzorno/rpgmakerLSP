#!/usr/bin/env python3
"""WO-0065: rebuild the disposable settlement vertical slice against real
Dragon Quest town grammar (see AtlasStudio/academy/case-studies/dragon-quest-town-grammar-001.md),
after WO-0064's independent review found the WO-0063 candidate reading as a
generic road-and-building diagram with no enclosing boundary, one repeated
building shell, and an undressed curiosity marker.

Keeps WO-0063's manifest/provenance/quality-audit/gallery machinery
unchanged (WO-0064 found it genuinely robust) and produces a new,
independent output tree rather than overwriting WO-0063's own -- that
output is cited evidence in WO-0064's report and stays intact.
"""

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

OUTPUT = REPO / "reports/atlas-import/wo0065"
CONTACTS = REPO / "reports/atlas-import/wo0063/contact_sheets"  # reuse WO-0063's verified Outside contact sheets
RENDERER = COMPILER / "style_study/wo0060/render_map.py"
SEEDS = (6301, 6302, 6303)
WIDTH, HEIGHT = 30, 24
TOWN = (2, 2, 26, 20)  # x, y, w, h -- inset from the map edge, walled/moated ring painted on its border


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rect(x: int, y: int, w: int, h: int) -> dict:
    return {"shape": "rect", "x": x, "y": y, "w": w, "h": h}


def build_plan(seed: int) -> dict:
    mirrored = seed % 2 == 0
    left, right = ("inn", "shop") if mirrored else ("shop", "inn")
    zones = {
        "entry": (13, 19, 4, 3, "entry_threshold"),
        "civic_spine": (13, 8, 4, 12, "civic_spine"),
        "landmark_plaza": (11, 3, 8, 5, "landmark_plaza"),
        f"{left}_plot": (4, 6, 8, 6, f"{left}_plot"),
        f"{right}_plot": (18, 6, 8, 6, f"{right}_plot"),
        "house_plot": (4 if not mirrored else 18, 14, 8, 6, "house_plot"),
        "curiosity_garden": (18 if not mirrored else 4, 14, 8, 6, "curiosity_garden"),
    }
    # Per-archetype footprint width, per dragon-quest-town-grammar-001.md finding
    # #3 ("buildings vary in footprint, not just signage") -- shop narrowest,
    # inn widest (it is the biggest building in most DQ towns), house smallest.
    footprint_w = {"shop": 5, "inn": 7, "house": 4}
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
        fw = footprint_w[building]
        fx = zx + (zw - fw) // 2
        footprint = rect(fx, zy + 1, fw, 4)
        obstacles.append({"obstacle_id": f"BLDG-{building.upper()}", "name": f"building_{building}", "area": footprint,
                          "blocking": True, "parent_zone": f"{building}_plot", "clearance": 1})
        anchors.append({"local_anchor_id": f"DOOR-{building.upper()}", "anchor": {"shape": "point", "x": fx + fw // 2, "y": zy + 5},
                        "trigger_intent": f"exterior_door_{building}"})
    cx, cy, cw, ch = zones["curiosity_garden"][:4]
    anchors.append({"local_anchor_id": "CURIOSITY-GARDEN", "anchor": {"shape": "point", "x": cx + cw // 2, "y": cy + ch - 2},
                    "trigger_intent": "optional_curiosity_hook"})
    payload = {
        "schema_version": "0.1", "blueprint_id": f"BP-WO0065-SETTLEMENT-{seed}", "atlas_screen_id": None,
        "title": f"Disposable Generated Settlement Seed {seed} (WO-0065 Dragon Quest grammar rebuild)",
        "source_documents": [
            "atlas/workorders/WO-0065-dragon-quest-settlement-grammar-remediation.md",
            "academy/case-studies/dragon-quest-town-grammar-001.md",
        ],
        "map_intent": {"purpose": "Non-canon reusable settlement vertical-slice fixture, rebuilt against Dragon Quest town grammar", "layout_mode": "procedural",
                       "generation_seed": seed, "critical_path_role": "disposable_fixture",
                       "archetype_ref": "ARCH-SETTLEMENT-VERTICAL-SLICE@0.2", "layout_family_ref": "LAY-SETTLEMENT-CIVIC-SPINE@0.2",
                       "variant_id": "mirrored" if mirrored else "standard"},
        "dimensions": {"width": WIDTH, "height": HEIGHT, "unit": "tile", "coordinate_system": "atlas_tile", "origin": "top_left"},
        "terrain": terrain,
        "traversable_areas": [{"area_id": f"ROAD-{i+1}", "from_zone": a, "to_zone": b, "connector_type": "road_connection", "required": required}
                              for i, (a, b, required) in enumerate(edges)],
        "obstacles": obstacles,
        "transfer_points": [{"transfer_id": "SETTLEMENT-ENTRY-EXIT", "anchor": {"shape": "point", "x": 15, "y": 23}, "placement_intent": "fixture_entry_exit"}],
        "event_anchors": anchors,
        "landmark_slots": [{"landmark_tag": "civic_well_landmark", "zone_role": "landmark_plaza", "zone_id": "landmark_plaza",
                            "required": True, "dominant": True, "anchor": {"shape": "point", "x": 15, "y": 5}}],
        "validation": {"entry_zone": "entry", "must_reach": ["landmark_plaza", "shop_plot", "inn_plot", "house_plot"],
                       "assembly_order": ["perimeter_boundary", "primary_landmark", "entry_and_civic_spine", "plots", "structures", "secondary_paths", "dressing"]},
        "generation_manifest_ref": f"GEN-WO0065-{seed}",
    }
    return MapPlan.from_dict(payload).to_dict()


def binding(tag: str, sheet: str, addressing: str, index: int, role: str, notes: str) -> dict:
    base = {"Outside_A5": 1536, "Outside_B": 0, "Outside_C": 256}.get(sheet, 0)
    tile_id = 2048 + index * 48 if addressing == "autotile_kind" else base + index
    return {"visual_tag": tag, "asset_sheet": sheet, "source_index": {"addressing": addressing, "index": index},
            "tile_id": tile_id, "role": role, "provenance": {"contact_sheet": f"{sheet.lower()}_{'kinds' if addressing == 'autotile_kind' else 'tiles'}.png", "notes": notes}}


def build_palette(style: str, flags: list[int]) -> dict:
    base_kind, plaza_kind = (16, 26) if style == "temperate" else (17, 34)
    entries = [
        binding("settlement_ground", "Outside_A2", "autotile_kind", base_kind, "ground", "Labeled Outside_A2 contact sheet; accepted project tileset."),
        binding("plaza_paving", "Outside_A2", "autotile_kind", plaza_kind, "ground", "Cobblestone/pebble kind on labeled Outside_A2 sheet -- distinct paved-plaza floor, per Coneria/Cantlin plaza-material finding."),
        binding("civic_road", "Outside_A2", "autotile_kind", 32 if style == "temperate" else 42, "road", "Warm brown dirt-path kind on labeled Outside_A2 sheet (temperate) -- Pass 2 correction: the Dragon Warrior/Dragon Quest town paths viewed directly (Brecconary, Cantlin, Rimuldar, Kol, Hamlin, Leftwyne) are warm dirt/brick, not grey cobblestone; kind 18 (grey, used in Pass 1) was a real color mismatch. Coastal keeps the grey cobblestone kind (42), read as a stone dockside path."),
        binding("boundary_water", "Outside_A1", "autotile_kind", 0, "boundary", "Plain water kind on labeled Outside_A1 sheet -- coastal perimeter moat, per Rimuldar finding."),
        binding("pond_water", "Outside_A1", "autotile_kind", 0, "landmark", "Same verified water kind as boundary_water, reused for the plaza's central pond -- per Hamlin/Leftwyne finding that water, not only a well, functions as the dominant landmark in several Dragon Quest towns."),
        binding("roof_left", "Outside_B", "normal_tile", 13, "building", "Roof left segment on labeled Outside_B sheet."),
        binding("roof_middle", "Outside_B", "normal_tile", 14, "building", "Roof middle segment on labeled Outside_B sheet."),
        binding("roof_right", "Outside_B", "normal_tile", 15, "building", "Roof right segment on labeled Outside_B sheet."),
        binding("wall_left", "Outside_B", "normal_tile", 82, "building", "Exterior wall left segment on labeled Outside_B sheet."),
        binding("wall_middle", "Outside_B", "normal_tile", 83, "building", "Exterior wall middle segment on labeled Outside_B sheet."),
        binding("wall_right", "Outside_B", "normal_tile", 84, "building", "Exterior wall right segment on labeled Outside_B sheet."),
        binding("window", "Outside_B", "normal_tile", 96, "building", "Window tile on labeled Outside_B sheet."),
        binding("door", "Outside_B", "normal_tile", 114, "threshold", "Exterior door tile on labeled Outside_B sheet."),
        binding("shop_sign", "Outside_B", "normal_tile", 66, "service", "Shield/exclamation shop sign on labeled Outside_B sheet."),
        binding("inn_sign", "Outside_B", "normal_tile", 70, "service", "'INN' text sign on labeled Outside_B sheet."),
        binding("house_sign", "Outside_B", "normal_tile", 137, "service", "Plain wooden signpost (two arrow-boards) on labeled Outside_B sheet -- gives House its own visible marker (WO-0064 F4: House previously had no sign at all). Index verified by direct crop after index 105 turned out to be a barred window, not a sign -- see WO-0065 report."),
        binding("civic_well_landmark", "Outside_B", "normal_tile", 139, "landmark", "Stone well/barrel on labeled Outside_B sheet."),
        binding("hedge", "Outside_B", "normal_tile", 178, "dressing", "Solid leaf hedge block on labeled Outside_B sheet -- single-tile temperate perimeter wall material, tiles edge-to-edge with no gaps (replaces an earlier two-tile 'tree top/base' pair that direct verification found was actually two different snow-pine sprites, not a matching top/bottom pair -- see WO-0065 report)."),
        binding("palm_tree", "Outside_B", "normal_tile", 236, "dressing", "Palm tree on labeled Outside_B sheet -- coastal-specific edge dressing, distinct material from the temperate hedge, per material-regional-contrast finding."),
        binding("flower_patch", "Outside_B", "normal_tile", 160, "dressing", "Flower patch on labeled Outside_B sheet."),
        binding("bush", "Outside_B", "normal_tile", 165, "dressing", "Round bush-tree on labeled Outside_B sheet, verified by direct crop."),
        binding("barrel", "Outside_B", "normal_tile", 141, "dressing", "Wooden barrel on labeled Outside_B sheet, verified by direct crop -- curiosity-cluster dressing."),
        binding("rock_pile", "Outside_B", "normal_tile", 140, "dressing", "Small rock pile on labeled Outside_B sheet -- curiosity-cluster dressing."),
        binding("mushroom_cluster", "Outside_B", "normal_tile", 234, "dressing", "Red-spotted mushroom cluster on labeled Outside_B sheet, verified by direct crop after index 232 turned out to be a plain rock pile, not mushrooms -- see WO-0065 report. Marks the curiosity nook as visually distinct from ordinary ground."),
    ]
    tileset_pngs = {path.stem: sha256(path) for path in (GAME / "img/tilesets").glob("Outside_*.png")}
    for item in entries:
        item["flags"] = int(flags[item["tile_id"]])
        item["passage"] = "passable" if not (item["flags"] & 15) else "blocked" if (item["flags"] & 15) == 15 else "directional"
        item["layer"] = "base" if item["asset_sheet"].startswith("Outside_A") else "object"
        item["adjacency"] = "autotile_48" if item["source_index"]["addressing"] == "autotile_kind" else "none"
        item["source_sha256"] = tileset_pngs[item["asset_sheet"]]
    return {"schema_version": "0.1", "tile_palette_id": f"PAL-WO0065-{style.upper()}-EXTERIOR", "version": "0.3",
            "style_pack_ref": f"STY-WO0063-{style.upper()}-SETTLEMENT", "target_engine": "rpg_maker_mz", "tileset_id": 2,
            "tileset_name": "Outside", "status": "generated_pending_live_review", "bindings": entries, "owner_repo": "rpgmakerLSP",
            "provenance": {"target_tilesets_sha256": sha256(GAME / "data/Tilesets.json"), "contact_sheet_root": str(CONTACTS),
                           "notes": "WO-0065 exterior palette, grounded in labeled Outside contact sheets, accepted clean-project tileset flags, and academy/case-studies/dragon-quest-town-grammar-001.md. Pass 2 (v0.3) additionally grounded in direct viewing of Kol (DQ1) and Hamlin/Leftwyne (DQ2)."},
            "human_review": {"rpg_maker_live_confirmed": False}}


def perimeter_cells(tx: int, ty: int, tw: int, th: int, gate_x0: int, gate_x1: int) -> set[tuple[int, int]]:
    cells = set()
    for x in range(tx, tx + tw):
        cells.add((x, ty)); cells.add((x, ty + th - 1))
    for y in range(ty, ty + th):
        cells.add((tx, y)); cells.add((tx + tw - 1, y))
    cells -= {(x, ty + th - 1) for x in range(gate_x0, gate_x1)}
    return cells


def path_cells() -> set[tuple[int, int]]:
    """Organic branching corridor set: an entry stem, an elbow into the
    plaza, then three separate branches out to each building plot (not one
    straight paved cross), per dragon-quest-town-grammar-001.md finding #2."""
    cells = set()
    def seg(x0, y0, x1, y1, width=2):
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                cells.add((x, y))
        return cells
    seg(14, 19, 15, 21)           # entry stem up from the gate
    seg(13, 12, 16, 19)           # elbow bend connecting entry stem to the civic spine
    seg(13, 8, 16, 13)            # civic spine core, adjacent to the plaza
    seg(14, 6, 16, 9)             # short branch up into the plaza
    seg(8, 9, 15, 10)             # branch west to shop/inn row
    seg(14, 9, 21, 10)            # branch east to shop/inn row
    seg(6, 10, 8, 15)             # branch down to house/curiosity row, west
    seg(20, 10, 22, 15)           # branch down to house/curiosity row, east
    return cells


def compile_map(plan: dict, palette: dict, style: str) -> tuple[dict, dict]:
    width, height = WIDTH, HEIGHT
    data = [0] * (width * height * 6)
    flags = json.loads((GAME / "data/Tilesets.json").read_text(encoding="utf-8"))[2]["flags"]
    by_tag = {item["visual_tag"]: item for item in palette["bindings"]}
    def set_tile(x, y, layer, value): data[(layer * height + y) * width + x] = value

    ground = {(x, y) for y in range(height) for x in range(width)}
    paint_region(set_tile, ground, by_tag["settlement_ground"]["source_index"]["index"], 0)

    tx, ty, tw, th = TOWN
    plaza = next(z for z in plan["terrain"] if z["terrain_type"] == "landmark_plaza")["area"]
    px, py, pw, ph = plaza["x"], plaza["y"], plaza["w"], plaza["h"]
    # Organic (chamfered, non-rectangular) plaza edge, per Kol's rounded open
    # clearing finding -- Pass 1 painted a hard rectangle.
    plaza_cells = {(x, y) for y in range(py, py + ph) for x in range(px, px + pw)}
    plaza_cells -= {(px, py), (px + 1, py), (px, py + 1), (px + pw - 1, py), (px + pw - 2, py), (px + pw - 1, py + 1),
                    (px, py + ph - 1), (px + 1, py + ph - 1), (px, py + ph - 2), (px + pw - 1, py + ph - 1), (px + pw - 2, py + ph - 1), (px + pw - 1, py + ph - 2)}
    paint_region(set_tile, plaza_cells, by_tag["plaza_paving"]["source_index"]["index"], 0)

    roads = path_cells()
    for anchor in plan["event_anchors"]:
        if anchor["local_anchor_id"].startswith("DOOR-"):
            ax, ay = anchor["anchor"]["x"], anchor["anchor"]["y"]
            roads |= {(ax, y) for y in range(ay, ay + 2)} | {(ax + 1, y) for y in range(ay, ay + 2)}
    roads -= {(x, y) for y in range(plaza["y"], plaza["y"] + plaza["h"]) for x in range(plaza["x"], plaza["x"] + plaza["w"])}
    paint_region(set_tile, roads, by_tag["civic_road"]["source_index"]["index"], 0)

    collision = set()

    gate_x0, gate_x1 = 14, 16
    boundary = perimeter_cells(tx, ty, tw, th, gate_x0, gate_x1)
    if style == "coastal":
        paint_region(set_tile, boundary, by_tag["boundary_water"]["source_index"]["index"], 0)
        collision |= boundary
    else:
        for (x, y) in sorted(boundary):
            set_tile(x, y, 2, by_tag["hedge"]["tile_id"])
            collision.add((x, y))

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
        if w >= 4:
            set_tile(x0 + 1, door_y, 2, by_tag["window"]["tile_id"]); set_tile(x0 + w - 2, door_y, 2, by_tag["window"]["tile_id"])
        sign = "shop_sign" if "SHOP" in obstacle["obstacle_id"] else "inn_sign" if "INN" in obstacle["obstacle_id"] else "house_sign"
        set_tile(door_x, y0 + 1, 3, by_tag[sign]["tile_id"])

    well = plan["landmark_slots"][0]["anchor"]; set_tile(well["x"], well["y"], 2, by_tag["civic_well_landmark"]["tile_id"]); collision.add((well["x"], well["y"]))
    # Small pond beside the well, per Hamlin/Leftwyne: water functions as a
    # dominant landmark in several Dragon Quest towns, not only a well.
    pond = {(well["x"] + 2, well["y"] + 1), (well["x"] + 3, well["y"] + 1)}
    paint_region(set_tile, pond, by_tag["pond_water"]["source_index"]["index"], 0)
    collision |= pond

    garden = next(item for item in plan["terrain"] if item["terrain_type"] == "curiosity_garden")["area"]
    gx, gy = garden["x"], garden["y"]
    for (dx, dy), tag in {(2, 2): "barrel", (3, 2): "rock_pile", (5, 2): "barrel", (2, 4): "mushroom_cluster", (5, 4): "mushroom_cluster"}.items():
        set_tile(gx + dx, gy + dy, 2, by_tag[tag]["tile_id"]); collision.add((gx + dx, gy + dy))

    dressing_tag = "palm_tree" if style == "coastal" else "bush"
    edge_spots = []
    for x in range(tx + 2, tx + tw - 2, 3):
        edge_spots.append((x, ty + 1)); edge_spots.append((x, ty + th - 2))
    for y in range(ty + 2, ty + th - 2, 3):
        edge_spots.append((tx + 1, y)); edge_spots.append((tx + tw - 2, y))
    occupied = collision | roads | {(x, y) for y in range(plaza["y"], plaza["y"] + plaza["h"]) for x in range(plaza["x"], plaza["x"] + plaza["w"])}
    for x, y in edge_spots:
        if (x, y) in occupied or not (tx <= x < tx + tw and ty <= y < ty + th):
            continue
        set_tile(x, y, 2, by_tag[dressing_tag]["tile_id"])
        collision.add((x, y))

    # Denser interior scatter (not just the boundary ring), per the Hamlin
    # finding: DQ2 town interiors carry trees/props scattered throughout the
    # walkable space, not concentrated only at the wall. Deterministic grid
    # offset by style so temperate/coastal don't scatter identically. A
    # clearance buffer around every door and the entry stem keeps this from
    # blocking access (Pass 2 first attempt did exactly that -- see report).
    clearance = set()
    for item in plan["transfer_points"] + plan["event_anchors"]:
        ax, ay = item["anchor"]["x"], item["anchor"]["y"]
        clearance |= {(ax + dx, ay + dy) for dx in (-1, 0, 1) for dy in (-2, -1, 0, 1)}
    clearance |= {(x, y) for y in range(gy - 1, gy + garden["h"] + 1) for x in range(gx - 1, gx + garden["w"] + 1)}
    occupied = collision | roads | plaza_cells | {(well["x"], well["y"])} | clearance
    offset = 0 if style == "temperate" else 1
    scatter_tag = "bush" if style == "temperate" else "palm_tree"
    for i, x in enumerate(range(tx + 1, tx + tw - 1)):
        for j, y in enumerate(range(ty + 1, ty + th - 1)):
            if (x, y) in occupied or not (tx <= x < tx + tw and ty <= y < ty + th):
                continue
            cell = (i + j + offset) % 9
            if cell == 0:
                set_tile(x, y, 2, by_tag["flower_patch"]["tile_id"])
            elif cell == 4:
                set_tile(x, y, 2, by_tag[scatter_tag]["tile_id"]); collision.add((x, y)); occupied.add((x, y))

    events = [None]
    semantic = plan["transfer_points"] + plan["event_anchors"]
    for item in semantic:
        identity = item.get("transfer_id") or item.get("local_anchor_id"); anchor = item["anchor"]
        comments = [{"code": 108, "indent": 0, "parameters": [f"WO-0065 semantic identity: {identity}; no unsupported destination/dialogue authored."]}]
        events.append({"id": len(events), "name": identity, "note": "WO-0065 semantic candidate anchor", "pages": [event_page(comments, trigger=0, priority=0)], "x": anchor["x"], "y": anchor["y"]})

    npc_spots = [(11, 10, 2), (18, 10, 6), (21, 11, 0), (9, 10, 4), (14, 15, 3)]
    for x, y, char_index in npc_spots:
        if (x, y) in collision or (x, y) not in roads:
            continue
        page = event_page(
            [{"code": 108, "indent": 0, "parameters": ["WO-0065 static villager presence; no dialogue authored, per constraint against inventing canon."]}],
            trigger=0, priority=1,
        )
        page["image"] = {"characterName": "People1", "characterIndex": char_index, "direction": 2, "pattern": 1, "tileId": 0}
        page["directionFix"] = True
        events.append({"id": len(events), "name": f"VILLAGER-{len(events)}", "note": "WO-0065 static NPC presence (no route, no dialogue)", "pages": [page], "x": x, "y": y})

    for x, y in sorted(collision):
        events.append({"id": len(events), "name": f"ADAPTER-COLLISION-{x}-{y}", "note": "Adapter building/landmark/boundary collision blocker",
                       "pages": [event_page([], trigger=0)], "x": x, "y": y})
    region_ids = {item["terrain_type"]: i + 1 for i, item in enumerate(plan["terrain"])}
    for item in plan["terrain"]:
        a = item["area"]
        for y in range(a["y"], a["y"] + a["h"]):
            for x in range(a["x"], a["x"] + a["w"]): set_tile(x, y, 5, region_ids[item["terrain_type"]])
    map_json = {"autoplayBgm": False, "autoplayBgs": False, "battleback1Name": "", "battleback2Name": "",
                "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90}, "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
                "disableDashing": False, "displayName": plan["title"], "encounterList": [], "encounterStep": 30, "height": height,
                "note": f"WO-0065 disposable settlement candidate; {palette['tile_palette_id']}", "parallaxLoopX": False, "parallaxLoopY": False,
                "parallaxName": "", "parallaxShow": True, "parallaxSx": 0, "parallaxSy": 0, "scrollType": 0, "specifyBattleback": False,
                "tilesetId": 2, "width": width, "data": data, "events": events}
    start = (15, 23); reached = bfs(width, height, start, collision)
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
    spec = importlib.util.spec_from_file_location("wo0065_renderer", RENDERER); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    module.GAME = str(GAME); module.render_map(str(map_path), str(GAME / "data/Tilesets.json"), str(output))


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
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
            records.append({"candidate_id": slug, "seed": seed, "style": style, "archetype": "ARCH-SETTLEMENT-VERTICAL-SLICE@0.2",
                            "layout_family": "LAY-SETTLEMENT-CIVIC-SPINE@0.2", "palette": palette["tile_palette_id"], "hard_passed": quality["hard_passed"],
                            "advisory_score": quality["advisory"]["score"], "render": str(render_path), "human_review": manifest["human_review"], "promotion": "not_applied"})
    gallery(records, OUTPUT / "settlement-gallery.png"); atomic_json(OUTPUT / "index.json", {"schema_version": "0.1", "candidate_count": len(records), "candidates": records})
    print(f"Generated {len(records)} WO-0065 settlement candidates")


def gallery(records: list[dict], path: Path) -> None:
    tw, th, lh = 360, 288, 80; image = Image.new("RGB", (tw * 3, (th + lh) * 2), (20, 23, 29)); draw = ImageDraw.Draw(image)
    for i, record in enumerate(records):
        source = Image.open(record["render"]).convert("RGB"); source.thumbnail((tw, th)); x, y = (i % 3) * tw, (i // 3) * (th + lh)
        image.paste(source, (x + (tw-source.width)//2, y)); draw.multiline_text((x+5,y+th+3), f"{record['candidate_id']}\n{record['archetype']}\n{record['layout_family']}\nHARD {'PASS' if record['hard_passed'] else 'FAIL'} | ADV {record['advisory_score']}", fill=(240,235,220))
    image.save(path)


if __name__ == "__main__": main()
