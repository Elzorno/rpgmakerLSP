---
atlas_id: ATLAS-TEC-045
title: Home Island Vertical Slice Backlog
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - IMP-HOM-009
  - ATLAS-TEC-040
  - ATLAS-TEC-041
  - ATLAS-TEC-042
related:
  - ATLAS-TEC-030
  - ATLAS-AI-010
---

# Home Island Vertical Slice Backlog

This backlog converts the Home Island Atlas specification into ordered implementation work.

It is intended for Codex, Claude, and future agents to work in controlled, testable chunks.

---

## Sprint Goal

Build the Journey I playable vertical slice from New Game start through mainland departure.

The first implementation target is function over polish.

---

## Priority Rules

1. Build state first.
2. Build screen transfers second.
3. Build critical-path story events third.
4. Add NPC dialogue scaffolds fourth.
5. Add enemies and battles fifth.
6. Add placeholder art/audio hooks last.
7. Polish only after the slice is playable end-to-end.

---

## Epic 1 — State Foundation

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-001 | Create Journey I switches | IMP-HOM-002 | All canonical switches exist |
| HOM-BL-002 | Create Journey I variables | IMP-HOM-002 | Current_Journey, Archive_Recovery_Percent, Current_Relay_Count exist |
| HOM-BL-003 | Create state debug notes or map comments | ATLAS-TEC-044 | Implementer can verify state values |

---

## Epic 2 — Ashford Start

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-010 | Build Elara House screen | SCR-HOM-ASH-002 | New Game can start here |
| HOM-BL-011 | Build Ashford Exterior screen | SCR-HOM-ASH-001 | Player can exit house and explore town |
| HOM-BL-012 | Build Ashford Shop screen | SCR-HOM-ASH-003 | Player can enter/exit shop |
| HOM-BL-013 | Add Ashford transfers | ATLAS-TEC-041 | TRN-HOM-001 through TRN-HOM-008 work |
| HOM-BL-014 | Add hidden item event | EVT-HOM-007 | Item can only be collected once |
| HOM-BL-015 | Add tremor trigger | EVT-HOM-009 | Skyreach route unlocks |

---

## Epic 3 — Sword Awakening Route

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-020 | Build Skyreach Hill Path | SCR-HOM-SKY-001 | Route is gated correctly |
| HOM-BL-021 | Build Hidden Cave Entrance | SCR-HOM-HCV-001 | Entering sets J1_HiddenCave_Entered |
| HOM-BL-022 | Build Hidden Cave Trials | SCR-HOM-HCV-002 | Three trial switches can be set |
| HOM-BL-023 | Build Sword Sanctum | SCR-HOM-HCV-003 | Sword can be obtained once |
| HOM-BL-024 | Add Sword archive message | ATLAS-STY-011 | Archive recovery becomes 3 |

---

## Epic 4 — Glassfield and Node Seven

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-030 | Build Glassfield Ruins Exterior | SCR-HOM-GLS-001 | Seal requires Sword |
| HOM-BL-031 | Build Sealed Node Upper | SCR-HOM-SND-001 | Entry sets J1_SealedNode_Entered |
| HOM-BL-032 | Build Sealed Node Core Path | SCR-HOM-SND-002 | Guardian chamber reachable |
| HOM-BL-033 | Build Guardian Chamber | SCR-HOM-SND-003 | Boss battle can start and resolve |
| HOM-BL-034 | Build Relay Node Seven Core | SCR-HOM-SND-004 | Node Seven event updates all final states |
| HOM-BL-035 | Add Node Seven archive message | ATLAS-STY-011 | Archive recovery becomes 5 |

---

## Epic 5 — Rustshore Departure

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-040 | Build Rustshore Docks | SCR-HOM-RST-001 | Boat is gated by mainland unlock |
| HOM-BL-041 | Build Mainland Departure sequence | SCR-HOM-RST-002 | Current_Journey becomes 2 |
| HOM-BL-042 | Add dockmaster dialogue states | SCR-HOM-RST-001 | Dialogue changes before/after unlock |

---

## Epic 6 — Battles and Enemies

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-050 | Create Meadow Gel enemy | MON-GEL-001 | Test battle works |
| HOM-BL-051 | Create Ash Rat enemy | MON-RAT-001 | Test battle works |
| HOM-BL-052 | Create Marsh Gel enemy | MON-GEL-002 | Test battle works |
| HOM-BL-053 | Create Node Seven Guardian boss | BOS-N07-001 | Boss event can resolve |
| HOM-BL-054 | Create basic troops | IMP-HOM-005 | Troops do not crash |

---

## Epic 7 — Dialogue and Audio Hooks

| Task ID | Task | Source | Acceptance |
|---|---|---|---|
| HOM-BL-060 | Add Elara dialogue pages | ATLAS-STY-010 | Pages reflect story state |
| HOM-BL-061 | Add Ashford NPC placeholder dialogue | ATLAS-STY-010 | Six village NPCs speak |
| HOM-BL-062 | Add archive sound hooks | ATLAS-AUD-010 | Placeholder SE plays |
| HOM-BL-063 | Add location BGM placeholders | IMP-HOM-008 | Each major screen has audio |

---

## Done Definition

The Home Island vertical slice is done when a new-game playthrough can complete:

```text
Elara House → Ashford → Skyreach → Hidden Cave → Sword → Glassfield → Sealed Node → Node Seven → Rustshore → Journey II start
```

without manual switch manipulation.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island vertical slice backlog |
