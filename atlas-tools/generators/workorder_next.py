#!/usr/bin/env python3
"""Generate the next Atlas work order."""

from __future__ import annotations

from dataclasses import dataclass
import json
from json import JSONDecodeError
from pathlib import Path
import re
import sys


WORKORDER_PREFIX = re.compile(r"^WO-(\d{4})(?:\b|[-_ ].*)")
WORKORDER_VALID = re.compile(r"^WO-(\d{4}).*\.md$")
WORKORDER_LIKE = re.compile(r"^WO-")
TEMPLATE_NAME = "workorder_template.md"
QUEUE_PATH = Path("atlas") / "planning" / "workorder_queue.json"
ATLAS_DOC_LINK = re.compile(r"`(atlas/docs/[^`]+?\.md)`")
REQUIRED_CANDIDATE_FIELDS = (
    "title",
    "slug",
    "milestone",
    "priority",
    "rationale",
    "goal",
    "files_to_inspect",
    "expected_outputs",
    "required_tasks",
    "constraints",
    "validation_commands",
    "deliverable_sections",
    "dependencies",
)


@dataclass(frozen=True)
class WorkOrder:
    number: int
    title: str
    path: Path
    text: str
    target_paths: tuple[str, ...]
    completed: bool


@dataclass(frozen=True)
class Candidate:
    title: str
    slug: str
    milestone: str
    priority: int
    rationale: str
    goal: str
    files_to_inspect: tuple[str, ...]
    expected_outputs: tuple[str, ...]
    required_tasks: tuple[str, ...]
    constraints: tuple[str, ...]
    validation_commands: tuple[str, ...]
    deliverable_sections: tuple[str, ...]
    dependencies: tuple[str, ...]


def find_repo_root(start: Path) -> Path:
    for path in [start, *start.parents]:
        if (path / "atlas").is_dir() and (path / "atlas-tools").is_dir():
            return path
    raise RuntimeError("Could not locate repository root containing atlas/ and atlas-tools/")


def audit_workorders(workorders_dir: Path) -> dict[int, list[Path]]:
    workorders: dict[int, list[Path]] = {}
    malformed: list[Path] = []

    for path in sorted(workorders_dir.iterdir()):
        if not WORKORDER_LIKE.match(path.name):
            continue

        prefix_match = WORKORDER_PREFIX.match(path.name)
        if not prefix_match:
            malformed.append(path)
            continue

        if not path.is_file():
            malformed.append(path)
            continue

        if path.suffix != ".md":
            malformed.append(path)
            continue

        valid_match = WORKORDER_VALID.match(path.name)
        if not valid_match:
            malformed.append(path)
            continue

        number = int(valid_match.group(1))
        workorders.setdefault(number, []).append(path)

    duplicate_numbers = {number: paths for number, paths in workorders.items() if len(paths) > 1}
    if malformed or duplicate_numbers:
        messages = ["Cannot generate next work order until atlas/workorders is unambiguous."]
        if malformed:
            messages.append("Malformed workorder-like entries:")
            messages.extend(f"- {path.name}" for path in malformed)
        if duplicate_numbers:
            messages.append("Duplicate work order numbers:")
            for number, paths in sorted(duplicate_numbers.items()):
                names = ", ".join(path.name for path in paths)
                messages.append(f"- WO-{number:04d}: {names}")
        raise RuntimeError("\n".join(messages))

    return workorders


def next_workorder_number(workorders_dir: Path) -> int:
    workorders = audit_workorders(workorders_dir)
    return max(workorders, default=0) + 1


def parse_workorders(repo_root: Path, workorders_dir: Path) -> list[WorkOrder]:
    audited = audit_workorders(workorders_dir)
    workorders: list[WorkOrder] = []

    validation_clean = is_validation_clean(repo_root / "atlas-tools" / "reports" / "atlas_validation_report.md")
    for number, paths in sorted(audited.items()):
        path = paths[0]
        text = path.read_text(encoding="utf-8")
        title = parse_title(text, path.stem)
        target_paths = tuple(sorted(set(ATLAS_DOC_LINK.findall(text))))
        completed = is_completed_workorder(repo_root, title, text, target_paths, validation_clean)
        workorders.append(
            WorkOrder(
                number=number,
                title=title,
                path=path,
                text=text,
                target_paths=target_paths,
                completed=completed,
            )
        )

    return workorders


def parse_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            title = re.sub(r"^#\s+WO-\d{4}\s+[-—]\s+", "", line).strip()
            return title or fallback
    return fallback


