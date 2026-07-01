---
object_id: IMP-HOM-009
atlas_id: IMP-HOM-009
title: Home Island Sprint Assembly
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - REG-HOM-001
    - JRN-001
  requires:
    - IMP-HOM-001
    - IMP-HOM-002
    - IMP-HOM-003
    - IMP-HOM-004
    - IMP-HOM-005
    - IMP-HOM-006
    - IMP-HOM-007
    - IMP-HOM-008
---

# Implementation Packet: Home Island Sprint Assembly

## Objective

Define the first complete Codex implementation sprint for Home Island.

This packet orders the existing Home Island implementation packets into a buildable sequence and identifies the minimum playable vertical slice.

---

## Atlas References

| ID | Reference |
|---|---|
| REG-HOM-001 | Home Island |
| JRN-001 | Journey I — The Dreamer |
| IMP-HOM-001 | Build Ashford |
| IMP-HOM-002 | Build Journey I State System |
| IMP-HOM-003 | Build Sword Awakening Sequence |
| IMP-HOM-004 | Build Node Seven Sequence |
| IMP-HOM-005 | Build Home Island Enemy Database |
| IMP-HOM-006 | Build Ashford NPC Dialogue |
| IMP-HOM-007 | Build Home Island Location Art Pipeline |
| IMP-HOM-008 | Build Home Island Audio Hooks |

---

## Sprint Goal

Create a playable Home Island vertical slice from new game start through Node Seven shutdown using placeholder art/audio where needed.

The goal is not polish. The goal is playable continuity.

---

## Recommended Build Order

1. `IMP-HOM-002` — Build Journey I State System
2. `IMP-HOM-001` — Build Ashford
3. `IMP-HOM-006` — Build Ashford NPC Dialogue
4. `IMP-HOM-005` — Build Home Island Enemy Database
5. `IMP-HOM-003` — Build Sword Awakening Sequence
6. `IMP-HOM-004` — Build Node Seven Sequence
7. `IMP-HOM-008` — Build Home Island Audio Hooks
8. `IMP-HOM-007` — Build Home Island Location Art Pipeline

Art can run in parallel, but implementation should not block on final art.

---

## Minimum Playable Slice

The slice is complete when the player can:

1. Start in Ashford.
2. Speak with Elara and villagers.
3. Trigger the tremor event.
4. Access Skyreach Hill.
5. Enter the Hidden Cave.
6. Obtain the Sword.
7. Open Glassfield Ruins.
8. Enter the Sealed Node.
9. Defeat the Node Seven Guardian placeholder.
10. Shut down Relay Node Seven.
11. Unlock mainland travel state.

---

## Required Placeholder Policy

Use placeholders freely for:

- tilesets,
- battlers,
- music,
- sound effects,
- final dialogue,
- portraits,
- animations.

Do not use placeholders for:

- switch names,
- variable names,
- object IDs,
- map naming conventions,
- quest state logic.

Those are canonical and should match Atlas.

---

## Acceptance Criteria

- All Journey I core switches and variables exist.
- Ashford is playable.
- Sword acquisition works.
- Node Seven shutdown works.
- Archive recovery updates from 0 to 3 to 5.
- Mainland travel unlock switch turns on.
- No event softlocks the player.
- Placeholder assets are clearly named and replaceable.

---

## Out of Scope

- Full mainland content.
- Final balance.
- Final art pass.
- Final audio pass.
- Final dialogue polish.
- Optional side quests.

---

## Playtest Exit Criteria

The sprint is ready for review when a tester can complete the slice without manual switch manipulation after starting a new game.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island sprint assembly packet |
