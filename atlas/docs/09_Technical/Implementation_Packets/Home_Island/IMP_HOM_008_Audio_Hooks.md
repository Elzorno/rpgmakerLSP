---
object_id: IMP-HOM-008
atlas_id: IMP-HOM-008
title: Build Home Island Audio Hooks
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - ATLAS-AUD-010
  requires:
    - ATLAS-AUD-001
    - IMP-HOM-002
---

# Implementation Packet: Build Home Island Audio Hooks

## Objective

Create the RPG Maker MZ audio hook plan for Home Island using placeholders first and final assets later.

---

## Atlas References

| ID | Reference |
|---|---|
| ATLAS-AUD-010 | Home Island Audio Cue Packet |
| ATLAS-AUD-001 | Audio Bible |
| IMP-HOM-002 | Journey I State System |

---

## Scope

Included:

- Location BGM/BGS placeholder assignments.
- Story event sound effect hooks.
- Suggested asset names.
- Acceptance criteria for audio review.

Out of scope:

- Final music composition.
- Final sound design.
- Voice acting.

---

## Suggested Asset Names

```text
BGM_AshfordTheme_v01.ogg
BGM_RustshoreDocks_v01.ogg
BGM_FogfenMarsh_v01.ogg
BGM_GlassfieldRuins_v01.ogg
BGM_SkyreachHill_v01.ogg
BGM_HiddenCave_v01.ogg
BGM_SealedNode_v01.ogg
SFX_SwordAuthentication_v01.ogg
SFX_ArchiveMessage_v01.ogg
SFX_GlassfieldSealOpen_v01.ogg
SFX_Node07Shutdown_v01.ogg
```

---

## Required Audio Hooks

| Event | Hook |
|---|---|
| Ashford map load | play Ashford BGM placeholder |
| Rustshore map load | play coastal BGM/BGS placeholder |
| Fogfen map load | play marsh BGM/BGS placeholder |
| Hidden Cave sanctum | reduce music / play ambience |
| Sword authentication | play SFX_SwordAuthentication |
| Archive message | play SFX_ArchiveMessage |
| Glassfield seal opens | play SFX_GlassfieldSealOpen |
| Node Seven shutdown | play SFX_Node07Shutdown |

---

## Acceptance Criteria

- Every Home Island major map has a placeholder audio assignment.
- Major story events have SE hooks even if using placeholder sounds.
- Audio does not block playtesting.
- Final asset replacement can happen by file name.

---

## Playtest Steps

1. Enter each Home Island location and confirm audio starts.
2. Trigger Sword authentication and confirm sound hook fires.
3. Trigger Glassfield seal and confirm sound hook fires.
4. Trigger Node Seven shutdown and confirm sound hook fires.
5. Confirm no event is silent due to missing file if placeholder exists.

---

## Open Questions

- Should Ashford use the same BGM before and after Node Seven?
- Should Sealed Node music stop fully at relay shutdown?
- Should archive messages use one universal sound effect?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island audio hook implementation packet |
