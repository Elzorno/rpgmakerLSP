---
atlas_id: ATLAS-TEC-056
title: Home Island Combat Database Spec
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-020
  - ATLAS-TEC-052
  - ATLAS-TEC-053
  - IMP-HOM-005
related:
  - CHR-KAI-001
  - MON-GEL-001
  - MON-GEL-002
  - MON-RAT-001
  - BOS-N07-001
---

# Home Island Combat Database Spec

## Objective

Define the RPG Maker MZ combat database rows required to build and test the Home Island vertical slice without inventing enemy stats, skills, states, troops, or first-pass player combat values outside Atlas.

This is a first-playable database specification. Values are expected to be tuned after implementation, but every required row has a stable ID and enough behavior to be entered into RPG Maker MZ.

---

## Source References

| ID | Reference |
|---|---|
| `ATLAS-TEC-052` | Truth Layer Diagram |
| `ATLAS-TEC-053` | Home Island Vertical Slice Readiness Review |
| `ATLAS-TEC-020` | RPG Maker MZ Bible |
| `IMP-HOM-005` | Build Home Island Enemy Database |
| `CHR-KAI-001` | Kai |
| `MON-GEL-001` | Meadow Gel |
| `MON-GEL-002` | Marsh Gel |
| `MON-RAT-001` | Ash Rat |
| `BOS-N07-001` | Node Seven Guardian |

---

## Database ID Allocation

Use the RPG Maker MZ database ranges defined in `ATLAS-TEC-020`.

| Database | ID | Name | Atlas Source | Notes |
|---|---:|---|---|---|
| Actor | 1 | Kai | `CHR-KAI-001` | Required starting actor |
| Class | 1 | Sword Bearer | `CHR-KAI-001` | First-pass balanced class label |
| Enemy | 1 | Meadow Gel | `MON-GEL-001` | Basic starter enemy |
| Enemy | 2 | Ash Rat | `MON-RAT-001` | Faster starter enemy |
| Enemy | 3 | Marsh Gel | `MON-GEL-002` | Early debuff variant |
| Enemy | 10 | Node Seven Guardian | `BOS-N07-001` | Journey I boss |
| Troop | 1 | HOM Field 1 | `MON-GEL-001` | One Meadow Gel |
| Troop | 2 | HOM Field 2 | `MON-GEL-001` | Two Meadow Gels |
| Troop | 3 | HOM Field 3 | `MON-RAT-001`, `MON-GEL-001` | Ash Rat plus Meadow Gel |
| Troop | 4 | HOM Fogfen 1 | `MON-GEL-002` | One Marsh Gel |
| Troop | 5 | HOM Fogfen 2 | `MON-GEL-002`, `MON-RAT-001` | Marsh Gel plus Ash Rat |
| Troop | 10 | HOM Node Boss | `BOS-N07-001` | One Node Seven Guardian |
| Skill | 1 | Attack | Engine default | Basic physical attack |
| Skill | 101 | Nibble | `MON-RAT-001` | Ash Rat pressure skill |
| Skill | 102 | Murk Bubble | `MON-GEL-002` | Low-risk signal debuff skill |
| Skill | 110 | Strike | `BOS-N07-001` | Guardian basic attack |
| Skill | 111 | Pulse Guard | `BOS-N07-001` | Guardian defensive action |
| Skill | 112 | Warning Tone | `BOS-N07-001` | Guardian telegraph action |
| Skill | 113 | Relay Burst | `BOS-N07-001` | Guardian heavy action |
| State | 1 | Knockout | Engine default | Use standard KO behavior |
| State | 11 | Signal-Slick | `MON-GEL-002` | Light accuracy debuff |
| State | 12 | Pulse Guard | `BOS-N07-001` | Temporary defense buff |
| State | 13 | Charging | `BOS-N07-001` | Telegraph marker for Relay Burst |
| Item | 1 | Potion | Prototype item | Basic early recovery item |
| Key Item | 201 | Sword / Project Excalibur | Sword truth layer | Story key item paired with weapon row |
| Weapon | 1 | Practice Sword | `CHR-KAI-001` | Starting weapon |
| Weapon | 2 | Sword / Project Excalibur | Sword truth layer | Story weapon after Sword acquisition |
| Armor | 1 | Plain Clothes | `CHR-KAI-001` | Starting armor |

