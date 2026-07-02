---
object_id: LOC-ASH-001
atlas_id: LOC-ASH-001
title: Ashford
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
    - CHR-KAI-001
    - NPC-ELA-001
    - QST-HOM-001
  related_to:
    - LOC-SKY-001
    - LOC-GLS-001
---

# Ashford

Ashford is Kai's home village and the emotional anchor of Journey I.

It should be warm, lived-in, ordinary, and quietly strange.

---

## Purpose

Ashford teaches the player what is worth saving before the adventure begins.

It introduces daily life, Kai's family connection, local folklore, and the first subtle signs that old technology exists beneath the surface.

---

## Player-Facing Description

A small village of timber homes, gardens, warm stone vents, patched fences, and repurposed metal from old ruins.

Villagers think of the old factory bones as useful scrap, sacred leftovers, or harmless oddities.

---

## Hidden Reality

Ashford is built inside and around the shell of an old-world factory or maintenance facility.

Old heat circulation, pipes, vents, and panels still function in limited ways, giving the village unusual warmth and reliable materials.

---

## Map Requirements

Required maps:

- Ashford exterior,
- Kai / Elara house,
- small shop,
- inn or rest house,
- elder/chief house,
- optional interiors.

---

## NPCs

| ID | Name | Role |
|---|---|---|
| CHR-KAI-001 | Kai | Begins here |
| NPC-ELA-001 | Grandmother Elara | Family anchor and keeper of warnings |

Future NPCs should include:

- village elder,
- shopkeeper,
- dock messenger,
- child near old metal panel,
- farmer using warm vent stones,
- villager who jokes about the forbidden hill.

---

## Quests

| ID | Quest | Role |
|---|---|---|
| QST-HOM-001 | Home Island Opening | Establishes Ashford and sends Kai into the first local objective |

---

## Treasure / Secrets

Ashford should include at least one classic hidden item.

Recommended early secret:

> Four steps south of the old warm-stone vent behind Elara's house, Kai can find a minor healing item or old coin.

This nods to classic exploration without copying protected content.

---

## Visual Direction

Warm earth tones, soft greens, golden light, and repurposed old metal used as ordinary building material.

Technology should appear as village texture, not sci-fi.

---

## Audio Direction

Ashford theme should be warm, simple, and hummable.

A subtle low old-world pulse may be audible near factory remnants but should not draw attention early.

---

## Story States

Ashford should change after:

- Kai receives initial local errands,
- the tremor/signal event,
- Kai obtains the Sword,
- Node Seven is shut down,
- Kai departs for the mainland.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | Home Island |
| contains | CHR-KAI-001 | Kai's home village |
| contains | NPC-ELA-001 | Elara's home |
| contains | QST-HOM-001 | Opening quest begins here |
| related_to | LOC-SKY-001 | Elara warns Kai about the hill |
| related_to | LOC-GLS-001 | Village stories reference old ruins |

---

## RPG Maker Implementation Notes

Start with a compact town map. Prioritize readable NPC routes and simple interiors.

Use events to update NPC dialogue by story switch.

Suggested switches:

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Sword_Obtained
J1_Node07_Offline
```

---

## Open Questions

- What is the elder/chief's name?
- Should Ashford have an inn, or should Elara's house function as the first rest point?
- Should the player be able to leave Ashford immediately, or should the first tutorial require talking to Elara?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford location object |
