# AI+Story Skill / Workflow / Production Readiness Audit

> Read-only audit. No story, image, prompt, card, project, or GenerationRun was created. No commit, no push. Evidence is cited by exact repository path; all validation commands below were run against the repo as-is on 2026-06-25.

## 0. Executive verdict

**NOT READY.**

The *foundations* are genuinely strong — the 4-layer architecture docs, the 11 canonical-asset templates (1:1 with their field schemas, fully normalized `type` values), the runtime tool layer (well-behaved: writes only to its own caches, blocks generation, approval-gated), and the **5 English-named codex-instructions** form a coherent new-doctrine path. But the repository currently contains **two parallel, mutually contradictory operating systems**, and the layer a human operator actually touches to run production — the **32 skill cards and 18 workflows** — implements the *old* model, contradicts the new doctrine, and cannot be executed as written:

- The 18 workflows are 11 near-duplicate clones that **explicitly forbid the exact artifact the doctrine requires** (`禁止创建…执行包` in 16/18 files) and **never write to `50-agent-work/`, `70-execution-packages/`, or `reference-assets/`** (0/18). The end-to-end image chain breaks at the external-generation handoff.
- The 32 skill cards have **no YAML frontmatter** (0/32), are **not in the skill registry** (the registry holds 12 unrelated narrative-technique skills), cite **no runtime command**, write to a monolithic `故事核心.json` instead of canonical cards, and **4 are unexecutable boilerplate stubs**.
- The QA/acceptance gates are hollow: **20/29 acceptance-checklists and 15/25 structure-specs are byte-identical placeholder stubs**. Only the R00 anchor gate and the runtime-module layer can actually block bad output.
- The **final step — assembling accepted ReferenceAssets into a complete illustrated story package — is undocumented in the new doctrine** (it exists only inside the contradictory legacy layer).

A determined expert could push a single pilot through the new-doctrine path (English codex-instructions + runtime CLI + templates) with heavy manual effort, but the system as a coherent whole **cannot yet reliably** produce a complete illustrated story package. The defects are correctable and concentrated; with the fixes in §8 the system can reach CONDITIONALLY READY.

## 1. Current system summary

AI+Story is an **Obsidian Story Production Wiki + runtime tool layer**.

- **Wiki (`02-wiki/story-lab/`)** is intended as the canonical, human-readable source of truth: Markdown "cards" for projects, worlds, characters, scenes, visual styles, prompt recipes, image execution packages, reference assets, skills/workflows, plus dashboards and indexes. **Today every card folder is an empty `.gitkeep` skeleton** (`10-projects`, `20-worlds`, `30-characters`, `40-scenes`, `50-visual-styles`, `70-execution-packages`, `reference-assets`) — expected for an un-piloted system; the templates that would populate them exist under `80-skills-tools-workflows/templates/canonical-assets/`.
- **Layers:** `01-raw` (immutable inputs), `02-wiki` (canonical), `50-agent-work` (operational records: runs/compiled-prompts/lint/qa/review-forms/repair-notes), `90-archive` (rejected/retired). All four exist as skeletons.
- **`runtime/`** is a validator/compiler/linter/QA-helper + cache producer exposed via `python runtime/aistory.py <subcommand>` (~45 subcommands, not the 5 the README advertises). It registers **12 narrative-technique skills** (`runtime/skill_registry/skills.json`), which are **not** the 32 wiki skill cards.
- **Two-window operating model** (WebGPT command window for planning/review; separate WebGPTImage window for generation) is documented in `00-system/architecture/` and `02-wiki/story-lab/maps/webgpt-two-window-workflow-map.md`, but is **named nowhere** in the 18 workflows or the 32 skill cards.

**Validation commands (all pass):**

| Command | Result | What it actually checks |
| --- | --- | --- |
| `status` | `{"status":"empty"}` | runtime/vault machine-state (empty repo). Does **not** read `02-wiki`. |
| `validate` | `pass` | JSON validity of `runtime/schemas/*` + `runtime/tests/fixtures/*` + 12-skill registry. **Does not check `02-wiki` card presence/layout.** |
| `validate-contracts` | `pass` (skill_count 12, r00_qa_count 14) | structure + cross-links of the 5 contract JSONs. |
| `check-contract-drift` | `pass` (0 broken links) | the **only** command touching `02-wiki`: 5 hard-coded R00 cards + Obsidian wiki-link integrity. Narrow. |
| `smoke-test` | `pass` (74 checks) | runtime behavior incl. "does-not-generate" guards — but those guards scan **deleted** legacy roots, so they pass vacuously. |

The structural reality: **canonical knowledge model is split.** Templates + English codex-instructions + architecture + runtime *boundary* docs follow the new "small canonical cards in 02-wiki, evidence in 50-agent-work" doctrine. The 32 skill cards + 18 workflows + 19 legacy Chinese codex-instructions + `runtime/README.md` follow the old "one monolithic `故事核心.json` is the single source of truth" model.

## 2. Skill inventory

32 skill cards in `02-wiki/story-lab/80-skills-tools-workflows/skills/` (path prefix omitted in column 1). **Systemic facts true of all 32:** no YAML frontmatter (0/32 — they use prose `状态：活动 / 唯一事实源：故事核心.json`); none cite a runtime `aistory.py` command; none are in `runtime/skill_registry/skills.json`. "Runtime support" column = the existing CLI that *could* back it but is **not wired**.