Do not add poison to the Home Island first playable. Marsh Gel uses `Signal-Slick` instead so the vertical slice does not require antidote economy, poison tutorial text, or recovery balancing.

---

## Actor And Class Rows

### Actor 1: Kai

| Field | Value |
|---|---|
| Name | Kai |
| Nickname | Blank |
| Class | 1 - Sword Bearer |
| Initial Level | 1 |
| Max Level | 10 for prototype database |
| Starting Equipment | Weapon 1 - Practice Sword; Armor 1 - Plain Clothes |
| Starting Items | 2x Potion |
| Combat Role | Balanced physical lead for Home Island |

### Class 1: Sword Bearer

| Stat | Level 1 | Level 3 Test Target | Notes |
|---|---:|---:|---|
| Max HP | 120 | 150 | Allows early mistakes without making Meadow Gel harmless |
| Max MP | 24 | 30 | Reserved for later protocol skill testing |
| Attack | 18 | 24 | Primary first-pass damage stat |
| Defense | 14 | 18 | Lets basic enemies remain readable |
| Magic Attack | 12 | 15 | Not central in Home Island first playable |
| Magic Defense | 12 | 16 | Used against Murk Bubble if implemented as magical hit |
| Agility | 16 | 20 | Faster than gels, close to Ash Rat |
| Luck | 10 | 12 | Neutral starter value |

Class traits:

- Hit Rate: `95%`
- Evasion Rate: `5%`
- Equip Weapon Type: Sword
- Equip Armor Type: Light

---

## Enemy Rows

### Enemy 1: Meadow Gel

| Field | Value |
|---|---|
| Atlas Source | `MON-GEL-001` |
| Max HP | 28 |
| Max MP | 0 |
| Attack | 9 |
| Defense | 6 |
| Magic Attack | 1 |
| Magic Defense | 4 |
| Agility | 8 |
| Luck | 8 |
| EXP | 4 |
| Gold | 3 |
| Drop 1 | Potion, 5% |
| Drop 2 | None |
| Drop 3 | None |

Action pattern:

| Condition | Skill | Rating |
|---|---|---:|
| Always | Attack | 5 |

### Enemy 2: Ash Rat

| Field | Value |
|---|---|
| Atlas Source | `MON-RAT-001` |
| Max HP | 22 |
| Max MP | 0 |
| Attack | 11 |
| Defense | 5 |
| Magic Attack | 1 |
| Magic Defense | 3 |
| Agility | 14 |
| Luck | 10 |
| EXP | 5 |
| Gold | 4 |
| Drop 1 | Potion, 8% |
| Drop 2 | None |
| Drop 3 | None |

Action pattern:

| Condition | Skill | Rating |
|---|---|---:|
| Always | Attack | 4 |
| Turn 2 + 2X | Nibble | 5 |

### Enemy 3: Marsh Gel

| Field | Value |
|---|---|
| Atlas Source | `MON-GEL-002` |
| Max HP | 36 |
| Max MP | 6 |
| Attack | 10 |
| Defense | 7 |
| Magic Attack | 8 |
| Magic Defense | 7 |
| Agility | 7 |
| Luck | 8 |
| EXP | 7 |
| Gold | 5 |
| Drop 1 | Potion, 10% |
| Drop 2 | None |
| Drop 3 | None |

Action pattern:

| Condition | Skill | Rating |
|---|---|---:|
| Always | Attack | 4 |
| Turn 2 + 3X | Murk Bubble | 5 |

### Enemy 10: Node Seven Guardian

