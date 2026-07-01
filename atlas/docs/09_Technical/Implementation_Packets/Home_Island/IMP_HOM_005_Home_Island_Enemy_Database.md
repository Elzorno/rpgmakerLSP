---
object_id: IMP-HOM-005
atlas_id: IMP-HOM-005
title: Build Home Island Enemy Database
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - MON-GEL-001
    - MON-GEL-002
    - MON-RAT-001
    - BOS-N07-001
  requires:
    - ATLAS-MON-001
    - ATLAS-TEC-020
---

# Implementation Packet: Build Home Island Enemy Database

## Objective

Create the first RPG Maker MZ enemy database entries and encounter logic for Home Island.

---

## Atlas References

| ID | Reference |
|---|---|
| FAM-GEL-001 | Gel Family |
| FAM-RAT-001 | Rat Family |
| MON-GEL-001 | Meadow Gel |
| MON-GEL-002 | Marsh Gel |
| MON-RAT-001 | Ash Rat |
| BOS-N07-001 | Node Seven Guardian |

---

## Scope

Included:

- first three common enemy entries,
- one boss placeholder entry,
- initial troop recommendations,
- early encounter placement guidance,
- placeholder balancing notes.

Out of scope:

- final battler art,
- final stat balance,
- final skill animations,
- final drop table tuning.

---

## Enemy Entries

| Suggested Enemy ID | Object ID | Name | Role |
|---|---|---|---|
| 1 | MON-GEL-001 | Meadow Gel | Basic starter enemy |
| 2 | MON-RAT-001 | Ash Rat | Faster starter enemy |
| 3 | MON-GEL-002 | Marsh Gel | Early status/debuff variant |
| 10 | BOS-N07-001 | Node Seven Guardian | Journey I boss |

---

## Troop Recommendations

| Suggested Troop | Composition | Use |
|---|---|---|
| Home Field 1 | 1 Meadow Gel | First simple encounter |
| Home Field 2 | 2 Meadow Gels | Basic group fight |
| Home Field 3 | 1 Ash Rat + 1 Meadow Gel | Speed contrast |
| Fogfen 1 | 1 Marsh Gel | Introduce variant |
| Fogfen 2 | 1 Marsh Gel + 1 Ash Rat | Slightly harder early fight |
| Node Boss | 1 Node Seven Guardian | Journey I climax |

---

## Skill Requirements

### Meadow Gel

```text
Attack
```

### Ash Rat

```text
Attack
Nibble(optional)
```

### Marsh Gel

```text
Attack
Murk Bubble(optional low-risk poison/debuff)
```

### Node Seven Guardian

```text
Strike
Pulse Guard
Warning Tone
Relay Burst
```

---

## Balance Philosophy

Early enemies should be forgiving.

The player should win basic field fights with normal attacks and occasional item use.

Marsh Gel may introduce status effects, but should not punish the player heavily before they have reliable recovery options.

Node Seven Guardian should feel like a real boss but should remain readable and fair.

---

## Encounter Placement

| Location | Recommended Enemies |
|---|---|
| Ashford outskirts | Meadow Gel, Ash Rat |
| Fogfen Marsh | Marsh Gel, Ash Rat |
| Glassfield Ruins | Meadow Gel, Ash Rat, early construct later |
| Sealed Node | Node Guardian plus possible construct enemies later |

---

## Required Assets

| Object ID | Asset Need |
|---|---|
| MON-GEL-001 | Battler image |
| MON-GEL-002 | Battler image / palette variant |
| MON-RAT-001 | Battler image |
| BOS-N07-001 | Boss battler image |

---

## Acceptance Criteria

- Enemies exist in RPG Maker database.
- Troops exist for basic testing.
- Encounters can be assigned to Home Island maps.
- Node Seven Guardian can be used in boss event.
- No enemy requires final art to function in prototype.

---

## Playtest Steps

1. Start test battle with Meadow Gel.
2. Start test battle with Ash Rat.
3. Start test battle with Marsh Gel.
4. Start test battle with Node Seven Guardian.
5. Confirm no troop crashes.
6. Confirm early fights are not overly punishing.

---

## Open Questions

- Should enemy stats be authored in Atlas before implementation or tuned directly in RPG Maker first?
- Should Marsh Gel introduce poison now or wait until mainland?
- Should Node Seven Guardian have a unique battle theme cue?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island enemy database packet |
