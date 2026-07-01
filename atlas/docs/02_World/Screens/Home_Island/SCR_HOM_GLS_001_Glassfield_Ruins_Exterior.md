---
object_id: SCR-HOM-GLS-001
atlas_id: SCR-HOM-GLS-001
title: Glassfield Ruins Exterior
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-GLS-001
rpg_maker_map_name: DGN_Glassfield_Ruins_Exterior
relationships:
  located_in:
    - LOC-GLS-001
  implements:
    - IMP-HOM-004
---

# SCR-HOM-GLS-001 — Glassfield Ruins Exterior

## Purpose

Glassfield Ruins Exterior is the first visible old-world ruin screen on Home Island.

It should feel beautiful, familiar, and unsettling before the hidden system is revealed.

---

## Map Intent

An open ruin field with cracked glass-like panels, grass, flowers, broken concrete, and a sealed lower entrance.

Recommended approximate size:

```text
42 x 34 tiles
```

---

## Required Visual Elements

- Cracked glass-like ground panels.
- Flowers growing through concrete.
- Half-buried metal ribs.
- Faint inactive blue-white lights.
- Sealed lower entrance.
- Optional small surface terminal / strange stone.
- Return route to island overworld / Ashford route.

---

## Required Events

| Event | Purpose |
|---|---|
| Sealed Entrance | Blocks access before Sword; opens after Sword |
| Optional Surface Fragment | Can show a small memory fragment or warning |
| Transfer Out | Returns to island route |
| Transfer Down | Leads to SCR-HOM-SND-001 after seal opens |

---

## Seal Logic

Before `J1_Sword_Obtained`, the lower entrance should not open.

After `J1_Sword_Obtained`, interacting with the seal should:

```text
J1_Glassfield_SealOpened = ON
```

Then allow transfer into Sealed Node.

---

## Switches Used

```text
J1_Sword_Obtained
J1_Glassfield_SealOpened
```

---

## Audio

Use quiet ruin exploration music or ambience.

After Sword acquisition, add subtle archive shimmer if possible.

---

## Encounters

Optional low-risk encounters outside the sealed entrance.

Recommended enemies:

- Meadow Gel
- Ash Rat

---

## Acceptance Criteria

- Player can explore ruins before the Sword.
- Lower entrance blocks progress before Sword.
- Lower entrance opens after Sword.
- Seal opening switch is set correctly.
- Transfer to Sealed Node works.
- Ruins visually bridge village folklore and old-world infrastructure.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Glassfield Ruins Exterior screen object |
