---
atlas_id: ATLAS-STY-021
title: Coalmouth Memory Fragments
status: Draft
version: 0.1
canonical: true
owner: Narrative Director
implementation_status: Not Started
dependencies:
  - QST-COA-001
  - REL-006
related:
  - ATLAS-STY-011
  - ATLAS-TEC-011
---

# Coalmouth Memory Fragments

This document defines first-pass memory fragments for the Coalmouth Mine Crisis.

---

## Purpose

Coalmouth fragments should reveal that old-world systems once protected workers and coordinated machinery.

They should deepen the industrial-control theme without overexplaining it.

---

## Fragment Rules

1. Keep fragments short.
2. Let Vera react in practical terms.
3. Show that the old world included ordinary workers, not only Architects.
4. Avoid using modern acronyms like ICS or SCADA in player-facing text.
5. Use system language only in brief archive readouts.

---

## Recommended Fragments

### Fragment 01 — Shift Safety Note

Trigger: first old control panel in Coalmouth Mine.

```text
SHIFT SAFETY NOTE

No override without two confirmations.
People are not timing errors.
```

Purpose: hints at safety systems and human-centered control.

---

### Fragment 02 — Vera Reaction

Trigger: after Fragment 01.

```text
Vera: Whoever wrote that knew machines need limits.

Vera: And people need someone willing to stop them.
```

Purpose: connects Vera emotionally to safety and responsibility.

---

### Fragment 03 — Broken Loop

Trigger: rail switch chamber.

```text
COMMAND LOOP DETECTED

Instruction repeated beyond safe threshold.
Local judgment required.
```

Purpose: shows automation failing without wisdom.

---

### Fragment 04 — Node Six Stabilization

Trigger: Relay Node Six sequence.

```text
NODE SIX: ISOLATED
ARCHIVE RECOVERY: 10%
TRUST CHAIN: PARTIAL
```

Purpose: establishes that not every node needs identical wording.

---

## Forbidden in Coalmouth

Do not fully reveal:

- NEMESIS identity,
- full relay map,
- the Architect’s guilt,
- Project Excalibur’s final purpose.

---

## Implementation Notes

Use simple text events, sound cue, and short pauses.

Potential common event:

```text
CE_MemoryFragment_Play
```

---

## Open Questions

- Should Coalmouth use ARCHIVE RECOVERY 10% or 12%?
- Should Vera be present for all memory fragments?
- Should Node Six say ISOLATED, STABILIZED, or OFFLINE?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth memory fragments |
