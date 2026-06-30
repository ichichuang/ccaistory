---
type: image_execution_package
id: iep-pilot-001-p02-fading-lamp-lane
title_zh: pilot-001 p02 灯火渐稀小路图像执行包
title_en: pilot-001 p02 The Fading-Lamp Lane Image Execution Package
status: ready
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
recipe_hash: "267c7dfe258e43ba"
recipe_hash_expected: "267c7dfe258e43ba"
recipe_hash_actual: "267c7dfe258e43ba"
recipe_hash_check: pass
compile_result_ref: 50-agent-work/story-lab/compiled-prompts/compiled-prompt-pilot-001-p02-fading-lamp-lane.json
semantic_lint_result_ref: 50-agent-work/story-lab/semantic-lint-results/semantic-lint-pilot-001-p02-fading-lamp-lane.json
compile_status: pass
semantic_lint_status: pass
webgptimage_handoff_status: prepared
webgptimage_handoff_record_ref: 50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p02-fading-lamp-lane-gptimage.md
downstream_generation_status: qa_passed_reference_asset_acceptance_pending
blocked_reason: "Workflow I passed the p02 repair candidate. Workflow J ReferenceAsset Acceptance is pending; no p02 ReferenceAsset is accepted."
target_model: "GPTImage manual window (human-operated); not authorized for automated generation"
aspect_ratio: "1:1"
reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
required_reference_assets:
  - ra-pilot-001-r00-master-style-character-anchor
prohibited_reference_assets: []
allowed_content:
  - "The shortcut lane begins after the p01 choice: a single narrowing lane, not a fork or road split."
  - "Street lamps are spaced farther apart, with smaller warm pools of light and widening dark gaps between them."
  - "First low, thin mist appears close to the ground while trees draw closer along the lane edge."
  - "Xiao He and Mama walk together, staying human and keeping the accepted p01 visual appearance, clothing, and relative proportions."
  - "Gentle unease rises through the shrinking lamp light and mist; the page remains child-safe and quiet."
forbidden_content:
  - "No p01 fork scene, no road split, no choice-point composition, and no p01 signpost layout."
  - "No copying the p01 scene event; this page must show only the fading-lamp lane content from scene-fading-lamp-lane."
  - "No failed old p01 image, removed warm-safe visual system, animalized humans, plush/doll/mascot drift, or new characters."
  - "No explicit gore, realistic corpse, real child abuse, severe child injury or visible trauma, sexual/adult content, or real-crime reproduction."
  - "No platform UI, prompt text, image id, WebGPTImage handoff text, long body text, or legible signpost words inside a future image."
output_assets: []
candidate_image_paths:
  - 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png
generation_run_ids:
  - gr-pilot-001-p02-repair-01-20260630-154548-webgptimage
related_assets:
  - scene-fading-lamp-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
  - ra-pilot-001-r00-master-style-character-anchor
source_paths:
  - 02-wiki/story-lab/40-scenes/scene-fading-lamp-lane.md
  - 02-wiki/story-lab/reference-assets/ra-pilot-001-r00-master-style-character-anchor.md
last_run: gr-pilot-001-p02-repair-01-20260630-154548-webgptimage
qa_result: pass
image_review_form_ref: 50-agent-work/story-lab/image-review-forms/review-pilot-001-p02-candidate-repair-01-20260630-154548.json
asset_qa_result_ref: 50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md
r00_dependency_policy: "Use ra-pilot-001-r00-master-style-character-anchor only for notebook paper texture, rough child-drawn line quality, red-pen annotation language, scanned-paper material feeling, Xiao He and Mama visual appearance, and their relative proportions. Do not borrow the p01 fork scene, signpost layout, road split, or story event."
maximum_anchor_reuse_policy: "R00 reuse is allowed only for p02-p14 continuity through explicit required_reference_assets binding. Each page must keep its own Scene and ImageExecutionPackage content."
previous_page_reference: iep-pilot-001-p01-fork-at-dusk
previous_page_scene_summary: "Open dusk fork; familiar road vs darker shortcut; right path begins at the edge of trees."
current_page_scene_summary: "The chosen shortcut has become one narrowing lane with weaker lamp light, wider dark gaps, closer trees, and first low mist."
r00_reference_asset: ra-pilot-001-r00-master-style-character-anchor
continuity_from_previous_page:
  - "same paper / style / characters / proportions from R00"
  - "same darker right-hand shortcut continues"
  - "Xiao He and Mama remain together and human"
scene_delta_from_previous_page:
  - "fork disappears; road becomes one lane"
  - "light becomes weaker"
  - "trees move slightly closer"
  - "thin low mist begins"
allowed_progression_delta:
  - "slightly darker than p01"
  - "slightly quieter than p01"
  - "early shortcut edge, not deep forest"
forbidden_continuity_breaks:
  - "no dense forest tunnel"
  - "no multiple prominent road lamps"
  - "no sudden deep-night environment"
  - "no p01 signpost / fork composition"
