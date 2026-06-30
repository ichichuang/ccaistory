---
type: story_project
id: pilot-001
title_zh: AI+Story Pilot 001
title_en: AI+Story Pilot 001
status: active
project_id: pilot-001
canonical: true
created_at: 2026-06-25
updated_at: 2026-06-30
owner: ichichuang
version: v0
tags:
  - story-lab
  - pilot
  - raw-intake
  - youtube-inspired
  - source-metadata-incomplete
related_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p02-fading-lamp-lane
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
  - iep-pilot-001-p02-fading-lamp-lane
  - iep-pilot-001-p03-dark-wooded-lane
final_package_status: not-started
required_asset_count: 0
accepted_asset_count: 2
publishing_readiness_status: blocked
---

# AI+Story Pilot 001

## Visual Pipeline Status

**Visual pipeline reset completed (2026-06-26).** The old warm-safe visual system was removed from active use and the visual pipeline was rebuilt around a single clean child-drawn horror notebook style for GPTImage production.

- Current workflow: **p03 GPTImage handoff prepared for human operation only. p01 R00 remains the only series master visual anchor, p02 is the previous-page scene continuity reference, and p03 generation remains blocked pending separately authorized human execution.**
- Current active visual system: `vs-pilot-001-child-horror-notebook`.
- Current active recipe: `pr-pilot-001-child-horror-notebook` (active `recipe_hash` `267c7dfe258e43ba` — the only active recipe hash for `pilot-001`).
- Workflows A (Raw Intake), B (Story Analysis), C (Character & Scene Extraction) remain accepted; the story core, graph, characters, and scenes are unchanged.
- Packages: **Option B (clean restart)** was chosen. `iep-pilot-001-p01-fork-at-dusk`, `iep-pilot-001-p02-fading-lamp-lane`, and draft `iep-pilot-001-p03-dark-wooded-lane` now exist. **p04-p14 packages remain deleted and must be recreated later, one at a time.**
- Failed earlier p01 output is **not accepted** and must **not** be used as a reference.
- **ReferenceAssets exist:** `ra-pilot-001-r00-master-style-character-anchor` and `ra-pilot-001-p02-fading-lamp-lane`.
- Workflow H for p01 is **started/completed**: one manual WebGPTImage / GPTImage candidate exists, with GenerationRun `gr-pilot-001-p01-20260626-172625-webgptimage`.
- Candidate image: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png`.
- Workflow I QA is **passed**. Workflow J accepted the candidate as `ra-pilot-001-r00-master-style-character-anchor`.
- WebGPTImage / GPTImage remains **manual**. No automated generation is authorized.
- Serialized production: **p01 is the designated series master anchor**. The accepted ReferenceAsset `ra-pilot-001-r00-master-style-character-anchor` is now the active R00 / series master visual reference for p02-p14. See [Series Continuity & Master Anchor](#series-continuity--master-anchor-serialized-production).
- Workflow H for p02 repair candidate is **backfilled**: one manual WebGPTImage / GPTImage repair candidate exists, with GenerationRun `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`.
- p02 candidate image: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`.
- p02 QA is **passed**. p02 ReferenceAsset: **accepted** as `ra-pilot-001-p02-fading-lamp-lane`. p02 accepted asset: **yes**.
- R00 master reference remains **p01 only**: `ra-pilot-001-r00-master-style-character-anchor`.

### Style is reusable; story content is variable

The child-drawn horror notebook style controls drawing method and atmosphere only (lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen circles/arrows, childish handwriting when story-appropriate, uneven proportions, matte scanned paper, creepy-but-child-drawn, supernatural permission). It must not inject wardrobes, door gaps, eyes, ghosts, or any example motif unless the current package asks for them. For every image, the strange event, location, characters, props, and emotional beat come from the approved `ImageExecutionPackage` and the canonical cards it binds. Human identity locks are intact (Xiao He = human child, Mama = human adult, Lantern Grandpa = human elderly man, Tangerine = cat; human characters never animal/plush/doll/mascot substitutes).

### Removed History Summary

An earlier warm-safe night-picture-book VisualStyle and its prompt recipe were used during the original visual pipeline, produced a failed p01 manual attempt (over-safe / polished digital / animalized humans / no horror), and have been **removed**. Their cards, old recipe hashes, repair iterations, stale handoffs, and stale compile/lint records are no longer part of the active pipeline and must not be bound. No image from that removed visual system was ever accepted; no ReferenceAsset was created from it.

### p02 Continuity Lesson Learned

p02 repair showed that visual style continuity alone is insufficient. The system must separately check page-to-page scene continuity, keep early pages from escalating too quickly, and require each hook to be a specific page-turn question rather than only a mood label. Future packages must define controlled deltas and forbidden continuity jumps before handoff; each page may only advance the environment and mystery by the amount justified by the Story Graph and the previous accepted page.


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
- Scene cards: `linked_packages` currently restored for p01, p02, and p03 only; p04-p14 scene-package links remain cleared pending package re-creation.

