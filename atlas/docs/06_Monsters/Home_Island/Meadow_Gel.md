---
object_id: MON-GEL-001
atlas_id: MON-GEL-001
title: Meadow Gel
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
    - REG-HOM-001
    - LOC-ASH-001
  drops_item: []
---

# Meadow Gel

Meadow Gel is the baseline early-game Gel variant.

---

## Purpose

Meadow Gel is likely one of the first enemies the player fights.

It should be harmless-looking, readable, and useful for teaching basic combat.

---

## Fantasy Presentation

A small greenish-blue gel creature found in fields and damp grass around Home Island.

---

## Hidden Reality

A low-risk adaptive gel organism thriving in wet soil and old infrastructure runoff.

---

## Encounter Role

First-tier basic enemy.

---

## Behavior

- basic attack,
- low HP,
- low damage,
- no status effects.

---

## Abilities

```text
Attack
```

Optional later:

```text
Wobble
```

A harmless or low-impact move that wastes a turn or slightly lowers defense.

---

## Drops / Rewards

Draft rewards:

- small gold,
- very low chance minor healing item.

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, charming original gel creature, green-blue palette, round readable shape, simple expressive face, no text, no background.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-GEL-001 | Gel Family |
| appears_in | REG-HOM-001 | Home Island fields |
| teaches | SYS-COMBAT-001 | Basic attack/defeat loop |

---

## RPG Maker Implementation Notes

Recommended as Enemy ID 1 if database is clean.

Use simple stats and default attack.

---

## Open Questions

- Should Meadow Gel be the very first random encounter?
- Should it have a rare item drop?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Meadow Gel monster object |
