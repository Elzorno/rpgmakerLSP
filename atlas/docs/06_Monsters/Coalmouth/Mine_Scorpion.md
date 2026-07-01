---
object_id: MON-SCP-001
atlas_id: MON-SCP-001
title: Mine Scorpion
object_type: Monster
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
family: FAM-SCP-001
relationships:
  belongs_to_family:
    - FAM-SCP-001
  appears_in:
    - LOC-CMN-001
---

# Mine Scorpion

Mine Scorpion is the first Scorpion Family variant and a Coalmouth Mine status-pressure enemy.

---

## Purpose

Mine Scorpion introduces more dangerous cave wildlife and prepares the player for region-specific encounter roles.

---

## Fantasy Presentation

A coal-dark scorpion that nests near warm seams and abandoned tool piles.

---

## Hidden Reality

A cave predator adapted to industrial warmth, mineral exposure, and old infrastructure runoff.

---

## Encounter Role

Moderate threat with possible poison or defense debuff.

---

## Behavior

- physical sting,
- possible low-risk poison,
- moderate speed,
- usually appears alone or with Soot Gel.

---

## Abilities

```text
Sting
Pinch
Venom Prick
```

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, stylized cave scorpion, coal-black shell, amber highlights, large readable claws, curved tail, classic JRPG style, not realistic horror.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-SCP-001 | Scorpion Family |
| appears_in | LOC-CMN-001 | Coalmouth Mine |

---

## RPG Maker Implementation Notes

Use poison carefully. If early recovery is weak, implement Venom Prick as a minor debuff first.

---

## Open Questions

- Should Mine Scorpion drop antidote-like items to teach recovery?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Mine Scorpion monster object |
