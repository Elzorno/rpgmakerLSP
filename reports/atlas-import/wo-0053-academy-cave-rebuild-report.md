# Sealed Node Academy Cave Rebuild Candidate

> **Final visual verdict: REJECTED.** Live RPG Maker inspection showed that the MV sample tile IDs were not semantically compatible with the live project's tileset assignment. Under `SF Inside` they rendered as bright green terrain and unrelated furniture; under the project's `Dungeon` entry the assumed cave kinds rendered as lava and fence/railing. The candidate terrain was removed and the committed scaffold terrain restored. This report preserves the failed experiment as evidence, not as a current candidate certification.

Date: 2026-07-10

## Outcome

Maps009-012 were rebuilt as replacement candidates after the first WO-0053 terrain pass was rejected for lacking official RPG Maker sample quality. Live visual review rejected the replacements as well. The committed scaffold terrain is now restored; only the separately verified Guardian and Relay event-logic corrections remain.

## Academy Evidence

Atlas Academy directly inspected official sample Map051 Stone Cave, Map053 Cursed Cave, and Map074 Ancient Ruins. The filed study is `AtlasStudio/academy/case-studies/official-map-002-cave-corpus.md`.

The implementation applies learned principles without copying sample geometry: irregular silhouettes, passage-width variation, alternating compression and release, chamber-specific focal clusters, open circulation centers, edge-weighted decoration, and a visible natural-cave to old-world-machine progression.

## Replacement Candidate Metrics

| Map | Reachable floor | Event reachability | Upper-layer coverage |
|---|---:|---:|---:|
| Map009 Sealed Node Upper | 359/359 | all | 14.1% |
| Map010 Core Path | 461/461 | all | 13.7% |
| Map011 Guardian Chamber | 283/283 | all | 12.2% |
| Map012 Relay Core | 191/191 | all | 17.2% |

The coverage now reaches or exceeds the restrained official Stone Cave reference (12.8%). The denser Cursed Cave and Ancient Ruins references remain useful upper bounds, not automatic targets for these smaller maps.

## Preserved Functionality

- Existing events, transfers, Guardian battle logic, Relay shutdown logic, switches, and variables were preserved.
- Every floor tile is connected from the common transfer arrival coordinate.
- Every event is on or adjacent to reachable floor.
- Maps remain `hand_authored` and are explicitly marked `replacement_candidate_pending_human_review`.

## Validation

- Atlas validation: zero errors, zero warnings.
- Ownership audit: Maps009-012 protected from pipeline overwrite.
- Route audit: `found=228 missing=21 warning=9`, unchanged project-level baseline.
- JSON and diff validation passed.

## Acceptance Boundary

No Academy metric can approve these maps. They require direct visual inspection in RPG Maker and a human runtime playtest. If rejected again, record the specific visual defects by map and region so Academy can diagnose them rather than infer from a general quality verdict.
