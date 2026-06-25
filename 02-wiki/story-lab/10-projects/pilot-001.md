---
type: story_project
id: pilot-001
title_zh: AI+Story Pilot 001
title_en: AI+Story Pilot 001
status: active
project_id: pilot-001
canonical: true
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v0
tags:
  - story-lab
  - pilot
  - raw-intake
  - youtube-inspired
  - source-metadata-incomplete
related_assets: []
source_paths:
  - 01-raw/story-lab/user-inputs/pilot-001/
main_characters: []
worlds: []
visual_styles: []
related_packages: []
final_package_status: not-started
required_asset_count: 0
accepted_asset_count: 0
publishing_readiness_status: blocked
---

# AI+Story Pilot 001

## Workflow Status

Current workflow: C — Character & Scene Extraction  
Status: active (Workflow B story core accepted at human gate)  
Previous workflow: A — Raw Story Intake (accepted); B — Story Analysis (accepted)  
Next workflow: D — Visual Style & PromptRecipe (blocked until Workflow C human gate)  
Image generation: blocked  
WebGPTImage handoff: blocked  
ImageExecutionPackage creation: blocked  

## Source Paths

- `01-raw/story-lab/user-inputs/pilot-001/`

## Source Metadata Status

Incomplete.

Missing:

- YouTube URL
- YouTube title
- YouTube channel

Do not infer or fabricate missing source metadata.

## Raw Input Summary

The raw input is a user-provided YouTube transcript containing multiple oral-story materials.

The transcript is not a publishable story. It is stored only as provenance and inspiration source material.

## Copyright & Adaptation Boundary

Current policy:

- Treat source as third-party copyrighted material unless explicit license proof is provided.
- Use as inspiration only.
- Do not preserve original wording, names, title, sequence, unique twist, channel identity, narrator expression, forum framing, or recognizable source packaging.
- Downstream story must be reconstructed as an original, children-safe illustrated story core.

See:

- `01-raw/story-lab/user-inputs/pilot-001/source-metadata.md`
- `01-raw/story-lab/user-inputs/pilot-001/copyright-adaptation-boundary.md`
- `01-raw/story-lab/user-inputs/pilot-001/story-analysis-placeholder.md`

## Story Core

Workflow B selected source cluster: **Cluster 3 — night journey / getting lost** (inspiration-only; fully reconstructed, original, children-safe).

- Target: children-safe illustrated picture book, ages 5–8, ~12–16 pages (built: 14 pages).
- Premise: A young child and their grown-up, heading home as night falls, try an unfamiliar shortcut and get lost on a dark, quiet road. In the dark the child's imagination turns ordinary things into scary-seeming things. By staying together, staying calm, and asking a kind helper, they discover each scary thing has an ordinary explanation and find their way home.
- Core conflict: child's fear of the dark/unknown vs. the need to stay calm and find the way home.
- Theme: scary-seeming things usually have an ordinary explanation; staying together and asking for help is brave; safety rule — don't take unfamiliar shortcuts in the dark.
- Ending type: rational-reassuring (mystery explained by ordinary causes) + safety lesson.
- Allowed abstract themes used: night travel & getting lost; fear of the unknown; mistaken supernatural explanation; mystery later explained by ordinary causes; courage / asking for help / safety rules.

Originality & child-safety: no source names, places, wording, plot sequence, twist, or imagery; no drunk driving, Ghost-Festival framing, song/CD, scary face, death, crime, or supernatural payoff. Fear resolves into safety. Dry-read safety check: PASS.

## Story Graph (summary)

- 14 page-nodes; arc rises p1–5, turns at p6 (stay calm / ask for help), resolves p7–14.
- Clues → payoffs (all resolved): glowing "eyes" → helper's cat; "ghost" moan + pale shape → wind + mist; cold + thinning lamps → strayed into open country.
- analyze-graph verdict: hook OK; every page has a page-turn question; no dangling clues; no mid-sag; protagonist makes a choice (not only observes); child-safety risk LOW. repair_priority: low. next_action: proceed_to_human_gate.
- Full nodes/edges + diagnostics: derived record at `50-agent-work/story-lab/runs/pilot-001-workflow-b-story-analysis.md` (gitignored derived cache; not a source of truth).

## Production Status

- Workflow B human approval gate: **ACCEPTED** (story core + page-count confirmed; 2026-06-25).
- Accepted story core (locked): Cluster 3 only; 14-page structure; rational-reassuring ending; child-safe mystery + safety lesson.
- Page count: 14 (within ~12–16 target); long-story page-count review not triggered.
- Dry-read safety check: PASS.
- Current: Workflow C — character & scene extraction (stops at the Workflow C human gate). Workflow D (visual/technique) and the image pipeline remain blocked.

## Blocked Actions

The following actions remain blocked until the Workflow B story-core gate is human-accepted and the later C/D human gates approve them:

- Character card creation
- Scene card creation
- VisualStyle creation
- PromptRecipe creation
- ImageExecutionPackage creation
- WebGPTImage prompt writing
- Image generation
- Final package assembly
- Publishing readiness

## Notes

This project begins from raw intake only. The raw source is not publishable text and must not be treated as final story prose.
