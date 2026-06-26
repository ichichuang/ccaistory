---
type: prompt_recipe
id: "pr-pilot-001-child-horror-notebook"
title_zh: pilot-001 儿童手绘怪谈作业本提示词配方
title_en: pilot-001 Child-Drawn Horror Notebook Prompt Recipe
status: draft
project_id: "pilot-001"
target_media: image
usable_for:
  - "child-drawn horror notebook illustration planning"
  - "future Workflow E image_execution_package binding"
  - "future Workflow F prompt compilation and semantic lint"
applicable_asset_types:
  - character
  - scene
  - image_execution_package
compatible_asset_types:
  - character
  - scene
  - visual_style
  - image_execution_package
recipe_hash: "58802ab763ac5dc6"
drift_check_policy: "recipe_hash = first 16 hex chars of sha256 over the UTF-8 text formed by joining with newlines, in document order, every line beginning with '- ' between the '## Allowed Content' and '## Dependency Rules' headers (i.e. the Allowed Content, Forbidden Content, and Negative Prompt Rules directives). Workflow F must recompute this from the reusable recipe payload, compare it with the stored recipe_hash, and block compilation on any mismatch or if concrete execution text, image_id binding, WebGPTImage handoff text, source-video identifiers, or hard content-safety violations (gore, sexual content, real child abuse, real-crime reproduction, in-image platform/prompt text) have been added. The check must NOT block merely because horror, supernatural, unexplained, ghost, or creepy content is present — those are allowed by this recipe."
related_assets: []
source_paths: []
tags:
  - story-lab
  - pilot-001
  - prompt-recipe
  - child-horror-notebook
  - supernatural-allowed
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 儿童手绘怪谈作业本提示词配方 / Child-Drawn Horror Notebook Prompt Recipe

> Visual-system refactor (2026-06-26). This card replaces the deprecated `pr-pilot-001-safe-night-picturebook`, which failed by enforcing over-safe, polished, animal-prone, no-horror output. Reusable recipe only. This card does not generate a concrete image, does not contain a WebGPTImage execution prompt, does not bind any single `image_id`, and must not be pasted into an image model as an execution sheet. Status remains `status: draft` (schema has no `accepted`/`active`); this refactor is **pending the repair human gate** and is not yet accepted in StoryProject `pilot-001`.

## Workflow D Gate / 工作流 D 门禁

Proposed recipe for the `pilot-001` D/F/G repair loop. Not yet accepted. Stored `recipe_hash` is recomputed for this new recipe as `58802ab763ac5dc6` (see Change Log); Workflow F must recompute and compare per `drift_check_policy`. Supersedes the deprecated `pr-pilot-001-safe-night-picturebook`.

## Purpose / 用途

Provide a reusable prompt structure for later Workflow E/F compilation of **child-drawn horror notebook** visuals for `pilot-001`. It keeps the look like a 9–12-year-old's scary-story notebook page — lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen circles, arrows, question marks, and childish Chinese handwriting — and **allows supernatural, unexplained, and creepy folk-tale content**. The fear must read as "a child's scary drawing," not realistic horror photography. Human characters stay human.

## Applicable Asset Types / 适用资产类型

- `character`: future character-anchor package drafting (human-only).
- `scene`: future scene illustration package drafting.
- `image_execution_package`: future package binding and compilation.

This recipe is not an execution package and is not tied to any page, shot, or `image_id`.

## Prompt Components / 提示词组件

Use these as reusable components during Workflow E/F only. Fill placeholders from approved canonical cards and package fields at compile time.

