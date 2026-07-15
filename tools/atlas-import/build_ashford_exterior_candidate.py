#!/usr/bin/env python3
"""Build a review-only Ashford Exterior v2 candidate from canonical Map001 events."""

from __future__ import annotations

import copy
import importlib.util
import json
import shutil
from collections import deque
from pathlib import Path

from autotile import paint_region


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
SOURCE = GAME / "data/Map001.json"
OUTPUT = REPO / "reports/atlas-import/ashford-exterior-rebuild-v2"
RENDERER = WORKSPACE / "AtlasStudio/atlas-tools/mapgen/compiler/style_study/wo0060/render_map.py"
WIDTH, HEIGHT = 40, 32


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    temp.replace(path)


def building(data: list[int], collision: set[tuple[int, int]], x0: int, y0: int, width: int, door_x: int, sign: int | None = None) -> None:
    def put(x: int, y: int, layer: int, tile: int) -> None:
        data[(layer * HEIGHT + y) * WIDTH + x] = tile
    for x in range(x0, x0 + width):
        put(x, y0, 2, 13 if x == x0 else 15 if x == x0 + width - 1 else 14)
    for y in range(y0 + 1, y0 + 5):
        for x in range(x0, x0 + width):
            put(x, y, 1, 82 if x == x0 else 84 if x == x0 + width - 1 else 83)
            collision.add((x, y))
    put(door_x, y0 + 4, 2, 114)
    put(x0 + 1, y0 + 4, 2, 96)
    put(x0 + width - 2, y0 + 4, 2, 96)
    if sign is not None:
        put(door_x, y0 + 2, 3, sign)


