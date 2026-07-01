---
object_id: FAM-SCP-001
atlas_id: FAM-SCP-001
title: Scorpion Family
object_type: MonsterFamily
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  contains:
    - MON-SCP-001
  appears_in:
    - REG-COA-001
    - LOC-CMN-001
---

# Scorpion Family

The Scorpion Family introduces status pressure and cave-adapted predators.

---

## Purpose

Scorpions add danger to mine and desert-like regions without requiring complex mechanics.

---

## Fantasy Presentation

Hard-shelled cave predators with stinging tails, often found near warm vents, coal seams, and old tunnels.

---

## Hidden Reality

Wildlife adapted to industrial heat, mineral exposure, and old infrastructure runoff.

---

## Silhouette

- Low body.
- Large claws.
- Curved raised tail.
- Clearly readable sting pose.

---

## Behavior Pattern

- moderate HP,
- sting attack,
- low chance poison or defense debuff,
- physical threat.

---

## Initial Variant

| ID | Name | Role |
|---|---|---|
| MON-SCP-001 | Mine Scorpion | Coalmouth mine status enemy |

---

## Art Direction

RPG Maker MZ front-view battler, transparent background, stylized cave scorpion, coal-black shell, amber highlights, readable claws and tail, not too realistic or frightening.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| contains | MON-SCP-001 | Coalmouth mine variant |
| appears_in | LOC-CMN-001 | Mine dungeon |

---

## RPG Maker Implementation Notes

Use carefully. Early poison should be low-risk and paired with accessible recovery.

---

## Open Questions

- Should Mine Scorpion introduce poison, or should it use a temporary defense debuff instead?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Scorpion Family object |
