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
deprecated_visual_styles:
  - vs-pilot-001-warm-safe-night-picturebook
related_packages:
  - iep-pilot-001-p01-fork-at-dusk
  - iep-pilot-001-p02-fading-lamp-lane
  - iep-pilot-001-p03-dark-wooded-lane-cold-trees
  - iep-pilot-001-p04-dark-wooded-lane-glowing-dots
  - iep-pilot-001-p05-dark-wooded-lane-mist-and-moan
  - iep-pilot-001-p06-dark-wooded-lane-steady-breath
  - iep-pilot-001-p07-lantern-cottage-warm-light
  - iep-pilot-001-p08-lantern-cottage-welcome
  - iep-pilot-001-p09-lantern-cottage-cat-eyes
  - iep-pilot-001-p10-lantern-cottage-wind-and-mist
  - iep-pilot-001-p11-lantern-cottage-open-country
  - iep-pilot-001-p12-return-to-bright-road
  - iep-pilot-001-p13-home-doorway
  - iep-pilot-001-p14-bedroom-window-goodnight
final_package_status: not-started
required_asset_count: 0
accepted_asset_count: 0
publishing_readiness_status: blocked
---

# AI+Story Pilot 001

## Workflow Status

- Current workflow: **D/F/G repair loop (visual-system refactor)** — rolled back from G.
- Status: the base visual system was refactored from warm-safe picture book to **child-drawn horror notebook**. p01 routed to `repair_02`; p02–p14 re-pointed and downgraded out of `ready`. Awaiting the **repair human gate**.
- Previous workflow: A — Raw Story Intake (accepted); B — Story Analysis (accepted); C — Character & Scene Extraction (accepted); D — Visual Style & PromptRecipe (**previously accepted; that visual-layer acceptance is now superseded by the refactor**).
- Workflow G p01 attempt: **failed** (over-safe / polished digital / animalized humans / no horror).
- Image accepted: **no**.
- ReferenceAsset: **none** (still empty).
- Image generation: **blocked** — stop at the repair human gate; do not generate images, call WebGPTImage, or create ReferenceAsset/GenerationRun.
- WebGPTImage handoff: p01 `repair_02` handoff prepared (gated, not executed); p02–p14 remain blocked.
- ImageExecutionPackage status: p01 = `ready` (repair_02 compile/lint pass, handoff pending the gate); p02–p14 = `draft` (stale under the new recipe; not auto-released).

## Visual System Refactor (2026-06-26)

This project underwent a **visual-system refactor**. The original warm-safe-night picture-book visual system failed in practice and biased generation away from the intended aesthetic.

- Old style failure reasons: **over-safe / polished digital / animalized humans / no horror**. The "warm-safe-night" framing and global "no horror / no supernatural / low fear" rules pushed output toward cute commercial-picture-book / fairy-tale-animal imagery.
- Root cause: **base visual system mismatch** — the VisualStyle and PromptRecipe themselves were wrong, not just a per-image prompt.
- Action: replaced the base visual system with a **child-drawn horror notebook** system that allows supernatural/unexplained content while keeping human-only characters and hard content-safety lines.

| Item | State |
|---|---|
| Workflow G p01 attempt | failed |
| Workflow D/F/G repair loop | required (in progress) |
| Reason | base visual system mismatch |
| Image accepted | no |
| ReferenceAsset | no |
| Next | visual system refactor → repair human gate → p01 repair_02 |

New (current) cards — pending the repair human gate (not yet re-accepted):

- VisualStyle: `vs-pilot-001-child-horror-notebook` (儿童手绘怪谈作业本风格)
- PromptRecipe: `pr-pilot-001-child-horror-notebook` (儿童手绘怪谈作业本提示词配方); recipe_hash `58802ab763ac5dc6`

Deprecated cards (history only; do not bind):

- `vs-pilot-001-warm-safe-night-picturebook` → `status: deprecated`
- `pr-pilot-001-safe-night-picturebook` → `status: deprecated`

Scope honored by this refactor: only the underlying VisualStyle / PromptRecipe / Package / Handoff were repaired. No image was generated, no WebGPTImage call was made, no ReferenceAsset or GenerationRun was created, and no final package was assembled. p01 story direction is unchanged (re-skin only).

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

