#!/usr/bin/env python3
"""Read-only audit of RPG Maker data against an Atlas Home Island export."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
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

EXTERNAL_TRANSFER_TARGETS = {
    "Journey II start": "JRN2_Landing_Placeholder",
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


def compact_norm(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "", norm(value).removeprefix("ce_").removeprefix("ce-"))


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


def map_info_by_screen(home: dict, map_infos: list) -> dict[str, dict]:
    by_name = rows_by_name(map_infos)
    result = {}
    for screen in home["screens"]:
        matches = by_name.get(norm(screen["rpg_maker_map_name"]), [])
        if matches:
            result[screen["screen_id"]] = matches[0]
    return result


def load_maps(data_dir: Path, map_infos: list) -> dict[int, dict]:
    maps = {}
    for row in map_infos:
        if not isinstance(row, dict) or not row.get("id"):
            continue
        map_id = int(row["id"])
        path = data_dir / f"Map{map_id:03d}.json"
        if path.exists():
            maps[map_id] = load_json(path)
    return maps


def iter_events(map_data: dict):
    for event in map_data.get("events", []):
        if isinstance(event, dict):
            yield event


def iter_page_commands(event: dict):
    for page_index, page in enumerate(event.get("pages", []), 1):
        for command in page.get("list", []):
            if isinstance(command, dict):
                yield page_index, command


def event_has_nonempty_commands(page: dict) -> bool:
    for command in page.get("list", []):
        if isinstance(command, dict) and command.get("code") not in {0, None}:
            return True
    return False


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


def audit_troop_event_pages(home: dict, troops: list) -> list[Finding]:
    findings: list[Finding] = []
    for troop in home["combat_database"]["troops"]:
        if "name" in troop:
            continue

        troop_id = troop["troop_id"]
        page = troop.get("page")
        commands = troop.get("commands", "")
        label = f"Troop {troop_id} event page {page}"

        if troop_id == "1-5":
            rows = [row_by_id(troops, str(index)) for index in range(1, 6)]
            missing_ids = [str(index) for index, row in zip(range(1, 6), rows) if row is None]
            if missing_ids:
                findings.append(Finding("Troop Event Pages", troop_id, label, MISSING, f"Missing troop row(s): {', '.join(missing_ids)}"))
                continue
            with_commands = []
            for index, row in zip(range(1, 6), rows):
                pages = row.get("pages", []) if isinstance(row, dict) else []
                if any(event_has_nonempty_commands(page_row) for page_row in pages):
                    with_commands.append(str(index))
            if with_commands:
                findings.append(Finding("Troop Event Pages", troop_id, label, WARNING, f"Expected no troop events, but commands exist on troop(s): {', '.join(with_commands)}"))
            else:
                findings.append(Finding("Troop Event Pages", troop_id, label, FOUND, "Troops 1-5 have no non-empty event page commands"))
            continue

        row = row_by_id(troops, troop_id)
        if row is None:
            findings.append(Finding("Troop Event Pages", troop_id, label, MISSING, "Troops.json row missing"))
            continue

        try:
            page_index = int(page)
        except (TypeError, ValueError):
            findings.append(Finding("Troop Event Pages", troop_id, label, WARNING, f"Unsupported page value {page!r}"))
            continue

        pages = row.get("pages", [])
        if page_index < 1 or page_index > len(pages):
            findings.append(Finding("Troop Event Pages", troop_id, label, MISSING, f"Expected page {page_index}; troop has {len(pages)} page(s)"))
            continue

        page_row = pages[page_index - 1]
        if "Optional" in commands and not event_has_nonempty_commands(page_row):
            findings.append(Finding("Troop Event Pages", troop_id, label, WARNING, "Optional troop page exists but contains no placeholder commands"))
        else:
            findings.append(Finding("Troop Event Pages", troop_id, label, FOUND, "Expected troop page exists and is parseable"))

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


def audit_atlas_events(home: dict, maps: dict[int, dict], screen_maps: dict[str, dict]) -> list[Finding]:
    findings: list[Finding] = []
    for event in home["events"]:
        screen = event["screen"]
        expected_name = event["event"]
        screen_map = screen_maps.get(screen)
        label = f"{screen} - {expected_name}"
        if not screen_map:
            findings.append(Finding("Atlas Events", event["event_id"], label, MISSING, "Source screen map is missing from MapInfos.json"))
            continue
        map_id = int(screen_map["id"])
        map_data = maps.get(map_id)
        if not map_data:
            findings.append(Finding("Atlas Events", event["event_id"], label, MISSING, f"Map{map_id:03d}.json is missing"))
            continue
        expected_key = compact_norm(expected_name)
        matches = [
            found_event
            for found_event in iter_events(map_data)
            if compact_norm(found_event.get("name", "")) == expected_key
        ]
        if matches:
            event_ids = ", ".join(str(found_event.get("id")) for found_event in matches)
            findings.append(Finding("Atlas Events", event["event_id"], label, FOUND, f"Map {map_id} event id(s): {event_ids}"))
        else:
            findings.append(Finding("Atlas Events", event["event_id"], label, MISSING, f"No event named {expected_name!r} on map {map_id}"))
    return findings


def audit_transfers(home: dict, maps: dict[int, dict], screen_maps: dict[str, dict]) -> list[Finding]:
    findings: list[Finding] = []
    for transfer in home["transfers"]:
        source = screen_maps.get(transfer["from"])
        target = screen_maps.get(transfer["to"])
        external_target_name = EXTERNAL_TRANSFER_TARGETS.get(transfer["to"])
        if target is None and external_target_name:
            # Extra placeholder maps such as Journey II are not Atlas screen
            # maps, so resolve them by their generated display name.
            for map_id, map_data in maps.items():
                if norm(map_data.get("displayName")) == norm("Journey II Landing Placeholder"):
                    target = {"id": map_id, "name": external_target_name}
                    break
        label = f"{transfer['from']} -> {transfer['to']}"
        if not source:
            findings.append(Finding("Transfers", transfer["transfer_id"], label, MISSING, "Source screen map is missing from MapInfos.json"))
            continue
        if not target:
            findings.append(Finding("Transfers", transfer["transfer_id"], label, MISSING, "Target screen map is missing from MapInfos.json"))
            continue
        source_id = int(source["id"])
        target_id = int(target["id"])
        source_map = maps.get(source_id)
        if not source_map:
            findings.append(Finding("Transfers", transfer["transfer_id"], label, MISSING, f"Map{source_id:03d}.json is missing"))
            continue

        matches = []
        for event in iter_events(source_map):
            for page_index, command in iter_page_commands(event):
                if command.get("code") != 201:
                    continue
                parameters = command.get("parameters", [])
                try:
                    command_target_id = int(parameters[1]) if len(parameters) >= 2 else 0
                except (TypeError, ValueError):
                    continue
                if command_target_id == target_id:
                    matches.append(f"event {event.get('id')} page {page_index}")

        if matches:
            findings.append(Finding("Transfers", transfer["transfer_id"], label, FOUND, f"Map {source_id} transfer command(s): {', '.join(matches)}"))
        else:
            findings.append(Finding("Transfers", transfer["transfer_id"], label, MISSING, f"No transfer command from map {source_id} to map {target_id}"))
    return findings


def event_command_codes(event: dict) -> list[int]:
    return [
        int(command.get("code", 0))
        for _, command in iter_page_commands(event)
        if isinstance(command.get("code", 0), int)
    ]


def has_atlas_placeholder_marker(event: dict) -> bool:
    for _, command in iter_page_commands(event):
        if command.get("code") != 356:
            continue
        parameters = command.get("parameters", [])
        if parameters and str(parameters[0]).startswith("AtlasPlaceholder "):
            return True
    return False


def has_executable_commands(event: dict) -> bool:
    non_executable_codes = {0, 108, 408, 401, 402, 404, 411, 412}
    return any(code not in non_executable_codes for code in event_command_codes(event))


def matching_event(map_data: dict, expected_name: str) -> dict | None:
    expected_key = compact_norm(expected_name)
    for event in iter_events(map_data):
        if compact_norm(event.get("name", "")) == expected_key:
            return event
    return None


def audit_executable_event_logic(home: dict, maps: dict[int, dict], screen_maps: dict[str, dict]) -> list[Finding]:
    findings: list[Finding] = []

    for event in home["events"]:
        screen_map = screen_maps.get(event["screen"])
        label = f"{event['screen']} - {event['event']}"
        if not screen_map:
            findings.append(Finding("Executable Event Logic", event["event_id"], label, MISSING, "Source screen map is missing"))
            continue
        map_id = int(screen_map["id"])
        map_data = maps.get(map_id)
        if not map_data:
            findings.append(Finding("Executable Event Logic", event["event_id"], label, MISSING, f"Map{map_id:03d}.json is missing"))
            continue
        found_event = matching_event(map_data, event["event"])
        if not found_event:
            findings.append(Finding("Executable Event Logic", event["event_id"], label, MISSING, f"Event not found on map {map_id}"))
            continue
        if has_atlas_placeholder_marker(found_event):
            findings.append(Finding("Executable Event Logic", event["event_id"], label, MISSING, "AtlasPlaceholder marker remains"))
            continue
        if not has_executable_commands(found_event):
            findings.append(Finding("Executable Event Logic", event["event_id"], label, MISSING, "Event has no executable command codes"))
            continue
        codes = sorted(set(event_command_codes(found_event)))
        findings.append(Finding("Executable Event Logic", event["event_id"], label, FOUND, f"Executable command codes: {', '.join(str(code) for code in codes)}"))

    for transfer in home["transfers"]:
        source = screen_maps.get(transfer["from"])
        target = screen_maps.get(transfer["to"])
        external_target_name = EXTERNAL_TRANSFER_TARGETS.get(transfer["to"])
        if target is None and external_target_name:
            for map_id, map_data in maps.items():
                if norm(map_data.get("displayName")) == norm("Journey II Landing Placeholder"):
                    target = {"id": map_id, "name": external_target_name}
                    break
        label = f"{transfer['from']} -> {transfer['to']}"
        if not source:
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, "Source screen map is missing"))
            continue
        if not target:
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, "Target screen map is missing"))
            continue
        source_id = int(source["id"])
        target_id = int(target["id"])
        map_data = maps.get(source_id)
        if not map_data:
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, f"Map{source_id:03d}.json is missing"))
            continue
        expected_name = f"{transfer['transfer_id']} {transfer['notes']}"
        found_event = matching_event(map_data, expected_name)
        if not found_event:
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, f"Transfer event not found on map {source_id}"))
            continue
        if has_atlas_placeholder_marker(found_event):
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, "AtlasPlaceholder marker remains"))
            continue
        transfer_targets = []
        for _, command in iter_page_commands(found_event):
            if command.get("code") != 201:
                continue
            parameters = command.get("parameters", [])
            try:
                transfer_targets.append(int(parameters[1]))
            except (IndexError, TypeError, ValueError):
                continue
        if target_id not in transfer_targets:
            findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, MISSING, f"No executable transfer command to map {target_id}"))
            continue
        findings.append(Finding("Executable Event Logic", transfer["transfer_id"], label, FOUND, f"Executable transfer command to map {target_id}"))

    return findings


def map_layer_values(map_data: dict, layer: int) -> list[int]:
    width = int(map_data.get("width", 0))
    height = int(map_data.get("height", 0))
    data = map_data.get("data", [])
    values = []
    for y in range(height):
        for x in range(width):
            offset = (layer * height + y) * width + x
            if offset < len(data):
                values.append(data[offset])
    return values


def map_tile_value(map_data: dict, layer: int, x: int, y: int) -> int:
    width = int(map_data.get("width", 0))
    height = int(map_data.get("height", 0))
    data = map_data.get("data", [])
    offset = (layer * height + y) * width + x
    if offset < 0 or offset >= len(data):
        return 0
    return int(data[offset] or 0)


def expected_region_ids(requirements: str) -> set[int]:
    return {
        int(match)
        for match in re.findall(r"Region\s+(\d+)", requirements)
        if int(match) > 0
    }


def relevant_events_for_screen(home: dict, screen_id: str) -> set[str]:
    names = {
        event["event"]
        for event in home["events"]
        if event["screen"] == screen_id
    }
    for transfer in home["transfers"]:
        if transfer["from"] == screen_id:
            names.add(f"{transfer['transfer_id']} {transfer['notes']}")
    return names


def audit_map_layout_readiness(home: dict, maps: dict[int, dict], screen_maps: dict[str, dict]) -> list[Finding]:
    findings: list[Finding] = []
    tileset_rows = {row["screen_id"]: row for row in home["tilesets"]}

    for screen in home["screens"]:
        screen_id = screen["screen_id"]
        screen_map = screen_maps.get(screen_id)
        if not screen_map:
            findings.append(Finding("Map Layout Readiness", screen_id, screen["rpg_maker_map_name"], MISSING, "Screen map is missing"))
            continue
        map_id = int(screen_map["id"])
        map_data = maps.get(map_id)
        if not map_data:
            findings.append(Finding("Map Layout Readiness", screen_id, screen["rpg_maker_map_name"], MISSING, f"Map{map_id:03d}.json is missing"))
            continue

        label = f"Map {map_id} - {screen['rpg_maker_map_name']}"
        floor_values = map_layer_values(map_data, 0)
        nonzero_floor = sum(1 for value in floor_values if value)
        if nonzero_floor:
            findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, f"Base terrain tiles painted: {nonzero_floor}"))
        else:
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, "No base terrain tiles painted"))

        tile_row = tileset_rows.get(screen_id, {})
        regions = {value for value in map_layer_values(map_data, 5) if value}
        required_regions = expected_region_ids(tile_row.get("region_id_requirements", ""))
        if "Region 0 only" in tile_row.get("region_id_requirements", ""):
            if regions:
                findings.append(Finding("Map Layout Readiness", screen_id, label, WARNING, f"Expected Region 0 only, found nonzero region IDs: {sorted(regions)}"))
            else:
                findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, "Region 0 only as expected"))
        elif required_regions.issubset(regions):
            findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, f"Required region IDs present: {sorted(required_regions)}"))
        else:
            missing_regions = sorted(required_regions - regions)
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, f"Missing region ID(s): {missing_regions}"))

        encounter_note = tile_row.get("encounter_zone_requirements", "")
        encounters = map_data.get("encounterList", [])
        if ("None" in encounter_note or "No random encounters" in encounter_note) and "Optional" not in encounter_note and encounters:
            findings.append(Finding("Map Layout Readiness", screen_id, label, WARNING, "Atlas marks this as encounter-free, but encounterList is populated"))
        elif "No random encounters" in encounter_note and not encounters:
            findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, "Random encounter policy is satisfied"))
        elif any(token in encounter_note for token in ("Troop", "troops", "encounters")) and "None" not in encounter_note:
            if encounters:
                troop_ids = sorted({row.get("troopId") for row in encounters if isinstance(row, dict)})
                findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, f"Encounter list populated with troop id(s): {troop_ids}"))
            else:
                findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, "Atlas allows or expects encounters, but encounterList is empty"))
        else:
            findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, "Encounter policy is satisfied"))

        expected_names = relevant_events_for_screen(home, screen_id)
        placed_events = [
            event
            for event in iter_events(map_data)
            if event.get("name") in expected_names
        ]
        if not expected_names:
            findings.append(Finding("Map Layout Readiness", screen_id, label, UNKNOWN, "No Atlas events or outgoing transfers on this screen"))
            continue
        if len(placed_events) != len(expected_names):
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, f"Expected {len(expected_names)} relevant events, found {len(placed_events)}"))
            continue
        if len(placed_events) > 2 and all(event.get("y") == 1 for event in placed_events):
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, "Events still appear in the generated placeholder row"))
            continue
        out_of_bounds = [
            event.get("name")
            for event in placed_events
            if not (0 <= int(event.get("x", -1)) < int(map_data["width"]) and 0 <= int(event.get("y", -1)) < int(map_data["height"]))
        ]
        if out_of_bounds:
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, f"Event(s) out of bounds: {out_of_bounds}"))
        elif any(map_tile_value(map_data, 0, int(event["x"]), int(event["y"])) in {1536, 2048} for event in placed_events):
            blocked = [
                event.get("name")
                for event in placed_events
                if map_tile_value(map_data, 0, int(event["x"]), int(event["y"])) in {1536, 2048}
            ]
            findings.append(Finding("Map Layout Readiness", screen_id, label, MISSING, f"Event tile(s) use blocked placeholder terrain: {blocked}"))
        else:
            coords = sorted({(event.get("x"), event.get("y")) for event in placed_events})
            findings.append(Finding("Map Layout Readiness", screen_id, label, FOUND, f"Relevant events placed on {len(coords)} coordinate(s)"))

    return findings


def audit_trial_state(home: dict, system: dict) -> list[Finding]:
    findings: list[Finding] = []
    switch_names = {norm(name): index for index, name in enumerate(system.get("switches", [])) if name}
    variable_names = {norm(name): index for index, name in enumerate(system.get("variables", [])) if name}
    for switch in home["trial_mechanics"]["switches"]:
        index = switch_names.get(norm(switch))
        if index is None:
            findings.append(Finding("Trial State", switch, switch, MISSING, "Switch name not found in System.json"))
        else:
            findings.append(Finding("Trial State", switch, switch, FOUND, f"System.json switch {index}"))
    for variable in home["trial_mechanics"]["variables"]:
        index = variable_names.get(norm(variable))
        if index is None:
            findings.append(Finding("Trial State", variable, variable, MISSING, "Variable name not found in System.json"))
        else:
            findings.append(Finding("Trial State", variable, variable, FOUND, f"System.json variable {index}"))
    return findings


def audit_common_events(home: dict, common_events: list) -> list[Finding]:
    findings: list[Finding] = []
    named_events = [
        row
        for row in common_events
        if isinstance(row, dict) and row.get("name")
    ]
    for candidate in home["common_event_candidates"]:
        expected_name = candidate["name"]
        expected_keys = {compact_norm(expected_name), compact_norm(candidate["candidate_id"])}
        matches = [
            row
            for row in named_events
            if any(expected_key in compact_norm(row.get("name", "")) for expected_key in expected_keys)
        ]
        label = f"{candidate['candidate_id']} - {expected_name}"
        if matches:
            ids = ", ".join(str(row.get("id")) for row in matches)
            findings.append(Finding("Common Events", candidate["candidate_id"], label, FOUND, f"CommonEvents.json id(s): {ids}"))
        else:
            findings.append(Finding("Common Events", candidate["candidate_id"], label, MISSING, "No common event with matching name"))
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
            "CommonEvents.json",
        }
    }
    screen_maps = map_info_by_screen(home, data_files["MapInfos.json"])
    maps = load_maps(data_dir, data_files["MapInfos.json"])

    findings: list[Finding] = []
    findings.extend(audit_maps(home, data_files["MapInfos.json"]))
    findings.extend(audit_database_allocation(home, data_files))
    findings.extend(audit_skill_details(home, data_files["Skills.json"]))
    findings.extend(audit_troop_details(home, data_files["Troops.json"]))
    findings.extend(audit_troop_event_pages(home, data_files["Troops.json"]))
    findings.extend(audit_tilesets(home, data_files["Tilesets.json"]))
    findings.extend(audit_animations(home, data_files["Animations.json"]))
    findings.extend(audit_common_events(home, data_files["CommonEvents.json"]))
    findings.extend(audit_trial_state(home, data_files["System.json"]))
    findings.extend(audit_atlas_events(home, maps, screen_maps))
    findings.extend(audit_transfers(home, maps, screen_maps))
    findings.extend(audit_executable_event_logic(home, maps, screen_maps))
    findings.extend(audit_map_layout_readiness(home, maps, screen_maps))
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
            "- `not machine-checkable yet` is reserved for export expectations that explicitly do not map to an RPG Maker database row, such as `Animation None`.",
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
