# Pipeline Runner结构规范

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：`runtime/contracts/`

## 1. 定位
Pipeline Runner 是 `runtime/` 的阶段编排层，负责把 contracts、状态机、门禁和 dry-run 执行记录串成可规划、可阻断、可恢复、可审计的流水线。

Pipeline Runner 不创建新故事，不创建故事项目，不生成图片，不生成源插图试产任务清单实例，不生成执行包或发布包。

## 2. 模块
- `runtime/pipeline_runner/planner.py`：读取 `pipeline_actions.json`、`state_machine.json`、`quality_gates.json`，生成计划。
- `runtime/pipeline_runner/executor.py`：接收计划并执行 dry-run 框架。
- `runtime/pipeline_runner/checkpoint.py`：写入和读取 `runtime/.runs/{run_id}/checkpoint.json`。
- `runtime/pipeline_runner/run_manifest.py`：写入和读取 `runtime/.runs/{run_id}/run_manifest.json`。
- `runtime/pipeline_runner/recovery.py`：根据 checkpoint 判断恢复状态。
- `runtime/pipeline_runner/pipeline_errors.py`：定义 Pipeline Runner 错误边界。

## 3. Contracts 边界
contracts 是 Pipeline Runner 的机器事实源：
- action 来源必须是 `runtime/contracts/pipeline_actions.json`。
- 状态迁移来源必须是 `runtime/contracts/state_machine.json`。
- 阶段门禁来源必须是 `runtime/contracts/quality_gates.json`。
- 若 contracts 缺失或不一致，pipeline 必须失败，不得静默降级。

## 4. Planner 输出
```json
{
  "passed": true,
  "project_path": "",
  "current_state": "",
  "next_allowed_action": "",
  "requested_until": "",
  "plan": [],
  "blocked_reason": [],
  "missing_inputs": []
}
```

无项目时返回 `empty_state_plan`。有项目时必须读取 `story_core.json` 或 `故事核心.json` 中的 `machine_state`。

## 5. Checkpoint 状态
允许的 step status：
- `pending`
- `running`
- `passed`
- `failed`
- `blocked`
- `waiting_for_manual_approval`
- `waiting_for_external_generation`

checkpoint 只写入 `runtime/.runs/{run_id}/checkpoint.json`，不得写入故事项目目录。

## 6. 人工与外部边界
外部出图阶段必须停在人工执行点，并返回 `waiting_for_external_generation`。

Pipeline Runner 不替代人工审美批准。`accept_asset`、`reject_asset` 和 `run_human_complete_reading` 不得自动越过人工批准点。

accepted/rejected 前必须存在 telemetry 与 asset QA。

## 7. 默认执行方式
Pipeline Runner 默认 dry-run。dry-run 只创建 run manifest 与 checkpoint，不生成图片、执行包或发布包。