**Refactored 2026-06-26 (see [Visual System Refactor](#visual-system-refactor-2026-06-26)).** The visual layer was rebuilt; the prior Workflow D acceptance of the warm-safe cards is superseded. The new cards retain `status: draft` (their schemas define no `accepted`/`active`) and are **pending the repair human gate** — not yet re-accepted.

Current (bound) cards:

- VisualStyle: `vs-pilot-001-child-horror-notebook`
- PromptRecipe: `pr-pilot-001-child-horror-notebook`
- recipe_hash: `58802ab763ac5dc6`
- Character `visual_style` references re-pointed to the new style
- Scene cards unchanged
- p01 re-pointed and recompiled as `repair_02`; p02–p14 re-pointed and downgraded out of `ready` (stale; not auto-released)

- [pilot-001 儿童手绘怪谈作业本风格 / Child-Drawn Horror Notebook Style](../50-visual-styles/vs-pilot-001-child-horror-notebook.md) — current; `status: draft`, pending the repair human gate.
- [pilot-001 儿童手绘怪谈作业本提示词配方 / Child-Drawn Horror Notebook Prompt Recipe](../60-prompts/pr-pilot-001-child-horror-notebook.md) — current; reusable recipe only, not an execution prompt.

Deprecated cards (history only; `status: deprecated`; do not bind):

- [pilot-001 温暖安全夜路图文书风格 / Warm Safe Night Picture Book Style](../50-visual-styles/vs-pilot-001-warm-safe-night-picturebook.md) — superseded; old hash `62b75f8590685a10` / `6020fc5e5c83e043` historical.
- [pilot-001 儿童安全夜路图文书提示词配方 / Child-Safe Night Picture Book Prompt Recipe](../60-prompts/pr-pilot-001-safe-night-picturebook.md) — superseded.

Neither the prior Workflow D acceptance nor this refactor authorizes image generation, prompt execution, WebGPTImage handoff, ReferenceAsset, or GenerationRun. The refactor stops at the repair human gate.

### Historical Workflow D/E/F/G (superseded for the visual layer)

The records below describe the original warm-safe pipeline and are kept for history. The visual-style/recipe bindings and `recipe_hash` values in them are now superseded by the refactor above.

Workflow E draft package creation was started on 2026-06-26 by explicit human instruction. Workflow E created the package plan only; it did not authorize WebGPTImage handoff, image generation, GenerationRun, ReferenceAsset, final package assembly, or publishing readiness.

Workflow E human gate accepted the draft package plan on 2026-06-26:

- Workflow E human gate: ACCEPTED for draft package plan.
- 14 ImageExecutionPackage draft cards accepted.
- p01–p14 coverage verified.
- All packages bind `vs-pilot-001-warm-safe-night-picturebook`.
- All packages bind `pr-pilot-001-safe-night-picturebook`.
- recipe_hash verified: `6020fc5e5c83e043`.
- Scene `linked_packages` verified.
- Package status remains `draft`.
- F/G/image generation remain blocked.

Workflow F human/QA gate accepted prompt compile and semantic lint on 2026-06-26:

- Workflow F human/QA gate: ACCEPTED (prompt compile + semantic lint passed; 2026-06-26).
- 14 ImageExecutionPackage cards compile pass.
- 14 ImageExecutionPackage cards semantic lint pass.
- 14 ImageExecutionPackage cards ready.
- recipe_hash verified for all packages: `6020fc5e5c83e043`.
- compiled prompt records created under `50-agent-work/story-lab/compiled-prompts/` (gitignored derived records).
- semantic lint records created under `50-agent-work/story-lab/semantic-lint-results/` (gitignored derived records).
- At Workflow F acceptance time, WebGPTImage handoff and image generation remained blocked.
- Current update: Workflow G has now created a p01-only manual handoff; image generation remains blocked until human execution evidence exists.

Workflow G manual handoff started on 2026-06-26 for p01 only:

- Workflow G status: STARTED for `iep-pilot-001-p01-fork-at-dusk` only.
- Controlled manual handoff record: `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/iep-pilot-001-p01-fork-at-dusk.md`.
- Compiled prompt source: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p01-fork-at-dusk.json`.
- Semantic lint source: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p01-fork-at-dusk.json`.
- WebGPTImage remains manual; no runtime or agent image generation occurred.
- No GenerationRun, ReferenceAsset, final package, or publishing record was created.
- p02–p14 remain blocked for Workflow G.

Execution packages (current status: p01 = `ready` repair_02 handoff pending the gate; p02–p14 = `draft`, stale under the new recipe, not auto-released):

- [p01 / The Fork at Dusk](../70-execution-packages/iep-pilot-001-p01-fork-at-dusk.md)
- [p02 / The Fading-Lamp Lane](../70-execution-packages/iep-pilot-001-p02-fading-lamp-lane.md)
- [p03 / The Dark Wooded Lane — Cold Trees](../70-execution-packages/iep-pilot-001-p03-dark-wooded-lane-cold-trees.md)
- [p04 / The Dark Wooded Lane — Glowing Dots](../70-execution-packages/iep-pilot-001-p04-dark-wooded-lane-glowing-dots.md)
- [p05 / The Dark Wooded Lane — Mist and Moan](../70-execution-packages/iep-pilot-001-p05-dark-wooded-lane-mist-and-moan.md)
- [p06 / The Dark Wooded Lane — Steady Breath](../70-execution-packages/iep-pilot-001-p06-dark-wooded-lane-steady-breath.md)
- [p07 / The Lantern Cottage — Warm Light](../70-execution-packages/iep-pilot-001-p07-lantern-cottage-warm-light.md)
- [p08 / The Lantern Cottage — Welcome](../70-execution-packages/iep-pilot-001-p08-lantern-cottage-welcome.md)
- [p09 / The Lantern Cottage — Cat Eyes](../70-execution-packages/iep-pilot-001-p09-lantern-cottage-cat-eyes.md)
- [p10 / The Lantern Cottage — Wind and Mist](../70-execution-packages/iep-pilot-001-p10-lantern-cottage-wind-and-mist.md)
- [p11 / The Lantern Cottage — Open Country](../70-execution-packages/iep-pilot-001-p11-lantern-cottage-open-country.md)
- [p12 / Back to the Bright Road](../70-execution-packages/iep-pilot-001-p12-return-to-bright-road.md)
- [p13 / The Home Doorway](../70-execution-packages/iep-pilot-001-p13-home-doorway.md)
- [p14 / Goodnight at the Window](../70-execution-packages/iep-pilot-001-p14-bedroom-window-goodnight.md)

## Production Status

> Visual layer refactored 2026-06-26 — see [Visual System Refactor](#visual-system-refactor-2026-06-26). The Workflow D/E/F acceptance bullets below are historical: their `vs-pilot-001-warm-safe-night-picturebook` / `pr-pilot-001-safe-night-picturebook` bindings and `6020fc5e5c83e043` hash are superseded by `vs-pilot-001-child-horror-notebook` / `pr-pilot-001-child-horror-notebook` (recipe_hash `58802ab763ac5dc6`). Packages are no longer all `ready` — p01 is `ready` (repair_02, gated) and p02–p14 are `draft` (stale, not auto-released).

- Workflow B human approval gate: **ACCEPTED** (story core + page-count confirmed; 2026-06-25).
- Accepted story core (locked): Cluster 3 only; 14-page structure; rational-reassuring ending; child-safe mystery + safety lesson.
- Page count: 14 (within ~12–16 target); long-story page-count review not triggered.
- Dry-read safety check: PASS.
- Workflow C human approval gate: **ACCEPTED** (character + scene canon confirmed; 2026-06-25).
  - 4 Character cards accepted
  - 7 Scene cards accepted
  - Referential integrity accepted
  - Source-distance / child-safety accepted
- Workflow D human approval gate: ACCEPTED (visual style + prompt recipe confirmed; 2026-06-26).
  - VisualStyle accepted: `vs-pilot-001-warm-safe-night-picturebook`
  - PromptRecipe accepted: `pr-pilot-001-safe-night-picturebook`
  - recipe_hash verified: `6020fc5e5c83e043`
  - Character visual_style references verified
  - Scene cards unchanged
  - source-distance / child-safety accepted
- Workflow E human approval gate: ACCEPTED (draft package plan confirmed; 2026-06-26).
  - 14 ImageExecutionPackage draft cards accepted
  - p01–p14 coverage verified
  - all packages bind `vs-pilot-001-warm-safe-night-picturebook`
  - all packages bind `pr-pilot-001-safe-night-picturebook`
  - recipe_hash verified: `6020fc5e5c83e043`
  - Scene `linked_packages` verified
  - package status advanced through Workflow F to `ready`
  - G/image generation remain blocked
- Workflow F human/QA gate: ACCEPTED (prompt compile + semantic lint passed; 2026-06-26).
  - 14 ImageExecutionPackage cards compile pass
  - 14 ImageExecutionPackage cards semantic lint pass
  - 14 ImageExecutionPackage cards ready
  - recipe_hash verified for all packages: `6020fc5e5c83e043`
  - compiled prompt records created under `50-agent-work/story-lab/compiled-prompts/` (gitignored derived records)
  - semantic lint records created under `50-agent-work/story-lab/semantic-lint-results/` (gitignored derived records)
  - At Workflow F acceptance time, WebGPTImage handoff and image generation remained blocked
  - Current update: p01-only Workflow G handoff created; image generation remains blocked until human execution evidence exists
- Visual-system refactor (2026-06-26): the warm-safe visual layer was deprecated and replaced; the prior Workflow D acceptance is superseded for the visual layer.
- Current workflow: **D/F/G repair loop** — rolled back from G; awaiting the repair human gate.
- Status: p01 re-pointed + recompiled as `repair_02` (gated handoff prepared, not executed); p02–p14 re-pointed and downgraded out of `ready`.
- Image pipeline remains blocked: no image generated, no WebGPTImage call, no ReferenceAsset, no GenerationRun.

## Blocked Actions

Workflows A, B, C are accepted. The Workflow D visual layer was **refactored** (warm-safe cards deprecated; new child-horror-notebook cards pending the repair human gate). p01 is routed to `repair_02`; p02–p14 are downgraded out of `ready` and not auto-released. The following remain blocked until the repair human gate and later human/QA gates are approved:

- The repair human gate for the new visual system (must approve before any p01 `repair_02` generation)
- WebGPTImage handoff execution for p01 (gated) and all of p02–p14
- Image generation (no image may be generated by this refactor)
- GenerationRun
- ReferenceAsset
- final package assembly
- publishing readiness
- recompile / relint of p02–p14 under the new recipe (required before they can return to `ready`)

## Notes

This project begins from raw intake only. The raw source is not publishable text and must not be treated as final story prose.
