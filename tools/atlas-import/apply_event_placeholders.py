#!/usr/bin/env python3
"""Apply Atlas event and transfer placeholders to a clean RPG Maker MZ skeleton."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-exports" / "home-island.json"
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

EXTERNAL_TARGETS = {
    "Journey II start": {"map_id": 50, "name": "JRN2_Landing_Placeholder", "display_name": "Journey II Landing Placeholder"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", default=str(DEFAULT_EXPORT), help="Path to atlas-exports/home-island.json.")
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="Clean RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def empty_command() -> dict:
    return {"code": 0, "indent": 0, "parameters": []}


def comment_command(text: str) -> dict:
    return {"code": 108, "indent": 0, "parameters": [text]}


def transfer_command(target_map_id: int, x: int = 8, y: int = 6) -> dict:
    return {"code": 201, "indent": 0, "parameters": [0, target_map_id, x, y, 0, 0]}


def switch_command(switch_id: int, value: bool = True) -> dict:
    return {"code": 121, "indent": 0, "parameters": [switch_id, switch_id, 0 if value else 1]}


def variable_command(variable_id: int, value: int) -> dict:
    return {"code": 122, "indent": 0, "parameters": [variable_id, variable_id, 0, 0, value]}


def plugin_placeholder_command(label: str) -> dict:
    return {"code": 356, "indent": 0, "parameters": [f"AtlasPlaceholder {label}"]}


def event_conditions() -> dict:
    return {
        "actorId": 1,
        "actorValid": False,
        "itemId": 1,
        "itemValid": False,
        "selfSwitchCh": "A",
        "selfSwitchValid": False,
        "switch1Id": 1,
        "switch1Valid": False,
        "switch2Id": 1,
        "switch2Valid": False,
        "variableId": 1,
        "variableValid": False,
        "variableValue": 0,
    }


def event_page(commands: list[dict], trigger: int = 0, priority: int = 1) -> dict:
    return {
        "conditions": event_conditions(),
        "directionFix": False,
        "image": {"characterIndex": 0, "characterName": "", "direction": 2, "pattern": 1, "tileId": 0},
        "list": commands + [empty_command()],
        "moveFrequency": 3,
        "moveRoute": {"list": [empty_command()], "repeat": True, "skippable": False, "wait": False},
        "moveSpeed": 3,
        "moveType": 0,
        "priorityType": priority,
        "stepAnime": False,
        "through": False,
        "trigger": trigger,
        "walkAnime": True,
    }


def make_event(event_id: int, name: str, x: int, y: int, commands: list[dict], note: str = "") -> dict:
    return {
        "id": event_id,
        "name": name,
        "note": note,
        "pages": [event_page(commands)],
        "x": x,
        "y": y,
    }


def map_lookup(project_root: Path) -> tuple[dict[str, int], dict[int, dict]]:
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    by_name = {
        row["name"]: int(row["id"])
        for row in map_infos
        if isinstance(row, dict) and row.get("name")
    }
    by_id = {
        int(row["id"]): row
        for row in map_infos
        if isinstance(row, dict) and row.get("id")
    }
    return by_name, by_id


def blank_map(display_name: str, note: str) -> dict:
    width = 17
    height = 13
    return {
        "autoplayBgm": False,
        "autoplayBgs": False,
        "battleback1Name": "",
        "battleback2Name": "",
        "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
        "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
        "disableDashing": False,
        "displayName": display_name,
        "encounterList": [],
        "encounterStep": 30,
        "height": height,
        "note": note,
        "parallaxLoopX": False,
        "parallaxLoopY": False,
        "parallaxName": "",
        "parallaxShow": True,
        "parallaxSx": 0,
        "parallaxSy": 0,
        "scrollType": 0,
        "specifyBattleback": False,
        "tilesetId": 2,
        "width": width,
        "data": [0 for _ in range(width * height * 6)],
        "events": [None],
    }


def ensure_external_targets(project_root: Path) -> int:
    map_infos_path = project_root / "data" / "MapInfos.json"
    map_infos = load_json(map_infos_path)
    changed = 0
    while len(map_infos) <= max(target["map_id"] for target in EXTERNAL_TARGETS.values()):
        map_infos.append(None)
    for label, target in EXTERNAL_TARGETS.items():
        map_id = target["map_id"]
        if not isinstance(map_infos[map_id], dict):
            map_infos[map_id] = {
                "id": map_id,
                "expanded": True,
                "name": target["name"],
                "order": map_id,
                "parentId": 0,
                "scrollX": 0,
                "scrollY": 0,
                "quick": False,
            }
            changed += 1
        map_path = project_root / "data" / f"Map{map_id:03d}.json"
        if not map_path.exists():
            write_json(
                map_path,
                blank_map(target["display_name"], f"External transfer target placeholder for {label}; BUILD-0003."),
            )
            changed += 1
    write_json(map_infos_path, map_infos)
    return changed


def next_event_id(events: list) -> int:
    ids = [event.get("id", 0) for event in events if isinstance(event, dict)]
    return max(ids, default=0) + 1


def next_position(map_data: dict, ordinal: int) -> tuple[int, int]:
    width = max(1, int(map_data.get("width", 17)))
    height = max(1, int(map_data.get("height", 13)))
    usable_width = max(1, width - 2)
    x = 1 + ((ordinal - 1) % usable_width)
    y = 1 + (((ordinal - 1) // usable_width) % max(1, height - 2))
    return x, y


def commands_for_atlas_event(event: dict) -> list[dict]:
    result = [
        comment_command(f"Atlas event {event['event_id']}: {event['event']}"),
        comment_command(f"Required result: {event['required_state_result']}"),
        plugin_placeholder_command(event["event_id"]),
    ]
    text = event["required_state_result"]
    switch_names = {
        "J1_Tremor_Event": 1,
        "J1_Skyreach_AccessOpen": 2,
        "J1_HiddenCave_Entered": 3,
        "J1_Trial_Body_Clear": 4,
        "J1_Trial_Mind_Clear": 5,
        "J1_Trial_Heart_Clear": 6,
        "J1_Sword_Obtained": 7,
        "J1_Glassfield_SealOpened": 8,
        "J1_SealedNode_Entered": 9,
        "J1_CorePath_DoorOpened": 10,
        "J1_Node07_GuardianDefeated": 11,
        "J1_Node07_RelayRestored": 12,
        "J1_Mainland_TravelUnlocked": 13,
    }
    for switch_name, switch_id in switch_names.items():
        if switch_name in text:
            result.append(switch_command(switch_id))
    if "Current_Journey = 2" in text:
        result.append(variable_command(1, 2))
    if "Archive_Recovery_Percent = 3" in text:
        result.append(variable_command(2, 3))
    return result


def apply_atlas_events(export: dict, project_root: Path) -> int:
    home = export["home_island"]
    by_name, _ = map_lookup(project_root)
    screen_to_map = {
        screen["screen_id"]: by_name[screen["rpg_maker_map_name"]]
        for screen in home["screens"]
    }
    grouped: dict[int, list[dict]] = {}
    for event in home["events"]:
        grouped.setdefault(screen_to_map[event["screen"]], []).append(event)

    count = 0
    for map_id, atlas_events in grouped.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        map_data = load_json(path)
        events = map_data.setdefault("events", [None])
        existing_names = {event.get("name") for event in events if isinstance(event, dict)}
        ordinal = len(existing_names) + 1
        for atlas_event in atlas_events:
            if atlas_event["event"] in existing_names:
                continue
            event_id = next_event_id(events)
            while event_id >= len(events):
                events.append(None)
            x, y = next_position(map_data, ordinal)
            events[event_id] = make_event(
                event_id,
                atlas_event["event"],
                x,
                y,
                commands_for_atlas_event(atlas_event),
                note=f"Atlas {atlas_event['event_id']}",
            )
            existing_names.add(atlas_event["event"])
            ordinal += 1
            count += 1
        write_json(path, map_data)
    return count


def apply_transfers(export: dict, project_root: Path) -> int:
    home = export["home_island"]
    by_name, _ = map_lookup(project_root)
    screen_to_map = {
        screen["screen_id"]: by_name[screen["rpg_maker_map_name"]]
        for screen in home["screens"]
    }
    for label, target in EXTERNAL_TARGETS.items():
        screen_to_map[label] = int(target["map_id"])
    count = 0
    grouped: dict[int, list[dict]] = {}
    for transfer in home["transfers"]:
        if transfer["to"] not in screen_to_map:
            continue
        grouped.setdefault(screen_to_map[transfer["from"]], []).append(transfer)

    for map_id, transfers in grouped.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        map_data = load_json(path)
        events = map_data.setdefault("events", [None])
        existing_names = {event.get("name") for event in events if isinstance(event, dict)}
        ordinal = len(existing_names) + 1
        for transfer in transfers:
            name = f"{transfer['transfer_id']} {transfer['notes']}"
            if name in existing_names:
                continue
            target_id = screen_to_map[transfer["to"]]
            event_id = next_event_id(events)
            while event_id >= len(events):
                events.append(None)
            x, y = next_position(map_data, ordinal)
            commands = [
                comment_command(f"Atlas transfer {transfer['transfer_id']}: {transfer['notes']}"),
                comment_command(f"Condition: {transfer['condition']}"),
                transfer_command(target_id),
            ]
            events[event_id] = make_event(event_id, name, x, y, commands, note=f"Atlas {transfer['transfer_id']}")
            existing_names.add(name)
            ordinal += 1
            count += 1
        write_json(path, map_data)
    return count


def troop_event_page(commands: list[dict], enemy_hp: int | None = None) -> dict:
    conditions = {
        "actorHp": 50,
        "actorId": 1,
        "actorValid": False,
        "enemyHp": enemy_hp if enemy_hp is not None else 50,
        "enemyIndex": 0,
        "enemyValid": enemy_hp is not None,
        "switchId": 1,
        "switchValid": False,
        "turnA": 0,
        "turnB": 0,
        "turnEnding": False,
        "turnValid": enemy_hp is None,
    }
    return {"conditions": conditions, "list": commands + [empty_command()], "span": 0}


def apply_troop_event_pages(project_root: Path) -> int:
    path = project_root / "data" / "Troops.json"
    troops = load_json(path)
    troop = troops[10]
    pages = troop.setdefault("pages", [])
    changed = 0
    if pages:
        if pages[0].get("list", [empty_command()])[0].get("code") == 0:
            pages[0]["list"] = [
                comment_command("BOSS_NODE_SEVEN_OPENING_PLACEHOLDER"),
                empty_command(),
            ]
            changed += 1
    else:
        pages.append(troop_event_page([comment_command("BOSS_NODE_SEVEN_OPENING_PLACEHOLDER")]))
        changed += 1

    if len(pages) < 2:
        pages.append(troop_event_page([comment_command("BOSS_NODE_SEVEN_HALF_HP_PLACEHOLDER")], enemy_hp=50))
        changed += 1
    elif not any(command.get("code") not in {0, None} for command in pages[1].get("list", [])):
        pages[1]["list"] = [
            comment_command("BOSS_NODE_SEVEN_HALF_HP_PLACEHOLDER"),
            empty_command(),
        ]
        changed += 1

    write_json(path, troops)
    return changed


def main() -> int:
    args = parse_args()
    export = load_json(Path(args.export).expanduser().resolve())
    project_root = Path(args.project_root).expanduser().resolve()
    external_changes = ensure_external_targets(project_root)
    event_count = apply_atlas_events(export, project_root)
    transfer_count = apply_transfers(export, project_root)
    troop_changes = apply_troop_event_pages(project_root)
    print(project_root)
    print(
        f"events_added={event_count} transfers_added={transfer_count} "
        f"troop_page_changes={troop_changes} external_target_changes={external_changes}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
