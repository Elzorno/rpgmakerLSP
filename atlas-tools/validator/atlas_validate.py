#!/usr/bin/env python3
"""Initial Atlas Markdown frontmatter validator."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "atlas" / "docs"
REPORTS = ROOT / "atlas-tools" / "reports"
REPORT_PATH = REPORTS / "atlas_validation_report.md"

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
SCALAR_FIELD = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")

CANONICAL_REQUIRED_FIELDS = ("atlas_id", "title")
SCREEN_REQUIRED_FIELDS = ("region", "location", "rpg_maker_map_name")


@dataclass(frozen=True)
class Page:
    path: Path
    fields: dict[str, str]

    @property
    def relpath(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the scalar subset of YAML frontmatter used by Atlas pages."""
    match = FRONTMATTER.match(text)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#") or line[0].isspace():
            continue

        field_match = SCALAR_FIELD.match(line)
        if not field_match:
            continue

        key, value = field_match.groups()
        fields[key.strip()] = normalize_scalar(value or "")

    return fields


def normalize_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def scan_pages() -> list[Page]:
    return [
        Page(path=path, fields=parse_frontmatter(path.read_text(encoding="utf-8")))
        for path in sorted(DOCS.rglob("*.md"))
    ]


def collect_ids(pages: list[Page], key: str) -> dict[str, list[str]]:
    ids: dict[str, list[str]] = defaultdict(list)
    for page in pages:
        value = page.fields.get(key)
        if value:
            ids[value].append(page.relpath)
    return ids


def duplicate_errors(ids: dict[str, list[str]], key: str) -> list[str]:
    errors = []
    for value, paths in sorted(ids.items()):
        if len(paths) > 1:
            errors.append(f"duplicate {key} `{value}` in {', '.join(paths)}")
    return errors


def validate(pages: list[Page]) -> tuple[list[str], list[str], dict[str, list[str]], dict[str, list[str]]]:
    errors: list[str] = []
    warnings: list[str] = []

    atlas_ids = collect_ids(pages, "atlas_id")
    object_ids = collect_ids(pages, "object_id")

    errors.extend(duplicate_errors(atlas_ids, "atlas_id"))
    errors.extend(duplicate_errors(object_ids, "object_id"))

    for page in pages:
        fields = page.fields
        if not fields:
            warnings.append(f"{page.relpath}: no YAML frontmatter found")
            continue

        if is_true(fields.get("canonical")):
            for field in CANONICAL_REQUIRED_FIELDS:
                if not fields.get(field):
                    errors.append(f"{page.relpath}: canonical page missing `{field}`")

        if fields.get("object_id") and not fields.get("object_type"):
            errors.append(f"{page.relpath}: object page missing `object_type`")

        if fields.get("object_type") == "Screen":
            for field in SCREEN_REQUIRED_FIELDS:
                if not fields.get(field):
                    errors.append(f"{page.relpath}: screen page missing `{field}`")

    return sorted(errors), sorted(warnings), atlas_ids, object_ids


def render_report(
    pages: list[Page],
    errors: list[str],
    warnings: list[str],
    atlas_ids: dict[str, list[str]],
    object_ids: dict[str, list[str]],
) -> str:
    canonical_count = sum(1 for page in pages if is_true(page.fields.get("canonical")))
    object_page_count = sum(1 for page in pages if page.fields.get("object_id"))
    screen_page_count = sum(1 for page in pages if page.fields.get("object_type") == "Screen")

    lines = [
        "# Atlas Validation Report",
        "",
        "## Summary",
        "",
        f"- Files scanned: {len(pages)}",
        f"- Canonical pages: {canonical_count}",
        f"- Object pages: {object_page_count}",
        f"- Screen pages: {screen_page_count}",
        f"- Unique atlas IDs: {len(atlas_ids)}",
        f"- Unique object IDs: {len(object_ids)}",
        f"- Errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Errors",
        "",
    ]

    lines.extend(f"- {error}" for error in errors) if errors else lines.append("None.")

    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {warning}" for warning in warnings) if warnings else lines.append("None.")

    lines.extend(
        [
            "",
            "## Scope",
            "",
            "- Scans Markdown files under `atlas/docs`.",
            "- Parses YAML frontmatter scalar fields only.",
            "- Checks duplicate `atlas_id` and `object_id` values.",
            "- Checks required v0.1 metadata for canonical, object, and screen pages.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    if not DOCS.exists():
        print(f"Atlas docs folder not found: {DOCS}", file=sys.stderr)
        return 2

    REPORTS.mkdir(parents=True, exist_ok=True)

    pages = scan_pages()
    errors, warnings, atlas_ids, object_ids = validate(pages)
    report = render_report(pages, errors, warnings, atlas_ids, object_ids)

    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report, end="")
    print(f"\nReport written to {REPORT_PATH.relative_to(ROOT).as_posix()}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
