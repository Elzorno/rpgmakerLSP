---
object_id: IMP-HOM-016
atlas_id: IMP-HOM-016
title: Build Home Island Routes
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - REG-HOM-001
    - ATLAS-TEC-043
  requires:
    - IMP-HOM-010
    - IMP-HOM-011
    - IMP-HOM-012
    - IMP-HOM-013
    - IMP-HOM-014
    - ATLAS-TEC-052
    - ATLAS-TEC-055
---

# Implementation Packet: Build Home Island Routes

## Objective

Create the implementation-facing production packet for connecting Home Island's critical-path screens and optional route branches.

This packet is about route flow and transfer safety, not new story content.

---

## Traceability

| Source | Role |
|---|---|
| REG-HOM-001 | Home Island region object |
| ATLAS-TEC-031 | Identifies Home Island route flow as a known packet gap |
| ATLAS-TEC-043 | Defines the required Home Island screen flow graph |
| IMP-HOM-010 | Ashford screen packet |
| IMP-HOM-011 | Skyreach and Hidden Cave screen packet |
| IMP-HOM-012 | Glassfield and Sealed Node screen packet |
| IMP-HOM-013 | Rustshore departure screen packet |
| IMP-HOM-014 | Rustshore Docks screen packet |
| ATLAS-TEC-052 | Defines layer discipline for meaning, gameplay, hidden truth, and implementation |
| ATLAS-TEC-055 | Defines executable transfer event pages |

---

## Critical Path

The required route flow follows `ATLAS-TEC-043`:

```text
SCR-HOM-ASH-002
-> SCR-HOM-ASH-001
-> SCR-HOM-SKY-001
-> SCR-HOM-HCV-001
-> SCR-HOM-HCV-002
-> SCR-HOM-HCV-003
-> SCR-HOM-GLS-001
-> SCR-HOM-SND-001
-> SCR-HOM-SND-002
-> SCR-HOM-SND-003
-> SCR-HOM-SND-004
-> SCR-HOM-RST-001
-> SCR-HOM-RST-002
-> Journey II Start
```

---

## Build Order

1. Confirm all implemented Home Island maps use the intended screen IDs and map names.
2. Wire Ashford to Skyreach using `J1_Skyreach_AccessOpen`.
3. Wire Skyreach and Hidden Cave return paths.
4. Wire Ashford or island route to Glassfield / Sealed Node using existing Sword and Node Seven gates.
5. Wire return paths from dungeon screens unless deliberately one-way.
6. Wire Rustshore access and mainland departure gate using `J1_Mainland_TravelUnlocked`.
7. Add debug notes or placeholders for any route target not yet implemented.

---

## Required Gates

| Gate | Required State | Opens |
|---|---|---|
| Skyreach access | `J1_Skyreach_AccessOpen` | SCR-HOM-SKY-001 |
| Sword Sanctum access | `J1_Trial_Body_Clear` + `J1_Trial_Mind_Clear` + `J1_Trial_Heart_Clear` | SCR-HOM-HCV-003 |
| Glassfield / Sealed Node access | `J1_Sword_Obtained` | SCR-HOM-SND-001 |
| Relay core access | `J1_Node07_GuardianDefeated` | SCR-HOM-SND-004 |
| Mainland departure | `J1_Mainland_TravelUnlocked` | SCR-HOM-RST-002 |

---

## Required Transfer Rules

- Every screen must have a valid entry path unless it is a cutscene-only destination.
- Every dungeon screen must have a return path unless deliberately one-way.
- No critical-path gate may depend on optional Fogfen content.
- Optional routes must return cleanly to the main Home Island route.
- Terminal critical-path transitions must eventually lead to Journey II start.

---

## Truth Layer Alignment

The story layer is Journey I's movement from home to Sword authentication, Node Seven shutdown, and departure.

The gameplay layer is readable exploration, gates, dungeons, and transfers.

The hidden layer is restoration of trust, relay state, and access authorization.

The implementation layer is switches, variables, transfers, event pages, map names, and placeholder destinations.

---

## Acceptance Criteria

- Player can move from new game start through the critical path without missing transfer targets.
- Story gates block and open the intended routes.
- Return transfers prevent dead ends.
- Optional screens do not block required progress.
- Rustshore departure remains gated until `J1_Mainland_TravelUnlocked`.
- Any missing Journey II destination is clearly marked as placeholder.
- No custom plugins are required.

---

## Playtest Steps

1. Start at `SCR-HOM-ASH-002`.
2. Transfer to `SCR-HOM-ASH-001`.
3. Confirm Skyreach is blocked before `J1_Skyreach_AccessOpen`.
4. Open Skyreach access and follow the Hidden Cave route.
5. Complete the Sword route and return to the main island path.
6. Follow the Glassfield / Sealed Node route through Node Seven.
7. Confirm mainland travel unlocks.
8. Travel to Rustshore and trigger departure.
9. Confirm any Journey II placeholder is clearly labeled.

---

## Open Questions

- Should Home Island use one shared overworld route map or direct screen-to-screen transfers for the vertical slice?
- Should optional Fogfen route access be added before or after critical path stability?
- Should Journey II start use Coalmouth directly or an intermediate mainland landing screen?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island route implementation packet |
