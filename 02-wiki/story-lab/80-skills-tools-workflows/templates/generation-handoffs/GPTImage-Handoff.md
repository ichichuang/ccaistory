---
type: generation_handoff_template
id: "GPTImage-Handoff"
title_zh: GPTImage 人工出图交接模板
title_en: GPTImage Manual Generation Handoff Template
status: active
target_workflow: "G-WebGPTImage-Manual-Generation-Handoff-Workflow"
created_at: 2026-06-30
updated_at: 2026-06-30
owner: ichichuang
canonical: true
---
# GPTImage Manual Generation Handoff Template

> This template is a controlled human handoff. It does not authorize Codex, runtime, or any automated process to call GPTImage or create image files.

## Target Page
- Package id:
- Project id:
- Page:
- Scene:
- Aspect ratio:

## Master Reference
- Upload the accepted R00 image.
- Use R00 only for style, character appearance, proportions, paper texture, line quality, matte scan behavior, and red-pen annotation language.
- Do not use R00 as story content, location content, prop content, or composition content unless the current ImageExecutionPackage explicitly requires the same element.

## Previous Page Continuity
- Previous page id:
- Previous accepted image or candidate reference:
- Previous scene summary:
- Current scene summary:
- What must be inherited:
- What changes on this page:
- What must not appear yet:

## What Must Stay From The Previous Page
- Scene geometry that must remain continuous:
- Light / darkness / density state that must remain continuous:
- Character position or relationship state that must remain continuous:
- Prior-page spatial logic that must not be broken:

## What May Change By Only One Step
- Allowed progression budget from previous page:
- Darkness / density / enclosure change:
- New clue or event change:
- What would be too much for this page:

## Hook Direction
- Page-turn question:
- Hook visual target:
- Red circle, arrow, or question mark target:
- Suggested short Chinese annotations, 1-3 options:
- Avoid generic mood labels unless the composition makes the visual question specific.

## Main Hook Semantics
- Intended clue semantics:
- Where the clue sits in the environment:
- How visible the clue should be:
- Why it belongs to this page:

## Common Misread To Avoid
- Object class the clue must not become:
- Visual traits that cause that misread:
- Negative instruction to prevent the misread:

## Do Not Overcorrect
- Repair guardrails:
- Continuity that must survive the repair:
- Environment / composition changes that would break the previous-page link:

## Read Order Goal
- First read: overall scene continuity from the previous page.
- Second read: hidden clue discovery.
- The hook must not dominate the whole composition before the scene reads correctly.

## Escalation Control
- Story-stage intensity:
- Controlled scene delta:
- What gets darker, stranger, closer, quieter, emptier, brighter, or safer:
- What would be too early for this page:
- Later-page elements that must not appear:

## Positive Prompt Payload
- Use only approved content from the current ImageExecutionPackage and compiled prompt.
- Keep page-specific scene content separate from R00 continuity instructions.

## Negative Constraints
- Forbidden continuity jumps:
- Forbidden style drift:
- Forbidden safety content:
- Forbidden in-image text or UI:

## Execution Record Fields
- actual_prompt_sent_to_external_tool:
- tool:
- model:
- parameters:
- output_path:
- operator:
- executed_at:
