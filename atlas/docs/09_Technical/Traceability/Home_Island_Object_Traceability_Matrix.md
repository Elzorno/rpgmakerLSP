---
atlas_id: ATLAS-TEC-031
title: Home Island Object Traceability Matrix
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
dependencies:
  - REG-HOM-001
  - JRN-001
  - IMP-HOM-009
related:
  - ATLAS-TEC-030
  - ATLAS-AI-010
---

# Home Island Object Traceability Matrix

This matrix connects Home Island design objects to the implementation packets that should build them.

---

## Purpose

This document helps Codex and future contributors see which Atlas objects are ready to build and which ones still need more planning.

---

## Core Objects

| Object ID | Object | Build Packet | Status |
|---|---|---|---|
| REG-HOM-001 | Home Island | IMP-HOM-009 | Ready |
| JRN-001 | Journey I — The Dreamer | IMP-HOM-009 | Ready |
| LOC-ASH-001 | Ashford | IMP-HOM-001, IMP-HOM-006 | Ready |
| LOC-RST-001 | Rustshore Docks | IMP-HOM-014 | Ready |
| LOC-FOG-001 | Fogfen Marsh | IMP-HOM-015 | Ready |
| LOC-GLS-001 | Glassfield Ruins | IMP-HOM-004 | Ready |
| LOC-SKY-001 | Skyreach Hill | IMP-HOM-003 | Ready |
| LOC-HCV-001 | Hidden Cave | IMP-HOM-003 | Ready |
| LOC-SND-001 | Sealed Node | IMP-HOM-004 | Ready |
| REL-007 | Relay Node Seven | IMP-HOM-004 | Ready |

---

## Story Objects

| Object ID | Object | Build Packet | Status |
|---|---|---|---|
| QST-HOM-001 | Home Island Opening | IMP-HOM-001, IMP-HOM-006 | Ready |
| QST-HOM-002 | The Sword Awakens | IMP-HOM-003 | Ready |
| QST-HOM-003 | Node Seven Offline | IMP-HOM-004 | Ready |

---

## Character Objects

| Object ID | Object | Build Packet | Status |
|---|---|---|---|
| CHR-KAI-001 | Kai | IMP-HOM-001, IMP-HOM-002 | Ready |
| NPC-ELA-001 | Grandmother Elara | IMP-HOM-001, IMP-HOM-006 | Ready |
| ATLAS-CHR-010 | Ashford NPC Roster | IMP-HOM-006 | Ready |

---

## Enemy Objects

| Object ID | Object | Build Packet | Status |
|---|---|---|---|
| FAM-GEL-001 | Gel Family | IMP-HOM-005 | Ready |
| FAM-RAT-001 | Rat Family | IMP-HOM-005 | Ready |
| MON-GEL-001 | Meadow Gel | IMP-HOM-005 | Ready |
| MON-GEL-002 | Marsh Gel | IMP-HOM-005 | Ready |
| MON-RAT-001 | Ash Rat | IMP-HOM-005 | Ready |
| BOS-N07-001 | Node Seven Guardian | IMP-HOM-004, IMP-HOM-005 | Ready |

---

## Production Objects

| Atlas ID | Area | Build Packet | Status |
|---|---|---|---|
| ATLAS-ART-010 | Battler prompts | IMP-HOM-005 | Ready |
| ATLAS-ART-011 | Location art prompts | IMP-HOM-007 | Ready |
| ATLAS-AUD-010 | Audio cue packet | IMP-HOM-008 | Ready |
| SCR-HOM-FOG-001 | Fogfen Marsh Field | IMP-HOM-015 | Ready |
| SCR-HOM-FOG-002 | Deeper Marsh Pocket | IMP-HOM-015 | Ready |
| ATLAS-TEC-030 | Vertical slice checklist | IMP-HOM-009 | Ready |
| ATLAS-AI-010 | Codex handoff | IMP-HOM-009 | Ready |

---

## Known Gaps

| Gap | Recommended Next Packet |
|---|---|
| Exploration rewards need clearer standards | Future exploration rewards packet |

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island traceability matrix |