- Positive style core (bind verbatim): `Chinese child-drawn horror notebook page, lined school notebook paper, rough pencil and ballpoint outlines, colored-pencil and crayon fill, visible eraser marks, red pen circles and arrows, childish Chinese handwriting, uneven proportions, imperfect hand-drawn perspective, matte scanned paper texture, creepy but child-drawn, supernatural mystery atmosphere, one clear strange event on the page`.
- Negative style core (bind verbatim): `no polished digital illustration, no commercial picture book finish, no fantasy animal characters, no anthropomorphic hedgehogs, no plush mascots, no 3D, no cinematic realism, no oil painting, no photorealism, no glossy gradients, no perfectly clean line art, no cute fairy tale animal cast, no over-rendered AI storybook style, no platform text, no prompt text`.
- Subject component: `{{approved_characters_from_character_cards}}` with human-only identity; childish drawing is fine but identity must stay clear.
- Character anti-drift component: `human characters drawn as humans; a child may be drawn childishly/stick-figure-leaning but never as an animal, hedgehog, plush, doll, or mascot; keep clothing and human child/adult identity readable`.
- Scene component: `{{approved_scene_from_scene_card}}` rendered as one clear strange event on a notebook page.
- Horror/atmosphere component: `supernatural, spooky, unexplained or half-explained folk-tale mood allowed; dark gaps, a talking wardrobe, a night window, strange eyes, a blurry shadow, a sound from under the bed/desk or inside a cupboard; red-pen circles/arrows/question marks and a short childish Chinese handwritten title (2–12 chars) marking the anomaly`.
- Content-safety component: `creepy but child-drawn, not realistic horror photography; no explicit gore, no realistic corpse, no real child abuse, no severe child injury/trauma, no sexual or adult content, no real-crime reproduction`.
- Source-distance component: `original reconstruction; no source-video names, places, wording, sequence packaging, or recognizable horror imagery`.

## Allowed Content / allowed_content

- Lined school notebook or old worksheet paper background with creases, pressure marks, smudges, worn corners, faint yellowing, and a matte scanned-paper look.
- Rough black pencil and ballpoint outlines with colored-pencil and crayon fill, visible eraser marks, uneven childish proportions, and imperfect hand-drawn perspective.
- Red-pen circles, arrows, and question marks plus short childish Chinese handwriting (2–12 characters) marking the strange thing on the page.
- One clear strange event per page: a talking wardrobe, darkness inside a door gap, a window at night, a sound from under the desk or bed or inside the cupboard, a blurry shadow, strange eyes, or a circled anomaly.
- Supernatural, spooky, unexplained, or half-explained folk-tale atmosphere where the fear reads as a child's scary drawing rather than a realistic horror film.
- Human characters drawn as humans with clear identity: for pilot-001, Xiao He as a 6–7-year-old human child in a yellow hooded raincoat, red boots, and small round backpack, and Mama as a human adult caregiver in a teal coat and scarf; a child may look scared, trembling, or hiding by a lamp.

## Forbidden Content / forbidden_content

- Polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, or perfectly clean vector line art.
- 3D, cinematic realism, photorealism, oil painting, film-like lighting, or realistic crime-evidence photography.
- Fantasy animal characters, anthropomorphic hedgehogs, plush mascots, cute fairy-tale animal casts, dolls, or any animal replacing a human character.
- Over-safe, over-warm, over-rational basis that explains every strange thing away as an ordinary cause; treating "no supernatural" or "low fear" as a rule is itself forbidden.
- Explicit gore, realistic corpses, real child abuse, severe injury or visible trauma inflicted on a child, sexual or adult content, or real-crime-case reproduction.
- Source-video names, places, wording, packaging, recognizable horror imagery, copied sequence framing, or any platform UI, prompt text, image id, or WebGPTImage handoff text inside the image.

## Negative Prompt Rules / negative rules

Apply these as reusable negative rules in later compiled prompts. They intentionally do NOT include "no horror", "no supernatural", "no ghost", or "low fear":

