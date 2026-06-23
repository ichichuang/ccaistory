# AI Story Compiler v0.1

`runtime/` is the executable layer for the AI+Story vault. The Obsidian documents remain the specification layer; this runtime turns the core gates into deterministic local checks.

## Commands

Run all commands from the project root.

```bash
python runtime/aistory.py status
python runtime/aistory.py validate
python runtime/aistory.py list-actions
python runtime/aistory.py can-run --project <project_path> --action <action>
python runtime/aistory.py select-skills --story-type horror --pages 12
python runtime/aistory.py plan-node-skills --page-role opening --page-index 1 --pages 12
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
- External image execution must be preceded by Prompt compilation and semantic lint.
- Asset acceptance requires execution telemetry and asset QA.
