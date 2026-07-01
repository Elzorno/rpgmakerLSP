---
atlas_id: ATLAS-MON-001
title: Monster Bible
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-CRT-001
  - ATLAS-STY-001
  - ATLAS-WLD-001
  - ATLAS-TEC-010
  - ATLAS-GME-001
related:
  - ATLAS-TEC-011
---

# Monster Bible

The Monster Bible defines the enemy design philosophy, monster families, variant structure, regional progression, boss logic, and production rules for _The Last Sword Protocol_.

This document is the foundation for future bestiary entries, battler prompts, RPG Maker enemy database work, and encounter design.

---

## Purpose

This document answers:

> What should enemies feel like, how do they evolve through the story, and how can we produce them realistically?

Monsters should support the world, not merely fill battles.

---

## Core Monster Philosophy

_The Last Sword Protocol_ should use Dragon Quest-inspired monster design principles without copying Dragon Quest monsters.

Enemies should be:

- readable,
- charming early,
- memorable,
- family-based,
- palette-variant friendly,
- mechanically simple at first,
- increasingly strange as NEMESIS influence grows.

The player should understand enemy families quickly and enjoy seeing new variants.

---

## Family-Based Design

The project should prioritize monster families over hundreds of unrelated one-off enemies.

A family shares:

- silhouette,
- animation logic,
- base behavior,
- art prompt foundation,
- sound identity,
- general combat role.

Variants change:

- color palette,
- small visual details,
- stats,
- region,
- elemental/status behavior,
- corruption level.

This keeps asset production realistic for RPG Maker MZ and AI-generated battlers.

---

## Monster Progression Arc

Enemies should evolve with the story.

```text
Early Game: Nature
Middle Game: Nature disturbed
Late Game: Nature rewritten
Endgame: System and biology merged
```

### Early Game

Enemies should feel like local wildlife, minor spirits, pests, or simple constructs. They can be dangerous, but they should retain charm.

### Middle Game

Enemies show signs of signal corruption, mechanical intrusion, odd behavior, or abnormal mutation.

### Late Game

Enemies become visibly unnatural: exposed circuitry, glassy growths, metal bones, repeated patterns, signal halos, broken symmetry.

### Endgame

Enemies become expressions of NEMESIS logic: optimized, controlled, recursive, or system-like.

---

## Initial Monster Families

| Family | Early Fantasy Read | Hidden Reality | Production Notes |
|---|---|---|---|
| Slime / Gel | Living ooze | Biofilm, waste culture, adaptive gel | Ideal palette-swap starter family |
| Rat | Cave or town pest | Wildlife near old infrastructure | Good early low-threat enemy |
| Crow | Ominous bird | Scavenger affected by signals | Useful overworld/ruin enemy |
| Wolf | Wild predator | Pack animal with signal disruption | Midgame physical threat |
| Scorpion | Desert/mine creature | Toxic adaptation near industrial waste | Status-focused family |
| Skeleton | Restless dead | Misread remains / defense constructs / armor husks | Fantasy layer must be handled carefully since no supernatural undead |
| Golem | Animated stone/metal guardian | Autonomous maintenance or security construct | Strong defensive family |
| Drone | Floating watcher | Old-world surveillance or repair unit | Technology becomes more visible |
| Automaton | Ancient machine soldier | Autonomous defense platform | Mid-to-late construct family |
| Cultist | Human enemy | Socially engineered or Herald-aligned follower | Use sparingly and respectfully |
| Aberration | Twisted monster | Bio-mechanical corruption | Late/endgame horror escalation |

---

## Example Family: Slime / Gel

### Role

Starter enemy family. Friendly silhouette, simple behavior, strong variant potential.

### Hidden Reality

Not magical slime. It may be an adaptive biofilm, chemical waste organism, or post-collapse gel lifeform evolved around old infrastructure.

### Variants

| Variant | Region | Behavior |
|---|---|---|
| Meadow Gel | Home Island | Basic attack |
| Marsh Gel | Fogfen Marsh | Poison chance |
| Spark Gel | Near relay systems | Minor lightning/status effect |
| Mirror Gel | Athenaeum ruins | Magic reflection or evasion |
| Relay Gel | Late relay areas | Buffs other enemies |
| Crowned Gel | Optional | Mini-boss / rare encounter |

### Art Notes

- Round, simple, expressive.
- Early variants should be cute or charming.
- Late variants may include embedded glass, wire, or glowing signal cores.

---

## Example Family: Rat

### Role

Low-level pest and cave enemy.

### Hidden Reality

Ordinary wildlife thriving around abandoned infrastructure and food stores.

### Variants

| Variant | Region | Behavior |
|---|---|---|
| Ash Rat | Ashford outskirts | Basic attack |
| Tunnel Rat | Mines/caves | Faster attack |
| Wire Rat | Coalmouth | Small shock attack |
| Plague Rat | Driftlands | Poison/status |
| Iron Rat | Dead Circuit | High defense, mechanical plating |

---

## Example Family: Golem

### Role

Heavy construct family, often tied to ruins or relay sites.

### Hidden Reality

