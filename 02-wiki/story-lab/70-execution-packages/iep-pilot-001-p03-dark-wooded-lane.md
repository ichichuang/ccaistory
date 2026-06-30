---
type: image_execution_package
id: iep-pilot-001-p03-dark-wooded-lane
title_zh: pilot-001 p03 黑黑的林间小路图像执行包
title_en: pilot-001 p03 The Dark Wooded Lane Image Execution Package
status: ready
project_id: pilot-001
scene_id: scene-dark-wooded-lane
page_or_spread_range: p03
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
recipe_hash_actual: "267c7dfe258e43ba"
recipe_hash_check: pass
compile_result_ref: 50-agent-work/story-lab/compiled-prompts/compiled-prompt-pilot-001-p03-dark-wooded-lane.json
semantic_lint_result_ref: 50-agent-work/story-lab/semantic-lint-results/semantic-lint-pilot-001-p03-dark-wooded-lane.json
compile_status: pass
semantic_lint_status: pass
webgptimage_handoff_status: prepared
webgptimage_handoff_record_ref: 50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p03-dark-wooded-lane-gptimage.md
downstream_generation_status: reference_asset_accepted
blocked_reason: "Workflow J accepted the p03 page-level ReferenceAsset. p04-p14 package creation, later-page generation, final package, and publishing records remain blocked until separately authorized."
target_model: "GPTImage manual window (human-operated); not authorized for automated generation"
aspect_ratio: "1:1"
reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p02-fading-lamp-lane
required_reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p02-fading-lamp-lane
prohibited_reference_assets: []
allowed_content:
  - "The same single shortcut lane continues from p02."
  - "The lane becomes darker and more enclosed than p02, but only as the next controlled step."
  - "Trees lean closer over the lane."
  - "Thin mist and slight cold breath-fog may appear."
  - "Xiao He and Mama walk close together, using the accepted R00 appearance and relative proportions."
  - "One first scare clue may appear: two tiny dim reflective eyes hidden low in the right-side bushes or shadow beside the lane."
  - "The eyes stay small, dim, integrated, and partly hidden, raising the page-turn question of whether something is watching from the bushes."
forbidden_content:
  - "No full monster, visible scary face, cat reveal, cottage, Lantern Grandpa, or later-page payoff."
  - "No pale drifting shape unless a later authorized p03 graph update assigns it to p03."
  - "No hollow pipe, wind moan, or sound scare unless a later authorized p03 graph update assigns it to p03."
  - "No multiple scares packed into one image and no deep horror climax."
  - "No p01 fork scene, p01 signpost layout, p02 fading-lamp composition copy, or replacement of R00 with p02."
  - "No explicit gore, realistic corpse, real child abuse, severe injury, sexual/adult content, or real-crime imagery."
  - "No platform UI, prompt text, image id, GPTImage handoff text, or long body text inside a future image."
output_assets:
  - ra-pilot-001-p03-dark-wooded-lane
candidate_image_paths:
  - 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p03-dark-wooded-lane/pilot-001-p03-candidate-20260630-205406.png
generation_run_ids:
  - gr-pilot-001-p03-20260630-205406-webgptimage
related_assets:
  - scene-dark-wooded-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p02-fading-lamp-lane
  - ra-pilot-001-p03-dark-wooded-lane
source_paths:
  - 02-wiki/story-lab/40-scenes/scene-dark-wooded-lane.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-r00-master-style-character-anchor.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-p02-fading-lamp-lane.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-p03-dark-wooded-lane.md
