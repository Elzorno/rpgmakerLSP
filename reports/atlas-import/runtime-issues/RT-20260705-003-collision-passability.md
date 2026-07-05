# Runtime Issue RT-20260705-003

## Summary

Collision and passability are inconsistent across generated map blocks.

## Checklist Reference

- Checklist file: `reports/atlas-import/build-0031-manual-runtime-playtest-checklist.md`
- Section: Movement and collision smoke test
- Step or row: Walk against blocked and traversable tiles

## Environment

- RPG Maker MZ version:
- Platform:
- Project path: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- Playtest date: 2026-07-05
- Tester: user

## Location

- Map ID: Multiple
- Map display name: Multiple Home Island maps
- Event name:
- Player coordinate:
- Event coordinate:

## Expected

Tiles used as blocking geometry should consistently block movement, while path and floor tiles should consistently allow movement.

## Actual

Collision is off. Some blocks are passable and others are not.

## Reproduction Steps

1. Start a playtest from the generated clean skeleton project.
2. Move into visible obstacle/block tiles on generated maps.
3. Compare passability behavior between similar-looking blocks.
4. Observe inconsistent collision.

## Evidence

- Screenshot:
- Short video:
- Console error:
- Save file:
- User report: "collision is off. Some blocks are passable and others are not."

## Severity

High: breaks map trust and can invalidate routes or barriers.

## Suspected Source

- Collision/passability
- Blueprint/layout generation
- RPG Maker tileset configuration

## Resolution Notes

Fixed in BUILD-0038, pending user runtime confirmation.

- Added `tools/atlas-import/apply_collision_passability_cleanup.py`.
- Updated map layout and blueprint map generators to clear upper-layer tiles above blocked base terrain.
- Applied the cleanup to the clean game project; 490 upper-layer tiles were cleared across 10 maps.
- Verified zero blocked base cells still have upper-layer tiles on Home Island maps 1-16.
