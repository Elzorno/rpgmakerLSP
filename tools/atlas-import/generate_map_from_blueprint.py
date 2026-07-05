#!/usr/bin/env python3
"""Generate one RPG Maker MZ map from an Atlas map blueprint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ATLAS_ROOT = ROOT.parent / "TheLastSwordProtocol-Atlas"
DEFAULT_PROJECT_ROOT = ROOT.parent / "TheLastSwordProtocol-Game"
DEFAULT_BLUEPRINT = DEFAULT_ATLAS_ROOT / "atlas-tools" / "mapgen" / "prototype" / "SCR-HOM-ASH-001.blueprint.json"

FLOOR = 2816
ALT_FLOOR = 2836
BLOCK = 1536
PATH = 3584

SCREEN_TO_MAP_NAME = {
    "SCR-HOM-ASH-001": "TWN_Ashford_Exterior",
    "SCR-HOM-ASH-002": "INT_Ashford_ElaraHouse",
    "SCR-HOM-ASH-003": "INT_Ashford_Shop",
    "SCR-HOM-SKY-001": "DGN_SkyreachHill_Path",
    "SCR-HOM-HCV-001": "DGN_HiddenCave_Entrance",
    "SCR-HOM-HCV-002": "DGN_HiddenCave_Trials",
    "SCR-HOM-HCV-003": "DGN_HiddenCave_Sanctum",
    "SCR-HOM-GLS-001": "DGN_Glassfield_Ruins_Exterior",
    "SCR-HOM-SND-001": "DGN_SealedNode_Upper",
    "SCR-HOM-SND-002": "DGN_SealedNode_CorePath",
    "SCR-HOM-SND-003": "DGN_SealedNode_Guardian",
    "SCR-HOM-SND-004": "DGN_SealedNode_RelayCore",
    "SCR-HOM-RST-001": "TWN_Rustshore_Docks",
    "SCR-HOM-RST-002": "CUT_Mainland_Departure",
    "SCR-HOM-FOG-001": "FLD_Fogfen_Marsh_Field",
    "SCR-HOM-FOG-002": "FLD_Fogfen_Deeper_Marsh_Pocket",
}

TRANSFER_EVENT_NAMES = {
    "TRN-HOM-001": "TRN-HOM-001 Elara House exit",
    "TRN-HOM-002": "TRN-HOM-002 Enter Elara House",
    "TRN-HOM-003": "TRN-HOM-003 Enter Ashford Shop",
    "TRN-HOM-004": "TRN-HOM-004 Shop exit",
    "TRN-HOM-005": "TRN-HOM-005 North path to Skyreach",
    "TRN-HOM-007": "TRN-HOM-007 South/east route to Rustshore",
    "TRN-HOM-015": "TRN-HOM-015 Route to Glassfield",
    "TRN-HOM-027": "TRN-HOM-027 Optional east route to Fogfen Marsh Field",
    "TRN-HOM-006": "TRN-HOM-006 Return from Skyreach route",
    "TRN-HOM-008": "TRN-HOM-008 Return from Rustshore route",
    "TRN-HOM-009": "TRN-HOM-009 Enter Hidden Cave",
    "TRN-HOM-010": "TRN-HOM-010 Exit cave",
    "TRN-HOM-011": "TRN-HOM-011 Enter trials",
    "TRN-HOM-012": "TRN-HOM-012 Return to entrance",
    "TRN-HOM-013": "TRN-HOM-013 Enter Sword Sanctum",
    "TRN-HOM-014": "TRN-HOM-014 Return from sanctum",
    "TRN-HOM-016": "TRN-HOM-016 Return from Glassfield",
    "TRN-HOM-017": "TRN-HOM-017 Enter Sealed Node",
    "TRN-HOM-018": "TRN-HOM-018 Exit Sealed Node",
    "TRN-HOM-019": "TRN-HOM-019 Proceed deeper",
    "TRN-HOM-020": "TRN-HOM-020 Return to upper node",
    "TRN-HOM-021": "TRN-HOM-021 Enter guardian chamber",
    "TRN-HOM-022": "TRN-HOM-022 Return to core path",
    "TRN-HOM-023": "TRN-HOM-023 Enter relay core",
    "TRN-HOM-024": "TRN-HOM-024 Return from relay core",
    "TRN-HOM-025": "TRN-HOM-025 Begin departure",
    "TRN-HOM-026": "TRN-HOM-026 Destination TBD: Coalmouth or landing screen",
    "TRN-HOM-028": "TRN-HOM-028 Return from Fogfen to Ashford-side route",
    "TRN-HOM-029": "TRN-HOM-029 Optional deeper marsh branch",
    "TRN-HOM-030": "TRN-HOM-030 Return from deeper marsh pocket",
}

NPC_EVENT_NAMES = {
    "EVT-HOM-003": "Child Near Old Panel",
    "EVT-HOM-004": "Farmer With Warm Stones",
    "EVT-HOM-005": "Skyreach Joker",
    "EVT-HOM-006": "Dock Messenger",
    "NPC-ASH-ELD-PLACEHOLDER": "Village Elder Placeholder",
}

TREASURE_EVENT_NAMES = {
    "EVT-HOM-007": "Hidden Item",
}

ANCHOR_EVENT_NAMES = {
    "EVT-HOM-001": "Player Start",
    "EVT-HOM-002": "Elara Intro Dialogue",
    "EVT-HOM-008": "Shopkeeper",
    "EVT-HOM-009": "Tremor Trigger",
    "EVT-HOM-010": "Skyreach Gate",
    "EVT-HOM-011": "Hidden Cave First Entry",
    "EVT-HOM-012": "Body Trial",
    "EVT-HOM-012A": "EVT-HOM-012A Body Trial Reset 1",
    "EVT-HOM-012B": "EVT-HOM-012B Body Trial Reset 2",
    "EVT-HOM-012C": "EVT-HOM-012C Body Trial Reset 3",
    "EVT-HOM-013": "Mind Trial",
    "EVT-HOM-013A": "EVT-HOM-013A Mind Marker Left",
    "EVT-HOM-013B": "EVT-HOM-013B Mind Marker Right",
    "EVT-HOM-013C": "EVT-HOM-013C Mind Marker Center",
    "EVT-HOM-014": "Heart Trial",
    "EVT-HOM-015": "Sanctum Gate",
    "EVT-HOM-016": "Sword Pedestal",
    "EVT-HOM-017": "Glassfield Seal",
    "EVT-HOM-018": "Surface Fragment",
    "EVT-HOM-019": "Sealed Node First Entry",
    "EVT-HOM-020": "Core Path Door",
    "EVT-HOM-021": "Node Seven Guardian",
    "EVT-HOM-022": "Relay Core",
    "EVT-HOM-023": "Dockmaster",
    "EVT-HOM-024": "Lighthouse Examine",
    "EVT-HOM-025": "Boat Transfer",
    "EVT-HOM-026": "Departure Sequence",
    "EVT-HOM-027": "Fogfen Entry / Exit Transfer",
    "EVT-HOM-029": "Signal-Tick Reed Pool",
    "EVT-HOM-030": "Deeper Marsh Return Transfer",
    "EVT-HOM-031": "Signal Pool / Cable Cluster Examine",
    "INT-ASH-WARM-STONE-VENT": "INT-ASH-WARM-STONE-VENT Warm-Stone Vent",
    "INT-ASH-OLD-PANEL": "INT-ASH-OLD-PANEL Old Panel",
    "INT-ASH-ELARA-KEEPSAKE": "INT-ASH-ELARA-KEEPSAKE Keepsake Shelf",
    "INT-ASH-SHOP-CABINET": "INT-ASH-SHOP-CABINET Metal Cabinet",
    "INT-SKY-GEOMETRIC-STONES": "INT-SKY-GEOMETRIC-STONES Geometric Stones",
    "INT-HCV-WALL-CARVING": "INT-HCV-WALL-CARVING Wall Carving",
}
TREASURE_EVENT_NAMES["EVT-HOM-028"] = "Hidden Item Landmark"
TREASURE_EVENT_NAMES["OBJ-HOM-FOG-009"] = "Deeper Marsh Reward Cache"

ENCOUNTER_POLICIES = {
    "SCR-HOM-ASH-001": [],
    "SCR-HOM-ASH-002": [],
    "SCR-HOM-ASH-003": [],
    "SCR-HOM-SKY-001": [
        {"regionSet": [1], "troopId": 1, "weight": 5},
        {"regionSet": [1], "troopId": 2, "weight": 4},
        {"regionSet": [1], "troopId": 3, "weight": 3},
    ],
    "SCR-HOM-HCV-001": [],
    "SCR-HOM-HCV-002": [],
    "SCR-HOM-HCV-003": [],
    "SCR-HOM-GLS-001": [
        {"regionSet": [1], "troopId": 1, "weight": 4},
        {"regionSet": [1], "troopId": 3, "weight": 3},
    ],
    "SCR-HOM-SND-001": [
        {"regionSet": [4], "troopId": 1, "weight": 3},
        {"regionSet": [4], "troopId": 2, "weight": 2},
    ],
    "SCR-HOM-SND-002": [
        {"regionSet": [4], "troopId": 1, "weight": 3},
        {"regionSet": [4], "troopId": 2, "weight": 2},
    ],
    "SCR-HOM-SND-003": [],
    "SCR-HOM-SND-004": [],
    "SCR-HOM-RST-001": [],
    "SCR-HOM-RST-002": [],
    "SCR-HOM-FOG-001": [
        {"regionSet": [2], "troopId": 4, "weight": 5},
        {"regionSet": [2], "troopId": 5, "weight": 4},
    ],
    "SCR-HOM-FOG-002": [
        {"regionSet": [2], "troopId": 4, "weight": 4},
        {"regionSet": [2], "troopId": 5, "weight": 5},
    ],
}

REGION_EXPORT_IDS = {
    "encounter": 1,
    "marsh_encounter": 2,
    "slow_bog": 3,
    "node_encounter": 4,
    "safe": 5,
}


def should_export_safe_regions(blueprint: dict[str, Any]) -> bool:
    return blueprint.get("atlas_screen_id") != "SCR-HOM-ASH-001"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT), help="Atlas blueprint JSON path.")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT), help="RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def tile_index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def set_tile(map_data: dict[str, Any], x: int, y: int, z: int, value: int) -> None:
    if 0 <= x < map_data["width"] and 0 <= y < map_data["height"]:
        map_data["data"][tile_index(map_data["width"], map_data["height"], x, y, z)] = value


def paint_rect(map_data: dict[str, Any], x: int, y: int, w: int, h: int, z: int, value: int) -> None:
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            set_tile(map_data, xx, yy, z, value)


def paint_border(map_data: dict[str, Any]) -> None:
    width = map_data["width"]
    height = map_data["height"]
    for x in range(width):
        set_tile(map_data, x, 0, 0, BLOCK)
        set_tile(map_data, x, height - 1, 0, BLOCK)
    for y in range(height):
        set_tile(map_data, 0, y, 0, BLOCK)
        set_tile(map_data, width - 1, y, 0, BLOCK)


def line_points(start: list[int], end: list[int]) -> list[tuple[int, int]]:
    x1, y1 = start
    x2, y2 = end
    points: list[tuple[int, int]] = []
    if x1 == x2:
        step = 1 if y2 >= y1 else -1
        points.extend((x1, y) for y in range(y1, y2 + step, step))
    elif y1 == y2:
        step = 1 if x2 >= x1 else -1
        points.extend((x, y1) for x in range(x1, x2 + step, step))
    else:
        # Manhattan fallback keeps generated paths tile-friendly and deterministic.
        points.extend(line_points([x1, y1], [x1, y2]))
        points.extend(line_points([x1, y2], [x2, y2]))
    return points


def anchor_point(anchor: dict[str, Any]) -> tuple[int, int]:
    if anchor["shape"] == "point":
        return int(anchor["x"]), int(anchor["y"])
    if anchor["shape"] == "rect":
        return int(anchor["x"] + anchor["w"] // 2), int(anchor["y"] + anchor["h"] // 2)
    raise ValueError(f"Unsupported anchor shape: {anchor['shape']}")


def paint_blueprint_layout(map_data: dict[str, Any], blueprint: dict[str, Any]) -> None:
    width = int(blueprint["dimensions"]["width"])
    height = int(blueprint["dimensions"]["height"])
    map_data["width"] = width
    map_data["height"] = height
    map_data["data"] = [0 for _ in range(width * height * 6)]
    paint_rect(map_data, 0, 0, width, height, 0, FLOOR)
    paint_rect(map_data, 2, 3, width - 4, height - 6, 0, ALT_FLOOR)
    paint_border(map_data)

    for terrain in blueprint.get("terrain", []):
        area = terrain.get("area", {})
        terrain_type = terrain.get("terrain_type")
        if area.get("shape") == "rect":
            value = PATH if terrain_type in {
                "village_path",
                "village_ground",
                "hill_path",
                "sacred_stone_path",
                "cave_passage",
                "carved_stone_threshold",
                "trial_path",
                "trial_chamber",
                "sanctum_threshold",
                "body_trial_lane",
                "mind_trial_floor",
                "heart_trial_floor",
                "sanctum_floor",
                "sanctum_dais",
                "geometric_floor",
                "ruin_path",
                "glassfield_ground",
                "cracked_glass_panel",
                "sealed_threshold",
                "node_corridor",
                "cave_machine_floor",
                "unstable_light_path",
                "coastal_path",
                "dock_planks",
                "shoreline_ground",
                "lighthouse_base",
                "boat_landing",
                "cutscene_dock",
                "departure_boat_path",
                "marsh_path",
                "marsh_ground",
                "shallow_bog",
                "reed_floor",
                "signal_pool",
                "cable_landmark",
                "interior_floor",
                "cozy_home_floor",
                "hearth_area",
                "keepsake_corner",
                "shop_floor",
                "counter_area",
                "shelf_area",
                "cabinet_corner",
            } else ALT_FLOOR
            paint_rect(map_data, int(area["x"]), int(area["y"]), int(area["w"]), int(area["h"]), 1, value)
        elif area.get("shape") == "polyline":
            points = area.get("points", [])
            for start, end in zip(points, points[1:]):
                for x, y in line_points(start, end):
                    set_tile(map_data, x, y, 1, PATH)

    for obstacle in blueprint.get("obstacles", []):
        if not obstacle.get("blocking"):
            continue
        area = obstacle["area"]
        if area["shape"] == "rect":
            paint_rect(map_data, int(area["x"]), int(area["y"]), int(area["w"]), int(area["h"]), 0, BLOCK)
        elif area["shape"] == "point":
            x, y = anchor_point(area)
            set_tile(map_data, x, y, 0, BLOCK)


def paint_blueprint_regions(map_data: dict[str, Any], blueprint: dict[str, Any]) -> None:
    has_encounter_region = any(
        region.get("region_type") in REGION_EXPORT_IDS and region.get("region_type") != "safe"
        for region in blueprint.get("enemy_regions", [])
    )
    for region in blueprint.get("enemy_regions", []):
        region_type = region.get("region_type")
        if region_type == "safe" and not has_encounter_region and not should_export_safe_regions(blueprint):
            continue
        value = REGION_EXPORT_IDS.get(region_type)
        area = region.get("area", {})
        if value is None or area.get("shape") != "rect":
            continue
        paint_rect(map_data, int(area["x"]), int(area["y"]), int(area["w"]), int(area["h"]), 5, value)


def open_anchor_tile(map_data: dict[str, Any], x: int, y: int) -> None:
    set_tile(map_data, x, y, 0, ALT_FLOOR)
    set_tile(map_data, x, y, 1, PATH)


def blank_page(comment: str) -> dict[str, Any]:
    return {
        "conditions": {
            "actorId": 1,
            "actorValid": False,
            "itemId": 1,
            "itemValid": False,
            "selfSwitchCh": "A",
            "selfSwitchValid": False,
            "switch1Id": 1,
            "switch1Valid": False,
            "switch2Id": 1,
            "switch2Valid": False,
            "variableId": 1,
            "variableValid": False,
            "variableValue": 0,
        },
        "directionFix": False,
        "image": {"characterIndex": 0, "characterName": "", "direction": 2, "pattern": 1, "tileId": 0},
        "list": [
            {"code": 108, "indent": 0, "parameters": [comment]},
            {"code": 0, "indent": 0, "parameters": []},
        ],
        "moveFrequency": 3,
        "moveRoute": {"list": [{"code": 0, "indent": 0, "parameters": []}], "repeat": True, "skippable": False, "wait": False},
        "moveSpeed": 3,
        "moveType": 0,
        "priorityType": 1,
        "stepAnime": False,
        "through": False,
        "trigger": 0,
        "walkAnime": True,
    }


def make_event(event_id: int, name: str, x: int, y: int, atlas_note: str) -> dict[str, Any]:
    return {
        "id": event_id,
        "name": name,
        "note": atlas_note,
        "pages": [blank_page(f"Atlas placeholder {atlas_note}: {name}")],
        "x": x,
        "y": y,
    }


def ensure_event_comment(event: dict[str, Any], text: str) -> None:
    pages = event.get("pages", [])
    if not pages:
        return
    commands = pages[0].setdefault("list", [])
    for command in commands:
        if command.get("code") in {108, 408} and command.get("parameters") == [text]:
            return
    commands.insert(0, {"code": 108, "indent": 0, "parameters": [text]})


def upsert_event(
    map_data: dict[str, Any],
    name: str,
    x: int,
    y: int,
    atlas_note: str,
    created: list[str],
    updated: list[str],
) -> None:
    events = map_data.setdefault("events", [])
    by_name = {event.get("name"): event for event in events if isinstance(event, dict)}
    event = by_name.get(name)
    if event:
        event["x"] = x
        event["y"] = y
        note = str(event.get("note", ""))
        if atlas_note not in note:
            event["note"] = f"{note} {atlas_note}".strip()
        ensure_event_comment(event, f"Atlas blueprint anchor {atlas_note}")
        updated.append(name)
        return

    next_id = max((event.get("id", 0) for event in events if isinstance(event, dict)), default=0) + 1
    events.append(make_event(next_id, name, x, y, atlas_note))
    created.append(name)


def apply_blueprint_events(map_data: dict[str, Any], blueprint: dict[str, Any]) -> tuple[list[str], list[str]]:
    created: list[str] = []
    updated: list[str] = []

    for transfer in blueprint.get("transfer_points", []):
        transfer_id = transfer["transfer_id"]
        name = TRANSFER_EVENT_NAMES.get(transfer_id, transfer_id)
        x, y = anchor_point(transfer["anchor"])
        open_anchor_tile(map_data, x, y)
        upsert_event(map_data, name, x, y, transfer_id, created, updated)

    for npc in blueprint.get("npc_spawns", []):
        atlas_id = npc.get("event_id") or npc.get("local_anchor_id")
        name = NPC_EVENT_NAMES.get(atlas_id, npc["npc_role"])
        x, y = anchor_point(npc["anchor"])
        open_anchor_tile(map_data, x, y)
        upsert_event(map_data, name, x, y, atlas_id, created, updated)

    for treasure in blueprint.get("treasure_locations", []):
        atlas_id = treasure["event_id"]
        name = TREASURE_EVENT_NAMES.get(atlas_id, atlas_id)
        x, y = anchor_point(treasure["anchor"])
        open_anchor_tile(map_data, x, y)
        upsert_event(map_data, name, x, y, atlas_id, created, updated)

    for anchor in blueprint.get("event_anchors", []):
        atlas_id = anchor.get("event_id") or anchor.get("local_anchor_id")
        name = ANCHOR_EVENT_NAMES.get(atlas_id, anchor.get("event_name", atlas_id))
        x, y = anchor_point(anchor["anchor"])
        open_anchor_tile(map_data, x, y)
        upsert_event(map_data, name, x, y, atlas_id, created, updated)

    return created, updated


def find_target_map_id(project_root: Path, blueprint: dict[str, Any]) -> int:
    map_name = SCREEN_TO_MAP_NAME.get(blueprint["atlas_screen_id"])
    if not map_name:
        raise ValueError(f"No RPG Maker map-name mapping for {blueprint['atlas_screen_id']}")
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    matches = [entry["id"] for entry in map_infos if isinstance(entry, dict) and entry.get("name") == map_name]
    if len(matches) != 1:
        raise ValueError(f"Expected one MapInfos entry named {map_name}, found {matches}")
    return int(matches[0])


def main() -> int:
    args = parse_args()
    blueprint_path = Path(args.blueprint).expanduser().resolve()
    project_root = Path(args.project_root).expanduser().resolve()
    blueprint = load_json(blueprint_path)
    if blueprint.get("atlas_screen_id") not in SCREEN_TO_MAP_NAME:
        raise ValueError(f"No supported map generation mapping for {blueprint.get('atlas_screen_id')}.")

    map_id = find_target_map_id(project_root, blueprint)
    map_path = project_root / "data" / f"Map{map_id:03d}.json"
    map_data = load_json(map_path)
    before = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))

    paint_blueprint_layout(map_data, blueprint)
    paint_blueprint_regions(map_data, blueprint)
    created, updated = apply_blueprint_events(map_data, blueprint)
    map_data["encounterList"] = ENCOUNTER_POLICIES.get(blueprint["atlas_screen_id"], [])
    map_data["encounterStep"] = 35 if map_data["encounterList"] else 30
    map_data["displayName"] = blueprint["title"]
    note = str(map_data.get("note", ""))
    marker = f"Generated from {blueprint['blueprint_id']}."
    if marker not in note:
        map_data["note"] = f"{note} {marker}".strip()

    after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        write_json(map_path, map_data)

    print(f"blueprint={blueprint_path}")
    print(f"map={map_path}")
    print(f"map_id={map_id}")
    print(f"events_created={len(created)}")
    for name in created:
        print(f"created={name}")
    print(f"events_updated={len(updated)}")
    for name in updated:
        print(f"updated={name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
