---
object_id: IMP-HOM-006
atlas_id: IMP-HOM-006
title: Build Ashford NPC Dialogue
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - ATLAS-STY-010
    - ATLAS-CHR-010
    - NPC-ELA-001
  requires:
    - IMP-HOM-001
    - IMP-HOM-002
---

# Implementation Packet: Build Ashford NPC Dialogue

## Objective

Implement first-pass Ashford NPC dialogue scaffolding in RPG Maker MZ using the Ashford Dialogue Packet and NPC Roster.

---

## Atlas References

| ID | Reference |
|---|---|
| ATLAS-STY-010 | Ashford Dialogue Packet |
| ATLAS-CHR-010 | Ashford NPC Roster |
| NPC-ELA-001 | Grandmother Elara |
| LOC-ASH-001 | Ashford |
| IMP-HOM-001 | Build Ashford |
| IMP-HOM-002 | Journey I State System |

---

## Scope

Included:

- Elara event pages for major story states.
- Placeholder dialogue for six village NPCs.
- Story-state condition structure.
- Comments in event pages identifying Atlas references.

Out of scope:

- Final polished dialogue.
- Portraits/faces.
- Branching choice-heavy conversations.
- Non-Ashford NPCs.

---

## Required NPC Events

| Event | Required States |
|---|---|
| Elara | Intro, After Tremor, After Sword, After Node Seven, Before Mainland |
| Village Elder | Intro, After Tremor, After Node Seven |
| Shopkeeper | Intro, After Node Seven |
| Child Near Old Panel | Intro, After Tremor |
| Farmer With Warm Stones | Intro, After Sword |
| Skyreach Joker | Intro, After Sword |
| Dock Messenger | Intro, After Node Seven |

---

## Required Switches

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Sword_Obtained
J1_Node07_Offline
J1_Mainland_TravelUnlocked
NPC_Ashford_PostNode07
```

---

## Dialogue Implementation Rule

Use short message boxes.

Avoid modern technical jargon in Ashford NPC dialogue.

Use the exact sample lines from `ATLAS-STY-010` as placeholders if final text is not available.

---

## Acceptance Criteria

- Elara has story-state event pages.
- Six placeholder NPCs have readable dialogue.
- NPCs change at least once after key story switches.
- Dialogue does not reveal the hidden technology layer too early.
- NPC events include comments referencing source Atlas packet.

---

## Playtest Steps

1. Start in Ashford.
2. Talk to every NPC.
3. Toggle `J1_Tremor_Event` and retest key NPCs.
4. Toggle `J1_Sword_Obtained` and retest Elara, Farmer, Skyreach Joker.
5. Toggle `J1_Node07_Offline` and retest village state.
6. Confirm no dialogue event blocks player movement.

---

## Open Questions

- Should Elara have a choice prompt before Kai leaves for Skyreach?
- Should the elder be named before implementation?
- Should Ashford NPC dialogue live directly in events or in an external text reference later?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford NPC dialogue implementation packet |
