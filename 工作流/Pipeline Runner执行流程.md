# Pipeline Runner执行流程

状态：活动  
生产体系：平台图文故事主线生产体系

## 1. 入口
从项目根目录执行：

```bash
python runtime/aistory.py pipeline-plan --until semantic_lint
python runtime/aistory.py pipeline-run --until semantic_lint --dry-run
python runtime/aistory.py list-runs
```

有项目时增加：

```bash
python runtime/aistory.py pipeline-plan --project <project_path> --until <gate>
python runtime/aistory.py pipeline-run --project <project_path> --until <gate> --dry-run
```

## 2. 规划
Planner 读取 `pipeline_actions.json`、`state_machine.json`、`quality_gates.json`。无项目时返回 `empty_state_plan`。有项目时读取 `story_core.machine_state`，并根据 `current_state`、`gate_result`、`next_allowed_action`、`blocked_actions` 生成 ordered steps。

## 3. 执行
Executor 默认 dry-run。dry-run 只创建：
- `runtime/.runs/{run_id}/run_manifest.json`
- `runtime/.runs/{run_id}/checkpoint.json`

Executor 不生成图片，不生成执行包，不生成发布包，不写故事项目目录。

## 4. 阻断
以下情况必须停止：
- action 被 story_core 或 state_machine 的 `blocked_actions` 阻断。
- required inputs 缺失。
- contracts 缺失或不一致。
- 阶段需要人工批准。
- 阶段进入外部出图执行点。

外部出图阶段返回 `waiting_for_external_generation`。人工批准阶段返回 `waiting_for_manual_approval`。

## 5. 恢复
使用：

```bash
python runtime/aistory.py pipeline-status --run-id <run_id>
python runtime/aistory.py pipeline-resume --run-id <run_id> --dry-run
```

Recovery 只读取 checkpoint。失败阶段返回 `repair_required`，人工批准点返回 `approval_required`，外部出图点返回 `external_generation_required`。

Recovery 不自动跳过失败阶段，不自动越过人工批准点，不自动重试外部出图。
