# 运行源插图语义Lint

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：故事核心.json

## 1. 任务定位
对 compiled_prompt 做语义一致性、禁项、依赖和验收条件 Lint。

成功时写入 `machine_state.current_state=source_prompt_semantic_lint_passed`，并把 `next_allowed_action` 设为 `generate_source_illustration_pilot_task_list`。本指令是可执行 SOP，不依赖“按某流程执行”这类外包描述。

## 2. 前置状态要求
- `source_prompt_compiled` 已通过。
- 每个待测资产必须有 compiled_prompt。

前置状态不满足时停止，不创建替代文件，不猜测缺失字段。

## 3. 必须读取的文件
- 故事项目/<project_id>/故事核心.json
- 故事项目/<project_id>/源插图Prompt编译/<asset_id>.json
- 结构规范/源插图语义Lint结构规范.md
- 提示词库/源插图语义Lint规则.md
- 生产技能/源插图语义Lint技能.md
- 模板/源插图语义Lint报告模板.md
- 验收清单/源插图语义Lint验收清单.md

## 4. 允许创建或更新的文件
- 故事项目/<project_id>/源插图语义Lint/<asset_id>.md
- 故事核心.json.visual_pipeline.semantic_lint
- 故事核心.json.machine_state

所有写入必须能从 `故事核心.json.derived_views` 或 `visual_pipeline` 回溯。

## 5. 禁止行为
- 不运行 Git 命令。
- 不创建历史故事、测试故事、图片、执行包、发布包、备份或复盘归档。
- 不调用 WebGPT、外部出图工具或任何自动批量生成图片能力，除非本阶段明确是人工外部单张执行后的回填。
- 不跳过上游门禁，不把派生视图当成第二事实源。
- 不引用历史故事名、历史 asset_id、旧项目或失败案例。

## 6. 详细执行步骤
1. 检查 prompt 是否缺少画面中心、输出类型、禁项、依赖和验收条件。
2. 检查 R00 是否误含人物、火柴人、场景、道具集合或符号散点。
3. 检查 reference_dependencies 是否满足，并标记未满足依赖。
4. 对 hard_fail 给出返回 Prompt 编译的修复点。
5. 所有 hard_fail 清零后解锁试产任务清单。

## 7. 质量门禁
- 任一 hard_fail 不得进入任务清单。
- reference_dependencies 不满足不得通过。
- Lint 报告必须逐资产给出 pass/rework/blocked。

## 8. machine_state 更新规则
- 成功：写入 `current_state=source_prompt_semantic_lint_passed`、`gate_result=passed`、`next_allowed_action=generate_source_illustration_pilot_task_list`。
- 需返修：保留当前上游状态，写入 `gate_result=rework_required`，并把返修位置写入 `quality_gates.<stage>.repair_target`。
- 阻断：写入 `gate_result=blocked`，保留 `next_allowed_action=resolve_blocker`。
- 每次更新必须同步记录本阶段派生视图路径或阻断原因。

## 9. blocked_actions 更新规则
- 上游未通过时必须阻断 `generate_images`、`generate_prompt_package`、`full_generation`、`publish`。
- 视觉链路未到 `pilot_task_list_ready` 前必须阻断外部出图。
- 没有 `compiled_prompt`、`semantic_lint=passed`、`execution_telemetry`、`actual_prompt_sent_to_external_tool` 和资产级验收时，必须阻断 `asset_accept`。
- R00 未 accepted 时必须阻断依赖 R00 的 R01/R02 和 S 页资产。

## 10. 失败回退路径
- 结构字段缺失：回退到 `故事核心状态机技能` 修复 story_core。
- 上游内容不足：回退到最近一个已通过的上游阶段。
- 视觉本体或 prompt 出错：回退到视觉资产本体或 Prompt 编译，不直接改候选图。
- 外部执行事实缺失：回退到执行遥测补录；无法补录时标记 blocked。

## 11. 最终验证
- 本阶段允许写入的文件存在且可追溯。
- JSON 文件可解析。
- `machine_state`、`blocked_actions`、`quality_gates` 与本阶段结论一致。
- 没有新增故事外产物、图片、执行包、发布包、备份或复盘归档。
- 下游入口只开放 `generate_source_illustration_pilot_task_list`。

## 12. 返回报告格式
- 是否完成：是/否
- 当前状态：source_prompt_semantic_lint_passed
- 下一允许动作：generate_source_illustration_pilot_task_list
- 已读取文件：列出实际读取路径
- 已创建或更新文件：列出实际路径
- 门禁结果：passed/rework_required/blocked
- blocked_actions：列出当前阻断动作
- 失败回退位置：如无则写“无”
- 残余风险：如无则写“无”
