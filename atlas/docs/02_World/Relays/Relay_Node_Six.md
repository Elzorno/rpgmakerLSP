---
object_id: REL-006
atlas_id: REL-006
title: Relay Node Six
object_type: Relay
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-COA-001
location: LOC-CMN-001
relationships:
  located_in:
    - LOC-CMN-001
  guarded_by: []
  related_to:
    - QST-COA-001
    - CHR-VER-001
---

# Relay Node Six

Relay Node Six is the Coalmouth regional relay tied to industrial control and mining infrastructure.

---

## Purpose

Node Six extends the relay structure introduced by Node Seven and shows the player that each region expresses the hidden system failure differently.

---

## Fantasy Presentation

Coalmouth residents understand Node Six indirectly as mine spirits, deep machinery, old curses, or angry earth.

---

## Hidden Reality

Node Six is an industrial relay connected to control systems, automation, old rail infrastructure, and machinery management.

Its failure manifests as unsafe machine behavior, false signals, and repeating command loops.

---

## Story Function

Node Six should make Vera’s perspective valuable. She recognizes patterns in the machinery before anyone has technical vocabulary for what is happening.

---

## Archive Recovery Effect

Draft target:

```text
ARCHIVE RECOVERY: 10% or 12%
CURRENT RELAY COUNT: 2
```

Final value should be decided after Journey II pacing is locked.

---

## Guardian / Boss

Reserved future boss ID:

```text
BOS-N06-001
```

Draft concept: Iron Foreman, a corrupted mining-control construct enforcing broken work cycles.

---

## Shutdown / Stabilization Sequence

Coalmouth may be better served by stabilizing Node Six rather than simply shutting it down.

Draft sequence:

1. Mine control loop is exposed.
2. Boss/guardian defeated or interrupted.
3. Vera helps interpret the machine rhythm.
4. Sword authenticates the relay.
5. Node Six is isolated from hostile commands.
6. Coalmouth machinery becomes safe enough to use again.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | LOC-CMN-001 | Hidden in Coalmouth Mine infrastructure |
| related_to | CHR-VER-001 | Vera helps interpret the failure |
| advances_quest | QST-COA-001 | Mine crisis relay objective |
| foreshadows | REL-005 | Each relay has a different failure mode |

---

## RPG Maker Implementation Notes

Use existing relay shutdown common-event pattern from Node Seven, but allow text to say STABILIZED or ISOLATED if that better fits the story.

---

## Open Questions

- Should the player-facing result be OFFLINE, STABILIZED, or ISOLATED?
- Should Vera join before the relay interaction?
- Should Node Six unlock a new Protocol Skill related to cleanse/override?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Relay Node Six object |
