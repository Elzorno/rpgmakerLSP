---
atlas_id: ATLAS-TEC-050
title: Atlas Build System Overview
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Planned
dependencies:
  - ATLAS-FND-006
  - ATLAS-FND-008
related:
  - ATLAS-TEC-040
  - ATLAS-TEC-041
  - ATLAS-TEC-042
  - ATLAS-TEC-044
---

# Atlas Build System Overview

The Atlas Build System is the future validation and generation layer for _The Last Sword Protocol_ design repository.

Its purpose is to make Atlas behave less like loose documentation and more like a compiled game-design specification.

---

## Purpose

The build system should eventually answer:

> Is Atlas internally consistent enough for Codex and other agents to implement without inventing missing design details?

---

## Build Philosophy

Atlas should be treated like source code.

That means:

- IDs must be unique.
- References must resolve.
- Required fields must exist.
- Screens must have transfers.
- Events must map to states.
- Implementation packets must have acceptance criteria.
- Playtest checklists must map to real objects.

---

## Proposed Folder Structure

```text
atlas/
  docs/
  schemas/
  validators/
  generators/
  reports/
```

---

## Proposed Commands

Future command names:

```text
atlas validate
atlas build-index
atlas build-nav
atlas trace
atlas report
```

---

## Validation Layers

| Layer | Purpose |
|---|---|
| ID Validation | Confirms Atlas IDs and object IDs are unique |
| Reference Validation | Confirms referenced IDs exist somewhere in Atlas |
| Metadata Validation | Confirms required frontmatter fields exist |
| Screen Validation | Confirms each screen has transfers, events, and acceptance criteria |
| State Validation | Confirms switches/variables have setters and readers |
| Implementation Validation | Confirms implementation packets have acceptance and playtest sections |
| Navigation Validation | Confirms major docs appear in mkdocs navigation or an index |

---

## First Practical Goal

The first version should be simple:

1. Scan all Markdown files under `atlas/docs`.
2. Extract YAML frontmatter.
3. Collect all `atlas_id` and `object_id` values.
4. Flag duplicate IDs.
5. Flag missing required metadata.
6. Generate a simple report.

---

## Non-Goals For Version 0.1

Do not attempt to parse every relationship table yet.

Do not attempt to modify RPG Maker project data yet.

Do not attempt full nav generation yet.

Start with validation and reporting.

---

## Agent Workflow

Codex should eventually run the validator before and after implementation passes.

Claude can use reports to identify missing design content.

The Creative Director can approve status changes from Draft to Locked after validation passes.

---

## Acceptance Criteria

The Atlas Build System is useful when it can produce a clear pass/fail report for Atlas consistency.

First milestone:

```text
No duplicate atlas_id/object_id values
No required frontmatter missing from canonical object pages
No Home Island screen missing from the screen registry
```

---

## Open Questions

- Should the validator be written in Python or Node.js?
- Should it run locally only, or also in GitHub Actions?
- Should generated reports be committed to the repo or treated as build artifacts?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Atlas Build System overview |
