# AI+Story P0 Operator-Layer Remediation Report

> Implementation report for the P0 fixes from `Skill-Workflow-Production-Readiness-Audit.md`. No real story / image / WebGPTImage prompt / project / card / GenerationRun / RepairNote / ReferenceAsset / publishing package was created — this is system repair only. Date: 2026-06-25. Branch: `main`. Not pushed.

## 0. Executive verdict

**CONDITIONALLY READY.**

The operator-facing layer now follows a single doctrine (Obsidian Markdown canonical cards + runtime tool layer). All 5 runtime validations pass, the forbidden old-doctrine strings are gone from every active document, the full image chain is wired across the 4 layers, and the previously-missing final-package assembly step exists. A first pilot can be run manually by following the A–L workflows + the English codex-instructions + the runtime CLI. Remaining items (full skill-body rewrites, runtime validator implementation, legacy-folder reconciliation, the other stub specs/checklists) are P1 and do not block the first pilot.

## 1. Summary of changes

134 files changed (110 modified + 24 new):
- **32 skill cards** transformed (frontmatter + doctrine note + removal of the `唯一事实源：故事核心.json` line) via a controlled, idempotent script; **8 new production skills** + **1 production skill map** authored; 4 stubs resolved.
- **18 workflows** transformed (frontmatter + prohibition removal); **12 new A–L production workflows** authored (incl. the final-assembly workflow).
- **19 legacy codex-instructions retired** (explicit `status: retired` frontmatter + banner); **13 active** (5 English + 7 runtime-runner + 1 new ASSEMBLE instruction) given doctrine-aligned frontmatter.
- **6 canonical templates + 6 field schemas** fixed (traceability chain, status enums, R00 fields).
- **4 dashboard `.base` files + 3 Dataview dashboards** rebound to correct fields/enums.
- **runtime/README.md** doctrine inversion corrected; **Runtime-Is-Tool-Layer.md** gained a missing-validators scope section.
- **7 acceptance checklists** filled with real pass/fail gates (6 stubs + 1 new final-package checklist).
- **Final-assembly doctrine** added: codex instruction + map + workflow + skill + checklist.
- One legacy-control duplicate SOP retired.

## 2. Doctrine conflicts resolved

| Conflict (from audit) | Resolution |
|---|---|
| Two source-of-truth models coexisting | Single doctrine enforced: `02-wiki` Markdown = production knowledge; `runtime/contracts` = validation rules; runtime/Artifact Registry = derived caches. The `唯一事实源：故事核心.json` line was removed from all 25 skill cards that had it and replaced with a canonical doctrine note; 19 legacy codex-instructions + 1 legacy-control SOP that assert the old model are now `status: retired`. |
| Workflows forbid ImageExecutionPackage | Prohibition removed from active workflows; new `E-ImageExecutionPackage-Creation-Workflow` is the single sanctioned creation entry. |
| `runtime/README.md` says "contracts win / contracts are source of truth" | Rewritten to the rules-vs-knowledge split; "block production and require reconciliation" on conflict; Artifact Registry explicitly labeled "not the canonical asset registry". |
| Verification: forbidden strings (`唯一事实源：故事核心.json`, `故事项目/`, `禁止.*执行包`) | **0 occurrences in active docs** — present only in migration/audit reports and explicitly-retired docs (allowed). |

## 3. Skill card remediation