last_run: gr-pilot-001-p03-20260630-205406-webgptimage
qa_result: pass
image_review_form_ref: 50-agent-work/story-lab/image-review-forms/review-pilot-001-p03-candidate-20260630-205406.json
asset_qa_result_ref: 50-agent-work/story-lab/qa-results/qa-pilot-001-p03-candidate-20260630-205406.md
r00_dependency_policy: "Use ra-pilot-001-r00-master-style-character-anchor only for global visual continuity: notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He and Mama design, and their relative proportions. Do not borrow the p01 fork scene, signpost layout, road split, or story event."
maximum_anchor_reuse_policy: "R00 reuse is allowed only for p02-p14 continuity through explicit required_reference_assets binding. Each page must keep its own Scene and ImageExecutionPackage content. The p02 page-level ReferenceAsset may guide only p03 previous-page scene continuity and must not replace R00."
previous_page_reference: iep-pilot-001-p02-fading-lamp-lane
previous_page_scene_summary: "Single shortcut lane after the fork; weaker light, wider dark gaps, first low mist, trees slightly closer."
current_page_scene_summary: "The shortcut continues into a darker wooded lane; trees lean closer, mist and cold breath-fog increase, and two tiny dim reflective eyes hide low in the right-side bushes or shadow beside the lane."
r00_reference_asset: ra-pilot-001-r00-master-style-character-anchor
previous_page_reference_asset: ra-pilot-001-p02-fading-lamp-lane
continuity_from_previous_page:
  - "same single shortcut lane continues from p02"
  - "same Xiao He and Mama appearance and proportions from R00"
  - "same child-drawn notebook page language"
  - "mist and weak light continue from p02"
scene_delta_from_previous_page:
  - "trees lean closer over the lane"
  - "mist and cold feeling increase slightly"
  - "first ambiguous scare clue appears: two tiny dim reflective eyes hidden low in the right-side bushes"
allowed_progression_delta:
  - "darker than p02"
  - "more enclosed than p02, but still not full fear peak"
  - "introduce only one first scare clue"
forbidden_continuity_breaks:
  - "no sudden monster face"
  - "no cat reveal"
  - "no cottage or Lantern Grandpa"
  - "no multiple simultaneous scare clues"
  - "no p01 fork or p02 fading-lamp composition copy"
page_hook_question: "Are those two tiny low lights in the bushes eyes?"
hook_visual_target: "two tiny dim reflective eyes hidden low in the right-side bushes or shadow beside the lane"
hook_annotation_guidance: "Use one short childlike note such as 是眼睛？; red circle or arrow should point to the hidden eyes, not random darkness."
hook_failure_mode_to_avoid:
  - "eyes read as street lamps, bulbs, or fixed artificial lights"
  - "eyes become too bright, centered, symmetrical, or dominant"
  - "eye repair turns the scene into a much denser or darker later-page forest"
symbol_semantics_target: "two tiny dim reflective eyes from a hidden living presence low in the right-side bushes"
symbol_misread_to_avoid: "street lamps, bulbs, fixed light sources, or decorative dots"
repair_guardrails:
  - "clarify the hidden-eye clue without enlarging the right-side dark mass"
  - "preserve p02 lane continuity, open sky, and readable path"
  - "do not add cat reveal, monster face, cottage, helper, or multiple scare clues"
progression_budget_from_previous_page: "Only one controlled step beyond p02: slightly darker, slightly quieter, slightly more enclosed, while preserving path readability and some dusk sky."
overcorrection_guardrail: "Do not darken, densify, or enclose the environment so much that previous-page continuity breaks."
composition_priority_order:
  - "first read: the same path continues deeper after p02"
  - "second read: the hidden-eye clue is discovered in the right-side bushes"
escalation_level: "p03 first gentle scare clue; one step beyond p02, before p04-p06 peak and calming turn"
continuity_qa_required: true
hook_qa_required: true
dependency_notes: "Depends on scene-dark-wooded-lane, char-xiaohe, char-mama, vs-pilot-001-child-horror-notebook, pr-pilot-001-child-horror-notebook, accepted R00 ReferenceAsset ra-pilot-001-r00-master-style-character-anchor, and accepted previous-page ReferenceAsset ra-pilot-001-p02-fading-lamp-lane."
blocking_notes: "Workflow J accepted the p03 page-level ReferenceAsset. p04-p14 package creation, later-page generation, final package, and publishing records remain blocked until separately authorized."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - child-horror-notebook
  - p03
  - ready
  - r00-required
  - previous-page-reference-required
  - continuity-hook-required
  - workflow-f-passed
  - webgptimage-handoff-prepared
  - generation-run-backfilled
  - qa-passed
  - workflow-i-passed
  - workflow-j-accepted
  - reference-asset-accepted
