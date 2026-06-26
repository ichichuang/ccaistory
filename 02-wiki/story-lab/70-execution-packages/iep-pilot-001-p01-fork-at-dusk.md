---
type: image_execution_package
id: iep-pilot-001-p01-fork-at-dusk
title_zh: pilot-001 p01 黄昏岔路口图像执行包
title_en: pilot-001 p01 The Fork at Dusk Image Execution Package
status: ready
project_id: pilot-001
scene_id: scene-fork-at-dusk
page_or_spread_range: p01
characters:
  - char-xiaohe
  - char-mama
character_ids:
  - char-xiaohe
  - char-mama
visual_style:
  - vs-pilot-001-warm-safe-night-picturebook
visual_style_id: vs-pilot-001-warm-safe-night-picturebook
prompt_recipe: pr-pilot-001-safe-night-picturebook
prompt_recipe_id: pr-pilot-001-safe-night-picturebook
recipe_hash: "6020fc5e5c83e043"
compile_result_ref: "50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p01-fork-at-dusk.json"
semantic_lint_result_ref: "50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p01-fork-at-dusk.json"
recipe_hash_check: "match"
recipe_hash_expected: "6020fc5e5c83e043"
recipe_hash_actual: "6020fc5e5c83e043"
compile_status: pass
semantic_lint_status: pass
workflow_f_gate: "accepted; prompt compile and semantic lint passed"
workflow_g_gate: "started for p01 only; controlled manual handoff created"
webgptimage_handoff_record_ref: "50-agent-work/story-lab/webgptimage-handoffs/pilot-001/iep-pilot-001-p01-fork-at-dusk.md"
webgptimage_handoff_status: "manual_pending"
downstream_generation_status: blocked
blocked_reason: "Image generation not run; pending human manual execution in WebGPTImage from the p01 handoff record."
repair_notes: []
target_model: "WebGPTImage manual window; execution pending human action"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Dusk fork in the road with Xiao He and Mama choosing between a familiar bright road and a shadowy unknown shortcut."
  - "Wooden signpost, warm dusk sky, first stars, gentle curiosity and mild unease."
forbidden_content:
  - "No horror, monster, ghost, gore, crime, adult content, occult or supernatural-punishment content."
  - "No source names, source places, copied source wording, image text, or WebGPTImage final prompt text."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-fork-at-dusk
  - char-xiaohe
  - char-mama
  - vs-pilot-001-warm-safe-night-picturebook
  - pr-pilot-001-safe-night-picturebook
source_paths: []
last_run: ""
qa_result: ""
r00_dependency_policy: "No R00 dependency. No ReferenceAsset exists or is required for this Workflow F compile/lint pass; any future anchor dependency must be separately accepted and declared before use."
maximum_anchor_reuse_policy: "No anchor reuse in this package. Do not create, reuse, or imply R00/R01/R02 assets from this package."
dependency_notes: "Depends only on accepted Workflow A-D canonical cards: StoryProject, Scene, Character, VisualStyle, and PromptRecipe."
blocking_notes: "Workflow F prompt compile / semantic lint passed. Workflow G manual handoff created for p01 only; image generation, GenerationRun, ReferenceAsset, final package, and publishing records remain blocked pending human execution evidence. p02-p14 handoffs remain blocked."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - workflow-e
  - workflow-f
  - ready
  - lint-passed
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p01 黄昏岔路口图像执行包 / The Fork at Dusk Image Execution Package

> Workflow F compile and semantic lint passed. Workflow G has created a controlled manual WebGPTImage handoff record for p01 only. This card is not a GenerationRun, ReferenceAsset, final package, publishing record, or image output.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p01`
- Scene: [scene-fork-at-dusk](../40-scenes/scene-fork-at-dusk.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-warm-safe-night-picturebook](../50-visual-styles/vs-pilot-001-warm-safe-night-picturebook.md)
- PromptRecipe: [pr-pilot-001-safe-night-picturebook](../60-prompts/pr-pilot-001-safe-night-picturebook.md)
- Recipe hash: `6020fc5e5c83e043`

## Target Asset / 目标资产

Workflow F ready package plan for the p01 page illustration: a gentle establishing image of the dusk road fork. No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-fork-at-dusk`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-warm-safe-night-picturebook`, PromptRecipe `pr-pilot-001-safe-night-picturebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: Workflow F compile and semantic lint passed. Workflow G manual handoff is started for p01 only; image generation remains pending human action in WebGPTImage.

## Allowed Content / 允许内容

- Dusk fork with one bright familiar road and one shadowy unknown shortcut.
- Xiao He in yellow raincoat and red boots; Mama in teal coat and scarf.
- Wooden signpost, gold-to-blue sky, first stars, warm readable light.
- Curiosity and mild unease only.

## Forbidden Content / 禁止内容

- No horror, realistic thriller, jump scares, monsters, ghost faces, gore, blood, crime, weapons, adult or sexualized content.
- No religious punishment, occult symbols, magic, possession, curses, or supernatural payoff.
- No source names, source places, source wording, copied sequence packaging, channel identity, or identifiable horror motifs.
- No printed narration, final prompt text, image IDs, or WebGPTImage handoff text in the source illustration.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-safe-night-picturebook` with verified `recipe_hash: 6020fc5e5c83e043`. Workflow F compiled this package into the referenced derived prompt record; this card does not contain external execution prompt text.

## Workflow F Compile and Semantic Lint / Workflow F 编译与语义 Lint

- Compile result: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p01-fork-at-dusk.json`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p01-fork-at-dusk.json`.
- Recipe hash comparison: `match` (`6020fc5e5c83e043`).
- Compile status: `pass`.
- Semantic lint status: `pass`.
- Package state: `ready`; Workflow G manual handoff is created for p01 only; image generation has not occurred.

## Workflow G Manual Handoff / Workflow G 人工交接

- Handoff record: `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/iep-pilot-001-p01-fork-at-dusk.md`.
- Handoff status: `manual_pending`.
- Scope: p01 only; p02-p14 are not released by this package update.
- WebGPTImage remains a manual external window action.
- No generated image file, GenerationRun, ReferenceAsset, final package, or publishing record is created by this package update.
- No external execution prompt has been backfilled here; manual evidence is required after the human operator uses the handoff in WebGPTImage.

## Reference Asset Binding / 参考资产绑定

`reference_assets`, `required_reference_assets`, and `prohibited_reference_assets` are empty because no accepted ReferenceAsset cards exist for `pilot-001` and none are required for this Workflow F compile/lint pass. Future anchors must be accepted and explicitly bound before any package may depend on them.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output target: page illustration plan only.
- No generated image file, no raw output, and no accepted asset are created here.

## Generation Order / 生成顺序

Initial full-story order: 1 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

Use only the controlled Workflow G handoff record listed above for p01 manual WebGPTImage execution. Do not execute p02-p14 from this package. Image generation remains pending until a human operator manually uses the handoff in WebGPTImage and records the required evidence.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm child-safe mood, readable road choice, stable character locks, source-distance compliance, and no forbidden content.

## Repair Triggers / 修复触发条件

Repair if the shortcut becomes threatening, Xiao He appears terrified, Mama appears unsafe, source-like identifiers appear, or any supernatural/horror cue is introduced.

## Result Backfill Procedure / 结果回填流程

No backfill now. After a human operator manually uses the p01 handoff and records execution evidence, GenerationRun and ReferenceAsset records must be created only through the relevant downstream workflows.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
