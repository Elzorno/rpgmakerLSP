# Runtime Issue RT-20260705-001

## Summary

Events display text IDs instead of readable runtime event text.

## Checklist Reference

- Checklist file: `reports/atlas-import/build-0031-manual-runtime-playtest-checklist.md`
- Section: Event interaction smoke test
- Step or row: Interact with generated placeholder events

## Environment

- RPG Maker MZ version:
- Platform:
- Project path: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- Playtest date: 2026-07-05
- Tester: user

## Location

- Map ID: Multiple
- Map display name: Multiple Home Island maps
- Event name: Multiple generated events
- Player coordinate:
- Event coordinate:

## Expected

Runtime events should show readable placeholder text or implemented event content while preserving Atlas traceability.

## Actual

Runtime events trigger a text ID instead of readable event text.

## Reproduction Steps

1. Start a playtest from the generated clean skeleton project.
2. Move to any nearby generated interaction event.
3. Interact with the event.
4. Observe that the message text is an ID-like placeholder rather than readable copy.

## Evidence

- Screenshot:
- Short video:
- Console error:
- Save file:
- User report: "events trigger a text ID instead of the actual event"

## Severity

High: breaks required route, reward, or story-gate comprehension.

## Suspected Source

- RPG Maker event command
- Atlas spec gap

## Resolution Notes

Fixed in BUILD-0037, pending user runtime confirmation.

- Added `tools/atlas-import/apply_readable_placeholder_text.py`.
- Replaced 55 runtime-visible `PH-*` Show Text lines across 17 RPG Maker data files with readable placeholder copy.
- Preserved placeholder status and avoided final dialogue/lore writing.
