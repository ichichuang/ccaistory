# AI Story Compiler v0.1

`runtime/` is the executable layer for the AI+Story vault. The Obsidian documents remain the specification layer; this runtime turns the core gates into deterministic local checks.

Skill Runtime v0.2 adds deterministic validation for creator-technique effects on `story_graph.nodes`. Skill Orchestrator selects skills; Skill Runtime checks whether those skills actually appear in node structure, generates repair patches, and decides whether the graph can proceed to the next gate.

## Commands

Run all commands from the project root.

```bash
python runtime/aistory.py status
python runtime/aistory.py validate
python runtime/aistory.py list-actions
python runtime/aistory.py can-run --project <project_path> --action <action>
python runtime/aistory.py select-skills --story-type horror --pages 12
python runtime/aistory.py plan-node-skills --page-role opening --page-index 1 --pages 12
python runtime/aistory.py evaluate-node --node <node_json_path>
python runtime/aistory.py generate-skill-patch --node <node_json_path>
python runtime/aistory.py check-skill-graph --graph <story_graph_json_path>
python runtime/aistory.py repair-skill-graph --graph <story_graph_json_path> --dry-run
python runtime/aistory.py check-graph --project <project_path>
python runtime/aistory.py compile-asset --spec <path_to_visual_asset_spec.json>
python runtime/aistory.py lint-asset --spec <path_to_visual_asset_spec.json>
python runtime/aistory.py lint-prompt --compiled <path_to_compiled_prompt.json>
python runtime/aistory.py validate-telemetry --telemetry <path_to_telemetry.json>
python runtime/aistory.py qa-asset --qa <path_to_asset_qa_result.json>
python runtime/aistory.py smoke-test
```

## Runtime Boundary

- The runtime does not create story projects.
- The runtime does not generate images.
- The runtime does not create execution packages or publishing packages.
- Skill Runtime repair is metadata-first: patch applier writes repair suggestions and required rewrite fields, not final story prose.
- External image execution must be preceded by Prompt compilation and semantic lint.
- Asset acceptance requires execution telemetry and asset QA.

## Skill Runtime

- `skill_orchestrator` is responsible for selecting skills.
- `skill_runtime.evaluator` verifies node fields, applied skills, validation questions, and hard failures.
- `skill_runtime.patch_generator` converts failures into structured repair instructions using `skills.json` repair actions.
- `skill_runtime.patch_applier` records suggestions in `repair_suggestions`, `technique_notes`, and `required_rewrite_fields`.
- `skill_runtime.repair_loop` creates `graph_repair_plan` and sets `next_action`.
