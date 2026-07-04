---
atlas_id: ATLAS-TEC-000
title: Technical Overview
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
dependencies:
  - ATLAS-HOME
related:
  - ATLAS-TEC-001
---

# 09 Technical

The Technical section defines how Atlas-approved content becomes an implementation.

RPG Maker MZ is the first implementation target, but Atlas remains engine independent.

## Technical Documents

| Atlas ID | Document | Purpose |
|---|---|---|
| ATLAS-TEC-001 | Development Standards | Defines production workflow and implementation rules |
| ATLAS-TEC-054 | RPG Maker Event Specification Standard | Defines reusable RPG Maker event page standards |
| ATLAS-TEC-055 | Home Island Executable Event Specs | Defines RPG Maker-ready Home Island vertical slice event pages |
| ATLAS-TEC-056 | Home Island Combat Database Spec | Defines RPG Maker-ready Home Island combat database rows |
| ATLAS-TEC-057 | Home Island Body Mind Heart Trial Mechanics Spec | Defines RPG Maker-ready Home Island trial mechanics |
| ATLAS-TEC-058 | RPG Maker MZ Vertical Slice Build Pipeline | Defines Atlas-to-RPG Maker vertical slice implementation order |
| ATLAS-TEC-059 | Home Island Tileset Assignment Matrix | Defines Home Island placeholder tilesets, passability, regions, and encounter zones |
| ATLAS-TEC-060 | Home Island Animation Assignment Matrix | Defines Home Island placeholder animations, story effects, and combat VFX |
| ATLAS-TEC-061 | Home Island Production Readiness Gate | Issues the production decision for Home Island first-playable implementation |

## Current Rule

If RPG Maker MZ can fake an effect convincingly, use the fake.
