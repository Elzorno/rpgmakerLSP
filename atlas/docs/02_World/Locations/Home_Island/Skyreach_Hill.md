---
object_id: LOC-SKY-001
atlas_id: LOC-SKY-001
title: Skyreach Hill
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
    - LOC-HCV-001
  related_to:
    - LOC-ASH-001
    - QST-HOM-002
---

# Skyreach Hill

Skyreach Hill is the forbidden northern landmark of Home Island.

It is where Kai first crosses from childhood curiosity into inherited responsibility.

---

## Purpose

Skyreach Hill creates the first major destination mystery.

The player should hear about it before they can safely understand it.

---

## Player-Facing Description

A wind-cut hill with old stones, strange carvings, and a cave entrance hidden near the top.

Villagers say the hill is unlucky, sacred, or cursed depending on who is asked.

---

## Hidden Reality

Skyreach Hill conceals physical security layers around the Project Excalibur Vaultlet.

Its carvings and trial spaces are degraded access-control architecture interpreted as ritual space.

---

## Map Requirements

Required maps:

- hill path exterior,
- upper hill overlook,
- cave entrance,
- optional small landmark for hidden clue or item.

---

## Quests

| ID | Quest | Role |
|---|---|---|
| QST-HOM-002 | The Sword Awakens | Main route to Hidden Cave and Project Excalibur |

---

## Visual Direction

Open sky, wind, old stone, grass, and subtle geometric security motifs.

Technology should appear as sacred geometry or ancient carvings.

---

## Audio Direction

Sparse wind and a faint high harmonic tone near the cave entrance.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | Northern Home Island |
| contains | LOC-HCV-001 | Hidden Cave / Excalibur Vaultlet |
| advances_quest | QST-HOM-002 | Leads to Sword awakening |
| related_to | NPC-ELA-001 | Elara warns Kai about this place |

---

## RPG Maker Implementation Notes

Gate access behind story switch after tremor or Elara warning.

Suggested switches:

```text
J1_Tremor_Event
J1_Skyreach_AccessOpen
```

---

## Open Questions

- Should the hill be reachable before the tremor but blocked by a warning?
- Should an optional hidden item foreshadow the Sword here?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Skyreach Hill location object |
