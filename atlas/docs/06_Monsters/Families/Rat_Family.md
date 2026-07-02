---
object_id: FAM-RAT-001
atlas_id: FAM-RAT-001
title: Rat Family
object_type: MonsterFamily
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  contains:
    - MON-RAT-001
  appears_in:
    - REG-HOM-001
    - LOC-ASH-001
    - LOC-GLS-001
---

# Rat Family

The Rat Family is an early low-threat wildlife family used in fields, storage areas, caves, and ruins.

---

## Purpose

Rats provide a familiar early enemy that grounds the world before stranger monsters appear.

---

## Fantasy Presentation

Scrappy island pests that steal grain, nest in old walls, and startle travelers near ruins.

---

## Hidden Reality

Ordinary wildlife thriving around abandoned infrastructure and food stores.

Later variants may show effects of old-world signal or industrial exposure.

---

## Silhouette

- Small body.
- Large ears.
- Curved tail.
- Alert posture.
- Slightly exaggerated JRPG readability.

---

## Behavior Pattern

- quick basic attack,
- low HP,
- may act before Gel enemies,
- teaches that not all monsters are magical.

---

## Initial Variants

| ID | Name | Role |
|---|---|---|
| MON-RAT-001 | Ash Rat | Home Island early pest |

---

## Art Direction

Charming but scruffy RPG Maker MZ front-view battler. Avoid realistic horror.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| contains | MON-RAT-001 | Early Home Island rat variant |
| appears_in | REG-HOM-001 | Home Island |
| appears_in | LOC-GLS-001 | Ruins and fields |

---

## RPG Maker Implementation Notes

Use as early enemy ID near Gel variants.

Simple attack only in first implementation.

---

## Open Questions

- Should Ash Rat appear in random encounters near Ashford or only in small event encounters?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Rat Family object |
