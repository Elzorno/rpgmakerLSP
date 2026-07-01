---
object_id: IMP-HOM-004
atlas_id: IMP-HOM-004
title: Build Node Seven Sequence
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - QST-HOM-003
    - LOC-GLS-001
    - LOC-SND-001
    - REL-007
  requires:
    - IMP-HOM-002
    - IMP-HOM-003
---

# Implementation Packet: Build Node Seven Sequence

## Objective

Create the Journey I climax sequence where Kai opens Glassfield Ruins, enters the Sealed Node, defeats the guardian, and brings Relay Node Seven offline.

---

## Atlas References

| ID | Reference |
|---|---|
| LOC-GLS-001 | Glassfield Ruins |
| LOC-SND-001 | Sealed Node |
| REL-007 | Relay Node Seven |
| QST-HOM-003 | Node Seven Offline |
| ITM-SWD-001 | The Sword / Project Excalibur |
| IMP-HOM-002 | Journey I State System |

---

## Scope

Included:

- Glassfield sealed entrance event.
- Sealed Node dungeon maps or placeholder maps.
- Guardian boss placeholder troop.
- Relay core event.
- Node Seven shutdown event.
- Mainland travel unlock.
- Ashford post-node state switch.

Out of scope:

- Final boss art.
- Final enemy balance.
- Final dungeon tileset polish.
- Final cutscene graphics.

---

## Required Maps

```text
DGN_Glassfield_Ruins_Exterior
DGN_SealedNode_Upper
DGN_SealedNode_CorePath
DGN_SealedNode_Guardian
DGN_SealedNode_RelayCore
```

Maps may be combined for first implementation if needed.

---

## Required Switches

```text
J1_Sword_Obtained
J1_Glassfield_SealOpened
J1_SealedNode_Entered
J1_Node07_GuardianDefeated
J1_Node07_Offline
J1_Mainland_TravelUnlocked
NPC_Ashford_PostNode07
```

---

## Required Variables

```text
Archive_Recovery_Percent = 5 after Node Seven shutdown
Current_Relay_Count = 1 after Node Seven shutdown
```

---

## Event Logic

### Glassfield Seal

Before Sword acquisition:

- seal is inactive or mysterious,
- optional message hints that something is missing.

After Sword acquisition:

- interaction opens lower entrance,
- set `J1_Glassfield_SealOpened = ON`.

### Sealed Node Entry

On first entry:

- set `J1_SealedNode_Entered = ON`,
- optionally show short archive distortion text.

### Guardian Encounter

Use placeholder troop for first implementation.

On defeat:

```text
J1_Node07_GuardianDefeated = ON
```

### Relay Core

After guardian defeat, allow interaction with relay core.

Shutdown event:

```text
J1_Node07_Offline = ON
Archive_Recovery_Percent = 5
Current_Relay_Count = 1
J1_Mainland_TravelUnlocked = ON
NPC_Ashford_PostNode07 = ON
```

Suggested text:

```text
NODE SEVEN: OFFLINE
ARCHIVE RECOVERY: 5%
```

---

## Acceptance Criteria

- Glassfield seal requires Sword acquisition.
- Player can enter Sealed Node after seal opens.
- Guardian blocks relay core until defeated.
- Relay shutdown updates all required switches and variables.
- Mainland travel is unlocked after shutdown.
- Ashford NPCs can reference post-node state.

---

## Playtest Steps

1. Confirm Glassfield seal blocks progress without Sword.
2. Set or obtain Sword.
3. Open Glassfield seal.
4. Enter Sealed Node.
5. Defeat guardian placeholder.
6. Activate relay core.
7. Confirm Node Seven switches and variables update.
8. Confirm Rustshore departure can now unlock in a later packet.

---

## Open Questions

- What is the guardian's final monster ID and name?
- Should shutdown say OFFLINE, CLEANSED, or QUIETED in player-facing text?
- Should mainland travel unlock immediately or after returning to Ashford/Elara?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Node Seven implementation packet |