- **Active skills: 35** · **deprecated: 4** · **needs_fix: 1** · (40 skill cards total + 1 `production-skill-map.md`).
- **Frontmatter coverage: 40/40 skill cards** (the map is a reference doc, intentionally without card frontmatter). Status normalized to the enum `active / draft / retired / deprecated / needs_fix`.
- **Runtime command coverage:** every skill's frontmatter declares `runtime_commands` + `runtime_support_status` (`runtime` vs `manual_only`). Manual-only skills are explicitly marked (intake, extraction, visual settings, storyboard, handoff, repair router, publish synthesis, full-read, technique distillation, archive).
- **8 new skills** (filling missing stages): Character-Extraction, Scene-Extraction, PromptRecipe-Authoring, ImageExecutionPackage-Creation, ReferenceAsset-Acceptance, Rejected-Asset-Archive, Final Illustrated Story Package Assembly, Publishing-Readiness.
- **Broken stubs resolved (4):** `创作者技法蒸馏技能` expanded to executable; `视觉候选失败复盘技能` → deprecated (→ `资产验收与返修技能`); `发布编排技能` → deprecated (→ `平台发布页合成技能`); `发布后数据回收技能` → needs_fix (deferred post-pilot, off the critical illustrated-story path).
- **Overlap reconciliation:** `总控编排` → deprecated (→ Pipeline Runner); `提示词生成` → deprecated (→ Prompt Compile / PromptRecipe-Authoring). `production-skill-map.md` documents merges and the narrative-vs-production split.
- **Narrative vs production skills:** `production-skill-map.md` clearly separates the **12 runtime-registered narrative-technique skills** (`runtime/skill_registry/skills.json`) from the **40 production workflow skill cards**, and per-skill runtime command + manual-only/retired status. The 12 narrative skills were left untouched (registry still validates count 12; `skill_definitions` consistency intact).

## 4. Workflow remediation

- **Active workflows: 21** · **deprecated: 9** (30 total).
- **Main-line SOP:** `平台图文故事生产流程.md` (runtime-integrated) retained as the umbrella SOP; 9 clone workflows demoted to `deprecated` with `deprecated_by` pointers.
- **12 new A–L workflows** wire the 4-layer card model:
  A Raw Story Intake · B Story Analysis & Canonical Card · C Character & Scene Extraction · D Visual Style & PromptRecipe · E ImageExecutionPackage Creation · F Prompt Compile & Semantic Lint · G WebGPTImage Manual Generation Handoff · H GenerationRun Backfill · I Image QA & Repair · J ReferenceAsset Acceptance · K Final Illustrated Story Package Assembly · L Publishing Readiness.
- **External window manual rewritten:** `外部出图工具出图窗口操作手册` → deprecated; replaced by `G-WebGPTImage-Manual-Generation-Handoff-Workflow` which names the two-window model, consumes an ImageExecutionPackage, returns candidates to `01-raw/generated-raw`, requires GenerationRun backfill, and never marks accepted itself.
- All A–L workflows reference the correct layers (verified: `01-raw`/`02-wiki`/`50-agent-work`/`90-archive`/`70-execution-packages`/`reference-assets`/`WebGPTImage`/`GenerationRun`/`RepairNote`/`ReferenceAsset`/`ImageExecutionPackage` all present across the set) and use backtick references (no unresolved `[[ ]]` links).

## 5. Image chain status

The active chain (workflows E → F → G → H → I → J → K → L) now writes the doctrine entities to the correct layers, with no-skip gates:

```
ImageExecutionPackage (02-wiki/70-execution-packages, status draft→ready after compile+lint)
  → compile-asset + lint-asset  (50-agent-work/compiled-prompts, semantic-lint-results)
  → WebGPTImage manual handoff  (受控执行单; candidates → 01-raw/generated-raw)
  → GenerationRun               (50-agent-work/runs; validate-telemetry — no telemetry ⇒ no accept)
  → 人工 image_review_form + asset_qa  (50-agent-work/image-review-forms, qa-results)
        ├─ pass  → ReferenceAsset accepted (02-wiki/reference-assets) [三件套 + accepted_by/at]
        ├─ rework→ RepairNote (50-agent-work/repair-notes) → 回上游重出
        └─ reject→ 90-archive/rejected-assets
  → Final Illustrated Story Package Assembly (02-wiki StoryProject Final Package + 50-agent-work record)
  → Publishing Readiness (50-agent-work/qa-results + 02-wiki final decision)
```

Hard rules encoded: no workflow skips GenerationRun; no accept without human image review; no accept without QA evidence (三件套); rejected/deprecated never become dependencies; Artifact Registry is treated as cache, not canonical; R00-not-accepted blocks R01/R02.

## 6. Template and metadata fixes

