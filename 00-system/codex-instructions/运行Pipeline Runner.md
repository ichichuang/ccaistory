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
