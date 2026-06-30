---
type: image_execution_package
id: iep-pilot-001-p04-low-moan-lane
title_zh: pilot-001 p04 低低声音的小路图像执行包
title_en: pilot-001 p04 The Low Moan Lane Image Execution Package
status: draft
project_id: pilot-001
scene_id: scene-dark-wooded-lane
page_or_spread_range: p04
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
webgptimage_handoff_status: ""
webgptimage_handoff_record_ref: ""
downstream_generation_status: blocked
blocked_reason: "p04 is a draft-only ImageExecutionPackage. Workflow F compile and semantic lint are the next authorized step; GPTImage handoff, generation, GenerationRun, ReferenceAsset creation, final package, and publishing records remain blocked."
target_model: "GPTImage manual window (human-operated); p04 generation not authorized at draft stage"
aspect_ratio: "1:1"
reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p03-dark-wooded-lane
required_reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p03-dark-wooded-lane
prohibited_reference_assets: []
allowed_content:
  - "The same single shortcut lane continues from p03."
  - "Xiao He and Mama continue walking close together."
  - "The two eye dots from p03 are gone or no longer the focus."
  - "The lane is a little darker and colder than p03, but still a controlled next step."
  - "Trees lean close, but the page must not become a full fear climax."
  - "A low moaning sound seems to come from just off the lane."
  - "The sound may be shown through childlike wavy sound lines, shaky marks, or red annotation."
  - "A small dark hollow pipe or old fence-pipe shape may be partly visible near the edge of the lane as an ambiguous clue, but do not explain it yet."
  - "The page-turn question is: What is making that low sound?"
forbidden_content:
  - "No cat reveal."
  - "No glowing eyes as the main hook."
  - "No full monster or visible scary face."
  - "No cottage or Lantern Grandpa."
  - "No pale drifting shape unless the Story Graph explicitly assigns it to p04."
  - "No multiple simultaneous scare clues."
  - "No deep horror climax."
  - "No explanation that the sound is wind in a pipe."
  - "No p01 fork, signpost, exact p02 composition copy, or exact p03 composition copy."
  - "No new characters."
  - "No gore, corpse, real child abuse, severe injury, sexual content, or real-crime imagery."
  - "No platform UI, prompt text, image id, or GPTImage handoff text inside a future image."
output_assets: []
candidate_image_paths: []
generation_run_ids: []
related_assets:
  - scene-dark-wooded-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
  - ra-pilot-001-r00-master-style-character-anchor
  - ra-pilot-001-p03-dark-wooded-lane
source_paths:
  - 02-wiki/story-lab/40-scenes/scene-dark-wooded-lane.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-r00-master-style-character-anchor.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-p03-dark-wooded-lane.md
last_run: ""
qa_result: ""
image_review_form_ref: ""
asset_qa_result_ref: ""
r00_dependency_policy: "Use ra-pilot-001-r00-master-style-character-anchor only for global visual continuity: notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He and Mama design, and their relative proportions. Do not borrow the p01 fork scene, signpost layout, road split, or story event."
maximum_anchor_reuse_policy: "R00 reuse is allowed only for p02-p14 continuity through explicit required_reference_assets binding. Each page must keep its own Scene and ImageExecutionPackage content. The p03 page-level ReferenceAsset may guide only p04 previous-page scene continuity and must not replace R00."
previous_page_reference: iep-pilot-001-p03-dark-wooded-lane
previous_page_scene_summary: "The dark wooded lane continues from p02; trees lean closer, mist and cold feeling increase, and two tiny hidden reflective eyes appear low in the bushes."
current_page_scene_summary: "The same dark lane continues; the eye clue is no longer the focus, and a low moaning sound seems to come from just off the lane near a partly hidden hollow fence-pipe or dark roadside object."
r00_reference_asset: ra-pilot-001-r00-master-style-character-anchor
previous_page_reference_asset: ra-pilot-001-p03-dark-wooded-lane
continuity_from_previous_page:
  - "same dark wooded shortcut lane continues from p03"
  - "same Xiao He and Mama appearance and proportions from R00"
  - "same child-drawn notebook page language"
  - "same mist, close trees, and cold feeling continue from p03"
