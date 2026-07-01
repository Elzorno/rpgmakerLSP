---
object_id: MON-GEL-002
atlas_id: MON-GEL-002
title: Marsh Gel
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
    - LOC-FOG-001
  drops_item: []
---

# Marsh Gel

Marsh Gel is the Fogfen Marsh variant of the Gel Family.

---

## Purpose

Marsh Gel introduces the idea that familiar enemy families can gain new behavior in different environments.

---

## Fantasy Presentation

A darker, swampy gel creature that bubbles out of marsh pools and clings to boots.

---

## Hidden Reality

An adaptive gel colony influenced by contaminated wetland runoff and submerged old-world cables.

---

## Encounter Role

Early status-teaching enemy.

---

## Behavior

- basic attack,
- slightly more HP than Meadow Gel,
- may inflict low-risk poison or slime status if the design needs an early state tutorial.

---

## Abilities

```text
Attack
Murk Bubble
```

`Murk Bubble` may have a small chance to inflict poison or a minor accuracy debuff.

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, same base silhouette as Meadow Gel, darker green marsh palette, small reed or mud details, faint pale glow, readable and charming but slightly uneasy.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-GEL-001 | Gel Family |
| appears_in | LOC-FOG-001 | Fogfen Marsh |
| foreshadows | REL-007 | Environmental signal disturbance |

---

## RPG Maker Implementation Notes

Use as early variant after player has fought Meadow Gel.

Do not make poison too punishing in the opening region.

---

## Open Questions

- Should poison exist this early, or should Marsh Gel use a harmless debuff first?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Marsh Gel monster object |
