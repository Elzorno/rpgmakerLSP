---
object_id: QST-HOM-003
atlas_id: QST-HOM-003
title: Node Seven Offline
object_type: Quest
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
journey: JRN-001
relationships:
  starts_at:
    - LOC-GLS-001
  involves:
    - CHR-KAI-001
  requires:
    - ITM-SWD-001
    - QST-HOM-002
  rewards: []
---

# Node Seven Offline

This quest is the Journey I climax. Kai enters the Sealed Node beneath Glassfield Ruins and shuts down Relay Node Seven.

---

## Purpose

This quest completes Home Island and reveals that the island's legends describe real infrastructure failures.

---

## Story Role

With the Sword awakened, Kai can access the lower ruins beneath Glassfield. There he confronts the Node Seven guardian and brings the first relay offline.

---

## Objectives

1. Reach Glassfield Ruins after obtaining the Sword.
2. Open the sealed lower entrance.
3. Explore the Sealed Node.
4. Defeat the guardian.
5. Interact with Relay Node Seven.
6. Shut down or cleanse the node.
7. Unlock mainland travel through Rustshore Docks.

---

## Completion Conditions

Quest completes when `J1_Node07_Offline` and `J1_Mainland_TravelUnlocked` are true.

---

## Rewards

- Mainland travel unlock.
- Archive recovery update.
- Ashford post-crisis NPC dialogue state.

---

## Switches

```text
J1_Glassfield_SealOpened
J1_SealedNode_Entered
J1_Node07_GuardianDefeated
J1_Node07_Offline
J1_Mainland_TravelUnlocked
NPC_Ashford_PostNode07
```

---

## Variables

Recommended:

```text
Archive_Recovery_Percent = 5
Current_Relay_Count = 1
```

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| requires | ITM-SWD-001 | Sword opens path |
| starts_at | LOC-GLS-001 | Glassfield entrance |
| advances_quest | LOC-SND-001 | Sealed Node dungeon |
| completes_quest | REL-007 | Relay Node Seven resolved |
| unlocks | LOC-RST-001 | Rustshore departure becomes available |

---

## RPG Maker Implementation Notes

Keep the first dungeon short and clear. It should teach relay-core interaction without overwhelming the player.

Use a post-boss event for relay shutdown.

---

## Playtest Checklist

- Player can find Glassfield after Sword acquisition.
- Seal opening is readable.
- Dungeon length is appropriate.
- Boss defeat triggers relay shutdown.
- Rustshore Docks unlocks afterward.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Node Seven Offline quest object |
