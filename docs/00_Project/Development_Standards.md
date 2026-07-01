---
Title: Development Standards
Version: 0.1
Status: Draft
Owner: Project Direction
Last Updated: 2026-07-01
Depends On: Project_Constitution.md, Studio_Manifesto.md
Referenced By: All production and AI workflow documents
---

# Development Standards

This document defines how *The Last Sword Protocol* should be developed once implementation resumes.

Implementation is currently paused. Existing RPG Maker MZ work is considered a prototype and capability test.

---

## 1. Atlas Comes First

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

## 2. Document Lifecycle

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

## 3. AI Agent Roles

### ChatGPT
Creative director, systems planner, continuity checker, and high-level documentation architect.

### Codex
Implementation engineer. Codex should modify RPG Maker JSON, events, maps, database entries, plugins, and tooling only after consulting Atlas.

### Claude
Narrative and documentation specialist. Claude should help with dialogue, NPC writing, books, memory fragments, quest text, and lore consistency.

### Image Generation Models
Asset production assistants. They should follow the Art Bible, Pixel Style Guide, Battler Guide, and Image Generation prompt library once those exist.

### Copilot
Local coding assistant. Best used for small scripts, repetitive edits, and tooling support.

---

## 4. RPG Maker MZ Reality Rule

Designs must remain practical for RPG Maker MZ.

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

## 5. Implementation Naming Standards

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

## 6. Preserve, Archive, Replace

The current implementation may contain useful assets and ideas.

Do not delete old concepts casually.

If something is removed from active production but may be useful later, move it to an archive location or document it in a design decision log.

Old ideas often become useful after the world becomes clearer.

---

## 7. Production Quality Bar

Before accepting implementation, ask:

1. Does it match Atlas?
2. Does it feel Dragon Quest-inspired without copying Dragon Quest?
3. Does it support wonder, curiosity, or hope?
4. Does it obey the hidden technology layer?
5. Is it maintainable in RPG Maker MZ?
6. Can another agent understand and extend it later?

If not, revise before expanding.
