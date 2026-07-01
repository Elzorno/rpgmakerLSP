---
object_id: MON-RAT-001
atlas_id: MON-RAT-001
title: Ash Rat
object_type: Monster
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
family: FAM-RAT-001
relationships:
  belongs_to_family:
    - FAM-RAT-001
  appears_in:
    - REG-HOM-001
    - LOC-GLS-001
  drops_item: []
---

# Ash Rat

Ash Rat is the first Rat Family variant for Home Island.

---

## Purpose

Ash Rat provides a grounded early enemy that contrasts with stranger gel creatures and old-world constructs.

---

## Fantasy Presentation

A quick gray island rat that nests in warm stones, storage sheds, and old walls.

---

## Hidden Reality

Mostly ordinary wildlife adapted to the warm microclimates created by old factory vents and buried infrastructure.

---

## Encounter Role

Fast early physical enemy.

---

## Behavior

- acts slightly faster than Meadow Gel,
- basic bite attack,
- low HP,
- low-to-medium early damage.

---

## Abilities

```text
Attack
Nibble
```

`Nibble` can be a slightly weaker or slightly faster attack if implemented.

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, small scruffy gray-brown rat, oversized ears, alert pose, charming early JRPG style, no horror, no background.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-RAT-001 | Rat Family |
| appears_in | REG-HOM-001 | Home Island fields and ruins |
| appears_in | LOC-GLS-001 | Glassfield Ruins outskirts |

---

## RPG Maker Implementation Notes

Use as early enemy ID near Gel variants.

Good encounter pairing: one Ash Rat plus one Meadow Gel.

---

## Open Questions

- Should Ash Rat drop a low-value crafting scrap later, or only gold/EXP?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ash Rat monster object |
