#!/usr/bin/env python3
"""Read-only audit of the per-map ownership ledger (WO-0031).

Reports each map's ledger state, flags maps present on disk but missing from
the ledger (and vice versa), and states whether pipeline writes are currently
permitted. Never modifies game data or the ledger.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from map_ownership_guard import LEDGER_FILENAME, WRITABLE_STATE, load_ledger

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROJECT = ROOT.parent / "TheLastSwordProtocol-Game"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT), help="RPG Maker MZ project root.")
    parser.add_argument("--report", default="", help="Optional Markdown report path.")
    return parser.parse_args()


def maps_on_disk(project_root: Path) -> list[int]:
    data_root = project_root / "data"
    ids: list[int] = []
    if data_root.exists():
        for path in sorted(data_root.glob("Map*.json")):
            match = re.fullmatch(r"Map(\d{3})\.json", path.name)
            if match:
                ids.append(int(match.group(1)))
    return ids


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    ledger = load_ledger(project_root)
    disk_ids = maps_on_disk(project_root)

    lines: list[str] = ["# Map Ownership Ledger Audit", "", f"- Project: `{project_root}`"]
    if ledger is None:
        lines.append(f"- Ledger: `{LEDGER_FILENAME}` MISSING OR UNREADABLE")
        lines.append("- Pipeline map writes permitted: NONE (fail safe: no ledger, no writes)")
    else:
        counts: dict[str, int] = {}
        for state in ledger.values():
            counts[state] = counts.get(state, 0) + 1
        lines.append(f"- Ledger: `{LEDGER_FILENAME}` OK ({len(ledger)} maps listed)")
        lines.append(
            "- States: " + ", ".join(f"{state}={count}" for state, count in sorted(counts.items()))
        )
        writable = sorted(map_id for map_id, state in ledger.items() if state == WRITABLE_STATE)
        lines.append(f"- Pipeline-writable maps ({WRITABLE_STATE}): {len(writable)}")
        lines.append("")
        lines.append("| Map | Ledger State | On Disk | Pipeline May Write |")
        lines.append("|---|---|---|---|")
        for map_id in sorted(set(ledger) | set(disk_ids)):
            state = ledger.get(map_id, "NOT IN LEDGER (not writable)")
            on_disk = "yes" if map_id in disk_ids else "no"
            may_write = "yes" if ledger.get(map_id) == WRITABLE_STATE else "NO"
            lines.append(f"| Map{map_id:03d} | {state} | {on_disk} | {may_write} |")
        unledgered = sorted(set(disk_ids) - set(ledger))
        if unledgered:
            lines.append("")
            lines.append(
                "Maps on disk but missing from the ledger (treated as NOT writable): "
                + ", ".join(f"Map{map_id:03d}" for map_id in unledgered)
            )
        missing_files = sorted(set(ledger) - set(disk_ids))
        if missing_files:
            lines.append("")
            lines.append(
                "Ledger entries with no map file on disk: "
                + ", ".join(f"Map{map_id:03d}" for map_id in missing_files)
            )

    report_text = "\n".join(lines) + "\n"
    print(report_text, end="")

    if args.report:
        report_path = Path(args.report).expanduser().resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report_text, encoding="utf-8")
        print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
