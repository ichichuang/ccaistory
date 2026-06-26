---
type: image_execution_package
id: iep-pilot-001-p02-fading-lamp-lane
title_zh: pilot-001 p02 灯火渐稀的小路图像执行包
title_en: pilot-001 p02 The Fading-Lamp Lane Image Execution Package
status: draft
project_id: pilot-001
scene_id: scene-fading-lamp-lane
page_or_spread_range: p02
characters:
  - char-xiaohe
  - char-mama
character_ids:
  - char-xiaohe
  - char-mama
visual_style:
  - vs-pilot-001-child-horror-notebook
visual_style_id: vs-pilot-001-child-horror-notebook
prompt_recipe: pr-pilot-001-child-horror-notebook
prompt_recipe_id: pr-pilot-001-child-horror-notebook
recipe_hash: "58802ab763ac5dc6"
compile_result_ref: "50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p02-fading-lamp-lane.json"
semantic_lint_result_ref: "50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p02-fading-lamp-lane.json"
recipe_hash_check: "stale"
recipe_hash_expected: "58802ab763ac5dc6"
recipe_hash_actual: ""
compile_status: stale
semantic_lint_status: stale
workflow_f_gate: "superseded by the 2026-06-26 visual-system refactor; stale under the new recipe; recompile/relint required; not auto-released"
downstream_generation_status: blocked
blocked_reason: "Visual-system refactor to vs-pilot-001-child-horror-notebook + pr-pilot-001-child-horror-notebook (recipe_hash 58802ab763ac5dc6). The prior warm-safe compile/lint is stale; this package must be recompiled and relinted under the new recipe before it can be ready. Not auto-released; image generation blocked."
repair_notes: []
target_model: "WebGPTImage blocked until Workflow G"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Shortcut lane with street lamps spaced farther apart, shrinking warm light pools, and first low mist."
  - "Xiao He and Mama walking together calmly as unease rises gently."
forbidden_content:
  - "No horror, monster, ghost, gore, crime, adult content, occult or supernatural-punishment content."
  - "No source names, source places, copied source wording, image text, or WebGPTImage final prompt text."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-fading-lamp-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
source_paths: []
last_run: ""
qa_result: ""
r00_dependency_policy: "No R00 dependency. No ReferenceAsset exists or is required for this Workflow F compile/lint pass; any future anchor dependency must be separately accepted and declared before use."
maximum_anchor_reuse_policy: "No anchor reuse in this package. Do not create, reuse, or imply R00/R01/R02 assets from this package."
dependency_notes: "Depends only on accepted Workflow A-D canonical cards: StoryProject, Scene, Character, VisualStyle, and PromptRecipe."
blocking_notes: "Re-pointed by the visual-system refactor and downgraded out of ready. Compile/lint under the deprecated warm-safe recipe is stale; recompile/relint under pr-pilot-001-child-horror-notebook is required before ready. Not auto-released. Workflow G WebGPTImage handoff, image generation, GenerationRun, ReferenceAsset, final package, and publishing records remain blocked."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - workflow-e
  - workflow-f
  - visual-system-refactor
  - child-horror-notebook
  - stale-recompile
  - blocked
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p02 灯火渐稀的小路图像执行包 / The Fading-Lamp Lane Image Execution Package

> Re-pointed by the 2026-06-26 visual-system refactor and downgraded out of `ready`. This package's prior Workflow F compile/lint ran against the now-deprecated warm-safe recipe and is STALE; it must be recompiled and relinted under `pr-pilot-001-child-horror-notebook` before it can be `ready` again. Not auto-released. This is not a WebGPTImage handoff, GenerationRun, ReferenceAsset, final package, publishing record, or image output.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p02`
- Scene: [scene-fading-lamp-lane](../40-scenes/scene-fading-lamp-lane.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash (new binding): `58802ab763ac5dc6` — not yet recompiled under the new recipe (stale)

## Target Asset / 目标资产

Workflow F ready package plan for the p02 page illustration: the shortcut begins to feel quietly wrong as lamps thin out. No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-fading-lamp-lane`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: visual-system refactor re-pointed this package to the child-horror-notebook style/recipe and downgraded it out of `ready`. The prior compile/lint is stale. Workflow G, WebGPTImage handoff, and image generation remain blocked; not auto-released.

## Allowed Content / 允许内容

- Street lamps set farther and farther apart, with warm pools of light shrinking.
- Narrowing shortcut lane, first low wisps of mist, trees drawing closer.
- Xiao He and Mama walking together, still calm and physically close.

## Forbidden Content / 禁止内容

- No horror, realistic thriller, jump scares, monsters, ghost faces, gore, blood, crime, weapons, adult or sexualized content.
- No religious punishment, occult symbols, magic, possession, curses, or supernatural payoff.
- No source names, source places, source wording, copied sequence packaging, channel identity, or identifiable horror motifs.
- No printed narration, final prompt text, image IDs, or WebGPTImage handoff text in the source illustration.

## Prompt Recipe Binding / Prompt 技法绑定

Re-pointed to `pr-pilot-001-child-horror-notebook` (recipe_hash `58802ab763ac5dc6`). The existing compiled-prompt record was produced under the deprecated `pr-pilot-001-safe-night-picturebook` and is STALE; this package must be recompiled under the new recipe before it can be `ready`. This card does not contain external execution prompt text.

## Workflow F Compile and Semantic Lint / Workflow F 编译与语义 Lint

- Compile result: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p02-fading-lamp-lane.json`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p02-fading-lamp-lane.json`.
- Recipe hash comparison: `stale` (expected `58802ab763ac5dc6`; the existing compiled record was hashed `6020fc5e5c83e043` under the deprecated recipe; recompile required).
- Compile status: `stale` (recompile required under the new recipe).
- Semantic lint status: `stale` (relint required under the new recipe).
- Package state: `draft`; downgraded from `ready` by the visual-system refactor. Not auto-released; blocked until recompiled/relinted under the new recipe and re-approved.

## Reference Asset Binding / 参考资产绑定

`reference_assets`, `required_reference_assets`, and `prohibited_reference_assets` are empty because no accepted ReferenceAsset cards exist for `pilot-001` and none are required for this Workflow F compile/lint pass. Future anchors must be accepted and explicitly bound before any package may depend on them.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output target: page illustration plan only.
- No generated image file, no raw output, and no accepted asset are created here.

## Generation Order / 生成顺序

Initial full-story order: 2 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

No WebGPTImage execution is authorized from this ready package. A later Workflow G handoff requires separate authorization after the Workflow F human/QA gate.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm mild unease only, clear thinning-lamps clue, stable character locks, source-distance compliance, and no forbidden content.

## Repair Triggers / 修复触发条件

Repair if the lane reads as horror, the mist forms figures or faces, Xiao He appears traumatized, or source-like identifiers appear.

## Result Backfill Procedure / 结果回填流程

No backfill now. If a later run is approved, GenerationRun and ReferenceAsset records must be created only through the relevant downstream workflows.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
