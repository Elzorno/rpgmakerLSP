---
atlas_id: ATLAS-TEC-041
title: Home Island Transfer Registry
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-040
related:
  - IMP-HOM-009
---

# Home Island Transfer Registry

This registry defines the canonical transfer graph for Home Island screens.

Every RPG Maker transfer event should map back to a transfer ID in this file.

---

## Purpose

The Transfer Registry answers:

> How does the player move between Home Island screens?

---

## Transfer ID Format

```text
TRN-HOM-000
```

Transfers are directional. A doorway usually needs two transfer IDs: one out and one back.

---

## Ashford Transfers

| Transfer ID | From | To | Condition | Notes |
|---|---|---|---|---|
| TRN-HOM-001 | SCR-HOM-ASH-002 | SCR-HOM-ASH-001 | Always or after intro | Elara House exit |
| TRN-HOM-002 | SCR-HOM-ASH-001 | SCR-HOM-ASH-002 | Always | Enter Elara House |
| TRN-HOM-003 | SCR-HOM-ASH-001 | SCR-HOM-ASH-003 | Always | Enter Ashford Shop |
| TRN-HOM-004 | SCR-HOM-ASH-003 | SCR-HOM-ASH-001 | Always | Shop exit |
| TRN-HOM-005 | SCR-HOM-ASH-001 | SCR-HOM-SKY-001 | Requires J1_Skyreach_AccessOpen | North path to Skyreach |
| TRN-HOM-006 | SCR-HOM-SKY-001 | SCR-HOM-ASH-001 | Always | Return from Skyreach route |
| TRN-HOM-007 | SCR-HOM-ASH-001 | SCR-HOM-RST-001 | Always | South/east route to Rustshore |
| TRN-HOM-008 | SCR-HOM-RST-001 | SCR-HOM-ASH-001 | Always | Return from Rustshore route |

---

## Sword Awakening Transfers

| Transfer ID | From | To | Condition | Notes |
|---|---|---|---|---|
| TRN-HOM-009 | SCR-HOM-SKY-001 | SCR-HOM-HCV-001 | Requires J1_Skyreach_AccessOpen | Enter Hidden Cave |
| TRN-HOM-010 | SCR-HOM-HCV-001 | SCR-HOM-SKY-001 | Always | Exit cave |
| TRN-HOM-011 | SCR-HOM-HCV-001 | SCR-HOM-HCV-002 | Always | Enter trials |
| TRN-HOM-012 | SCR-HOM-HCV-002 | SCR-HOM-HCV-001 | Always | Return to entrance |
| TRN-HOM-013 | SCR-HOM-HCV-002 | SCR-HOM-HCV-003 | Requires all trial switches | Enter Sword Sanctum |
| TRN-HOM-014 | SCR-HOM-HCV-003 | SCR-HOM-HCV-002 | Always | Return from sanctum |

---

## Glassfield and Sealed Node Transfers

| Transfer ID | From | To | Condition | Notes |
|---|---|---|---|---|
| TRN-HOM-015 | SCR-HOM-ASH-001 | SCR-HOM-GLS-001 | Always or island route | Route to Glassfield |
| TRN-HOM-016 | SCR-HOM-GLS-001 | SCR-HOM-ASH-001 | Always | Return from Glassfield |
| TRN-HOM-017 | SCR-HOM-GLS-001 | SCR-HOM-SND-001 | Requires J1_Glassfield_SealOpened | Enter Sealed Node |
| TRN-HOM-018 | SCR-HOM-SND-001 | SCR-HOM-GLS-001 | Always | Exit Sealed Node |
| TRN-HOM-019 | SCR-HOM-SND-001 | SCR-HOM-SND-002 | Always | Proceed deeper |
| TRN-HOM-020 | SCR-HOM-SND-002 | SCR-HOM-SND-001 | Always | Return to upper node |
| TRN-HOM-021 | SCR-HOM-SND-002 | SCR-HOM-SND-003 | Always | Enter guardian chamber |
| TRN-HOM-022 | SCR-HOM-SND-003 | SCR-HOM-SND-002 | Always | Return to core path |
| TRN-HOM-023 | SCR-HOM-SND-003 | SCR-HOM-SND-004 | Requires J1_Node07_GuardianDefeated | Enter relay core |
| TRN-HOM-024 | SCR-HOM-SND-004 | SCR-HOM-SND-003 | Always | Return from relay core |

---

## Rustshore Departure Transfers

| Transfer ID | From | To | Condition | Notes |
|---|---|---|---|---|
| TRN-HOM-025 | SCR-HOM-RST-001 | SCR-HOM-RST-002 | Requires J1_Mainland_TravelUnlocked and player confirmation | Begin departure |
| TRN-HOM-026 | SCR-HOM-RST-002 | Journey II start | Current_Journey = 2 | Destination TBD: Coalmouth or landing screen |

---

## Validation Rules

- Every transfer event in RPG Maker should map to a transfer ID.
- Every one-way transfer must be intentional.
- Story-gated transfers must name their required switch.
- No transfer should strand the player without a return route unless it is a deliberate cutscene transition.

---

## Open Questions

- Should routes through the island overworld become their own screens?
- Should Fogfen Marsh connect from Ashford or from a shared overworld route?
- Should Coalmouth arrival get a `TRN-J2-001` transfer ID instead of staying as Journey II start placeholder?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island transfer registry |
