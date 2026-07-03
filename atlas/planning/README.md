# Atlas Planner Queue

`workorder_queue.json` is the editable candidate queue used by:

```text
/usr/bin/python3 atlas-tools/cli/atlas.py next
```

The planner reads candidates in priority order, skips candidates already represented by an open work order, and writes the selected candidate into the next `atlas/workorders/WO-####-slug.md` file.

## Candidate Fields

Each candidate must include:

- `title`: Human-readable work order title.
- `slug`: Filename slug after the `WO-####-` prefix.
- `milestone`: Roadmap or production milestone this candidate advances.
- `priority`: Lower numbers are selected first.
- `rationale`: Why this work order should exist.
- `goal`: Work order goal text.
- `files_to_inspect`: Source files the implementer should read first.
- `expected_outputs`: Files or outputs the work order should produce.
- `required_tasks`: Numbered task list for the generated work order.
- `constraints`: Guardrails for the generated work order.
- `validation_commands`: Commands required to verify the work order.
- `deliverable_sections`: Implementation report headings.
- `dependencies`: Dependency notes included in the planning rationale.

Optional fields:

- `active`: Set to `false` to keep a candidate in the queue but prevent generation.

The generator fails with a clear error if the queue file is missing, malformed, or missing required fields.
