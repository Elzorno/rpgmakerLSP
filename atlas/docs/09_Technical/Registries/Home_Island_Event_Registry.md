---
atlas_id: ATLAS-TEC-042
title: Home Island Event Registry
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-040
  - ATLAS-TEC-041
related:
  - IMP-HOM-009
  - ATLAS-TEC-055
  - ATLAS-TEC-057
---

# Home Island Event Registry

This registry defines the canonical event inventory for the Home Island vertical slice.

Every important RPG Maker MZ event should map back to an event ID in this file.

---

## Purpose

The Event Registry answers:

> What events must exist for Home Island to be playable from Ashford start through mainland departure?

---

## Event ID Format

```text
EVT-HOM-000
```

Event IDs are design identifiers, not RPG Maker event numbers. RPG Maker event numbers may change during implementation.

---

## Ashford Events

| Event ID | Screen | Event | Required State / Result |
|---|---|---|---|
| EVT-HOM-001 | SCR-HOM-ASH-002 | Player Start | New game begins here |
| EVT-HOM-002 | SCR-HOM-ASH-002 | Elara Intro Dialogue | Supports story-state pages |
| EVT-HOM-003 | SCR-HOM-ASH-001 | Child Near Old Panel | Dialogue changes after tremor |
| EVT-HOM-004 | SCR-HOM-ASH-001 | Farmer With Warm Stones | Dialogue changes after Sword |
| EVT-HOM-005 | SCR-HOM-ASH-001 | Skyreach Joker | Reinforces hill taboo |
| EVT-HOM-006 | SCR-HOM-ASH-001 | Dock Messenger | Foreshadows Rustshore |
| EVT-HOM-007 | SCR-HOM-ASH-001 | Hidden Item | Self-switch after collection |
| EVT-HOM-008 | SCR-HOM-ASH-003 | Shopkeeper | Shop or placeholder process |
| EVT-HOM-009 | SCR-HOM-ASH-001 | Tremor Trigger | Sets J1_Tremor_Event and J1_Skyreach_AccessOpen |

---

## Skyreach and Hidden Cave Events

| Event ID | Screen | Event | Required State / Result |
|---|---|---|---|
| EVT-HOM-010 | SCR-HOM-SKY-001 | Skyreach Gate | Blocks until J1_Skyreach_AccessOpen |
| EVT-HOM-011 | SCR-HOM-HCV-001 | Hidden Cave First Entry | Sets J1_HiddenCave_Entered |
| EVT-HOM-012 | SCR-HOM-HCV-002 | Body Trial | Sets J1_Trial_Body_Clear |
| EVT-HOM-013 | SCR-HOM-HCV-002 | Mind Trial | Sets J1_Trial_Mind_Clear |
| EVT-HOM-014 | SCR-HOM-HCV-002 | Heart Trial | Sets J1_Trial_Heart_Clear |
| EVT-HOM-015 | SCR-HOM-HCV-002 | Sanctum Gate | Requires all trial switches |
| EVT-HOM-016 | SCR-HOM-HCV-003 | Sword Pedestal | Sets J1_Sword_Obtained and Archive_Recovery_Percent = 3 |

---

## Glassfield and Sealed Node Events

| Event ID | Screen | Event | Required State / Result |
|---|---|---|---|
| EVT-HOM-017 | SCR-HOM-GLS-001 | Glassfield Seal | Requires Sword, sets J1_Glassfield_SealOpened |
| EVT-HOM-018 | SCR-HOM-GLS-001 | Surface Fragment | Optional memory warning |
| EVT-HOM-019 | SCR-HOM-SND-001 | Sealed Node First Entry | Sets J1_SealedNode_Entered |
| EVT-HOM-020 | SCR-HOM-SND-002 | Core Path Door | Sets J1_CorePath_DoorOpened if used |
| EVT-HOM-021 | SCR-HOM-SND-003 | Node Seven Guardian | Starts boss, sets J1_Node07_GuardianDefeated |
| EVT-HOM-022 | SCR-HOM-SND-004 | Relay Core | Sets Node Seven and mainland unlock states |

---

## Rustshore Events

| Event ID | Screen | Event | Required State / Result |
|---|---|---|---|
| EVT-HOM-023 | SCR-HOM-RST-001 | Dockmaster | Blocks or permits departure by state |
| EVT-HOM-024 | SCR-HOM-RST-001 | Lighthouse Examine | Subtle old-world signal flavor |
| EVT-HOM-025 | SCR-HOM-RST-001 | Boat Transfer | Requires J1_Mainland_TravelUnlocked and confirmation |
| EVT-HOM-026 | SCR-HOM-RST-002 | Departure Sequence | Sets Current_Journey = 2 |

---

## Optional Fogfen Events

| Event ID | Screen | Event | Required State / Result |
|---|---|---|---|
| EVT-HOM-027 | SCR-HOM-FOG-001 | Fogfen Entry / Exit Transfer | Always available optional branch transfer |
| EVT-HOM-028 | SCR-HOM-FOG-001 | Hidden Item Landmark | Self-switch after collection |
| EVT-HOM-029 | SCR-HOM-FOG-001 | Signal-Tick Reed Pool | Optional environmental clue only |
| EVT-HOM-030 | SCR-HOM-FOG-002 | Deeper Marsh Return Transfer | Always returns to SCR-HOM-FOG-001 |
| EVT-HOM-031 | SCR-HOM-FOG-002 | Signal Pool / Cable Cluster Examine | Optional environmental clue only |

---

## Common Event Candidates

| Candidate ID | Name | Purpose |
|---|---|---|
| CE-ARCHIVE-MSG | Archive Message Display | Reusable old-system text display |
| CE-SWORD-AUTH | Sword Authentication | Sword acquisition sequence support |
| CE-RELAY-RESOLVE | Relay Resolution | Shared relay status update pattern |
| CE-SCREEN-FADE | Screen Transition Helper | Reusable fade and transfer support |
| CE_Trial_Complete_Chime | Trial Completion Chime | Optional shared completion feedback from ATLAS-TEC-057 |
| CE_Trial_Reset | Trial Reset Feedback | Optional shared harmless trial reset feedback from ATLAS-TEC-057 |

---

## Validation Rules

- Story-critical events must appear in this registry.
- Optional flavor events should appear here if they touch switches, variables, or memory fragments.
- Implementation reports should mention which event IDs were completed.
- RPG Maker event numbers should not replace Atlas event IDs.

---

## Next Event Work

- Promote major NPC events to full NPC object references if they become recurring characters.
- Add Coalmouth Event Registry after Coalmouth screens are defined.
- Add event-to-switch traceability matrix later.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island event registry |
| 0.2 | Added optional Fogfen event IDs |
| 0.3 | Linked executable event specs |
| 0.4 | Linked executable Body, Mind, and Heart trial mechanics |
