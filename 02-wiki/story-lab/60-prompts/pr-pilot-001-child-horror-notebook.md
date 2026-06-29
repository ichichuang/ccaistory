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
recipe_hash: "267c7dfe258e43ba"
drift_check_policy: "recipe_hash = first 16 hex chars of sha256 over the UTF-8 text formed by joining with single newlines, in document order, every line beginning with '- ' between the '## Allowed Content' and '## Dependency Rules' headers (the Allowed Content, Forbidden Content, and Negative Prompt Rules directives), EXCLUDING any line containing a '{{...}}' placeholder and any line inside an 'Examples, not requirements' block. The basis is therefore the reusable, story-independent style / safety / supernatural-permission directives only; it deliberately does NOT include concrete package content (specific characters, scene, or page), the per-page strange-event placeholder, or the motif examples (which are illustrative, never mandatory story content). Workflow F must recompute this from the reusable recipe payload, compare it with the stored recipe_hash, and block compilation on any mismatch or if concrete execution text, image_id binding, WebGPTImage handoff text, source-video identifiers, or hard content-safety violations (gore, sexual content, real child abuse, real-crime reproduction, in-image platform/prompt text) have been added. The check must NOT block merely because horror, supernatural, unexplained, ghost, or creepy content is present — those are allowed by this recipe."
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

> Clean active PromptRecipe for `pilot-001` GPTImage production (visual pipeline reset 2026-06-26). Reusable, story-driven recipe only. This card does not generate a concrete image, does not contain a GPTImage execution prompt, does not bind any single `image_id`, and must not be pasted into an image model as an execution sheet. `status: draft` (schema has no `accepted`/`active`). An earlier warm-safe night-picture-book recipe was removed from the project and must not be bound.

## Production Gate / 生产门禁

Active reusable recipe for `pilot-001` clean GPTImage production-handoff preparation. Story-driven — motifs are examples only, never mandatory. The stored `recipe_hash` is `267c7dfe258e43ba`, the **only active recipe hash** for `pilot-001`; Workflow F must recompute and compare per `drift_check_policy`. Image generation stays manual and blocked until a human operator uses the clean GPTImage prompt.

## Purpose / 用途

Provide a reusable prompt structure for later Workflow E/F compilation of **child-drawn horror notebook** visuals for `pilot-001`. It keeps the look like a 9–12-year-old's scary-story notebook page — lined paper, rough pencil/ballpoint, colored-pencil/crayon, eraser marks, red-pen circles, arrows, question marks, and childish Chinese handwriting — and **allows supernatural, unexplained, and creepy folk-tale content**. The fear must read as "a child's scary drawing," not realistic horror photography. Human characters stay human.

## Applicable Asset Types / 适用资产类型

- `character`: future character-anchor package drafting (human-only).
- `scene`: future scene illustration package drafting.
- `image_execution_package`: future package binding and compilation.

This recipe is not an execution package and is not tied to any page, shot, or `image_id`.

## Prompt Components / 提示词组件

Use these as reusable components during Workflow E/F only. Each component's source is fixed below; fill placeholders from approved canonical cards and the bound package's fields at compile time. **Style is reusable; story content is variable** — the style/atmosphere/safety components never change per page, while the character, scene, and strange-event components are supplied by the approved cards and `ImageExecutionPackage`.

- **Style component (fixed)** — bind verbatim, identical on every page. Positive style core: `Chinese child-drawn horror notebook page, lined school notebook paper, rough pencil and ballpoint outlines, colored-pencil and crayon fill, visible eraser marks, red pen circles and arrows, childish Chinese handwriting, uneven proportions, imperfect hand-drawn perspective, matte scanned paper texture, creepy but child-drawn, supernatural mystery atmosphere, one clear strange event on the page`. Negative style core: `no polished digital illustration, no commercial picture book finish, no fantasy animal characters, no anthropomorphic hedgehogs, no plush mascots, no 3D, no cinematic realism, no oil painting, no photorealism, no glossy gradients, no perfectly clean line art, no cute fairy tale animal cast, no over-rendered AI storybook style, no platform text, no prompt text`.
- **Character component (from Character cards)** — `{{approved_characters_from_character_cards}}`, human-only identity; a child may be drawn childishly/stick-figure-leaning but never as an animal, hedgehog, plush, doll, or mascot; keep clothing and human child/adult identity readable. Character facts come only from the approved Character cards.
- **Scene component (from Scene card)** — `{{approved_scene_from_scene_card}}`: location, layout, time of day, and staging come only from the approved Scene card.
- **Story-specific strange event component (from ImageExecutionPackage allowed_content)** — `{{story_specific_strange_event_from_package}}` rendered in the child-drawn horror notebook style. The one strange event on the page comes only from the approved package's `allowed_content`; do not invent or inject any motif the package does not contain.
- **Annotation component** — red-pen circles, arrows, and question marks, plus a short childish handwritten Chinese note/title (2–12 chars), may highlight the package-specific anomaly or the point of uncertainty. Annotations may mark the event but must never replace the actual scene, and must not spell long legible sentences.
- **Content-safety component** — block explicit gore, realistic corpse, real child abuse, severe child injury/trauma, sexual or adult content, real-crime reproduction, and any in-image platform UI, prompt text, image IDs, or WebGPTImage handoff text. Always enforced.
- **Supernatural-permission component** — horror, supernatural, ghostly, strange, unexplained, or half-explained content is allowed whenever it is story/package-appropriate and must not be blocked merely for being supernatural. This permission never forces supernatural content; it only removes the old blanket ban.
- **Source-distance component** — `original reconstruction; no source-video names, places, wording, sequence packaging, or recognizable horror imagery`.

