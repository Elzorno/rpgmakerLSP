#!/usr/bin/env python3
"""Clear passable upper-layer tiles above blocked base terrain."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from map_ownership_guard import load_ledger, map_write_allowed, skip_message


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    parser.add_argument("--report", default="", help="Optional Markdown report path.")
    parser.add_argument("--max-map-id", type=int, default=16, help="Highest generated Home Island map ID to clean.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def tile_index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def is_blocked_base(tile_id: int, flags: list[int]) -> bool:
    return 0 <= tile_id < len(flags) and (flags[tile_id] & 0x0F) == 0x0F


def clean_map(map_data: dict[str, Any], flags: list[int]) -> list[tuple[int, int, int, int]]:
    width = int(map_data["width"])
    height = int(map_data["height"])
    data = map_data["data"]
    cleared: list[tuple[int, int, int, int]] = []
    for y in range(height):
        for x in range(width):
            base = data[tile_index(width, height, x, y, 0)]
            if not is_blocked_base(base, flags):
                continue
            for z in range(1, 4):
                index = tile_index(width, height, x, y, z)
                value = data[index]
                if value:
                    data[index] = 0
                    cleared.append((x, y, z, value))
    return cleared


def build_report(project_root: Path, cleared_by_map: dict[str, list[tuple[int, int, int, int]]]) -> str:
    total = sum(len(values) for values in cleared_by_map.values())
    lines = [
        "# BUILD-0038 - Collision Passability Cleanup Report",
        "",
        "## Objective",
        "",
        "Remove passable upper-layer tiles from cells whose base terrain is blocked by the RPG Maker tileset flags.",
        "",
        "## Project",
        "",
        f"- Project root: `{project_root}`",
        "",
        "## Result",
        "",
        f"- Maps changed: {len(cleared_by_map)}",
        f"- Upper-layer tiles cleared: {total}",
        "",
        "## Cause",
        "",
        "Generated layouts could paint blocked base terrain, then leave a passable layer-1 terrain/path tile above it. RPG Maker MZ checks upper layers before the base layer, so those cells could become passable even though the layout intended them to block movement.",
        "",
        "## Maps Updated",
        "",
    ]
    for map_name, cleared in sorted(cleared_by_map.items()):
        lines.append(f"- `{map_name}`: {len(cleared)} upper-layer tile(s) cleared")
    lines.extend(["", "## Sample Cleared Tiles", ""])
    sample_count = 0
    for map_name, cleared in sorted(cleared_by_map.items()):
        for x, y, z, tile_id in cleared:
            lines.append(f"- `{map_name}` ({x}, {y}) layer {z}: cleared tile {tile_id}")
            sample_count += 1
            if sample_count >= 25:
                lines.append("- Additional cleared tiles omitted from sample list.")
                return "\n".join(lines) + "\n"
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    data_root = project_root / "data"
    tilesets = load_json(data_root / "Tilesets.json")
    flags_by_id = {
        int(row["id"]): row.get("flags", [])
        for row in tilesets
        if isinstance(row, dict) and row.get("id")
    }

    cleared_by_map: dict[str, list[tuple[int, int, int, int]]] = {}
    ledger = load_ledger(project_root)
    for map_id in range(1, args.max_map_id + 1):
        path = data_root / f"Map{map_id:03d}.json"
        if not map_write_allowed(ledger, map_id):
            print(skip_message(ledger, map_id, "apply_collision_passability_cleanup"))
            continue
        map_data = load_json(path)
        flags = flags_by_id.get(int(map_data["tilesetId"]), [])
        cleared = clean_map(map_data, flags)
        if cleared:
            write_json(path, map_data)
            cleared_by_map[path.name] = cleared

    report_path = Path(args.report).expanduser().resolve() if args.report else None
    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(build_report(project_root, cleared_by_map), encoding="utf-8")

    print(f"project_root={project_root}")
    print(f"maps_updated={len(cleared_by_map)}")
    print(f"upper_tiles_cleared={sum(len(values) for values in cleared_by_map.values())}")
    if report_path:
        print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