| Skill path (…/skills/) | Skill name | Purpose | Inputs | Outputs → layer | Runtime support (latent) | Workflow dependency | Risk | Verdict | Required fix |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Artifact Registry技能.md` | Artifact Registry | Stable id/hash/lineage/status for artifacts | artifact payload, parent ids | registry → **runtime-cache** | `artifact-register/-validate/-lineage` | Artifact Registry产物登记流程 | low (mitigates pollution) | OK | add frontmatter; declare derived-cache role |
| `Multimodal QA技能.md` | Multimodal QA | Turn external image results into auditable human review | human review answers + evidence | review form, `asset_qa_result` → should be **50-agent-work** | `generate/validate/merge-image-qa` | Multimodal QA人工复核流程 | strong gate; output layer unnamed | OK | name `50-agent-work` output; frontmatter |
| `Pipeline Runner技能.md` | Pipeline Runner | Plan/block/resume/audit stages | story_core, contracts | run manifest → **runtime-cache** | `pipeline-plan/run/status/resume` | Pipeline Runner执行流程 | mislabels contracts as 事实源 | needs-fix | point 事实源 at 02-wiki card |
| `Skill Executor技能.md` | Skill Executor | Convert problems → reviewable proposed_changes | story_graph, runtime patches | proposed_changes → **layer undeclared** (should be 50-agent-work/repair-notes) | `score-skill-candidate`, `execute-skill-graph` | Skill Executor候选修复流程 | output layer undeclared | needs-fix | declare 50-agent-work target |
| `Skill Runtime技能.md` | Skill Runtime | Check creator-technique landing on nodes | story_graph, skills.json | node eval, patch → dry-run | `evaluate-node`, `repair-skill-graph` | Skill Runtime修复流程 | hardcodes "12 skills" | needs-fix | derive skill count from registry |
| `Story Analyzer技能.md` | Story Analyzer | Content-aware graph diagnosis | story_core, story_graph | recommended_skill_plan → none | `analyze-story/-graph` | Story Analyzer诊断流程 | overlaps 4 dedicated skills; no status | needs-fix | reconcile weakness-detection ownership |
| `机器事实源Contracts技能.md` | Contracts | Maintain `runtime/contracts/` validation rules | contract JSON, skills.json | contracts → **runtime-cache** | `validate-contracts`, `check-contract-drift` | Contracts同步流程 | most aligned card | OK | add frontmatter; centralize magic counts |
| `总控编排技能.md` | Master Orchestration | "Run orchestration stage w/o skipping state machine" | story_core + specs | derived view → unnamed | none | none (orphaned) | **boilerplate stub**; dup of Pipeline Runner | needs-fix | merge into Pipeline Runner or make concrete |
| `提示词巡检与任务清单技能.md` | Prompt Patrol / Task-list | Arrange lint-passed prompts into pilot task-list | compiled_prompts, lint, deps | `pilot_task_list` → story_core | (lint/compile engines) | 新故事从输入到试产流程 | depends on skills not wired | needs-fix | wire upstream/downstream skills |
| `故事输入与版权改编技能.md` | Story Intake / Copyright | Raw input → legal, traceable story-core | source_material, copyright | story_core fields → **02-wiki story_core** | none (manual) | 故事核心状态机技能 | never references `01-raw` provenance | needs-fix | reference 01-raw immutable input |
| `故事核心状态机技能.md` | Story State Machine | Maintain story_core state machine + gates | machine_state, gates | story_core fields | (state_machine.json via Contracts) | 长故事页数合理性审查技能 | tri-owned with Pipeline Runner+Contracts | needs-fix | state division of labor |
| `故事极简化与最小可行故事评估技能.md` | Minimization / MVS | "Run minimization stage" | story_core + specs | derived view → unnamed | none | none (orphaned) | **boilerplate stub**; MVS criteria undefined | needs-fix | define MVS rubric + wiring |
| `故事图扩展与连贯性审查技能.md` | Graph Expansion / Continuity | Expand core graph; review continuity | story_graph, continuity | platform_story_graph → story_core | `check-graph` | 故事钩子强化技能 | no human gate at rewrite | needs-fix | add review gate |
| `故事钩子强化技能.md` | Hook Reinforcement | Strengthen opening/turn/ending hooks | story_graph.hooks | hook_revisions → story_core | `analyze-graph`/registry skill `page_turn_hook` | 平台图文故事编排技能 | writes rewrites w/ **no approval gate** | needs-fix | add approval gate; reconcile w/ Skill Executor |
| `长故事页数合理性审查技能.md` | Page-count Plausibility | Judge page count/pacing/completion risk | story_graph, target_pages | quality_gates.long_story_page_count | `estimate-pages` | 故事图扩展与连贯性审查技能 | no quantitative thresholds | needs-fix | define platform thresholds |
| `人工完整阅读技能.md` | Manual Full Read | Full human read of publish page | publish_page, accepted_assets | quality_gates.manual_full_reading | none (human) | 发布前检查 (skill absent) | upstream synth skill missing | OK | confirm upstream/downstream exist |
| `创作者技法蒸馏技能.md` | Technique Distillation | "Run technique-distillation stage" | (generic) | unnamed | (feeds skills.json) | 创作者技法蒸馏流程 | **stub**; author-style-leak risk | broken | expand + author-style guard |
| `视觉设定技能.md` | Visual Settings | Constrain story visual rules | platform pages, tone, policies | visual_rules → story_core | none | 视觉资产本体技能 | overlaps 视觉资产本体 | needs-fix | merge boundary; concrete schema |
| `视觉资产本体技能.md` | Visual Asset Ontology | Define each asset role/boundary/policy | asset_manifest, visual_rules | asset_ontology → story_core | `compile-asset` precondition | 源插图Prompt编译技能 | **defines R00 boundary — overload origin** | needs-fix | cap R00 dependents; frontmatter |
| `提示词生成技能.md` | Prompt Fragment Gen | Reusable prompt fragments (not compile) | prompt_locks, visual_rules | prompt_fragments → story_core | (`lint-prompt` adjacent) | 源插图Prompt编译技能 | **redundant** w/ Prompt Compile | redundant | fold into Prompt Compile or define handoff |
| `源插图Prompt编译技能.md` | Source-Illust Prompt Compile | Compile ontology → compiled_prompt | asset_ontology, deps | compiled_prompts → story_core (should be 50-agent-work) | **`compile-asset`** (exists, unused) | 源插图语义Lint技能 | prompt-drift; reference-drift | needs-fix | wire `compile-asset`; single prompt writer |
| `源插图语义Lint技能.md` | Semantic Lint | Lint compiled_prompt for missing/forbidden | compiled_prompt, negatives | semantic_lint → story_core (should be 50-agent-work) | **`lint-prompt`/`lint_engine`** (the R00 guard) | 提示词巡检与任务清单技能 | strongest auto R00 guard **unwired** | needs-fix | wire `lint_engine`; output→50-agent-work |
| `图文分镜与图读测试技能.md` | Storyboard / Image-read | Page comprehensible from image+text alone | platform pages, focus | image_reading_test → story_core | none (judgment) | 视觉设定/视觉资产本体技能 | no pass/fail rubric | needs-fix | add rubric |
| `出图执行技能.md` | Image Execution | Govern manual single-image external gen | pilot_task_list, compiled_prompt | candidate + actual prompt → story_core | none by design (human window) | 图像执行遥测技能 | QA-bypass; no ImageExecutionPackage ref | needs-fix | reference 70-execution-packages handoff |
| `图像执行遥测技能.md` | Execution Telemetry | Record real external-gen facts | actual_prompt, tool_config | execution_telemetry → story_core (should be 50-agent-work) | **`validate-telemetry`** (exists, unused) | 资产级细粒度验收技能 | **forgeable accept precondition** | needs-fix | wire telemetry; tamper-resist |
| `资产级细粒度验收技能.md` | Asset-level Acceptance | Per-asset accept/reject/rework decision | ontology, telemetry, candidates | asset_acceptance → story_core (should be 50-agent-work) | **`qa-asset`** (exists, unused) | 资产验收与返修技能 | **auto-accepts w/o human form** (QA-bypass) | needs-fix | subordinate to human image_review_form |
| `资产验收与返修技能.md` | Acceptance & Repair Router | Route rejected/rework; protect deps | asset_acceptance, deps | repair_queue/accepted_assets → story_core | `repair_loop` (narrative only) | 平台发布页合成技能 | **acceptance-field schism**; reference-drift | needs-fix | one canonical accepted store |
| `视觉候选失败复盘技能.md` | Visual Failure Post-mortem | "Run failure post-mortem stage" | (generic) | unnamed | none | none (orphaned) | **stub**; indistinct from Router/QA | broken | expand or merge into Router |
| `发布编排技能.md` | Publish Orchestration | "Run publish-orchestration stage" | (generic) | unnamed | (`pipeline-run`) | none (orphaned) | **stub**; dup of Publish-page Synth | broken | define or delete in favor of Synth |
| `平台发布页合成技能.md` | Publish-page Synthesis | Compose publish page from accepted assets | platform pages, accepted_assets | publish_page → story_core | none | 人工完整阅读技能 | inherits acceptance-field schism | needs-fix | pin accepted_assets to canonical store |
| `平台图文故事编排技能.md` | Platform Story Orchestration | Page-level image/text responsibilities | platform_story_graph, hooks | platform_story_pages → story_core | none | 图文分镜与图读测试技能 | story-fact drift (page vs story) | needs-fix | bind page-gen to story_graph read-only |
| `发布后数据回收技能.md` | Post-publish Data Recovery | "Run post-publish recovery stage" | (generic) | unnamed | none | none (orphaned) | **stub**; off critical path | broken | expand or mark out-of-scope-v1 |

**Cluster verdicts:** runtime/system skills are the healthiest (concrete, but mislabel layers/事实源); the visual→publish skills are *architecturally coherent on paper but operationally disconnected* (correct guard text, real checklists exist, real runtime exists, yet zero wiring); 4 cards (`视觉候选失败复盘`, `发布编排`, `发布后数据回收`, `创作者技法蒸馏`) are **unexecutable stubs**; the QA cluster has **3+ competing "accepted" fields** (`asset_acceptance` / `asset_results`+`accepted_assets` / `asset_qa_result`) and **two competing acceptance engines** (auto-decider `资产级细粒度验收` vs human-form `Multimodal QA`).

## 3. Workflow inventory

18 workflows in `02-wiki/story-lab/80-skills-tools-workflows/workflows/`. **Systemic fact:** files 1–11 are near-identical clones of one 18-stage SOP (same §4 stage list, same §5–§11 gate/prohibition lists); they differ only in the goal line and one downstream wiki-link. Verified across all 18: **0 mention `50-agent-work`, `70-execution-packages`, `reference-assets`, or `WebGPTImage`; 16/18 contain the prohibition `禁止创建…执行包`** (e.g. `故事生产标准作业流程.md:65`). Files 12–18 are genuinely distinct and runtime-backed.

| Workflow path (…/workflows/) | Name | Trigger | Inputs / required cards | Outputs → layer | Human gate | QA gate | Runtime dependency | Risk | Verdict | Required fix |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `故事生产标准作业流程.md` | Full SOP 0→pre-publish | new story | legal input; creates story_core | story_core.machine_state | 6 checkpoints | 13 gates | none named | **forbids 执行包 the doctrine requires** | needs-fix | reconcile with ImageExecutionPackage |
| `新故事从输入到试产流程.md` | Input→pilot task-list | new input | raw input, copyright | pilot task-list → unnamed | yes (boilerplate) | yes | none | clone of SOP truncated | redundant | collapse into SOP phase |
| `平台图文故事生产流程.md` | Platform production | end-to-end | story_core, story_graph + **CLI results** | story_core.machine_state | yes | **runtime gates** | `can-run`,`compile-asset`,`lint-asset`,`qa-asset` (all exist) | best clone; folders unnamed | OK | name 50-agent-work/70/ref folders |
| `视觉执行编译流程.md` | Ontology→prompt→lint | after image-read | ontology card | compiled_prompt → unnamed | yes | paper/style_policy block | `compile-asset`/`lint-asset` | compiled_prompt folder unnamed | needs-fix | write to 60-prompts |
| `图像试产与连续性验证流程.md` | Candidate→telemetry→accept | candidates returned | task-list, exec facts | accept/reject → unnamed | yes | R00-before-R01/R02 | `validate-telemetry`/`qa-asset` | not bound to 50-agent-work/reference-assets | needs-fix | bind to 50-agent-work + reference-assets |
| `外部出图工具出图窗口操作手册.md` | External-gen window manual | about to generate | lint-passed compiled_prompt | candidate facts → unnamed | implicit | boilerplate | none (correct) | **titled "window manual" but names WebGPTImage 0× and is an 18-stage clone** | broken | rewrite as real WebGPTImage manual consuming ImageExecutionPackage |
| `源插图到平台发布页流程.md` | Accepted→publish page | assets accepted | accepted assets | publish layout → unnamed | 人工完整阅读 | forbids rejected | none | "排版方案 allowed vs 发布包 forbidden" undefined | needs-fix | define publish-page home |
| `长故事扩展流程.md` | Long-story expansion | over page budget | story_graph, page budget | expanded graph → unnamed | boilerplate | page review | `estimate-pages` | full 18-stage clone for 1 sub-phase | redundant | reduce to sub-loop |
| `story_graph钩子强化流程.md` | Hook reinforcement | weak hooks | reviewed story_graph | hook_scores graph → unnamed | boilerplate | — | `analyze-graph` | full clone for single stage | redundant | collapse to sub-step |
| `创作者技法蒸馏流程.md` | Technique distillation | distill from source | legal source, copyright | technique modules → unnamed | boilerplate | copyright gate | none | full story-pipeline clone for orthogonal task | redundant | detach from 18-stage template |
| `本地知识库回填手册.md` | Local KB backfill | results returned | telemetry, candidates, QA | **story_core only** | boilerplate | — | none | **backfills only `故事核心.json`, not 02-wiki cards/50-agent-work** (contradicts Contracts同步流程) | needs-fix | redirect to 50-agent-work + canonical cards |
| `Artifact Registry产物登记流程.md` | Artifact registration | artifact produced | payload, parents | `registry.json` → runtime-cache | — | accept-needs-telemetry+QA | `artifact-*` | path literal `.artifacts/` vs dir `artifact_registry/` | OK | confirm registry path |
| `Contracts同步流程.md` | Contracts sync | rule change | contract JSON | contracts + specs | — | drift rules | `validate-contracts`,`check-contract-drift`,`smoke-test` | **clearest ownership doc** | OK | enumerate contract↔spec pairs |
| `Multimodal QA人工复核流程.md` | Human image QA | gen complete | candidate + telemetry registered | review form, `asset_qa_result` → unnamed | yes (human) | **pass-only→accept** | `generate/validate/merge-image-qa` | output folder unnamed | OK | name 50-agent-work/image-review-forms |
| `Pipeline Runner执行流程.md` | Pipeline plan/run/recover | orchestration | story_core, contracts | `.runs/{id}` → runtime-cache | `waiting_for_manual_approval` | blocked_actions | `pipeline-plan/run/status/resume` | strongest engineering doc; windows unnamed | OK | label external-gen stop as WebGPTImage handoff |
| `Skill Executor候选修复流程.md` | Candidate repair | runtime found problem | node/graph + patch | proposed_changes (dry-run) | **approval required** | hard-fail blocking | `score-skill-candidate` | approved changes' persistence unstated | OK | persist approved changes to card |
| `Skill Runtime修复流程.md` | Skill landing repair | after selection | story_graph.nodes, skills.json | repair suggestions (dry-run) | downstream | fallbacks | `evaluate-node`,`repair-skill-graph` | requires Orchestrator (no workflow file) | OK | add Skill Orchestrator workflow |
| `Story Analyzer诊断流程.md` | Diagnosis | after skill-runtime | story_core/graph JSON | diagnostic JSON | downstream | high-risk stop | `analyze-story/-graph` | report persistence unstated | OK | persist report if it informs review |

**Connectivity:** the text side (intake → story_core → page review → hooks → Skill Runtime/Executor/Analyzer → orchestration) is intact and runtime-backed. **The chain breaks at the image-execution handoff:** no workflow creates an ImageExecutionPackage (and 16/18 forbid it), none write to `50-agent-work/`, none write accepted assets to `reference-assets/` or rejected to `90-archive/`. Through the 18 workflows alone, production dead-ends at "外部出图单张执行" with no execution package, no run record, and no canonical ReferenceAsset.

## 4. Skill-to-workflow coverage map

| Production stage | Required skill | Existing skill path | Existing workflow path | Coverage | Gap | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| Raw story intake | intake | `skills/故事输入与版权改编技能.md` | `新故事从输入到试产流程.md` + codex `START_NEW_STORY_OBSIDIAN_WIKI.md` | partial | skill never references `01-raw`; workflow writes story_core not StoryProject card | wire intake to `01-raw` + StoryProject template |
| Story core extraction | state machine | `故事核心状态机技能.md` | `故事生产标准作业流程.md` | partial | writes monolithic `故事核心.json`, not canonical card | reconcile JSON-model vs card-model |
| Copyright/adaptation review | copyright | `故事输入与版权改编技能.md` | `创作者技法蒸馏流程.md` (boundary) | yes | — | minor |
| Story simplification | minimization | `故事极简化与最小可行故事评估技能.md` | none | **stub** | MVS criteria undefined; orphaned | define rubric or merge |
| Minimum-viable-story eval | minimization | same as above | none | **stub** | same | same |
| Story graph creation | graph expansion | `故事图扩展与连贯性审查技能.md` | `长故事扩展流程.md` | partial | no human gate; graph home unnamed | add gate |
| Character extraction | — | **none** | **none** | **MISSING** | no skill/workflow creates `30-characters` Character cards | author Character-extraction skill+workflow |
| Scene extraction | — | **none** | **none** | **MISSING** | no skill/workflow creates `40-scenes` Scene cards | author Scene-extraction skill+workflow |
| Visual style definition | visual settings | `视觉设定技能.md` | `视觉执行编译流程.md` | partial | writes story_core field, not `50-visual-styles` VisualStyle card | wire to VisualStyle template |
| Prompt recipe selection | prompt | `提示词生成技能.md` + `源插图Prompt编译技能.md` | `视觉执行编译流程.md` | partial | two prompt skills, no PromptRecipe card in `60-prompts` (only legacy library) | unify; create PromptRecipe cards |
| Image execution package creation | — | `视觉资产本体技能.md` (partial) | **none** (workflows forbid it) | **MISSING/blocked** | only codex `CREATE_IMAGE_EXECUTION_PACKAGE.md` does it | wire workflows to ImageExecutionPackage |
| Prompt compile | prompt compile | `源插图Prompt编译技能.md` | `视觉执行编译流程.md` | latent | `compile-asset` exists, unwired | wire CLI |
| Semantic lint | lint | `源插图语义Lint技能.md` | (in 视觉执行编译流程) | latent | `lint-prompt`/`lint_engine` exists, unwired | wire CLI |
| External image generation handoff | image execution | `出图执行技能.md` | `外部出图工具出图窗口操作手册.md` | partial | window manual names WebGPTImage 0× | rewrite as real window manual |
| GenerationRun backfill | telemetry | `图像执行遥测技能.md` | `本地知识库回填手册.md` + codex `BACKFILL_GENERATION_RUN.md` | partial | workflow backfills story_core not GenerationRun card in `50-agent-work/runs` | redirect backfill targets |
| Image QA | multimodal QA | `Multimodal QA技能.md` | `Multimodal QA人工复核流程.md` | yes (runtime) | output folder unnamed | name 50-agent-work |
| RepairNote creation | repair | `资产验收与返修技能.md` | codex `REPAIR_FAILED_IMAGE_RUN.md` | partial | skill writes story_core; RepairNote card route only in codex | wire to RepairNote template |
| ReferenceAsset acceptance | acceptance | `资产级细粒度验收技能.md` | `图像试产与连续性验证流程.md` + codex `ACCEPT_REFERENCE_ASSET.md` | partial | skill auto-accepts; card route only in codex | subordinate to human QA; wire template |
| Rejected asset archive | — | (router skill) | **none** (no `90-archive` route in workflows) | **MISSING** | only codex routes to `90-archive/rejected-assets` | add archive route to workflow |
| Final illustrated story package assembly | publish synthesis | `平台发布页合成技能.md` | `源插图到平台发布页流程.md` | **legacy-only** | **new doctrine has no documented multi-asset assembly step** | author assembly instruction + map |
| Publishing readiness check | manual read | `人工完整阅读技能.md` | (publish workflow) | partial | downstream "发布前检查" skill absent | confirm publish tail |

**Three coverage holes that block the doctrine's data model:** (a) no Character/Scene extraction skill or workflow populates `30-characters`/`40-scenes`; (b) no workflow creates the ImageExecutionPackage / GenerationRun / RepairNote / ReferenceAsset cards (only the orphaned English codex-instructions do); (c) no documented final-package assembly in the new doctrine.

## 5. Template and metadata audit

11 templates (`…/templates/canonical-assets/`) vs 11 schemas (`…/metadata-fields/*.fields.md`). **`type` is fully normalized** (lowercase snake_case, 1:1 with fileClass); **templates and schemas agree on field keys for all 11 entities** (no schema-only or template-only fields). Weaknesses concentrate in the image-production traceability tail and status enums.

| Template | Required fields present | Required sections present | Queryable by Dataview/Bases | Risk | Verdict | Required fix |
| --- | --- | --- | --- | --- | --- | --- |
| `StoryProject.md` | yes (18 keys) | yes (10) | yes | references `worlds`/World entity with no template | OK | add World template or drop `worlds` |
| `Character.md` | yes | yes (7) | yes (`failure_count`,`visual_style`) | low | OK | none |
| `Scene.md` | yes | yes (8) | yes | `linked_packages` link present (but board queries wrong field — §dashboards) | OK | none |
| `VisualStyle.md` | yes | yes (9) | yes | low | OK | none |
| `PromptRecipe.md` | yes | yes (8) | yes (`target_media`) | low | OK | none |
| `ImageExecutionPackage.md` | yes (24 keys) | yes (**13 sections**) | yes (richest) | **heaviest template** for manual reuse | OK | add minimal short-form / mark optional sections |
| `GenerationRun.md` | yes | yes (~12) | yes | `repair_package` field actually holds a `repair_note` id (misnamed) | needs-fix | rename `repair_package`→`repair_note` |
| `RepairNote.md` | yes | yes (10) | yes (`priority`) | dup `status`+`repair_status`; **no forward link to resulting ReferenceAsset** | needs-fix | add `output_asset`→ReferenceAsset; collapse status |
| `ReferenceAsset.md` | yes | yes (11) | yes (`quality_status`) | **default `status: draft` not in enum** `candidate/accepted/rejected/deprecated`; dup `status`+`quality_status`; **no typed `source_run`** | needs-fix | fix default; add `source_run`→GenerationRun; merge status |
| `SkillCard.md` | yes (`runtime_support`,`related_workflows`) | yes (8) | yes | unused by the 32 real skill cards | OK | adopt for real skill cards |
| `WorkflowCard.md` | yes (`trigger`,`runtime_commands`,`related_skills`) | yes (9) | yes | unused by the 18 real workflows | OK | adopt for real workflows |

**Traceability chain (frontmatter only):** Package↔Run is clean and bidirectional (`last_run`/`package_id`). Run→RepairNote works but the field is misnamed (`repair_package` holds a repair_note id). **RepairNote→ReferenceAsset is BROKEN (no link field).** ReferenceAsset→originating Run is **weak** (provenance lives only in body + untyped `qa_evidence`; no typed `source_run`). `source_paths`→`01-raw` and `project_id`→StoryProject are present on **all 11** entities. `status` is bespoke per entity (acceptable as a lifecycle) but **ReferenceAsset's default violates its own enum** and two entities carry redundant dual-status fields (drift risk).

**Critical observation:** the templates correctly follow the *new* doctrine — e.g. `ReferenceAsset.fields.md:38` "证据落 `50-agent-work`，结论回填本卡". This is the model the 32 skill cards and 18 workflows do **not** follow. Templates are the strongest evidence the new doctrine is real and implementable; the skills/workflows simply have not been ported to them.

## 6. Runtime alignment audit

The runtime *behaves* as a tool layer (verified: only `runtime/.artifacts/registry.json` and `runtime/.runs/{id}/` are ever written; nothing writes to `01-raw`/`02-wiki`/`50-agent-work`; smoke-test asserts no story/image/package generation). Misalignment is in self-declared precedence, dead legacy wiring, and absence of any check enforcing the new doctrine.

| Runtime module | Current role | Should remain? | New-architecture role | Risk | Required fix |
| --- | --- | --- | --- | --- | --- |
| `contracts` | load/validate 5 JSON contracts; drift check | yes | machine-readable **validation rules only** | **`runtime/README.md:3`: "contracts are the source of truth … contracts win"** — inverts the Markdown-canonical doctrine | rewrite README precedence (contracts = rules, subordinate to 02-wiki content) |
| `skill_registry` | load `skills.json`; enforce ==`skill_definitions.json` (12 skills) | yes-but-reduce | one skill validation table | `skills.json` duplicates `skill_definitions.json` verbatim | collapse to one machine copy |
| `pipeline_runner` | dry-run plan/exec; halt at approval/external-gen; writes `.runs/` | yes | orchestration + run manifests (cache) | low (cache-only, gen blocked) | label external-gen stop as WebGPTImage handoff |
| `story_analyzer` | read-only graph diagnostics | yes | diagnostic/QA helper | none; presupposes `story_core.json` is authoritative | document input as derived from cards |
| `skill_executor` | dry-run candidates + `proposed_changes` (approval-required, non-mutating) | yes | approval-first repair proposer | none | none |
| `prompt_compiler` | spec→`compiled_prompt` | yes | compiler / cache producer | hardcodes R00 acceptance criteria (3rd copy) | source criteria from `visual_assets.json` |
| `lint_engine` | lint prompts; R00 forbidden terms from contract | yes | linter (R00 drift guard) | R01/R02/S terms hardcoded inline (`semantic_lint.py:81,86,91`) | move to `visual_assets.json` |
| `artifact_registry` | register/validate artifact id/hash/lineage; gate accepts; writes `.artifacts/` | yes-but-reframe | **derived cache** + validator | cache-by-path but **canonical-by-tone** (no "derived/rebuildable" self-description) | add "derived cache, not canonical" docstring |
| `multimodal_qa` | schema-only human image-review validation; pass-only→accept | yes | human-in-loop QA helper | none | none |
| `tests` | 74 smoke checks incl. "does-not-generate" guards | yes-but-fix | boundary + behavior regression | **guards scan deleted legacy roots** (`故事项目`,`资产库`,`执行包`,`发布包`) → vacuously pass; **0 references to `01-raw/02-wiki/50-agent-work/90-archive`** | repoint guards at new layers; add 4-layer doctrine tests |

**Drift-catching (the 9 cases):** (a) wrong-layer writes — **NO** validator; (b) missing canonical card — **PARTIAL** (R00-only via `check-contract-drift`); (c) missing GenerationRun — PARTIAL (artifact-level); (d) missing RepairNote — **NO** (no RepairNote artifact type); (e) missing ReferenceAsset — **YES**; (f) accepted image without QA — **YES** (strong); (g) prompt recipe drift — PARTIAL (hash stored, not diffed); (h) reference asset drift — PARTIAL (same); (i) story-fact drift — **NO** (no card↔JSON reconciliation). **Dead legacy paths still in code:** `core/io.py:45` probes `故事核心.json`; `pipeline_actions.json:11` gates on `concrete_story_project_exists`; `validate_contracts.py:166` `HISTORICAL_STORY_PATTERNS`.

## 7. End-to-end dry-run result

Hypothetical: a user provides a short eerie children-safe illustrated story. Walking the 14 expected steps:

1. **Raw input → `01-raw/story-lab/user-inputs/<project-id>/`.** Supported by: codex `START_NEW_STORY_OBSIDIAN_WIKI.md` (correct layer). Missing: the `故事输入与版权改编技能` skill never references `01-raw`. Fails if: operator follows the skill, not the codex-instruction. Improve: wire intake skill to `01-raw`.
2. **StoryProject card → `02-wiki/.../10-projects/`.** Supported by: `StoryProject.md` template + codex-instruction. Missing: no *workflow/skill* creates it (workflows create `故事核心.json`). Fails if: operator runs the SOP workflow. Improve: reconcile JSON-vs-card model.
3. **Character cards → `30-characters/`.** Supported by: `Character.md` template only. **Missing: no skill or workflow extracts characters.** Fails: nothing produces these cards. Improve: author Character-extraction skill+workflow.
4. **Scene cards → `40-scenes/`.** Same as step 3 — **template only, no producer.** Improve: author Scene-extraction skill+workflow.
5. **VisualStyle cards → `50-visual-styles/`.** Supported by: `VisualStyle.md` + `视觉设定技能`. Missing: skill writes `story_core.visual_rules`, not a card. Improve: wire to template.
6. **PromptRecipe cards → `60-prompts/`.** Supported by: `PromptRecipe.md` template. Missing: `60-prompts` holds only a `legacy-prompt-library/`; two prompt skills write story_core fields. Improve: unify prompt skills; emit PromptRecipe cards.
7. **ImageExecutionPackage → `70-execution-packages/`.** Supported by: `ImageExecutionPackage.md` + codex `CREATE_IMAGE_EXECUTION_PACKAGE.md`. **Blocked: 16/18 workflows forbid execution packages.** Fails: the operator-facing workflows prohibit the doctrine's central artifact. Improve: rewrite workflows to create it.
8. **runtime validates/lints/compiles.** Supported by: `compile-asset`, `lint-asset`/`lint-prompt`, `validate-telemetry`, `qa-asset` (all exist and pass smoke-test). Missing: no skill/workflow *invokes* them (0 CLI references). Improve: wire skills→CLI.
9. **WebGPTImage receives controlled execution sheet.** Supported by: `webgpt-two-window-workflow-map.md` + codex-instruction. Missing: the workflow titled `外部出图工具出图窗口操作手册.md` names WebGPTImage 0× and is an SOP clone. Fails: no usable window runbook. Improve: rewrite as a real window manual consuming the ImageExecutionPackage.
10. **Candidates → `01-raw/story-lab/generated-raw/`.** Supported by: layer exists; lineage map uses `generated-raw`. Minor inconsistency: `BACKFILL_GENERATION_RUN.md:11` lands raw in `user-inputs/`. Improve: standardize raw-output subfolder.
11. **GenerationRun/QA/review-form/RepairNote → `50-agent-work/story-lab/`.** Supported by: templates + 3 codex-instructions + runtime QA. **Missing: the `本地知识库回填手册` workflow backfills only `故事核心.json`, never `50-agent-work` or cards.** Fails: records land in the wrong model. Improve: redirect backfill.
12. **Accepted ReferenceAsset → `02-wiki/.../reference-assets/`.** Supported by: `ReferenceAsset.md` + codex `ACCEPT_REFERENCE_ASSET.md` + runtime accept-gate. Risk: template default `status: draft` is out-of-enum; no `source_run` link. Improve: fix template; route via workflow.
13. **Rejected → `90-archive/story-lab/rejected-assets/`.** Supported by: codex `REPAIR_FAILED_IMAGE_RUN.md` only. **Missing: no workflow routes to `90-archive`.** Improve: add archive route.
14. **Final illustrated package assembled after gates pass.** **Missing in the new doctrine entirely** — maps stop at a single accepted ReferenceAsset; multi-asset assembly exists only in the legacy/contradictory layer. Also, the gates that should guard it (R01/R02/semantic-lint/asset-level/human-read/pre-illustration) are **empty stub checklists** — only R00 and runtime-level QA can block. Improve: author the assembly step + fill the gates.

**Net dry-run:** every step is *individually* supported by *some* artifact — but the supporting artifact is almost always the orphaned English codex-instruction or a bare template, while the operator-facing skill/workflow points at the contradictory old model. Steps 3, 4, 7, 13, 14 have no working producer at all in the new doctrine.

## 8. Critical blockers

Only blockers that prevent reliable final production.

1. **Two contradictory operating doctrines coexist as active docs.**
   - Path: `02-wiki/story-lab/80-skills-tools-workflows/skills/*` (32 cards) + `…/workflows/*` (18) + `00-system/codex-instructions/` (19 legacy Chinese files declaring `唯一事实源：故事核心.json`, 16 referencing deleted `故事项目/`) vs. the new doctrine in `00-system/architecture/`, templates, and the 5 English codex-instructions.
   - Problem: the operator-facing layer implements the old monolithic-JSON model and contradicts the canonical-card model.
   - Why it blocks: an operator cannot follow both; the skills/workflows actively forbid the doctrine's required artifacts.
   - Fix: rewrite or retire the legacy skills/workflows/instructions onto the 4-layer card model; or formally mark them legacy and elevate the English path.
   - Priority: **P0**.

2. **Workflows forbid the ImageExecutionPackage and never write doctrine layers.**
   - Path: all 18 `…/workflows/*.md` (e.g. `故事生产标准作业流程.md:65` `禁止创建…执行包`; verified 0/18 mention `50-agent-work`/`70-execution-packages`/`reference-assets`).
   - Problem: the end-to-end image chain has no producer for ImageExecutionPackage/GenerationRun/ReferenceAsset.
   - Why it blocks: the WebGPTImage window has no doctrine-defined input; accepted assets never reach `reference-assets/`.
   - Fix: rewrite the image-side workflows to create ImageExecutionPackage (`70`), GenerationRun/QA/RepairNote (`50-agent-work`), accepted ReferenceAsset (`reference-assets`), rejected (`90-archive`).
   - Priority: **P0**.

3. **32 skill cards are unexecutable as written.**
   - Path: `…/skills/*.md` (0/32 frontmatter; 0/32 in `runtime/skill_registry/skills.json`; 4 stubs: `视觉候选失败复盘技能.md`, `发布编排技能.md`, `发布后数据回收技能.md`, `创作者技法蒸馏技能.md`).
   - Problem: no machine-loadable identity, no runtime wiring, wrong write target (`故事核心.json`), and key skills are boilerplate.
   - Why it blocks: skills can't be invoked/validated; QA/acceptance skills auto-accept without the human image-review form (QA-bypass).
   - Fix: add frontmatter (adopt `SkillCard.md`), register the production skills, wire each to its existing `aistory.py` command, redirect operational outputs to `50-agent-work`, expand the 4 stubs, and subordinate `资产级细粒度验收` to the human `Multimodal QA` form.
   - Priority: **P0**.

4. **Image-pipeline acceptance gates are hollow.**
   - Path: `…/acceptance-checklists/` (20/29 byte-identical stubs incl. `资产级细粒度验收清单.md`, `源插图语义Lint验收清单.md`, `人工完整阅读清单.md`, `R01角色锚图验收清单.md`, `R02场景道具锚图验收清单.md`, `完整故事出图前验收清单.md`) and `…/structure-specs/` (15/25 stubs).
   - Problem: only R00 and runtime-module checks enforce anything; R01/R02/lint/asset-level/human-read/pre-illustration gates have no pass/fail criteria.
   - Why it blocks: accepted images and the final package are essentially unguarded beyond R00 — the system can publish unvalidated output.
   - Fix: port the criteria that already exist in the fleshed-out structure-specs and `00-dashboard/legacy-control/状态机与门禁.md` into the stub checklists.
   - Priority: **P1**.

5. **No documented final-package assembly in the new doctrine.**
   - Path: `02-wiki/story-lab/maps/story-production-system-map.md` (stops at single accepted ReferenceAsset); assembly only in legacy `00-system/codex-instructions/生成平台发布页排版方案.md`.
   - Problem: the intended deliverable — a complete illustrated multi-image story package — has no current-doctrine step.
   - Why it blocks: the system can accept individual assets but cannot assemble the final output without re-using the contradicted legacy model.
   - Fix: author an English codex-instruction + map + WorkflowCard for project-level assembly into `02-wiki`.
   - Priority: **P1**.

6. **Broken/weak traceability links in the image tail.**
   - Path: `…/templates/canonical-assets/ReferenceAsset.md` (default `status: draft` ∉ enum; no `source_run`), `RepairNote.md` (no forward link to ReferenceAsset; dup status), `GenerationRun.md` (`repair_package` misnamed).
   - Problem: `RepairNote→ReferenceAsset` chain is unlinkable; accepted-asset provenance is not query-traceable.
   - Why it blocks: lineage/QA audit and dashboards under-report; drift cannot be traced.
   - Fix: add `RepairNote.output_asset` and `ReferenceAsset.source_run`; fix the ReferenceAsset default; rename `repair_package`→`repair_note`.
   - Priority: **P1**.

7. **runtime/README declares contracts canonical (doctrine inversion).**
   - Path: `runtime/README.md:3` "contracts are the machine-readable source of truth … If Markdown conflicts with contracts, contracts win."
   - Problem: directly contradicts `00-system/runtime-boundary/Markdown-Is-Canonical.md:7`.
   - Why it blocks: it reframes the tool layer as the canonical system, undermining the whole wiki-canonical premise for any reader who starts in `runtime/`.
   - Fix: restate as "contracts own validation *rules*; 02-wiki Markdown owns production *knowledge*" (the resolution the 00-system docs already use).
   - Priority: **P1**.

## 9. Non-blocking improvements

- **Dashboard field-binding bugs** (boards under-report once cards exist): `image-package-board` queries `package_id` but the template id field is `id`; `bases/scene-board.base` queries `related_assets` instead of `linked_packages`; `bases/reference-asset-gallery.base` images on `cover_image` (ReferenceAsset has `file_location`); `bases/repair-queue.base` filters `repair_status != "done"` but the enum value is `closed`. Fix the four bindings and purge non-enum status values from comments/prose (`active`,`pending`,`done`,`running`,`blocked`,`success`,`partial`,`approved`).
- **Carry the R00-overload guard into the new doctrine.** The "R00 must not contain characters/stick-figures/full scenes/prop sets/symbol scatter; R00-not-accepted blocks R01/R02" rule lives only in legacy `建立视觉资产本体.md:49`. Add it to `ImageExecutionPackage.md`/`ReferenceAsset.md` and cap how many packages may reuse one R00 anchor.
- **Reduce rule duplication:** R00 criteria are encoded in 3 places (contract + `qa_engine` + `prompt_compiler`); collapse `skills.json` into `skill_definitions.json` (loader already supports it); move R01/R02/S forbidden terms from `lint_engine` inline literals into `visual_assets.json`.
- **Repoint runtime tests at the new layers** and add positive tests asserting the 4-layer write rules (currently 0 references to `01-raw/02-wiki/50-agent-work/90-archive`).
- **Add a `StoryProject.worlds` World template** or drop the field.
- **Update the docs that advertise only 5 runtime commands** — there are ~45; `validate` does not check `02-wiki`. Consider a real `validate-vault` that checks card presence/layer placement.
- **Provide short-form variants** of the heaviest templates (`ImageExecutionPackage` 13 sections, `GenerationRun`, `ReferenceAsset`) for repeated manual use.

## 10. Redundancy and simplification recommendations

- **Workflows (merge):** 11 of 18 are clones of one 18-stage SOP. Keep `平台图文故事生产流程.md` (runtime-integrated) as the single main-line SOP; demote `故事生产标准作业流程.md` and `新故事从输入到试产流程.md` to redirects; convert `视觉执行编译/图像试产/源插图到发布页/长故事扩展/story_graph钩子强化/创作者技法蒸馏/本地知识库回填` into short phase-notes referencing the SOP instead of re-cloning all 18 stages + gates. **Rewrite** `外部出图工具出图窗口操作手册.md` from a clone into a real WebGPTImage window manual. The 7 distinct files (`Artifact Registry`, `Contracts`, `Multimodal QA`, `Pipeline Runner`, `Skill Executor`, `Skill Runtime`, `Story Analyzer`) are healthy — keep.
- **Skills (merge/deprecate):** fold `提示词生成技能` into `源插图Prompt编译技能` (or hard-define the fragment→compiled handoff); merge `总控编排技能` into Pipeline Runner; reconcile the QA quartet `资产级细粒度验收`(decide) / `资产验收与返修`(route) / `视觉候选失败复盘`(post-mortem) / `Multimodal QA`(human form) onto **one canonical accepted store** gated by the human form; deprecate the 3 off-path stubs (`视觉候选失败复盘`,`发布编排`,`发布后数据回收`) or rebuild them; collapse `视觉设定`↔`视觉资产本体` policy overlap; reconcile Story Analyzer's weakness-detection with the dedicated hook/page/minimization skills.
- **Checklists/specs (deduplicate):** 20/29 checklists and 15/25 specs are byte-identical boilerplate — replace with filled content ported from `legacy-control/状态机与门禁.md` and the fleshed specs; collapse the 5-way source-illustration checklist fragmentation (4 are identical).
- **Reconcile the two control systems:** `00-dashboard/legacy-control/` already encodes the gate model the empty checklists are meant to provide — pick one source of truth (the specs forbid a second) and delete or fold the other.

## 11. Final answer to the core question

**Verdict:** NOT READY (foundations solid; operator-facing layer is the wrong doctrine and the final assembly step is missing).

**Reason:** The architecture, the 11 canonical templates, the runtime tool layer, and the 5 English codex-instructions form a coherent path from a user story to accepted reference assets. But the layer an operator actually uses — the 32 skill cards and 18 workflows — implements the abandoned monolithic-`故事核心.json` model, has no frontmatter/registry/runtime wiring, contains 4 unexecutable stubs, and **explicitly forbids the ImageExecutionPackage the doctrine requires** while never writing to `50-agent-work`/`70-execution-packages`/`reference-assets`. The acceptance gates are 20/29 empty stubs (only R00 is real), and the **final illustrated-package assembly step is undocumented in the new doctrine**. The system therefore cannot *reliably* reach a complete illustrated story package as currently structured, even though individual stages are achievable by an expert hand-following the English instructions + runtime CLI.

**Required fixes before first pilot (P0):**
1. Choose one doctrine; rewrite or formally retire the 32 skill cards + 18 workflows + 19 legacy codex-instructions onto the canonical-card / 4-layer model.
2. Make the image-side workflows create ImageExecutionPackage (`70`) → GenerationRun/QA/RepairNote (`50-agent-work`) → accepted ReferenceAsset (`reference-assets`) → rejected (`90-archive`); remove the `禁止…执行包` prohibition.
3. Give the production skill cards frontmatter, register them, wire each to its existing `aistory.py` command, and redirect operational outputs to `50-agent-work`; expand the 4 stubs; subordinate auto-acceptance to the human image-review form.
4. Author the final-package assembly step (instruction + map + WorkflowCard) in the new doctrine.
5. Fix the ReferenceAsset/RepairNote/GenerationRun template chain links and the out-of-enum `status` default.

**Required fixes before scale production:**
- Fill the 20 stub acceptance-checklists and 15 stub structure-specs (port from `状态机与门禁.md` + fleshed specs); add Character/Scene extraction skills+workflows; fix `runtime/README.md` precedence; repoint runtime tests at the new layers and add wrong-layer-write + card-presence validation; fix the 4 dashboard field bindings; carry the R00-overload guard into the canonical templates; deduplicate the rule copies (R00/skills.json) and the legacy-control vs checklists control systems.

**Manual configuration needed:** Obsidian with Dataview + Bases enabled; `python3` (3.13 present) for the runtime CLI; an operator who knows to follow the English codex-instructions (not the legacy skills/workflows); an external WebGPTImage generation surface; and, until fixes land, manual hand-off between the runtime CLI and card creation (no command creates cards).

**Remaining risk:** Even after wiring, the dominant residual risks are **QA-bypass** (acceptance can occur without the human image-review form; gates are mostly empty), **story-fact / reference / prompt drift** (no validator reconciles `story_core` JSON against canonical cards; recipe/reference hashes are stored but not diffed; the strongest auto R00 guard in `lint_engine` is currently unwired), **R00 anchor overload** (guard exists only in the legacy layer), and **doctrine relapse** (the contradictory legacy docs remain active and will mislead operators until retired).
