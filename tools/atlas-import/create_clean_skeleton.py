#!/usr/bin/env python3
"""Create a clean RPG Maker MZ skeleton from the Atlas Home Island export."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-exports" / "home-island.json"
DEFAULT_TARGET = ROOT.parent / "TheLastSwordProtocol-Game"

GAME_TITLE = "The Last Sword Protocol"

SWITCH_NAMES = {
    1: "J1_Tremor_Event",
    2: "J1_Skyreach_AccessOpen",
    3: "J1_HiddenCave_Entered",
    4: "J1_Trial_Body_Clear",
    5: "J1_Trial_Mind_Clear",
    6: "J1_Trial_Heart_Clear",
    7: "J1_Sword_Obtained",
    8: "J1_Glassfield_SealOpened",
    9: "J1_SealedNode_Entered",
    10: "J1_CorePath_DoorOpened",
    11: "J1_Node07_GuardianDefeated",
    12: "J1_Node07_RelayRestored",
    13: "J1_Mainland_TravelUnlocked",
    14: "J1_Departure_Confirmed",
    50: "Trial_Body_Active",
    51: "Trial_Mind_Active",
    52: "Trial_Heart_Active",
}

VARIABLE_NAMES = {
    1: "Current_Journey",
    2: "Archive_Recovery_Percent",
    50: "Trial_Body_Attempts",
    51: "Trial_Mind_SequenceStep",
    52: "Trial_Heart_IntentChoice",
    80: "Current_Encounter_Zone",
}

COMMON_EVENT_NAMES = {
    1: "CE_Archive_Message_Display",
    2: "CE_Sword_Authentication",
    3: "CE_Relay_Resolution",
    4: "CE_Screen_Transition_Helper",
    5: "CE_Trial_Complete_Chime",
    6: "CE_Trial_Reset_Feedback",
}

TILESET_IDS = {
    "Outside": 2,
    "Inside": 3,
    "Dungeon": 4,
    "SF Outside": 5,
    "SF Inside": 6,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--export",
        default=str(DEFAULT_EXPORT),
        help="Path to atlas-exports/home-island.json.",
    )
    parser.add_argument(
        "--target",
        default=str(DEFAULT_TARGET),
        help="Target RPG Maker MZ project directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Remove and recreate the target directory if it already exists.",
    )
    return parser.parse_args()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def copy_tree(source: Path, target: Path) -> None:
    if source.exists():
        shutil.copytree(source, target, dirs_exist_ok=True)


def blank_array(size: int) -> list:
    return [None for _ in range(size + 1)]


def empty_audio(name: str = "") -> dict:
    return {"name": name, "pan": 0, "pitch": 100, "volume": 90}


def empty_damage() -> dict:
    return {"critical": False, "elementId": 0, "formula": "0", "type": 0, "variance": 20}


def empty_command() -> dict:
    return {"code": 0, "indent": 0, "parameters": []}


def class_params() -> list[list[int]]:
    params = []
    starts = [450, 80, 32, 28, 18, 18, 24, 24]
    gains = [18, 4, 2, 2, 1, 1, 1, 1]
    for start, gain in zip(starts, gains):
        params.append([0] + [start + (level - 1) * gain for level in range(1, 100)])
    return params


def make_actor(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "battlerName": "Actor1_1",
        "characterIndex": 0,
        "characterName": "Actor1",
        "classId": 1,
        "equips": [1, 0, 0, 1, 0],
        "faceIndex": 0,
        "faceName": "Actor1",
        "traits": [],
        "initialLevel": 1,
        "maxLevel": 99,
        "name": name,
        "nickname": "Atlas Build",
        "note": "BUILD-0001 Atlas-reserved actor row.",
        "profile": "Atlas placeholder actor for the Home Island vertical slice.",
    }


def make_class(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "expParams": [30, 20, 30, 30],
        "traits": [
            {"code": 23, "dataId": 0, "value": 1},
            {"code": 22, "dataId": 0, "value": 0.95},
            {"code": 22, "dataId": 1, "value": 0.05},
            {"code": 51, "dataId": 1, "value": 0},
            {"code": 52, "dataId": 1, "value": 0},
            {"code": 52, "dataId": 4, "value": 0},
        ],
        "learnings": [],
        "name": name,
        "note": "BUILD-0001 Atlas-reserved class row.",
        "params": class_params(),
    }


def make_skill(row_id: int, name: str, animation_id: int) -> dict:
    return {
        "id": row_id,
        "animationId": animation_id,
        "damage": {
            "critical": row_id == 1,
            "elementId": -1 if row_id == 1 else 1,
            "formula": "a.atk * 4 - b.def * 2" if row_id == 1 else "a.atk * 2 - b.def",
            "type": 1,
            "variance": 20,
        },
        "description": "Atlas placeholder skill.",
        "effects": [{"code": 21, "dataId": 0, "value1": 1, "value2": 0}],
        "hitType": 1,
        "iconIndex": 76,
        "message1": "%1 attacks!" if row_id == 1 else f"%1 uses {name}!",
        "message2": "",
        "mpCost": 0,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved skill row.",
        "occasion": 1,
        "repeats": 1,
        "requiredWtypeId1": 0,
        "requiredWtypeId2": 0,
        "scope": 1,
        "speed": 0,
        "stypeId": 0 if row_id == 1 else 2,
        "successRate": 100,
        "tpCost": 0,
        "tpGain": 5 if row_id == 1 else 0,
        "messageType": 1,
    }


def make_item(row_id: int, name: str, key_item: bool = False) -> dict:
    effects = [] if key_item else [{"code": 11, "dataId": 0, "value1": 0, "value2": 50}]
    return {
        "id": row_id,
        "animationId": 41 if not key_item else 0,
        "consumable": not key_item,
        "damage": empty_damage(),
        "description": "Atlas placeholder key item." if key_item else "Restores a small amount of HP.",
        "effects": effects,
        "hitType": 0,
        "iconIndex": 176 if key_item else 208,
        "itypeId": 2 if key_item else 1,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved item row.",
        "occasion": 0 if not key_item else 3,
        "price": 0 if key_item else 50,
        "repeats": 1,
        "scope": 7 if not key_item else 0,
        "speed": 0,
        "successRate": 100,
        "tpGain": 0,
    }


def make_weapon(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "animationId": 6,
        "description": "Atlas placeholder weapon.",
        "etypeId": 1,
        "traits": [{"code": 31, "dataId": 1, "value": 0}],
        "iconIndex": 97,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved weapon row.",
        "params": [0, 0, 5 if row_id == 1 else 12, 0, 0, 0, 0, 0],
        "price": 0,
        "wtypeId": 1,
    }


def make_armor(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "atypeId": 1,
        "description": "Atlas placeholder armor.",
        "etypeId": 4,
        "traits": [],
        "iconIndex": 135,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved armor row.",
        "params": [0, 0, 0, 2, 0, 0, 0, 0],
        "price": 0,
    }


def make_enemy(row_id: int, name: str) -> dict:
    skill_id = 110 if row_id == 10 else 1
    return {
        "id": row_id,
        "actions": [{"conditionParam1": 0, "conditionParam2": 0, "conditionType": 0, "rating": 5, "skillId": skill_id}],
        "battlerHue": 0,
        "battlerName": "Goblin" if row_id != 10 else "Blackknight",
        "dropItems": [
            {"dataId": 1, "denominator": 1, "kind": 0},
            {"dataId": 1, "denominator": 1, "kind": 0},
            {"dataId": 1, "denominator": 1, "kind": 0},
        ],
        "exp": 5 if row_id != 10 else 30,
        "traits": [{"code": 22, "dataId": 0, "value": 0.95}],
        "gold": 3 if row_id != 10 else 25,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved enemy row.",
        "params": [80, 0, 14, 10, 10, 10, 12, 12] if row_id != 10 else [450, 40, 30, 24, 18, 18, 20, 20],
    }


def troop_page() -> dict:
    return {
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
            "turnValid": False,
        },
        "list": [empty_command()],
        "span": 0,
    }


def make_troop(row_id: int, name: str) -> dict:
    enemy_id = 10 if row_id == 10 else min(row_id, 3)
    return {
        "id": row_id,
        "members": [{"enemyId": enemy_id, "x": 408, "y": 280, "hidden": False}],
        "name": name,
        "pages": [troop_page()],
    }


def make_state(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "autoRemovalTiming": 0,
        "chanceByDamage": 100,
        "iconIndex": 1 if row_id == 1 else 0,
        "maxTurns": 1,
        "message1": "%1 has fallen!" if row_id == 1 else "",
        "message2": "%1 is affected by %2!" if row_id != 1 else "%1 is slain!",
        "message3": "",
        "message4": "%1 recovers!" if row_id != 1 else "%1 revives!",
        "minTurns": 1,
        "motion": 3 if row_id == 1 else 0,
        "name": name,
        "note": "BUILD-0001 Atlas-reserved state row.",
        "overlay": 0,
        "priority": 100 if row_id == 1 else 50,
        "releaseByDamage": False,
        "removeAtBattleEnd": row_id != 1,
        "removeByDamage": False,
        "removeByRestriction": False,
        "removeByWalking": False,
        "restriction": 4 if row_id == 1 else 0,
        "stepsToRemove": 100,
        "traits": [{"code": 23, "dataId": 9, "value": 0}] if row_id == 1 else [],
        "messageType": 1,
    }


def make_common_event(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "list": [
            {"code": 108, "indent": 0, "parameters": [f"BUILD-0001 placeholder for {name}."]},
            empty_command(),
        ],
        "name": name,
        "switchId": 1,
        "trigger": 0,
    }


def make_map(screen: dict, tileset_name: str) -> dict:
    width = 17
    height = 13
    return {
        "autoplayBgm": False,
        "autoplayBgs": False,
        "battleback1Name": "",
        "battleback2Name": "",
        "bgm": empty_audio(),
        "bgs": empty_audio(),
        "disableDashing": False,
        "displayName": screen["screen"],
        "encounterList": [],
        "encounterStep": 30,
        "height": height,
        "note": f"Atlas screen {screen['screen_id']}; BUILD-0001 placeholder map.",
        "parallaxLoopX": False,
        "parallaxLoopY": False,
        "parallaxName": "",
        "parallaxShow": True,
        "parallaxSx": 0,
        "parallaxSy": 0,
        "scrollType": 0,
        "specifyBattleback": False,
        "tilesetId": TILESET_IDS.get(tileset_name, 2),
        "width": width,
        "data": [0 for _ in range(width * height * 6)],
        "events": [None],
    }


def make_map_info(row_id: int, name: str) -> dict:
    return {
        "id": row_id,
        "expanded": True,
        "name": name,
        "order": row_id,
        "parentId": 0,
        "scrollX": 0,
        "scrollY": 0,
        "quick": False,
    }


def patch_system(system: dict) -> dict:
    system = dict(system)
    system["gameTitle"] = GAME_TITLE
    system["editMapId"] = 1
    system["startMapId"] = 2
    system["startX"] = 8
    system["startY"] = 6
    system["partyMembers"] = [1]
    system["testTroopId"] = 1
    system["optSideView"] = True
    system["switches"] = [""] + [SWITCH_NAMES.get(i, "") for i in range(1, 201)]
    system["variables"] = [""] + [VARIABLE_NAMES.get(i, "") for i in range(1, 151)]
    for vehicle in ("boat", "ship", "airship"):
        if isinstance(system.get(vehicle), dict):
            system[vehicle] = dict(system[vehicle])
            system[vehicle]["startMapId"] = 0
            system[vehicle]["startX"] = 0
            system[vehicle]["startY"] = 0
    return system


def prepare_target(target: Path, force: bool) -> None:
    if target.exists():
        if not force:
            raise SystemExit(f"Target already exists. Use --force to replace it: {target}")
        shutil.rmtree(target)
    target.mkdir(parents=True)


def copy_runtime_files(target: Path) -> None:
    for file_name in ("index.html", "package.json", "game.rmmzproject"):
        shutil.copy2(ROOT / file_name, target / file_name)
    for directory in ("audio", "css", "effects", "fonts", "icon", "img", "movies"):
        copy_tree(ROOT / directory, target / directory)
    copy_tree(ROOT / "js" / "libs", target / "js" / "libs")
    for file_name in (
        "main.js",
        "rmmz_core.js",
        "rmmz_managers.js",
        "rmmz_objects.js",
        "rmmz_scenes.js",
        "rmmz_sprites.js",
        "rmmz_windows.js",
    ):
        shutil.copy2(ROOT / "js" / file_name, target / "js" / file_name)
    (target / "js" / "plugins").mkdir(parents=True, exist_ok=True)
    write_json(target / "js" / "plugins.js", [])
    (target / "save").mkdir(exist_ok=True)


def write_static_project_files(target: Path) -> None:
    (target / ".gitignore").write_text("/save/\n*.bak\n*.tmp\n.DS_Store\n", encoding="utf-8")
    (target / "README.md").write_text(
        "\n".join(
            [
                "# The Last Sword Protocol - Clean RPG Maker MZ Skeleton",
                "",
                "Generated by BUILD-0001 from the Atlas Home Island export.",
                "",
                "This project is the clean Atlas implementation target. The legacy `rpgmakerLSP` project remains reference material.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def build_database(export: dict, target: Path) -> None:
    home = export["home_island"]
    data_dir = target / "data"
    source_data = ROOT / "data"

    allocation = home["combat_database"]["database_id_allocation"]
    by_database: dict[str, list[dict]] = {}
    for row in allocation:
        by_database.setdefault(row["database"], []).append(row)

    actors = blank_array(20)
    for row in by_database.get("Actor", []):
        actors[int(row["id"])] = make_actor(int(row["id"]), row["name"])
    write_json(data_dir / "Actors.json", actors)

    classes = blank_array(20)
    for row in by_database.get("Class", []):
        classes[int(row["id"])] = make_class(int(row["id"]), row["name"])
    write_json(data_dir / "Classes.json", classes)

    skills = blank_array(149)
    skill_animation = {int(row["skill_id"]): int(row["animation"]) for row in home["combat_database"]["skills"]}
    for row in by_database.get("Skill", []):
        row_id = int(row["id"])
        skills[row_id] = make_skill(row_id, row["name"], skill_animation.get(row_id, 0))
    write_json(data_dir / "Skills.json", skills)

    items = blank_array(249)
    for row in by_database.get("Item", []):
        items[int(row["id"])] = make_item(int(row["id"]), row["name"])
    for row in by_database.get("Key Item", []):
        items[int(row["id"])] = make_item(int(row["id"]), row["name"], key_item=True)
    write_json(data_dir / "Items.json", items)

    weapons = blank_array(49)
    for row in by_database.get("Weapon", []):
        weapons[int(row["id"])] = make_weapon(int(row["id"]), row["name"])
    write_json(data_dir / "Weapons.json", weapons)

    armors = blank_array(49)
    for row in by_database.get("Armor", []):
        armors[int(row["id"])] = make_armor(int(row["id"]), row["name"])
    write_json(data_dir / "Armors.json", armors)

    enemies = blank_array(99)
    for row in by_database.get("Enemy", []):
        enemies[int(row["id"])] = make_enemy(int(row["id"]), row["name"])
    write_json(data_dir / "Enemies.json", enemies)

    troops = blank_array(99)
    for row in by_database.get("Troop", []):
        troops[int(row["id"])] = make_troop(int(row["id"]), row["name"])
    for row in home["combat_database"]["troops"]:
        if "name" not in row:
            continue
        row_id = int(row["troop_id"])
        if row_id < len(troops):
            troops[row_id] = make_troop(row_id, row["name"])
    write_json(data_dir / "Troops.json", troops)

    states = blank_array(49)
    for row in by_database.get("State", []):
        states[int(row["id"])] = make_state(int(row["id"]), row["name"])
    write_json(data_dir / "States.json", states)

    common_events = blank_array(49)
    for row_id, name in COMMON_EVENT_NAMES.items():
        common_events[row_id] = make_common_event(row_id, name)
    write_json(data_dir / "CommonEvents.json", common_events)

    source_tilesets = load_json(source_data / "Tilesets.json")
    tilesets = blank_array(6)
    for name, row_id in TILESET_IDS.items():
        tilesets[row_id] = source_tilesets[row_id]
        tilesets[row_id]["name"] = name
    write_json(data_dir / "Tilesets.json", tilesets)

    animation_ids = {
        int(row["animation_id"])
        for row in home["animations"]["core_animation_ids"]
        if str(row["animation_id"]).isdigit()
    }
    for rows in (home["animations"]["combat_animation_matrix"], home["animations"]["story_event_animation_matrix"]):
        for row in rows:
            animation_id = row.get("rpg_maker_animation_id")
            if str(animation_id).isdigit():
                animation_ids.add(int(animation_id))
    source_animations = load_json(source_data / "Animations.json")
    animations = blank_array(max(animation_ids))
    for row_id in sorted(animation_ids):
        animations[row_id] = source_animations[row_id]
    write_json(data_dir / "Animations.json", animations)

    system = patch_system(load_json(source_data / "System.json"))
    write_json(data_dir / "System.json", system)


def build_maps(export: dict, target: Path) -> None:
    home = export["home_island"]
    data_dir = target / "data"
    tileset_by_screen = {
        row["screen_id"]: row["placeholder_tileset"]
        for row in home["tilesets"]
    }
    map_infos = [None]
    for map_id, screen in enumerate(home["screens"], 1):
        map_infos.append(make_map_info(map_id, screen["rpg_maker_map_name"]))
        write_json(
            data_dir / f"Map{map_id:03d}.json",
            make_map(screen, tileset_by_screen.get(screen["screen_id"], "Outside")),
        )
    write_json(data_dir / "MapInfos.json", map_infos)


def write_manifest(export: dict, target: Path) -> None:
    home = export["home_island"]
    manifest = {
        "build": "BUILD-0001",
        "source_export": {
            "export_name": export.get("export_name"),
            "schema_version": export.get("schema_version"),
            "generated_at": export.get("generated_at"),
            "source": export.get("source"),
        },
        "project": {
            "title": GAME_TITLE,
            "target": str(target),
            "maps": len(home["screens"]),
            "transfers": len(home["transfers"]),
            "events": len(home["events"]),
        },
        "reservation_policy": {
            "maps": "1-49 reserved for Home Island vertical slice",
            "database": "Atlas Home Island rows written at exported IDs",
            "switches": "1-49 Journey 1, 50-79 trials, 80-99 Home Island optional, 100-149 combat, 150-199 debug",
            "variables": "1-49 journey/story, 50-79 trials, 80-99 encounter support, 100-149 debug",
            "common_events": "1-49 Atlas common events",
        },
    }
    write_json(target / "atlas_skeleton_manifest.json", manifest)


def main() -> int:
    args = parse_args()
    export_path = Path(args.export).expanduser().resolve()
    target = Path(args.target).expanduser().resolve()
    export = load_json(export_path)

    prepare_target(target, args.force)
    copy_runtime_files(target)
    write_static_project_files(target)
    build_database(export, target)
    build_maps(export, target)
    write_manifest(export, target)

    print(target)
    print("maps=16 database=reserved switches=200 variables=150 common_events=49")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
