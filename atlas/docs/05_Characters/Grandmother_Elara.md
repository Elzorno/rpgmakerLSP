---
object_id: NPC-ELA-001
atlas_id: NPC-ELA-001
title: Grandmother Elara
object_type: NPC
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  appears_in:
    - LOC-ASH-001
  related_to:
    - CHR-KAI-001
    - LOC-SKY-001
    - QST-HOM-001
    - QST-HOM-002
---

# Grandmother Elara

Grandmother Elara is Kai's emotional anchor and the keeper of inherited warnings on Home Island.

---

## Purpose

Elara makes the opening personal.

She preserves fragments of old-world safety procedures as family tradition, caution, and love.

---

## Role In Story

Elara warns Kai about Skyreach Hill and gives emotional context to the island's old stories.

Her warnings should become more meaningful after the player learns the hidden truth.

---

## Player-Facing Identity

Kai's grandmother, caretaker, and storyteller.

---

## Hidden-Layer Role

Elara does not fully understand Project Excalibur or Node Seven, but her family/community tradition preserves instructions that once protected the secure enclave.

---

## Personality

- warm,
- protective,
- perceptive,
- quietly worried,
- more knowledgeable than she claims,
- emotionally honest.

---

## Knowledge Level

Folk with inherited warning fragments.

She should not speak in technical language.

---

## Dialogue Rules

Elara should speak plainly and lovingly.

She should avoid exposition dumps. Her best lines should sound like family advice that later becomes prophecy-like in hindsight.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| appears_in | LOC-ASH-001 | Lives in Ashford |
| related_to | CHR-KAI-001 | Grandmother / caretaker |
| related_to | LOC-SKY-001 | Warns Kai about the hill |
| starts_quest | QST-HOM-001 | Opening guidance |
| advances_quest | QST-HOM-002 | Warning before Sword quest |

---

## RPG Maker Implementation Notes

Elara should have multiple dialogue states:

```text
Intro
After village exploration
After tremor
After Sword obtained
After Node Seven offline
Before mainland departure
```

---

## Open Questions

- Is Elara biologically related to the Architect's line, or did she inherit warnings through community tradition?
- Does she know the Sword is real?
- Should she give Kai a starting item?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Grandmother Elara NPC object |
