---
atlas_id: ATLAS-AI-010
title: Home Island Vertical Slice Codex Handoff
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
dependencies:
  - IMP-HOM-009
  - ATLAS-TEC-030
related:
  - ATLAS-AI-001
---

# Home Island Vertical Slice Codex Handoff

This document gives Codex a compact starting brief for implementing the first playable vertical slice.

---

## Mission

Build the Journey I Home Island vertical slice from Ashford start through Node Seven shutdown.

Use Atlas as source of truth.

---

## Read First

Codex should read these documents before implementation:

1. `ATLAS-PRJ-001` — Project Constitution
2. `ATLAS-CRT-001` — Creative Bible
3. `ATLAS-TEC-020` — RPG Maker MZ Bible
4. `IMP-HOM-009` — Home Island Sprint Assembly
5. `ATLAS-TEC-030` — Home Island Vertical Slice Playtest Checklist

---

## Build Order

Follow this order:

```text
IMP-HOM-002
IMP-HOM-001
IMP-HOM-006
IMP-HOM-005
IMP-HOM-003
IMP-HOM-004
IMP-HOM-008
IMP-HOM-007
```

---

## Non-Negotiables

Do not rename canonical switches, variables, object IDs, or map naming patterns without updating Atlas.

Use placeholders for art, audio, and dialogue when needed.

Do not block implementation waiting for final generated assets.

---

## Required End State

A new game can be played from Ashford through Node Seven shutdown without manual switch editing.

At the end:

```text
J1_Sword_Obtained = ON
J1_Node07_Offline = ON
J1_Mainland_TravelUnlocked = ON
Archive_Recovery_Percent = 5
Current_Relay_Count = 1
```

---

## Report Back Format

When implementation is complete, Codex should report:

```markdown
# Home Island Vertical Slice Implementation Report

## Completed

## Files Changed

## Maps Created

## Switches Created

## Variables Created

## Database Entries Created

## Placeholder Assets Used

## Playtest Result

## Issues / Open Questions
```

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Codex handoff for Home Island vertical slice |
