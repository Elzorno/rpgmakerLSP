#!/usr/bin/env python3
"""Read-only validator for Atlas Home Island export JSON."""

from __future__ import annotations

import json
from pathlib import Path
import sys


EXPECTED_SCHEMA_VERSION = "1.0.0"
REQUIRED_TOP_LEVEL = {
    "schema_version",
    "export_name",
    "generated_at",
    "source",
    "contract",
    "home_island",
}
REQUIRED_HOME_ISLAND = {
    "screens",
    "transfers",
    "events",
    "common_event_candidates",
    "combat_database",
    "trial_mechanics",
    "tilesets",
    "animations",
    "production_readiness",
}
REQUIRED_COMBAT = {
    "database_id_allocation",
    "skills",
    "troops",
    "encounter_placement",
}
REQUIRED_ANIMATIONS = {
    "core_animation_ids",
    "combat_animation_matrix",
    "story_event_animation_matrix",
}


def load_export(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Atlas export not found: {path}")
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in Atlas export: {error}")


def require_keys(label: str, data: dict, keys: set[str], errors: list[str]) -> None:
    missing = sorted(keys - set(data))
    if missing:
        errors.append(f"{label} missing keys: {', '.join(missing)}")


def require_nonempty(label: str, value: object, errors: list[str]) -> None:
    if not value:
        errors.append(f"{label} is empty")


def validate(payload: dict) -> list[str]:
    errors: list[str] = []

    require_keys("export", payload, REQUIRED_TOP_LEVEL, errors)

    if payload.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        errors.append(
            f"unsupported schema_version {payload.get('schema_version')!r}; "
            f"expected {EXPECTED_SCHEMA_VERSION!r}"
        )

    if payload.get("export_name") != "home-island":
        errors.append(f"unsupported export_name {payload.get('export_name')!r}; expected 'home-island'")

    if payload.get("contract", {}).get("read_only_import") is not True:
        errors.append("contract.read_only_import must be true for WO-0018")

    home_island = payload.get("home_island", {})
    if not isinstance(home_island, dict):
        errors.append("home_island must be an object")
        return errors

    require_keys("home_island", home_island, REQUIRED_HOME_ISLAND, errors)

    for key in ("screens", "transfers", "events", "tilesets"):
        require_nonempty(f"home_island.{key}", home_island.get(key), errors)

    combat = home_island.get("combat_database", {})
    if isinstance(combat, dict):
        require_keys("home_island.combat_database", combat, REQUIRED_COMBAT, errors)
        for key in REQUIRED_COMBAT:
            require_nonempty(f"home_island.combat_database.{key}", combat.get(key), errors)
    else:
        errors.append("home_island.combat_database must be an object")

    trial = home_island.get("trial_mechanics", {})
    if isinstance(trial, dict):
        for key in ("source", "event_ids", "switches", "variables"):
            require_nonempty(f"home_island.trial_mechanics.{key}", trial.get(key), errors)
    else:
        errors.append("home_island.trial_mechanics must be an object")

    animations = home_island.get("animations", {})
    if isinstance(animations, dict):
        require_keys("home_island.animations", animations, REQUIRED_ANIMATIONS, errors)
        for key in REQUIRED_ANIMATIONS:
            require_nonempty(f"home_island.animations.{key}", animations.get(key), errors)
    else:
        errors.append("home_island.animations must be an object")

    decision = home_island.get("production_readiness", {}).get("decision")
    if not decision or not str(decision).startswith("GO"):
        errors.append(f"production readiness decision is not GO-class: {decision!r}")

    return errors


def summarize(payload: dict) -> str:
    home = payload["home_island"]
    combat = home["combat_database"]
    animations = home["animations"]

    lines = [
        "# Atlas Export Import Validation",
        "",
        "Result: PASS",
        "",
        "## Export",
        "",
        f"- Name: {payload['export_name']}",
        f"- Schema: {payload['schema_version']}",
        f"- Generated: {payload['generated_at']}",
        f"- Source repo: {payload['source'].get('repository')}",
        f"- Source commit: {payload['source'].get('git_commit')}",
        "",
        "## Expected RPG Maker Resources",
        "",
        f"- Maps/screens: {len(home['screens'])}",
        f"- Transfer events: {len(home['transfers'])}",
        f"- Atlas events: {len(home['events'])}",
        f"- Common event candidates: {len(home['common_event_candidates'])}",
        f"- Database allocation rows: {len(combat['database_id_allocation'])}",
        f"- Skill rows: {len(combat['skills'])}",
        f"- Troop rows: {len(combat['troops'])}",
        f"- Tileset assignments: {len(home['tilesets'])}",
        f"- Core animation IDs: {len(animations['core_animation_ids'])}",
        f"- Combat animation beats: {len(animations['combat_animation_matrix'])}",
        f"- Story/event animation beats: {len(animations['story_event_animation_matrix'])}",
        "",
        "## Read-Only Contract",
        "",
        "- This validator did not modify RPG Maker data files.",
        "- Future import/apply tooling must be authorized by a separate work order.",
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/atlas-import/validate_atlas_export.py <atlas-export.json>", file=sys.stderr)
        return 1

    path = Path(sys.argv[1]).expanduser().resolve()
    payload = load_export(path)
    errors = validate(payload)

    if errors:
        print("# Atlas Export Import Validation")
        print()
        print("Result: FAIL")
        print()
        for error in errors:
            print(f"- {error}")
        return 1

    print(summarize(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
