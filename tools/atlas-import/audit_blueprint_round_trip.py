#!/usr/bin/env python3
"""Read-only audit comparing an Atlas map blueprint to generated RPG Maker data."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ATLAS_ROOT = ROOT.parent / "TheLastSwordProtocol-Atlas"
DEFAULT_PROJECT_ROOT = ROOT.parent / "TheLastSwordProtocol-Game"
DEFAULT_BLUEPRINT = DEFAULT_ATLAS_ROOT / "atlas-tools" / "mapgen" / "prototype" / "SCR-HOM-ASH-001.blueprint.json"
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "build-0010-blueprint-round-trip-audit.md"
GENERATOR_PATH = ROOT / "tools" / "atlas-import" / "generate_map_from_blueprint.py"

FOUND = "found"
MISSING = "missing"
WARNING = "present with warning"


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
    parser.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT), help="Atlas blueprint JSON path.")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT), help="RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Required JSON file not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {path}: {error}")


def load_generator_module():
    spec = importlib.util.spec_from_file_location("atlas_map_generator", GENERATOR_PATH)
    if not spec or not spec.loader:
        raise SystemExit(f"Could not load generator module: {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tile_index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def tile_value(map_data: dict[str, Any], x: int, y: int, z: int) -> int | None:
    if not (0 <= x < map_data["width"] and 0 <= y < map_data["height"]):
        return None
    index = tile_index(map_data["width"], map_data["height"], x, y, z)
    if index >= len(map_data.get("data", [])):
        return None
    return map_data["data"][index]


def anchor_point(anchor: dict[str, Any]) -> tuple[int, int]:
    if anchor["shape"] == "point":
        return int(anchor["x"]), int(anchor["y"])
    if anchor["shape"] == "rect":
        return int(anchor["x"] + anchor["w"] // 2), int(anchor["y"] + anchor["h"] // 2)
    raise SystemExit(f"Unsupported anchor shape: {anchor['shape']}")


def iter_events(map_data: dict[str, Any]):
    for event in map_data.get("events", []):
        if isinstance(event, dict):
            yield event


def iter_commands(event: dict[str, Any]):
    for page in event.get("pages", []):
        for command in page.get("list", []):
            if isinstance(command, dict):
                yield command


def command_text(command: dict[str, Any]) -> str:
    parameters = command.get("parameters", [])
    return " ".join(str(value) for value in parameters)


def event_contains_atlas_id(event: dict[str, Any], atlas_id: str) -> bool:
    if atlas_id in str(event.get("name", "")) or atlas_id in str(event.get("note", "")):
        return True
    for command in iter_commands(event):
        if command.get("code") in {108, 408} and atlas_id in command_text(command):
            return True
    return False


def event_by_name(map_data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {event.get("name", ""): event for event in iter_events(map_data)}


def finding(findings: list[Finding], category: str, check_id: str, expected: str, predicate: bool, detail: str, warning: bool = False) -> None:
    status = FOUND if predicate else (WARNING if warning else MISSING)
    findings.append(Finding(category, check_id, expected, status, detail if predicate else f"Expected {detail}"))


def target_map_id(project_root: Path, blueprint: dict[str, Any], generator) -> int:
    map_name = generator.SCREEN_TO_MAP_NAME.get(blueprint["atlas_screen_id"])
    if not map_name:
        raise SystemExit(f"No generator map-name mapping for {blueprint['atlas_screen_id']}")
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    matches = [entry for entry in map_infos if isinstance(entry, dict) and entry.get("name") == map_name]
    if len(matches) != 1:
        raise SystemExit(f"Expected one MapInfos entry named {map_name}, found {len(matches)}")
    return int(matches[0]["id"])


def expected_anchor_events(blueprint: dict[str, Any], generator) -> list[tuple[str, str, tuple[int, int], str]]:
    rows: list[tuple[str, str, tuple[int, int], str]] = []
    for transfer in blueprint.get("transfer_points", []):
        atlas_id = transfer["transfer_id"]
        rows.append(("Transfer Anchors", atlas_id, anchor_point(transfer["anchor"]), generator.TRANSFER_EVENT_NAMES.get(atlas_id, atlas_id)))
    for npc in blueprint.get("npc_spawns", []):
        atlas_id = npc.get("event_id") or npc.get("local_anchor_id")
        rows.append(("NPC Anchors", atlas_id, anchor_point(npc["anchor"]), generator.NPC_EVENT_NAMES.get(atlas_id, npc["npc_role"])))
    for treasure in blueprint.get("treasure_locations", []):
        atlas_id = treasure["event_id"]
        rows.append(("Treasure Anchors", atlas_id, anchor_point(treasure["anchor"]), generator.TREASURE_EVENT_NAMES.get(atlas_id, atlas_id)))
    for anchor in blueprint.get("event_anchors", []):
        atlas_id = anchor.get("event_id") or anchor.get("local_anchor_id")
        rows.append(("Event Anchors", atlas_id, anchor_point(anchor["anchor"]), generator.ANCHOR_EVENT_NAMES.get(atlas_id, anchor.get("event_name", atlas_id))))
    return rows


def audit_map_shape(blueprint: dict[str, Any], map_data: dict[str, Any], map_id: int, map_path: Path) -> list[Finding]:
    findings: list[Finding] = []
    width = int(blueprint["dimensions"]["width"])
    height = int(blueprint["dimensions"]["height"])
    finding(findings, "Map Shape", "MAP-001", "RPG Maker target map exists", map_path.exists(), str(map_path))
    finding(findings, "Map Shape", "MAP-002", f"Map ID {map_id}", True, f"map_id={map_id}")
    finding(findings, "Map Shape", "MAP-003", f"Width {width}", map_data.get("width") == width, f"width={map_data.get('width')}")
    finding(findings, "Map Shape", "MAP-004", f"Height {height}", map_data.get("height") == height, f"height={map_data.get('height')}")
    finding(findings, "Map Shape", "MAP-005", "Six RPG Maker tile layers", len(map_data.get("data", [])) == width * height * 6, f"data length={len(map_data.get('data', []))}")
    finding(findings, "Map Shape", "MAP-006", f"Display name {blueprint['title']}", map_data.get("displayName") == blueprint["title"], f"displayName={map_data.get('displayName')}")
    finding(findings, "Map Shape", "MAP-007", "Blueprint generation marker", blueprint["blueprint_id"] in str(map_data.get("note", "")), f"note contains {blueprint['blueprint_id']}")
    return findings


def audit_event_anchors(blueprint: dict[str, Any], map_data: dict[str, Any], generator) -> list[Finding]:
    findings: list[Finding] = []
    events = event_by_name(map_data)
    for category, atlas_id, (x, y), name in expected_anchor_events(blueprint, generator):
        event = events.get(name)
        finding(findings, category, atlas_id, f"Event `{name}` exists", event is not None, "event exists")
        if not event:
            continue
        finding(findings, category, f"{atlas_id}-POS", f"`{name}` at ({x}, {y})", event.get("x") == x and event.get("y") == y, f"actual=({event.get('x')}, {event.get('y')})")
        finding(findings, category, f"{atlas_id}-TRACE", f"`{name}` preserves {atlas_id}", event_contains_atlas_id(event, atlas_id), "Atlas ID present in name, note, or comments")
        ground = tile_value(map_data, x, y, 0)
        finding(findings, category, f"{atlas_id}-TILE", f"`{name}` has a concrete tile", ground not in {None, 0}, f"layer0 tile={ground}")
    return findings


def audit_region_policy(blueprint: dict[str, Any], map_data: dict[str, Any], generator) -> list[Finding]:
    findings: list[Finding] = []
    safe_regions = [region for region in blueprint.get("enemy_regions", []) if region.get("region_type") == "safe"]
    encounter_regions = [
        region
        for region in blueprint.get("enemy_regions", [])
        if region.get("region_type") in generator.REGION_EXPORT_IDS and region.get("region_type") != "safe"
    ]
    expected_encounters = generator.ENCOUNTER_POLICIES.get(blueprint["atlas_screen_id"], [])
    finding(findings, "Encounter Policy", "ENC-001", "Blueprint declares region policy", bool(safe_regions or encounter_regions), f"safe={len(safe_regions)} encounter={len(encounter_regions)}")
    finding(findings, "Encounter Policy", "ENC-002", "RPG Maker encounter list matches exporter policy", map_data.get("encounterList") == expected_encounters, f"encounterList={map_data.get('encounterList')}")
    width = map_data["width"]
    height = map_data["height"]
    region_values = Counter(tile_value(map_data, x, y, 5) for y in range(height) for x in range(width))
    nonzero_regions = sorted(value for value in region_values if value not in {None, 0})
    expected_types = set()
    for region in encounter_regions:
        expected_types.add(region.get("region_type"))
    if safe_regions and (encounter_regions or generator.should_export_safe_regions(blueprint)):
        expected_types.add("safe")
    expected_region_ids = sorted(generator.REGION_EXPORT_IDS[region_type] for region_type in expected_types)
    finding(findings, "Encounter Policy", "ENC-003", "RPG Maker region IDs match blueprint region types", nonzero_regions == expected_region_ids, f"nonzero region IDs={nonzero_regions}")
    return findings


def audit_blueprint_engine_independence(blueprint: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    serialized = json.dumps(blueprint)
    forbidden_keys = ["mapId", "map_id", "tilesetId", "tileset_id", "animationId", "animation_id", "eventId", "event_id_rpg"]
    leaked = [key for key in forbidden_keys if key in serialized]
    finding(findings, "Blueprint Contract", "BP-001", "Blueprint has Atlas screen ID", bool(blueprint.get("atlas_screen_id")), f"atlas_screen_id={blueprint.get('atlas_screen_id')}")
    finding(findings, "Blueprint Contract", "BP-002", "Blueprint contains no RPG Maker engine IDs", leaked == [], f"engine-specific keys={leaked}")
    finding(findings, "Blueprint Contract", "BP-003", "Blueprint source documents are recorded", bool(blueprint.get("source_documents")), f"source_documents={len(blueprint.get('source_documents', []))}")
    return findings


def status_counts(findings: list[Finding]) -> Counter:
    return Counter(finding.status for finding in findings)


def grouped_counts(findings: list[Finding]) -> dict[str, Counter]:
    counts: dict[str, Counter] = defaultdict(Counter)
    for item in findings:
        counts[item.category][item.status] += 1
    return counts


def render_table(findings: list[Finding]) -> list[str]:
    lines = ["| Status | Category | Check ID | Expected | Detail |", "|---|---|---|---|---|"]
    for item in findings:
        lines.append(f"| {item.status} | {item.category} | `{item.check_id}` | {item.expected} | {item.detail} |")
    return lines


def write_report(output: Path, blueprint_path: Path, project_root: Path, map_path: Path, findings: list[Finding]) -> None:
    counts = status_counts(findings)
    grouped = grouped_counts(findings)
    lines = [
        "# Atlas Blueprint Round-Trip Audit",
        "",
        "This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.",
        "",
        f"- Blueprint: `{blueprint_path}`",
        f"- Project root: `{project_root}`",
        f"- RPG Maker map: `{map_path}`",
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
        category_counts = grouped[category]
        lines.append(f"| {category} | {category_counts[FOUND]} | {category_counts[MISSING]} | {category_counts[WARNING]} |")
    lines.extend(["", "## Findings", ""])
    lines.extend(render_table(findings))
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This audit does not modify RPG Maker data files.",
            "- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.",
            "- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.",
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    output = Path(args.output).expanduser().resolve()
    blueprint_path = Path(args.blueprint).expanduser().resolve()
    project_root = Path(args.project_root).expanduser().resolve()
    generator = load_generator_module()
    blueprint = load_json(blueprint_path)
    map_id = target_map_id(project_root, blueprint, generator)
    map_path = project_root / "data" / f"Map{map_id:03d}.json"
    map_data = load_json(map_path)

    findings: list[Finding] = []
    findings.extend(audit_blueprint_engine_independence(blueprint))
    findings.extend(audit_map_shape(blueprint, map_data, map_id, map_path))
    findings.extend(audit_event_anchors(blueprint, map_data, generator))
    findings.extend(audit_region_policy(blueprint, map_data, generator))
    write_report(output, blueprint_path, project_root, map_path, findings)

    counts = status_counts(findings)
    print(output)
    print(f"found={counts[FOUND]} missing={counts[MISSING]} warning={counts[WARNING]}")
    return 1 if counts[MISSING] or counts[WARNING] else 0


if __name__ == "__main__":
    raise SystemExit(main())
