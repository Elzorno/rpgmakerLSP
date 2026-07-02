---
object_id: LOC-FOG-001
atlas_id: LOC-FOG-001
title: Fogfen Marsh
object_type: Location
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
journey:
  - JRN-001
relationships:
  located_in:
    - REG-HOM-001
  related_to:
    - REG-HOM-001
---

# Fogfen Marsh

Fogfen Marsh is the eastern wetland of Home Island and the first place where nature feels slightly wrong.

---

## Purpose

Fogfen gives the player early combat practice, optional exploration, and the first environmental hint that old signals affect living things.

---

## Player-Facing Description

A misty marsh of reeds, shallow water, bent trees, soft lights, and strange pools that villagers avoid at dusk.

---

## Hidden Reality

Submerged cables and residual electromagnetic fields disturb local wildlife and create odd marsh phenomena.

---

## Map Requirements

- marsh field map,
- deeper marsh pocket,
- optional hidden item landmark,
- possible route clue toward Glassfield.

---

## Enemies / Encounters

Recommended early enemies:

- Marsh Gel,
- Ash Rat,
- Field Crow,
- small marsh predator.

---

## Treasure / Secrets

Include at least one hidden item based on NPC clue or unusual landmark.

---

## Visual Direction

Mist, reeds, muted greens, water reflections, and faint unnatural blue-white or pale violet glows.

---

## Audio Direction

Soft marsh ambience, insects, distant water, and occasional barely-audible signal tick.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | Eastern Home Island |
| teaches | SYS-EXPLORATION-001 | Optional exploration and hidden item logic |
| foreshadows | REL-007 | Signal disturbance hints at hidden infrastructure |

---

## RPG Maker Implementation Notes

Use low-level random encounters or event encounters depending on final design.

Keep the marsh optional unless used as a tutorial objective.

---

## Open Questions

- Should Fogfen be required before Skyreach Hill?
- Should Marsh Gel be the first status-effect enemy?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Fogfen Marsh location object |
