#!/usr/bin/env python3
"""Map ownership ledger guard for write-capable atlas-import scripts (WO-0031).

The clean game project carries a per-map ownership ledger at
`<project_root>/map_ownership.json`. Write-capable pipeline scripts must
consult it before writing any `data/MapXXX.json` and may only write maps
whose state is `generated`.

Fail-safe rules:
- Missing or unreadable ledger -> NO map writes are permitted.
- Map id not listed in the ledger -> that map is NOT writable.
- Any entry with an unknown state invalidates the ledger entirely.
"""

from __future__ import annotations

import json
from pathlib import Path

LEDGER_FILENAME = "map_ownership.json"
WRITABLE_STATE = "generated"
VALID_STATES = {"generated", "hand_authored", "locked"}


def load_ledger(project_root: Path) -> dict[int, str] | None:
    """Return {map_id: state} from the project ledger, or None when the ledger
    is missing, unreadable, or malformed. None means no map writes are allowed."""
    path = Path(project_root) / LEDGER_FILENAME
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        entries = payload["maps"]
        ledger: dict[int, str] = {}
        for key, entry in entries.items():
            state = str(entry.get("state", "")).strip()
            if state not in VALID_STATES:
                return None
            ledger[int(key)] = state
        return ledger
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None


def map_write_allowed(ledger: dict[int, str] | None, map_id: int) -> bool:
    if ledger is None:
        return False
    return ledger.get(int(map_id)) == WRITABLE_STATE


def skip_message(ledger: dict[int, str] | None, map_id: int, script_name: str) -> str:
    map_label = f"Map{int(map_id):03d}"
    if ledger is None:
        return (
            f"OWNERSHIP GUARD: {script_name} refused to write {map_label}: "
            f"{LEDGER_FILENAME} is missing or unreadable (fail safe: no ledger, no writes)."
        )
    state = ledger.get(int(map_id))
    if state is None:
        return (
            f"OWNERSHIP GUARD: {script_name} skipped {map_label}: "
            f"not listed in {LEDGER_FILENAME} (fail safe: unlisted maps are not writable)."
        )
    return (
        f"OWNERSHIP GUARD: {script_name} skipped {map_label}: "
        f"ledger state is '{state}'; only '{WRITABLE_STATE}' maps may be written."
    )


def register_generated_map(project_root: Path, map_id: int, name: str = "") -> bool:
    """Record a newly pipeline-created map as 'generated' in the ledger.

    Returns True when the map may be created (already listed as generated, or
    successfully registered). Returns False when the ledger is missing or
    unreadable, or the map is listed with a non-generated state (fail safe:
    the caller must not create/write the map)."""
    path = Path(project_root) / LEDGER_FILENAME
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        entries = payload["maps"]
        key = str(int(map_id))
        if key in entries:
            return str(entries[key].get("state", "")).strip() == WRITABLE_STATE
        entries[key] = {"state": WRITABLE_STATE, "atlas_screen": None, "name": name}
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(
            f"OWNERSHIP GUARD: registered new pipeline-created Map{int(map_id):03d} "
            f"as '{WRITABLE_STATE}' in {LEDGER_FILENAME}."
        )
        return True
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return False


def filter_writable(
    ledger: dict[int, str] | None, map_ids, script_name: str
) -> tuple[list[int], list[str]]:
    """Split map_ids into (writable, skip_messages), preserving order."""
    writable: list[int] = []
    messages: list[str] = []
    for map_id in map_ids:
        if map_write_allowed(ledger, map_id):
            writable.append(int(map_id))
        else:
            messages.append(skip_message(ledger, map_id, script_name))
    return writable, messages