created_at: 2026-06-30
updated_at: 2026-06-30
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p03 黑黑的林间小路图像执行包 / The Dark Wooded Lane Image Execution Package

> Ready p03 ImageExecutionPackage after Workflow F compile and semantic lint. It binds the accepted R00 master visual reference for global style, character, and proportion continuity, plus the accepted p02 page-level ReferenceAsset for immediate previous-page scene continuity. Workflow H backfilled one manual candidate, Workflow I image QA passed, and Workflow J accepted the p03 page-level ReferenceAsset `ra-pilot-001-p03-dark-wooded-lane`. This does not create p04-p14 packages, a final package, or publishing records.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p03`
- Scene: [scene-dark-wooded-lane](../40-scenes/scene-dark-wooded-lane.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash: `267c7dfe258e43ba`
- Required R00 reference: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md)
- Required previous-page reference: [ra-pilot-001-p02-fading-lamp-lane](../reference-assets/ra-pilot-001-p02-fading-lamp-lane.md)
- Package status: `ready`
- WebGPTImage handoff status: `prepared`
- WebGPTImage handoff record: `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p03-dark-wooded-lane-gptimage.md`
- Downstream generation status: `reference_asset_accepted`
- GenerationRun: `gr-pilot-001-p03-20260630-205406-webgptimage`
- Candidate image: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p03-dark-wooded-lane/pilot-001-p03-candidate-20260630-205406.png`
- QA status: pass
- Image review form: `50-agent-work/story-lab/image-review-forms/review-pilot-001-p03-candidate-20260630-205406.json`
- Asset QA result: `50-agent-work/story-lab/qa-results/qa-pilot-001-p03-candidate-20260630-205406.md`
- Accepted ReferenceAsset: [ra-pilot-001-p03-dark-wooded-lane](../reference-assets/ra-pilot-001-p03-dark-wooded-lane.md)
- Compile result: `50-agent-work/story-lab/compiled-prompts/compiled-prompt-pilot-001-p03-dark-wooded-lane.json`
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/semantic-lint-pilot-001-p03-dark-wooded-lane.json`
- Next workflow: p04 package creation later, when separately authorized

## Target Asset / 目标资产

Planning and acceptance card for the p03 page illustration. The page begins the darker wooded-lane sequence: the same shortcut continues from p02, trees lean closer, mist and slight breath-fog increase, and two tiny dim reflective eyes hidden low in the right-side bushes create the first gentle scare clue.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-dark-wooded-lane`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required R00 ReferenceAsset: `ra-pilot-001-r00-master-style-character-anchor`.
- Required previous-page ReferenceAsset: `ra-pilot-001-p02-fading-lamp-lane`.
- p03 GenerationRun exists: `gr-pilot-001-p03-20260630-205406-webgptimage`.
- Workflow I QA passed for the p03 candidate.
- Workflow J accepted page-level ReferenceAsset `ra-pilot-001-p03-dark-wooded-lane`.
- No final package, publishing record, or p04-p14 package exists.

## Previous Page Continuity / 前页连续性

