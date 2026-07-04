#!/usr/bin/env python3
"""Replace clean-skeleton Atlas placeholders with executable RPG Maker events."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-exports" / "home-island.json"
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

SWITCHES = {
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
    "J1_Departure_Confirmed": 14,
    "Trial_Body_Active": 50,
    "Trial_Mind_Active": 51,
    "Trial_Heart_Active": 52,
}

VARIABLES = {
    "Current_Journey": 1,
    "Archive_Recovery_Percent": 2,
    "Trial_Body_Attempts": 50,
    "Trial_Mind_SequenceStep": 51,
    "Trial_Heart_IntentChoice": 52,
    "Current_Encounter_Zone": 80,
}

ITEMS = {
    "Potion": 1,
    "Archive Fragment": 201,
}

WEAPONS = {
    "Last Sword": 2,
}

COMMON_EVENTS = {
    "CE_Trial_Complete_Chime": 5,
    "CE_Trial_Reset_Feedback": 6,
}

EXTERNAL_TARGETS = {
    "Journey II start": 50,
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


def command(code: int, parameters: list | None = None, indent: int = 0) -> dict:
    return {"code": code, "indent": indent, "parameters": parameters or []}


def empty_command() -> dict:
    return command(0)


def comment(text: str, indent: int = 0) -> dict:
    return command(108, [text], indent)


def text(line: str, indent: int = 0) -> list[dict]:
    return [
        command(101, ["", 0, 0, 2, ""], indent),
        command(401, [line], indent),
    ]


def switch(name: str, value: bool = True, indent: int = 0) -> dict:
    return command(121, [SWITCHES[name], SWITCHES[name], 0 if value else 1], indent)


def variable(name: str, value: int, indent: int = 0) -> dict:
    return command(122, [VARIABLES[name], VARIABLES[name], 0, 0, value], indent)


def variable_add(name: str, value: int, indent: int = 0) -> dict:
    return command(122, [VARIABLES[name], VARIABLES[name], 1, 0, value], indent)


def self_switch(channel: str = "A", value: bool = True, indent: int = 0) -> dict:
    return command(123, [channel, 0 if value else 1], indent)


def change_item(name: str, amount: int = 1, indent: int = 0) -> dict:
    return command(126, [ITEMS[name], 0, 0, amount], indent)


def change_weapon(name: str, amount: int = 1, indent: int = 0) -> dict:
    return command(127, [WEAPONS[name], 0, 0, amount], indent)


def call_common(name: str, indent: int = 0) -> dict:
    return command(117, [COMMON_EVENTS[name]], indent)


def transfer_to(map_id: int, x: int = 8, y: int = 6, indent: int = 0) -> list[dict]:
    return [
        command(221, indent=indent),
        command(201, [0, map_id, x, y, 0, 0], indent),
        command(222, indent=indent),
    ]


def shop_process(indent: int = 0) -> list[dict]:
    return [
        comment("Atlas shop placeholder inventory: Potion only.", indent),
        command(302, [0, ITEMS["Potion"], 0, 0], indent),
    ]


def battle_node_guardian(indent: int = 0) -> list[dict]:
    return [
        comment("Atlas boss placeholder: Node Seven Guardian troop.", indent),
        command(301, [0, 10, True, True], indent),
        switch("J1_Node07_GuardianDefeated", True, indent),
    ]


def choices(options: list[str], branch_commands: list[list[dict]], indent: int = 0) -> list[dict]:
    commands = [command(102, [options, 0, 0, 2, 0], indent)]
    for index, option in enumerate(options):
        commands.append(command(402, [index, option], indent))
        commands.extend(with_indent(branch_commands[index], indent + 1))
    commands.append(command(404, indent=indent))
    return commands


def conditional_switch(name: str, true_branch: list[dict], false_branch: list[dict], indent: int = 0) -> list[dict]:
    switch_id = SWITCHES[name]
    return [
        command(111, [0, switch_id, 0], indent),
        *with_indent(true_branch, indent + 1),
        command(411, indent=indent),
        *with_indent(false_branch, indent + 1),
        command(412, indent=indent),
    ]


def with_indent(commands: list[dict], indent: int) -> list[dict]:
    adjusted = []
    for item in commands:
        next_item = dict(item)
        next_item["indent"] = int(next_item.get("indent", 0)) + indent
        adjusted.append(next_item)
    return adjusted


def event_conditions(switch_name: str | None = None, self_switch_channel: str | None = None) -> dict:
    conditions = {
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
    if switch_name:
        conditions["switch1Id"] = SWITCHES[switch_name]
        conditions["switch1Valid"] = True
    if self_switch_channel:
        conditions["selfSwitchCh"] = self_switch_channel
        conditions["selfSwitchValid"] = True
    return conditions


def event_page(
    commands: list[dict],
    *,
    trigger: int = 0,
    priority: int = 1,
    switch_name: str | None = None,
    self_switch_channel: str | None = None,
) -> dict:
    return {
        "conditions": event_conditions(switch_name, self_switch_channel),
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


def inactive_self_switch_page() -> dict:
    return event_page([comment("Already resolved by Self Switch A.")], self_switch_channel="A")


def one_time_page(commands: list[dict], *, trigger: int = 0, priority: int = 1) -> list[dict]:
    return [event_page(commands + [self_switch("A")], trigger=trigger, priority=priority), inactive_self_switch_page()]


def event_logic(event_id: str, event_name: str) -> list[dict]:
    base = [comment(f"Atlas executable event {event_id}: {event_name}")]
    placeholder_text = f"PH-DLG-{event_id}"

    logic: dict[str, list[dict]] = {
        "EVT-HOM-001": one_time_page(base + [variable("Current_Journey", 1), variable("Archive_Recovery_Percent", 0), *text("PH-DLG-EVT-HOM-001-PLAYER-START")], trigger=3),
        "EVT-HOM-002": [event_page(base + text("PH-DLG-EVT-HOM-002-ELARA-INTRO"))],
        "EVT-HOM-003": [event_page(base + text("PH-DLG-EVT-HOM-003-CHILD-PANEL"))],
        "EVT-HOM-004": [event_page(base + text("PH-DLG-EVT-HOM-004-FARMER-WARM-STONES"))],
        "EVT-HOM-005": [event_page(base + text("PH-DLG-EVT-HOM-005-SKYREACH-TABOO"))],
        "EVT-HOM-006": [event_page(base + text("PH-DLG-EVT-HOM-006-DOCK-MESSENGER"))],
        "EVT-HOM-007": one_time_page(base + [change_item("Potion"), *text("PH-ITEM-EVT-HOM-007-HIDDEN-POTION")]),
        "EVT-HOM-008": [event_page(base + shop_process())],
        "EVT-HOM-009": one_time_page(base + [switch("J1_Tremor_Event"), switch("J1_Skyreach_AccessOpen"), *text("PH-STORY-EVT-HOM-009-TREMOR")], trigger=3),
        "EVT-HOM-010": [event_page(base + conditional_switch("J1_Skyreach_AccessOpen", text("PH-GATE-EVT-HOM-010-SKYREACH-OPEN"), text("PH-GATE-EVT-HOM-010-SKYREACH-BLOCKED")))],
        "EVT-HOM-011": one_time_page(base + [switch("J1_HiddenCave_Entered"), *text("PH-STORY-EVT-HOM-011-HIDDEN-CAVE-ENTRY")]),
        "EVT-HOM-012": one_time_page(base + [switch("Trial_Body_Active"), variable_add("Trial_Body_Attempts", 1), switch("Trial_Body_Active", False), switch("J1_Trial_Body_Clear"), call_common("CE_Trial_Complete_Chime"), *text("PH-TRIAL-EVT-HOM-012-BODY-CLEAR")]),
        "EVT-HOM-013": one_time_page(base + [switch("Trial_Mind_Active"), variable("Trial_Mind_SequenceStep", 3), switch("Trial_Mind_Active", False), switch("J1_Trial_Mind_Clear"), call_common("CE_Trial_Complete_Chime"), *text("PH-TRIAL-EVT-HOM-013-MIND-CLEAR")]),
        "EVT-HOM-014": [
            event_page(base + [
                switch("Trial_Heart_Active"),
                *choices(
                    ["Protect home", "Seek truth", "Turn back"],
                    [
                        [variable("Trial_Heart_IntentChoice", 1), switch("J1_Trial_Heart_Clear"), switch("Trial_Heart_Active", False), call_common("CE_Trial_Complete_Chime"), *text("PH-TRIAL-EVT-HOM-014-HEART-PROTECT"), self_switch("A")],
                        [variable("Trial_Heart_IntentChoice", 2), switch("J1_Trial_Heart_Clear"), switch("Trial_Heart_Active", False), call_common("CE_Trial_Complete_Chime"), *text("PH-TRIAL-EVT-HOM-014-HEART-TRUTH"), self_switch("A")],
                        [variable("Trial_Heart_IntentChoice", 3), switch("Trial_Heart_Active", False), call_common("CE_Trial_Reset_Feedback"), *text("PH-TRIAL-EVT-HOM-014-HEART-RESET")],
                    ],
                ),
            ]),
            inactive_self_switch_page(),
        ],
        "EVT-HOM-015": [event_page(base + text("PH-GATE-EVT-HOM-015-SANCTUM-REQUIRES-TRIALS"))],
        "EVT-HOM-016": one_time_page(base + [change_weapon("Last Sword"), change_item("Archive Fragment"), switch("J1_Sword_Obtained"), variable("Archive_Recovery_Percent", 3), *text("PH-STORY-EVT-HOM-016-SWORD-AWAKENING")]),
        "EVT-HOM-017": one_time_page(base + [switch("J1_Glassfield_SealOpened"), *text("PH-GATE-EVT-HOM-017-GLASSFIELD-SEAL")]),
        "EVT-HOM-018": one_time_page(base + text("PH-STORY-EVT-HOM-018-SURFACE-FRAGMENT")),
        "EVT-HOM-019": one_time_page(base + [switch("J1_SealedNode_Entered"), *text("PH-STORY-EVT-HOM-019-SEALED-NODE-ENTRY")]),
        "EVT-HOM-020": one_time_page(base + [switch("J1_CorePath_DoorOpened"), *text("PH-GATE-EVT-HOM-020-CORE-PATH")]),
        "EVT-HOM-021": one_time_page(base + [*battle_node_guardian(), *text("PH-BOSS-EVT-HOM-021-NODE-SEVEN-DEFEATED")]),
        "EVT-HOM-022": one_time_page(base + [switch("J1_Node07_RelayRestored"), switch("J1_Mainland_TravelUnlocked"), variable("Archive_Recovery_Percent", 5), *text("PH-STORY-EVT-HOM-022-RELAY-CORE-RESTORED")]),
        "EVT-HOM-023": [event_page(base + conditional_switch("J1_Mainland_TravelUnlocked", text("PH-DLG-EVT-HOM-023-DOCKMASTER-READY"), text("PH-DLG-EVT-HOM-023-DOCKMASTER-BLOCKED")))],
        "EVT-HOM-024": one_time_page(base + text("PH-STORY-EVT-HOM-024-LIGHTHOUSE-SIGNAL")),
        "EVT-HOM-025": [event_page(base + conditional_switch("J1_Mainland_TravelUnlocked", choices(["Depart", "Stay"], [[switch("J1_Departure_Confirmed"), *text("PH-CHOICE-EVT-HOM-025-DEPARTURE-CONFIRMED")], text("PH-CHOICE-EVT-HOM-025-STAY")]), text("PH-CHOICE-EVT-HOM-025-DEPARTURE-LOCKED")))],
        "EVT-HOM-026": one_time_page(base + [variable("Current_Journey", 2), *text("PH-STORY-EVT-HOM-026-DEPARTURE-SEQUENCE")], trigger=3),
        "EVT-HOM-027": [event_page(base + text("PH-TRANSFER-EVT-HOM-027-FOGFEN-ENTRY-EXIT"))],
        "EVT-HOM-028": one_time_page(base + [change_item("Potion"), *text("PH-ITEM-EVT-HOM-028-HIDDEN-POTION")]),
        "EVT-HOM-029": one_time_page(base + text("PH-STORY-EVT-HOM-029-SIGNAL-TICK-REED-POOL")),
        "EVT-HOM-030": [event_page(base + text("PH-TRANSFER-EVT-HOM-030-DEEPER-MARSH-RETURN"))],
        "EVT-HOM-031": one_time_page(base + text("PH-STORY-EVT-HOM-031-SIGNAL-POOL-CABLE-CLUSTER")),
    }
    return logic.get(event_id, [event_page(base + text(placeholder_text))])


def transfer_logic(transfer: dict, target_map_id: int) -> list[dict]:
    transfer_id = transfer["transfer_id"]
    base = [
        comment(f"Atlas executable transfer {transfer_id}: {transfer['notes']}"),
        comment(f"Condition: {transfer['condition']}"),
    ]
    transfer_commands = base + transfer_to(target_map_id)

    single_switch_gates = {
        "TRN-HOM-005": "J1_Skyreach_AccessOpen",
        "TRN-HOM-009": "J1_Skyreach_AccessOpen",
        "TRN-HOM-017": "J1_Glassfield_SealOpened",
        "TRN-HOM-023": "J1_Node07_GuardianDefeated",
        "TRN-HOM-025": "J1_Mainland_TravelUnlocked",
    }

    if transfer_id == "TRN-HOM-013":
        gated = conditional_switch(
            "J1_Trial_Body_Clear",
            conditional_switch(
                "J1_Trial_Mind_Clear",
                conditional_switch(
                    "J1_Trial_Heart_Clear",
                    transfer_to(target_map_id),
                    text("PH-GATE-TRN-HOM-013-HEART-TRIAL-REQUIRED"),
                ),
                text("PH-GATE-TRN-HOM-013-MIND-TRIAL-REQUIRED"),
            ),
            text("PH-GATE-TRN-HOM-013-BODY-TRIAL-REQUIRED"),
        )
        return [event_page(base + gated, trigger=1, priority=0)]

    if transfer_id == "TRN-HOM-025":
        gated = conditional_switch(
            "J1_Mainland_TravelUnlocked",
            choices(["Depart", "Stay"], [[switch("J1_Departure_Confirmed"), *transfer_to(target_map_id)], text("PH-CHOICE-TRN-HOM-025-STAY")]),
            text("PH-GATE-TRN-HOM-025-MAINLAND-LOCKED"),
        )
        return [event_page(base + gated, trigger=0, priority=1)]

    gate_switch = single_switch_gates.get(transfer_id)
    if gate_switch:
        return [
            event_page(base + text(f"PH-GATE-{transfer_id}-LOCKED"), trigger=1, priority=0),
            event_page(transfer_commands, trigger=1, priority=0, switch_name=gate_switch),
        ]

    return [event_page(transfer_commands, trigger=1, priority=0)]


def map_id_by_screen(export: dict, project_root: Path) -> dict[str, int]:
    map_infos = load_json(project_root / "data" / "MapInfos.json")
    by_name = {
        row["name"]: int(row["id"])
        for row in map_infos
        if isinstance(row, dict) and row.get("name")
    }
    return {
        screen["screen_id"]: by_name[screen["rpg_maker_map_name"]]
        for screen in export["home_island"]["screens"]
    }


def event_matches(event: dict, expected_name: str) -> bool:
    return str(event.get("name", "")).strip().lower() == expected_name.strip().lower()


def replace_event_pages(map_data: dict, expected_name: str, pages: list[dict]) -> bool:
    for event in map_data.get("events", []):
        if isinstance(event, dict) and event_matches(event, expected_name):
            if event.get("pages") != pages:
                event["pages"] = pages
                return True
            return False
    raise SystemExit(f"Expected event not found on {map_data.get('displayName')}: {expected_name}")


def apply_map_event_logic(export: dict, project_root: Path) -> int:
    home = export["home_island"]
    screen_maps = map_id_by_screen(export, project_root)
    changed = 0
    grouped: dict[int, list[dict]] = {}
    for event in home["events"]:
        grouped.setdefault(screen_maps[event["screen"]], []).append(event)

    for map_id, events in grouped.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        before = path.read_text(encoding="utf-8")
        map_data = json.loads(before)
        for event in events:
            if replace_event_pages(map_data, event["event"], event_logic(event["event_id"], event["event"])):
                changed += 1
        after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        if after != before:
            path.write_text(after, encoding="utf-8")
    return changed


def apply_transfer_logic(export: dict, project_root: Path) -> int:
    home = export["home_island"]
    screen_maps = map_id_by_screen(export, project_root)
    screen_maps.update(EXTERNAL_TARGETS)
    changed = 0
    grouped: dict[int, list[dict]] = {}
    for transfer in home["transfers"]:
        grouped.setdefault(screen_maps[transfer["from"]], []).append(transfer)

    for map_id, transfers in grouped.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        before = path.read_text(encoding="utf-8")
        map_data = json.loads(before)
        for transfer in transfers:
            event_name = f"{transfer['transfer_id']} {transfer['notes']}"
            target_map_id = screen_maps[transfer["to"]]
            if replace_event_pages(map_data, event_name, transfer_logic(transfer, target_map_id)):
                changed += 1
        after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        if after != before:
            path.write_text(after, encoding="utf-8")
    return changed


def apply_troop_logic(project_root: Path) -> int:
    path = project_root / "data" / "Troops.json"
    before = path.read_text(encoding="utf-8")
    troops = json.loads(before)
    troop = troops[10]
    troop["pages"] = [
        {
            "conditions": {
                "actorHp": 50,
                "actorId": 1,
                "actorValid": False,
                "enemyHp": 50,
                "enemyIndex": 0,
                "enemyValid": False,
                "switchId": 1,
                "switchValid": False,
                "turnA": 0,
                "turnB": 0,
                "turnEnding": False,
                "turnValid": True,
            },
            "list": [comment("PH-BOSS-NODE-SEVEN-OPENING"), *text("PH-BOSS-NODE-SEVEN-OPENING"), empty_command()],
            "span": 0,
        },
        {
            "conditions": {
                "actorHp": 50,
                "actorId": 1,
                "actorValid": False,
                "enemyHp": 50,
                "enemyIndex": 0,
                "enemyValid": True,
                "switchId": 1,
                "switchValid": False,
                "turnA": 0,
                "turnB": 0,
                "turnEnding": False,
                "turnValid": False,
            },
            "list": [comment("PH-BOSS-NODE-SEVEN-HALF-HP"), *text("PH-BOSS-NODE-SEVEN-HALF-HP"), empty_command()],
            "span": 0,
        },
    ]
    after = json.dumps(troops, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        path.write_text(after, encoding="utf-8")
        return 1
    return 0


def main() -> int:
    args = parse_args()
    export = load_json(Path(args.export).expanduser().resolve())
    project_root = Path(args.project_root).expanduser().resolve()
    event_changes = apply_map_event_logic(export, project_root)
    transfer_changes = apply_transfer_logic(export, project_root)
    troop_changes = apply_troop_logic(project_root)
    print(project_root)
    print(f"events_updated={event_changes} transfers_updated={transfer_changes} troop_page_changes={troop_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
