---
object_id: FAM-GEL-001
atlas_id: FAM-GEL-001
title: Gel Family
object_type: MonsterFamily
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  contains:
    - MON-GEL-001
    - MON-GEL-002
  appears_in:
    - REG-HOM-001
    - LOC-FOG-001
---

# Gel Family

The Gel Family is the first core monster family for _The Last Sword Protocol_.

Gels fill the classic early-game slime role without copying any specific Dragon Quest monster design.

---

## Purpose

Gels teach the player basic combat, monster families, palette variants, and the idea that nature around old infrastructure behaves strangely.

---

## Fantasy Presentation

Small, bouncy, semi-transparent ooze creatures found in fields, marshes, and damp ruins.

Villagers see them as pests rather than monsters of legend.

---

## Hidden Reality

Gels are adaptive biofilm organisms, chemical waste colonies, or post-collapse gel lifeforms that thrive around old infrastructure runoff.

They are not magical slime.

---

## Silhouette

- Round or teardrop body.
- Simple expressive face.
- Strong readable outline.
- Slight wobble implied by shape.
- No direct imitation of existing slime mascots.

---

## Behavior Pattern

Baseline behavior:

- basic physical attack,
- low HP,
- low threat,
- occasional simple status variant later.

---

## Variant Rules

Variants should be palette-friendly.

Early variants remain cute. Later variants can include embedded glass, wire, or glowing signal cores.

---

## Initial Variants

| ID | Name | Role |
|---|---|---|
| MON-GEL-001 | Meadow Gel | First basic enemy |
| MON-GEL-002 | Marsh Gel | Early status/poison variant |

---

## Art Direction

RPG Maker MZ front-view battler, transparent background, colorful but original, readable silhouette, charming early-game tone.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| contains | MON-GEL-001 | Basic field variant |
| contains | MON-GEL-002 | Marsh variant |
| appears_in | REG-HOM-001 | Home Island enemy family |
| appears_in | LOC-FOG-001 | Marsh variant appears in Fogfen |

---

## RPG Maker Implementation Notes

Use one base battler shape with palette variants.

Recommended database range: early enemy IDs 1–10.

---

## Open Questions

- Should the family be called Gel, Droplet, Puddle, or something else in player-facing text?
- Should Gel enemies make squeaky or wet sound effects?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Gel Family object |