### Examples, not requirements / 示例，非必需

The motifs below are **examples of the visual language only** — they show the *kind* of strange event the style can render. They are **not** mandatory content and are **not** part of `recipe_hash`. **Do not add these examples to a compiled prompt unless they are present in the approved package or scene.**

- a talking wardrobe / 会说话的衣柜
- darkness inside a door gap / 门缝里的黑暗
- a window at night / 夜里的窗户
- strange eyes / 奇怪的眼睛
- a blurry ghost shadow / 模糊的鬼影
- a sound from under the desk or bed or inside a cupboard / 桌下、床下或柜子里的声音
- a red-pen circled anomaly / 红笔圈出的异常处

The compiled scene event must instead come from `{{story_specific_strange_event_from_package}}`; these examples must never become a fixed checklist, and a page may contain none of them.

## Allowed Content / allowed_content

The directives below are the reusable, story-independent drawing-method, atmosphere, and safety/permission envelope. The single strange event itself is NOT fixed here — it is supplied per page by the approved package (see the story-specific strange event component). The placeholder line (containing `{{ }}`) and any "Examples, not requirements" motif are illustrative and are excluded from `recipe_hash`.

- Lined school notebook or old worksheet paper background with creases, pressure marks, smudges, worn corners, faint yellowing, and a matte scanned-paper look.
- Rough black pencil and ballpoint outlines with colored-pencil and crayon fill, visible eraser marks, uneven childish proportions, and imperfect hand-drawn perspective.
- Red-pen circles, arrows, and question marks plus short childish Chinese handwriting (2–12 characters) marking the package-specific strange thing, never replacing the scene and never spelling long legible sentences.
- One clear strange event per page, supplied only by the approved package: `{{story_specific_strange_event_from_package}}` rendered in the child-drawn horror notebook style; the recipe itself fixes no specific motif.
- Supernatural, spooky, unexplained, or half-explained folk-tale atmosphere is allowed where story/package-appropriate, with the fear reading as a child's scary drawing rather than a realistic horror film; supernatural content must not be blocked merely for being supernatural.
- Human characters drawn as humans with clear identity taken only from the approved Character cards; childish, stick-figure-leaning drawing is fine but identity must stay readable and must never become an animal, hedgehog, plush, doll, or mascot.

## Forbidden Content / forbidden_content

- Polished digital illustration, commercial picture-book finish, over-rendered AI storybook style, glossy gradients, or perfectly clean vector line art.
- 3D, cinematic realism, photorealism, oil painting, film-like lighting, or realistic crime-evidence photography.
- Fantasy animal characters, anthropomorphic hedgehogs, plush mascots, cute fairy-tale animal casts, dolls, or any animal replacing a human character.
- Over-safe, over-warm, over-rational basis that explains every strange thing away as an ordinary cause; treating "no supernatural" or "low fear" as a rule is itself forbidden.
- Explicit gore, realistic corpses, real child abuse, severe injury or visible trauma inflicted on a child, sexual or adult content, or real-crime-case reproduction.
- Source-video names, places, wording, packaging, recognizable horror imagery, copied sequence framing, or any platform UI, prompt text, image id, or WebGPTImage handoff text inside the image.
- Injecting any example motif from the recipe's "Examples, not requirements" list when it is not present in the approved package or scene; those example motifs are illustrative only and are never mandatory content.

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
- Must not invent ReferenceAsset dependencies. No reference assets are accepted; the failed earlier p01 candidate must never be used as a reference, anchor, or continuity dependency.
- Must not include actual WebGPTImage execution text, final per-image prompts, raw image outputs, or `image_id` bindings.

