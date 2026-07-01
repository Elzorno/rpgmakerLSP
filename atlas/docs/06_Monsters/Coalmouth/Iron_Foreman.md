---
object_id: BOS-N06-001
atlas_id: BOS-N06-001
title: Iron Foreman
object_type: Boss
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  appears_in:
    - LOC-CMN-001
  guards:
    - REL-006
  related_to:
    - QST-COA-001
    - CHR-VER-001
---

# Iron Foreman

Iron Foreman is the draft boss concept for the Coalmouth Mine Crisis and Relay Node Six.

---

## Purpose

Iron Foreman embodies broken labor automation and unsafe command loops.

It is not evil. It is a degraded control construct still enforcing work cycles after context has failed.

---

## Fantasy Presentation

A towering mine overseer spirit made of iron, coal, chains, signal lamps, and grinding tools.

Miners believe it punishes those who anger the deep mine.

---

## Hidden Reality

A corrupted industrial supervisory construct or control platform enforcing invalid commands through old mining equipment.

---

## Encounter Role

Journey II first regional boss.

---

## Behavior

- physical strikes,
- summons or activates mine hazards,
- uses command-like buffs on construct enemies,
- telegraphs heavy machine attacks.

---

## Abilities

```text
Overtime Order
Piston Slam
Warning Bell
Shift Collapse
```

`Warning Bell` should telegraph `Shift Collapse` or another heavy attack.

---

## Art Direction

Front-view RPG Maker MZ boss battler, transparent background, industrial mine guardian made of iron plates, coal dust, chains, old signal lamps, heavy tool-like arms, amber furnace glow, authoritative foreman silhouette, original design, not demonic.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| appears_in | LOC-CMN-001 | Mine boss arena |
| guards | REL-006 | Protects or embodies Node Six failure |
| completes_quest | QST-COA-001 | Defeat enables stabilization |
| related_to | CHR-VER-001 | Vera helps interpret the system failure |

---

## RPG Maker Implementation Notes

Use readable attack patterns. Avoid complex multi-phase mechanics in first implementation.

Suggested switch:

```text
J2_Node06_GuardianDefeated
```

---

## Open Questions

- Should Iron Foreman be defeated, shut down, or re-tasked?
- Should Vera have a special interaction during the fight?
- Should it summon Soot Gels or Coal Golems?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Iron Foreman boss object |
