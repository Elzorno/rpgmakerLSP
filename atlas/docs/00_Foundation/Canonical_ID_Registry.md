---
atlas_id: ATLAS-FND-008
title: Canonical ID Registry
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-003
  - ATLAS-FND-006
related:
  - ATLAS-FND-007
  - ATLAS-FND-009
---

# Canonical ID Registry

The Canonical ID Registry defines stable object identifiers for Atlas OS.

Atlas IDs identify documents. Object IDs identify game-world objects.

Both are permanent once assigned.

---

## Purpose

This document answers:

> What ID patterns should Atlas objects use, and which initial object IDs are reserved?

---

## Prime Rule

IDs are stable. Names can change.

If `LOC-ASH-001` is renamed from Ashford to Ashford Village later, the ID remains `LOC-ASH-001`.

---

## Object ID Format

```text
CLASS-SHORTCODE-NUMBER
```

Examples:

```text
REG-HOM-001
LOC-ASH-001
NPC-ELA-001
QST-HOM-001
MON-GEL-001
REL-007
```

---

## Class Prefixes

| Prefix | Object Class |
|---|---|
| REG | Region |
| LOC | Location |
| CHR | Major character / party / central story figure |
| NPC | Supporting named NPC |
| QST | Quest |
| FAM | Monster family |
| MON | Monster / enemy variant |
| BOS | Boss |
| ITM | Item |
| EQP | Equipment |
| SKL | Skill |
| SYS | System |
| REL | Relay node |
| JRN | Journey |
| AST | Asset requirement |
| IMP | Implementation packet |

---

## Shortcode Rules

Shortcodes should be:

- 3 to 5 letters when practical,
- memorable,
- stable,
- based on original object name or region,
- unique within the class when possible.

Examples:

| Object | Shortcode |
|---|---|
| Home Island | HOM |
| Ashford | ASH |
| Skyreach Hill | SKY |
| Glassfield Ruins | GLS |
| Coalmouth | COA |
| Athenaeum | ATH |
| Irongate | IRN |
| Driftlands | DRF |
| New Meridian | NMD |
| Dead Circuit | DCT |

---

## Reserved Initial Region IDs

| ID | Name | Status |
|---|---|---|
| REG-HOM-001 | Home Island | Reserved |
| REG-COA-001 | Coalmouth Region | Reserved |
| REG-ATH-001 | Athenaeum Region | Reserved |
| REG-IRN-001 | Irongate Region | Reserved |
| REG-DRF-001 | Driftlands | Reserved |
| REG-NMD-001 | New Meridian Region | Reserved |
| REG-DCT-001 | Dead Circuit | Reserved |
| REG-VLT-001 | Vault Region | Reserved |
| REG-LOK-001 | Lost Kingdom | Reserved |

---

## Reserved Initial Location IDs

| ID | Name | Status |
|---|---|---|
| LOC-ASH-001 | Ashford | Reserved |
| LOC-RST-001 | Rustshore Docks | Reserved |
| LOC-FOG-001 | Fogfen Marsh | Reserved |
| LOC-GLS-001 | Glassfield Ruins | Reserved |
| LOC-SKY-001 | Skyreach Hill | Reserved |
| LOC-HCV-001 | Hidden Cave / Excalibur Vaultlet | Reserved |
| LOC-SND-001 | Sealed Node | Reserved |
| LOC-COA-001 | Coalmouth | Reserved |
| LOC-CMN-001 | Coalmouth Mine | Reserved |
| LOC-ATH-001 | The Athenaeum | Reserved |
| LOC-SGT-001 | Signal Tower | Reserved |
| LOC-IRN-001 | Irongate | Reserved |
| LOC-IBK-001 | Irongate Bunker | Reserved |
| LOC-DRF-001 | The Drift | Reserved |
| LOC-BRS-001 | Buried Relay Station | Reserved |
| LOC-NMD-001 | New Meridian | Reserved |
| LOC-MCR-001 | Meridian Core | Reserved |
| LOC-DCT-001 | Dead Circuit Wastes | Reserved |
| LOC-BSP-001 | Broken Spire | Reserved |
| LOC-VLT-001 | The Vault Exterior | Reserved |
| LOC-NCR-001 | NEMESIS Core | Reserved |

---

## Reserved Initial Character IDs

| ID | Name | Status |
|---|---|---|
| CHR-KAI-001 | Kai | Reserved |
| CHR-VER-001 | Vera | Reserved |
| CHR-ELD-001 | Eldon | Reserved |
| CHR-CIP-001 | Cipher | Reserved |
| CHR-HER-001 | The Herald | Reserved |
| CHR-ARC-001 | The Architect | Reserved |
| CHR-NEM-001 | NEMESIS | Reserved |
| NPC-ELA-001 | Grandmother Elara | Reserved |

---

## Reserved Initial Relay IDs

Relay IDs use world node numbers directly.

| ID | Name | Region | Status |
|---|---|---|---|
| REL-007 | Node Seven | Home Island | Reserved |
| REL-006 | Node Six | Coalmouth | Reserved |
| REL-005 | Node Five | Athenaeum | Reserved |
| REL-004 | Node Four | Irongate | Reserved |
| REL-003 | Node Three | Driftlands | Reserved |
| REL-002 | Node Two | New Meridian | Reserved |
| REL-001 | Node One | Dead Circuit | Reserved |

---

## Reserved Initial Journey IDs

| ID | Name | Status |
|---|---|---|
| JRN-001 | Journey I — The Dreamer | Reserved |
| JRN-002 | Journey II — The Forgotten World | Reserved |
| JRN-003 | Journey III — The Architects | Reserved |
| JRN-004 | Journey IV — The Broken Trust | Reserved |
| JRN-005 | Journey V — The Last Protocol | Reserved |

---

## Reserved Initial Monster Family IDs

| ID | Name | Status |
|---|---|---|
| FAM-GEL-001 | Gel Family | Reserved |
| FAM-RAT-001 | Rat Family | Reserved |
| FAM-CRO-001 | Crow Family | Reserved |
| FAM-WLF-001 | Wolf Family | Reserved |
| FAM-SCP-001 | Scorpion Family | Reserved |
| FAM-HSK-001 | Husk / Skeleton Family | Reserved |
| FAM-GLM-001 | Golem Family | Reserved |
| FAM-DRN-001 | Drone Family | Reserved |
| FAM-AUT-001 | Automaton Family | Reserved |
| FAM-ABR-001 | Aberration Family | Reserved |

---

## Reserved Initial Quest IDs

| ID | Name | Status |
|---|---|---|
| QST-HOM-001 | Home Island Opening | Reserved |
| QST-HOM-002 | The Sword Awakens | Reserved |
| QST-HOM-003 | Node Seven Offline | Reserved |
| QST-COA-001 | Coalmouth Mine Crisis | Reserved |
| QST-ATH-001 | The Corrupted Archive | Reserved |
| QST-IRN-001 | Orders From Above | Reserved |
| QST-DRF-001 | Relic Sickness | Reserved |
| QST-NMD-001 | The Civic Mandate | Reserved |
| QST-DCT-001 | Into the Dead Circuit | Reserved |
| QST-VLT-001 | The Last Protocol | Reserved |

---

## ID Assignment Process

1. Check this registry before creating a new object.
2. Reuse a reserved ID if the object matches.
3. Assign the next sequential number if no reserved ID exists.
4. Add the new ID to this registry.
5. Use the ID consistently in metadata and relationship tables.

---

## Future Expansion

This registry should eventually be split or generated automatically from object metadata.

Until tooling exists, this page is the manual source of truth for object IDs.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial canonical object ID registry |
