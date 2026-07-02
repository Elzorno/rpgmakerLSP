---
object_id: LOC-HCV-001
atlas_id: LOC-HCV-001
title: Hidden Cave / Excalibur Vaultlet
object_type: Location
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
journey:
  - JRN-001
relationships:
  located_in:
    - LOC-SKY-001
  contains:
    - ITM-SWD-001
  related_to:
    - CHR-KAI-001
    - QST-HOM-002
---

# Hidden Cave / Excalibur Vaultlet

The Hidden Cave is the concealed trial site beneath Skyreach Hill where Kai obtains the Sword.

The fantasy layer presents it as a sacred cave. The hidden layer identifies it as a small secure Project Excalibur access facility.

---

## Purpose

This location is the first major transformation point in the game.

Kai enters as a curious island youth and leaves as the authenticated bearer of the Sword.

---

## Player-Facing Description

A quiet cave of old stone, reflective walls, carved symbols, sealed chambers, and a pedestal holding the legendary Sword.

It should feel sacred before it feels technical.

---

## Hidden Reality

The cave is a secure authentication vaultlet protecting Project Excalibur.

The trials are degraded identity, judgment, and readiness checks preserved as ritualized challenge chambers.

---

## Map Requirements

Required maps:

- cave entrance,
- trial chamber one,
- trial chamber two,
- trial chamber three,
- inner sanctum / Sword pedestal.

---

## Trial Structure

Suggested trial meanings:

| Trial | Fantasy Presentation | Hidden Reality |
|---|---|---|
| Body | simple combat/navigation challenge | basic safety and presence validation |
| Mind | observation puzzle | pattern recognition / challenge-response |
| Heart | choice or memory moment | trust / intent evaluation |

---

## Key Item

| ID | Item | Role |
|---|---|---|
| ITM-SWD-001 | The Sword / Project Excalibur | Primary story artifact |

---

## Visual Direction

Stone cave with geometric lines, dim blue-white lights, ancient panels treated as runes, and a clear pedestal focal point.

---

## Audio Direction

Begin with quiet cave ambience. Remove most music near the Sword pedestal. Use a rising authentication tone when the Sword awakens.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | LOC-SKY-001 | Hidden under Skyreach Hill |
| contains | ITM-SWD-001 | Sword is obtained here |
| advances_quest | QST-HOM-002 | Sword awakening quest |
| related_to | CHR-KAI-001 | Kai is authenticated here |

---

## RPG Maker Implementation Notes

Use evented trials and a cutscene for Sword authentication.

Suggested switches/variables:

```text
J1_HiddenCave_Entered
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
J1_Sword_Obtained
Archive_Recovery_Percent = 3
```

---

## Open Questions

- Should the trials be mandatory gameplay challenges or short narrative events?
- Should the Sword speak immediately or only display archive text?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Hidden Cave location object |
