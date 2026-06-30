---
type: workflow_note
id: "P03-Continuity-Hook-Repair-Lesson"
title_zh: p03 连续性与钩子返修经验
title_en: p03 Continuity and Hook Repair Lesson
status: active
project_id: pilot-001
related_assets:
  - iep-pilot-001-p03-dark-wooded-lane
  - ra-pilot-001-p03-dark-wooded-lane
tags: [workflow-note, story-lab, continuity, hook, repair]
created_at: 2026-06-30
updated_at: 2026-06-30
owner: ichichuang
version: v0
canonical: true
---
# p03 Continuity and Hook Repair Lesson

## Lesson

Local hook success is not enough. A page can make its strange clue clearer while becoming less harmonious with the previous accepted page.

## Reusable Rules

- Series continuity outranks isolated dramatic effect.
- Clue semantics must be disambiguated before handoff; record both the intended clue and the object class it must not become.
- Repairs must preserve prior-page spatial logic, light state, path readability, and character/proportion continuity.
- Page progression should be incremental, not theatrical.
- The clue should be readable but integrated: first read the continuing scene, then discover the clue.

## p03 Failure Pattern

- Symbol ambiguity: intended hidden eyes were repeatedly at risk of reading as lamps.
- Overcorrection: fixing the eyes could make the page too dark, too dense, or too enclosed for p03.
- Continuity drift: a locally improved hook can weaken previous-page continuity.
- Balance problem: the strange clue must be readable without dominating the full page composition too early.

## Process Consequence

Future ImageExecutionPackages, GPTImage handoffs, semantic lint, and Workflow I QA must include symbol semantics, common misread, progression budget, overcorrection guardrail, and read-order checks whenever a page has an ambiguous visual clue or a repair loop.
