---
object_id: LOC-CMN-001
atlas_id: LOC-CMN-001
title: Coalmouth Mine
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
    - REL-006
  related_to:
    - LOC-COA-001
    - QST-COA-001
---

# Coalmouth Mine

Coalmouth Mine is the first mainland dungeon and the player’s introduction to industrial old-world systems.

---

## Purpose

The mine demonstrates that the world’s problems are connected to broken infrastructure, not isolated curses.

It should feel like a fantasy mine first and an industrial control failure second.

---

## Player-Facing Description

A deep mine of rails, carts, support beams, coal dust, lamp light, locked gates, and old machinery that sometimes moves without workers.

Miners believe the mine spirits are angry.

---

## Hidden Reality

The mine contains old industrial control systems and Relay Node Six infrastructure.

The crisis is caused by degraded automation, bad commands, feedback loops, and corrupted relay influence.

---

## Map Requirements

Required maps:

- mine entrance,
- upper tunnels,
- rail switch chamber,
- old machine room,
- relay control chamber,
- boss arena / Node Six access area.

---

## Gameplay Role

Introduce:

- rail/switch puzzle logic,
- stronger enemy variants,
- Vera’s practical insight,
- first mainland relay shutdown or stabilization.

---

## Visual Direction

Coal, rock, rails, lanterns, gears, control boxes, old panels, warning lights, and cable bundles mistaken for roots or mine veins.

---

## Audio Direction

Low percussion, clanking machinery, distant rail squeal, and a repeating rhythm that becomes unsettling near Node Six.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-COA-001 | Coalmouth Region |
| contains | REL-006 | Node Six hidden in mine infrastructure |
| advances_quest | QST-COA-001 | Main dungeon for mine crisis |
| related_to | CHR-VER-001 | Vera understands the machinery patterns |

---

## RPG Maker Implementation Notes

Use simple evented rail switches and doors. Do not build a complex rail physics system.

Fake machinery behavior with events, movement routes, switches, and sound effects.

---

## Open Questions

- Does Node Six go offline, stabilize, or become trusted after the dungeon?
- Should Vera join before entering the mine or during the mine?
- What boss guards the mine relay?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth Mine location object |
