---
object_id: LOC-RST-001
atlas_id: LOC-RST-001
title: Rustshore Docks
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
    - QST-HOM-003
---

# Rustshore Docks

Rustshore Docks are the small southern harbor of Home Island and the player's eventual exit point to the mainland.

---

## Purpose

Rustshore shows the player that a larger world exists before they are ready to leave.

It becomes meaningful after Node Seven is shut down.

---

## Player-Facing Description

Weathered docks, old ropes, fishing boats, sea grass, and a patched lighthouse made partly from ancient metal.

---

## Hidden Reality

The lighthouse contains fragments of an old sensor or signal array. Dockworkers treat it as stubborn equipment, not technology.

---

## Map Requirements

- dock exterior,
- dockmaster hut,
- lighthouse/event area,
- boat transfer event after unlock.

---

## Story States

Before Node Seven, boats are unavailable due to weather, broken equipment, or local caution.

After Node Seven, the route to the mainland opens.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | South coast of Home Island |
| unlocks | JRN-002 | Mainland departure after Journey I |
| related_to | QST-HOM-003 | Unlocks after Node Seven Offline |

---

## RPG Maker Implementation Notes

Use transfer event gated by `J1_Mainland_TravelUnlocked`.

---

## Open Questions

- Who is the dockmaster?
- Should the lighthouse be optional or required before departure?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Rustshore Docks location object |
