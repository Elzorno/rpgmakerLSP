#!/usr/bin/env python3
"""Replace runtime-visible Atlas placeholder IDs with readable placeholder text."""

from __future__ import annotations

import argparse
import json
import re

from pathlib import Path
from typing import Any

from map_ownership_guard import load_ledger, map_write_allowed, skip_message


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"

PREFIX_LABELS = {
    "PH-BOSS": "Boss beat",
    "PH-CHOICE": "Choice",
    "PH-DLG": "Dialogue",
    "PH-EXAMINE": "Examine",
    "PH-GATE": "Route gate",
    "PH-ITEM": "Item",
    "PH-STORY": "Story beat",
    "PH-TRANSFER": "Transfer",
    "PH-TRIAL": "Trial",
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    parser.add_argument("--report", default="", help="Optional Markdown report path.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def split_placeholder(value: str) -> tuple[str, str]:
    for prefix in sorted(PREFIX_LABELS, key=len, reverse=True):
        if value == prefix:
            return prefix, ""
        marker = f"{prefix}-"
        if value.startswith(marker):
            return prefix, value[len(marker):]
    return "PH", value[3:] if value.startswith("PH-") else value


def strip_atlas_id(text: str) -> str:
    parts = [part for part in text.split("-") if part]
    if not parts:
        return ""
    if parts[0] in {"EVT", "TRN"} and len(parts) > 3 and parts[2].isdigit():
        return "-".join(parts[3:])
    if parts[0] == "OBJ":
        for index, part in enumerate(parts):
            if part.isdigit() and index + 1 < len(parts):
                return "-".join(parts[index + 1:])
        return "-".join(parts[1:])
    if parts[0] == "INT" and len(parts) > 2:
        return "-".join(parts[2:])
    return text


def title_fragment(value: str) -> str:
    value = strip_atlas_id(value)
    if not value:
        return "pending Atlas content"
    words = [word for word in value.split("-") if word]
    if not words:
        return "pending Atlas content"
    small = {"a", "an", "and", "at", "for", "in", "of", "or", "the", "to"}
    formatted = []
    for index, word in enumerate(words):
        lower = word.lower()
        if index > 0 and lower in small:
            formatted.append(lower)
        else:
            formatted.append(lower.capitalize())
    return " ".join(formatted)


def readable_text(placeholder_id: str) -> str:
    prefix, remainder = split_placeholder(placeholder_id)
    label = PREFIX_LABELS.get(prefix, "Placeholder")
    fragment = title_fragment(remainder)

    if prefix == "PH-DLG":
        return f"[Placeholder] {fragment} dialogue."
    if prefix == "PH-STORY":
        return f"[Placeholder] Story beat: {fragment}."
    if prefix == "PH-GATE":
        return f"[Placeholder] Route gate: {fragment}."
    if prefix == "PH-TRIAL":
        return f"[Placeholder] Trial feedback: {fragment}."
    if prefix == "PH-ITEM":
        return f"[Placeholder] Item result: {fragment}."
    if prefix == "PH-CHOICE":
        return f"[Placeholder] Choice result: {fragment}."
    if prefix == "PH-TRANSFER":
        return f"[Placeholder] Transfer note: {fragment}."
    if prefix == "PH-EXAMINE":
        return f"[Placeholder] Examine: {fragment}."
    if prefix == "PH-BOSS":
        return f"[Placeholder] Boss beat: {fragment}."
    return f"[Placeholder] {label}: {fragment}."


def iter_commands(node: Any):
    if isinstance(node, dict):
        if "code" in node and "parameters" in node:
            yield node
        for value in node.values():
            yield from iter_commands(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_commands(item)


def replace_visible_text(payload: Any) -> list[tuple[str, str]]:
    replacements: list[tuple[str, str]] = []
    for command in iter_commands(payload):
        if command.get("code") != 401:
            continue
        parameters = command.get("parameters")
        if not isinstance(parameters, list) or not parameters:
            continue
        value = parameters[0]
        if not isinstance(value, str) or not value.startswith("PH-"):
            continue
        replacement = readable_text(value)
        parameters[0] = replacement
        replacements.append((value, replacement))
    return replacements


def build_report(project_root: Path, replacements_by_file: dict[str, list[tuple[str, str]]]) -> str:
    total = sum(len(items) for items in replacements_by_file.values())
    lines = [
        "# BUILD-0037 - Readable Runtime Placeholder Text Report",
        "",
        "## Objective",
        "",
        "Replace runtime-visible Atlas placeholder IDs with readable placeholder text in the clean RPG Maker MZ project.",
        "",
        "## Project",
        "",
        f"- Project root: `{project_root}`",
        "",
        "## Result",
        "",
        f"- Files changed: {len(replacements_by_file)}",
        f"- Text commands updated: {total}",
        "",
        "## Policy",
        "",
        "- Visible RPG Maker Show Text commands should not display raw Atlas placeholder IDs.",
        "- Replacement text remains explicitly marked as placeholder copy.",
        "- Final story dialogue, lore, and quest writing were not invented.",
        "- Atlas traceability remains in generator logic, event names, comments, and this report.",
        "",
        "## Files Updated",
        "",
    ]
    for file_name, replacements in sorted(replacements_by_file.items()):
        lines.append(f"- `{file_name}`: {len(replacements)} text command(s)")
    lines.extend(["", "## Replacement Samples", ""])
    sample_count = 0
    for file_name, replacements in sorted(replacements_by_file.items()):
        for original, replacement in replacements:
            lines.append(f"- `{file_name}`: `{original}` -> {replacement}")
            sample_count += 1
            if sample_count >= 25:
                lines.append("- Additional replacements omitted from sample list.")
                return "\n".join(lines) + "\n"
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    data_root = project_root / "data"
    if not data_root.exists():
        raise SystemExit(f"Missing RPG Maker data directory: {data_root}")

    replacements_by_file: dict[str, list[tuple[str, str]]] = {}
    ledger = load_ledger(project_root)
    for path in sorted(data_root.glob("*.json")):
        map_match = re.fullmatch(r"Map(\d{3})\.json", path.name)
        if map_match and not map_write_allowed(ledger, int(map_match.group(1))):
            print(skip_message(ledger, int(map_match.group(1)), "apply_readable_placeholder_text"))
            continue
        payload = load_json(path)
        replacements = replace_visible_text(payload)
        if replacements:
            write_json(path, payload)
            replacements_by_file[path.name] = replacements

    report_path = Path(args.report).expanduser().resolve() if args.report else None
    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(build_report(project_root, replacements_by_file), encoding="utf-8")

    print(f"project_root={project_root}")
    print(f"files_updated={len(replacements_by_file)}")
    print(f"text_commands_updated={sum(len(items) for items in replacements_by_file.values())}")
    if report_path:
        print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
