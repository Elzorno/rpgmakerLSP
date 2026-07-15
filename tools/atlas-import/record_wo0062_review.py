#!/usr/bin/env python3
"""Record a human gallery decision without changing scores or promotion."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import date
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("index", type=Path)
    parser.add_argument("candidate_id")
    parser.add_argument("decision", choices=("accepted", "rejected"))
    parser.add_argument("--reviewer", required=True)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()
    payload = json.loads(args.index.read_text(encoding="utf-8"))
    candidate = next((item for item in payload["candidates"] if item["candidate_id"] == args.candidate_id), None)
    if candidate is None:
        raise SystemExit(f"unknown candidate_id: {args.candidate_id}")
    candidate["human_review"] = {
        "status": "human_accepted_review_candidate" if args.decision == "accepted" else "human_rejected_review_candidate",
        "decision": args.decision, "reviewer": args.reviewer, "reviewed_at": date.today().isoformat(), "notes": args.notes,
    }
    candidate["promotion"] = "not_applied"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=args.index.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, args.index)
    print(f"Recorded {args.decision} review for {args.candidate_id}; production promotion not applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
