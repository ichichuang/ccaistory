---
type: image_execution_package
id: iep-pilot-001-p08-lantern-cottage-welcome
title_zh: pilot-001 p08 守灯小屋欢迎图像执行包
title_en: pilot-001 p08 Lantern Cottage Welcome Image Execution Package
status: ready
project_id: pilot-001
scene_id: scene-lantern-cottage
page_or_spread_range: p08
characters:
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
character_ids:
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
visual_style:
  - vs-pilot-001-warm-safe-night-picturebook
visual_style_id: vs-pilot-001-warm-safe-night-picturebook
prompt_recipe: pr-pilot-001-safe-night-picturebook
prompt_recipe_id: pr-pilot-001-safe-night-picturebook
recipe_hash: "6020fc5e5c83e043"
compile_result_ref: "50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p08-lantern-cottage-welcome.json"
semantic_lint_result_ref: "50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p08-lantern-cottage-welcome.json"
recipe_hash_check: "match"
recipe_hash_expected: "6020fc5e5c83e043"
recipe_hash_actual: "6020fc5e5c83e043"
compile_status: pass
semantic_lint_status: pass
workflow_f_gate: "human_qa_gate; WebGPTImage blocked; image generation blocked"
downstream_generation_status: blocked
blocked_reason: ""
repair_notes: []
target_model: "WebGPTImage blocked until Workflow G"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Lantern Grandpa warmly welcomes Xiao He and Mama with lantern light."
  - "Relief begins; the old road and open fields are explained as ordinary and safe."
forbidden_content:
  - "No horror, monster, ghost, gore, crime, adult content, occult or supernatural-punishment content."
  - "Lantern Grandpa must never read as eerie, sinister, ambiguous, predatory, uncanny, or magical."
  - "No source names, source places, copied source wording, image text, or WebGPTImage final prompt text."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-lantern-cottage
  - char-xiaohe
  - char-mama
  - char-lantern-grandpa
  - vs-pilot-001-warm-safe-night-picturebook
  - pr-pilot-001-safe-night-picturebook
source_paths: []
last_run: ""
qa_result: ""
r00_dependency_policy: "No R00 dependency. No ReferenceAsset exists or is required for this Workflow F compile/lint pass; any future anchor dependency must be separately accepted and declared before use."
maximum_anchor_reuse_policy: "No anchor reuse in this package. Do not create, reuse, or imply R00/R01/R02 assets from this package."
dependency_notes: "Depends only on accepted Workflow A-D canonical cards: StoryProject, Scene, Character, VisualStyle, and PromptRecipe."
blocking_notes: "Workflow F prompt compile / semantic lint passed. Stop at Workflow F human/QA gate; Workflow G WebGPTImage handoff, image generation, GenerationRun, ReferenceAsset, final package, and publishing records remain blocked."
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

# pilot-001 p08 守灯小屋欢迎图像执行包 / Lantern Cottage Welcome Image Execution Package

> Workflow F compile and semantic lint passed. This is not a WebGPTImage handoff, GenerationRun, ReferenceAsset, final package, publishing record, or image output.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p08`
- Scene: [scene-lantern-cottage](../40-scenes/scene-lantern-cottage.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md), [char-lantern-grandpa](../30-characters/char-lantern-grandpa.md)
- VisualStyle: [vs-pilot-001-warm-safe-night-picturebook](../50-visual-styles/vs-pilot-001-warm-safe-night-picturebook.md)
- PromptRecipe: [pr-pilot-001-safe-night-picturebook](../60-prompts/pr-pilot-001-safe-night-picturebook.md)
- Recipe hash: `6020fc5e5c83e043`

## Target Asset / 目标资产

Workflow F ready package plan for the p08 page illustration: a kind welcome in lantern light and the first ordinary explanation for being lost. No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-lantern-cottage`, Character cards `char-xiaohe`, `char-mama`, and `char-lantern-grandpa`, VisualStyle `vs-pilot-001-warm-safe-night-picturebook`, PromptRecipe `pr-pilot-001-safe-night-picturebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: Workflow F compile and semantic lint passed; stop at Workflow F human/QA gate. Workflow G, WebGPTImage handoff, and image generation remain blocked.

## Allowed Content / 允许内容

- Lantern Grandpa with round glasses, soft grey beard, brown cardigan, and a glowing lantern.
- Xiao He and Mama warmed by cottage light; relief beginning.
- Simple visual cue that the old road runs toward open fields and can be confusing in the dark.

## Forbidden Content / 禁止内容

- No horror, realistic thriller, jump scares, monsters, ghost faces, gore, blood, crime, weapons, adult or sexualized content.
- No religious punishment, occult symbols, magic, possession, curses, or supernatural payoff.
- Lantern Grandpa must never read as eerie, sinister, ambiguous, predatory, uncanny, or magical.
- No source names, source places, source wording, copied sequence packaging, channel identity, or identifiable horror motifs.
- No printed narration, final prompt text, image IDs, or WebGPTImage handoff text in the source illustration.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-safe-night-picturebook` with verified `recipe_hash: 6020fc5e5c83e043`. Workflow F compiled this package into the referenced derived prompt record; this card does not contain external execution prompt text.

## Workflow F Compile and Semantic Lint / Workflow F 编译与语义 Lint

- Compile result: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p08-lantern-cottage-welcome.json`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p08-lantern-cottage-welcome.json`.
- Recipe hash comparison: `match` (`6020fc5e5c83e043`).
- Compile status: `pass`.
- Semantic lint status: `pass`.
- Package state: `ready`; downstream WebGPTImage handoff and image generation remain blocked until separate Workflow G authorization.

## Reference Asset Binding / 参考资产绑定

`reference_assets`, `required_reference_assets`, and `prohibited_reference_assets` are empty because no accepted ReferenceAsset cards exist for `pilot-001` and none are required for this Workflow F compile/lint pass. Future anchors must be accepted and explicitly bound before any package may depend on them.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output target: page illustration plan only.
- No generated image file, no raw output, and no accepted asset are created here.

## Generation Order / 生成顺序

Initial full-story order: 8 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

No WebGPTImage execution is authorized from this ready package. A later Workflow G handoff requires separate authorization after the Workflow F human/QA gate.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm Grandpa reads safe and welcoming, relief is visible, and the explanation remains ordinary.

## Repair Triggers / 修复触发条件

Repair if Grandpa reads uncanny, the scene suggests danger or punishment, or source-like identifiers appear.

## Result Backfill Procedure / 结果回填流程

No backfill now. If a later run is approved, GenerationRun and ReferenceAsset records must be created only through the relevant downstream workflows.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
