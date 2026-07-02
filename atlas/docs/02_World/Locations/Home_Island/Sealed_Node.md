---
object_id: LOC-SND-001
atlas_id: LOC-SND-001
title: Sealed Node
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
    - LOC-GLS-001
  contains:
    - REL-007
  related_to:
    - QST-HOM-003
---

# Sealed Node

The Sealed Node is the Journey I climax dungeon beneath Glassfield Ruins.

It is the first place where fantasy cave language and old-world infrastructure begin to visibly overlap.

---

## Purpose

The Sealed Node proves that Ashford and Home Island were never separate from the larger mystery.

It gives the player the first relay shutdown and establishes the archive recovery pattern.

---

## Player-Facing Description

A sealed underground ruin where stone corridors give way to strange glowing panels, humming walls, and an inner chamber said to hold the island's curse.

---

## Hidden Reality

The Sealed Node is the lower facility housing Relay Node Seven, a secure enclave relay tied to Project Excalibur.

Its guardian systems remain active but degraded.

---

## Map Requirements

Required maps:

- upper sealed corridor,
- cave-machine hybrid passage,
- relay approach chamber,
- guardian/boss arena,
- relay core chamber.

---

## Relay

| ID | Relay | Role |
|---|---|---|
| REL-007 | Node Seven | First relay node shutdown |

---

## Visual Direction

Start as cave/ruin. Progress toward visible panels, cables, glass, and inactive machinery.

This dungeon should be the first controlled visual reveal of the hidden layer.

---

## Audio Direction

Low hum, distant pulses, cave ambience, and a short clean chime after Node Seven goes offline.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | LOC-GLS-001 | Beneath Glassfield Ruins |
| contains | REL-007 | Node Seven relay core |
| completes_quest | QST-HOM-003 | Journey I climax objective |
| related_to | ITM-SWD-001 | Sword enables access and shutdown |

---

## RPG Maker Implementation Notes

Use a boss troop before the relay core.

Suggested switches:

```text
J1_SealedNode_Entered
J1_Node07_GuardianDefeated
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

Suggested variable update:

```text
Archive_Recovery_Percent = 5
```

---

## Open Questions

- What is the Node Seven guardian's final name?
- Should Node Seven raise archive recovery from 3% to 5%, or stay at 3% until mainland?
- Should the dungeon include one visible terminal-style text sequence after shutdown?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sealed Node location object |