def build() -> tuple[dict, dict]:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    candidate = copy.deepcopy(source)
    data = [0] * (WIDTH * HEIGHT * 6)
    def put(x: int, y: int, layer: int, tile: int) -> None:
        data[(layer * HEIGHT + y) * WIDTH + x] = tile

    paint_region(put, {(x, y) for y in range(HEIGHT) for x in range(WIDTH)}, 16, 0)

    # Curving south-to-square civic spine and explicit branches to every route.
    road = set()
    def box(x0: int, y0: int, x1: int, y1: int) -> None:
        road.update((x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1))
    box(17, 27, 20, 31); box(17, 23, 22, 28); box(19, 17, 24, 24)
    box(17, 12, 22, 19); box(18, 0, 21, 13)
    box(13, 12, 34, 15); box(22, 8, 39, 11); box(23, 21, 39, 24)
    box(7, 13, 19, 16); box(13, 25, 20, 28)
    paint_region(put, road, 32, 0)

    plaza = {(x, y) for y in range(15, 22) for x in range(17, 28)}
    plaza -= {(17, 15), (27, 15), (17, 21), (27, 21)}
    paint_region(put, plaza, 26, 0)

    collision: set[tuple[int, int]] = set()
    # Inn, Shop, Elara House; two smaller cottage shells add residential depth.
    building(data, collision, 10, 6, 8, 14, 70)
    building(data, collision, 28, 11, 7, 31, 66)
    building(data, collision, 13, 22, 8, 17, None)
    building(data, collision, 3, 4, 6, 6, None)
    building(data, collision, 3, 23, 5, 5, None)

    # Partial valley/forest boundary, deliberately open at all canonical exits.
    openings = {(x, y) for x in range(18, 22) for y in (0, 1)}
    openings |= {(x, y) for x in range(16, 21) for y in (30, 31)}
    openings |= {(x, y) for x in (38, 39) for y in range(7, 12)}
    openings |= {(x, y) for x in (38, 39) for y in range(21, 25)}
    boundary = {(x, y) for x in range(WIDTH) for y in (0, 1, 30, 31)} | {(x, y) for x in (0, 1, 38, 39) for y in range(HEIGHT)}
    for x, y in sorted(boundary - openings):
        put(x, y, 2, 165); collision.add((x, y))

    # Old-facility drainage channel with clear route crossings.
    drain = {(36, y) for y in range(2, 30)} | {(37, y) for y in range(2, 30)}
    drain -= {(x, y) for x in (36, 37) for y in range(8, 12)}
    drain -= {(x, y) for x in (36, 37) for y in range(21, 25)}
    paint_region(put, drain, 0, 0); collision |= drain

    # Well, garden/farm, orchard, shop supplies, repair shed texture, factory ribs.
    put(24, 18, 2, 139); collision.add((24, 18))
    for x in range(4, 12):
        put(x, 17, 2, 165 if x in (4, 11) else 160)
    for x, y, tile in [
        (5, 18, 160), (7, 18, 160), (9, 18, 160), (11, 18, 160),
        (4, 20, 178), (7, 20, 178), (10, 20, 178),
        (27, 16, 141), (28, 16, 179), (29, 16, 140),
        (34, 17, 141), (35, 17, 140),
        (30, 4, 176), (31, 4, 177), (30, 5, 184), (31, 5, 185),
        (6, 12, 160), (8, 12, 160), (3, 14, 165), (11, 4, 165),
        (25, 5, 165), (34, 6, 165), (4, 28, 165), (9, 27, 165),
    ]:
        put(x, y, 2, tile)
        if tile not in (160,): collision.add((x, y))

    # Reposition canonical anchors around the reconciled geometry; pages/lists remain byte-equivalent objects.
    positions = {
        1: (7, 12), 2: (10, 18), 3: (22, 5), 4: (21, 28), 5: (9, 20),
        6: (20, 9), 7: (17, 26), 8: (31, 15), 9: (20, 0), 10: (18, 31),
        11: (39, 9), 12: (39, 23), 13: (25, 17), 14: (9, 16), 15: (7, 11),
        16: (15, 22), 17: (30, 11), 18: (8, 16), 19: (5, 16), 20: (22, 18),
        21: (9, 18), 22: (20, 2), 23: (14, 10), 24: (19, 27), 25: (29, 16),
        26: (11, 19), 27: (25, 20),
    }
    for event in candidate["events"]:
        if event and event["id"] in positions:
            event["x"], event["y"] = positions[event["id"]]

    candidate["data"] = data
    candidate["note"] = "Review candidate only: SCR-HOM-ASH-001 v0.2 / IMP-HOM-017 v0.2 reconciled rebuild; production Map001 not overwritten."
    candidate["events"] = candidate["events"]

    # Conservative collision audit from authored footprints/boundaries/water.
    start = (18, 30)
    seen, queue = {start}, deque([start])
    while queue:
        x, y = queue.popleft()
        for point in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= point[0] < WIDTH and 0 <= point[1] < HEIGHT and point not in collision and point not in seen:
                seen.add(point); queue.append(point)
    failures = []
    for event in candidate["events"]:
        if not event: continue
        point = (event["x"], event["y"])
        ring = {(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)}
        if point not in seen and not ring & seen:
            failures.append({"id": event["id"], "name": event["name"], "position": list(point)})
    audit = {"result": "pass" if not failures else "fail", "origin": list(start), "reachable_cells": len(seen), "event_failures": failures,
             "source_event_count": len([e for e in source["events"] if e]), "candidate_event_count": len([e for e in candidate["events"] if e]),
             "event_command_payloads_preserved": all(source["events"][i]["pages"] == candidate["events"][i]["pages"] for i in range(1, len(source["events"]))) }
    return candidate, audit


def render(map_path: Path, output: Path) -> None:
    spec = importlib.util.spec_from_file_location("ashford_renderer", RENDERER)
    module = importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(module)
    module.GAME = str(GAME); module.render_map(str(map_path), str(GAME / "data/Tilesets.json"), str(output))


def main() -> None:
    if OUTPUT.exists(): shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    candidate, audit = build()
    map_path = OUTPUT / "Map001.reconciled-candidate.json"
    atomic_json(map_path, candidate); atomic_json(OUTPUT / "route-audit.json", audit)
    render(map_path, OUTPUT / "ashford-exterior-reconciled-render.png")
    if audit["result"] != "pass": raise SystemExit(f"route audit failed: {audit['event_failures']}")
    print(f"candidate={map_path}\nroute_audit=pass reachable={audit['reachable_cells']}")


if __name__ == "__main__":
    main()
