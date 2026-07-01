---
object_id: LOC-COA-001
atlas_id: LOC-COA-001
title: Coalmouth
object_type: Location
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-COA-001
journey:
  - JRN-002
relationships:
  located_in:
    - REG-COA-001
  contains:
    - CHR-VER-001
    - QST-COA-001
  related_to:
    - LOC-CMN-001
    - REL-006
---

# Coalmouth

Coalmouth is the first mainland town and the player’s introduction to Journey II’s wider world.

It should feel more worn, pressured, and industrial than Ashford, but still human and worth saving.

---

## Purpose

Coalmouth introduces the theme of broken systems that people depend on.

It also introduces Vera, who gives the party a practical, machine-aware perspective without using modern technical language too early.

---

## Player-Facing Description

A mining town of soot-dark roofs, lamp posts, old rails, pulley towers, coal carts, stubborn workers, and warm lights in narrow streets.

The mine is the town’s livelihood, but lately its machinery has been moving out of rhythm.

---

## Hidden Reality

Coalmouth is built around old industrial infrastructure and degraded control systems.

The “mine spirits” are automation failures, corrupted control loops, and old machinery responding to bad signals.

---

## Map Requirements

Required maps:

- Coalmouth exterior,
- inn/rest house,
- supply shop,
- Vera’s workshop,
- mine office or foreman hut,
- mine entrance.

---

## NPCs

Required first-pass NPC roles:

- Vera,
- foreman,
- worried miner,
- injured worker,
- old railkeeper,
- child who imitates machine rhythms,
- shopkeeper,
- ferry/road guide from Home Island route.

---

## Quests

| ID | Quest | Role |
|---|---|---|
| QST-COA-001 | Coalmouth Mine Crisis | Main regional quest and first mainland node arc |

---

## Visual Direction

Use soot, stone, warm lamps, old rails, scaffolding, and repurposed metal.

Technology should look like mine equipment, control boxes, old rail signals, and strange panels built into practical spaces.

---

## Audio Direction

Work rhythm, low percussion, distant metal clanks, and a subtle repeating machine pattern that becomes more obvious near the mine.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-COA-001 | Coalmouth Region |
| contains | CHR-VER-001 | Vera’s introduction location |
| contains | QST-COA-001 | Mine crisis starts here |
| related_to | LOC-CMN-001 | Town depends on mine |
| related_to | REL-006 | Node Six affects the mine systems |

---

## RPG Maker Implementation Notes

Coalmouth should not exceed Ashford scope by too much in first implementation. Start with a compact town and expand later.

---

## Open Questions

- What is the foreman’s name?
- Is Vera respected, dismissed, or blamed by townspeople?
- Does Coalmouth have a rail gate that becomes functional after the mine crisis?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth location object |
