# AI Story Compiler v0.1

`runtime/` is the executable layer for the AI+Story vault. `runtime/contracts/` is the machine-readable source of truth; Obsidian Markdown is the explanatory layer. If Markdown conflicts with contracts, contracts win.

Skill Runtime v0.2 adds deterministic validation for creator-technique effects on `story_graph.nodes`. Skill Orchestrator selects skills; Skill Runtime checks whether those skills actually appear in node structure, generates repair patches, and decides whether the graph can proceed to the next gate.

Skill Executor adds the dry-run candidate layer. Skill Runtime discovers failures and produces patches; Skill Executor turns those patches into structured candidates, scores them, resolves conflicts, and emits `proposed_changes`. It does not write formal story fields. Every proposed change requires human approval before application.

Pipeline Runner adds the dry-run orchestration layer. It reads `pipeline_actions.json`, `state_machine.json`, and `quality_gates.json` to produce auditable plans, run manifests, checkpoints, and recovery status. Pipeline Runner does not replace human aesthetic approval and does not call external image tools.

Story Analyzer adds the content-aware diagnostic layer between Skill Runtime and Skill Executor. It reads `story_core` or `story_graph`, diagnoses story type, page count, node weaknesses, clue payoff, tension curve, and character stakes, then emits `recommended_skill_plan`, `repair_priority`, and `next_action`. It does not rewrite content.

## Commands

Run all commands from the project root.

```bash
python runtime/aistory.py status
python runtime/aistory.py validate
python runtime/aistory.py list-contracts
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py list-actions
python runtime/aistory.py can-run --project <project_path> --action <action>
python runtime/aistory.py analyze-story --story-core <story_core_json_path>
python runtime/aistory.py analyze-graph --graph <story_graph_json_path>
python runtime/aistory.py classify-story --story-core <story_core_json_path>
python runtime/aistory.py estimate-pages --story-core <story_core_json_path>
python runtime/aistory.py analyze-clues --graph <story_graph_json_path>
python runtime/aistory.py analyze-tension --graph <story_graph_json_path>
python runtime/aistory.py analyze-stakes --graph <story_graph_json_path>
python runtime/aistory.py select-skills --story-type horror --pages 12
python runtime/aistory.py plan-node-skills --page-role opening --page-index 1 --pages 12
python runtime/aistory.py evaluate-node --node <node_json_path>
python runtime/aistory.py generate-skill-patch --node <node_json_path>
python runtime/aistory.py check-skill-graph --graph <story_graph_json_path>
python runtime/aistory.py repair-skill-graph --graph <story_graph_json_path> --dry-run
python runtime/aistory.py execute-skill-node --node <node_json_path>
python runtime/aistory.py execute-skill-graph --graph <story_graph_json_path>
python runtime/aistory.py score-skill-candidate --candidate <candidate_json_path>
python runtime/aistory.py resolve-skill-conflicts --candidates <candidates_json_path>
python runtime/aistory.py check-graph --project <project_path>
python runtime/aistory.py compile-asset --spec <path_to_visual_asset_spec.json>
python runtime/aistory.py lint-asset --spec <path_to_visual_asset_spec.json>
python runtime/aistory.py lint-prompt --compiled <path_to_compiled_prompt.json>
python runtime/aistory.py validate-telemetry --telemetry <path_to_telemetry.json>
python runtime/aistory.py qa-asset --qa <path_to_asset_qa_result.json>
python runtime/aistory.py pipeline-plan --until semantic_lint
python runtime/aistory.py pipeline-plan --project <project_path> --until <gate>
python runtime/aistory.py pipeline-run --until semantic_lint --dry-run
python runtime/aistory.py pipeline-run --project <project_path> --until <gate> --dry-run
python runtime/aistory.py pipeline-status --run-id <run_id>
python runtime/aistory.py pipeline-resume --run-id <run_id> --dry-run
python runtime/aistory.py list-runs
python runtime/aistory.py smoke-test
```

## Runtime Boundary

- Machine rule changes start in `runtime/contracts/`, then docs and tests are synchronized.
- The runtime does not create story projects.
- The runtime does not generate images.
- The runtime does not create execution packages or publishing packages.
- Pipeline Runner defaults to dry-run and only writes run artifacts under `runtime/.runs/{run_id}/`.
- Pipeline Runner actions, state transitions, and gates must come from contracts.
- Story Analyzer high-risk results must stop before Skill Executor.
- External image execution must stop at `waiting_for_external_generation`.
- Skill Runtime repair is metadata-first: patch applier writes repair suggestions and required rewrite fields, not final story prose.
- Skill Executor candidate repair is approval-first: it emits `proposed_changes` with `human_approval_required=true` and does not overwrite `story_graph` fields.
- Author style imitation is forbidden.
- Hook strength must not override clarity or child safety.
- External image execution must be preceded by Prompt compilation and semantic lint.
- Asset acceptance requires execution telemetry and asset QA.

## Pipeline Runner

- `pipeline_runner.planner` returns `empty_state_plan`, blocked plans, missing-input plans, or ordered steps.
- `pipeline_runner.executor` accepts planner output and runs the dry-run framework without creating story files.
- `pipeline_runner.checkpoint` writes `runtime/.runs/{run_id}/checkpoint.json`.
- `pipeline_runner.run_manifest` writes `runtime/.runs/{run_id}/run_manifest.json`.
- `pipeline_runner.recovery` returns `repair_required`, `approval_required`, `external_generation_required`, `resume_available`, or `complete`.

## Skill Runtime

- `skill_orchestrator` is responsible for selecting skills.
- When `story_analysis_result.recommended_skill_plan` exists, `skill_orchestrator` prioritizes Analyzer advice.
- `skill_runtime.evaluator` verifies node fields, applied skills, validation questions, and hard failures.
- `skill_runtime.patch_generator` converts failures into structured repair instructions using `skills.json` repair actions.
- `skill_runtime.patch_applier` records suggestions in `repair_suggestions`, `technique_notes`, and `required_rewrite_fields`.
- `skill_runtime.repair_loop` creates `graph_repair_plan` and sets `next_action`.

## Story Analyzer

- `story_analyzer.story_type_classifier` classifies story type and recommends global skills.
- `story_analyzer.page_count_estimator` estimates page ranges and shortening risk.
- `story_analyzer.node_diagnostics` checks node-level story weaknesses.
- `story_analyzer.clue_ledger` blocks unpaid and orphan clues.
- `story_analyzer.tension_curve` blocks flat or declining middle sections.
- `story_analyzer.character_stakes` blocks missing reader-care reasons and observer-only protagonists.
- `story_analyzer.analyzer` aggregates diagnostics into `story_analysis_result`.
- Analyzer does not rewrite content. Content repair remains `Skill Executor -> proposed_changes -> human approval`.

## Skill Executor

- `skill_executor.candidate_generator` creates structured candidates from Skill Runtime patches without calling external LLMs.
- `skill_executor.candidate_scorer` scores candidates across clarity, hook strength, next-page pull, emotional pull, skill alignment, safety, originality, and platform readability.
- `skill_executor.conflict_resolver` identifies field-level conflicts such as hook strength versus clarity and threat escalation versus child safety.
- `skill_executor.proposed_changes` selects the highest-scoring safe candidate per field and marks it for human approval.
- `skill_executor.executor` exposes node and graph dry-run execution.
