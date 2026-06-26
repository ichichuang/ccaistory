---
type: image_execution_package
id: iep-pilot-001-p06-dark-wooded-lane-steady-breath
title_zh: pilot-001 p06 黑黑林路稳稳呼吸图像执行包
title_en: pilot-001 p06 Dark Wooded Lane Steady Breath Image Execution Package
status: draft
project_id: pilot-001
scene_id: scene-dark-wooded-lane
page_or_spread_range: p06
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
target_model: "WebGPTImage blocked until Workflow G"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Xiao He and Mama stop together, hold hands, breathe, and choose to stay calm."
  - "Small pocket of warm safety within the dark lane."
forbidden_content:
  - "No horror, monster, ghost, gore, crime, adult content, occult or supernatural-punishment content."
  - "No panic, abandonment, traumatic crying, or unsafe caregiver depiction."
  - "No source names, source places, copied source wording, image text, or WebGPTImage final prompt text."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-dark-wooded-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-warm-safe-night-picturebook
  - pr-pilot-001-safe-night-picturebook
source_paths: []
last_run: ""
qa_result: ""
r00_dependency_policy: "No R00 dependency. No ReferenceAsset exists for pilot-001; this package must remain draft until any future anchor dependency is separately accepted and declared."
maximum_anchor_reuse_policy: "No anchor reuse at draft stage. Do not create, reuse, or imply R00/R01/R02 assets from this package."
dependency_notes: "Depends only on accepted Workflow A-D canonical cards: StoryProject, Scene, Character, VisualStyle, and PromptRecipe."
blocking_notes: "Workflow E human review required before ready. Workflow F prompt compile / semantic lint, Workflow G WebGPTImage handoff, image generation, GenerationRun, ReferenceAsset, final package, and publishing records are blocked."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - workflow-e
  - draft
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p06 黑黑林路稳稳呼吸图像执行包 / Dark Wooded Lane Steady Breath Image Execution Package

> Workflow E draft only. This is not a compiled prompt, WebGPTImage handoff, GenerationRun, ReferenceAsset, final package, or image output.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p06`
- Scene: [scene-dark-wooded-lane](../40-scenes/scene-dark-wooded-lane.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-warm-safe-night-picturebook](../50-visual-styles/vs-pilot-001-warm-safe-night-picturebook.md)
- PromptRecipe: [pr-pilot-001-safe-night-picturebook](../60-prompts/pr-pilot-001-safe-night-picturebook.md)
- Recipe hash: `6020fc5e5c83e043`

## Target Asset / 目标资产

Draft plan for the p06 page illustration: the emotional turn where Xiao He and Mama pause, breathe, and choose calm. No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-dark-wooded-lane`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-warm-safe-night-picturebook`, PromptRecipe `pr-pilot-001-safe-night-picturebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: human review required before `ready`; F/G and image generation blocked.

## Allowed Content / 允许内容

- Xiao He and Mama close together, holding hands, taking a steady breath.
- Dark lane remains visible but less threatening; a small warm safety focus around the figures.
- Xiao He's fear begins to settle.

## Forbidden Content / 禁止内容

- No horror, realistic thriller, jump scares, monsters, ghost faces, gore, blood, crime, weapons, adult or sexualized content.
- No religious punishment, occult symbols, magic, possession, curses, or supernatural payoff.
- No panic, abandonment, traumatic crying, unsafe caregiver behavior, or scolding tone.
- No source names, source places, source wording, copied sequence packaging, channel identity, or identifiable horror motifs.
- No printed narration, final prompt text, image IDs, or WebGPTImage handoff text in the source illustration.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-safe-night-picturebook` with verified `recipe_hash: 6020fc5e5c83e043`. This package only binds the recipe; it does not compile a prompt.

## Reference Asset Binding / 参考资产绑定

`reference_assets`, `required_reference_assets`, and `prohibited_reference_assets` are empty because no accepted ReferenceAsset cards exist for `pilot-001`. Future anchors must be accepted and explicitly bound before this package can become `ready`.

## Canvas and Output Rules / 画布与输出规则

- Draft aspect ratio: `1:1`.
- Output target: page illustration plan only.
- No generated image file, no raw output, and no accepted asset are created here.

## Generation Order / 生成顺序

Initial full-story order: 6 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

No WebGPTImage execution is authorized from this draft. A later Workflow G handoff may be written only after this package becomes `ready` through Workflow E human review and Workflow F compile/lint.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm the calming turn is visually clear, caregiver proximity is visible, and fear is already reducing.

## Repair Triggers / 修复触发条件

Repair if the page still reads as peak fear, the caregiver appears panicked, or supernatural/horror cues remain dominant.

## Result Backfill Procedure / 结果回填流程

No backfill now. If a later run is approved, GenerationRun and ReferenceAsset records must be created only through the relevant downstream workflows.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
