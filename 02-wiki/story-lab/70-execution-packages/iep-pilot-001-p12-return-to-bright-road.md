---
type: image_execution_package
id: iep-pilot-001-p12-return-to-bright-road
title_zh: pilot-001 p12 回到亮亮的大路图像执行包
title_en: pilot-001 p12 Back to the Bright Road Image Execution Package
status: draft
project_id: pilot-001
scene_id: scene-return-to-bright-road
page_or_spread_range: p12
characters:
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
character_ids:
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
visual_style:
  - vs-pilot-001-child-horror-notebook
visual_style_id: vs-pilot-001-child-horror-notebook
prompt_recipe: pr-pilot-001-child-horror-notebook
prompt_recipe_id: pr-pilot-001-child-horror-notebook
recipe_hash: "267c7dfe258e43ba"
compile_result_ref: "50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p12-return-to-bright-road.json"
semantic_lint_result_ref: "50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p12-return-to-bright-road.json"
recipe_hash_check: "stale"
recipe_hash_expected: "267c7dfe258e43ba"
recipe_hash_actual: ""
compile_status: stale
semantic_lint_status: stale
workflow_f_gate: "superseded by the 2026-06-26 visual-system refactor; stale under the new recipe; recompile/relint required; not auto-released"
downstream_generation_status: blocked
blocked_reason: "Visual-system refactor to vs-pilot-001-child-horror-notebook + pr-pilot-001-child-horror-notebook (recipe_hash 267c7dfe258e43ba). The prior warm-safe compile/lint is stale; this package must be recompiled and relinted under the new recipe before it can be ready. Not auto-released; image generation blocked."
repair_notes: []
target_model: "WebGPTImage blocked until Workflow G"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Lantern Grandpa guides Xiao He and Mama back toward the familiar evenly lit road."
  - "Wooden signpost callback, warm lamplight, Xiao He walking a little braver."
forbidden_content:
  - "Hard content-safety only (live): no gore, no realistic corpse, no real child abuse, no severe child injury or trauma, no crime, no adult or sexual content."
  - "Superseded as a global style ban under vs-pilot-001-child-horror-notebook: 'No horror / No ghost / No supernatural / occult / supernatural-punishment' is no longer a project-wide style rule; this page's rational-safe tone is a story-layer choice only, not a ban on supernatural content."
  - "No chase, danger, punishment, or supernatural rescue."
  - "No source names, source places, copied source wording, image text, or WebGPTImage final prompt text."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-return-to-bright-road
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
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

# pilot-001 p12 回到亮亮的大路图像执行包 / Back to the Bright Road Image Execution Package

> Re-pointed by the 2026-06-26 visual-system refactor and downgraded out of `ready`. This package's prior Workflow F compile/lint ran against the now-deprecated warm-safe recipe and is STALE; it must be recompiled and relinted under `pr-pilot-001-child-horror-notebook` before it can be `ready` again. Not auto-released. This is not a WebGPTImage handoff, GenerationRun, ReferenceAsset, final package, publishing record, or image output.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p12`
- Scene: [scene-return-to-bright-road](../40-scenes/scene-return-to-bright-road.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md), [char-lantern-grandpa](../30-characters/char-lantern-grandpa.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash (new binding): `267c7dfe258e43ba` — not yet recompiled under the new recipe (stale)

## Target Asset / 目标资产

Workflow F ready package plan for the p12 page illustration: guided movement back into warm familiar lamplight. No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-return-to-bright-road`, Character cards `char-xiaohe`, `char-mama`, and `char-lantern-grandpa`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: visual-system refactor re-pointed this package to the child-horror-notebook style/recipe and downgraded it out of `ready`. The prior compile/lint is stale. Workflow G, WebGPTImage handoff, and image generation remain blocked; not auto-released.

## Allowed Content / 允许内容

- Lantern Grandpa guiding Xiao He and Mama from dark lane toward evenly spaced warm road lamps.
- Wooden signpost callback to the opening fork.
- Xiao He walking taller and braver; Mama calm and close.

## Forbidden Content / 禁止内容

- Hard content-safety (live under the new style): no gore, no blood, no realistic corpse, no real child abuse, no severe child injury or visible trauma, no crime reproduction, no weapons used to harm, no sexual or adult content.
- Superseded as a global style ban: the prior "No horror, realistic thriller, jump scares, monsters, ghost faces" wording no longer acts as a project-wide style ban under `vs-pilot-001-child-horror-notebook`. Any remaining page-level rational-safe constraints below are story-layer choices for this specific rational-reassuring story, not a ban on supernatural or creepy content for the project.
- Superseded as a global style ban: "no religious punishment, occult symbols, magic, possession, curses, or supernatural payoff" is no longer a project-wide style rule under the new visual system; it is retained only as this page's story-layer rational-safe choice for this rational-reassuring story.
- No chase, danger, punishment, or supernatural rescue.
- No source names, source places, source wording, copied sequence packaging, channel identity, or identifiable horror motifs.
- No printed narration, final prompt text, image IDs, or WebGPTImage handoff text in the source illustration.

## Prompt Recipe Binding / Prompt 技法绑定

Re-pointed to `pr-pilot-001-child-horror-notebook` (recipe_hash `267c7dfe258e43ba`). The existing compiled-prompt record was produced under the deprecated `pr-pilot-001-safe-night-picturebook` and is STALE; this package must be recompiled under the new recipe before it can be `ready`. This card does not contain external execution prompt text.

## Workflow F Compile and Semantic Lint / Workflow F 编译与语义 Lint

- Compile result: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p12-return-to-bright-road.json`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p12-return-to-bright-road.json`.
- Recipe hash comparison: `stale` (expected `267c7dfe258e43ba`; the existing compiled record was hashed `6020fc5e5c83e043` under the deprecated recipe; recompile required).
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

Initial full-story order: 12 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

No WebGPTImage execution is authorized from this ready package. A later Workflow G handoff requires separate authorization after the Workflow F human/QA gate.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm hopeful motion, visible safety, character continuity, and the return-road callback.

## Repair Triggers / 修复触发条件

Repair if the image reintroduces threat, loses Grandpa's safe-helper cues, or includes source-like identifiers.

## Result Backfill Procedure / 结果回填流程

No backfill now. If a later run is approved, GenerationRun and ReferenceAsset records must be created only through the relevant downstream workflows.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
