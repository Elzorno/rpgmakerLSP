---
atlas_id: ATLAS-TEC-001
title: Development Standards
status: Approved
version: 0.5
canonical: true
owner: Technical Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-PRJ-002
  - ATLAS-FND-001
related:
  - ATLAS-CRT-001
---

# Development Standards

This document defines how _The Last Sword Protocol_ should be developed once implementation resumes.

Implementation is currently paused. Existing RPG Maker MZ work is considered a prototype and capability test.

---

## Atlas Comes First

Every major feature begins as documentation before implementation.

Preferred flow:

```text
Design in Atlas
→ Review
→ Approve
→ Implement in RPG Maker MZ
→ Test
→ Update Atlas if needed
```

Do not allow implementation to become the place where the project invents its identity.

---

## Document Lifecycle

All major documents use this lifecycle:

```text
Draft → Review → Approved → Locked
```

- **Draft**: Active creative development.
- **Review**: Ready for critique.
- **Approved**: Accepted as directionally correct.
- **Locked**: Canonical for implementation.

Locked documents should not be casually rewritten. If they need changes, create a revision note and update dependent documents.

---

## AI Agent Roles

### Creative Director

Protects the vision, maintains Atlas coherence, resolves creative conflicts, and checks whether ideas belong.

### Technical Director

Implements approved Atlas content in code, data, RPG Maker maps, database files, events, plugins, and tooling.

### Narrative Director

Expands dialogue, NPC writing, books, memory fragments, quest text, and lore consistency.

### Art Director

Produces visual assets following Atlas-approved art direction and prompt standards.

### Production Director

Approves direction and owns final project decisions.

---

## RPG Maker MZ Reality Rule

Designs must remain practical for RPG Maker MZ while RPG Maker MZ is the first implementation target.

Use built-in systems whenever possible:

- maps,
- transfer events,
- switches,
- variables,
- common events,
- database enemies,
- troops,
- skills,
- items,
- states,
- animations,
- picture events,
- screen tint and flash,
- simple plugin extensions when justified.

Avoid required systems that depend on complex custom engines, real-time hacking minigames, procedural generation, or plugin-heavy combat rewrites.

If RPG Maker MZ can fake it convincingly, fake it.

---

## Implementation Naming Standards

Use readable names for switches, variables, and common events.

Preferred switch style:

```text
Act1_Sword_Obtained
Act1_Island_Node_Offline
Act2_World_Open
Memory_Archive_03_Percent
Coalmouth_Mine_Cleared
Athenaeum_Node_Offline
```

Avoid vague names such as:

```text
Switch 21
Door Open
Boss Dead
Thing Done
```

---

## Preserve, Archive, Replace

The current implementation may contain useful assets and ideas.

Do not delete old concepts casually.

If something is removed from active production but may be useful later, move it to an archive location or document it in a design decision log.

Old ideas often become useful after the world becomes clearer.

---

## Production Quality Bar

Before accepting implementation, ask:

1. Does it match Atlas?
2. Does it feel Dragon Quest-inspired without copying Dragon Quest?
3. Does it support wonder, curiosity, or hope?
4. Does it obey the hidden technology layer?
5. Is it maintainable in RPG Maker MZ?
6. Can another agent understand and extend it later?

If not, revise before expanding.

---

## Future Expansion

This page should later split into:

- RPG Maker MZ Bible
- Switch Standards
- Variable Standards
- Common Event Standards
- Database ID Ranges
- Plugin Standards
- Asset Naming Standards
- Build/Test Workflow

---

## Revision History

| Version | Change |
|---|---|
| 0.5 | Migrated and refactored into Atlas Technical section |
