---
type: codex_instruction
id: "运行Pipeline Runner"
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
# 运行Pipeline Runner

## 目标
运行 Pipeline Runner 的规划、dry-run、状态查询与恢复检查。

## 前置条件
- 当前库必须保持空故事状态。
- 不得创建新故事。
- 不得创建故事项目。
- 不得生成图片。
- 不得调用 WebGPT 或外部出图工具。
- 不得生成源插图试产任务清单实例。
- 不得生成执行包或发布包。

## 指令
从项目根目录执行：

```bash
python runtime/aistory.py validate
python runtime/aistory.py validate-contracts
python runtime/aistory.py pipeline-plan --until semantic_lint
python runtime/aistory.py pipeline-run --until semantic_lint --dry-run
python runtime/aistory.py list-runs
```

查看单次运行：

```bash
python runtime/aistory.py pipeline-status --run-id <run_id>
python runtime/aistory.py pipeline-resume --run-id <run_id> --dry-run
```

## 验收
- 输出必须为 JSON。
- Pipeline Runner 必须默认 dry-run。
- `runtime/.runs/{run_id}/run_manifest.json` 可读取。
- `runtime/.runs/{run_id}/checkpoint.json` 可读取。
- 人工批准点不得自动越过。
- 外部出图阶段必须等待人工执行。
- accepted/rejected 前必须有 telemetry 与 asset QA。
