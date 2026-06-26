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
  - vs-pilot-001-child-horror-notebook
visual_style_id: vs-pilot-001-child-horror-notebook
prompt_recipe: pr-pilot-001-child-horror-notebook
prompt_recipe_id: pr-pilot-001-child-horror-notebook
recipe_hash: "58802ab763ac5dc6"
compile_result_ref: "50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p01-fork-at-dusk-repair_02.json"
semantic_lint_result_ref: "50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p01-fork-at-dusk-repair_02.json"
recipe_hash_check: "match"
recipe_hash_expected: "58802ab763ac5dc6"
recipe_hash_actual: "58802ab763ac5dc6"
compile_status: pass
semantic_lint_status: pass
workflow_f_gate: "repair_02 prompt compile and semantic lint passed against the new child-horror-notebook visual system"
workflow_g_gate: "repair_02 prepared for p01 only; controlled manual handoff created; candidate not accepted; awaiting repair human gate"
webgptimage_handoff_record_ref: "50-agent-work/story-lab/webgptimage-handoffs/pilot-001/iep-pilot-001-p01-fork-at-dusk-repair_02.md"
webgptimage_handoff_status: "repair_02_manual_pending"
downstream_generation_status: blocked
blocked_reason: "Visual-system refactor. The prior p01 manual generation failed (over-safe / polished digital / animalized humans / no horror) under the now-deprecated warm-safe base style. p01 is re-pointed to vs-pilot-001-child-horror-notebook + pr-pilot-001-child-horror-notebook and recompiled as repair_02. Image generation stays blocked: stop at the repair human gate; do not accept any prior candidate."
repair_notes:
  - repair-pilot-001-p01-visual-system-refactor
  - repair-pilot-001-p01-webgptimage-style-species-drift
target_model: "WebGPTImage manual window; repair_02 execution pending repair human gate + human action"
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Dusk fork in the road drawn as a child's notebook page: a familiar bright road versus a darker unknown shortcut, with a wooden signpost readable only as an object."
  - "Xiao He as a human child (yellow hooded raincoat, red boots, small round backpack) and Mama as a human adult caregiver (teal coat, scarf), drawn childishly but clearly human."
  - "Lined school-notebook paper with creases and a matte scanned look; rough pencil/ballpoint outlines, colored-pencil/crayon fill, visible eraser marks; a red-pen circle, arrow, or question mark on the dark shortcut and a short childish Chinese handwritten note are allowed."
forbidden_content:
  - "No polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, or clean vector line art."
  - "No 3D, cinematic realism, photorealism, oil painting, film lighting, or realistic crime-evidence photography."
  - "No animals replacing Xiao He or Mama; no hedgehogs, mice, rabbits, bears, dolls, plush-like humans, mascots, or anthropomorphic figures."
  - "No explicit gore, realistic corpse, real child abuse, severe child injury or visible trauma, sexual or adult content, or real-crime reproduction."
  - "No source names, source places, copied source wording, recognizable horror imagery, or any in-image platform/prompt/image-id/WebGPTImage handoff text or legible sign words."
output_assets: []
generation_run_ids: []
related_assets:
  - scene-fork-at-dusk
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
source_paths: []
last_run: ""
qa_result: "failed"
r00_dependency_policy: "No R00 dependency. No ReferenceAsset exists or is required for this Workflow F repair_02 compile/lint pass; any future anchor dependency must be separately accepted and declared before use."
maximum_anchor_reuse_policy: "No anchor reuse in this package. Do not create, reuse, or imply R00/R01/R02 assets from this package."
dependency_notes: "Depends only on accepted Workflow A-C canonical cards (StoryProject, Scene, Character) plus the new D-stage VisualStyle/PromptRecipe pending the repair human gate."
blocking_notes: "Prior p01 manual WebGPTImage result failed (over-safe / polished digital / animalized humans / no horror) and is not accepted. The visual-system refactor re-pointed this package to the child-horror-notebook style/recipe and recompiled it as repair_02. Image generation evidence, GenerationRun, ReferenceAsset, final package, and publishing records remain blocked pending the repair human gate and new repair_02 execution + QA. p02-p14 handoffs remain blocked."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - workflow-d
  - workflow-f
  - workflow-g
  - ready
  - lint-passed
  - repair-02
  - visual-system-refactor
  - child-horror-notebook
  - needs-manual-regeneration
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p01 黄昏岔路口图像执行包 / The Fork at Dusk Image Execution Package

> The prior p01 manual WebGPTImage result failed and is not accepted. A visual-system refactor replaced the deprecated warm-safe base style with the child-drawn horror notebook system, re-pointed this package, and recompiled it as `repair_02`. This card is not a GenerationRun, ReferenceAsset, final package, publishing record, or image output. Image generation remains blocked at the repair human gate.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p01`
- Scene: [scene-fork-at-dusk](../40-scenes/scene-fork-at-dusk.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash: `58802ab763ac5dc6`
- Repair notes: `repair-pilot-001-p01-visual-system-refactor` (active); `repair-pilot-001-p01-webgptimage-style-species-drift` (superseded)

## Target Asset / 目标资产

Workflow F `repair_02` package plan for the p01 page illustration: the dusk road fork rendered as a child-drawn horror notebook page, with human-only character locks. Story direction is unchanged (re-skin only, per the repair human decision). No image asset is created by this card.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-fork-at-dusk`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required ReferenceAsset cards: none currently available or created.
- Blocking state: prior p01 manual candidate failed and must not be accepted or reused. The base visual system was refactored. Workflow F `repair_02` compile/lint passed against the new recipe. Workflow G `repair_02` manual handoff is prepared for p01 only; image generation remains blocked at the repair human gate.