Maintenance, construction, or security machines misunderstood as animated stone or metal guardians.

### Variants

| Variant | Region | Behavior |
|---|---|---|
| Clay Golem | Early ruins | Slow physical attacker |
| Coal Golem | Coalmouth | Fire/soot behavior |
| Iron Golem | Irongate | High defense |
| Archive Golem | Athenaeum | Protects knowledge systems |
| Relay Golem | Relay nodes | Buffs or guards systems |
| Titan Golem | Optional/endgame | Boss-level construct |

---

## Skeleton Design Rule

Because Atlas has locked that there is no supernatural magic, skeleton enemies require special handling.

They should not literally be reanimated dead by necromancy.

Acceptable hidden explanations:

- old armor frames mistaken for skeletons,
- medical teaching constructs,
- defense drones wearing bone-like plating,
- corrupted exoskeletal remains,
- folk interpretation of mechanical husks.

Fantasy presentation can still call them skeletons if villagers believe that is what they are.

---

## Human Enemies

Human enemies should be used carefully.

They may include:

- bandits,
- desperate scavengers,
- Herald followers,
- corrupted guards,
- cultic zealots.

Design rules:

1. Avoid making ordinary poverty into villainy.
2. Human enemies should usually have context.
3. Herald-aligned humans should demonstrate social engineering and fear.
4. Avoid overusing human battles in a hopeful JRPG tone.

---

## Boss Philosophy

Bosses should represent story systems, not just large enemies.

A good boss should answer:

1. What local problem does this boss embody?
2. What hidden system is failing?
3. What does defeating it change in the world?
4. What does the player learn afterward?

---

## Relay Bosses

Relay bosses are guardians, corrupted systems, or system manifestations attached to major nodes.

| Node | Region | Boss Concept | Hidden Theme |
|---|---|---|---|
| Node 7 | Home Island | Sealed Guardian | Authentication / secure enclave |
| Node 6 | Coalmouth | Iron Foreman | ICS automation compromise |
| Node 5 | Athenaeum | Archive Warden | Integrity / data poisoning |
| Node 4 | Irongate | Command Saint / War Engine | Spoofed authority |
| Node 3 | Driftlands | Relic Carrier | Supply-chain compromise |
| Node 2 | New Meridian | Civic Mandate | Privilege abuse / centralized control |
| Node 1 | Dead Circuit | Backbone Seraph | Trust chain collapse |

Names are draft concepts and may change.

---

## Regional Encounter Logic

### Home Island

Mostly natural and charming enemies:

- Meadow Gel,
- Ash Rat,
- Field Crow,
- Marsh Gel,
- young wolf or local predator,
- early cave construct.

### Coalmouth

Industrial enemies:

- Tunnel Rat,
- Coal Golem,
- Soot Gel,
- Mine Scorpion,
- broken maintenance drones.

### Athenaeum

Knowledge/archive enemies:

- Mirror Gel,
- Paper Wisp-like data scraps (must have hidden tech explanation),
- Archive Golem,
- corrupted librarian construct,
- signal birds.

### Irongate

Authority and defense enemies:

- Iron Golem,
- armored hounds,
- Herald soldiers,
- command drones,
- defense automatons.

### Driftlands

Trade and survival enemies:

- Plague Rat,
- Sand Scorpion,
- caravan bandits,
- relic-infected wildlife,
- supply-chain corrupted constructs.

### Dead Circuit

Late-game enemies:

- Iron Rat,
- Relay Gel,
- broken angelic constructs,
- aberrations,
- drone swarms,
- automaton elites.

---

## Art Production Rules

Monster art should be designed for reuse.

Each family should have:

- base silhouette,
- palette variants,
- optional minor detail variants,
- front-view battler prompt,
- RPG Maker MZ scale target,
- face/icon need if used in UI,
- animation notes if animated later.

### AI Image Prompt Rule

Prompts should define:

1. family silhouette,
2. charm level,
3. corruption level,
4. region,
5. palette,
6. RPG Maker MZ front-view battler format,
7. transparent background requirement when needed.

---

## Combat Design Rules

1. Early enemies should teach basic mechanics.
2. Variant names should communicate behavior.
3. Status effects should be introduced gradually.
4. Bosses should have readable patterns.
5. Avoid difficulty spikes caused by obscure mechanics.
6. Recolors are not lazy if variants are meaningful.

---

## Future Expansion

This document will later split into:

- Enemy Family Standards
- Slime / Gel Family
- Rat Family
- Crow Family
- Scorpion Family
- Wolf Family
- Skeleton / Husk Family
- Golem Family
- Drone Family
- Automaton Family
- Aberration Family
- Boss Bible
- Regional Encounter Tables
- RPG Maker Enemy Database Mapping
- Battler Prompt Library

---

## Open Questions

- Should the basic slime-like family be called Slime, Gel, Droplet, Puddle, or something original?
- How close can monster charm feel to Dragon Quest without becoming imitation?
- Should human enemies appear in random encounters or only as story encounters?
- Should late-game aberrations remain colorful or become visually colder and more technological?
- Should enemy names use fantasy terms early and technical terms late?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Monster Bible foundation |