page_hook_question: "The light is getting weaker; can they still see the way ahead?"
hook_visual_target: "dim gap ahead / weak lamp / low mist on the road"
hook_annotation_guidance: "Use a short childlike note such as 看不清？ or 灯少了."
escalation_level: "early p02 controlled unease; one step beyond p01, before deep wooded-lane intensity"
continuity_qa_required: true
hook_qa_required: true
dependency_notes: "Depends on scene-fading-lamp-lane, char-xiaohe, char-mama, vs-pilot-001-child-horror-notebook, pr-pilot-001-child-horror-notebook, and accepted R00 ReferenceAsset ra-pilot-001-r00-master-style-character-anchor."
blocking_notes: "Workflow I image QA passed for the p02 repair candidate. ReferenceAsset acceptance, final package, publishing records, and p03-p14 package creation remain blocked until separately authorized."
final_assembly_dependency: pilot-001
tags:
  - story-lab
  - pilot-001
  - image-execution-package
  - child-horror-notebook
  - p02
  - ready
  - r00-required
  - workflow-f-passed
  - generation-run-backfilled
  - qa-passed
  - workflow-i-passed
created_at: 2026-06-29
updated_at: 2026-06-30
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 p02 灯火渐稀小路图像执行包 / The Fading-Lamp Lane Image Execution Package

> Ready p02 ImageExecutionPackage after Workflow F compile and semantic lint. It binds the accepted R00 master visual reference for narrow continuity only. Workflow H backfilled one manual repair candidate; Workflow I image QA passed. This does not mark p02 accepted and does not create a ReferenceAsset, final package, or publishing record.

## Package Summary / 执行包概要

- Project: `pilot-001`
- Page: `p02`
- Scene: [scene-fading-lamp-lane](../40-scenes/scene-fading-lamp-lane.md)
- Characters: [char-xiaohe](../30-characters/char-xiaohe.md), [char-mama](../30-characters/char-mama.md)
- VisualStyle: [vs-pilot-001-child-horror-notebook](../50-visual-styles/vs-pilot-001-child-horror-notebook.md)
- PromptRecipe: [pr-pilot-001-child-horror-notebook](../60-prompts/pr-pilot-001-child-horror-notebook.md)
- Recipe hash: `267c7dfe258e43ba`
- Required R00 reference: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md)
- Package status: `ready`
- WebGPTImage handoff status: `prepared`
- WebGPTImage handoff record: `50-agent-work/story-lab/webgptimage-handoffs/pilot-001/handoff-pilot-001-p02-fading-lamp-lane-gptimage.md`
- Downstream generation status: `qa_passed_reference_asset_acceptance_pending`
- GenerationRun: `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`
- Candidate image: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`
- QA status: pass
- Image review form: `50-agent-work/story-lab/image-review-forms/review-pilot-001-p02-candidate-repair-01-20260630-154548.json`
- Asset QA result: `50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md`
- Compile result: `50-agent-work/story-lab/compiled-prompts/compiled-prompt-pilot-001-p02-fading-lamp-lane.json`
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/semantic-lint-pilot-001-p02-fading-lamp-lane.json`

## Target Asset / 目标资产

Planning card for the p02 page illustration. The page shows the shortcut lane beginning: lamps are farther apart, warm light pools shrink, first low mist appears, and Xiao He and Mama walk together while unease rises gently.

## Dependency Graph / 依赖图

- Required canonical cards: StoryProject `pilot-001`, Scene `scene-fading-lamp-lane`, Character cards `char-xiaohe` and `char-mama`, VisualStyle `vs-pilot-001-child-horror-notebook`, PromptRecipe `pr-pilot-001-child-horror-notebook`.
- Required ReferenceAsset: `ra-pilot-001-r00-master-style-character-anchor`.
- One p02 repair GenerationRun exists: `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`.
- Workflow I QA passed for the p02 repair candidate.
- No output ReferenceAsset exists for p02.

## Previous Page Continuity / 前页连续性

- Previous page: [iep-pilot-001-p01-fork-at-dusk](iep-pilot-001-p01-fork-at-dusk.md).
- Previous accepted image / master reference: [ra-pilot-001-r00-master-style-character-anchor](../reference-assets/ra-pilot-001-r00-master-style-character-anchor.md).
- Previous scene summary: open dusk fork; familiar road vs darker shortcut; the right path begins at the edge of trees.
- Current scene summary: the chosen shortcut has become one narrowing lane with weaker lamp light, wider dark gaps, closer trees, and first low mist.
- Must inherit: same paper, style, characters, proportions, and the already chosen darker shortcut direction.
- Must not inherit: p01 fork/signpost composition or choice-point event.

## Scene Delta From Previous Page / 相对前页的场景变化

- Fork disappears; road becomes one lane.
- Light becomes weaker.
- Trees move slightly closer.
- Thin low mist begins.

## Allowed Progression / 允许递进

- Slightly darker than p01.
- Slightly quieter than p01.
- Early shortcut edge only; not deep wooded-lane intensity.
- One controlled step stronger than the accepted p01 master image.

