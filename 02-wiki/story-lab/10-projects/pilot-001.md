---
type: story_project
id: pilot-001
title_zh: AI+Story Pilot 001
title_en: AI+Story Pilot 001
status: active
project_id: pilot-001
canonical: true
created_at: 2026-06-25
updated_at: 2026-06-26
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
visual_styles:
  - vs-pilot-001-child-horror-notebook
related_packages:
  - iep-pilot-001-p01-fork-at-dusk
final_package_status: not-started
required_asset_count: 0
accepted_asset_count: 0
publishing_readiness_status: blocked
---

# AI+Story Pilot 001

## Visual Pipeline Status

**Visual pipeline reset completed (2026-06-26).** The old warm-safe visual system was removed from active use and the visual pipeline was rebuilt around a single clean child-drawn horror notebook style for GPTImage production.

- Current workflow: **clean GPTImage production handoff preparation.**
- Current active visual system: `vs-pilot-001-child-horror-notebook`.
- Current active recipe: `pr-pilot-001-child-horror-notebook` (active `recipe_hash` `267c7dfe258e43ba` — the only active recipe hash for `pilot-001`).
- Workflows A (Raw Intake), B (Story Analysis), C (Character & Scene Extraction) remain accepted; the story core, graph, characters, and scenes are unchanged.
- Packages: **Option B (clean restart)** was chosen — only `iep-pilot-001-p01-fork-at-dusk` exists, as a fresh `draft`. **p02-p14 packages were deleted and must be recreated later.**
- Failed earlier p01 output is **not accepted** and must **not** be used as a reference.
- **No image accepted. No ReferenceAsset exists. No GenerationRun exists.**
- WebGPTImage / GPTImage remains **manual**. Image generation remains **blocked** until the user manually uses the clean p01 GPTImage prompt.

### Style is reusable; story content is variable

The child-drawn horror notebook style controls drawing method and atmosphere only (lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen circles/arrows, childish handwriting when story-appropriate, uneven proportions, matte scanned paper, creepy-but-child-drawn, supernatural permission). It must not inject wardrobes, door gaps, eyes, ghosts, or any example motif unless the current package asks for them. For every image, the strange event, location, characters, props, and emotional beat come from the approved `ImageExecutionPackage` and the canonical cards it binds. Human identity locks are intact (Xiao He = human child, Mama = human adult, Lantern Grandpa = human elderly man, Tangerine = cat; human characters never animal/plush/doll/mascot substitutes).

### Removed History Summary

An earlier warm-safe night-picture-book VisualStyle and its prompt recipe were used during the original visual pipeline, produced a failed p01 manual attempt (over-safe / polished digital / animalized humans / no horror), and have been **removed**. Their cards, old recipe hashes, repair iterations, stale handoffs, and stale compile/lint records are no longer part of the active pipeline and must not be bound. No image was ever accepted; no ReferenceAsset or GenerationRun was ever created.


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

## Visual Style & Prompt Recipe

Visual pipeline reset 2026-06-26 - see [Visual Pipeline Status](#visual-pipeline-status). One clean active VisualStyle and one clean active PromptRecipe; the old warm-safe cards were removed.

Current (active) cards:

- VisualStyle: `vs-pilot-001-child-horror-notebook` - [Child-Drawn Horror Notebook Style](../50-visual-styles/vs-pilot-001-child-horror-notebook.md); `status: draft`. Drawing method and atmosphere only; motifs are examples, not requirements.
- PromptRecipe: `pr-pilot-001-child-horror-notebook` - [Child-Drawn Horror Notebook Prompt Recipe](../60-prompts/pr-pilot-001-child-horror-notebook.md); reusable, story-driven recipe only, not an execution prompt.
- recipe_hash: `267c7dfe258e43ba` (the only active recipe hash for `pilot-001`).
- Character `visual_style` references point to the active style; global warm-safe visual bans were removed/downgraded to story-layer role notes; human identity locks preserved.
- Scene cards: `linked_packages` reset to p01 only (other scenes cleared pending package re-creation).

Neither this card nor the active visual system authorizes image generation, prompt execution, GPTImage handoff execution, ReferenceAsset, or GenerationRun. Image generation stays manual and blocked until the user uses the clean p01 GPTImage prompt.

## Execution Packages

**Option B (clean restart)** chosen. Only one package exists:

- [p01 / The Fork at Dusk](../70-execution-packages/iep-pilot-001-p01-fork-at-dusk.md) - fresh `draft`, bound to the active style/recipe (`recipe_hash` `267c7dfe258e43ba`); not compiled, not linted, no handoff executed; image generation blocked.

p02-p14 packages were deleted in the reset and **must be recreated later** before the full 14-page story can proceed.

## Production Status

- Workflow B human approval gate: **ACCEPTED** (story core + page-count confirmed; 2026-06-25).
- Accepted story core (locked): Cluster 3 only; 14-page structure; rational-reassuring ending; child-safe mystery + safety lesson.
- Page count: 14 (within ~12-16 target).
- Dry-read safety check: PASS.
- Workflow C human approval gate: **ACCEPTED** (character + scene canon confirmed; 2026-06-25): 4 Character cards, 7 Scene cards, referential integrity, source-distance / child-safety.
- Visual pipeline reset (2026-06-26): old warm-safe VisualStyle + PromptRecipe removed; single clean child-horror-notebook style/recipe active (`recipe_hash` `267c7dfe258e43ba`); packages reset to a single fresh p01 draft (Option B).
- Current workflow: **clean GPTImage production handoff preparation.**
- Image pipeline remains blocked: no image generated, no GPTImage call, no ReferenceAsset, no GenerationRun. WebGPTImage / GPTImage stays manual.

## Blocked Actions

Workflows A, B, C are accepted. The visual pipeline was reset to a single clean child-horror-notebook style/recipe and a single fresh p01 draft package. The following remain blocked:

- Image generation (no image may be generated; GPTImage stays manual until the user uses the clean prompt)
- GPTImage handoff execution
- GenerationRun
- ReferenceAsset
- final package assembly
- publishing readiness
- re-creation + compile/lint of p02-p14 packages (required before the full story can proceed)


## Notes

This project begins from raw intake only. The raw source is not publishable text and must not be treated as final story prose.
