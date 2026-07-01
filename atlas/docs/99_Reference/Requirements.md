---
atlas_id: ATLAS-REQ-001
title: Requirements
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-PRJ-003
  - ATLAS-TEC-001
related:
  - ATLAS-REF-001
---

# Requirements

The Requirements page captures implementation-neutral requirements derived from Atlas.

Requirements are not design notes. They are statements that future implementation can be checked against.

---

## Purpose

This document answers:

> What must be true for the game and Atlas implementation to satisfy the approved design?

---

## Requirement Format

```text
REQ-0000 — Requirement Name
Statement: The project shall...
Source: Atlas document or decision record
Status: Draft / Approved / Locked
Trace: Future implementation references
```

---

## Foundational Requirements

### REQ-0001 — Atlas Authority

Statement: Implementation shall derive from Atlas. If implementation and Atlas disagree, Atlas is authoritative.

Source: DDR-0001, Project Constitution

Status: Locked

---

### REQ-0002 — No Supernatural Magic

Statement: Every magic-like phenomenon shall have a canonical non-supernatural explanation in Atlas.

Source: DDR-0002, Atlas Concordance

Status: Locked

---

### REQ-0003 — Main Story Without External Guide

Statement: The player shall be able to complete the main story without consulting an external guide.

Source: Player Promise

Status: Locked

---

### REQ-0004 — Exploration Rewards

Statement: Every major town, dungeon, and region shall include at least one optional reward for observation or curiosity.

Source: Player Promise, Creative Bible

Status: Approved

---

### REQ-0005 — Dragon Quest-Inspired, Not Copied

Statement: The game shall preserve the spirit of classic Dragon Quest-style exploration, warmth, and enemy families without copying protected characters, monsters, places, or terms.

Source: Studio Manifesto

Status: Locked

---

### REQ-0006 — Hidden Technology Consistency

Statement: The hidden technology layer shall remain internally consistent across story, gameplay, art, audio, and implementation.

Source: Atlas Concordance, Cybersecurity Layer Bible

Status: Approved

---

### REQ-0007 — RPG Maker Practicality

Statement: Core gameplay and story progression shall be practical to implement in RPG Maker MZ using native systems unless an exception is approved.

Source: Development Standards, RPG Maker MZ Bible

Status: Approved

---

### REQ-0008 — Monster Family Reuse

Statement: The bestiary shall prioritize reusable monster families and meaningful variants over large numbers of unrelated one-off enemies.

Source: Monster Bible

Status: Approved

---

### REQ-0009 — Wonder Before Explanation

Statement: The player shall encounter mysterious phenomena before receiving technical explanations.

Source: Project Constitution, Creative Bible, Story Structure Bible

Status: Locked

---

### REQ-0010 — Hopeful Ending

Statement: The ending shall leave the player with a sense of restoration, peace, and future possibility.

Source: Player Promise, Story Structure Bible

Status: Locked

---

## Future Expansion

Future requirements should trace to:

- regions,
- towns,
- dungeons,
- characters,
- monster families,
- systems,
- RPG Maker maps,
- switches and variables,
- playtest checklists.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial requirements foundation |
