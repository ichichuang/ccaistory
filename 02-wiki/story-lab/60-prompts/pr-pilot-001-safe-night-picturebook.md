---
type: prompt_recipe
id: "pr-pilot-001-safe-night-picturebook"
title_zh: pilot-001 儿童安全夜路图文书提示词配方
title_en: pilot-001 Child-Safe Night Picture Book Prompt Recipe
status: deprecated
project_id: "pilot-001"
target_media: image
usable_for:
  - "children-safe picture-book illustration planning"
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
recipe_hash: "62b75f8590685a10"
drift_check_policy: "recipe_hash = first 16 hex chars of sha256 over the UTF-8 text formed by joining with newlines, in document order, every line beginning with '- ' between the 'Allowed Content' and 'Dependency Rules' headers (i.e. the Allowed Content, Forbidden Content, and Negative Prompt Rules directives). Workflow F must recompute this from the reusable recipe payload, compare it with the stored recipe_hash, and block compilation on any mismatch or if concrete execution text, image_id binding, WebGPTImage handoff text, source-video identifiers, or forbidden content has been added."
related_assets: []
source_paths: []
tags:
  - story-lab
  - pilot-001
  - prompt-recipe
  - children-safe
  - deprecated
  - superseded
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 儿童安全夜路图文书提示词配方 / Child-Safe Night Picture Book Prompt Recipe

> ⛔ DEPRECATED (2026-06-26 visual-system refactor). Superseded by [pr-pilot-001-child-horror-notebook](./pr-pilot-001-child-horror-notebook.md). This recipe enforced over-safe, polished, animal-prone, no-horror output and is no longer bound by any `pilot-001` package. Kept for history only. Reusable recipe only; it does not generate a concrete image, does not contain a WebGPTImage execution prompt, and binds no `image_id`.

## Deprecation / 弃用

- Status: `deprecated`. Superseded by `pr-pilot-001-child-horror-notebook` (current recipe_hash `267c7dfe258e43ba`, consistency-refined from `58802ab763ac5dc6`).
- Reason: over-safe / polished digital / animalized humans / no horror; its global "no horror / no supernatural / low fear" negative rules and "rounded friendly shapes" wording biased the model toward a cute commercial picture book.
- All `pilot-001` execution packages have been re-pointed to the new recipe. The stale `recipe_hash` values below (`62b75f8590685a10` / `6020fc5e5c83e043`) are historical only.

## Workflow D Gate / 工作流 D 门禁 (historical)

This PromptRecipe was previously accepted for `pilot-001` through the StoryProject gate record; the historical hardened `recipe_hash` was `62b75f8590685a10`. That acceptance is now superseded by the visual-system refactor.

## Purpose / 用途

Provide a reusable prompt structure for later Workflow E/F compilation of child-safe picture-book visuals for `pilot-001`. It keeps the visual direction warm, gentle, low-fear, and source-distant while preserving ordinary natural explanations for night, wind, mist, and reflected cat eyes.

## Applicable Asset Types / 适用资产类型

- `character`: future character-anchor package drafting.
- `scene`: future scene illustration package drafting.
- `image_execution_package`: future package binding and compilation.

This recipe is not an execution package and is not tied to any page, shot, or `image_id`.

## Prompt Components / 提示词组件

Use these as reusable components during Workflow E/F only. Fill placeholders from approved canonical cards and package fields at compile time.

- Visual style component: `children-safe illustrated picture book; soft watercolor, gouache, and colored-pencil texture; warm lantern amber against readable blue-violet night; rounded friendly shapes; low-fear mood`.
- Visual anti-drift component: `hand-made matte paper finish; visible pencil sketch marks, colored-pencil grain, watercolor blooms, gouache opacity, and small imperfect hand-drawn linework; not polished digital fantasy or cinematic lighting`.
- Subject component: `{{approved_characters_from_character_cards}}` with human-only identity, locked clothing, proportions, and expressions.
- Character anti-drift component: `Xiao He is a human child about six or seven in a buttercup-yellow hooded raincoat, red rubber boots, and small round backpack; Mama is a human adult caregiver in a teal coat and soft scarf; never animals, dolls, plush figures, mascots, or anthropomorphic substitutes`.
- Scene component: `{{approved_scene_from_scene_card}}` with ordinary natural causes visible or foreshadowed.
- Safety component: `mild, reassuring tension only; safe caregiver proximity; warm helper cues; no traumatic fear`.
- Explanation component: `darkness, wind, mist, and reflected eyes are ordinary natural phenomena; no magic or supernatural cause`.
- Source-distance component: `original reconstruction; no source-video names, places, wording, sequence packaging, or recognizable horror imagery`.

## Allowed Content / allowed_content

