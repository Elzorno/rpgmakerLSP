---
atlas_id: ATLAS-FND-009
title: Object Template Library
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-006
  - ATLAS-FND-007
  - ATLAS-FND-008
related:
  - ATLAS-FND-005
---

# Object Template Library

The Object Template Library provides reusable page templates for Atlas OS objects.

Use these templates when creating new regions, locations, NPCs, quests, monsters, items, relays, systems, assets, and implementation packets.

---

## Purpose

This document answers:

> What structure should each Atlas object page follow?

---

## Prime Rule

Every new object page should use the closest matching template.

Do not invent page structure unless the object model lacks a suitable template.

---

## Region Template

```markdown
---
object_id: REG-XXX-000
atlas_id: REG-XXX-000
title: Region Name
object_type: Region
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
journey: []
relationships:
  contains: []
  related_to: []
---

# Region Name

## Purpose

## Player-Facing Summary

## Hidden Reality

## Geography

## Culture

## Major Locations

## Travel Routes

## Encounter Philosophy

## Story Role

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Location Template

```markdown
---
object_id: LOC-XXX-000
atlas_id: LOC-XXX-000
title: Location Name
object_type: Location
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
region: REG-XXX-000
journey: []
relationships:
  located_in: []
  contains: []
  related_to: []
---

# Location Name

## Purpose

## Player-Facing Description

## Hidden Reality

## Map Requirements

## NPCs

## Quests

## Shops / Services

## Enemies / Encounters

## Treasure / Secrets

## Visual Direction

## Audio Direction

## Story States

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Character / NPC Template

```markdown
---
object_id: CHR-XXX-000
atlas_id: CHR-XXX-000
title: Character Name
object_type: Character
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
relationships:
  appears_in: []
  related_to: []
  starts_quest: []
---

# Character Name

## Purpose

## Role In Story

## Player-Facing Identity

## Hidden-Layer Role

## Personality

## Knowledge Level

## Dialogue Rules

## Character Arc

## Gameplay Role

## Visual Direction

## Audio / Motif Notes

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Quest Template

```markdown
---
object_id: QST-XXX-000
atlas_id: QST-XXX-000
title: Quest Name
object_type: Quest
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
journey: JRN-000
relationships:
  starts_at: []
  involves: []
  requires: []
  rewards: []
---

# Quest Name

## Purpose

## Story Role

## Starting Conditions

## Objectives

## Key NPCs

## Key Locations

## Required Items / Systems

## Completion Conditions

## Rewards

## Dialogue Beats

## Switches

## Variables

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Playtest Checklist

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Monster Family Template

```markdown
---
object_id: FAM-XXX-000
atlas_id: FAM-XXX-000
title: Monster Family Name
object_type: MonsterFamily
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
relationships:
  contains: []
  appears_in: []
---

# Monster Family Name

## Purpose

## Fantasy Presentation

## Hidden Reality

## Silhouette

## Behavior Pattern

## Variant Rules

## Regional Use

## Art Direction

## Audio Direction

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Monster Template

```markdown
---
object_id: MON-XXX-000
atlas_id: MON-XXX-000
title: Monster Name
object_type: Monster
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
family: FAM-XXX-000
relationships:
  belongs_to_family: []
  appears_in: []
  drops_item: []
---

# Monster Name

## Purpose

## Fantasy Presentation

## Hidden Reality

## Encounter Role

## Behavior

## Abilities

## Weaknesses / Resistances

## Drops / Rewards

## Art Direction

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Item Template

```markdown
---
object_id: ITM-XXX-000
atlas_id: ITM-XXX-000
title: Item Name
object_type: Item
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
relationships:
  found_in: []
  required_by: []
  rewards_from: []
---

# Item Name

## Purpose

## Player-Facing Description

## Hidden Reality

## Gameplay Function

## Acquisition

## Use Conditions

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Relay Template

```markdown
---
object_id: REL-000
atlas_id: REL-000
title: Relay Node Name
object_type: Relay
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
region: REG-XXX-000
location: LOC-XXX-000
relationships:
  located_in: []
  guarded_by: []
  unlocks: []
  related_to: []
---

# Relay Node Name

## Purpose

## Fantasy Presentation

## Hidden Reality

## Story Function

## Archive Recovery Effect

## Guardian / Boss

## Shutdown Sequence

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|

## RPG Maker Implementation Notes

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Implementation Packet Template

```markdown
---
object_id: IMP-XXX-000
atlas_id: IMP-XXX-000
title: Implementation Packet Name
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: false
owner: Technical Director
implementation_status: Not Started
relationships:
  implements: []
  requires: []
---

# Implementation Packet Name

## Objective

## Atlas References

## Scope

## Files / Data Areas

## Required Maps

## Required Switches

## Required Variables

## Required Database Entries

## Required Assets

## Event Logic

## Acceptance Criteria

## Playtest Steps

## Out of Scope

## Open Questions

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Future Expansion

Additional templates may be added for:

- shops,
- books,
- memory fragments,
- cutscenes,
- skills,
- equipment,
- sound effects,
- image prompts,
- playtest reports.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Atlas OS template library |
