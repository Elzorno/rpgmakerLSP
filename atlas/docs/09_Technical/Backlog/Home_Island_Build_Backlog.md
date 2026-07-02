---
atlas_id: ATLAS-TEC-032
title: Home Island Build Backlog
status: Draft
version: 0.1
canonical: true
owner: Production Director
implementation_status: Not Started
dependencies:
  - IMP-HOM-009
  - ATLAS-TEC-031
related:
  - ATLAS-AI-010
---

# Home Island Build Backlog

This backlog organizes the Home Island vertical slice into small tasks for Codex, Claude, image generation, and playtesting.

---

## Purpose

This document answers:

> What should be built next, and in what order?

---

## Backlog Rule

Every task should reference an Atlas object or implementation packet.

If a task cannot point to Atlas, update Atlas first.

---

## Sprint 1 — State and Shell

| Task ID | Task | Owner | Source | Done When |
|---|---|---|---|---|
| HOM-BLD-001 | Create Journey I switches and variables | Codex | IMP-HOM-002 | State names exist and are reusable |
| HOM-BLD-002 | Create Ashford exterior placeholder map | Codex | IMP-HOM-001 | Player can walk around town |
| HOM-BLD-003 | Create Elara house interior | Codex | IMP-HOM-001 | Player can enter and exit house |
| HOM-BLD-004 | Add six Ashford placeholder NPCs | Codex | ATLAS-CHR-010 | NPCs are placed and interactable |
| HOM-BLD-005 | Add hidden item behind warm-stone vent | Codex | IMP-HOM-001 | Item can be collected once |

---

## Sprint 2 — Opening Flow

| Task ID | Task | Owner | Source | Done When |
|---|---|---|---|---|
| HOM-BLD-006 | Add Elara intro dialogue scaffold | Codex / Claude | ATLAS-STY-010 | Elara has intro dialogue |
| HOM-BLD-007 | Add village NPC dialogue states | Codex / Claude | IMP-HOM-006 | NPCs respond to story switches |
| HOM-BLD-008 | Add tremor event | Codex | QST-HOM-001 | Tremor turns on required switches |
| HOM-BLD-009 | Add Skyreach access gate | Codex | IMP-HOM-003 | Path opens after tremor |

---

## Sprint 3 — Sword Sequence

| Task ID | Task | Owner | Source | Done When |
|---|---|---|---|---|
| HOM-BLD-010 | Create Skyreach Hill placeholder map | Codex | LOC-SKY-001 | Player reaches cave entrance |
| HOM-BLD-011 | Create Hidden Cave trial map(s) | Codex | LOC-HCV-001 | Trial flow is playable |
| HOM-BLD-012 | Add Sword pedestal event | Codex | IMP-HOM-003 | Sword acquisition works |
| HOM-BLD-013 | Add archive recovery text | Codex | ATLAS-STY-011 | Archive becomes 3% |

---

## Sprint 4 — Node Seven Sequence

| Task ID | Task | Owner | Source | Done When |
|---|---|---|---|---|
| HOM-BLD-014 | Create Glassfield Ruins placeholder map | Codex | LOC-GLS-001 | Seal event exists |
| HOM-BLD-015 | Create Sealed Node placeholder dungeon | Codex | LOC-SND-001 | Player can reach guardian |
| HOM-BLD-016 | Add Node Seven Guardian placeholder battle | Codex | BOS-N07-001 | Boss can be defeated |
| HOM-BLD-017 | Add relay shutdown event | Codex | REL-007 | Archive becomes 5% and mainland unlocks |

---

## Sprint 5 — Production Polish Pass

| Task ID | Task | Owner | Source | Done When |
|---|---|---|---|---|
| HOM-BLD-018 | Add placeholder audio hooks | Codex | IMP-HOM-008 | Major maps/events have audio placeholders |
| HOM-BLD-019 | Generate first battler references | Art Director | ATLAS-ART-010 | Four battler concepts exist |
| HOM-BLD-020 | Generate location art references | Art Director | ATLAS-ART-011 | Home Island locations have references |
| HOM-BLD-021 | Run vertical slice checklist | Tester | ATLAS-TEC-030 | Slice can be completed or issues are logged |

---

## Parking Lot

These are useful but not required for the first vertical slice:

- Optional Fogfen Marsh side quest.
- Rustshore dockmaster named NPC.
- Elara portrait.
- Ashford town theme final music.
- Final battler art cleanup.
- Mainland arrival cutscene.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island build backlog |
