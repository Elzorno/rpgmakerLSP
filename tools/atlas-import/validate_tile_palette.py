#!/usr/bin/env python3
"""Fail-closed verifier for WO-0060 RPG Maker MZ tile palettes."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SHEET_BASES = {"Inside_A5": 1536, "Inside_B": 0, "Inside_C": 256}
ALLOWED_STATUS = {"generated_pending_live_review", "approved"}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def passage(flags: int) -> str:
    directional = flags & 0x0F
    if directional == 0:
        return "passable"
    if directional == 0x0F:
        return "blocked"
    return "directional"


def layer(sheet: str, flags: int) -> str:
    if flags & 0x10:
        return "upper_star"
    return "base" if sheet.startswith("Inside_A") else "object"


def expected_tile_id(binding: dict[str, Any]) -> int:
    source = binding["source_index"]
    if source["addressing"] == "autotile_kind":
        return 2048 + int(source["index"]) * 48
    if source["addressing"] == "normal_tile":
        return SHEET_BASES[binding["asset_sheet"]] + int(source["index"])
    raise ValueError(f"unknown addressing {source['addressing']!r}")


def verify_palette(
    palette: dict[str, Any], *, style_pack: dict[str, Any], project_root: Path, contact_root: Path
) -> list[Finding]:
    findings: list[Finding] = []
    status = palette.get("status")
    if status not in ALLOWED_STATUS:
        findings.append(Finding("invalid_status", f"status must be one of {sorted(ALLOWED_STATUS)}"))
    if status == "approved" and not palette.get("human_review", {}).get("rpg_maker_live_confirmed"):
        findings.append(Finding("approval_without_live_review", "approved palettes require recorded live RPG Maker confirmation"))
    if palette.get("style_pack_ref") != style_pack.get("style_pack_id"):
        findings.append(Finding("style_pack_mismatch", "palette style_pack_ref does not match supplied StylePack"))

    tilesets_path = project_root / "data" / "Tilesets.json"
    rows = load(tilesets_path)
    tileset = next((row for row in rows if row and row.get("id") == palette.get("tileset_id")), None)
    if not tileset or tileset.get("name") != palette.get("tileset_name"):
        return findings + [Finding("tileset_mismatch", "target tileset id/name was not found")]
    flags = tileset["flags"]

    expected_tags = set(style_pack.get("visual_tags", []))
    bound_tags: set[str] = set()
    for index, binding in enumerate(palette.get("bindings", [])):
        prefix = f"binding[{index}]"
        tag = binding.get("visual_tag", "")
        bound_tags.add(tag)
        if tag not in expected_tags:
            findings.append(Finding("unknown_visual_tag", f"{prefix} binds unknown tag {tag!r}"))
        notes = str(binding.get("provenance", {}).get("notes", ""))
        if "placeholder" in notes.lower() or "guess" in notes.lower() or not notes:
            findings.append(Finding("unverified_semantics", f"{prefix} lacks affirmative semantic provenance"))
        contact = contact_root / str(binding.get("provenance", {}).get("contact_sheet", ""))
        if not contact.is_file():
            findings.append(Finding("missing_contact_sheet", f"{prefix} contact sheet does not exist: {contact}"))
        sheet = str(binding.get("asset_sheet", ""))
        asset = project_root / "img" / "tilesets" / f"{sheet}.png"
        if not asset.is_file():
            findings.append(Finding("missing_asset_sheet", f"{prefix} source sheet does not exist: {asset}"))
            continue
        if binding.get("source_sha256") != sha256(asset):
            findings.append(Finding("source_hash_mismatch", f"{prefix} source PNG hash differs"))
        try:
            calculated_id = expected_tile_id(binding)
        except (KeyError, TypeError, ValueError) as exc:
            findings.append(Finding("invalid_address", f"{prefix}: {exc}"))
            continue
        if binding.get("tile_id") != calculated_id:
            findings.append(Finding("tile_id_mismatch", f"{prefix} expected tile id {calculated_id}"))
            continue
        actual_flags = int(flags[calculated_id])
        checks = {
            "flags": actual_flags,
            "passage": passage(actual_flags),
            "layer": layer(sheet, actual_flags),
            "adjacency": "autotile_48" if binding["source_index"]["addressing"] == "autotile_kind" else "none",
        }
        for field, actual in checks.items():
            if binding.get(field) != actual:
                findings.append(Finding(f"{field}_mismatch", f"{prefix} records {binding.get(field)!r}; target has {actual!r}"))

    missing = sorted(expected_tags - bound_tags)
    if missing:
        findings.append(Finding("missing_visual_tags", f"unbound StylePack tags: {', '.join(missing)}"))
    duplicates = sorted(tag for tag in bound_tags if tag and sum(1 for b in palette["bindings"] if b.get("visual_tag") == tag) > 1)
    # Multi-tile objects are legitimate; component labels make their ordering explicit.
    for tag in duplicates:
        entries = [b for b in palette["bindings"] if b.get("visual_tag") == tag]
        if any(not entry.get("component") for entry in entries):
            findings.append(Finding("ambiguous_multitile_binding", f"repeated tag {tag!r} requires component labels"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("palette", type=Path)
    parser.add_argument("style_pack", type=Path)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--contact-root", type=Path, required=True)
    args = parser.parse_args()
    findings = verify_palette(load(args.palette), style_pack=load(args.style_pack), project_root=args.project_root, contact_root=args.contact_root)
    for finding in findings:
        print(f"ERROR {finding.code}: {finding.message}")
    if findings:
        print(f"FAIL {len(findings)} finding(s)")
        return 1
    print(f"PASS {args.palette.name}: {len(load(args.palette)['bindings'])} verified bindings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
