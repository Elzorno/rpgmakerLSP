---
atlas_id: ATLAS-TEC-040
title: Home Island Screen Registry
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-FND-010
  - REG-HOM-001
related:
  - IMP-HOM-009
---

# Home Island Screen Registry

This registry lists every canonical Home Island screen object currently defined in Atlas.

Use this page as the production checkpoint for Journey I screen completion.

---

## Purpose

The Screen Registry answers:

> What playable screens currently exist for Home Island, and what is their implementation role?

---

## Screen List

| Screen ID | Screen | Location | RPG Maker Map Name | Implementation Packet | Status |
|---|---|---|---|---|---|
| SCR-HOM-ASH-001 | Ashford Exterior | LOC-ASH-001 | TWN_Ashford_Exterior | IMP-HOM-010 | Draft |
| SCR-HOM-ASH-002 | Elara House Interior | LOC-ASH-001 | INT_Ashford_ElaraHouse | IMP-HOM-010 | Draft |
| SCR-HOM-ASH-003 | Ashford Shop Interior | LOC-ASH-001 | INT_Ashford_Shop | IMP-HOM-010 | Draft |
| SCR-HOM-SKY-001 | Skyreach Hill Path | LOC-SKY-001 | DGN_SkyreachHill_Path | IMP-HOM-011 | Draft |
| SCR-HOM-HCV-001 | Hidden Cave Entrance | LOC-HCV-001 | DGN_HiddenCave_Entrance | IMP-HOM-011 | Draft |
| SCR-HOM-HCV-002 | Hidden Cave Trials | LOC-HCV-001 | DGN_HiddenCave_Trials | IMP-HOM-011 | Draft |
| SCR-HOM-HCV-003 | Sword Sanctum | LOC-HCV-001 | DGN_HiddenCave_Sanctum | IMP-HOM-011 | Draft |
| SCR-HOM-GLS-001 | Glassfield Ruins Exterior | LOC-GLS-001 | DGN_Glassfield_Ruins_Exterior | IMP-HOM-012 | Draft |
| SCR-HOM-SND-001 | Sealed Node Upper | LOC-SND-001 | DGN_SealedNode_Upper | IMP-HOM-012 | Draft |
| SCR-HOM-SND-002 | Sealed Node Core Path | LOC-SND-001 | DGN_SealedNode_CorePath | IMP-HOM-012 | Draft |
| SCR-HOM-SND-003 | Guardian Chamber | LOC-SND-001 | DGN_SealedNode_Guardian | IMP-HOM-012 | Draft |
| SCR-HOM-SND-004 | Relay Node Seven Core | LOC-SND-001 | DGN_SealedNode_RelayCore | IMP-HOM-012 | Draft |
| SCR-HOM-RST-001 | Rustshore Docks | LOC-RST-001 | TWN_Rustshore_Docks | IMP-HOM-013 | Draft |
| SCR-HOM-RST-002 | Mainland Departure | LOC-RST-001 | CUT_Mainland_Departure | IMP-HOM-013 | Draft |
| SCR-HOM-FOG-001 | Fogfen Marsh Field | LOC-FOG-001 | FLD_Fogfen_Marsh_Field | IMP-HOM-015 | Draft |
| SCR-HOM-FOG-002 | Deeper Marsh Pocket | LOC-FOG-001 | FLD_Fogfen_Deeper_Marsh_Pocket | IMP-HOM-015 | Draft |

---

## Current Coverage

Home Island currently has screen-level coverage for:

- Ashford opening area,
- Sword awakening route,
- Glassfield and Sealed Node climax,
- Rustshore departure route.
- optional Fogfen Marsh exploration branch.

---

## Completion Rule

A screen may move from Draft to Locked only when:

1. its transfer links are defined,
2. its required events are defined,
3. its switches and variables are listed,
4. its acceptance criteria are testable,
5. Codex can implement it without inventing new design details.

---

## Next Registry Work

- Add Coalmouth screen registry after Coalmouth screens are created.
- Add automated validation later to check every SCR ID appears in this registry.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island screen registry |