- no polished digital illustration; no commercial picture book finish; no over-rendered AI storybook style; no glossy gradients; no perfectly clean line art
- no 3D; no cinematic realism; no photorealism; no oil painting; no film lighting; no realistic crime-scene photo look
- no fantasy animal characters; no anthropomorphic hedgehogs; no plush mascots; no cute fairy tale animal cast; no dolls; no animal replacing a human character
- no over-safe over-warm tone; no forced ordinary-cause explanation; do not add "no supernatural" or "low fear" as a rule
- no explicit gore; no realistic corpse; no real child abuse; no severe child injury or visible trauma; no sexual or adult content; no real-crime reproduction
- no source-video names, places, dialogue, packaging, or recognizable horror imagery; no platform UI, prompt text, image id, or WebGPTImage handoff text inside the image

## Dependency Rules / 依赖规则

- Must bind `vs-pilot-001-child-horror-notebook` as the visual style in any future package.
- Must draw character facts only from approved Character cards (human-only) and scene facts only from approved Scene cards.
- Must not invent ReferenceAsset dependencies. No reference assets are accepted; the failed warm-safe p01 candidate must never be used as a reference, anchor, or continuity dependency.
- Must not include actual WebGPTImage execution text, final per-image prompts, raw image outputs, or `image_id` bindings.

## Workflow E/F Compilation Placeholders / 后续编译预留位

Reserved for later workflows; do not fill in this card:

- `{{image_execution_package_id}}`
- `{{scene_id}}`
- `{{character_ids}}`
- `{{page_or_spread_range}}`
- `{{allowed_content_from_package}}`
- `{{forbidden_content_from_package}}`
- `{{reference_assets_after_acceptance}}`
- `{{compiled_prompt_output_path}}`
- `{{semantic_lint_result_path}}`

Workflow E may bind this recipe to an ImageExecutionPackage only after the refactor's repair human gate. Workflow F may compile and lint only after a valid package exists.

## QA Gates / QA 门禁

- Repair human gate: human review confirms the notebook-horror visual system, human-only characters, allowed supernatural content, hard content-safety lines, source-distance, and no execution prompt.
- Workflow E/F: future `compile-asset`, `lint-asset`, and `lint-prompt` must block if a hard content-safety violation appears (gore, sexual content, real child abuse, real-crime reproduction, in-image platform/prompt text), if recipe text is mixed with a concrete execution prompt, or if the recipe_hash mismatches. They must NOT block merely for horror/supernatural/creepy content.
- WebGPTImage remains blocked until a later G handoff from a ready, lint-passed package; this refactor authorizes only a p01 `repair_02` handoff pending human action.

## Repair Hooks / 修复钩子

- If the image looks like a polished AI storybook or commercial picture book: increase lined-paper texture, rough pencil/ballpoint, eraser marks, red-pen marks, and childish imperfection; remove glossy gradients and clean vector lines.
- If a human character becomes an animal, hedgehog, plush, doll, or mascot: restore an ordinary human child/adult drawn childishly, with the locked clothing from the Character cards, identity clearly readable.
- If the page becomes over-safe / over-warm / over-explained: restore the strange event, allow the supernatural/unexplained mood, and keep the red-pen anomaly marks; do not rewrite the scare into an ordinary cause.
- If it drifts toward realistic horror or gore: pull back to "child's scary drawing" — childish lines, crayon/colored-pencil, notebook paper — and remove any realistic blood, corpse, or trauma.
- If 3D / cinematic / photoreal creeps in: restore matte scanned hand-drawn paper.
- If source-derived imagery appears: remove names, locations, sequence packaging, and recognizable horror motifs; return to approved canonical cards.
- If any platform UI, prompt text, image id, or handoff text appears in the image: remove it.

## Change Log / 变更记录

- 2026-06-26: Created as the visual-system refactor recipe replacing the deprecated `pr-pilot-001-safe-night-picturebook`. Reframes the base direction from warm-safe picture book to child-drawn horror notebook; allows supernatural/unexplained content; keeps human-only character locks and hard content-safety lines. No image execution authorized.
- 2026-06-26: Computed a reproducible `recipe_hash` = `58802ab763ac5dc6` (sha256-short over the 18 Allowed/Forbidden/Negative directive lines) and documented the drift-check basis in `drift_check_policy`, including that horror/supernatural content must not trigger a block.
