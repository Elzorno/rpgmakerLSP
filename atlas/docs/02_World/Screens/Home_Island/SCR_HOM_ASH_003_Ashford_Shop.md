---
object_id: SCR-HOM-ASH-003
atlas_id: SCR-HOM-ASH-003
title: Ashford Shop Interior
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-ASH-001
rpg_maker_map_name: INT_Ashford_Shop
relationships:
  located_in:
    - LOC-ASH-001
  implements:
    - IMP-HOM-001
    - IMP-HOM-006
---

# SCR-HOM-ASH-003 — Ashford Shop Interior

## Purpose

Ashford Shop introduces basic item economy and practical preparation before leaving town.

---

## Map Intent

Small shop interior with a counter, shelves, and one shopkeeper event.

Recommended approximate size:

```text
15 x 11 tiles
```

---

## Required Visual Elements

- Counter.
- Shelves/barrels/crates.
- Shopkeeper.
- Door transfer back to Ashford Exterior.
- Optional old metal storage cabinet treated as normal furniture.

---

## Required Events

| Event | Purpose |
|---|---|
| Shopkeeper | Dialogue and shop processing |
| Transfer Exit | Leads to SCR-HOM-ASH-001 |
| Optional Cabinet Examine | Tiny old-world oddity line |

---

## Suggested Shop Inventory

First pass inventory should be simple:

- minor healing item,
- antidote or equivalent if poison exists early,
- basic utility item if available,
- no expensive gear yet.

---

## Story States

At minimum:

```text
Intro
After Node Seven
```

---

## Switches Used

```text
J1_Node07_Offline
NPC_Ashford_PostNode07
```

---

## Audio

Ashford interior/town BGM placeholder.

---

## Encounters

None.

---

## Acceptance Criteria

- Player can enter and exit shop.
- Shopkeeper dialogue works.
- Shop processing works or has placeholder message.
- Inventory does not break early-game balance.

---

## Open Questions

- Should Ashford sell antidotes if Marsh Gel poison is enabled?
- Should shop inventory change after Node Seven?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford Shop screen object |
