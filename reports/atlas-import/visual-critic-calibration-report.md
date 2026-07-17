# Visual Critic Calibration Report (WO-0075)

Date: 2026-07-16
Module: `AtlasStudio/atlas-tools/mapgen/compiler/visual_critic.py`
Command: `python3 atlas-tools/mapgen/compiler/visual_critic.py --calibrate`

## What this is

The automated visual critic (WO-0075) scores a rendered map against the
Academy's Dragon Quest town-grammar checklist and the classic-JRPG Review
Gate, automating the ten `AVCP-HOM-ASH-001` aesthetic constraints that
`quality_gate.py` had parked in `NOT_YET_AUTOMATABLE` (first-camera salience,
path rhythm/bends, decoration density, colour/material identity, limited
vocabulary). This report is the **go/no-go calibration**: before the critic is
allowed to gate anything, a backend must reproduce the pass/pass/reject
discrimination on three renders whose human verdicts are already known.

## Method

- **Reference-anchored.** Each candidate render is judged alongside the two
  accepted maps as the "hand-crafted" bar, not scored in isolation.
- **Rubric.** 12 criteria (7 core, 5 soft). A single **core** fail rejects; a
  soft fail or an accumulation of partials flags; otherwise pass. The critic
  never emits "accept" — a clean map is only ever a candidate for Chris's
  decision, preserving WO-0072's "recommends, never accepts" rule.
- **Backend for this run:** `recorded` — the genuine per-criterion judgements
  formed by the **Claude/Opus (claude-opus-4-8) frontier VLM viewing the three
  renders during the WO-0075 agent session**, recorded verbatim in
  `visual_critic.py::session_frontier_critiques` and replayed reproducibly.
  Provenance is the frontier VLM via the agent session, **not** a live API
  call.

## Result

```
label                expected   actual   ok   note
map017               pass       pass     Y
map001               pass       pass     Y
wo0073_candidate     reject     reject   Y    cited required core failures:
                                              ENCLOSURE-001, MATERIAL-IDENTITY-001, PATH-ORGANIC-001
CALIBRATION: PASS   (covers AVCP ASH-BUILD-002, ASH-DENSITY-001, ASH-FIRST-001,
                     ASH-FIRST-002, ASH-MATERIAL-001, ASH-MATERIAL-002,
                     ASH-PATH-002, ASH-PATH-003, ASH-RHYTHM-001, ASH-VOCAB-001)
```

The set of AVCP ids the critic covers equals `quality_gate.NOT_YET_AUTOMATABLE`
exactly (asserted in `tests/test_visual_critic.py`).

### Per-render summary

- **Map017** (`academy-inspection-002-map017-render.png`, the accepted 8/8
  calibration map): 12/12 pass. Enclosure via river + tree-line; winding
  branching paths; bridge-to-plaza compression/release; a dominant statue
  landmark; varied timber buildings; dense scattered decoration.
- **Map001** (`wo-0036-map001-render.png`, accepted production Ashford):
  overall pass, with two honest partials (path rhythm softer than Map017's
  around the large central paved area; a well but no open-water landmark). The
  partials show the rubric has resolution — it does not blanket-pass an
  accepted map.
- **WO-0073 candidate** (`ashford-mapvision-v3/ashford-mapvision-candidate-render.png`,
  human-rejected as "mechanical"): overall **reject**, with 9 core/soft fails.
  It fails, in its own words, on no perimeter (open field), a rigid plus-shaped
  path that dead-ends at walls not doors, four identical brown shells, a single
  material over flat green, near-empty decoration, and no dominant landmark —
  the exact reasons Chris gave. The lone non-fail is VOCAB-LIMITED (its palette
  is limited, arguably *too* limited).

## Scope of trust (read this before relying on it)

- **What is validated:** the **rubric discriminates** correctly when driven by
  a capable frontier VLM. The critic, in frontier/agent-driven mode, correctly
  rejects the mechanical map for the right reasons and passes the two accepted
  maps. This closes the WO-0072 feedback gap in which three candidates passed
  every automated gate and still reached Chris.
- **What is NOT yet validated:** an **unattended local** backend. The
  `OllamaVisionBackend` is built and unit-tested (prompt build + JSON parse),
  but this environment has **no vision model pulled** (only text models:
  mistral, deepseek-r1, qwen-coder, qwen3.5, gemma4), and **no `ANTHROPIC_API_KEY`**
  is set, so no live model was called. The calibration therefore does not claim
  the critic runs itself yet.
- The critic is a **pre-screen**, not an approver. `apply_human_decision`
  (Chris only) remains the sole path to acceptance.

## To make it unattended (next step, not done here)

1. Pull a vision model: `ollama pull llama3.2-vision` (≈8 GB) or `llava`.
2. Re-run against the same fixed set: `visual_critic.py --calibrate --backend ollama --model llama3.2-vision`.
3. If it reproduces pass/pass/reject **with** the three cited core failures on
   WO-0073, wire it as the unattended default; otherwise keep it untrusted and
   use `--backend anthropic` (needs a key) as the frontier escalation path. A
   small local model may well fail this — the calibration exists precisely to
   catch that before it gates.

## Local-backend attempt — 2026-07-16 follow-up (result: FAIL, stays untrusted)

Both candidate vision models were pulled and calibrated. **Neither qualifies as
the unattended-local backend.** The calibration harness caught this exactly as
designed — no untrustworthy backend was wired into the gate.

- **`llama3.2-vision`** — cannot run on this host. Ollama 0.32.0's llama-server
  rejects the model at load: `unknown model architecture: 'mllama'` (HTTP 500 on
  every request). The runtime is too old for Llama-3.2-Vision's `mllama`
  architecture; the model would need a newer Ollama build. Not attempted further.
- **`llava`** — loads and genuinely sees the renders, but **FAILS calibration**:
  `visual_critic.py --calibrate --backend ollama --model llava` returns
  reject / reject / reject (expected pass / pass / reject). Failure mode is
  non-discrimination: llava emits near-identical per-criterion critiques across
  all three maps (same "settlement enclosed by a wall" pass, same path
  partials/fails) essentially independent of image content — it even
  hallucinates a perimeter wall on the WO-0073 candidate, which is an open field
  with no enclosure. It also returns no AVCP criterion ids, so on WO-0073 it
  "did not cite required core failures (ENCLOSURE-001, PATH-ORGANIC-001)" even
  though it nominally rejected. Evidence:
  `visual-critic-calibration/ollama-llava/*.json`.

**Standing conclusion:** the critic remains trusted **only** in frontier /
agent-driven mode (the `recorded` frontier-VLM run above). Unattended-local
automation is still unproven and must not gate. Paths forward, in order of
effort: (a) set `ANTHROPIC_API_KEY` and use `--backend anthropic`
(claude-opus-4-8) as the frontier escalation — known-good rubric, just a live
API call instead of the recorded replay; (b) upgrade Ollama and retry
`llama3.2-vision`; (c) try a stronger local VLM (e.g. a Qwen2.5-VL / larger
llava variant) and re-calibrate. Until one of these passes the three-render
go/no-go, the recorded frontier critique is the only trusted source.

## Evidence files

- `visual-critic-calibration/visual-critic-map017.json`
- `visual-critic-calibration/visual-critic-map001.json`
- `visual-critic-calibration/visual-critic-wo0073_candidate.json`

Each is the full per-criterion critique (verdict + falsifiable reason + AVCP
refs) for one render, persisted in the same JSON-evidence convention as the
gate's `*.gate_evidence.json`.
