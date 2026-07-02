---
object_id: QST-HOM-001
atlas_id: QST-HOM-001
title: Home Island Opening
object_type: Quest
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
journey: JRN-001
relationships:
  starts_at:
    - LOC-ASH-001
  involves:
    - CHR-KAI-001
    - NPC-ELA-001
  rewards: []
---

# Home Island Opening

The Home Island Opening quest introduces Ashford, Kai, Grandmother Elara, and the basic exploration language of the game.

---

## Purpose

This quest lets the player learn movement, NPC interaction, village tone, and curiosity rewards before the Sword plot begins.

---

## Story Role

Kai begins an ordinary day in Ashford. Small errands and village conversations establish home, folklore, and local warnings.

---

## Starting Conditions

New game begins in or near Kai and Elara's house in Ashford.

---

## Objectives

1. Speak with Grandmother Elara.
2. Explore Ashford.
3. Talk to key villagers.
4. Learn about Skyreach Hill and Glassfield Ruins.
5. Trigger the tremor or signal event that opens the route toward QST-HOM-002.

---

## Key NPCs

| ID | Name | Role |
|---|---|---|
| CHR-KAI-001 | Kai | Player character |
| NPC-ELA-001 | Grandmother Elara | Emotional anchor and warning source |

---

## Completion Conditions

Quest completes when the tremor/signal event occurs and the player receives the next major objective leading toward Skyreach Hill.

---

## Switches

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Skyreach_AccessOpen
```

---

## Variables

None required initially.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| starts_at | LOC-ASH-001 | Quest begins in Ashford |
| involves | NPC-ELA-001 | Elara gives emotional context |
| unlocks | QST-HOM-002 | Leads to Sword awakening |

---

## RPG Maker Implementation Notes

Use simple NPC dialogue events and one story event to trigger the tremor.

Avoid long cutscenes. Let the player move around early.

---

## Playtest Checklist

- Player understands where they are.
- Player meets Elara.
- Player hears about Skyreach Hill.
- Player sees at least one old-world oddity.
- Quest transitions clearly into QST-HOM-002.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island Opening quest object |