| Field | Value |
|---|---|
| Atlas Source | `BOS-N07-001` |
| Max HP | 260 |
| Max MP | 30 |
| Attack | 22 |
| Defense | 16 |
| Magic Attack | 18 |
| Magic Defense | 16 |
| Agility | 10 |
| Luck | 12 |
| EXP | 45 |
| Gold | 0 |
| Drop 1 | None |
| Drop 2 | None |
| Drop 3 | None |

Action pattern:

| Condition | Skill | Rating |
|---|---|---:|
| Always | Strike | 5 |
| Turn 1 + 3X | Warning Tone | 6 |
| Turn 2 + 3X | Relay Burst | 7 |
| HP 0% to 50% | Pulse Guard | 5 |

The `Warning Tone` / `Relay Burst` pattern is the required readability rule for this boss. The first-pass implementation may enforce it with turn conditions instead of a custom AI script.

---

## Skill Rows

Use Animation ID `1` for all combat skills until `BLK-HOM-005` assigns final or approved placeholder animations. This keeps the combat database runnable while leaving animation polish tracked separately.

| Skill ID | Name | Scope | Hit Type | Formula | Effects | Animation | Notes |
|---:|---|---|---|---|---|---:|---|
| 1 | Attack | 1 Enemy | Physical | Engine default | Normal attack | 1 | Keep default Attack row unless project defaults differ |
| 101 | Nibble | 1 Enemy | Physical | `a.atk * 3 - b.def * 2` | None | 1 | Faster Ash Rat pressure without status load |
| 102 | Murk Bubble | 1 Enemy | Magical | `a.mat * 2 + a.atk - b.mdf` | Add State 11 at 30% | 1 | Debuff replaces poison for first playable |
| 110 | Strike | 1 Enemy | Physical | `a.atk * 4 - b.def * 2` | None | 1 | Guardian basic attack |
| 111 | Pulse Guard | The User | Certain Hit | `0` | Add State 12 at 100% | 1 | Guardian defensive beat |
| 112 | Warning Tone | The User | Certain Hit | `0` | Add State 13 at 100% | 1 | Telegraph before Relay Burst |
| 113 | Relay Burst | 1 Enemy | Magical | `a.atk * 4 + a.mat * 2 - b.mdf * 2` | Remove State 13 from user if practical | 1 | Heavy readable attack after Warning Tone |

Recommended shared skill settings:

| Field | Value |
|---|---|
| Occasion | Battle Screen |
| Success Rate | 95% for physical attacks; 100% for guard/telegraph actions |
| Variance | 15% for damage skills; 0% for non-damage skills |
| Critical Hits | Yes for physical damage skills; No for Murk Bubble and non-damage skills |

---

## State Rows

### State 11: Signal-Slick

| Field | Value |
|---|---|
| Restriction | None |
| Priority | 45 |
| Remove at Battle End | Yes |
| Auto-removal Timing | Turn End |
| Duration | 2 turns |
| Remove by Damage | No |
| Traits | Hit Rate `-10%` |
| Message | `%1 is coated in murky signal residue.` |

### State 12: Pulse Guard

| Field | Value |
|---|---|
| Restriction | None |
| Priority | 50 |
| Remove at Battle End | Yes |
| Auto-removal Timing | Turn End |
| Duration | 2 turns |
| Remove by Damage | No |
| Traits | Defense `+25%`; Magic Defense `+25%` |
| Message | `%1 raises a defensive pulse.` |

### State 13: Charging

| Field | Value |
|---|---|
| Restriction | None |
| Priority | 55 |
| Remove at Battle End | Yes |
| Auto-removal Timing | Turn End |
| Duration | 1 turn |
| Remove by Damage | No |
| Traits | None |
| Message | `%1 begins building relay pressure.` |

---

## Item, Weapon, And Armor Rows

