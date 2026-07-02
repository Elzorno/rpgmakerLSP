---
atlas_id: ATLAS-GME-001
title: Gameplay Systems Bible
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-CRT-001
  - ATLAS-TEC-010
  - ATLAS-TEC-011
related:
  - ATLAS-WLD-001
  - ATLAS-STY-000
  - ATLAS-TEC-001
---

# Gameplay Systems Bible

The Gameplay Systems Bible defines how familiar JRPG mechanics operate in _The Last Sword Protocol_ and how those mechanics map to the hidden technology layer.

This document does not replace RPG Maker implementation standards. It explains what gameplay systems mean inside the world.

---

## Purpose

This document answers:

> What does each gameplay mechanic represent in the visible fantasy layer, the hidden reality layer, and implementation?

The goal is to keep gameplay simple and familiar while making the world internally coherent.

---

## Design Rule

Gameplay should feel like a classic Dragon Quest-inspired turn-based JRPG.

The hidden meaning should deepen the systems, not complicate them.

A player who never notices the cybersecurity layer should still understand how to play.

---

## Core System Mapping

| Gameplay System | Fantasy Understanding | Hidden Reality | RPG Maker Representation |
|---|---|---|---|
| HP | Health / vitality | Biological condition | Actor HP |
| MP | Mana / spirit power | Sword energy reserve or system budget | Actor MP |
| Level | Experience and growth | Synchronization with Sword and combat learning | Actor level |
| Experience | Battle experience | Pattern learning / adaptation | EXP |
| Gold | Currency | Local trade economy | Gold |
| Save Point | Shrine of Memory | Archive terminal | Save event |
| Inn | Rest and recovery | Biological rest, local care | Recover all / gold cost |
| Church / Revival | Sacred restoration | Medical recovery / backup restoration | Revive event or service |
| Spell | Magic | Protocol action or system command | Skill |
| Skill | Technique | Learned combat action or Sword function | Skill |
| Equipment | Weapons and armor | Tools, interfaces, permission-bearing relics | Database equipment |
| Key Item | Important relic | Token, credential, data fragment, physical tool | Key item |
| Status Effect | Curse / blessing / condition | Corruption, signal effect, injury, authentication state | State |
| Fast Travel | Warp / ancient road | Relay routing | Common event / transfer |
| Boss Battle | Monster or guardian | Node guardian, corrupted system, or major threat | Troop encounter |
| Quest | Local problem | Human consequence of hidden system failure | Switch/variable chain |

---

## HP and Survival

### Fantasy Layer

HP represents physical vitality and endurance.

### Hidden Reality Layer

HP remains mostly biological. Not every system requires a cybersecurity metaphor.

### Production Layer

Use normal RPG Maker HP. Keep combat readable and traditional.

### Design Rule

Do not overcomplicate HP. Let it be health.

---

## MP and Protocol Energy

### Fantasy Layer

Villagers may call it spirit, mana, focus, or inner strength.

### Hidden Reality Layer

For Kai, MP represents energy available to Project Excalibur-linked protocol actions. For other party members, MP may represent stamina, focus, device charge, or specialized training depending on character.

### Production Layer

Use normal RPG Maker MP.

### Design Rule

MP can be described differently by character, but mechanically it remains simple.

---

## Leveling

### Fantasy Layer

Characters grow stronger through adventure.

### Hidden Reality Layer

Kai becomes more synchronized with the Sword and gains practical experience interpreting old systems. Other characters improve through training, field experience, and confidence.

### Production Layer

Use standard RPG Maker leveling.

### Design Rule

Do not require a custom leveling system. The hidden explanation is narrative, not mechanical complexity.

---

## Save Points / Memory Shrines

### Fantasy Layer

A Memory Shrine is a place where travelers pray and entrust their journey to the ancestors.

### Hidden Reality Layer

A Memory Shrine is an archive terminal, still powered enough to record state, synchronize limited data, and sometimes recover minor injuries.

### Production Layer

Use evented save points.

Optional effects:

- save command,
- recover all,
- play chime,
- screen glow,
- short archive text,
- update archive-related variables.

### Design Rule

Save points are one of the earliest clues that “magic” behaves like infrastructure.

---

## Resurrection / Revival

### Fantasy Layer

A priest, shrine, or sacred relic restores fallen companions.

### Hidden Reality Layer

Revival represents emergency medical recovery, nanomedical intervention, or recovery from a stored biological support protocol. This should remain slightly abstract to avoid making death feel too clinical.

### Production Layer

Use standard RPG Maker revive services or items.

### Design Rule

Revival should be treated as rare, sacred, and familiar to JRPG players. Do not over-explain it early.

---

## Protocol Skills / Magic

### Fantasy Layer

Protocol skills appear to be magic: light, seals, cleansing, barriers, echoes, and restoration.

### Hidden Reality Layer

