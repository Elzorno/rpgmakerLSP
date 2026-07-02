---
object_id: SCR-HOM-SKY-001
atlas_id: SCR-HOM-SKY-001
title: Skyreach Hill Path
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SKY-001
rpg_maker_map_name: DGN_SkyreachHill_Path
relationships:
  located_in:
    - LOC-SKY-001
  implements:
    - IMP-HOM-003
---

# SCR-HOM-SKY-001 — Skyreach Hill Path

## Purpose

Skyreach Hill Path is the first forbidden-feeling screen after Ashford.

It should make the player feel they have crossed from ordinary village life into old inherited warning.

---

## Map Intent

A narrow uphill path with wind, grass, old stones, and a visible cave entrance near the top.

Recommended approximate size:

```text
30 x 40 tiles
```

---

## Required Visual Elements

- Winding hill path.
- Tall grass and wind-swept stones.
- Geometric carved ruins that look sacred rather than technical.
- Overlook or cliff edge.
- Cave entrance leading to Hidden Cave.
- Optional small landmark for hidden clue or item.

---

## Required Events

| Event | Purpose |
|---|---|
| Entry Gate / Warning | Blocks or warns before access switch |
| Transfer to Hidden Cave | Leads to SCR-HOM-HCV-001 |
| Optional Landmark Examine | Foreshadows authentication geometry |
| Return Transfer | Back toward Ashford / island route |

---

## Story Gate

Before `J1_Skyreach_AccessOpen`, the route should be blocked or strongly discouraged.

After `J1_Skyreach_AccessOpen`, the player can climb to the cave.

---

## Switches Used

```text
J1_Tremor_Event
J1_Skyreach_AccessOpen
J1_HiddenCave_Entered
```

---

## Audio

Use airy hill ambience or sparse sacred theme placeholder.

Include wind as BGS if available.

---

## Encounters

Optional very light encounters only. This screen should focus on mood and destination.

---

## Transfer Points

| Destination | Condition |
|---|---|
| Ashford / island route | Always available |
| SCR-HOM-HCV-001 Hidden Cave Entrance | Requires `J1_Skyreach_AccessOpen` |

---

## Acceptance Criteria

- Player understands this is forbidden/sacred terrain.
- Cave entrance is visually clear.
- Access gate works.
- Player cannot softlock on the hill.
- Screen introduces geometric old-world motifs subtly.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Skyreach Hill Path screen object |
