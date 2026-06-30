---
type: acceptance_checklist
id: "Series-Continuity-and-Hook-Checklist"
status: active
stage: image_execution_package
target_layer: "02-wiki/story-lab/70-execution-packages"
related_runtime_commands: ["lint-asset", "lint-prompt", "generate-image-review-form", "validate-image-review", "qa-asset"]
related_templates: ["ImageExecutionPackage", "GPTImage-Handoff"]
owner: ichichuang
updated_at: 2026-06-30
---
# Series Continuity and Hook Checklist

## Purpose
For every serialized image page after p01, verify that the page is the next controlled step after the previous accepted page. R00 controls visual continuity; the immediately previous accepted page controls scene continuity and progression.

## A. R00 Visual Continuity
- [ ] Same paper or notebook surface.
- [ ] Same child-drawn line quality.
- [ ] Same coloring material.
- [ ] Same red-pen annotation behavior.
- [ ] Same character designs.
- [ ] Same character height ratio and proportions.
- [ ] No animalization, plush, doll, mascot, or anthropomorphic replacement of human characters.
- [ ] No style polish drift.
- [ ] No commercial picture-book drift.
- [ ] No 3D, photoreal, cinematic, or over-rendered drift.

## B. Previous Page Scene Continuity
- [ ] Location continues logically from the previous accepted page.
- [ ] Path, room, road, building, or other scene geometry does not jump unexpectedly.
- [ ] Density, darkness, fog, light, crowding, or visual pressure evolves gradually.
- [ ] `continuity_priority`: the new page still feels like a direct continuation of the previous accepted page before it reads as an isolated dramatic image.
- [ ] No sudden new props or infrastructure unless previously seeded or story-required.
- [ ] No copy-paste of the previous page composition.
- [ ] No hard scene reset unless approved by the Story Graph.

## C. Narrative Progression
- [ ] Page intensity fits its story position.
- [ ] Page does not feel like a later page too early.
- [ ] Only one or two meaningful changes are introduced.
- [ ] Scare or mystery escalation is controlled.
- [ ] `progression_budget`: the page is only one controlled step beyond the previous accepted page.
- [ ] `overcorrection_risk`: repair did not solve one issue by creating a stronger continuity break.
- [ ] Rational and safety story arc remains intact unless the Story Core says otherwise.

## D. Hook Strength
- [ ] Page has one clear visual question.
- [ ] Hook is specific, not generic.
- [ ] `symbol_semantics_clarity`: the intended clue reads as the intended clue, not another object class (for example, eyes vs lamps).
- [ ] Red annotation points to the actual uncertainty.
- [ ] `hook_integration`: the clue integrates into the environment instead of becoming an isolated block or early full-page focus.
- [ ] Hook invites the next page.
- [ ] Hook comes from approved page content.
- [ ] Hook text is short, childlike, and page-specific.

Good short hook examples:

- `灯少了`
- `看不清？`
- `前面呢？`
- `谁在响？`
- `那是什么？`
- `是不是眼睛？`
- `声音呢？`

Weak hook examples:

- `有点黑`, if it only describes mood.
- `好可怕`, if no specific visual question exists.
- Random red circles that do not point to the story uncertainty.

## General Rule
Each page may only advance the environment and mystery by the amount justified by the Story Graph and the previous accepted page. This checklist applies to any scene type: school hallway, bedroom, elevator, family photo, village road, cupboard, window, river path, apartment corridor, or another approved scene.
