---
type: image_execution_package
id: iep-pilot-001-p01-fork-at-dusk
title_zh: pilot-001 p01 黄昏岔路口图像执行包
title_en: pilot-001 p01 The Fork at Dusk Image Execution Package
status: draft
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
recipe_hash: "267c7dfe258e43ba"
recipe_hash_expected: "267c7dfe258e43ba"
recipe_hash_actual: ""
recipe_hash_check: ""
compile_result_ref: ""
semantic_lint_result_ref: ""
compile_status: ""
semantic_lint_status: ""
webgptimage_handoff_status: manual_candidate_generated
downstream_generation_status: reference_asset_accepted
blocked_reason: "Workflow J accepted the p01 ReferenceAsset. Later-page generation, final package, and publishing records remain blocked until p02-p14 packages are recreated and validated."
target_model: "GPTImage manual window (human-operated); not authorized for automated generation"
aspect_ratio: "1:1"
reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
required_reference_assets: []
prohibited_reference_assets: []
allowed_content:
  - "Dusk fork in the road drawn as a child's notebook page: a familiar bright road versus a darker unknown shortcut, with a wooden signpost readable only as an object (no legible words)."
  - "Xiao He as a human child (yellow hooded raincoat, red boots, small round backpack) and Mama as a human adult caregiver (teal coat, scarf), drawn childishly but unmistakably human."
  - "Lined school-notebook paper with creases and a matte scanned look; rough pencil/ballpoint outlines, colored-pencil/crayon fill, visible eraser marks; a red-pen circle, arrow, or question mark may mark the darker shortcut or the point of uncertainty; an optional short childish Chinese handwritten note (2-12 chars) may be used only if this page calls for it."
forbidden_content:
  - "Hard content-safety: no explicit gore, no realistic corpse, no real child abuse, no severe child injury or trauma, no sexual or adult content, no real-crime reproduction."
  - "No animals replacing Xiao He or Mama; no hedgehogs, mice, rabbits, bears, dolls, plush-like humans, mascots, or anthropomorphic figures."
  - "No polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, clean vector line art, 3D, cinematic realism, photorealism, or oil painting."
  - "No legible signpost words; no platform UI, prompt text, image id, or GPTImage handoff text inside the image; no source names, places, wording, or recognizable source imagery."
output_assets:
  - ra-pilot-001-r00-master-style-character-anchor
candidate_image_paths:
  - 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png
generation_run_ids:
  - gr-pilot-001-p01-20260626-172625-webgptimage
related_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - scene-fork-at-dusk
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
source_paths:
  - 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png
last_run: gr-pilot-001-p01-20260626-172625-webgptimage
qa_result: pass
image_review_form_ref: 50-agent-work/story-lab/image-review-forms/review-pilot-001-p01-candidate-20260626-172625.json
asset_qa_result_ref: 50-agent-work/story-lab/qa-results/qa-pilot-001-p01-candidate-20260626-172625.md
r00_dependency_policy: "Workflow J accepted ra-pilot-001-r00-master-style-character-anchor as the p01 R00 master visual reference. Future packages may borrow only its narrow style, paper, red-pen annotation, character appearance, and proportion properties through explicit ReferenceAsset dependency declarations."
maximum_anchor_reuse_policy: "Reuse is limited to p02-p14 continuity. Do not copy the p01 fork scene, story event, prop layout, or unrelated motifs into later pages unless the downstream ImageExecutionPackage requires them."
dependency_notes: "Depends on accepted Workflow A-C canonical cards (StoryProject, Scene, Character), the clean VisualStyle/PromptRecipe, and the accepted p01 ReferenceAsset output ra-pilot-001-r00-master-style-character-anchor."
blocking_notes: "Workflow J ReferenceAsset acceptance is complete. Later-page generation, final package, and publishing records remain blocked until p02-p14 packages are recreated, compiled/linted, generated, QAed, and accepted."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - child-horror-notebook
  - draft
  - clean-reset
  - generation-run-backfilled
  - qa-passed
  - workflow-j-accepted
  - reference-asset-accepted
created_at: 2026-06-26
updated_at: 2026-06-29
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p01 黄昏岔路口图像执行包 / The Fork at Dusk Image Execution Package

> Fresh `draft` package created in the 2026-06-26 visual pipeline reset. It binds the clean child-drawn horror notebook VisualStyle and PromptRecipe. Workflow H backfilled one manual WebGPTImage / GPTImage candidate and GenerationRun. Workflow I QA passed, and Workflow J accepted the candidate as the p01 ReferenceAsset `ra-pilot-001-r00-master-style-character-anchor`.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p01`
- Scene: [scene-fork-at-dusk](../40-scenes/scene-fork-at-dusk.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash: `267c7dfe258e43ba` (the only active recipe hash for `pilot-001`)
- GenerationRun: `gr-pilot-001-p01-20260626-172625-webgptimage`
- Candidate image: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png`
- QA status: pass
- QA evidence: `50-agent-work/story-lab/qa-results/qa-pilot-001-p01-candidate-20260626-172625.md`
- Accepted ReferenceAsset: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md)

