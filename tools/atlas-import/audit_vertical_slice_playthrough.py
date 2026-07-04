#!/usr/bin/env python3
"""Read-only Home Island vertical-slice playthrough audit for the clean skeleton."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "build-0008-vertical-slice-playthrough-audit.md"

FOUND = "found"
MISSING = "missing"
WARNING = "present with warning"
UNKNOWN = "not machine-checkable yet"


@dataclass(frozen=True)
class Finding:
    category: str
    check_id: str
    expected: str
    status: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output",
        nargs="?",
        default=str(DEFAULT_OUTPUT),
        help="Markdown report path.",
    )
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="Clean RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_maps(project_root: Path) -> dict[int, dict]:
    maps = {}
    for path in (project_root / "data").glob("Map[0-9][0-9][0-9].json"):
        maps[int(path.stem.removeprefix("Map"))] = load_json(path)
    return maps


def iter_events(map_data: dict):
    for event in map_data.get("events", []):
        if isinstance(event, dict):
            yield event


def find_event(maps: dict[int, dict], map_id: int, name: str) -> dict | None:
    map_data = maps.get(map_id)
    if not map_data:
        return None
    for event in iter_events(map_data):
        if event.get("name") == name:
            return event
    return None


def commands(event: dict) -> list[dict]:
    result = []
    for page in event.get("pages", []):
        for command in page.get("list", []):
            if isinstance(command, dict):
                result.append(command)
    return result


def page_conditions(event: dict) -> list[dict]:
    return [
        page.get("conditions", {})
        for page in event.get("pages", [])
        if isinstance(page, dict)
    ]


def has_switch_on(event: dict, switch_id: int) -> bool:
    return any(command.get("code") == 121 and command.get("parameters") == [switch_id, switch_id, 0] for command in commands(event))


def has_variable_set(event: dict, variable_id: int, value: int) -> bool:
    return any(command.get("code") == 122 and command.get("parameters") == [variable_id, variable_id, 0, 0, value] for command in commands(event))


def has_transfer(event: dict, target_map_id: int) -> bool:
    for command in commands(event):
        if command.get("code") != 201:
            continue
        parameters = command.get("parameters", [])
        if len(parameters) >= 2 and parameters[1] == target_map_id:
            return True
    return False


def has_battle(event: dict, troop_id: int) -> bool:
    for command in commands(event):
        if command.get("code") != 301:
            continue
        parameters = command.get("parameters", [])
        if len(parameters) >= 2 and parameters[1] == troop_id:
            return True
    return False


def has_item_gain(event: dict, item_id: int) -> bool:
    return any(command.get("code") == 126 and command.get("parameters", [])[:3] == [item_id, 0, 0] for command in commands(event))


def has_weapon_gain(event: dict, weapon_id: int) -> bool:
    return any(command.get("code") == 127 and command.get("parameters", [])[:3] == [weapon_id, 0, 0] for command in commands(event))


def has_gated_page(event: dict, switch_id: int) -> bool:
    for conditions in page_conditions(event):
        if conditions.get("switch1Valid") and conditions.get("switch1Id") == switch_id:
            return True
        if conditions.get("switch2Valid") and conditions.get("switch2Id") == switch_id:
            return True
    return False


def has_conditional_switch(event: dict, switch_id: int) -> bool:
    return any(command.get("code") == 111 and command.get("parameters") == [0, switch_id, 0] for command in commands(event))


def check_event(maps: dict[int, dict], findings: list[Finding], check_id: str, map_id: int, event_name: str) -> dict | None:
    event = find_event(maps, map_id, event_name)
    if event:
        findings.append(Finding("Critical Route", check_id, f"Map {map_id} event {event_name}", FOUND, f"Event id {event.get('id')} at ({event.get('x')}, {event.get('y')})"))
        return event
    findings.append(Finding("Critical Route", check_id, f"Map {map_id} event {event_name}", MISSING, "Event not found"))
    return None


def check_predicate(findings: list[Finding], category: str, check_id: str, expected: str, predicate: bool, detail: str) -> None:
    findings.append(Finding(category, check_id, expected, FOUND if predicate else MISSING, detail if predicate else f"Missing: {detail}"))


def audit_start(project_root: Path, maps: dict[int, dict]) -> list[Finding]:
    findings: list[Finding] = []
    system = load_json(project_root / "data" / "System.json")
    start_map_id = system.get("startMapId")
    start_x = system.get("startX")
    start_y = system.get("startY")
    check_predicate(findings, "Start State", "START-001", "Start map is Elara House map 2", start_map_id == 2, f"startMapId={start_map_id}")
    check_predicate(findings, "Start State", "START-002", "Start coordinate is within map bounds", start_map_id in maps and 0 <= start_x < maps[start_map_id]["width"] and 0 <= start_y < maps[start_map_id]["height"], f"start=({start_x}, {start_y})")
    return findings


def audit_route(maps: dict[int, dict]) -> list[Finding]:
    findings: list[Finding] = []

    effects = [
        ("ROUTE-001", 2, "Player Start", [(has_variable_set, (1, 1), "Current_Journey = 1"), (has_variable_set, (2, 0), "Archive_Recovery_Percent = 0")]),
        ("ROUTE-002", 2, "TRN-HOM-001 Elara House exit", [(has_transfer, (1,), "Transfer to Ashford Exterior")]),
        ("ROUTE-003", 1, "Tremor Trigger", [(has_switch_on, (1,), "J1_Tremor_Event ON"), (has_switch_on, (2,), "J1_Skyreach_AccessOpen ON")]),
        ("ROUTE-004", 1, "TRN-HOM-005 North path to Skyreach", [(has_transfer, (4,), "Transfer to Skyreach"), (has_gated_page, (2,), "Gate requires J1_Skyreach_AccessOpen")]),
        ("ROUTE-005", 4, "TRN-HOM-009 Enter Hidden Cave", [(has_transfer, (5,), "Transfer to Hidden Cave"), (has_gated_page, (2,), "Gate requires J1_Skyreach_AccessOpen")]),
        ("ROUTE-006", 5, "Hidden Cave First Entry", [(has_switch_on, (3,), "J1_HiddenCave_Entered ON")]),
        ("ROUTE-007", 5, "TRN-HOM-011 Enter trials", [(has_transfer, (6,), "Transfer to Hidden Cave Trials")]),
        ("ROUTE-008", 6, "Body Trial", [(has_switch_on, (4,), "J1_Trial_Body_Clear ON")]),
        ("ROUTE-009", 6, "Mind Trial", [(has_switch_on, (5,), "J1_Trial_Mind_Clear ON")]),
        ("ROUTE-010", 6, "Heart Trial", [(has_switch_on, (6,), "J1_Trial_Heart_Clear ON")]),
        ("ROUTE-011", 6, "TRN-HOM-013 Enter Sword Sanctum", [(has_transfer, (7,), "Transfer to Sword Sanctum"), (has_conditional_switch, (4,), "Checks Body trial"), (has_conditional_switch, (5,), "Checks Mind trial"), (has_conditional_switch, (6,), "Checks Heart trial")]),
        ("ROUTE-012", 7, "Sword Pedestal", [(has_switch_on, (7,), "J1_Sword_Obtained ON"), (has_variable_set, (2, 3), "Archive_Recovery_Percent = 3"), (has_item_gain, (201,), "Sword key item gained"), (has_weapon_gain, (2,), "Sword weapon gained")]),
        ("ROUTE-013", 8, "Glassfield Seal", [(has_switch_on, (8,), "J1_Glassfield_SealOpened ON")]),
        ("ROUTE-014", 8, "TRN-HOM-017 Enter Sealed Node", [(has_transfer, (9,), "Transfer to Sealed Node Upper"), (has_gated_page, (8,), "Gate requires J1_Glassfield_SealOpened")]),
        ("ROUTE-015", 9, "Sealed Node First Entry", [(has_switch_on, (9,), "J1_SealedNode_Entered ON")]),
        ("ROUTE-016", 10, "Core Path Door", [(has_switch_on, (10,), "J1_CorePath_DoorOpened ON")]),
        ("ROUTE-017", 11, "Node Seven Guardian", [(has_battle, (10,), "Battle Processing troop 10"), (has_switch_on, (11,), "J1_Node07_GuardianDefeated ON")]),
        ("ROUTE-018", 11, "TRN-HOM-023 Enter relay core", [(has_transfer, (12,), "Transfer to Relay Core"), (has_gated_page, (11,), "Gate requires J1_Node07_GuardianDefeated")]),
        ("ROUTE-019", 12, "Relay Core", [(has_switch_on, (12,), "J1_Node07_RelayRestored ON"), (has_switch_on, (13,), "J1_Mainland_TravelUnlocked ON"), (has_variable_set, (2, 5), "Archive_Recovery_Percent = 5")]),
        ("ROUTE-020", 13, "TRN-HOM-025 Begin departure", [(has_transfer, (14,), "Transfer to departure map"), (has_conditional_switch, (13,), "Checks J1_Mainland_TravelUnlocked"), (has_switch_on, (14,), "J1_Departure_Confirmed ON")]),
        ("ROUTE-021", 14, "Departure Sequence", [(has_variable_set, (1, 2), "Current_Journey = 2")]),
        ("ROUTE-022", 14, "TRN-HOM-026 Destination TBD: Coalmouth or landing screen", [(has_transfer, (50,), "Transfer to Journey II placeholder")]),
    ]

    for check_id, map_id, event_name, predicates in effects:
        event = check_event(maps, findings, check_id, map_id, event_name)
        if not event:
            continue
        for predicate, args, detail in predicates:
            check_predicate(findings, "Critical Route Effects", check_id, f"{event_name}: {detail}", predicate(event, *args), detail)

    return findings


def audit_return_transfers(maps: dict[int, dict]) -> list[Finding]:
    findings: list[Finding] = []
    transfers = [
        ("RETURN-001", 7, "TRN-HOM-014 Return from sanctum", 6),
        ("RETURN-002", 6, "TRN-HOM-012 Return to entrance", 5),
        ("RETURN-003", 5, "TRN-HOM-010 Exit cave", 4),
        ("RETURN-004", 4, "TRN-HOM-006 Return from Skyreach route", 1),
        ("RETURN-005", 9, "TRN-HOM-018 Exit Sealed Node", 8),
        ("RETURN-006", 10, "TRN-HOM-020 Return to upper node", 9),
        ("RETURN-007", 11, "TRN-HOM-022 Return to core path", 10),
        ("RETURN-008", 12, "TRN-HOM-024 Return from relay core", 11),
        ("RETURN-009", 13, "TRN-HOM-008 Return from Rustshore route", 1),
    ]
    for check_id, map_id, event_name, target in transfers:
        event = check_event(maps, findings, check_id, map_id, event_name)
        if event:
            check_predicate(findings, "Return Transfers", check_id, f"{event_name}: transfer to map {target}", has_transfer(event, target), f"Transfer to map {target}")
    return findings


def audit_manual_scope() -> list[Finding]:
    return [
        Finding(
            "Manual Runtime Scope",
            "MANUAL-001",
            "Manual RPG Maker runtime playthrough",
            UNKNOWN,
            "JSON audit proves route structure; hands-on runtime timing/input feel still requires RPG Maker playtest.",
        )
    ]


def status_counts(findings: list[Finding]) -> Counter:
    return Counter(finding.status for finding in findings)


def render_table(findings: list[Finding]) -> list[str]:
    lines = ["| Status | Category | Check ID | Expected | Detail |", "|---|---|---|---|---|"]
    for finding in findings:
        lines.append(f"| {finding.status} | {finding.category} | `{finding.check_id}` | {finding.expected} | {finding.detail} |")
    return lines


def render_report(project_root: Path, findings: list[Finding]) -> str:
    counts = status_counts(findings)
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.category].append(finding)

    lines = [
        "# BUILD-0008 - Home Island Vertical Slice Playthrough Audit",
        "",
        "This read-only audit checks the clean RPG Maker MZ skeleton for a machine-visible Home Island route from new game start to the Journey II placeholder.",
        "",
        f"- Project root: `{project_root}`",
        "",
        "## Summary",
        "",
        f"- Found: {counts[FOUND]}",
        f"- Missing: {counts[MISSING]}",
        f"- Present with warning: {counts[WARNING]}",
        f"- Not machine-checkable yet: {counts[UNKNOWN]}",
        f"- Total findings: {len(findings)}",
        "",
        "## Category Summary",
        "",
        "| Category | Found | Missing | Warning | Not Machine-Checkable |",
        "|---|---:|---:|---:|---:|",
    ]
    for category in sorted(grouped):
        category_counts = status_counts(grouped[category])
        lines.append(
            f"| {category} | {category_counts[FOUND]} | {category_counts[MISSING]} | "
            f"{category_counts[WARNING]} | {category_counts[UNKNOWN]} |"
        )

    lines.extend(["", "## Findings", ""])
    for category in sorted(grouped):
        lines.extend([f"### {category}", ""])
        lines.extend(render_table(grouped[category]))
        lines.append("")

    lines.extend(
        [
            "## Notes",
            "",
            "- `missing` means a critical route event, transfer, switch, variable, battle, or reward command was not found.",
            "- `not machine-checkable yet` is limited to hands-on RPG Maker runtime playtest feel and timing.",
            "- This audit does not modify RPG Maker data files.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    maps = load_maps(project_root)
    findings = []
    findings.extend(audit_start(project_root, maps))
    findings.extend(audit_route(maps))
    findings.extend(audit_return_transfers(maps))
    findings.extend(audit_manual_scope())
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(project_root, findings), encoding="utf-8")
    counts = status_counts(findings)
    print(output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path)
    print(f"found={counts[FOUND]} missing={counts[MISSING]} warning={counts[WARNING]} unknown={counts[UNKNOWN]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
