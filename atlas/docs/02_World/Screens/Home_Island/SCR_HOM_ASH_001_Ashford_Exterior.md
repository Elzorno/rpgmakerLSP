---
object_id: SCR-HOM-ASH-001
atlas_id: SCR-HOM-ASH-001
title: Ashford Exterior
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-ASH-001
rpg_maker_map_name: TWN_Ashford_Exterior
relationships:
  located_in:
    - LOC-ASH-001
  contains:
    - NPC-ELA-001
    - QST-HOM-001
  implements:
    - IMP-HOM-001
---

# SCR-HOM-ASH-001 — Ashford Exterior

## Purpose

Ashford Exterior is the first exterior screen of the game and the player's first impression of the world.

It must establish warmth, ordinary life, hidden old-world remnants, and curiosity.

---

## Map Intent

A compact village exterior with clear navigation and several small points of interest.

Recommended approximate size:

```text
40 x 32 tiles
```

This can be adjusted during implementation, but the map should remain small enough to understand quickly.

---

## Required Visual Elements

- Elara/Kai house visible near the starting area.
- Warm-stone vent behind or near Elara's house.
- Reused metal panels as fences or wall pieces.
- Village center or common path.
- Shop exterior.
- Elder house exterior.
- North path toward Skyreach Hill.
- South/east path toward Rustshore or island overworld.
- At least one child near an old humming panel.

---

## Required Events

| Event | Purpose |
|---|---|
| Transfer to Elara House | Connects to SCR-HOM-ASH-002 |
| Transfer to Shop | Connects to SCR-HOM-ASH-003 |
| Transfer to Elder House | Placeholder interior |
| Hidden Item Event | Four steps south of warm-stone vent |
| Child Near Old Panel | Old tech as play |
| Farmer With Warm Stones | Old tech as daily utility |
| Skyreach Joker | Reinforces hill taboo |
| Dock Messenger | Foreshadows Rustshore |
| North Exit | Toward Skyreach / island route |
| South Exit | Toward Rustshore / island route |

---

## NPC Placement

| NPC Role | Placement |
|---|---|
| Child Near Old Panel | West or central old metal wall |
| Farmer With Warm Stones | Garden patch near vent |
| Skyreach Joker | Near northern path |
| Dock Messenger | Near southern road |
| Village Elder | Outside elder house or central square |

---

## Hidden Item

Classic exploration nod:

```text
Four steps south of the warm-stone vent behind Elara's house.
```

Reward placeholder:

```text
Minor healing item or old coin
```

Event must self-switch after collection.

---

## Story States

This screen must support:

```text
STATE_01_INTRO
STATE_02_AFTER_TREMOR
STATE_03_AFTER_SWORD
STATE_04_AFTER_NODE07
STATE_05_BEFORE_MAINLAND_DEPARTURE
```

---

## Switches Used

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Sword_Obtained
J1_Node07_Offline
NPC_Ashford_PostNode07
```

---

## Audio

Use Ashford town BGM placeholder.

Optional ambient old vent sound near warm-stone vent.

---

## Encounters

No random encounters inside village.

---

## Transfer Points

| Destination | Condition |
|---|---|
| SCR-HOM-ASH-002 Elara House | Always available |
| SCR-HOM-ASH-003 Shop | Always available |
| Skyreach route | Blocked until `J1_Skyreach_AccessOpen` |
| Rustshore route | Available as world route, but mainland departure blocked until later |

---

## Acceptance Criteria

- Player can navigate the village without confusion.
- Required NPC placeholders exist.
- Hidden item works once.
- Transfers work.
- North route can be gated by story switch.
- Screen communicates warm village + subtle old technology.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford Exterior screen object |