scene_delta_from_previous_page:
  - "hidden-eye clue recedes and is not the main focus"
  - "a low sound / moan becomes the new page clue"
  - "a small ambiguous hollow pipe or dark roadside object may appear off the lane"
  - "sound is represented by subtle childlike wavy marks or red annotation"
allowed_progression_delta:
  - "slightly more uneasy than p03"
  - "introduce only one new clue: the low sound"
  - "keep the scene before full fear peak"
forbidden_continuity_breaks:
  - "no cat reveal"
  - "no repeated eye-centered hook"
  - "no visible monster or face"
  - "no cottage or Lantern Grandpa"
  - "no pale drifting shape if not assigned to p04"
  - "no explanation of the sound source"
  - "no multiple simultaneous scares"
page_hook_question: "What is making that low sound?"
hook_visual_target: "subtle wavy sound marks or a red circle near the dark roadside pipe / hollow object area"
hook_annotation_guidance: "Use one short childlike note such as 谁在响？ or 声音呢？; red mark should point to the sound clue, not random darkness."
hook_failure_mode_to_avoid:
  - "sound clue becomes a visible monster"
  - "sound clue becomes music / singing / human voice"
  - "page repeats the p03 eye hook instead of introducing the sound hook"
symbol_semantics_target: "unseen low moaning sound from an ambiguous roadside object, later explainable as wind in a hollow fence-pipe"
symbol_misread_to_avoid: "monster voice / ghost face / human singer / obvious explanation / repeated glowing eyes"
repair_guardrails:
  - "do not over-darken or densify the lane beyond p03"
  - "do not reveal the ordinary cause yet"
  - "do not add multiple scares"
progression_budget_from_previous_page: "one controlled step beyond p03: eye clue fades from focus, low sound clue begins"
overcorrection_guardrail: "Do not make the sound clue so dramatic that it becomes a horror climax or breaks the quiet child-safe mystery tone."
composition_priority_order:
  - "first read: same wooded lane continues from p03"
  - "second read: Xiao He and Mama notice a low sound"
  - "third read: red annotation points toward the sound clue"
escalation_level: "p04 second gentle scare clue; after p03 hidden eyes, before pale shape and before p06 calming turn"
continuity_qa_required: true
hook_qa_required: true
dependency_notes: "Depends on scene-dark-wooded-lane, char-xiaohe, char-mama, vs-pilot-001-child-horror-notebook, pr-pilot-001-child-horror-notebook, accepted R00 ReferenceAsset ra-pilot-001-r00-master-style-character-anchor, and accepted previous-page ReferenceAsset ra-pilot-001-p03-dark-wooded-lane."
blocking_notes: "p04 generation remains blocked. Next workflow is p04 Workflow F compile and semantic lint; no handoff, image generation, GenerationRun, ReferenceAsset, final package, or publishing record is created by this draft package."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - child-horror-notebook
  - p04
  - draft
  - r00-required
  - previous-page-reference-required
  - continuity-hook-required
  - generation-blocked
created_at: 2026-06-30
updated_at: 2026-06-30
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p04 低低声音的小路图像执行包 / The Low Moan Lane Image Execution Package

> Draft-only p04 ImageExecutionPackage. It binds the accepted R00 master visual reference for global style, character, and proportion continuity, plus the accepted p03 page-level ReferenceAsset for immediate previous-page scene continuity. No compile, semantic lint, handoff, image generation, GenerationRun, ReferenceAsset, final package, or publishing record is created here.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p04`
- Scene: [scene-dark-wooded-lane](../40-scenes/scene-dark-wooded-lane.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash: `267c7dfe258e43ba`
- Required R00 reference: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md)
- Required previous-page reference: [ra-pilot-001-p03-dark-wooded-lane](../reference-assets/ra-pilot-001-p03-dark-wooded-lane.md)
- Package status: `draft`
- Downstream generation status: `blocked`
- Next workflow: p04 Workflow F compile + semantic lint

## Target Asset / 目标资产

Draft planning card for the p04 page illustration. The page is the second gentle scare clue after p03: the same dark wooded shortcut lane continues, Xiao He and Mama stay close together, the earlier eye clue recedes, and a low moaning sound seems to come from just off the lane near a partly hidden hollow fence-pipe or dark roadside object.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-dark-wooded-lane`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required R00 ReferenceAsset: `ra-pilot-001-r00-master-style-character-anchor`.
- Required previous-page ReferenceAsset: `ra-pilot-001-p03-dark-wooded-lane`.
- No p04 compile result, semantic lint result, handoff, candidate image, GenerationRun, ReferenceAsset, final package, or publishing record exists.

