#!/usr/bin/env python3
"""Read-only audit of RPG Maker data against an Atlas Home Island export."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "home-island-data-readiness-audit.md"

FOUND = "found"
MISSING = "missing"
WARNING = "present with warning"
UNKNOWN = "not machine-checkable yet"


DATABASE_FILES = {
    "Actor": "Actors.json",
    "Class": "Classes.json",
    "Enemy": "Enemies.json",
    "Troop": "Troops.json",
    "Skill": "Skills.json",
    "State": "States.json",
    "Item": "Items.json",
    "Key Item": "Items.json",
    "Weapon": "Weapons.json",
    "Armor": "Armors.json",
}


@dataclass(frozen=True)
class Finding:
    category: str
    atlas_id: str
    expected: str
    status: str
    detail: str


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Required JSON file not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {path}: {error}")


def load_export(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Atlas export not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in Atlas export: {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only audit of RPG Maker data against an Atlas Home Island export.",
    )
    parser.add_argument("export", help="Path to atlas-exports/home-island.json")
    parser.add_argument(
        "output",
        nargs="?",
        default=str(DEFAULT_OUTPUT),
        help="Markdown report path. Defaults to reports/atlas-import/home-island-data-readiness-audit.md.",
    )
    parser.add_argument(
        "--project-root",
        default=str(ROOT),
        help="RPG Maker project root to audit. Defaults to this repository.",
    )
    return parser.parse_args()


def norm(value: object) -> str:
    return str(value or "").strip().lower()


def row_by_id(rows: list, row_id: str) -> dict | None:
    try:
        target = int(row_id)
    except (TypeError, ValueError):
        return None
    if target < 0 or target >= len(rows):
        return None
    row = rows[target]
    return row if isinstance(row, dict) else None


def rows_by_name(rows: list) -> dict[str, list[dict]]:
    index: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if isinstance(row, dict) and row.get("name"):
            index[norm(row["name"])].append(row)
    return index


def audit_maps(home: dict, map_infos: list) -> list[Finding]:
    findings: list[Finding] = []
    by_name = rows_by_name(map_infos)
    for screen in home["screens"]:
        name = screen["rpg_maker_map_name"]
        matches = by_name.get(norm(name), [])
        if matches:
            ids = ", ".join(str(row.get("id")) for row in matches)
            findings.append(Finding("Maps", screen["screen_id"], name, FOUND, f"MapInfos id(s): {ids}"))
        else:
            findings.append(Finding("Maps", screen["screen_id"], name, MISSING, "No MapInfos entry with this map name"))
    return findings


def audit_database_allocation(home: dict, data: dict[str, list]) -> list[Finding]:
    findings: list[Finding] = []
    allocation = home["combat_database"]["database_id_allocation"]

    for expected in allocation:
        database = expected["database"]
        row_id = expected["id"]
        name = expected["name"]
        atlas_source = expected.get("atlas_source", "")
        filename = DATABASE_FILES.get(database)
        if not filename:
            findings.append(Finding(database, atlas_source, f"{database} {row_id} {name}", UNKNOWN, "No audit mapping for database type"))
            continue

        rows = data[filename]
        row = row_by_id(rows, row_id)
        label = f"{database} {row_id} - {name}"
        if row is None:
            by_name = rows_by_name(rows).get(norm(name), [])
            if by_name:
                ids = ", ".join(str(match.get("id")) for match in by_name)
                findings.append(Finding(database, atlas_source, label, WARNING, f"Name exists at different id(s): {ids}"))
            else:
                findings.append(Finding(database, atlas_source, label, MISSING, f"{filename} has no row at id {row_id}"))
            continue

        actual_name = row.get("name", "")
        if norm(actual_name) == norm(name):
            findings.append(Finding(database, atlas_source, label, FOUND, f"{filename} id {row_id} matches name"))
        else:
            by_name = rows_by_name(rows).get(norm(name), [])
            if by_name:
                ids = ", ".join(str(match.get("id")) for match in by_name)
                detail = f"ID {row_id} is named {actual_name!r}; expected name exists at id(s): {ids}"
            else:
                detail = f"ID {row_id} is named {actual_name!r}; expected name not found elsewhere"
            findings.append(Finding(database, atlas_source, label, WARNING, detail))

    return findings


def audit_skill_details(home: dict, skills: list) -> list[Finding]:
    findings: list[Finding] = []
    for skill in home["combat_database"]["skills"]:
        row_id = skill["skill_id"]
        name = skill["name"]
        animation = skill.get("animation", "")
        row = row_by_id(skills, row_id)
        label = f"Skill {row_id} - {name}"
        if row is None:
            findings.append(Finding("Skill Details", row_id, label, MISSING, "Skills.json row missing"))
            continue
        details = []
        status = FOUND
        if norm(row.get("name")) != norm(name):
            status = WARNING
            details.append(f"name is {row.get('name')!r}")
        if str(row.get("animationId", "")) != str(animation):
            status = WARNING
            details.append(f"animationId is {row.get('animationId')!r}, expected {animation!r}")
        findings.append(
            Finding(
                "Skill Details",
                row_id,
                label,
                status,
                "; ".join(details) if details else "Name and animation ID match",
            )
        )
    return findings


def audit_troop_details(home: dict, troops: list) -> list[Finding]:
    findings: list[Finding] = []
    for troop in home["combat_database"]["troops"]:
        if "name" not in troop:
            findings.append(
                Finding(
                    "Troop Event Pages",
                    troop["troop_id"],
                    f"Troop {troop['troop_id']} event page {troop.get('page')}",
                    UNKNOWN,
                    "Troop event page command parsing is not implemented in WO-0020",
                )
            )
            continue
        row_id = troop["troop_id"]
        name = troop["name"]
        row = row_by_id(troops, row_id)
        label = f"Troop {row_id} - {name}"
        if row is None:
            findings.append(Finding("Troop Details", row_id, label, MISSING, "Troops.json row missing"))
        elif norm(row.get("name")) == norm(name):
            findings.append(Finding("Troop Details", row_id, label, FOUND, "Troop row name matches"))
        else:
            findings.append(Finding("Troop Details", row_id, label, WARNING, f"Troop row name is {row.get('name')!r}"))
    return findings


def audit_tilesets(home: dict, tilesets: list) -> list[Finding]:
    findings: list[Finding] = []
    by_name = rows_by_name(tilesets)
    seen: set[str] = set()
    for tile in home["tilesets"]:
        name = tile["placeholder_tileset"]
        if name in seen:
            continue
        seen.add(name)
        matches = by_name.get(norm(name), [])
        if matches:
            ids = ", ".join(str(row.get("id")) for row in matches)
            findings.append(Finding("Tilesets", name, name, FOUND, f"Tilesets.json id(s): {ids}"))
        else:
            findings.append(Finding("Tilesets", name, name, MISSING, "No Tilesets.json row with this name"))
    return findings


def audit_animations(home: dict, animations: list) -> list[Finding]:
    findings: list[Finding] = []
    expected_rows: dict[str, str] = {}
    for row in home["animations"]["core_animation_ids"]:
        expected_rows[row["animation_id"]] = row["animation_name"]
    for row in home["animations"]["combat_animation_matrix"]:
        expected_rows.setdefault(row["rpg_maker_animation_id"], row["animation_name"])
    for row in home["animations"]["story_event_animation_matrix"]:
        expected_rows.setdefault(row["rpg_maker_animation_id"], row["animation_name"])

    def animation_sort(item: tuple[str, str]) -> int:
        try:
            return int(item[0])
        except (TypeError, ValueError):
            return 999999

    for animation_id, name in sorted(expected_rows.items(), key=animation_sort):
        row = row_by_id(animations, animation_id)
        label = f"Animation {animation_id} - {name}"
        if str(animation_id).lower() == "none":
            findings.append(Finding("Animations", animation_id, label, UNKNOWN, "Atlas explicitly allows no RPG Maker animation"))
            continue
        if row is None:
            findings.append(Finding("Animations", animation_id, label, MISSING, "Animations.json row missing"))
        elif norm(row.get("name")) == norm(name):
            findings.append(Finding("Animations", animation_id, label, FOUND, "Animation row name matches"))
        else:
            findings.append(Finding("Animations", animation_id, label, WARNING, f"Animation row name is {row.get('name')!r}"))
    return findings


def audit_non_machine_checkable(home: dict) -> list[Finding]:
    findings: list[Finding] = []
    for transfer in home["transfers"]:
        findings.append(
            Finding(
                "Transfers",
                transfer["transfer_id"],
                f"{transfer['from']} -> {transfer['to']}",
                UNKNOWN,
                "Requires map event command parsing; not implemented in WO-0020",
            )
        )
    for event in home["events"]:
        findings.append(
            Finding(
                "Atlas Events",
                event["event_id"],
                f"{event['screen']} - {event['event']}",
                UNKNOWN,
                "Requires map event page parsing; not implemented in WO-0020",
            )
        )
    for switch in home["trial_mechanics"]["switches"]:
        findings.append(
            Finding(
                "Trial State",
                switch,
                switch,
                UNKNOWN,
                "RPG Maker switch names are stored in System.json arrays and require future range policy audit",
            )
        )
    for variable in home["trial_mechanics"]["variables"]:
        findings.append(
            Finding(
                "Trial State",
                variable,
                variable,
                UNKNOWN,
                "RPG Maker variable names are stored in System.json arrays and require future range policy audit",
            )
        )
    return findings


def run_audit(payload: dict, project_root: Path = ROOT) -> list[Finding]:
    home = payload["home_island"]
    data_dir = project_root / "data"
    data_files = {
        filename: load_json(data_dir / filename)
        for filename in {
            "MapInfos.json",
            "Actors.json",
            "Classes.json",
            "Items.json",
            "Weapons.json",
            "Armors.json",
            "Skills.json",
            "States.json",
            "Enemies.json",
            "Troops.json",
            "Tilesets.json",
            "Animations.json",
            "System.json",
        }
    }

    findings: list[Finding] = []
    findings.extend(audit_maps(home, data_files["MapInfos.json"]))
    findings.extend(audit_database_allocation(home, data_files))
    findings.extend(audit_skill_details(home, data_files["Skills.json"]))
    findings.extend(audit_troop_details(home, data_files["Troops.json"]))
    findings.extend(audit_tilesets(home, data_files["Tilesets.json"]))
    findings.extend(audit_animations(home, data_files["Animations.json"]))
    findings.extend(audit_non_machine_checkable(home))
    return findings


def status_counts(findings: list[Finding]) -> Counter:
    return Counter(finding.status for finding in findings)


def render_table(findings: list[Finding]) -> list[str]:
    lines = ["| Status | Category | Atlas / Expected ID | Expected | Detail |", "|---|---|---|---|---|"]
    for finding in findings:
        lines.append(
            f"| {finding.status} | {finding.category} | `{finding.atlas_id}` | "
            f"{finding.expected} | {finding.detail} |"
        )
    return lines


def render_report(payload: dict, findings: list[Finding]) -> str:
    source = payload.get("source", {})
    counts = status_counts(findings)
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.category].append(finding)

    lines = [
        "# Home Island RPG Maker Data Readiness Audit",
        "",
        "This report compares the Atlas Home Island export against current RPG Maker MZ data files.",
        "",
        "The audit is read-only. It does not modify RPG Maker JSON, maps, events, assets, or project settings.",
        "",
        "## Export Metadata",
        "",
        f"- Export: `{payload.get('export_name')}`",
        f"- Schema: `{payload.get('schema_version')}`",
        f"- Generated: `{payload.get('generated_at')}`",
        f"- Source repo: `{source.get('repository')}`",
        f"- Source commit: `{source.get('git_commit')}`",
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
            "- `missing` means the expected Atlas row or map name was not found in the current RPG Maker data.",
            "- `present with warning` usually means an ID exists but its name differs from Atlas, or the expected name exists at a different ID.",
            "- `not machine-checkable yet` means the export expectation requires parsing RPG Maker map events, event commands, switch ranges, or variable ranges beyond this work order.",
            "- Write-capable import behavior remains out of scope.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    export_path = Path(args.export).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    project_root = Path(args.project_root).expanduser().resolve()

    payload = load_json(export_path)
    findings = run_audit(payload, project_root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(payload, findings), encoding="utf-8")

    counts = status_counts(findings)
    print(output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path)
    print(f"found={counts[FOUND]} missing={counts[MISSING]} warning={counts[WARNING]} unknown={counts[UNKNOWN]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
