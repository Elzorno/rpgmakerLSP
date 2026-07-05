#!/usr/bin/env python3
"""Read-only audit of Atlas Home Island transfers against RPG Maker maps."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-exports" / "home-island.json"
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "build-0027-all-map-route-audit.md"

FOUND = "found"
MISSING = "missing"
WARNING = "present with warning"

EXTERNAL_TRANSFER_TARGETS = {
    "Journey II start": "JRN2_Landing_Placeholder",
}


@dataclass(frozen=True)
class Finding:
    category: str
    check_id: str
    expected: str
    status: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", default=str(DEFAULT_EXPORT), help="Path to atlas-exports/home-island.json.")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    parser.add_argument(
        "output",
        nargs="?",
        default=str(DEFAULT_OUTPUT),
        help="Markdown report path.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Required JSON file not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {path}: {error}")


def iter_events(map_data: dict[str, Any]):
    for event in map_data.get("events", []):
        if isinstance(event, dict):
            yield event


def iter_commands(event: dict[str, Any]):
    for page_index, page in enumerate(event.get("pages", []), 1):
        for command in page.get("list", []):
            if isinstance(command, dict):
                yield page_index, command


def command_text(command: dict[str, Any]) -> str:
    return " ".join(str(value) for value in command.get("parameters", []))


def event_contains(event: dict[str, Any], atlas_id: str) -> bool:
    if atlas_id in str(event.get("name", "")) or atlas_id in str(event.get("note", "")):
        return True
    for _, command in iter_commands(event):
        if command.get("code") in {108, 408} and atlas_id in command_text(command):
            return True
    return False


def rows_by_name(rows: list[Any]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if isinstance(row, dict) and row.get("name"):
            index[str(row["name"]).strip().lower()].append(row)
    return index


def map_info_by_screen(export: dict[str, Any], map_infos: list[Any]) -> dict[str, dict[str, Any]]:
    by_name = rows_by_name(map_infos)
    result: dict[str, dict[str, Any]] = {}
    for screen in export["home_island"]["screens"]:
        matches = by_name.get(str(screen["rpg_maker_map_name"]).strip().lower(), [])
        if matches:
            result[screen["screen_id"]] = matches[0]
    return result


def screen_by_map_id(screen_maps: dict[str, dict[str, Any]]) -> dict[int, str]:
    return {int(row["id"]): screen_id for screen_id, row in screen_maps.items()}


def load_project_maps(project_root: Path, map_infos: list[Any]) -> dict[int, dict[str, Any]]:
    maps: dict[int, dict[str, Any]] = {}
    for row in map_infos:
        if not isinstance(row, dict) or not row.get("id"):
            continue
        map_id = int(row["id"])
        path = project_root / "data" / f"Map{map_id:03d}.json"
        if path.exists():
            maps[map_id] = load_json(path)
    return maps


def tile_index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def tile_value(map_data: dict[str, Any], x: int, y: int, z: int) -> int | None:
    if not (0 <= x < map_data["width"] and 0 <= y < map_data["height"]):
        return None
    index = tile_index(map_data["width"], map_data["height"], x, y, z)
    data = map_data.get("data", [])
    if index >= len(data):
        return None
    return data[index]


def find_transfer_event(map_data: dict[str, Any], transfer_id: str) -> dict[str, Any] | None:
    for event in iter_events(map_data):
        if event_contains(event, transfer_id):
            return event
    return None


def transfer_commands(event: dict[str, Any]) -> list[tuple[int, list[Any]]]:
    result = []
    for page_index, command in iter_commands(event):
        if command.get("code") == 201:
            result.append((page_index, command.get("parameters", [])))
    return result


def target_map_for_transfer(
    transfer: dict[str, Any],
    screen_maps: dict[str, dict[str, Any]],
    map_infos_by_name: dict[str, list[dict[str, Any]]],
) -> tuple[int | None, str]:
    target = transfer["to"]
    if target in screen_maps:
        return int(screen_maps[target]["id"]), target
    external_name = EXTERNAL_TRANSFER_TARGETS.get(target)
    if external_name:
        matches = map_infos_by_name.get(external_name.lower(), [])
        if matches:
            return int(matches[0]["id"]), target
    return None, target


def add_finding(findings: list[Finding], category: str, check_id: str, expected: str, ok: bool, detail: str, warning: bool = False) -> None:
    status = FOUND if ok else (WARNING if warning else MISSING)
    findings.append(Finding(category, check_id, expected, status, detail if ok else f"Expected {detail}"))


def audit_transfer_rows(
    export: dict[str, Any],
    project_root: Path,
    map_infos: list[Any],
    maps: dict[int, dict[str, Any]],
    screen_maps: dict[str, dict[str, Any]],
) -> tuple[list[Finding], dict[str, set[str]]]:
    findings: list[Finding] = []
    graph: dict[str, set[str]] = defaultdict(set)
    by_name = rows_by_name(map_infos)

    for transfer in export["home_island"]["transfers"]:
        transfer_id = transfer["transfer_id"]
        source = transfer["from"]
        target = transfer["to"]
        source_info = screen_maps.get(source)
        add_finding(findings, "Transfer Source", f"{transfer_id}-SRC", f"{source} has RPG Maker map", source_info is not None, f"source map for {source}")
        if not source_info:
            continue
        source_map_id = int(source_info["id"])
        source_map = maps.get(source_map_id)
        add_finding(findings, "Transfer Source", f"{transfer_id}-MAP", f"Map {source_map_id} JSON exists", source_map is not None, f"Map{source_map_id:03d}.json exists")
        if not source_map:
            continue

        event = find_transfer_event(source_map, transfer_id)
        add_finding(findings, "Transfer Event", transfer_id, f"{transfer_id} event exists on {source}", event is not None, "event containing transfer ID")
        if not event:
            continue
        x = int(event.get("x", -1))
        y = int(event.get("y", -1))
        in_bounds = 0 <= x < source_map["width"] and 0 <= y < source_map["height"]
        add_finding(findings, "Transfer Event", f"{transfer_id}-POS", f"{transfer_id} event is in source map bounds", in_bounds, f"event position=({x}, {y}) source size={source_map['width']}x{source_map['height']}")
        add_finding(findings, "Transfer Event", f"{transfer_id}-TILE", f"{transfer_id} event sits on concrete tile", tile_value(source_map, x, y, 0) not in {None, 0}, f"layer0 tile={tile_value(source_map, x, y, 0)}")

        target_map_id, target_label = target_map_for_transfer(transfer, screen_maps, by_name)
        add_finding(findings, "Transfer Target", f"{transfer_id}-TARGET", f"{target_label} resolves to RPG Maker map", target_map_id is not None, f"target={target_label}")
        if target_map_id is None:
            continue

        commands = transfer_commands(event)
        matching = [params for _, params in commands if len(params) >= 2 and params[1] == target_map_id]
        add_finding(findings, "Transfer Command", f"{transfer_id}-CMD", f"{transfer_id} transfers to map {target_map_id}", bool(matching), f"transfer command to map {target_map_id}")
        target_map = maps.get(target_map_id)
        if target_map and matching:
            coordinate_ok = False
            details = []
            for params in matching:
                tx = int(params[2]) if len(params) > 2 else -1
                ty = int(params[3]) if len(params) > 3 else -1
                ok = 0 <= tx < target_map["width"] and 0 <= ty < target_map["height"]
                coordinate_ok = coordinate_ok or ok
                details.append(f"({tx}, {ty}) in {target_map['width']}x{target_map['height']}={ok}")
            add_finding(findings, "Transfer Command", f"{transfer_id}-DEST", f"{transfer_id} destination coordinate is in bounds", coordinate_ok, "; ".join(details))

        if target in screen_maps and matching:
            graph[source].add(target)

    return findings, graph


def audit_reachability(
    project_root: Path,
    maps: dict[int, dict[str, Any]],
    screen_maps: dict[str, dict[str, Any]],
    graph: dict[str, set[str]],
) -> list[Finding]:
    findings: list[Finding] = []
    system = load_json(project_root / "data" / "System.json")
    by_map = screen_by_map_id(screen_maps)
    start_screen = by_map.get(int(system.get("startMapId", 0)))
    add_finding(findings, "Reachability", "REACH-START", "Game start map resolves to Home Island screen", start_screen is not None, f"startMapId={system.get('startMapId')} start_screen={start_screen}")
    if not start_screen:
        return findings

    seen = {start_screen}
    queue = deque([start_screen])
    while queue:
        screen = queue.popleft()
        for target in sorted(graph.get(screen, [])):
            if target not in seen:
                seen.add(target)
                queue.append(target)

    for screen_id in sorted(screen_maps):
        add_finding(findings, "Reachability", f"REACH-{screen_id}", f"{screen_id} reachable from {start_screen}", screen_id in seen, f"reachable screens={len(seen)}")

    return findings


def audit_orphan_transfer_events(export: dict[str, Any], maps: dict[int, dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    known = {transfer["transfer_id"] for transfer in export["home_island"]["transfers"]}
    for map_id, map_data in sorted(maps.items()):
        for event in iter_events(map_data):
            name = str(event.get("name", ""))
            if "TRN-HOM-" not in name:
                continue
            transfer_id = next((part for part in name.split() if part.startswith("TRN-HOM-")), "")
            if transfer_id and transfer_id not in known:
                findings.append(Finding("Transfer Hygiene", f"ORPHAN-{map_id}-{event.get('id')}", "No orphan transfer events", WARNING, f"{name} on map {map_id} not present in Atlas export"))
    if not findings:
        findings.append(Finding("Transfer Hygiene", "ORPHAN-000", "No orphan transfer events", FOUND, "All TRN-HOM events found in maps are present in Atlas export"))
    return findings


def status_counts(findings: list[Finding]) -> Counter:
    return Counter(finding.status for finding in findings)


def render_table(findings: list[Finding]) -> list[str]:
    lines = ["| Status | Category | Check ID | Expected | Detail |", "|---|---|---|---|---|"]
    for finding in findings:
        lines.append(f"| {finding.status} | {finding.category} | `{finding.check_id}` | {finding.expected} | {finding.detail} |")
    return lines


def render_report(export_path: Path, project_root: Path, findings: list[Finding]) -> str:
    counts = status_counts(findings)
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.category].append(finding)

    lines = [
        "# BUILD-0027 - All-Map Playtest Route Audit",
        "",
        "This read-only audit checks Atlas Home Island transfer expectations against current RPG Maker MZ map data.",
        "",
        f"- Atlas export: `{export_path}`",
        f"- Project root: `{project_root}`",
        "",
        "## Summary",
        "",
        f"- Found: {counts[FOUND]}",
        f"- Missing: {counts[MISSING]}",
        f"- Present with warning: {counts[WARNING]}",
        f"- Total findings: {len(findings)}",
        "",
        "## Category Summary",
        "",
        "| Category | Found | Missing | Warning |",
        "|---|---:|---:|---:|",
    ]
    for category in sorted(grouped):
        category_counts = status_counts(grouped[category])
        lines.append(f"| {category} | {category_counts[FOUND]} | {category_counts[MISSING]} | {category_counts[WARNING]} |")

    lines.extend(["", "## Findings", ""])
    for category in sorted(grouped):
        lines.extend([f"### {category}", ""])
        lines.extend(render_table(grouped[category]))
        lines.append("")

    lines.extend(
        [
            "## Notes",
            "",
            "- This audit follows transfer commands found in RPG Maker JSON; it does not simulate player collision, switch timing, or runtime plugin behavior.",
            "- A reachable screen means at least one directed transfer-command path exists from the configured start map, ignoring story gates.",
            "- This audit does not modify RPG Maker data files.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    export_path = Path(args.export).expanduser().resolve()
    project_root = Path(args.project_root).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    export = load_json(export_path)
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    maps = load_project_maps(project_root, map_infos)
    screen_maps = map_info_by_screen(export, map_infos)

    findings, graph = audit_transfer_rows(export, project_root, map_infos, maps, screen_maps)
    findings.extend(audit_reachability(project_root, maps, screen_maps, graph))
    findings.extend(audit_orphan_transfer_events(export, maps))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(export_path, project_root, findings), encoding="utf-8")
    counts = status_counts(findings)
    print(output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path)
    print(f"found={counts[FOUND]} missing={counts[MISSING]} warning={counts[WARNING]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
