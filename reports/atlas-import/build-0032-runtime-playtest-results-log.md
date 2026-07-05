# BUILD-0032 - Runtime Playtest Results Log

This log records results from executing `build-0031-manual-runtime-playtest-checklist.md`.

## Current Status

Run in progress. First user playtest pass completed after BUILD-0035.

## Test Session

- RPG Maker MZ version:
- Platform:
- Project path: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- Tester: user
- Date: 2026-07-05
- Build/commit references:
  - `rpgmakerLSP` commit `1f68e4e` (`build: fix clean skeleton plugins global`)
  - `TheLastSwordProtocol-Game` commit `bcbc718` (`fix: define RPG Maker plugin list global`)
  - `TheLastSwordProtocol-Atlas` commit `7a3a1bb` (`feat(atlas): add Ashford Shop map blueprint`)

## Summary

| Result | Count |
|---|---:|
| Passed | 2 |
| Failed | 3 |
| Blocked | 0 |
| Not Run | 0 |

## Issues

| Issue ID | Severity | Checklist Reference | Summary | Status |
|---|---|---|---|---|
| RT-20260705-001 | High | Runtime event interaction | Events show text IDs instead of readable runtime event text. | Fixed in BUILD-0037; needs runtime confirmation |
| RT-20260705-002 | Medium | Map readability / player guidance | Maps lack landmarks, so the player cannot reliably infer what to do. | Fixed in BUILD-0039; needs runtime confirmation |
| RT-20260705-003 | High | Collision / passability | Collision is inconsistent; some blocks are passable and others are not. | Fixed in BUILD-0038; needs runtime confirmation |
| RT-20260705-004 | Blocker | Project boot | RPG Maker reports unable to read `plugins.js`. | Fixed in BUILD-0040; needs runtime confirmation |

## Passing Findings

- Player movement works.
- No new runtime errors appeared after the BUILD-0035 `$plugins` fix.

## Final Decision

NO GO.

The build now boots and accepts player movement. BUILD-0037 removes visible placeholder text IDs, BUILD-0038 removes passable upper-layer tiles over blocked terrain, and BUILD-0039 assigns visible placeholder graphics to all generated Home Island event pages.

GO WITH FIXES.

No known data-level blocker remains from the first user runtime report or the later `plugins.js` load report, but the fixes need runtime confirmation in RPG Maker MZ before the first journey can be called playtest-certified.

Use one of:

- GO: no blockers; continue to next implementation stage.
- GO WITH FIXES: issues exist but do not block next stage.
- NO GO: one or more blockers must be fixed before proceeding.