## Series Master Anchor / 系列主锚

**p01 is the designated series master anchor.** In this serialized picture book, style, character, and proportion consistency are mandatory across all pages. Workflow J accepted the p01 image as the **master visual reference** for every later page (p02-p14): later pages upload it as the master reference and inherit its notebook-paper style, line quality, red-pen language, matte texture, square format, character design, and proportions. Only the page-specific scene event changes (see the project card's "Series Continuity & Master Anchor" section and the recipe's "Series Continuity Prefix").

- Current state: Workflow J accepted [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md). The R00 / series master visual anchor is active for future p02-p14 package recreation.
- Scope: the anchor controls only notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He / Mama visual appearance, and their relative proportions. It does not control future story events or force later pages to copy the p01 fork scene.

## Target Asset / 目标资产

Draft package plan for the p01 page illustration: the dusk road fork rendered as a child-drawn horror notebook page, with human-only character locks. Story direction is the dusk fork scene (re-skin only). One candidate image path is recorded for QA, and Workflow J accepted it as `ra-pilot-001-r00-master-style-character-anchor`.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-fork-at-dusk`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Accepted ReferenceAsset output: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md)
- State: fresh draft with one manual candidate backfilled, Workflow I QA passed, and Workflow J ReferenceAsset acceptance complete. p02-p14 packages are still deleted and must be recreated later.

## Allowed Content / 允许内容

- Dusk fork drawn as a child's notebook page: one bright familiar road and one darker unknown shortcut, with a wooden signpost readable only as an object (no legible words).
- Xiao He as a human child in a yellow hooded raincoat, red boots, and small round backpack; Mama as a human adult caregiver in a teal coat and scarf. Both drawn childishly (uneven proportions, wobbly lines) but unmistakably human.
- Lined school-notebook paper with creases, smudges, worn corners, and a faintly yellowed matte scanned look; rough pencil/ballpoint outlines, colored-pencil/crayon fill, and visible eraser marks.
- A red-pen circle, arrow, or question mark may mark the darker shortcut or the point of uncertainty; an optional short childish Chinese handwritten note/title (2-12 chars) may be used only if this page calls for it.
- Mild unease and curiosity; the child may look a little scared. The strange event/atmosphere for this page comes from this package only — no wardrobe, door gap, ghost shadow, or other example motif is injected.

## Forbidden Content / 禁止内容

- No explicit gore, realistic corpse, real child abuse, severe child injury or visible trauma, sexual or adult content, or real-crime reproduction.
- No animals replacing Xiao He or Mama; no hedgehogs, mice, rabbits, bears, dolls, plush-like humans, mascot characters, or anthropomorphic figures.
- No polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, clean vector line art, 3D, cinematic realism, photorealism, oil painting, or film-like lighting.
- No legible signpost words; no platform UI, prompt text, image id, or GPTImage handoff text inside the image; no source names, places, wording, or recognizable source imagery.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-child-horror-notebook` (active `recipe_hash` `267c7dfe258e43ba`). This card holds no compiled prompt text and no external execution prompt. Compilation and semantic lint are downstream (Workflow F) and have not been run for this fresh draft.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1` (square image).
- Output target: page illustration plan only.
- Candidate image path: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p01-fork-at-dusk/pilot-001-p01-candidate-20260626-172625.png`.
- `output_assets` records `ra-pilot-001-r00-master-style-character-anchor` as the accepted p01 ReferenceAsset output.

## Generation Order / 生成顺序

Initial full-story order: 1 of 14. Planning metadata only; does not authorize generation.

## Manual Execution Notes / 人工执行说明

Image generation was performed manually in WebGPTImage / GPTImage for this candidate and backfilled through Workflow H. Workflow J acceptance is complete. This card does not authorize automated generation, p02 start, or later-page generation.

## QA Acceptance Criteria / QA 验收标准

Workflow I QA confirmed: human child and human mother only (no animal/mascot/plush/doll); Xiao He and Mama visual locks; child-drawn horror notebook aesthetic (lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen marks, childish proportions, matte scanned paper); readable bright-vs-dark road choice; source-distance compliance; and no in-image platform/prompt/handoff text or legible sign words.

## Reference Asset Binding / 参考资产绑定

`reference_assets` includes the accepted p01 ReferenceAsset `ra-pilot-001-r00-master-style-character-anchor`. `required_reference_assets` and `prohibited_reference_assets` remain empty for this p01 source package. Future p02-p14 packages must explicitly bind this ReferenceAsset before using it as the master visual reference.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

The accepted p01 ReferenceAsset is the active R00 / series master visual reference. Its reuse is narrow: paper texture, rough line quality, red-pen annotation language, scanned-paper feeling, Xiao He / Mama appearance, and their relative proportions. It must not make later pages copy the p01 fork scene or bypass each page's own ImageExecutionPackage.
