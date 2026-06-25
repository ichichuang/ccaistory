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
main_characters:
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
  - char-juzi-cat
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

## Characters

Workflow C extracted 4 canonical Character cards (`30-characters/`):

- [小禾 / Xiao He](../30-characters/char-xiaohe.md) — protagonist (the child).
- [妈妈 / Mama](../30-characters/char-mama.md) — caregiver / travel companion.
- [守灯爷爷 / Lantern Grandpa](../30-characters/char-lantern-grandpa.md) — the safe helper at the cottage.
- [橘子 / Tangerine the Cat](../30-characters/char-juzi-cat.md) — the cat; the ordinary cause of the "glowing eyes".

## Scenes

Workflow C extracted 7 canonical Scene cards (`40-scenes/`) covering the 14-page graph:

- [黄昏岔路口 / The Fork at Dusk](../40-scenes/scene-fork-at-dusk.md) — p1.
- [灯火渐稀的小路 / The Fading-Lamp Lane](../40-scenes/scene-fading-lamp-lane.md) — p2.
- [黑黑的林间小路 / The Dark Wooded Lane](../40-scenes/scene-dark-wooded-lane.md) — p3–p6 (scares + calming turn).
- [守灯小屋 / The Lantern Cottage](../40-scenes/scene-lantern-cottage.md) — p7–p11 (rescue + ordinary-cause payoffs).
- [回到亮亮的大路 / Back to the Bright Road](../40-scenes/scene-return-to-bright-road.md) — p12.
- [家门口 / The Home Doorway](../40-scenes/scene-home-doorway.md) — p13.
- [窗边的晚安 / Goodnight at the Window](../40-scenes/scene-bedroom-window.md) — p14.

## Production Status

- Workflow B human approval gate: **ACCEPTED** (story core + page-count confirmed; 2026-06-25).
- Accepted story core (locked): Cluster 3 only; 14-page structure; rational-reassuring ending; child-safe mystery + safety lesson.
- Page count: 14 (within ~12–16 target); long-story page-count review not triggered.
- Dry-read safety check: PASS.
- Current: Workflow C — character & scene extraction **COMPLETE; awaiting Workflow C human gate** (canon sign-off). Extracted 4 Character cards + 7 Scene cards. Workflow D (visual/technique) and the image pipeline remain blocked.

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
