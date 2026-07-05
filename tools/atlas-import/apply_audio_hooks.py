#!/usr/bin/env python3
"""Apply first-playable Home Island placeholder audio hooks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from map_ownership_guard import load_ledger, map_write_allowed, skip_message


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

MAP_AUDIO = {
    1: {"bgm": "Town1"},
    2: {"bgm": "Town1"},
    3: {"bgm": "Town1"},
    4: {"bgm": "Field3", "bgs": "Wind4"},
    5: {"bgm": "Dungeon2", "bgs": "Drips"},
    6: {"bgm": "Dungeon2", "bgs": "Drips"},
    7: {"bgs": "Darkness"},
    8: {"bgm": "Dungeon3", "bgs": "Wind4"},
    9: {"bgm": "Dungeon6", "bgs": "Darkness"},
    10: {"bgm": "Dungeon6", "bgs": "Darkness"},
    11: {"bgm": "Dungeon5", "bgs": "Darkness"},
    12: {"bgm": "Dungeon6", "bgs": "Darkness"},
    13: {"bgm": "Ship1", "bgs": "Sea"},
    14: {"bgm": "Scene2", "bgs": "Wave1"},
    15: {"bgm": "Field2", "bgs": "River"},
    16: {"bgm": "Field2", "bgs": "River"},
    50: {"bgm": "Scene2"},
}

EVENT_SE = {
    "Hidden Item": "Item3",
    "Tremor Trigger": "Earth4",
    "Body Trial": "Chime2",
    "Mind Trial": "Chime2",
    "Heart Trial": "Chime2",
    "Sword Pedestal": "Flash2",
    "Glassfield Seal": "Barrier",
    "Surface Fragment": "Computer",
    "Core Path Door": "Open4",
    "Node Seven Guardian": "Battle1",
    "Relay Core": "Computer",
    "Lighthouse Examine": "Bell3",
    "Departure Sequence": "Decision3",
    "Hidden Item Landmark": "Item3",
    "Signal-Tick Reed Pool": "Computer",
    "Signal Pool / Cable Cluster Examine": "Computer",
}

COMMON_EVENT_SE = {
    1: ("CE_Archive_Message_Display", "Computer"),
    2: ("CE_Sword_Authentication", "Flash2"),
    3: ("CE_Relay_Resolution", "Computer"),
    5: ("CE_Trial_Complete_Chime", "Chime2"),
    6: ("CE_Trial_Reset_Feedback", "Buzzer2"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="Clean RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def audio(name: str = "", volume: int = 90, pitch: int = 100, pan: int = 0) -> dict:
    return {"name": name, "pan": pan, "pitch": pitch, "volume": volume}


def play_se(name: str, indent: int = 0, volume: int = 90) -> dict:
    return {"code": 250, "indent": indent, "parameters": [audio(name, volume)]}


def comment(text: str) -> dict:
    return {"code": 108, "indent": 0, "parameters": [text]}


def empty_command() -> dict:
    return {"code": 0, "indent": 0, "parameters": []}


def ensure_audio_files(project_root: Path) -> None:
    for map_audio in MAP_AUDIO.values():
        for folder, key in (("bgm", "bgm"), ("bgs", "bgs")):
            name = map_audio.get(key)
            if name and not (project_root / "audio" / folder / f"{name}.ogg").exists():
                raise SystemExit(f"Missing placeholder {folder.upper()} file: {name}.ogg")
    se_names = set(EVENT_SE.values()) | {name for _, name in COMMON_EVENT_SE.values()}
    for name in se_names:
        if not (project_root / "audio" / "se" / f"{name}.ogg").exists():
            raise SystemExit(f"Missing placeholder SE file: {name}.ogg")


def apply_map_audio(map_data: dict, assignment: dict) -> None:
    bgm_name = assignment.get("bgm", "")
    bgs_name = assignment.get("bgs", "")
    map_data["autoplayBgm"] = bool(bgm_name)
    map_data["bgm"] = audio(bgm_name)
    map_data["autoplayBgs"] = bool(bgs_name)
    map_data["bgs"] = audio(bgs_name, 60 if bgs_name else 90)


def command_has_se(command: dict, se_name: str) -> bool:
    if command.get("code") != 250:
        return False
    parameters = command.get("parameters", [])
    return bool(parameters and isinstance(parameters[0], dict) and parameters[0].get("name") == se_name)


def add_se_to_page(page: dict, se_name: str) -> bool:
    commands = page.get("list", [])
    if any(command_has_se(command, se_name) for command in commands):
        return False
    insert_at = 0
    while insert_at < len(commands) and commands[insert_at].get("code") == 108:
        insert_at += 1
    commands.insert(insert_at, play_se(se_name, commands[insert_at - 1].get("indent", 0) if insert_at else 0))
    return True


def apply_event_audio(map_data: dict) -> int:
    changes = 0
    for event in map_data.get("events", []):
        if not isinstance(event, dict):
            continue
        se_name = EVENT_SE.get(event.get("name", ""))
        if not se_name:
            continue
        pages = event.get("pages", [])
        if pages and add_se_to_page(pages[0], se_name):
            changes += 1
    return changes


def apply_common_events(project_root: Path) -> int:
    path = project_root / "data" / "CommonEvents.json"
    before = path.read_text(encoding="utf-8")
    common_events = json.loads(before)
    for event_id, (event_name, se_name) in COMMON_EVENT_SE.items():
        event = common_events[event_id]
        event["name"] = event_name
        event["list"] = [
            comment(f"BUILD-0006 audio hook: {event_name}"),
            play_se(se_name),
            empty_command(),
        ]
    after = json.dumps(common_events, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        path.write_text(after, encoding="utf-8")
        return 1
    return 0


def apply_maps(project_root: Path) -> tuple[int, int]:
    maps_changed = 0
    event_hooks = 0
    ledger = load_ledger(project_root)
    for map_id, assignment in MAP_AUDIO.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        if not path.exists():
            continue
        if not map_write_allowed(ledger, map_id):
            print(skip_message(ledger, map_id, "apply_audio_hooks"))
            continue
        before = path.read_text(encoding="utf-8")
        map_data = json.loads(before)
        apply_map_audio(map_data, assignment)
        event_hooks += apply_event_audio(map_data)
        note = str(map_data.get("note", ""))
        if "BUILD-0006 audio hooks" not in note:
            map_data["note"] = f"{note} BUILD-0006 audio hooks.".strip()
        after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        if after != before:
            path.write_text(after, encoding="utf-8")
            maps_changed += 1
    return maps_changed, event_hooks


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    ensure_audio_files(project_root)
    maps_changed, event_hooks = apply_maps(project_root)
    common_event_changes = apply_common_events(project_root)
    print(project_root)
    print(f"maps_updated={maps_changed} event_se_hooks_added={event_hooks} common_event_changes={common_event_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
