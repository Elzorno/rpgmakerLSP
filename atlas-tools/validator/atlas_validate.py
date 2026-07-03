from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "atlas" / "docs"
REPORTS = ROOT / "atlas-tools" / "reports"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

def parse_frontmatter(text):
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data

def main():
    REPORTS.mkdir(parents=True, exist_ok=True)

    atlas_ids = {}
    object_ids = {}
    errors = []
    warnings = []

    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        rel = path.relative_to(ROOT)

        if fm.get("canonical", "").lower() == "true":
            if not fm.get("atlas_id"):
                errors.append(f"{rel}: missing atlas_id")
            if not fm.get("title"):
                errors.append(f"{rel}: missing title")

        atlas_id = fm.get("atlas_id")
        object_id = fm.get("object_id")

        if atlas_id:
            if atlas_id in atlas_ids:
                errors.append(f"duplicate atlas_id {atlas_id}: {atlas_ids[atlas_id]} and {rel}")
            atlas_ids[atlas_id] = rel

        if object_id:
            if object_id in object_ids:
                errors.append(f"duplicate object_id {object_id}: {object_ids[object_id]} and {rel}")
            object_ids[object_id] = rel

        if fm.get("object_type") == "Screen":
            for required in ["region", "location", "rpg_maker_map_name"]:
                if not fm.get(required):
                    errors.append(f"{rel}: screen missing {required}")

    report = []
    report.append("# Atlas Validation Report\n")
    report.append(f"Files scanned: {len(list(DOCS.rglob('*.md')))}")
    report.append(f"Atlas IDs found: {len(atlas_ids)}")
    report.append(f"Object IDs found: {len(object_ids)}")
    report.append(f"Errors: {len(errors)}")
    report.append(f"Warnings: {len(warnings)}\n")

    if errors:
        report.append("## Errors")
        report.extend(f"- {e}" for e in errors)
    else:
        report.append("## Errors\nNone.")

    report.append("\n## Warnings")
    report.extend(f"- {w}" for w in warnings) if warnings else report.append("None.")

    output = "\n".join(report)
    (REPORTS / "atlas_validation_report.md").write_text(output, encoding="utf-8")
    print(output)

    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())