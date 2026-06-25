---
type: codex_instruction
id: "运行Artifact Registry校验"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "runtime-cache"
related_templates: []
related_workflows: []
human_gate: yes
runtime_role: "tool-layer runner: invoke runtime CLI (validate/compile/lint/qa/cache); never canonical, never external image generation"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
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
