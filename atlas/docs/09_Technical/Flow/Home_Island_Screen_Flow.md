---
atlas_id: ATLAS-TEC-043
title: Home Island Screen Flow
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
  - ATLAS-TEC-030
---

# Home Island Screen Flow

This document defines the playable screen flow for the Home Island vertical slice.

It is the high-level map transfer graph that Codex should use when wiring RPG Maker MZ transfer events.

---

## Purpose

This document answers:

> Can the player move from new game start to mainland departure without missing or ambiguous screen transitions?

---

## Core Flow

```mermaid
flowchart TD
    A[SCR-HOM-ASH-002\nElara House Interior] --> B[SCR-HOM-ASH-001\nAshford Exterior]
    B --> C[SCR-HOM-ASH-003\nAshford Shop Interior]
    C --> B
    B --> D[SCR-HOM-SKY-001\nSkyreach Hill Path]
    D --> E[SCR-HOM-HCV-001\nHidden Cave Entrance]
    E --> F[SCR-HOM-HCV-002\nHidden Cave Trials]
    F --> G[SCR-HOM-HCV-003\nSword Sanctum]
    G --> F
    F --> E
    E --> D
    D --> B
    B --> H[SCR-HOM-GLS-001\nGlassfield Ruins Exterior]
    H --> I[SCR-HOM-SND-001\nSealed Node Upper]
    I --> J[SCR-HOM-SND-002\nSealed Node Core Path]
    J --> K[SCR-HOM-SND-003\nGuardian Chamber]
    K --> L[SCR-HOM-SND-004\nRelay Node Seven Core]
    L --> K
    K --> J
    J --> I
    I --> H
    H --> B
    B --> M[SCR-HOM-RST-001\nRustshore Docks]
    M --> N[SCR-HOM-RST-002\nMainland Departure]
    N --> O[Journey II Start]
```

---

## Story Gates

| Gate | Required State | Opens |
|---|---|---|
| Skyreach access | J1_Skyreach_AccessOpen | SCR-HOM-SKY-001 |
| Sword Sanctum access | J1_Trial_Body_Clear + J1_Trial_Mind_Clear + J1_Trial_Heart_Clear | SCR-HOM-HCV-003 |
| Glassfield lower entrance | J1_Sword_Obtained | SCR-HOM-SND-001 |
| Relay core access | J1_Node07_GuardianDefeated | SCR-HOM-SND-004 |
| Mainland departure | J1_Mainland_TravelUnlocked | SCR-HOM-RST-002 |

---

## Required Critical Path

The minimum critical path is:

```text
SCR-HOM-ASH-002
→ SCR-HOM-ASH-001
→ SCR-HOM-SKY-001
→ SCR-HOM-HCV-001
→ SCR-HOM-HCV-002
→ SCR-HOM-HCV-003
→ SCR-HOM-GLS-001
→ SCR-HOM-SND-001
→ SCR-HOM-SND-002
→ SCR-HOM-SND-003
→ SCR-HOM-SND-004
→ SCR-HOM-RST-001
→ SCR-HOM-RST-002
→ Journey II Start
```

---

## Optional / Non-Critical Screens

| Screen | Status | Notes |
|---|---|---|
| SCR-HOM-ASH-003 | Optional but recommended | Early shop and prep |
| SCR-HOM-FOG-001 / SCR-HOM-FOG-002 | Optional defined branch | Optional exploration content; must not block critical path |
| Elder House / Inn | Not yet defined | Add only if needed for pacing |

---

## Flow Validation Rules

- Every screen must have at least one valid entry path unless it is a cutscene-only destination.
- Every dungeon screen must have a return path unless deliberately one-way.
- Story gates must have a clear switch condition.
- No critical path gate may depend on an optional screen.
- Every terminal critical-path transition must eventually lead to Journey II start.

---

## Open Questions

- Should Glassfield route go through a shared Home Island overworld screen instead of directly from Ashford?
- Should Rustshore departure be reachable before Glassfield as optional exploration?
- Should Journey II start be Coalmouth directly or a mainland landing screen?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island screen flow graph |
