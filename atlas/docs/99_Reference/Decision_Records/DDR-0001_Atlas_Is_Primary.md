---
atlas_id: ATLAS-DDR-0001
title: DDR-0001 — Atlas Is Primary
status: Locked
version: 1.0
canonical: true
owner: Production Director
implementation_status: Not Applicable
dependencies: []
related:
  - ATLAS-HOME
  - ATLAS-FND-001
---

# DDR-0001 — Atlas Is Primary

## Status

Locked

---

## Context

The project began as an RPG Maker MZ prototype and capability test.

As the world, story, hidden cybersecurity layer, and production methodology developed, the design became larger than a single RPG Maker implementation.

---

## Decision

Atlas is now the primary deliverable and creative authority for _The Last Sword Protocol_.

RPG Maker MZ is the first implementation target, not the definition of the project.

---

## Rationale

Atlas preserves the universe, design logic, production rules, and creative vision independently of engine choice.

If the project later moves to another engine, Atlas remains valid.

---

## Consequences

- Implementation must derive from Atlas.
- Major design changes must be reflected in Atlas first.
- AI agents should consult Atlas before modifying the game.
- The repository should increasingly organize around Atlas as a first-class product.

---

## Related Pages

- [Project Atlas Home](../../index.md)
- [Atlas Operating System](../../00_Foundation/Atlas_Operating_System.md)
