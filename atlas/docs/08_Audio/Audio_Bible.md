---
atlas_id: ATLAS-AUD-001
title: Audio Bible
status: Draft
version: 0.1
canonical: true
owner: Audio Direction
implementation_status: Not Started
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-CRT-001
  - ATLAS-WLD-001
  - ATLAS-STY-001
related:
  - ATLAS-ART-001
  - ATLAS-TEC-010
---

# Audio Bible

The Audio Bible defines the music and sound language for _The Last Sword Protocol_.

It guides future music direction, sound effects, leitmotifs, environmental audio, UI sounds, battle themes, and audio prompts.

---

## Purpose

This document answers:

> What should the world sound like, and how should the soundtrack reveal the hidden truth over time?

Audio should reinforce memory, place, mystery, and hope.

---

## Core Audio Rule

The soundtrack should feel like a classic JRPG adventure first.

The hidden technology layer should enter gradually through subtle textures, pulses, drones, filtered tones, and rhythmic patterns that become more recognizable as old-world systems are revealed.

---

## Audio Pillars

| Pillar | Meaning |
|---|---|
| Melody | Important places should be hummable and emotionally clear |
| Memory | Themes should evolve as the player learns more |
| Warmth | Towns should sound human, not mechanical |
| Mystery | Ruins should invite curiosity rather than only fear |
| Hope | Even sad tracks should leave emotional light |
| Transformation | Technology tones should move from hidden texture to explicit identity |

---

## Musical Progression Curve

```text
Journey I: Acoustic warmth, simple melodies, subtle strange tones
Journey II: Regional themes with faint pulses and old-world motifs
Journey III: Archive motifs become clearer and more structured
Journey IV: Machine textures and rhythmic systems emerge openly
Journey V: Fantasy melody and machine motif resolve together
```

---

## Core Leitmotifs

| Motif | Emotional Meaning | Use |
|---|---|---|
| Kai's Theme | Curiosity becoming responsibility | Home, quiet reflection, final return |
| Sword / Excalibur Motif | Trust, recognition, hidden purpose | Sword awakening, doors, relay events |
| Archive Motif | Memory, lost people, recovered truth | Memory fragments, shrines, old terminals |
| NEMESIS Motif | Order without wisdom | Herald scenes, Dead Circuit, Vault |
| Ashford Theme | Home, warmth, ordinary life | Starting village and return moments |
| Restoration Motif | Hope after repair | Node shutdowns, healed towns, ending |

---

## Regional Audio Language

| Region | Audio Identity | Hidden Tech Texture |
|---|---|---|
| Ashford | Warm melody, woodwinds/strings, gentle rhythm | Barely audible low pulse near ruins |
| Fogfen Marsh | Soft percussion, misty pads, uneasy intervals | Distant electric hum, submerged signal ticks |
| Skyreach Hill | Airy, sacred, sparse | High harmonic tone during authentication |
| Coalmouth | Percussion, low strings, work rhythm | Industrial clanks and repeating machine patterns |
| Athenaeum | Harp/piano-like patterns, quiet reverence | Data-like arpeggios, reversed tones |
| Irongate | March rhythm, brass-like strength | Command pulse, rigid percussion grid |
| Driftlands | Hand drums, plucked strings, traveling rhythm | Broken radio-like fragments in relic scenes |
| New Meridian | Grand civic theme, layered harmony | Subtle city power grid and transit tones |
| Dead Circuit | Sparse, cold, mechanical | Exposed drones, data pulses, signal sweep |
| Vault | Cathedral scale + machine precision | Full NEMESIS motif, cold system tones |

---

## Sound Effects Principles

Sound effects should support the hidden layer without explaining it.

| Event | Fantasy Sound | Hidden Layer Cue |
|---|---|---|
| Shrine save | chime, breath, soft bell | archive sync pulse |
| Sword authentication | rising tone, crystalline ring | challenge-response beeps hidden in texture |
| Door unlock | stone shift, rune flare | access granted chirp layered quietly |
| Curse | low sting, distortion | corrupted signal texture |
| Relay shutdown | bass drop, silence, clean chime | system power-down and trust reset |
| Memory fragment | soft static into melody | archive playback start |
| NEMESIS voice | calm filtered presence | clinical signal, minimal emotion |

---

## NEMESIS Audio Rules

NEMESIS should not sound demonic.

It should sound controlled, clean, patient, and inhumanly certain.

Possible characteristics:

- filtered voice,
- low steady tone,
- precise pauses,
- minimal reverb,
- occasional harmonic dissonance,
- no rage,
- no monster growl unless filtered through another entity.

---

## Battle Music Rules

Battle music should remain energetic and approachable.

Avoid making every battle feel apocalyptic.

Suggested categories:

- standard battle,
- dangerous region battle,
- boss battle,
- relay boss,
- Herald battle,
- Dead Circuit battle,
- NEMESIS final sequence.

Relay bosses should include fragments of the region theme and the Sword/Excalibur motif.

---

## Silence Rules

Silence is a design tool.

Use silence or near-silence for:

- first Sword authentication,
- major archive reveals,
- Dead Circuit arrival,
- before NEMESIS speaks directly,
- the moment after final revocation.

Do not overuse silence in normal exploration.

---

## Production Rules

1. Music should loop cleanly.
2. Tracks should be usable in RPG Maker MZ without complex middleware.
3. Important motifs should be reusable across tracks.
4. Sound effects should be short and readable.
5. Audio names should follow clear implementation naming.
6. Avoid copyrighted musical imitation.

---

## Future Expansion

This document will later split into:

- Music Philosophy
- Leitmotif Guide
- Region Theme Guide
- Battle Theme Guide
- NEMESIS Sound Language
- Sound Effect Library
- Audio Asset Naming Standards
- Music Prompt Library

---

## Open Questions

- Should the soundtrack lean chiptune, orchestral pixel-RPG, or hybrid?
- Should major memory fragments use voice-like sound design without actual voice acting?
- Should NEMESIS ever have a fully voiced line, or remain text plus sound design?
- Should each relay node have a short shutdown jingle variation?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Audio Bible foundation |
