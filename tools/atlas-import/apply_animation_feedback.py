#!/usr/bin/env python3
"""Apply first-playable Home Island animation and feedback hooks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

EVENT_ANIMATIONS = {
    "Hidden Item": 40,
    "Hidden Cave First Entry": 40,
    "Body Trial": 40,
    "Mind Trial": 40,
    "Heart Trial": 117,
    "Sanctum Gate": 117,
    "Sword Pedestal": 117,
    "Glassfield Seal": 117,
    "Surface Fragment": 106,
    "Core Path Door": 40,
    "Node Seven Guardian": 40,
    "Relay Core": 120,
    "Lighthouse Examine": 40,
    "Hidden Item Landmark": 40,
    "Signal-Tick Reed Pool": 106,
    "Signal Pool / Cable Cluster Examine": 106,
}

COMMON_EVENT_ANIMATIONS = {
    1: ("CE_Archive_Message_Display", 106),
    2: ("CE_Sword_Authentication", 117),
    3: ("CE_Relay_Resolution", 120),
    5: ("CE_Trial_Complete_Chime", 40),
    6: ("CE_Trial_Reset_Feedback", 54),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="Clean RPG Maker MZ project root.")
    return parser.parse_args()


def show_animation(animation_id: int, indent: int = 0, character_id: int = 0, wait: bool = True) -> dict:
    return {"code": 212, "indent": indent, "parameters": [character_id, animation_id, wait]}


def comment(text: str) -> dict:
    return {"code": 108, "indent": 0, "parameters": [text]}


def empty_command() -> dict:
    return {"code": 0, "indent": 0, "parameters": []}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def ensure_animation_rows(project_root: Path) -> None:
    animations = load_json(project_root / "data" / "Animations.json")
    for animation_id in sorted(set(EVENT_ANIMATIONS.values()) | {value for _, value in COMMON_EVENT_ANIMATIONS.values()}):
        if animation_id >= len(animations) or not isinstance(animations[animation_id], dict):
            raise SystemExit(f"Missing animation row {animation_id}")


def command_has_animation(command: dict, animation_id: int) -> bool:
    if command.get("code") != 212:
        return False
    parameters = command.get("parameters", [])
    return len(parameters) >= 2 and parameters[1] == animation_id


def add_animation_to_page(page: dict, animation_id: int, character_id: int = 0) -> bool:
    commands = page.get("list", [])
    if any(command_has_animation(command, animation_id) for command in commands):
        return False
    insert_at = 0
    while insert_at < len(commands) and commands[insert_at].get("code") in {108, 250}:
        insert_at += 1
    indent = commands[insert_at - 1].get("indent", 0) if insert_at else 0
    commands.insert(insert_at, show_animation(animation_id, indent, character_id))
    return True


def apply_map_events(project_root: Path) -> tuple[int, int]:
    maps_changed = 0
    hooks_added = 0
    for path in sorted((project_root / "data").glob("Map*.json")):
        if not re.fullmatch(r"Map\d{3}\.json", path.name):
            continue
        before = path.read_text(encoding="utf-8")
        map_data = json.loads(before)
        map_hooks_added = 0
        for event in map_data.get("events", []):
            if not isinstance(event, dict):
                continue
            animation_id = EVENT_ANIMATIONS.get(event.get("name", ""))
            if not animation_id:
                continue
            pages = event.get("pages", [])
            if pages and add_animation_to_page(pages[0], animation_id):
                map_hooks_added += 1
                hooks_added += 1
        note = str(map_data.get("note", ""))
        if map_hooks_added and "BUILD-0007 animation feedback" not in note:
            map_data["note"] = f"{note} BUILD-0007 animation feedback.".strip()
        after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        if after != before:
            path.write_text(after, encoding="utf-8")
            maps_changed += 1
    return maps_changed, hooks_added


def apply_common_events(project_root: Path) -> int:
    path = project_root / "data" / "CommonEvents.json"
    before = path.read_text(encoding="utf-8")
    common_events = json.loads(before)
    changed = 0
    for event_id, (event_name, animation_id) in COMMON_EVENT_ANIMATIONS.items():
        event = common_events[event_id]
        commands = event.setdefault("list", [empty_command()])
        if any(command_has_animation(command, animation_id) for command in commands):
            continue
        insert_at = 0
        while insert_at < len(commands) and commands[insert_at].get("code") in {108, 250}:
            insert_at += 1
        commands.insert(insert_at, show_animation(animation_id, 0, -1))
        if not any(command.get("code") == 108 and "BUILD-0007" in str(command.get("parameters", [""])[0]) for command in commands):
            commands.insert(0, comment(f"BUILD-0007 animation hook: {event_name}"))
        changed += 1
    after = json.dumps(common_events, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        path.write_text(after, encoding="utf-8")
    return changed


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    ensure_animation_rows(project_root)
    maps_changed, hooks_added = apply_map_events(project_root)
    common_event_changes = apply_common_events(project_root)
    print(project_root)
    print(f"maps_updated={maps_changed} event_animation_hooks_added={hooks_added} common_event_changes={common_event_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
