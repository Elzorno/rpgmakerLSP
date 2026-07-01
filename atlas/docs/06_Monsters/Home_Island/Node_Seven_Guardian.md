---
object_id: BOS-N07-001
atlas_id: BOS-N07-001
title: Node Seven Guardian
object_type: Boss
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  appears_in:
    - LOC-SND-001
  guards:
    - REL-007
  related_to:
    - QST-HOM-003
---

# Node Seven Guardian

Node Seven Guardian is the first major boss of _The Last Sword Protocol_.

The name is a production placeholder. The final player-facing name may be more fantasy-oriented.

---

## Purpose

The Guardian protects Relay Node Seven and teaches the player that some “monsters” are actually old systems still carrying out degraded instructions.

---

## Fantasy Presentation

A sealed guardian beneath the island, believed to be the source or keeper of the island's curse.

---

## Hidden Reality

A degraded security construct or autonomous defense system associated with the secure enclave relay.

It is not evil. It is enforcing old rules without proper context.

---

## Encounter Role

Journey I climax boss.

---

## Behavior

Draft behavior:

- basic attack,
- charged attack every few turns,
- defensive stance or barrier,
- short warning before stronger move.

The fight should be readable and not overly difficult.

---

## Abilities

```text
Strike
Pulse Guard
Warning Tone
Relay Burst
```

`Warning Tone` can telegraph `Relay Burst` on the next turn.

---

## Art Direction

Front-view RPG Maker MZ boss battler, transparent background, ancient stone-and-metal guardian, cave-machine hybrid, blue-white core light with unstable red cracks, readable silhouette, not too horror-heavy, early-game boss scale.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| appears_in | LOC-SND-001 | Sealed Node boss arena |
| guards | REL-007 | Protects Relay Node Seven |
| completes_quest | QST-HOM-003 | Defeat enables relay shutdown |

---

## RPG Maker Implementation Notes

Recommended as first boss troop.

Use simple mechanics and a clear post-defeat switch:

```text
J1_Node07_GuardianDefeated
```

---

## Open Questions

- Final player-facing name?
- Should the guardian be stone, metal, or both?
- Should it visibly power down rather than die?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Node Seven Guardian boss object |
