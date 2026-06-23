# Pipeline Runner验收清单

状态：活动  
生产体系：平台图文故事主线生产体系

## 1. 结构
- [ ] `runtime/pipeline_runner/` 存在。
- [ ] `planner.py`、`executor.py`、`checkpoint.py`、`run_manifest.py`、`recovery.py`、`pipeline_errors.py` 存在。
- [ ] `runtime/aistory.py` 暴露 pipeline CLI。

## 2. Contracts
- [ ] Pipeline Runner 读取 `pipeline_actions.json`。
- [ ] Pipeline Runner 读取 `state_machine.json`。
- [ ] Pipeline Runner 读取 `quality_gates.json`。
- [ ] contracts 缺失时失败，不静默降级。
- [ ] `validate-contracts` 能发现 pipeline action、state、gate 链接不一致。

## 3. Planner
- [ ] 无项目时返回 `empty_state_plan`。
- [ ] 有效 story_core 可生成 ordered steps。
- [ ] blocked action 必须阻断。
- [ ] required inputs 缺失必须返回 missing inputs。
- [ ] plan only 不写项目文件。

## 4. Executor
- [ ] 默认 dry-run。
- [ ] 不调用 WebGPT 或外部出图工具。
- [ ] 不生成图片。
- [ ] 不生成源插图试产任务清单实例。
- [ ] 不生成执行包或发布包。
- [ ] 外部出图阶段停在 `waiting_for_external_generation`。
- [ ] 人工批准阶段停在 `waiting_for_manual_approval`。
- [ ] accepted/rejected 前要求 telemetry 与 asset QA。

## 5. Recovery
- [ ] failed 返回 `repair_required`。
- [ ] waiting_for_manual_approval 返回 `approval_required`。
- [ ] waiting_for_external_generation 返回 `external_generation_required`。
- [ ] 不自动跳过失败阶段。
- [ ] 不自动重试外部出图。

## 6. 验证命令
```bash
python runtime/aistory.py validate
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
python runtime/aistory.py pipeline-plan --until semantic_lint
python runtime/aistory.py pipeline-run --until semantic_lint --dry-run
python runtime/aistory.py list-runs
python -m compileall -q runtime
```
