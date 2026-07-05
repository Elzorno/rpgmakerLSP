#!/usr/bin/env python3
"""Apply visible placeholder graphics to generated Home Island events."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from map_ownership_guard import load_ledger, map_write_allowed, skip_message


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

LANDMARK_IMAGES = {
    "boss": {"characterName": "$BigMonster1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "chest": {"characterName": "!Chest", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "crystal": {"characterName": "!Crystal", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "door": {"characterName": "!Door1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "gate": {"characterName": "!$Gate1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "npc": {"characterName": "People1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "panel": {"characterName": "!$ SP CONTROL PANEL-V1-LIGHT", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "pedestal": {"characterName": "!Weapon", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "switch": {"characterName": "!Switch1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
    "transfer": {"characterName": "!Other1", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
}

NPC_NAMES = {
    "Child Near Old Panel",
    "Dock Messenger",
    "Dockmaster",
    "Elara Intro Dialogue",
    "Farmer With Warm Stones",
    "Shopkeeper",
    "Skyreach Joker",
}

CHEST_NAMES = {
    "Deeper Marsh Reward Cache",
    "Hidden Item",
    "Hidden Item Landmark",
}

PANEL_KEYWORDS = ("Panel", "Cabinet", "Relay Core", "Signal", "Lighthouse", "Cable Cluster")
CRYSTAL_KEYWORDS = ("Trial", "Fragment", "Crystal", "Reed Pool", "Wall Carving", "Geometric Stones", "Keepsake")
GATE_KEYWORDS = ("Gate", "Seal", "Door")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    parser.add_argument("--report", default="", help="Optional Markdown report path.")
    parser.add_argument("--max-map-id", type=int, default=16, help="Highest generated Home Island map ID to update.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def classify_event(name: str) -> str:
    if name.startswith("TRN-"):
        return "transfer"
    if name in NPC_NAMES:
        return "npc"
    if name in CHEST_NAMES or "Hidden Potion" in name or "Reward" in name:
        return "chest"
    if "Guardian" in name:
        return "boss"
    if "Pedestal" in name or "Sword" in name:
        return "pedestal"
    if any(keyword in name for keyword in PANEL_KEYWORDS):
        return "panel"
    if any(keyword in name for keyword in GATE_KEYWORDS):
        return "gate"
    if any(keyword in name for keyword in CRYSTAL_KEYWORDS):
        return "crystal"
    return "switch"


def apply_image_to_event(event: dict[str, Any]) -> tuple[bool, str]:
    name = str(event.get("name", ""))
    category = classify_event(name)
    image = LANDMARK_IMAGES[category]
    changed = False
    for page in event.get("pages", []):
        if not isinstance(page, dict):
            continue
        if page.get("image") != image:
            page["image"] = dict(image)
            changed = True
        if category in {"gate", "panel", "pedestal", "switch", "transfer"} and not page.get("directionFix"):
            page["directionFix"] = True
            changed = True
        if category in {"crystal", "panel", "switch"} and not page.get("stepAnime"):
            page["stepAnime"] = True
            changed = True
    return changed, category


def build_report(project_root: Path, updates: dict[str, list[tuple[str, str]]]) -> str:
    total = sum(len(items) for items in updates.values())
    lines = [
        "# BUILD-0039 - Placeholder Landmark Images Report",
        "",
        "## Objective",
        "",
        "Make generated Home Island events visible enough for first-playable route testing by assigning existing placeholder character graphics.",
        "",
        "## Project",
        "",
        f"- Project root: `{project_root}`",
        "",
        "## Result",
        "",
        f"- Maps changed: {len(updates)}",
        f"- Events updated: {total}",
        "",
        "## Policy",
        "",
        "- Uses existing project assets only.",
        "- Does not create final art.",
        "- Does not modify Atlas story, lore, dialogue, quests, or mechanics.",
        "- Treats graphics as placeholder landmarks for playtest orientation.",
        "",
        "## Maps Updated",
        "",
    ]
    for map_name, items in sorted(updates.items()):
        lines.append(f"- `{map_name}`: {len(items)} event(s)")
    lines.extend(["", "## Event Categories", ""])
    category_counts: dict[str, int] = {}
    for items in updates.values():
        for _, category in items:
            category_counts[category] = category_counts.get(category, 0) + 1
    for category, count in sorted(category_counts.items()):
        lines.append(f"- `{category}`: {count}")
    lines.extend(["", "## Sample Events", ""])
    sample_count = 0
    for map_name, items in sorted(updates.items()):
        for event_name, category in items:
            lines.append(f"- `{map_name}`: `{event_name}` -> `{category}`")
            sample_count += 1
            if sample_count >= 35:
                lines.append("- Additional events omitted from sample list.")
                return "\n".join(lines) + "\n"
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    data_root = project_root / "data"
    updates: dict[str, list[tuple[str, str]]] = {}

    ledger = load_ledger(project_root)
    for map_id in range(1, args.max_map_id + 1):
        path = data_root / f"Map{map_id:03d}.json"
        if not map_write_allowed(ledger, map_id):
            print(skip_message(ledger, map_id, "apply_placeholder_landmark_images"))
            continue
        map_data = load_json(path)
        map_updates: list[tuple[str, str]] = []
        for event in map_data.get("events", []):
            if not isinstance(event, dict):
                continue
            changed, category = apply_image_to_event(event)
            if changed:
                map_updates.append((str(event.get("name", "")), category))
        if map_updates:
            write_json(path, map_data)
            updates[path.name] = map_updates

    report_path = Path(args.report).expanduser().resolve() if args.report else None
    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(build_report(project_root, updates), encoding="utf-8")

    print(f"project_root={project_root}")
    print(f"maps_updated={len(updates)}")
    print(f"events_updated={sum(len(items) for items in updates.values())}")
    if report_path:
        print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
