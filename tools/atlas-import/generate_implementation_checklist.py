#!/usr/bin/env python3
"""Generate a read-only RPG Maker implementation checklist from an Atlas export."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "reports" / "atlas-import" / "home-island-implementation-checklist.md"


def load_export(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Atlas export not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in Atlas export: {error}")


def checkbox(text: str) -> str:
    return f"- [ ] {text}"


def val(row: dict, key: str, default: str = "TBD") -> str:
    value = row.get(key)
    return str(value) if value not in (None, "") else default


def render_header(payload: dict) -> list[str]:
    source = payload.get("source", {})
    readiness = payload["home_island"].get("production_readiness", {})
    return [
        "# Home Island RPG Maker Implementation Checklist",
        "",
        "Generated from the Atlas Home Island export.",
        "",
        "## Export Metadata",
        "",
        f"- Export: `{payload.get('export_name')}`",
        f"- Schema: `{payload.get('schema_version')}`",
        f"- Generated: `{payload.get('generated_at')}`",
        f"- Source repo: `{source.get('repository')}`",
        f"- Source commit: `{source.get('git_commit')}`",
        f"- Source branch: `{source.get('git_branch')}`",
        f"- Production decision: `{readiness.get('decision')}`",
        "",
        "## Read-Only Rule",
        "",
        "This checklist is generated from Atlas. It does not modify RPG Maker JSON, maps, events, assets, or project settings.",
        "",
    ]


def render_maps(home: dict) -> list[str]:
    lines = ["## Map / Screen Checklist", ""]
    tilesets = {row["screen_id"]: row for row in home["tilesets"]}
    for screen in home["screens"]:
        tile = tilesets.get(screen["screen_id"], {})
        lines.extend(
            [
                checkbox(
                    f"`{screen['screen_id']}` `{screen['rpg_maker_map_name']}` - "
                    f"{screen['screen']} using tileset `{val(tile, 'placeholder_tileset')}`"
                ),
                f"  - Location: `{screen['location']}`",
                f"  - Implementation packet: `{screen['implementation_packet']}`",
                f"  - Terrain: {val(tile, 'required_terrain_types')}",
                f"  - Passability: {val(tile, 'passability_needs')}",
                f"  - Regions: {val(tile, 'region_id_requirements')}",
                f"  - Encounter zones: {val(tile, 'encounter_zone_requirements')}",
                f"  - Placement notes: {val(tile, 'transfer_event_placement_notes')}",
            ]
        )
    lines.append("")
    return lines


def render_transfers(home: dict) -> list[str]:
    lines = ["## Transfer Event Checklist", ""]
    for transfer in home["transfers"]:
        lines.append(
            checkbox(
                f"`{transfer['transfer_id']}` from `{transfer['from']}` to `{transfer['to']}` "
                f"when `{transfer['condition']}` - {transfer['notes']}"
            )
        )
    lines.append("")
    return lines


def render_events(home: dict) -> list[str]:
    lines = ["## Atlas Event Checklist", ""]
    for event in home["events"]:
        lines.append(
            checkbox(
                f"`{event['event_id']}` on `{event['screen']}` - {event['event']} "
                f"({event['required_state_result']})"
            )
        )
    if home["common_event_candidates"]:
        lines.extend(["", "### Common Event Candidates", ""])
        for event in home["common_event_candidates"]:
            lines.append(checkbox(f"`{event['candidate_id']}` - {event['name']}: {event['purpose']}"))
    lines.append("")
    return lines


def render_combat(home: dict) -> list[str]:
    combat = home["combat_database"]
    lines = ["## Combat Database Checklist", "", "### Database Allocation", ""]
    for row in combat["database_id_allocation"]:
        lines.append(
            checkbox(
                f"{row['database']} `{row['id']}` - {row['name']} "
                f"(Atlas: `{row['atlas_source']}`; {row['notes']})"
            )
        )
    lines.extend(["", "### Skills", ""])
    for row in combat["skills"]:
        lines.append(
            checkbox(
                f"Skill `{row['skill_id']}` {row['name']} - animation `{row['animation']}`, "
                f"formula/effects: {row['formula']} / {row['effects']}"
            )
        )
    lines.extend(["", "### Troops", ""])
    for row in combat["troops"]:
        if "name" in row:
            lines.append(checkbox(f"Troop `{row['troop_id']}` {row['name']} - {row['members']}"))
        else:
            lines.append(
                checkbox(
                    f"Troop event page `{row['troop_id']}` page `{val(row, 'page')}` - "
                    f"{val(row, 'condition')}: {val(row, 'commands')}"
                )
            )
    lines.extend(["", "### Encounter Placement", ""])
    for row in combat["encounter_placement"]:
        lines.append(checkbox(f"{row['atlas_screen_group']} - {row['troops']}"))
    lines.append("")
    return lines


def render_trials(home: dict) -> list[str]:
    trial = home["trial_mechanics"]
    lines = ["## Trial Mechanics Checklist", ""]
    lines.append(f"Source: `{trial['source']}`")
    lines.append("")
    for event_id in trial["event_ids"]:
        lines.append(checkbox(f"Implement trial event/gate `{event_id}` from Atlas trial mechanics"))
    for switch in trial["switches"]:
        lines.append(checkbox(f"Create or verify switch `{switch}`"))
    for variable in trial["variables"]:
        lines.append(checkbox(f"Create or verify variable `{variable}`"))
    lines.append("")
    return lines


def render_animations(home: dict) -> list[str]:
    animations = home["animations"]
    lines = ["## Animation Assignment Checklist", "", "### Core Animation IDs", ""]
    for row in animations["core_animation_ids"]:
        lines.append(checkbox(f"Animation `{row['animation_id']}` {row['animation_name']} - {row['approved_use']}"))
    lines.extend(["", "### Combat Animation Beats", ""])
    for row in animations["combat_animation_matrix"]:
        lines.append(
            checkbox(
                f"{row['beat']} - animation `{row['rpg_maker_animation_id']}` "
                f"{row['animation_name']} ({row['use_case']})"
            )
        )
    lines.extend(["", "### Story / Event Animation Beats", ""])
    for row in animations["story_event_animation_matrix"]:
        lines.append(
            checkbox(
                f"{row['beat']} - animation `{row['rpg_maker_animation_id']}` "
                f"{row['animation_name']} ({row['use_case']})"
            )
        )
    lines.append("")
    return lines


def render_report_prompts() -> list[str]:
    return [
        "## Implementation Report Prompts",
        "",
        "- [ ] List Atlas IDs implemented.",
        "- [ ] List RPG Maker maps created or modified.",
        "- [ ] List RPG Maker database rows created or modified.",
        "- [ ] List transfer IDs implemented.",
        "- [ ] List event IDs implemented.",
        "- [ ] List placeholder assets used.",
        "- [ ] List playtest route covered.",
        "- [ ] List blockers, defects, or Atlas gaps discovered.",
        "- [ ] Confirm no implementation-only design decisions were made without Atlas follow-up.",
        "",
    ]


def render(payload: dict) -> str:
    home = payload["home_island"]
    lines: list[str] = []
    lines.extend(render_header(payload))
    lines.extend(render_maps(home))
    lines.extend(render_transfers(home))
    lines.extend(render_events(home))
    lines.extend(render_combat(home))
    lines.extend(render_trials(home))
    lines.extend(render_animations(home))
    lines.extend(render_report_prompts())
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print(
            "Usage: python tools/atlas-import/generate_implementation_checklist.py "
            "<atlas-export.json> [output.md]",
            file=sys.stderr,
        )
        return 1

    export_path = Path(sys.argv[1]).expanduser().resolve()
    output_path = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) == 3 else DEFAULT_OUTPUT
    payload = load_export(export_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render(payload), encoding="utf-8")
    print(output_path.relative_to(ROOT).as_posix() if output_path.is_relative_to(ROOT) else output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