Neither this card nor the active visual system authorizes automated image generation. The p01 candidate was produced manually, backfilled through Workflow H, passed Workflow I QA, and was accepted through Workflow J as `ra-pilot-001-r00-master-style-character-anchor`.

## Execution Packages

**Option B (clean restart)** chosen. Current recreated packages:

- [p01 / The Fork at Dusk](../70-execution-packages/iep-pilot-001-p01-fork-at-dusk.md) - fresh `draft`, bound to the active style/recipe (`recipe_hash` `267c7dfe258e43ba`); Workflow H backfilled one manual candidate and GenerationRun; Workflow I QA passed; Workflow J accepted [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md).
- [p02 / The Fading-Lamp Lane](../70-execution-packages/iep-pilot-001-p02-fading-lamp-lane.md) - `ready`, bound to the active style/recipe and required R00 ReferenceAsset `ra-pilot-001-r00-master-style-character-anchor`; Workflow F compile and semantic lint passed; Workflow H repair candidate backfilled with GenerationRun `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`; Workflow I QA passed; Workflow J accepted page-level ReferenceAsset [ra-pilot-001-p02-fading-lamp-lane](../reference-assets/ra-pilot-001-p02-fading-lamp-lane.md); no final package or publishing record exists.
- [p03 / The Dark Wooded Lane](../70-execution-packages/iep-pilot-001-p03-dark-wooded-lane.md) - `ready`, bound to required R00 ReferenceAsset [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md) for global visual continuity and required previous-page ReferenceAsset [ra-pilot-001-p02-fading-lamp-lane](../reference-assets/ra-pilot-001-p02-fading-lamp-lane.md) for scene continuity only; Workflow F compile and semantic lint passed; GPTImage handoff is prepared for human operation only; generation remains blocked.

p04-p14 packages remain deleted after the reset and **must be recreated later** before the full 14-page story can proceed.

## Series Continuity & Master Anchor (serialized production)

This is a **serialized** picture book: across all pages **style consistency, character consistency, and proportion consistency are mandatory**. To enforce that, **p01 (the dusk fork page) is the designated series master anchor**. Workflow J accepted `ra-pilot-001-r00-master-style-character-anchor`; that accepted p01 image is now the master visual reference for every later page (p02-p14). Only the scene event changes from page to page; the look stays locked to the master.

> **Accepted master reference (current state).** The p01 image at `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png` is accepted as `ra-pilot-001-r00-master-style-character-anchor`. The R00 / series master visual anchor is active. It controls notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He / Mama visual appearance, and relative proportions only; it does not control future story events or force future pages to copy the p01 fork scene.

### Continuity Rule Set (mandatory for every future page)

Every later page must match the accepted p01 master on **all** of the following:

- **same notebook-paper style** — lined school-notebook page, same paper character.
- **same rough child-drawn line quality** — rough pencil/ballpoint outlines, colored-pencil/crayon fill, visible eraser marks, uneven childish proportions, imperfect hand-drawn perspective.
- **same red-pen annotation language** — red-pen circles, arrows, and question marks (plus optional short childish Chinese handwriting) used the same way to mark the page's anomaly/uncertainty, never replacing the scene.
- **same matte scanned paper texture** — matte scanned-paper look with creases, smudges, worn corners, faint yellowing.
- **same square format** — 1:1 square image on every page.
- **same character appearance** — character designs identical to the master (see Character Continuity).
- **same character proportions** — identical body/head proportions and relative heights to the master.
- **same emotional rendering language** — childlike fear, trembling, unease, curiosity, relief drawn in the same gentle child-drawn register (never realistic trauma).

### Character Continuity (never redesign, never animalize)

- **Xiao He** = human child; buttercup-yellow hooded raincoat, red rubber boots, small round backpack; short dark hair; ~6-7-year-old child proportions.
- **Mama** = human adult caregiver; teal coat and soft scarf; medium-length dark hair; adult proportions, clearly taller than Xiao He.
- **Never redesign** Xiao He or Mama — clothing, hair, face, and palette stay fixed to the master.
- **Never animalize** them — no animal, hedgehog, plush, doll, mascot, or anthropomorphic substitute; they stay human on every page.
- **Keep relative height and proportions stable** across all pages — Xiao He stays a small child beside a taller adult Mama; their size ratio does not drift page to page.
- (Lantern Grandpa = human elderly man and Tangerine = cat keep their identity locks too when they appear.)

### Page Continuity (per future page)

- **Every future page must use the accepted p01 image as the style and character reference** (uploaded as the master reference at GPTImage time).
- **Only the scene event changes** from page to page — the location/beat/strange event comes from that page's `ImageExecutionPackage` and Scene card.
- **Style, material, page language, and proportions stay stable** — paper, line quality, red-pen language, matte texture, square format, character design, and proportions are inherited from the master and must not drift.
- A page is a continuity failure (repair / regenerate) if the style, paper, character design, or proportions diverge from the master, or if a human character is animalized.