- Previous page package: [iep-pilot-001-p02-fading-lamp-lane](iep-pilot-001-p02-fading-lamp-lane.md).
- Previous accepted page reference: [ra-pilot-001-p02-fading-lamp-lane](../reference-assets/ra-pilot-001-p02-fading-lamp-lane.md).
- Previous scene summary: single shortcut lane after the fork; weaker light, wider dark gaps, first low mist, trees slightly closer.
- Current scene summary: the shortcut continues into a darker wooded lane; trees lean closer, mist and cold breath-fog increase, and two tiny dim reflective eyes hide low in the right-side bushes or shadow beside the lane.
- Must inherit from R00: notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He / Mama design, and relative proportions.
- Must inherit from p02: the lane has already become a single path, light is weaker, first mist exists, and trees have begun to move closer.
- Must not inherit: p01 fork/signpost composition, p02 composition copy, or p02 as a global style anchor.

## Scene Delta From Previous Page / 相对前页的场景变化

- Trees lean closer over the lane.
- Mist and cold feeling increase slightly.
- First ambiguous scare clue appears: two tiny dim reflective eyes hidden low in the right-side bushes.

## Allowed Progression / 允许递进

- Darker than p02.
- More enclosed than p02, but still not the full fear peak.
- Introduce only one first scare clue.
- Keep p03 as the first step into the darker wooded-lane sequence, before the p04-p06 peak and calming turn.

## Forbidden Continuity Breaks / 禁止连续性断裂

- No sudden monster face.
- No cat reveal.
- No cottage or Lantern Grandpa.
- No multiple simultaneous scare clues.
- No p01 fork or p02 fading-lamp composition copy.
- No replacement of R00 with p02.

## Page Hook / Page-Turn Question / 本页钩子与翻页问题

Are those two tiny low lights in the bushes eyes?

## Hook Annotation Guidance / 钩子标注指导

Point the red circle and arrow at the two tiny dim reflective eyes hidden low in the right-side bushes or shadow beside the lane. Use one short childlike note such as `是眼睛？`; do not make the eyes into a clear face, cat reveal, lamp, or centered composition.

## Allowed Content / 允许内容

- The same single shortcut lane continues from p02.
- The lane is darker and more enclosed than p02, but only as the next controlled step.
- Trees lean closer over the lane.
- Thin mist and slight cold breath-fog may appear.
- Xiao He and Mama walk close together, staying human and keeping the accepted R00 appearance, clothing, and relative proportions.
- Two tiny dim reflective eyes may appear low in the right-side bushes or shadow beside the lane as one ambiguous first scare clue.
- Gentle, child-safe unease rises through the darker lane, closer trees, mist, breath-fog, and one distant uncertainty.

## Forbidden Content / 禁止内容

- No full monster, visible scary face, cat reveal, cottage, Lantern Grandpa, or later-page payoff.
- No pale drifting shape unless a later authorized p03 graph update assigns it to p03.
- No hollow pipe, wind moan, or sound scare unless a later authorized p03 graph update assigns it to p03.
- No multiple scares packed into one image and no deep horror climax.
- No copying the p01 fork/signpost event or the p02 fading-lamp composition.
- No failed old p01 image, removed warm-safe visual system, animalized humans, plush/doll/mascot drift, or new characters.
- No explicit gore, realistic corpse, real child abuse, severe injury, sexual/adult content, real-crime imagery, platform UI, prompt text, image id, GPTImage handoff text, or long body text inside a future image.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-child-horror-notebook` with active `recipe_hash` `267c7dfe258e43ba`. Workflow F recomputed `recipe_hash_actual` as `267c7dfe258e43ba`; `recipe_hash_check`, `compile_status`, and `semantic_lint_status` are all `pass`. This card does not contain compiled prompt text and does not contain external-tool execution text.

## Reference Asset Binding / 参考资产绑定

`required_reference_assets` includes both `ra-pilot-001-r00-master-style-character-anchor` and `ra-pilot-001-p02-fading-lamp-lane`.

R00 controls only global visual continuity: paper texture, line quality, red-pen annotation language, Xiao He / Mama design, and proportions. It must not transfer the p01 fork scene, p01 signpost layout, p01 road split, or p01 story event into p03.

The p02 ReferenceAsset controls only previous-page scene continuity: the lane has already become a single path, light is weaker, first mist exists, and trees have begun to move closer. It is not a global style anchor and must not replace R00.

Workflow J accepted `ra-pilot-001-p03-dark-wooded-lane` as this package's page-level output ReferenceAsset. It is not R00 and must not replace `ra-pilot-001-r00-master-style-character-anchor`. It may be used later only as the immediate previous-page continuity reference for p04.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output assets: `ra-pilot-001-p03-dark-wooded-lane`.
- Candidate image paths: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p03-dark-wooded-lane/pilot-001-p03-candidate-20260630-205406.png`.
- Generation runs: `gr-pilot-001-p03-20260630-205406-webgptimage`.

