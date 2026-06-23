# 运行Artifact Registry校验

在项目根目录执行：

```bash
python runtime/aistory.py artifact-check-registry
python runtime/aistory.py smoke-test
python runtime/aistory.py validate
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python -m compileall -q runtime
```

如需使用隔离 registry 验证：

```bash
python runtime/aistory.py artifact-register --artifact <artifact_json_path> --registry <test_registry_path>
python runtime/aistory.py artifact-lineage --artifact-id <artifact_id> --registry <test_registry_path>
python runtime/aistory.py artifact-validate --artifact-id <artifact_id> --registry <test_registry_path>
```

校验目标：

- 不允许同名候选覆盖。
- 不允许无 telemetry accepted。
- 不允许无 QA accepted。
- `rejected` / `deprecated` asset 不得作为参考依赖。
- accepted reference asset 必须能追溯到 compiled_prompt、external_generation_candidate、execution_telemetry 和 asset_qa_result。
