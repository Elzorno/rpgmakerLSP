---
object_id: SCR-HOM-RST-001
atlas_id: SCR-HOM-RST-001
title: Rustshore Docks
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-RST-001
rpg_maker_map_name: TWN_Rustshore_Docks
relationships:
  located_in:
    - LOC-RST-001
  implements:
    - IMP-HOM-013
---

# SCR-HOM-RST-001 — Rustshore Docks

## Purpose

Rustshore Docks is the Home Island departure screen.

It should show the player that a wider world exists, while gating mainland travel until Relay Node Seven has been resolved.

---

## Map Intent

A small coastal dock map with a boat, dockmaster, lighthouse, and route back to the island.

Recommended approximate size:

```text
34 x 26 tiles
```

---

## Required Visual Elements

- Wooden dock and small fishing boat.
- Dockmaster hut.
- Small lighthouse made partly from ancient metal.
- Sea grass and shoreline details.
- Return path to island route.
- Boat transfer point for mainland departure.

---

## Required Events

| Event | Purpose |
|---|---|
| Dockmaster | Explains why travel is blocked or available |
| Boat Transfer | Sends player to mainland route after unlock |
| Lighthouse Examine | Shows subtle old-world signal behavior |
| Transfer Back | Returns to Home Island route / Ashford route |

---

## Travel Gate

Before Node Seven resolution:

```text
J1_Mainland_TravelUnlocked = OFF
```

The boat transfer should be blocked with dockmaster dialogue.

After Node Seven resolution:

```text
J1_Mainland_TravelUnlocked = ON
```

The player can depart for Journey II / Coalmouth route.

---

## Switches Used

```text
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

---

## Audio

Use coastal BGM or BGS placeholder with waves.

After Node Seven, lighthouse tone should feel steadier if represented.

---

## Encounters

None on dock screen.

---

## Acceptance Criteria

- Player can visit docks before mainland travel is unlocked.
- Boat departure is blocked before `J1_Mainland_TravelUnlocked`.
- Boat departure becomes available after `J1_Mainland_TravelUnlocked`.
- Dockmaster dialogue reflects both states.
- Lighthouse reinforces hidden technology subtly.
- Player can return to Home Island route.

---

## Open Questions

- Should mainland travel go directly to Coalmouth or to a short world-map crossing screen?
- Should dockmaster become a named NPC object?
- Should lighthouse behavior change visibly after Node Seven?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Rustshore Docks screen object |