## Generation Order / 生成顺序

Initial full-story order: 3 of 14. This card records the accepted p03 page-level result only and does not authorize p04-p14 generation.

## Manual Execution Status / 人工执行状态

The p03 GPTImage handoff was prepared at `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p03-dark-wooded-lane-gptimage.md`. The actual prompt sent differed from the prepared handoff; exact prompt provenance was supplied by the user and recorded in `50-agent-work/story-lab/runs/gr-pilot-001-p03-20260630-205406-webgptimage.md`. Codex did not generate a new image. Workflow H backfilled the manual candidate, Workflow I QA passed, and Workflow J accepted the p03 page-level ReferenceAsset.

## QA Acceptance Criteria / QA 验收标准

Workflow I QA verified that p03 preserves R00 visual and character continuity, uses p02 only as immediate previous-page scene continuity, keeps the scene to the approved first dark-wooded-lane step, includes only the tiny hidden-eye clue as the first scare clue, avoids eye/lamp ambiguity, avoids overcorrection into a later deep-forest page, and avoids all forbidden later-page reveals and safety violations.

## Continuity QA Criteria / 连续性 QA 标准

- R00 visual continuity passes for paper, line quality, coloring material, red-pen language, character appearance, and Xiao He / Mama height ratio.
- Previous-page scene continuity passes: p03 continues from p02's single shortcut lane, weaker light, first mist, and slightly closer trees.
- Environment progression stays controlled: only closer trees, slightly more mist/cold, and two tiny low hidden eyes are introduced.
- Forbidden continuity breaks are absent.

## Hook QA Criteria / 钩子 QA 标准

- Candidate has one clear visual question around the two tiny hidden eyes in the right-side bushes.
- The eyes read as possible eyes, not lamps, bulbs, or fixed artificial lights.
- Red annotation points to the eyes, not to a random part of the lane.
- Annotation text is short, childlike, and page-specific.
- The clue remains integrated into the environment and does not dominate the whole composition.
- The eyes remain ambiguous and tiny, not a monster face or cat reveal.

## Repair Triggers / 修复触发条件

Repair or regenerate later if the generated p03 image copies the p02 composition, drops the single-lane continuity, jumps to a deep horror climax, makes the eyes read as lamps, enlarges the right-side dark mass until it dominates the page, shows a monster/face/cat/cottage/helper, packs in the pipe sound or pale drifting shape without authorization, loses R00 notebook material or character/proportion continuity, animalizes either human, uses a generic or misplaced hook annotation, creates a ReferenceAsset without acceptance, or violates child-safety constraints.

## Result Backfill Procedure / 结果回填流程

Workflow F compile and semantic lint records are written under `50-agent-work`. Workflow H backfilled the manual candidate GenerationRun, Workflow I QA passed, and Workflow J accepted the page-level ReferenceAsset. Later workflows must separately authorize p04 package creation and any later generation.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

The accepted R00 master visual reference is mandatory for p03 continuity, but its scope is narrow. It controls only visual continuity properties named in `r00_dependency_policy`; p03's location, event, props, hook, and allowed scare clue come from `scene-dark-wooded-lane`, the previous p02 scene continuity reference, and this ImageExecutionPackage.