## Allowed Content / 允许内容

- Dusk fork drawn as a child's notebook page: one bright familiar road and one darker unknown shortcut, with a wooden signpost readable only as an object (no legible words).
- Xiao He as a human child in a yellow hooded raincoat, red boots, and small round backpack; Mama as a human adult caregiver in a teal coat and scarf. Both drawn childishly (uneven proportions, wobbly lines) but unmistakably human.
- Lined school-notebook paper with creases, smudges, worn corners, and a faintly yellowed matte scanned look; rough pencil/ballpoint outlines, colored-pencil/crayon fill, and visible eraser marks.
- Red-pen circle, arrow, or question mark drawn on the dark shortcut, plus an optional short childish Chinese handwritten note/title (2–12 characters) as drawn content.
- Mild unease and curiosity; the child may look a little scared. Supernatural content is permitted by the visual system but not required for this mild establishing page.

## Forbidden Content / 禁止内容

- No polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, or perfectly clean vector line art.
- No 3D, cinematic realism, photorealism, oil painting, film-like lighting, or realistic crime-evidence photography.
- No animals replacing Xiao He or Mama; no hedgehogs, mice, rabbits, bears, dolls, plush-like humans, mascot characters, or anthropomorphic figures.
- No explicit gore, realistic corpses, real child abuse, severe child injury or visible trauma, sexual or adult content, or real-crime reproduction.
- No source names, source places, source wording, copied sequence packaging, channel identity, or recognizable horror motifs.
- No printed/typeset narration, captions, final prompt text, image IDs, UI artifacts, or WebGPTImage handoff text inside the source illustration. Childish hand-drawn notes/titles and red-pen marks are allowed as drawn content; a signpost may be visually readable only as an object, not legible words.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-child-horror-notebook` with verified `repair_02` `recipe_hash: 58802ab763ac5dc6`. Workflow F compiled this package into the referenced derived repair_02 prompt record; this card does not contain external execution prompt text.

## Workflow F Compile and Semantic Lint / Workflow F 编译与语义 Lint

- Compile result: `50-agent-work/story-lab/compiled-prompts/iep-pilot-001-p01-fork-at-dusk-repair_02.json`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/iep-pilot-001-p01-fork-at-dusk-repair_02.json`.
- Recipe hash comparison: `match` (`58802ab763ac5dc6`).
- Compile status: `pass`.
- Semantic lint status: `pass`.
- Package state: `ready` for the p01 `repair_02` handoff only; prior manual candidate failed and is not accepted.

## Workflow G Manual Handoff / Workflow G 人工交接

- Handoff record: `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/iep-pilot-001-p01-fork-at-dusk-repair_02.md`.
- Handoff status: `repair_02_manual_pending`.
- Scope: p01 only; p02-p14 are not released by this package update.
- WebGPTImage remains a manual external window action and is not authorized until the repair human gate approves the new visual system.
- No prior p01 candidate (original or warm-safe `repair_01` plan) may be accepted, uploaded, reused, or treated as a reference.
- No generated image file, GenerationRun, ReferenceAsset, final package, or publishing record is created by this package update.

## Reference Asset Binding / 参考资产绑定

`reference_assets`, `required_reference_assets`, and `prohibited_reference_assets` are empty because no accepted ReferenceAsset cards exist for `pilot-001` and none are required for this Workflow F repair_02 compile/lint pass. Future anchors must be accepted and explicitly bound before any package may depend on them.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output target: page illustration plan only.
- No generated image file, no raw output, and no accepted asset are created here.

## Generation Order / 生成顺序

Initial full-story order: 1 of 14. This order is planning metadata only and does not authorize generation.

## Manual Execution Instructions / 人工执行说明

Use only the controlled Workflow G `repair_02` handoff record listed above for p01 manual WebGPTImage execution, and only after the repair human gate approves the new visual system. Do not execute p02-p14 from this package. Do not use any prior p01 image as a reference. Image generation remains pending until a human operator manually uses the repair_02 handoff in WebGPTImage and records the required evidence.

## QA Acceptance Criteria / QA 验收标准

Later QA must confirm: human child and human mother only (no animal/mascot/plush/doll); Xiao He and Mama visual locks; child-drawn horror notebook aesthetic (lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen marks, childish proportions, matte scanned paper); creepy-but-child-drawn (not realistic horror, not gore); readable road choice; source-distance compliance; and no in-image platform/prompt/handoff text or legible sign words.

## Repair Triggers / 修复触发条件

Repair if Xiao He or Mama becomes animal-like, doll-like, plush-like, mascot-like, or anthropomorphic; if Xiao He's yellow raincoat/red boots/backpack or Mama's teal coat/scarf fail; if the image becomes polished digital, 3D, photoreal, oil painting, or cinematic; if it drifts into realistic gore or trauma; if in-image platform/prompt/handoff text or legible sign words appear; or if source-like identifiers appear.

## Result Backfill Procedure / 结果回填流程

No backfill now. After the repair human gate and after a human operator manually uses the p01 repair_02 handoff and records execution evidence, GenerationRun records must be created only through the relevant downstream workflow. ReferenceAsset creation remains blocked until QA passes; no failed candidate may ever become a ReferenceAsset.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

No R00, R01, or R02 dependency exists. The package must not imply a global style anchor or create reference assets.
