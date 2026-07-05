#!/usr/bin/env python3
"""Read-only audit for executable RPG Maker event-command coverage."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-exports" / "home-island.json"
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "build-0030-event-command-coverage-audit.md"

FOUND = "found"
MISSING = "missing"
WARNING = "present with warning"

COMMENT_ONLY_CODES = {0, 108, 408}
TEXT_CODES = {101, 401}
TRANSFER_CODES = {201}
REWARD_CODES = {126, 127}
STATE_CODES = {121, 122, 123}
SHOP_CODES = {302}
BATTLE_CODES = {301}
CHOICE_CODES = {102, 402, 404}
CONDITIONAL_CODES = {111, 411, 412}
COMMON_EVENT_CODES = {117}
VISUAL_CODES = {221, 222, 250, 337}

LOCAL_ANCHORS = {
    "INT-ASH-WARM-STONE-VENT": "INT-ASH-WARM-STONE-VENT Warm-Stone Vent",
    "INT-ASH-OLD-PANEL": "INT-ASH-OLD-PANEL Old Panel",
    "INT-ASH-ELARA-KEEPSAKE": "INT-ASH-ELARA-KEEPSAKE Keepsake Shelf",
    "INT-ASH-SHOP-CABINET": "INT-ASH-SHOP-CABINET Metal Cabinet",
    "INT-SKY-GEOMETRIC-STONES": "INT-SKY-GEOMETRIC-STONES Geometric Stones",
    "INT-HCV-WALL-CARVING": "INT-HCV-WALL-CARVING Wall Carving",
    "OBJ-HOM-FOG-009": "Deeper Marsh Reward Cache",
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
    parser.add_argument("output", nargs="?", default=str(DEFAULT_OUTPUT), help="Markdown report path.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Required JSON file not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {path}: {error}")


def rows_by_name(rows: list[Any]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if isinstance(row, dict) and row.get("name"):
            result[str(row["name"]).strip().lower()].append(row)
    return result


def map_id_by_screen(export: dict[str, Any], map_infos: list[Any]) -> dict[str, int]:
    by_name = rows_by_name(map_infos)
    result = {}
    for screen in export["home_island"]["screens"]:
        matches = by_name.get(str(screen["rpg_maker_map_name"]).strip().lower(), [])
        if matches:
            result[screen["screen_id"]] = int(matches[0]["id"])
    return result


def load_maps(project_root: Path) -> dict[int, dict[str, Any]]:
    maps = {}
    for path in (project_root / "data").glob("Map[0-9][0-9][0-9].json"):
        maps[int(path.stem.removeprefix("Map"))] = load_json(path)
    return maps


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


def event_contains(event: dict[str, Any], marker: str) -> bool:
    if marker in str(event.get("name", "")) or marker in str(event.get("note", "")):
        return True
    for _, command in iter_commands(event):
        if command.get("code") in {108, 408} and marker in command_text(command):
            return True
    return False


def find_event_by_marker(maps: dict[int, dict[str, Any]], map_id: int | None, marker: str, expected_name: str | None = None) -> dict[str, Any] | None:
    search_maps = [maps[map_id]] if map_id in maps else maps.values()
    for map_data in search_maps:
        for event in iter_events(map_data):
            if expected_name and str(event.get("name", "")).strip() == expected_name:
                return event
            if event_contains(event, marker):
                return event
    return None


def executable_codes(event: dict[str, Any]) -> list[int]:
    return [
        int(command.get("code", 0))
        for _, command in iter_commands(event)
        if int(command.get("code", 0)) not in COMMENT_ONLY_CODES
    ]


def code_summary(codes: list[int]) -> str:
    counts = Counter(codes)
    return ", ".join(f"{code}x{count}" for code, count in sorted(counts.items())) or "none"


def add(findings: list[Finding], category: str, check_id: str, expected: str, ok: bool, detail: str, warning: bool = False) -> None:
    status = FOUND if ok else (WARNING if warning else MISSING)
    findings.append(Finding(category, check_id, expected, status, detail if ok else f"Expected {detail}"))


def audit_event_marker(findings: list[Finding], category: str, marker: str, event: dict[str, Any] | None, required_codes: set[int] | None = None) -> None:
    add(findings, category, marker, f"{marker} event exists", event is not None, "event found")
    if not event:
        return
    codes = executable_codes(event)
    add(findings, category, f"{marker}-EXEC", f"{marker} has executable commands", bool(codes), f"codes={code_summary(codes)}")
    if required_codes:
        has_required = any(code in required_codes for code in codes)
        add(findings, category, f"{marker}-REQ", f"{marker} includes required command family", has_required, f"codes={code_summary(codes)}")


def audit_atlas_events(export: dict[str, Any], maps: dict[int, dict[str, Any]], screen_maps: dict[str, int]) -> list[Finding]:
    findings: list[Finding] = []
    for row in export["home_island"]["events"]:
        marker = row["event_id"]
        map_id = screen_maps.get(row["screen"])
        event = find_event_by_marker(maps, map_id, marker)
        required = None
        if marker == "EVT-HOM-008":
            required = SHOP_CODES
        elif marker == "EVT-HOM-021":
            required = BATTLE_CODES
        elif marker in {"EVT-HOM-007", "EVT-HOM-016", "EVT-HOM-028"}:
            required = REWARD_CODES
        elif marker in {"EVT-HOM-001", "EVT-HOM-009", "EVT-HOM-011", "EVT-HOM-012", "EVT-HOM-013", "EVT-HOM-014", "EVT-HOM-017", "EVT-HOM-019", "EVT-HOM-020", "EVT-HOM-022", "EVT-HOM-026"}:
            required = STATE_CODES
        else:
            required = TEXT_CODES | CHOICE_CODES | CONDITIONAL_CODES | COMMON_EVENT_CODES | VISUAL_CODES
        audit_event_marker(findings, "Atlas Event Commands", marker, event, required)
    return findings


def audit_transfer_events(export: dict[str, Any], maps: dict[int, dict[str, Any]], screen_maps: dict[str, int]) -> list[Finding]:
    findings: list[Finding] = []
    for row in export["home_island"]["transfers"]:
        marker = row["transfer_id"]
        event = find_event_by_marker(maps, screen_maps.get(row["from"]), marker)
        audit_event_marker(findings, "Transfer Commands", marker, event, TRANSFER_CODES | CHOICE_CODES | CONDITIONAL_CODES)
    return findings


def audit_local_anchors(maps: dict[int, dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    for marker, name in LOCAL_ANCHORS.items():
        event = find_event_by_marker(maps, None, marker, name)
        required = REWARD_CODES if marker == "OBJ-HOM-FOG-009" else TEXT_CODES
        audit_event_marker(findings, "Local Anchor Commands", marker, event, required)
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
        "# BUILD-0030 - Event Command Coverage Audit",
        "",
        "This read-only audit checks whether Atlas events, Atlas transfers, and generated local anchors have executable RPG Maker event commands.",
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

    lines.extend([
        "## Notes",
        "",
        "- Executable commands are commands beyond comments and event terminators.",
        "- The audit checks command-family presence, not final dialogue quality or runtime timing.",
        "- This audit does not modify RPG Maker data files.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    export_path = Path(args.export).expanduser().resolve()
    project_root = Path(args.project_root).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    export = load_json(export_path)
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    maps = load_maps(project_root)
    screen_maps = map_id_by_screen(export, map_infos)

    findings = []
    findings.extend(audit_atlas_events(export, maps, screen_maps))
    findings.extend(audit_transfer_events(export, maps, screen_maps))
    findings.extend(audit_local_anchors(maps))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(export_path, project_root, findings), encoding="utf-8")
    counts = status_counts(findings)
    print(output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path)
    print(f"found={counts[FOUND]} missing={counts[MISSING]} warning={counts[WARNING]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
