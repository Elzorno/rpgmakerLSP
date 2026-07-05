# BUILD-0036 - Runtime Playtest Findings Triage

## Objective

Convert the first successful post-boot user playtest findings into actionable runtime blockers for the Home Island first journey.

## Source Finding

User playtest report, 2026-07-05:

- Movement works.
- Events trigger a text ID instead of the actual event.
- Maps are not complete, so there are no landmarks to help determine what to do.
- Collision is off. Some blocks are passable and others are not.
- No new runtime errors so far.

## Triage

| Area | Runtime Status | Severity | Issue |
|---|---|---|---|
| Boot/runtime errors | Passing | None | No new runtime errors after BUILD-0035. |
| Player movement | Passing | None | Movement works. |
| Event text | Failing | High | `RT-20260705-001`: event commands show ID-like text instead of readable placeholder copy. |
| Map readability | Failing | Medium | `RT-20260705-002`: maps lack landmarks and route cues. |
| Collision/passability | Failing | High | `RT-20260705-003`: generated block/passability behavior is inconsistent. |

## Recommended Fix Order

1. Replace runtime-visible text IDs with readable placeholder event text while preserving Atlas IDs in comments or metadata.
2. Audit generated tile IDs against RPG Maker tileset passability flags and correct the generated map/tile baseline.
3. Add placeholder landmarks and route cues grounded in Atlas screen/object specifications.

## Current Gate

NO GO.

The first journey has passed boot and basic movement, but it is not yet playable enough for a route-confidence test.