def is_completed_workorder(
    repo_root: Path,
    title: str,
    text: str,
    target_paths: tuple[str, ...],
    validation_clean: bool,
) -> bool:
    lower_title = title.lower()
    lower_text = text.lower()
    if "validation cleanup" in lower_title and validation_clean:
        return True

    if "validation result" in lower_text and "0 errors" in lower_text and "0 warnings" in lower_text:
        return True

    if target_paths and all((repo_root / target_path).exists() for target_path in target_paths):
        return True

    return False


def is_validation_clean(report_path: Path) -> bool:
    if not report_path.exists():
        return False
    text = report_path.read_text(encoding="utf-8")
    return "- Errors: 0" in text and "- Warnings: 0" in text


def slugify_title(title: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title.lower())
    return "-".join(words)


def render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def load_candidates(repo_root: Path) -> list[Candidate]:
    queue_path = repo_root / QUEUE_PATH
    if not queue_path.exists():
        raise RuntimeError(f"Planner queue file is missing: {queue_path.relative_to(repo_root)}")

    try:
        payload = json.loads(queue_path.read_text(encoding="utf-8"))
    except JSONDecodeError as error:
        raise RuntimeError(
            f"Planner queue file is malformed JSON: {queue_path.relative_to(repo_root)}:{error.lineno}:{error.colno} {error.msg}"
        ) from error

    if not isinstance(payload, dict):
        raise RuntimeError("Planner queue file must contain a JSON object.")

    raw_candidates = payload.get("candidates")
    if not isinstance(raw_candidates, list):
        raise RuntimeError("Planner queue file must include a `candidates` array.")

    candidates: list[Candidate] = []
    for index, raw_candidate in enumerate(raw_candidates, 1):
        if not isinstance(raw_candidate, dict):
            raise RuntimeError(f"Planner queue candidate #{index} must be a JSON object.")
        if raw_candidate.get("active", True) is False:
            continue

        missing = [field for field in REQUIRED_CANDIDATE_FIELDS if field not in raw_candidate]
        if missing:
            raise RuntimeError(f"Planner queue candidate #{index} missing required field(s): {', '.join(missing)}")

        title = require_text(raw_candidate, "title", index)
        slug = require_slug(raw_candidate, index)
        milestone = require_text(raw_candidate, "milestone", index)
        priority = require_int(raw_candidate, "priority", index)
        rationale = require_text(raw_candidate, "rationale", index)
        goal = require_text(raw_candidate, "goal", index)
        files_to_inspect = require_text_list(raw_candidate, "files_to_inspect", index)
        expected_outputs = require_text_list(raw_candidate, "expected_outputs", index)
        required_tasks = require_text_list(raw_candidate, "required_tasks", index)
        constraints = require_text_list(raw_candidate, "constraints", index)
        validation_commands = require_text_list(raw_candidate, "validation_commands", index)
        deliverable_sections = require_text_list(raw_candidate, "deliverable_sections", index)
        dependencies = require_text_list(raw_candidate, "dependencies", index)

        candidates.append(
            Candidate(
                title=title,
                slug=slug,
                milestone=milestone,
                priority=priority,
                rationale=rationale,
                goal=goal,
                files_to_inspect=files_to_inspect,
                expected_outputs=expected_outputs,
                required_tasks=required_tasks,
                constraints=constraints,
                validation_commands=validation_commands,
                deliverable_sections=deliverable_sections,
                dependencies=dependencies,
            )
        )

    if not candidates:
        raise RuntimeError("Planner queue has no active candidates.")

    return candidates


def require_text(candidate: dict[str, object], field: str, index: int) -> str:
    value = candidate[field]
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Planner queue candidate #{index} field `{field}` must be a non-empty string.")
    return value.strip()


def require_slug(candidate: dict[str, object], index: int) -> str:
    slug = require_text(candidate, "slug", index)
    if slugify_title(slug) != slug:
        raise RuntimeError(
            f"Planner queue candidate #{index} field `slug` must contain lowercase letters, numbers, and hyphens only."
        )
    return slug


def require_int(candidate: dict[str, object], field: str, index: int) -> int:
    value = candidate[field]
    if not isinstance(value, int):
        raise RuntimeError(f"Planner queue candidate #{index} field `{field}` must be an integer.")
    return value


