---
atlas_id: ATLAS-AUD-010
title: Home Island Audio Cue Packet
status: Draft
version: 0.1
canonical: true
owner: Audio Direction
implementation_status: Not Started
dependencies:
  - ATLAS-AUD-001
  - REG-HOM-001
related:
  - LOC-ASH-001
  - LOC-RST-001
  - LOC-FOG-001
  - LOC-GLS-001
  - LOC-SKY-001
  - LOC-HCV-001
  - LOC-SND-001
  - REL-007
---

# Home Island Audio Cue Packet

This packet defines first-pass music and sound direction for Home Island.

---

## Purpose

Home Island audio should establish warmth, memory, curiosity, and the first hints of old systems beneath the world.

---

## Location Music Direction

| Location | Music Direction | Hidden Texture |
|---|---|---|
| Ashford | Warm, simple, hummable town theme | Very subtle low pulse near old vents |
| Rustshore Docks | Light coastal melody, gentle waves | Occasional lighthouse tone |
| Fogfen Marsh | Misty, sparse, soft percussion | Faint ticking or distant hum |
| Glassfield Ruins | Quiet wonder, slow melody | Soft archive-like shimmer |
| Skyreach Hill | Airy, sacred, wind-forward | High harmonic authentication tone |
| Hidden Cave | Sparse cave ambience, minimal melody | Blue-white chime texture near sanctum |
| Sealed Node | Low pulse, cave-machine hybrid | Relay hum and warning tone |

---

## Required Sound Effects

| Cue ID | Event | Direction |
|---|---|---|
| SFX-HOM-001 | Warm-stone vent | Soft low breath / gentle heat |
| SFX-HOM-002 | Tremor event | Low rumble, short and non-destructive |
| SFX-HOM-003 | Sword authentication | Rising clear tone, crystalline but not magical-only |
| SFX-HOM-004 | Archive message | Soft static into chime |
| SFX-HOM-005 | Glassfield seal opens | Stone shift plus clean access tone |
| SFX-HOM-006 | Node Seven shutdown | Bass drop, silence, clean confirmation chime |
| SFX-HOM-007 | Lighthouse settles | Distant bell/light tone |

---

## Leitmotif Usage

### Kai Theme

Very subtle in Ashford and departure moments.

### Sword / Excalibur Motif

First appears during Sword authentication.

### Archive Motif

Use lightly during memory fragments and relay text.

### Restoration Motif

First clear use after Node Seven shutdown.

---

## Implementation Notes

Use RPG Maker MZ BGM/BGS/SE slots with placeholder assets until final audio exists.

Do not block implementation waiting for final music.

---

## Acceptance Criteria

- Each Home Island location has audio direction.
- Major story events have sound cue targets.
- Audio supports hidden technology subtly.
- Codex can use placeholders now and swap final assets later.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island audio cue packet |
