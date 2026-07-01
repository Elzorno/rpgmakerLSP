---
object_id: LOC-GLS-001
atlas_id: LOC-GLS-001
title: Glassfield Ruins
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
  contains:
    - LOC-SND-001
  related_to:
    - REL-007
    - QST-HOM-003
---

# Glassfield Ruins

Glassfield Ruins are the first major old-world site the player can explore on Home Island.

They should feel beautiful, broken, and confusing rather than threatening at first.

---

## Purpose

Glassfield teaches the player that the island contains old systems beneath its folklore.

It is the visible surface clue for Relay Node Seven.

---

## Player-Facing Description

A field of cracked glassy stone, metal ribs, flowers growing through concrete, and half-buried walls.

Villagers avoid the deeper sections because lights sometimes flicker under the ground after storms.

---

## Hidden Reality

Glassfield is the exposed upper structure of a secure relay facility and identity socket tied to Node Seven.

Its visible ruins are only the surface of the Sealed Node below.

---

## Map Requirements

Required maps:

- exterior ruins,
- shallow interior/ruin corridors,
- sealed lower entrance,
- transfer path to Sealed Node after Sword authentication.

---

## Quests

| ID | Quest | Role |
|---|---|---|
| QST-HOM-003 | Node Seven Offline | Leads into the Sealed Node climax |

---

## Visual Direction

Soft grass, cracked concrete, glass-like panels, old metal, flowers, and faint blue-white inactive lights.

Old technology should feel like archaeology.

---

## Audio Direction

Quiet exploration music with wind and occasional distant pulse.

After Sword awakening, add subtle archive tones.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | Central Home Island |
| contains | LOC-SND-001 | Sealed Node lies below |
| related_to | REL-007 | Surface structure of Node Seven |
| advances_quest | QST-HOM-003 | Opens after Sword authentication |

---

## RPG Maker Implementation Notes

Use conditional events so the lower entrance is inactive before the Sword and opens afterward.

Suggested switches:

```text
J1_Sword_Obtained
J1_Glassfield_SealOpened
J1_Node07_Offline
```

---

## Open Questions

- Should the player visit Glassfield before Skyreach Hill as foreshadowing?
- Should Glassfield include a low-level puzzle before the main Sealed Node entry?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Glassfield Ruins location object |
