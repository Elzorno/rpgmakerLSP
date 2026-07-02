---
object_id: MON-GLM-001
atlas_id: MON-GLM-001
title: Coal Golem
object_type: Monster
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
family: FAM-GLM-001
relationships:
  belongs_to_family:
    - FAM-GLM-001
  appears_in:
    - LOC-CMN-001
---

# Coal Golem

Coal Golem is the first heavy construct-style enemy in Coalmouth Mine.

---

## Purpose

Coal Golem teaches the player that some mine threats are machinery or maintenance systems interpreted as monsters.

---

## Fantasy Presentation

A hulking coal-and-stone body that lumbers through mine tunnels as if pulled by the deep earth.

---

## Hidden Reality

A degraded hauling or maintenance construct responding to corrupted industrial control commands.

---

## Encounter Role

Slow defensive enemy.

---

## Behavior

- high defense,
- slow action,
- heavy strike,
- may guard or charge.

---

## Abilities

```text
Heavy Strike
Brace
Coal Toss
```

---

## Art Direction

Front-view RPG Maker MZ battler, transparent background, chunky coal-and-stone construct with old metal braces, warm amber cracks, heavy arms, readable silhouette, classic JRPG enemy style.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| belongs_to_family | FAM-GLM-001 | Golem Family |
| appears_in | LOC-CMN-001 | Coalmouth Mine |
| foreshadows | REL-006 | Old automation systems failing |

---

## RPG Maker Implementation Notes

Use sparingly in early Coalmouth mine encounters.

Consider weakness to Vera tool skill once Vera is implemented.

---

## Open Questions

- Should Coal Golem be optional before Vera joins?
- Should it resist normal physical damage slightly?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coal Golem monster object |