## Series Continuity Prefix / 系列连贯前缀

Reusable master-reference prefix for **serialized production**: prepend this to every **later page's** compiled prompt (p02 onward) and upload the **accepted p01 master image** as the reference, so style, character design, proportions, and page language stay locked to the master while only the scene event changes. Use it only once a genuinely accepted p01 image exists — a failed or unaccepted candidate must never be the master. This is operational continuity language and is **not** part of `recipe_hash`. The page's own strange event still comes from that page's `ImageExecutionPackage` `allowed_content`.

```
Use the uploaded image as the MASTER REFERENCE for style, character design, proportions, and page language. Match it exactly.

Keep the same child-drawn horror notebook look on lined school-notebook paper; the same rough pencil and ballpoint line quality with colored-pencil and crayon fill and visible eraser marks; the same uneven childish proportions and imperfect hand-drawn perspective; the same red-pen annotation language (red circles, arrows, and question marks, plus an optional short childish Chinese handwritten note marking this page's anomaly, never replacing the scene); the same matte scanned-paper texture with creases, smudges, and worn corners; and the same 1:1 square format.

Keep the characters identical to the master. Xiao He is a human child in a buttercup-yellow hooded raincoat, red rubber boots, and a small round backpack, with short dark hair and the proportions of a six-to-seven-year-old child. Mama is a human adult caregiver in a teal coat and a soft scarf, with medium-length dark hair and adult proportions, clearly taller than Xiao He. Do not redesign them, do not change their clothing or palette, and never turn them into an animal, hedgehog, plush, doll, mascot, or anthropomorphic figure. Keep their relative height and body proportions the same as the master on every page, and keep the same gentle, childlike emotional rendering (childlike fear, unease, curiosity, relief — never realistic trauma).

Only the scene event changes for this page: {{story_specific_strange_event_from_package}}, taken from the approved ImageExecutionPackage and Scene card. Render that one event in the master's style. Do not change the style, paper, materials, line quality, red-pen language, proportions, or character design. Do not add any platform UI, prompt text, image id, caption, watermark, or readable sign words inside the image. No polished digital illustration, no 3D, no photorealism, no animalized humans, no anthropomorphic hedgehogs, no plush mascots, no explicit gore, no sexual content, no real-crime imagery.
```

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
- GPTImage remains blocked until a human operator manually uses a clean p01 GPTImage handoff built from a ready, lint-passed package; this card authorizes no automated image generation, GenerationRun, ReferenceAsset, or final package.

## Repair Hooks / 修复钩子

- If the image looks like a polished AI storybook or commercial picture book: increase lined-paper texture, rough pencil/ballpoint, eraser marks, red-pen marks, and childish imperfection; remove glossy gradients and clean vector lines.
- If a human character becomes an animal, hedgehog, plush, doll, or mascot: restore an ordinary human child/adult drawn childishly, with the locked clothing from the Character cards, identity clearly readable.
- If the page becomes over-safe / over-warm / over-explained: restore the strange event, allow the supernatural/unexplained mood, and keep the red-pen anomaly marks; do not rewrite the scare into an ordinary cause.
- If it drifts toward realistic horror or gore: pull back to "child's scary drawing" — childish lines, crayon/colored-pencil, notebook paper — and remove any realistic blood, corpse, or trauma.
- If 3D / cinematic / photoreal creeps in: restore matte scanned hand-drawn paper.
- If source-derived imagery appears: remove names, locations, sequence packaging, and recognizable horror motifs; return to approved canonical cards.
- If any platform UI, prompt text, image id, or handoff text appears in the image: remove it.

## Change Log / 变更记录

- 2026-06-26 (visual pipeline reset): Established as the single clean, reusable, **story-driven** PromptRecipe for `pilot-001` GPTImage production. The earlier warm-safe night-picture-book recipe and all of its intermediate recipe hashes were removed from the active pipeline. Components: fixed style / character (from Character cards) / scene (from Scene card) / story-specific strange event (from `ImageExecutionPackage` `allowed_content`) / annotation / content-safety / supernatural-permission / source-distance. The fixed motif list was replaced by `{{story_specific_strange_event_from_package}}`; motifs are kept only in an "Examples, not requirements" block and are excluded from `recipe_hash`. Active `recipe_hash` = `267c7dfe258e43ba` (sha256-short over the 18 reusable Allowed/Forbidden/Negative directive lines, excluding the `{{ }}` placeholder line and the example motifs). No image execution authorized.
