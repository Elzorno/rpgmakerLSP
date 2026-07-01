---
object_id: ITM-SWD-001
atlas_id: ITM-SWD-001
title: The Sword / Project Excalibur
object_type: Item
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
relationships:
  found_in:
    - LOC-HCV-001
  required_by:
    - LOC-SND-001
    - REL-007
  related_to:
    - CHR-KAI-001
    - CHR-ARC-001
    - CHR-NEM-001
---

# The Sword / Project Excalibur

The Sword is the central artifact of _The Last Sword Protocol_.

To the player and the world, it is a legendary blade. In hidden reality, it is Project Excalibur: the last trusted interface to the old-world security architecture.

---

## Purpose

The Sword gives the game its fantasy identity and hidden technical spine.

It must feel magical before it feels technological.

---

## Player-Facing Description

A blade sealed in the hidden cave beneath Skyreach Hill. It responds to Kai and awakens with ancient light.

Early text should emphasize awe, recognition, and mystery.

---

## Hidden Reality

Project Excalibur functions as:

- hardware root of trust,
- identity-bound authorization device,
- archive interface,
- relay validation tool,
- emergency revocation mechanism.

---

## Gameplay Function

Initial functions:

- unlocks story progression,
- grants access to sealed systems,
- enables archive recovery,
- may function as Kai's weapon,
- may unlock Protocol Skills over time.

---

## Acquisition

Found in:

| Relationship | Target ID | Notes |
|---|---|---|
| found_in | LOC-HCV-001 | Hidden Cave / Excalibur Vaultlet |

---

## Use Conditions

The Sword should not give full access immediately.

Authority expands as:

- archive recovery increases,
- relay nodes are resolved,
- Kai learns the truth,
- trust is restored across the world.

---

## RPG Maker Implementation Notes

Represent as both:

- key item, and possibly
- weapon.

Suggested switches:

```text
J1_Sword_Obtained
SYS_ProtocolSkills_Unlocked
```

Suggested variable:

```text
Archive_Recovery_Percent
```

---

## Open Questions

- Should the Sword be equippable immediately, or first appear only as key item?
- Should it visually change as archive recovery increases?
- Should Protocol Skills be tied to the Sword as skill type?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sword / Project Excalibur item object |
