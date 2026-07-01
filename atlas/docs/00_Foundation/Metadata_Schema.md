---
atlas_id: ATLAS-FND-004
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-003
related:
  - ATLAS-FND-005
---

# Metadata Schema

Every Atlas page begins with YAML front matter.

Metadata allows humans and AI agents to understand the status, dependencies, and production role of each page.

---

## Required Metadata

```yaml
---
atlas_id: ATLAS-XXX-000
title: Page Title
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
dependencies: []
related: []
---
```

---

## Field Definitions

| Field | Meaning |
|---|---|
| atlas_id | Stable ID assigned by the Atlas ID Specification |
| title | Human-readable page title |
| status | Draft, Review, Approved, or Locked |
| version | Document version |
| canonical | Whether the page is currently authoritative |
| owner | Role responsible for page direction |
| implementation_status | Not Applicable, Not Started, In Progress, Implemented, Needs Revision |
| dependencies | Atlas IDs or page names that must be read first |
| related | Related Atlas IDs or page names |

---

## Status Values

### Draft

The page is being actively developed and should not be treated as final.

### Review

The page is ready for critique and consistency checking.

### Approved

The page is directionally accepted but may still receive refinements.

### Locked

The page is canonical for implementation. Changes require revision notes.

---

## Implementation Status Values

| Value | Meaning |
|---|---|
| Not Applicable | Page is not directly implemented |
| Not Started | No implementation work done |
| In Progress | Implementation has started |
| Implemented | Implementation matches this page |
| Needs Revision | Implementation or design has diverged |

---

## Optional Metadata

Use optional fields for production pages:

```yaml
journey: I
region: Home Island
map_ids: []
asset_status: Not Started
writing_status: Not Started
art_status: Not Started
rpgmaker_status: Not Started
```

---

## AI Interpretation Rule

AI agents must not treat `Draft` pages as final unless the user explicitly authorizes temporary use.

AI agents may implement from `Approved` or `Locked` pages.

`Locked` pages take priority over conflicting lower-status pages.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial metadata schema |