- Warm, soft, children-safe picture-book night scenes.
- Readable darkness with lantern light, window glow, road light, and gentle mist.
- Human Xiao He: a 6-7-year-old child with buttercup-yellow hooded raincoat, red rubber boots, and small round backpack.
- Human Mama: adult caregiver with teal coat, soft scarf, calm presence, and visible caregiver proximity.
- Hand-made tactile matte paper finish with visible pencil, colored-pencil, watercolor, and gouache traces.
- Xiao He showing mild, comfort-seeking nervousness that can be soothed.
- Mama as calm and reassuring.
- Lantern Grandpa as warm, safe, trustworthy, and welcoming.
- Tangerine the Cat as friendly; eye shine only from lantern-light reflection.
- Wind, cold air, mist, and darkness explained through ordinary natural causes.
- Cozy cottage, safe road, hand-holding, steady breathing, asking for help, and relief.

## Forbidden Content / forbidden_content

- Horror, realistic thriller, jump-scare staging, monsters, ghost faces, gore, blood, crime, adult content, or sexualized content.
- Religious punishment, superstition-as-threat, occult symbols, magic, possession, curses, or supernatural explanations.
- Terrified, traumatized, hysterical, abandoned, or endangered-child imagery.
- Lantern Grandpa rendered as eerie, sinister, ambiguous, predatory, uncanny, or magical.
- Cat eyes rendered as magical glow, demonic eyes, possession, or supernatural signal.
- Mist, trees, windows, or shadows forming faces, bodies, ghosts, monsters, or threatening figures.
- Source-video names, places, wording, expressions, plot packaging, channel identity, or identifiable horror motifs.
- Animals replacing human characters, including hedgehogs, mice, rabbits, bears, cute animals, mascot characters, dolls, plush-like humans, or anthropomorphic figures.
- Polished digital fantasy illustration, cinematic lighting, glossy over-rendered AI storybook finish, or cute-animal fairytale look.

## Negative Prompt Rules / negative rules

Apply these as reusable negative rules in later compiled prompts:

- no horror; no realistic thriller; no jump scare; no monster; no ghost; no ghost face; no gore; no blood; no corpse; no crime scene; no weapon threat
- no adult content; no sexualized content; no religious punishment; no occult ritual; no curse; no possession; no supernatural payoff
- no terrifying panic; no traumatic crying; no abandoned child; no uncanny adult; no sinister old man; no menacing cat; no magical glowing eyes
- no faces in mist; no faces in trees; no faces in windows; no threatening shadow figure; no hidden monster silhouette
- no copied source-video names, places, dialogue, narrator phrasing, scene packaging, or recognizable horror imagery
- no animals replacing people; no hedgehog child; no hedgehog mother; no mouse, rabbit, bear, cute animal, mascot, doll, plush-like human, or anthropomorphic character replacing Xiao He or Mama
- no polished digital fantasy illustration; no cinematic lighting; no glossy over-rendered AI storybook finish; no cute-animal fairytale look

## Dependency Rules / 依赖规则

- Must bind `vs-pilot-001-warm-safe-night-picturebook` as the visual style in any future package.
- Must draw character facts only from approved Character cards and scene facts only from approved Scene cards.
- Must not invent ReferenceAsset dependencies. Reference assets remain unavailable until accepted by the later ReferenceAsset workflow.
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

Workflow E may bind this recipe to an ImageExecutionPackage only after Workflow D human approval. Workflow F may compile and lint only after a valid package exists.

## QA Gates / QA 门禁

- Workflow D: human review confirms reusable recipe only, source-distance, child safety, and no execution prompt.
- Workflow E/F: future `compile-asset`, `lint-asset`, and `lint-prompt` must block if forbidden content appears or if recipe text is mixed with a concrete execution prompt.
- WebGPTImage remains blocked until a later G handoff from a ready, lint-passed package.

## Repair Hooks / 修复钩子

- If the image direction becomes scary: increase warm light, caregiver proximity, readable ground, and ordinary-cause cues.
- If Xiao He appears too frightened: reduce facial distress and use mild hand-clutching, breathing, or comforted posture.
- If Xiao He or Mama becomes animal-like, plush-like, doll-like, mascot-like, or anthropomorphic: restore ordinary human child/adult anatomy and the locked clothing from the Character cards.
- If the image becomes too polished or digital: increase visible pencil, colored-pencil, watercolor, gouache, matte paper grain, and imperfect hand-drawn edges.
- If Lantern Grandpa appears uncanny: add warm front light, open posture, gentle smile, round glasses, and cottage context.
- If Tangerine's eyes appear magical: reduce glow and state reflected lantern light only.
- If source-derived imagery appears: remove names, locations, sequence packaging, and recognizable horror motifs; return to approved canonical cards.

## Change Log / 变更记录

- 2026-06-26: Created as Workflow D draft recipe for human review; no image execution authorized.
- 2026-06-26: Set a reproducible `recipe_hash` (sha256-short over the Allowed/Forbidden/Negative directive lines) and documented the drift-check basis in `drift_check_policy` so Workflow F can recompute and compare deterministically.
- 2026-06-26: Workflow D human gate accepted in StoryProject `pilot-001`; recipe remains reusable only and does not authorize Workflow E/F/G execution.
- 2026-06-26: Repair p01 manual generation failure by strengthening human-only character locks and hand-made anti-polish rules; p01 requires a new `repair_01` handoff and must not be accepted until QA passes.