## Forbidden Continuity Breaks / 禁止连续性断裂

- No dense forest tunnel.
- No multiple prominent road lamps or lamp-lined road.
- No sudden deep-night environment.
- No p01 signpost / fork composition.
- No new characters, vehicles, buildings, or story props not required by this package.

## Page Hook / Page-Turn Question / 本页钩子与翻页问题

The light is getting weaker; can Xiao He and Mama still see the way ahead?

## Hook Annotation Guidance / 钩子标注指导

Point the red circle, arrow, or question mark at the dim gap ahead, the weak lamp, or the low mist on the road. Use one short childlike annotation such as `看不清？` or `灯少了`; do not place a random red mark away from the page uncertainty.

## Allowed Content / 允许内容

- A single narrowing shortcut lane that has begun after the p01 choice.
- Street lamps spaced farther apart, with shrinking warm pools of light and widening dark gaps.
- First low, thin mist near the ground; trees closer along the verge.
- Xiao He and Mama walking together, using the accepted R00 appearance and relative proportions.
- Mild, child-safe unease through composition, light spacing, and mist.

## Forbidden Content / 禁止内容

- No p01 fork scene, road split, choice-point layout, or p01 signpost layout.
- No copying the p01 event into p02; the scene content must stay the fading-lamp lane.
- No failed old p01 image or removed warm-safe visual system.
- No animalized Xiao He or Mama, plush/doll/mascot substitutions, new characters, cat, cottage, ghost payoff, or later-page events.
- No explicit gore, realistic corpse, real child abuse, severe injury, sexual/adult content, or real-crime evidence styling.

## Prompt Recipe Binding / Prompt 技法绑定

Bound to `pr-pilot-001-child-horror-notebook` with active `recipe_hash` `267c7dfe258e43ba`. Workflow F recomputed `recipe_hash_actual` as `267c7dfe258e43ba`; `recipe_hash_check`, `compile_status`, and `semantic_lint_status` are all `pass`. This card does not contain compiled prompt text and does not contain external-tool execution text.

## Reference Asset Binding / 参考资产绑定

`required_reference_assets` includes `ra-pilot-001-r00-master-style-character-anchor`. The R00 asset is used only for style, paper texture, line quality, red-pen annotation language, scanned-paper material feeling, Xiao He / Mama appearance, and relative proportions.

It must not transfer the p01 fork scene, p01 signpost layout, p01 road split, or p01 story event into p02.

## Canvas and Output Rules / 画布与输出规则

- Planned aspect ratio: `1:1`.
- Candidate image paths: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`.
- Output assets: none.
- Generation runs: `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`.

## Generation Order / 生成顺序

Initial full-story order: 2 of 14. This card is planning metadata only and does not authorize generation.

## Manual Execution Status / 人工执行状态

The p02 GPTImage handoff was executed manually outside Codex, and Workflow H backfilled one repair candidate. Codex did not generate a new image. Workflow I image QA passed, and no ReferenceAsset acceptance exists for p02.

## QA Acceptance Criteria / QA 验收标准

Workflow I QA verified the p02 scene content, R00 continuity, human-only Xiao He and Mama, child-safe mild unease, no p01 fork/signpost copy, no platform/prompt/handoff text inside the image, and no prohibited safety content.

## Continuity QA Criteria / 连续性 QA 标准

- R00 visual continuity passes for paper, line quality, coloring material, red-pen language, character appearance, and Xiao He / Mama height ratio.
- Previous-page scene continuity passes: p02 must feel like the chosen shortcut after p01, not a reset or a later deep-forest page.
- Environment progression stays controlled: only weaker light, slightly closer trees, and first low mist are introduced.
- Forbidden continuity breaks are absent.

## Hook QA Criteria / 钩子 QA 标准

- Candidate has one clear visual question around the weakening light and whether the path ahead is still visible.
- Red annotation points to the dim gap, weak lamp, or low mist.
- Annotation text is short, childlike, and page-specific.
- Generic mood-only labels do not pass.

## Repair Triggers / 修复触发条件

Repair or regenerate later if the generated p02 image copies the p01 fork/signpost layout, omits the fading lamp lane, jumps too quickly into dense/dark later-page intensity, adds unseeded infrastructure or new props, loses the R00 notebook material and character/proportion continuity, animalizes either human, uses a generic or misplaced hook annotation, introduces later-page events, or violates child-safety constraints.

## Result Backfill Procedure / 结果回填流程

The current repair candidate has been backfilled through Workflow H and passed Workflow I image QA. It must next be accepted or rejected through Workflow J. This package has no accepted ReferenceAsset.

## R00 Anchor Dependency Policy / R00 锚图依赖策略

The accepted R00 master visual reference is mandatory for future p02 generation, but its scope is narrow. It controls only visual continuity properties named in `r00_dependency_policy`; p02's location, event, props, and mood come from `scene-fading-lamp-lane` and this ImageExecutionPackage.