## Previous Page Continuity / 前页连续性

- Previous page package: [iep-pilot-001-p03-dark-wooded-lane](iep-pilot-001-p03-dark-wooded-lane.md).
- Previous accepted page reference: [ra-pilot-001-p03-dark-wooded-lane](../reference-assets/ra-pilot-001-p03-dark-wooded-lane.md).
- Previous scene summary: the dark wooded lane continues from p02; trees lean closer, mist and cold feeling increase, and two tiny hidden reflective eyes appear low in the bushes.
- Current scene summary: the same dark lane continues; the eye clue is no longer the focus, and a low moaning sound seems to come from just off the lane near a partly hidden hollow fence-pipe or dark roadside object.
- Must inherit from R00: notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He / Mama design, and relative proportions.
- Must inherit from p03: same dark wooded shortcut lane, close trees, mist, and cold feeling.
- Must not inherit: p03 as global style anchor, p03 hidden eyes as the main hook, exact p03 composition, or p01 fork/signpost content.

## Scene Delta From Previous Page / 相对前页的场景变化

- Hidden-eye clue recedes and is not the main focus.
- A low sound / moan becomes the new page clue.
- A small ambiguous hollow pipe or dark roadside object may appear off the lane.
- Sound is represented by subtle childlike wavy marks or red annotation.

## Allowed Progression / 允许递进

- Slightly more uneasy than p03.
- Introduce only one new clue: the low sound.
- Keep the scene before the full fear peak.
- Trees may lean close, but the page must stay in the quiet child-safe mystery tone.

## Forbidden Continuity Breaks / 禁止连续性断裂

- No cat reveal.
- No repeated eye-centered hook.
- No visible monster or face.
- No cottage or Lantern Grandpa.
- No pale drifting shape if not assigned to p04.
- No explanation of the sound source.
- No multiple simultaneous scares.

## Page Hook / Page-Turn Question / 本页钩子与翻页问题

What is making that low sound?

## Hook Annotation Guidance / 钩子标注指导

Use one short childlike note such as `谁在响？` or `声音呢？`. The red mark should point toward the sound clue near the dark roadside pipe or hollow object area, not to random darkness.

## Hook Semantics and Repair Guardrails / 钩子语义与返修护栏

- Hook failure modes to avoid: sound clue becomes a visible monster; sound clue becomes music, singing, or a human voice; page repeats the p03 eye hook instead of introducing the sound hook.
- Symbol semantics target: unseen low moaning sound from an ambiguous roadside object, later explainable as wind in a hollow fence-pipe.
- Symbol misread to avoid: monster voice, ghost face, human singer, obvious explanation, or repeated glowing eyes.
- Repair guardrails: do not over-darken or densify the lane beyond p03; do not reveal the ordinary cause yet; do not add multiple scares.
- Progression budget: one controlled step beyond p03, with the eye clue fading from focus and the low sound clue beginning.
- Overcorrection guardrail: do not make the sound clue so dramatic that it becomes a horror climax or breaks the quiet child-safe mystery tone.
- Composition priority order: first read the same wooded lane continuing from p03; second read Xiao He and Mama noticing a low sound; third read the red annotation pointing toward the sound clue.

## Allowed Content / 允许内容

- The same single shortcut lane continues from p03.
- Xiao He and Mama continue walking close together, staying human and keeping the accepted R00 appearance, clothing, and relative proportions.
- The two eye dots from p03 are gone or no longer the focus.
- The lane is a little darker and colder than p03, but still a controlled next step.
- Trees lean close, but the page must not become a full fear climax.
- A low moaning sound seems to come from just off the lane.
- The sound may be shown through childlike wavy sound lines, shaky marks, or red annotation.
- A small dark hollow pipe or old fence-pipe shape may be partly visible near the edge of the lane as an ambiguous clue, but do not explain it yet.

