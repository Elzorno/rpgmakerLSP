#!/usr/bin/env python3
"""Apply executable placeholder logic to generated local examine anchors."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

ITEMS = {
    "Potion": 1,
}

LOCAL_EXAMINES = {
    1: {
        "INT-ASH-WARM-STONE-VENT Warm-Stone Vent": "INT-ASH-WARM-STONE-VENT",
        "INT-ASH-OLD-PANEL Old Panel": "INT-ASH-OLD-PANEL",
    },
    2: {
        "INT-ASH-ELARA-KEEPSAKE Keepsake Shelf": "INT-ASH-ELARA-KEEPSAKE",
    },
    3: {
        "INT-ASH-SHOP-CABINET Metal Cabinet": "INT-ASH-SHOP-CABINET",
    },
    4: {
        "INT-SKY-GEOMETRIC-STONES Geometric Stones": "INT-SKY-GEOMETRIC-STONES",
    },
    5: {
        "INT-HCV-WALL-CARVING Wall Carving": "INT-HCV-WALL-CARVING",
    },
}

ONE_TIME_REWARDS = {
    16: {
        "Deeper Marsh Reward Cache": "OBJ-HOM-FOG-009",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
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


def self_switch(channel: str = "A", value: bool = True, indent: int = 0) -> dict:
    return command(123, [channel, 0 if value else 1], indent)


def change_item(name: str, amount: int = 1, indent: int = 0) -> dict:
    return command(126, [ITEMS[name], 0, 0, amount], indent)


def event_conditions(self_switch_channel: str | None = None) -> dict:
    return {
        "actorId": 1,
        "actorValid": False,
        "itemId": 1,
        "itemValid": False,
        "selfSwitchCh": self_switch_channel or "A",
        "selfSwitchValid": self_switch_channel is not None,
        "switch1Id": 1,
        "switch1Valid": False,
        "switch2Id": 1,
        "switch2Valid": False,
        "variableId": 1,
        "variableValid": False,
        "variableValue": 0,
    }


def event_page(commands: list[dict], *, self_switch_channel: str | None = None) -> dict:
    return {
        "conditions": event_conditions(self_switch_channel),
        "directionFix": False,
        "image": {"characterIndex": 0, "characterName": "", "direction": 2, "pattern": 1, "tileId": 0},
        "list": commands + [empty_command()],
        "moveFrequency": 3,
        "moveRoute": {"list": [empty_command()], "repeat": True, "skippable": False, "wait": False},
        "moveSpeed": 3,
        "moveType": 0,
        "priorityType": 1,
        "stepAnime": False,
        "through": False,
        "trigger": 0,
        "walkAnime": True,
    }


def examine_pages(anchor_id: str) -> list[dict]:
    return [
        event_page([
            comment(f"Atlas local examine {anchor_id}"),
            *text(f"PH-EXAMINE-{anchor_id}"),
        ])
    ]


def reward_pages(anchor_id: str) -> list[dict]:
    return [
        event_page([
            comment(f"Atlas local reward {anchor_id}"),
            change_item("Potion"),
            *text(f"PH-ITEM-{anchor_id}-POTION"),
            self_switch("A"),
        ]),
        event_page([
            comment(f"Atlas local reward {anchor_id} already collected"),
            *text(f"PH-ITEM-{anchor_id}-EMPTY"),
        ], self_switch_channel="A"),
    ]


def replace_pages(map_data: dict[str, Any], event_name: str, pages: list[dict]) -> bool:
    for event in map_data.get("events", []):
        if not isinstance(event, dict):
            continue
        if str(event.get("name", "")).strip() == event_name:
            if event.get("pages") != pages:
                event["pages"] = pages
                return True
            return False
    raise SystemExit(f"Expected local anchor event not found: {event_name}")


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    changed: list[str] = []

    for map_id, events in {**LOCAL_EXAMINES, **ONE_TIME_REWARDS}.items():
        path = project_root / "data" / f"Map{map_id:03d}.json"
        map_data = load_json(path)
        before = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        for event_name, anchor_id in events.items():
            pages = reward_pages(anchor_id) if map_id in ONE_TIME_REWARDS else examine_pages(anchor_id)
            if replace_pages(map_data, event_name, pages):
                changed.append(f"Map{map_id:03d}:{event_name}")
        after = json.dumps(map_data, ensure_ascii=False, separators=(",", ":"))
        if after != before:
            write_json(path, map_data)

    print(f"project_root={project_root}")
    print(f"events_updated={len(changed)}")
    for item in changed:
        print(f"updated={item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
