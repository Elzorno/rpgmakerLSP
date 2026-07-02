---
atlas_id: ATLAS-TEC-051
title: Atlas Validation Rules
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Planned
---

# Atlas Validation Rules

This page lists the first consistency checks for Atlas.

## First Checks

- Every canonical page should have an `atlas_id`.
- Atlas IDs should be unique.
- Object IDs should be unique.
- Canonical pages should have a title.
- Object pages should have an object type.
- Screen pages should identify their region, location, and RPG Maker map name.
- Implementation packets should include acceptance criteria.
- Story-critical states should be traceable to events.

## First Validator Scope

Version 0.1 should only scan Markdown frontmatter and report missing or repeated IDs.

## Later Validator Scope

Later versions can check registries, transfer links, event IDs, state traceability, and implementation packet completeness.

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial validation rule summary |