| Database | ID | Name | Core Fields |
|---|---:|---|---|
| Item | 1 | Potion | Scope: 1 Ally; Occasion: Always; Effect: Recover HP 50; Price: 50 |
| Key Item | 201 | Sword / Project Excalibur | Scope: None; Occasion: Never; Used for story ownership tracking |
| Weapon | 1 | Practice Sword | Attack +6; Price: 0; Weapon Type: Sword |
| Weapon | 2 | Sword / Project Excalibur | Attack +12; Magic Attack +4; Price: 0; Weapon Type: Sword |
| Armor | 1 | Plain Clothes | Defense +4; Magic Defense +2; Price: 0; Armor Type: Light |

The Sword appears as both a key item and a weapon row because the Truth Layer Diagram defines it as a story, gameplay, and implementation object. The event that awards it should set the relevant story switch and grant both rows if the prototype needs the weapon equipped immediately.

---

## Troop Rows

| Troop ID | Name | Members | Battle Test Purpose |
|---:|---|---|---|
| 1 | HOM Field 1 | 1x Enemy 1 Meadow Gel | First single-enemy check |
| 2 | HOM Field 2 | 2x Enemy 1 Meadow Gel | Early group check |
| 3 | HOM Field 3 | 1x Enemy 2 Ash Rat, 1x Enemy 1 Meadow Gel | Speed contrast check |
| 4 | HOM Fogfen 1 | 1x Enemy 3 Marsh Gel | Debuff introduction check |
| 5 | HOM Fogfen 2 | 1x Enemy 3 Marsh Gel, 1x Enemy 2 Ash Rat | Harder Fogfen check |
| 10 | HOM Node Boss | 1x Enemy 10 Node Seven Guardian | Journey I boss check |

Troop event pages:

| Troop ID | Page | Condition | Span | Commands |
|---:|---:|---|---|---|
| 1-5 | None | None | None | No troop event pages required |
| 10 | 1 | Turn 0 | Battle | Optional battle text placeholder: `BOSS_NODE_SEVEN_OPENING_PLACEHOLDER` |
| 10 | 2 | Enemy HP 0% to 50% | Battle | Optional battle text placeholder: `BOSS_NODE_SEVEN_HALF_HP_PLACEHOLDER` |

If placeholder battle text is omitted, the boss remains build-ready as long as its action pattern preserves the Warning Tone before Relay Burst.

---

## Encounter Placement

| Atlas Screen Group | Troops |
|---|---|
| Ashford outskirts and early field paths | Troop 1, Troop 2, Troop 3 |
| Fogfen Marsh traversable screens | Troop 4, Troop 5 |
| Glassfield approach | Troop 1, Troop 3 |
| Sealed Node | Troop 10 only |

Do not add random encounters to Ashford village interiors, trial rooms, the Sword chamber, or post-boss relay interaction screens unless a later Atlas packet explicitly requests them.

---

## System Settings For First Playable Testing

| Setting | Value |
|---|---|
| Starting Party | Actor 1 - Kai |
| Battle System | RPG Maker MZ default turn battle |
| Side View | Enabled if the project uses side-view actors; this spec does not require custom battle plugins |
| Defeat Handling | Use event-level defeat branches for required boss battles |
| Test Target | Kai at Level 2-3 should defeat Troop 10 with Potion use and readable Relay Burst timing |

---

## Balance Notes

- Meadow Gel should fall in 2-3 normal attacks at Level 1.
- Ash Rat should feel faster but fragile.
- Marsh Gel should teach that status/debuff skills exist without creating a poison-recovery blocker.
- Node Seven Guardian should take roughly 6-9 turns at Level 2-3 using first-pass values.
- If the boss defeats Kai before the player sees the Warning Tone / Relay Burst pattern twice, reduce `Relay Burst` damage before changing story or event structure.
- Final tuning remains non-blocking once these rows exist in the RPG Maker database.

---

## Validation

Run:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Expected result:

- 0 errors,
- 0 warnings.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island combat database specification |
