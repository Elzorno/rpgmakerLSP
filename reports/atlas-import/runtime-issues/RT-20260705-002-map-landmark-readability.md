# Runtime Issue RT-20260705-002

## Summary

Maps are structurally present but lack enough landmarks for player orientation.

## Checklist Reference

- Checklist file: `reports/atlas-import/build-0031-manual-runtime-playtest-checklist.md`
- Section: Route readability
- Step or row: Traverse Home Island route

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

Each map should include enough placeholder landmarks, route cues, or object placement to let a player infer the intended next action.

## Actual

Maps are incomplete and lack landmarks, so the player cannot reliably determine what to do.

## Reproduction Steps

1. Start a playtest from the generated clean skeleton project.
2. Move through the available Home Island maps.
3. Attempt to infer the intended next action from visible map content.
4. Observe missing landmark and route guidance.

## Evidence

- Screenshot:
- Short video:
- Console error:
- Save file:
- User report: "the maps are not complete so there is no landmarks to help determine what to do"

## Severity

Medium: confusing behavior with workaround.

## Suspected Source

- Blueprint/layout generation
- Atlas spec gap

## Resolution Notes

Open. Preferred next fix after text/collision is a placeholder landmark and route-readability pass grounded in Atlas screen objects.