def require_text_list(candidate: dict[str, object], field: str, index: int) -> tuple[str, ...]:
    value = candidate[field]
    if not isinstance(value, list) or not value:
        raise RuntimeError(f"Planner queue candidate #{index} field `{field}` must be a non-empty array.")
    items: list[str] = []
    for item_index, item in enumerate(value, 1):
        if not isinstance(item, str) or not item.strip():
            raise RuntimeError(
                f"Planner queue candidate #{index} field `{field}` item #{item_index} must be a non-empty string."
            )
        items.append(item.strip())
    return tuple(items)


def candidate_is_duplicate(candidate: Candidate, workorders: list[WorkOrder]) -> bool:
    candidate_title = normalize_text(candidate.title)
    candidate_targets = set(candidate.expected_outputs)
    for workorder in workorders:
        if workorder.completed:
            continue
        if normalize_text(workorder.title) == candidate_title:
            return True
        if candidate_targets and candidate_targets.intersection(workorder.text.split()):
            return True
        if candidate_targets and any(target in workorder.text for target in candidate_targets):
            return True
    return False


def normalize_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def choose_candidate(candidates: list[Candidate], workorders: list[WorkOrder]) -> tuple[Candidate, list[str]]:
    skipped: list[str] = []
    for candidate in sorted(candidates, key=lambda item: item.priority):
        if candidate_is_duplicate(candidate, workorders):
            skipped.append(f"{candidate.title}: already present in an open work order")
            continue
        return candidate, skipped

    raise RuntimeError(
        "No nonduplicate unfinished work order candidate found.\n"
        + "\n".join(f"- {item}" for item in skipped)
    )


def build_planning_rationale(candidate: Candidate, workorders: list[WorkOrder], skipped: list[str]) -> str:
    completed = [workorder for workorder in workorders if workorder.completed]
    open_items = [workorder for workorder in workorders if not workorder.completed]
    lines = [
        f"- Selected milestone: {candidate.milestone}.",
        f"- Decision: {candidate.rationale}",
        f"- Completed work orders considered: {len(completed)}.",
        f"- Open work orders considered: {len(open_items)}.",
    ]
    if candidate.dependencies:
        lines.append("- Dependencies:")
        lines.extend(f"  - {dependency}" for dependency in candidate.dependencies)
    if skipped:
        lines.append("- Skipped duplicate candidates:")
        lines.extend(f"  - {item}" for item in skipped)
    return "\n".join(lines)


def build_workorder(repo_root: Path, workorder_id: str, candidate: Candidate, workorders: list[WorkOrder], skipped: list[str]) -> str:
    template_path = repo_root / "atlas-tools" / "templates" / TEMPLATE_NAME
    template = template_path.read_text(encoding="utf-8")

    values = {
        "WORK_ORDER_ID": workorder_id,
        "TITLE": candidate.title,
        "GOAL": candidate.goal,
        "PLANNING_RATIONALE": build_planning_rationale(candidate, workorders, skipped),
        "READ_FIRST": "\n".join(f"- `{path}`" for path in candidate.files_to_inspect),
        "REQUIRED_TASKS": "\n".join(f"{index}. {task}" for index, task in enumerate(candidate.required_tasks, 1)),
        "CONSTRAINTS": "\n".join(f"- {constraint}" for constraint in candidate.constraints),
        "VALIDATION": "\n".join(f"- `{command}`" for command in candidate.validation_commands),
        "DELIVERABLE": "\n".join(
            ["Produce an Implementation Report with:", ""]
            + [f"## {section}" for section in candidate.deliverable_sections]
            + ["", "Do not commit."]
        ),
    }
    return render_template(template, values)


def main() -> int:
    try:
        repo_root = find_repo_root(Path(__file__).resolve())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    workorders_dir = repo_root / "atlas" / "workorders"
    workorders_dir.mkdir(parents=True, exist_ok=True)

    try:
        number = next_workorder_number(workorders_dir)
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    workorders = parse_workorders(repo_root, workorders_dir)
    try:
        candidates = load_candidates(repo_root)
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    try:
        candidate, skipped = choose_candidate(candidates, workorders)
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    workorder_id = f"WO-{number:04d}"
    filename = f"{workorder_id}-{candidate.slug}.md"
    output_path = workorders_dir / filename

    if output_path.exists():
        print(f"Work order already exists: {output_path.relative_to(repo_root)}", file=sys.stderr)
        return 1

    output_path.write_text(build_workorder(repo_root, workorder_id, candidate, workorders, skipped), encoding="utf-8")
    print(output_path.relative_to(repo_root).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
