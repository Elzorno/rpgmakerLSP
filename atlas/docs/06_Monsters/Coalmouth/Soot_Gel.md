---
object_id: MON-GEL-003
atlas_id: MON-GEL-003
title: Soot Gel
object_type: Monster
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
family: FAM-GEL-001
relationships:
  belongs_to_family:
    - FAM-GEL-001
  appears_in:
    - REG-COA-001
    - LOC-CMN-001
---

# Soot Gel

Soot Gel is the Coalmouth-region Gel variant.

---

## Purpose

Soot Gel shows that familiar enemy families adapt to regional conditions.

---

## Fantasy Presentation

A dark, smoky gel creature that leaves smudges on mine walls and tools.

---

## Hidden Reality

A gel colony adapted to coal dust, heat, mineral runoff, and old industrial residue.

---

## Encounter Role

Early mainland basic enemy with slightly higher durability than Home Island gels.

---

## Behavior

- basic attack,
- minor blind/accuracy debuff optional,
- pairs well with Ash Rat or Mine Scorpion variants.

---

## Abilities

```text
Attack
Soot Puff
```

`Soot Puff` may slightly reduce accuracy or simply deal minor damage in the first implementation.

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, Gel Family silhouette, dark gray-black soot palette, tiny amber glow flecks, soft smoky edges but clean readable outline.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-GEL-001 | Gel Family |
| appears_in | LOC-CMN-001 | Coalmouth Mine |

---

## RPG Maker Implementation Notes

Use as basic mine enemy after the player has learned Meadow Gel and Marsh Gel behavior.

---

## Open Questions

- Should Soot Puff be a real debuff or cosmetic until balance pass?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Soot Gel monster object |
