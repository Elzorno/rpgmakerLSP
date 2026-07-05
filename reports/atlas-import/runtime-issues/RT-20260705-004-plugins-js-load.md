# Runtime Issue RT-20260705-004

## Summary

RPG Maker reports that it is unable to read `plugins.js`.

## Checklist Reference

- Checklist file: `reports/atlas-import/build-0031-manual-runtime-playtest-checklist.md`
- Section: Runtime boot
- Step or row: Open/playtest the clean RPG Maker MZ project

## Environment

- RPG Maker MZ version:
- Platform: macOS
- Project path: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- Playtest date: 2026-07-05
- Tester: user

## Location

- File: `js/plugins.js`

## Expected

RPG Maker should read `js/plugins.js`, define `$plugins`, and continue booting the project.

## Actual

RPG Maker reports that it cannot read `plugins.js`.

## Reproduction Steps

1. Open `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/game.rmmzproject` in RPG Maker MZ.
2. Attempt to load or playtest the project.
3. Observe the `plugins.js` read failure.

## Evidence

- User report: "rpgmaker wont load. says unable to read plugins.js"

## Severity

Blocker: prevents project loading or playtest.

## Suspected Source

- Plugin/runtime behavior
- Generated clean skeleton file shape

## Resolution Notes

Fixed in BUILD-0040, pending user runtime confirmation.

- Normalized `js/plugins.js` to RPG Maker's generated multi-line format.
- Updated `tools/atlas-import/create_clean_skeleton.py` so future skeleton rebuilds use the same format.
- Verified `plugins.js` evaluates and defines `$plugins` as an array.
- Verified local HTTP fetch of `/js/plugins.js` returns `200`.
