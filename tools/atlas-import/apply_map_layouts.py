#!/usr/bin/env python3
"""Apply first-playable Home Island placeholder map layouts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

FLOOR = 2816
ALT_FLOOR = 2836
BLOCK = 1536
WATER = 2048
PATH = 3584
BLOCKING_BASE_TILES = {BLOCK, WATER}


EVENT_POSITIONS = {
    1: {
        "Child Near Old Panel": (7, 5),
        "Farmer With Warm Stones": (5, 7),
        "Skyreach Joker": (8, 3),
        "Dock Messenger": (10, 7),
        "Hidden Item": (8, 10),
        "Tremor Trigger": (8, 6),
        "TRN-HOM-002 Enter Elara House": (4, 5),
        "TRN-HOM-003 Enter Ashford Shop": (12, 5),
        "TRN-HOM-005 North path to Skyreach": (8, 0),
        "TRN-HOM-007 South/east route to Rustshore": (16, 9),
        "TRN-HOM-015 Route to Glassfield": (0, 9),
        "TRN-HOM-027 Optional east route to Fogfen Marsh Field": (16, 5),
    },
    2: {
        "Player Start": (8, 6),
        "Elara Intro Dialogue": (8, 4),
        "TRN-HOM-001 Elara House exit": (8, 12),
    },
    3: {
        "Shopkeeper": (8, 5),
        "TRN-HOM-004 Shop exit": (8, 12),
    },
    4: {
        "Skyreach Gate": (8, 3),
        "TRN-HOM-006 Return from Skyreach route": (8, 12),
        "TRN-HOM-009 Enter Hidden Cave": (8, 0),
    },
    5: {
        "Hidden Cave First Entry": (8, 9),
        "TRN-HOM-010 Exit cave": (8, 12),
        "TRN-HOM-011 Enter trials": (8, 0),
    },
    6: {
        "Body Trial": (4, 4),
        "Mind Trial": (8, 4),
        "Heart Trial": (12, 4),
        "Sanctum Gate": (8, 2),
        "TRN-HOM-012 Return to entrance": (8, 12),
        "TRN-HOM-013 Enter Sword Sanctum": (8, 0),
    },
    7: {
        "Sword Pedestal": (8, 5),
        "TRN-HOM-014 Return from sanctum": (8, 12),
    },
    8: {
        "Glassfield Seal": (8, 3),
        "Surface Fragment": (5, 7),
        "TRN-HOM-016 Return from Glassfield": (0, 10),
        "TRN-HOM-017 Enter Sealed Node": (8, 0),
    },
    9: {
        "Sealed Node First Entry": (8, 9),
        "TRN-HOM-018 Exit Sealed Node": (8, 12),
        "TRN-HOM-019 Proceed deeper": (8, 0),
    },
    10: {
        "Core Path Door": (8, 5),
        "TRN-HOM-020 Return to upper node": (8, 12),
        "TRN-HOM-021 Enter guardian chamber": (8, 0),
    },
    11: {
        "Node Seven Guardian": (8, 5),
        "TRN-HOM-022 Return to core path": (8, 12),
        "TRN-HOM-023 Enter relay core": (8, 0),
    },
    12: {
        "Relay Core": (8, 5),
        "TRN-HOM-024 Return from relay core": (8, 12),
    },
    13: {
        "Dockmaster": (8, 7),
        "Lighthouse Examine": (3, 4),
        "Boat Transfer": (13, 8),
        "TRN-HOM-008 Return from Rustshore route": (0, 9),
        "TRN-HOM-025 Begin departure": (14, 8),
    },
    14: {
        "Departure Sequence": (8, 6),
        "TRN-HOM-026 Destination TBD: Coalmouth or landing screen": (8, 0),
    },
    15: {
        "Fogfen Entry / Exit Transfer": (1, 10),
        "Hidden Item Landmark": (6, 8),
        "Signal-Tick Reed Pool": (10, 5),
        "TRN-HOM-028 Return from Fogfen to Ashford-side route": (0, 10),
        "TRN-HOM-029 Optional deeper marsh branch": (16, 4),
    },
    16: {
        "Deeper Marsh Return Transfer": (1, 10),
        "Signal Pool / Cable Cluster Examine": (10, 5),
        "TRN-HOM-030 Return from deeper marsh pocket": (0, 10),
    },
}


ENCOUNTERS = {
    4: [{"regionSet": [1], "troopId": 1, "weight": 5}, {"regionSet": [1], "troopId": 2, "weight": 4}, {"regionSet": [1], "troopId": 3, "weight": 3}],
    8: [{"regionSet": [1], "troopId": 1, "weight": 4}, {"regionSet": [1], "troopId": 3, "weight": 3}],
    9: [{"regionSet": [4], "troopId": 1, "weight": 3}, {"regionSet": [4], "troopId": 2, "weight": 2}],
    10: [{"regionSet": [4], "troopId": 1, "weight": 3}, {"regionSet": [4], "troopId": 2, "weight": 2}],
    15: [{"regionSet": [2], "troopId": 4, "weight": 5}, {"regionSet": [2], "troopId": 5, "weight": 4}],
    16: [{"regionSet": [2], "troopId": 4, "weight": 4}, {"regionSet": [2], "troopId": 5, "weight": 5}],
}

REGION_RECTS = {
    4: [(1, 2, 15, 9, 1), (7, 0, 9, 2, 5)],
    5: [(7, 1, 9, 11, 5)],
    6: [(1, 1, 15, 11, 5)],
    7: [(1, 1, 15, 11, 5)],
    8: [(1, 2, 15, 10, 1), (7, 0, 9, 3, 5)],
    9: [(2, 2, 14, 10, 4), (7, 9, 9, 12, 5)],
    10: [(2, 2, 14, 10, 4), (7, 4, 9, 6, 5)],
    11: [(1, 1, 15, 11, 5)],
    12: [(1, 1, 15, 11, 5)],
    14: [(1, 1, 15, 11, 5)],
    15: [(2, 2, 14, 10, 2), (5, 6, 8, 9, 3), (0, 9, 2, 11, 5), (15, 3, 16, 5, 5)],
    16: [(2, 2, 14, 10, 2), (6, 5, 12, 8, 3), (0, 9, 2, 11, 5)],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="Clean RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def set_tile(map_data: dict, x: int, y: int, z: int, value: int) -> None:
    if 0 <= x < map_data["width"] and 0 <= y < map_data["height"]:
        map_data["data"][index(map_data["width"], map_data["height"], x, y, z)] = value


def clear_upper_tiles_above_blocked_base(map_data: dict) -> int:
    cleared = 0
    width = map_data["width"]
    height = map_data["height"]
    for y in range(height):
        for x in range(width):
            if map_data["data"][index(width, height, x, y, 0)] not in BLOCKING_BASE_TILES:
                continue
            for z in range(1, 4):
                tile_index = index(width, height, x, y, z)
                if map_data["data"][tile_index]:
                    map_data["data"][tile_index] = 0
                    cleared += 1
    return cleared


def paint_rect(map_data: dict, x1: int, y1: int, x2: int, y2: int, z: int, value: int) -> None:
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            set_tile(map_data, x, y, z, value)


def paint_region(map_data: dict, x1: int, y1: int, x2: int, y2: int, region: int) -> None:
    paint_rect(map_data, x1, y1, x2, y2, 5, region)


def paint_border(map_data: dict, value: int) -> None:
    width = map_data["width"]
    height = map_data["height"]
    for x in range(width):
        set_tile(map_data, x, 0, 0, value)
        set_tile(map_data, x, height - 1, 0, value)
    for y in range(height):
        set_tile(map_data, 0, y, 0, value)
        set_tile(map_data, width - 1, y, 0, value)


def paint_path(map_data: dict, points: list[tuple[int, int]]) -> None:
    for x, y in points:
        set_tile(map_data, x, y, 1, PATH)


def all_points_between(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    x1, y1 = start
    x2, y2 = end
    points = []
    if x1 == x2:
        step = 1 if y2 >= y1 else -1
        for y in range(y1, y2 + step, step):
            points.append((x1, y))
    elif y1 == y2:
        step = 1 if x2 >= x1 else -1
        for x in range(x1, x2 + step, step):
            points.append((x, y1))
    return points


def reset_layout(map_data: dict) -> None:
    width = map_data["width"]
    height = map_data["height"]
    map_data["data"] = [0 for _ in range(width * height * 6)]
    paint_rect(map_data, 0, 0, width - 1, height - 1, 0, FLOOR)
    paint_border(map_data, BLOCK)


def terrain_pass(map_id: int, map_data: dict) -> None:
    if map_id in {1, 4, 8, 13, 15, 16}:
        paint_rect(map_data, 1, 1, map_data["width"] - 2, map_data["height"] - 2, 0, ALT_FLOOR)
    if map_id in {13, 15, 16}:
        paint_rect(map_data, 1, 1, 4, 3, 0, WATER)
    if map_id in {15, 16}:
        paint_rect(map_data, 11, 2, 15, 4, 0, WATER)
        paint_rect(map_data, 2, 8, 5, 10, 0, WATER)
    if map_id in {2, 3, 5, 6, 7, 9, 10, 11, 12, 14}:
        paint_rect(map_data, 2, 2, map_data["width"] - 3, map_data["height"] - 3, 0, FLOOR)


def path_pass(map_id: int, map_data: dict) -> None:
    points: list[tuple[int, int]] = []
    if map_id == 1:
        points += all_points_between((8, 0), (8, 11))
        points += all_points_between((0, 9), (16, 9))
        points += all_points_between((4, 5), (12, 5))
        points += all_points_between((8, 5), (16, 5))
    elif map_id in {4, 5, 9, 10, 11, 12, 14}:
        points += all_points_between((8, 0), (8, 12))
        points += all_points_between((4, 6), (12, 6))
    elif map_id == 6:
        points += all_points_between((8, 0), (8, 12))
        points += all_points_between((4, 4), (12, 4))
    elif map_id in {2, 3, 7}:
        points += all_points_between((8, 4), (8, 12))
        points += all_points_between((6, 6), (10, 6))
    elif map_id == 8:
        points += all_points_between((8, 0), (8, 10))
        points += all_points_between((0, 10), (12, 10))
        points += all_points_between((5, 7), (12, 7))
    elif map_id == 13:
        points += all_points_between((0, 9), (14, 9))
        points += all_points_between((8, 7), (14, 7))
        points += all_points_between((3, 4), (8, 4))
    elif map_id in {15, 16}:
        points += all_points_between((0, 10), (16, 10))
        points += all_points_between((10, 5), (16, 5))
        points += all_points_between((6, 8), (10, 8))
    paint_path(map_data, points)


def region_pass(map_id: int, map_data: dict) -> None:
    for x1, y1, x2, y2, region in REGION_RECTS.get(map_id, []):
        paint_region(map_data, x1, y1, x2, y2, region)


def apply_encounters(map_id: int, map_data: dict) -> None:
    map_data["encounterList"] = ENCOUNTERS.get(map_id, [])
    map_data["encounterStep"] = 35 if map_id in {4, 8, 9, 10} else 30
    if map_id == 16:
        map_data["encounterStep"] = 25


def move_events(map_id: int, map_data: dict) -> int:
    positions = EVENT_POSITIONS.get(map_id, {})
    moved = 0
    for event in map_data.get("events", []):
        if not isinstance(event, dict):
            continue
        position = positions.get(event.get("name", ""))
        if position and (event.get("x"), event.get("y")) != position:
            event["x"], event["y"] = position
            moved += 1
    return moved


def open_event_tiles(map_id: int, map_data: dict) -> None:
    for x, y in EVENT_POSITIONS.get(map_id, {}).values():
        set_tile(map_data, x, y, 0, FLOOR)
        set_tile(map_data, x, y, 1, PATH)


def apply_map(project_root: Path, map_id: int) -> tuple[bool, int]:
    path = project_root / "data" / f"Map{map_id:03d}.json"
    before = path.read_text(encoding="utf-8")
    map_data = json.loads(before)
    reset_layout(map_data)
    terrain_pass(map_id, map_data)
    path_pass(map_id, map_data)
    region_pass(map_id, map_data)
    open_event_tiles(map_id, map_data)
    clear_upper_tiles_above_blocked_base(map_data)
    apply_encounters(map_id, map_data)
    moved = move_events(map_id, map_data)
    note = str(map_data.get("note", ""))
    if "BUILD-0005 placeholder layout" not in note:
        map_data["note"] = f"{note} BUILD-0005 placeholder layout.".strip()
    after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        path.write_text(after, encoding="utf-8")
        return True, moved
    return False, moved


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    changed = 0
    moved = 0
    for map_id in range(1, 17):
        did_change, moved_count = apply_map(project_root, map_id)
        changed += 1 if did_change else 0
        moved += moved_count
    print(project_root)
    print(f"maps_updated={changed} events_moved={moved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