They are commands issued through Project Excalibur or supporting relics.

Examples:

| Skill Fantasy Name | Hidden Function | Gameplay Role |
|---|---|---|
| Seal | Establish trust boundary | Defensive buff / lock interaction |
| Cleanse | Remove corruption | Cure state |
| Echo | Read residual archive | Reveal clue / lore |
| Restore | Repair biological or system damage | Heal |
| Ward | Isolate party from hostile signal | Resistance buff |
| Override | Issue privileged command | Late-game puzzle/boss mechanic |

### Production Layer

Use RPG Maker skills, states, common events, and animations.

### Design Rule

Early skill names should lean fantasy. Late-game descriptions may become more technical as Kai understands the truth.

---

## Equipment

### Fantasy Layer

Weapons, armor, charms, crests, and relics improve the party.

### Hidden Reality Layer

Some equipment is ordinary. Some relic equipment carries credentials, interfaces, or trusted circuitry.

### Production Layer

Use normal RPG Maker weapons, armor, and accessories.

### Design Rule

Not all equipment needs a hidden technology explanation. Ordinary swords and armor can exist. Relics should matter when they are special.

---

## Key Items

### Fantasy Layer

Ancient keys, crests, crystals, seals, and relics unlock progress.

### Hidden Reality Layer

Key items may represent:

- physical access tokens,
- RFID-like identifiers,
- private key fragments,
- data shards,
- permission tokens,
- hardware modules,
- old-world tools.

### Production Layer

Use RPG Maker key items checked by events.

### Design Rule

Key items should feel meaningful, not arbitrary. Whenever possible, NPC clues should foreshadow their use.

---

## Status Effects

Status effects should preserve JRPG readability while supporting the hidden layer.

| Status | Fantasy | Hidden Reality |
|---|---|---|
| Poison | Venom / curse | Biological toxin or corrupted environmental exposure |
| Blind | Darkness | Sensor disruption / injury |
| Silence | Sealed voice | Command channel blocked |
| Confusion | Bewilderment | Signal interference or hostile process influence |
| Paralysis | Binding curse | Neural/muscular disruption or stun field |
| Sleep | Magical sleep | Sedative, fatigue, or low-frequency signal |
| Blessing | Sacred protection | Trusted state / authentication buff |
| Corruption | Dark infection | Malware-like compromise or signal poisoning |

### Production Layer

Use RPG Maker states.

### Design Rule

Keep player-facing names readable. Hidden explanations belong in Atlas unless the story has reached the reveal stage.

---

## Fast Travel

### Fantasy Layer

The party uses ancient roads, warp shrines, or restored relay paths.

### Hidden Reality Layer

Fast travel is authenticated relay routing through limited surviving infrastructure.

### Production Layer

Use common events and transfer player commands.

### Design Rule

Fast travel should unlock through restoration, not convenience alone.

---

## Relay Progression

### Fantasy Layer

The party restores sacred sites or breaks curses across the world.

### Hidden Reality Layer

The party takes relay nodes offline, validates them, or revokes corrupted authority to recover parts of the Sword archive.

### Production Layer

Use switches and variables:

```text
Node_07_Offline
Node_06_Offline
Archive_Recovery_Percent
Act2_World_Open
```

### Design Rule

Relays are the project’s equivalent of classic magical objectives. They should feel meaningful in both fantasy and hidden-reality terms.

---

## Exploration Rewards

Exploration should reward curiosity through:

- hidden items,
- lore clues,
- memory fragments,
- rare enemies,
- optional bosses,
- shortcuts,
- NPC changes,
- environmental reveals.

### Design Rule

A suspicious landmark should usually contain something.

---

## Death and Failure

### Fantasy Layer

Defeat means the party collapses and must recover.

### Hidden Reality Layer

No special explanation is required for normal party defeat.

### Production Layer

Use RPG Maker default defeat handling unless a story battle requires custom logic.

### Design Rule

Do not over-engineer failure states in early production.

---

## Production Constraints

Use simple RPG Maker systems first.

Avoid required mechanics that need:

- real-time hacking minigames,
- custom combat engines,
- procedural puzzles,
- complex plugin chains,
- heavily scripted UI systems.

The illusion matters more than technical novelty.

---

## Future Expansion

This document will later split into dedicated pages:

- Protocol Skill List
- Status Effect Bible
- Equipment and Relic Standards
- Save Shrine Implementation
- Fast Travel and Relay Routing
- Exploration Reward Standards
- Combat Balance Philosophy
- RPG Maker Database Mapping

---

## Open Questions

- Should MP be called MP in the UI, or renamed later?
- Should Protocol Skills be visibly distinct from ordinary combat skills?
- Should only Kai use protocol skills, or should other party members gain device-based equivalents?
- How much healing should be technological versus ordinary herbal/medical care?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Gameplay Systems Bible foundation |