## Forbidden Content / 禁止内容

- No cat reveal.
- No glowing eyes as the main hook.
- No full monster or visible scary face.
- No cottage or Lantern Grandpa.
- No pale drifting shape unless the Story Graph explicitly assigns it to p04.
- No multiple simultaneous scare clues.
- No deep horror climax.
- No explanation that the sound is wind in a pipe.
- No p01 fork, signpost, exact p02 composition copy, or exact p03 composition copy.
- No new characters.
- No failed old p01 image, removed warm-safe visual system, animalized humans, plush/doll/mascot drift, or new characters.
- No explicit gore, realistic corpse, real child abuse, severe injury, sexual/adult content, real-crime imagery, platform UI, prompt text, image id, or GPTImage handoff text inside a future image.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-child-horror-notebook` with active `recipe_hash` `267c7dfe258e43ba`. Workflow F has not been run for this draft. This card does not contain compiled prompt text and does not contain external-tool execution text.

## Reference Asset Binding / 参考资产绑定

`required_reference_assets` includes both `ra-pilot-001-r00-master-style-character-anchor` and `ra-pilot-001-p03-dark-wooded-lane`.

R00 controls only global visual continuity: paper texture, rough child-drawn line quality, red-pen annotation language, Xiao He / Mama design, and proportions. It must not transfer the p01 fork scene, p01 signpost layout, p01 road split, or p01 story event into p04.

The p03 ReferenceAsset controls only previous-page scene continuity: the same dark wooded lane continues, trees are close, thin mist and cold feeling continue, and the first eye clue has just happened. It is not a global style anchor and must not replace R00.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Output assets: none at draft stage.
- Candidate image paths: none.
- Generation runs: none.

## Generation Order / 生成顺序

Initial full-story order: 4 of 14. This card is a draft package only and does not authorize image generation.

## Manual Execution Status / 人工执行状态

No handoff has been created for p04, and no manual or automated image generation is authorized by this draft. The next workflow is p04 Workflow F compile and semantic lint.

## QA Acceptance Criteria / QA 验收标准

When a later workflow authorizes QA, p04 must preserve R00 visual and character continuity, use p03 only as immediate previous-page scene continuity, keep the scene to the approved second gentle scare clue, introduce only the low sound hook, avoid repeating the p03 eye hook, avoid all forbidden later-page reveals and safety violations, and keep the ordinary cause unexplained.

## Continuity QA Criteria / 连续性 QA 标准

- R00 visual continuity must pass for paper, line quality, coloring material, red-pen language, character appearance, and Xiao He / Mama height ratio.
- Previous-page scene continuity must pass: p04 continues from p03's dark wooded lane, close trees, mist, and cold feeling.
- Environment progression stays controlled: only the eye clue fading and the low sound clue beginning are introduced.
- Forbidden continuity breaks are absent.

## Hook QA Criteria / 钩子 QA 标准

- Candidate has one clear visual question around the low sound.
- The sound clue reads as an unseen low moaning sound, not a visible monster, ghost face, singer, or obvious explanation.
- Red annotation points toward the sound clue near the dark roadside pipe or hollow object area.
- Annotation text is short, childlike, and page-specific.
- The clue remains subtle and integrated into the lane.

## Repair Triggers / 修复触发条件

Repair or regenerate later if a generated p04 image repeats the p03 eye hook, shows a monster/face/cat/cottage/helper, introduces the pale drifting shape without authorization, explains the sound source too early, packs in multiple scare clues, loses R00 notebook material or character/proportion continuity, animalizes either human, uses a generic or misplaced hook annotation, creates a ReferenceAsset without acceptance, or violates child-safety constraints.

## Result Backfill Procedure / 结果回填流程

No result backfill is authorized by this draft. Later workflows must separately authorize compile/lint, handoff, manual generation, run backfill, image QA, and ReferenceAsset acceptance in that order.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

The accepted R00 master visual reference is mandatory for p04 continuity, but its scope is narrow. It controls only visual continuity properties named in `r00_dependency_policy`; p04's location, event, prop clue, hook, and allowed scare clue come from `scene-dark-wooded-lane`, the previous p03 scene continuity reference, and this ImageExecutionPackage.