### Reusable GPTImage continuity prefix

For later pages, prepend the **Series Continuity Prefix** defined in `pr-pilot-001-child-horror-notebook` (see that recipe's "Series Continuity Prefix" section) to the page's compiled prompt, with the accepted p01 master image uploaded as the reference. The prefix locks style, character design, proportions, and page language to the master; the page's own scene event is the only variable.

## Production Status

- Workflow B human approval gate: **ACCEPTED** (story core + page-count confirmed; 2026-06-25).
- Accepted story core (locked): Cluster 3 only; 14-page structure; rational-reassuring ending; child-safe mystery + safety lesson.
- Page count: 14 (within ~12-16 target).
- Dry-read safety check: PASS.
- Workflow C human approval gate: **ACCEPTED** (character + scene canon confirmed; 2026-06-25): 4 Character cards, 7 Scene cards, referential integrity, source-distance / child-safety.
- Visual pipeline reset (2026-06-26): old warm-safe VisualStyle + PromptRecipe removed; single clean child-horror-notebook style/recipe active (`recipe_hash` `267c7dfe258e43ba`); packages reset to a single fresh p01 draft (Option B).
- Workflow H GenerationRun backfill for p01: **COMPLETED** (2026-06-29 backfill of 2026-06-26 manual WebGPTImage / GPTImage candidate).
- Candidate image exists at `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png`.
- GenerationRun: `50-agent-work/story-lab/runs/gr-pilot-001-p01-20260626-172625-webgptimage.md`.
- Workflow I image QA for p01: **PASSED**.
- QA evidence: `50-agent-work/story-lab/qa-results/qa-pilot-001-p01-candidate-20260626-172625.md`.
- Workflow J ReferenceAsset Acceptance for p01: **ACCEPTED**.
- Accepted ReferenceAsset: `ra-pilot-001-r00-master-style-character-anchor`.
- R00 / series master visual anchor active: **yes**.
- p02 ImageExecutionPackage recreation: **COMPLETED** with required R00 master visual reference.
- p02 Workflow F prompt compile and semantic lint: **PASSED**.
- p02 Workflow H repair candidate backfill: **COMPLETED**.
- p02 candidate image exists at `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`.
- p02 GenerationRun: `50-agent-work/story-lab/runs/gr-pilot-001-p02-repair-01-20260630-154548-webgptimage.md`.
- p02 QA evidence: `50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md`.
- Workflow J ReferenceAsset Acceptance for p02: **ACCEPTED**.
- Accepted p02 ReferenceAsset: `ra-pilot-001-p02-fading-lamp-lane`.
- p03 ImageExecutionPackage recreation: **COMPLETED as draft only** with required references `ra-pilot-001-r00-master-style-character-anchor` and `ra-pilot-001-p02-fading-lamp-lane`.
- p03 Workflow F prompt compile and semantic lint: **PASSED**.
- p03 package status: **ready**.
- p03 GPTImage handoff preparation: **PREPARED** at `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p03-dark-wooded-lane-gptimage.md`.
- p03 downstream generation status: **blocked**. No p03 image generation, GenerationRun, or ReferenceAsset exists.
- p04-p14 packages: **not created**.
- Current workflow: **p03 ready package and GPTImage handoff exist. Next controlled step is separately authorized human GPTImage execution. Stop before external image execution, GenerationRun creation, or ReferenceAsset creation unless separately authorized.**
- p01 QA status: **pass**.
- p01 ReferenceAsset status: **accepted**.
- p02 QA status: **pass**.
- p02 ReferenceAsset status: **accepted**.

## Blocked Actions

Workflows A, B, C are accepted. Workflow H backfilled one p01 candidate and GenerationRun, Workflow I QA passed, and Workflow J accepted the p01 ReferenceAsset. Workflow J also accepted the p02 page-level ReferenceAsset. The following remain blocked:

- p03 image generation, GenerationRun creation, and ReferenceAsset creation until human execution and the next backfill/QA workflows are separately authorized
- p04-p14 package creation or generation until each package is recreated from canonical cards
- final package assembly
- publishing readiness
- p04-p14 re-creation + compile/lint (required before the full story can proceed)

## Next Workflow

p03 GPTImage handoff preparation is complete, using `ra-pilot-001-r00-master-style-character-anchor` for global visual continuity and `ra-pilot-001-p02-fading-lamp-lane` as the immediately previous accepted page reference for p03 scene continuity. Next controlled step is separately authorized human GPTImage execution. Do not generate images, create GenerationRuns, create ReferenceAssets, create p04-p14 packages, create a final package, or create publishing records before the relevant later workflow is authorized.


## Notes

This project begins from raw intake only. The raw source is not publishable text and must not be treated as final story prose.