| Template | Fix |
|---|---|
| ReferenceAsset | default `status: draft` → `candidate` (in-enum); added `source_run`, `source_generation_run`, `source_image_review_form`, `source_asset_qa_result`, `source_repair_note`, `accepted_by`, `accepted_at`, `qa_required: true`, `allowed_usage`, `forbidden_usage`, `r00_anchor_scope`; body sections for provenance + R00 scope. |
| RepairNote | added `output_asset`, `target_reference_asset`, `source_generation_run`, `linked_image_review_form`, `close_status`; **removed duplicate `repair_status`** (single `status`). |
| GenerationRun | **`repair_package` → `repair_note`**; added `image_execution_package`, `output_candidates`, `image_review_form`, `asset_qa_result`, `final_decision`, `backfill_status`. |
| ImageExecutionPackage | added `generation_run_ids`, `required_reference_assets`, `prohibited_reference_assets`, `r00_dependency_policy`, `maximum_anchor_reuse_policy`, `final_assembly_dependency`; body R00 policy section. |
| PromptRecipe | added `recipe_hash`, `drift_check_policy`, `compatible_asset_types`. |
| StoryProject | added `final_package_status`, `required_asset_count`, `accepted_asset_count`, `publishing_readiness_status`. |

All 6 `.fields.md` schemas updated to match. **Traceability chain closed:** RepairNote → ReferenceAsset link added (`output_asset`/`target_reference_asset`); ReferenceAsset → originating run typed via `source_generation_run`. Dashboards fixed: `image-package-board` `package_id`→`id`; `scene-board` `related_assets`→`linked_packages`; `reference-asset-gallery` `cover_image`→`file_location`; `repair-queue` `repair_status != "done"`→`status != "closed"`; non-enum status values purged from comments/prose.

## 7. Runtime boundary fixes

- `runtime/README.md:3` rewritten — contracts own validation rules, 02-wiki owns production knowledge, runtime outputs + Artifact Registry are derived caches, conflicts block and require reconciliation, Artifact Registry is not canonical.
- `Runtime-Is-Tool-Layer.md` gained §7 documenting the missing validators (scope only, not implemented): `validate-vault`, wrong-layer-write detector, card↔cache reconciliation, StoryProject asset-count consistency, required-GenerationRun-before-acceptance, required-image-review-before-accepted, prompt-recipe drift, reference-asset drift, story-fact drift; plus a note that the smoke-test "does-not-generate" guards still point at deleted legacy roots (vacuous) and should be repointed at the new layers.
- **Runtime logic and tests were NOT modified** (per the no-weakening constraint). `compileall` passes; smoke-test passes.

## 8. Acceptance checklist fixes

7 checklists now carry real pass/fail criteria, blocking conditions, required evidence, output decision, target layer, related templates, and runtime command:
`源插图语义Lint验收清单`, `资产级细粒度验收清单`, `R01角色锚图验收清单`, `R02场景道具锚图验收清单`, `人工完整阅读清单`, `完整故事出图前验收清单`, and the new `Final Illustrated Story Package Readiness Checklist`. (R00 anchor checklist was already real and was left untouched — it is a `check-contract-drift` R00 source file.)

## 9. R00 overload guard

The R00-anchor-overload rule, previously only in legacy instructions, is now carried into the new doctrine:
- **ImageExecutionPackage** template: `r00_dependency_policy`, `maximum_anchor_reuse_policy`, `prohibited_reference_assets` + a body "R00 Anchor Dependency Policy" section (must declare the exact borrowed property; use R01/R02 or specific accepted ReferenceAsset for character/scene continuity, not a generic R00).
- **ReferenceAsset** template: `r00_anchor_scope` + body "R00 Anchor Scope" section (R00 = `paper-stroke-anchor`, narrow property only).
- **E-ImageExecutionPackage-Creation-Workflow** + **I-Image-QA-and-Repair-Workflow**: R00 dependency declaration; R00-not-accepted blocks R01/R02.
- **R01 / R02 acceptance checklists**: R00-not-accepted is a blocking condition; R01 must not carry full scenes/plots, R02 must not carry full character systems.
- **final-illustrated-story-package-map** + field-schema validation notes reinforce it.

