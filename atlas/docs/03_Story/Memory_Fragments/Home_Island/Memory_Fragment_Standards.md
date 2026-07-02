---
atlas_id: ATLAS-STY-011
title: Home Island Memory Fragment Standards
status: Draft
version: 0.1
canonical: true
owner: Narrative Director
implementation_status: Not Started
dependencies:
  - ATLAS-STY-001
  - ATLAS-TEC-010
related:
  - QST-HOM-002
  - QST-HOM-003
---

# Home Island Memory Fragment Standards

This document defines the first memory fragment rules for Journey I.

Memory fragments should deepen mystery without explaining too much too early.

---

## Purpose

Journey I memory fragments should confirm that the Sword is connected to old-world systems while preserving wonder.

They should not fully explain NEMESIS, the Architect, or the Collapse.

---

## Fragment Rules

1. Keep fragments short.
2. Use partial context.
3. Avoid full exposition.
4. Include ordinary human detail when possible.
5. Let the player feel something before understanding it.
6. Use technical-looking text sparingly.

---

## Recommended Journey I Fragments

### Fragment 01 — Authentication

Trigger: Sword awakening.

```text
AUTHORIZATION ACCEPTED
ARCHIVE RECOVERY: 3%
```

Purpose: first clear sign that the Sword is not only magical.

---

### Fragment 02 — Warning Echo

Trigger: optional after Sword awakening or first shrine interaction.

```text
If this message is recovered, the island seal has failed.

Do not reconnect the relay without verified authority.
```

Purpose: foreshadow that the island was sealed intentionally.

---

### Fragment 03 — Human Detail

Trigger: optional Glassfield terminal/surface ruin.

```text
Maintenance note:

South vent still warms the village side.
Leave it running. The children play there in winter.
```

Purpose: show that the old world was lived in by ordinary people.

---

### Fragment 04 — Node Seven Shutdown

Trigger: Relay Node Seven shutdown.

```text
NODE SEVEN: OFFLINE
ARCHIVE RECOVERY: 5%
TRUST CHAIN: PARTIAL
```

Purpose: establish relay progression and trust-chain language.

---

## Forbidden in Journey I

Do not reveal:

- NEMESIS as AI,
- the full identity of the Architect,
- the full Collapse cause,
- the exact meaning of Project Excalibur,
- the full relay network map.

---

## Implementation Notes

Memory fragments can be implemented with:

- Show Text,
- darkened screen,
- sound effect,
- short pause,
- optional picture overlay later.

Use common event candidate:

```text
CE_MemoryFragment_Play
```

---

## Open Questions

- Should Fragment 02 be mandatory or optional?
- Should Fragment 03 be hidden in Glassfield for curious players?
- Should the term “trust chain” appear as early as Journey I?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Journey I memory fragment standards |