## 10. Validation results

| Check | Result |
|---|---|
| `aistory.py status` | `empty` (no project — expected) |
| `aistory.py validate` | **pass** |
| `aistory.py validate-contracts` | **pass** (skills 12, R00 QA 14) |
| `aistory.py check-contract-drift` | **pass** (0 broken links) |
| `aistory.py smoke-test` | **pass** |
| `python -m compileall runtime` | **OK** |
| Forbidden old-doctrine strings in active docs | **0** (only in migration/audit reports + retired docs) |
| Required new-layer vocab in A–L workflows | all 11 terms present |
| Forbidden live-asset strings (KHN2_001, CLEAN_WHITE_NOTEBOOK, R00_人工外部生成操作单) | **clean** |
| Tracked binaries | **none** |

## 11. Remaining risks

1. **Skill bodies still use legacy `story_core.*` field language.** The frontmatter (`input_layer`/`output_layer`) + per-card doctrine note re-map this to the correct layers, but full body rewrites of the ~25 transformed skills onto the card model are P1.
2. **Runtime validators are documented, not implemented.** Layer-write rules, card presence, drift checks, and the StoryProject asset-count check are scoped in `Runtime-Is-Tool-Layer.md §7` but not enforced by code yet — so doctrine adherence still relies on operator discipline + the human gates.
3. **Runtime tests still vacuous.** The "does-not-generate" guards scan deleted legacy roots; not repointed (no-weakening-tests constraint). P1: repoint at new layers + add positive 4-layer tests.
4. **Deprecated clones retained.** 9 deprecated workflows + 5 deprecated/needs_fix skills + 19 retired instructions remain in-tree (marked, not deleted) for history. Operators must follow `active` cards only; relapse risk until they are pruned.
5. **Legacy folders not fully reconciled.** `00-dashboard/legacy-control/`, `60-prompts/legacy-prompt-library/`, `legacy-templates/` still hold a parallel control/prompt system (the offending SOP was retired; the rest are non-conflicting but duplicative).
6. **Other stub specs/checklists.** Only the 7 production-critical checklists were filled (per audit §12 minimum); ~13 other checklists and ~15 structure-specs remain thin (P1).
7. **No real cards exist yet.** All `02-wiki` card folders are still empty skeletons; the pilot will create the first real cards — dashboards/queries are unverified against live data until then.

## 12. Readiness verdict

**Can the first new story pilot start now?** Yes — manually. An operator can run a pilot by: (1) following workflows A→L in order; (2) using the 5 English codex-instructions + the new ASSEMBLE instruction for the create/backfill/accept/assemble steps; (3) driving `runtime/aistory.py` for compile/lint/telemetry/QA/registry; (4) creating cards from `templates/canonical-assets/` and filling frontmatter per the `.fields.md` schemas; (5) honoring the human gates and acceptance checklists.

**Manual constraints that remain:**
- Card creation is manual — no runtime command creates `02-wiki` cards.
- Obsidian with Dataview + Bases enabled for the dashboards; `python3` for the CLI; an external WebGPTImage generation surface for the handoff.
- Follow `status: active` cards only; ignore `deprecated`/`retired` ones.
- Image binaries stay out of git (`.gitignore`); cards carry `file_location` paths.

**Must still be fixed before scale production:**
- Implement the documented runtime validators (esp. wrong-layer-write + validate-vault + acceptance-prerequisite + drift checks) and repoint/extend the runtime tests to the 4-layer doctrine.
- Rewrite the ~25 transformed skill bodies fully onto the card model (remove residual `story_core` language).
- Prune or archive the deprecated clones and reconcile the legacy-control/legacy-prompt-library/legacy-templates folders.
- Fill the remaining stub checklists and structure-specs; add a `World` template or drop `StoryProject.worlds`.

**Remaining risk:** primarily QA-bypass/drift if operators ignore the human gates (the gates are now defined but not yet machine-enforced), and doctrine relapse while deprecated/retired docs remain in-tree. Both are mitigated by the explicit `status` markers, the doctrine notes, and the no-skip gates encoded in the A–L workflows.
