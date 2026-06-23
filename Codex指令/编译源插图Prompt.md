# 编译源插图Prompt

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：故事核心.json

## 1. 任务定位
把资产本体编译为可发送给外部出图工具的 compiled_prompt，但不执行出图。

成功时写入 `machine_state.current_state=source_prompt_compiled`，并把 `next_allowed_action` 设为 `run_source_prompt_semantic_lint`。本指令是可执行 SOP，不依赖“按某流程执行”这类外包描述。

## 2. 前置状态要求
- `visual_asset_ontology_passed` 已通过。
- 每个待编译资产必须有本体 JSON 和验收问题。

前置状态不满足时停止，不创建替代文件，不猜测缺失字段。

## 3. 必须读取的文件
- 故事项目/<project_id>/故事核心.json
- 故事项目/<project_id>/视觉资产本体/<asset_id>.json
- 模板/源插图Prompt编译模板.json
- 结构规范/源插图Prompt编译结构规范.md
- 提示词库/源插图Prompt编译规则.md
- 提示词库/负面约束.md
- 生产技能/源插图Prompt编译技能.md
- 验收清单/源插图Prompt编译验收清单.md

## 4. 允许创建或更新的文件
- 故事项目/<project_id>/源插图Prompt编译/<asset_id>.json
- 故事核心.json.visual_pipeline.compiled_prompts
- 故事核心.json.machine_state

所有写入必须能从 `故事核心.json.derived_views` 或 `visual_pipeline` 回溯。

## 5. 禁止行为
- 不运行 Git 命令。
- 不创建历史故事、测试故事、图片、执行包、发布包、备份或复盘归档。
- 不调用 WebGPT、外部出图工具或任何自动批量生成图片能力，除非本阶段明确是人工外部单张执行后的回填。
- 不跳过上游门禁，不把派生视图当成第二事实源。
- 不引用历史故事名、历史 asset_id、旧项目或失败案例。

## 6. 详细执行步骤
1. 逐资产读取本体，不直接从故事正文拼 prompt。
2. 按模板生成 compiled_prompt、positive_constraints、negative_constraints 和 asset_specific_acceptance_criteria。
3. 把 reference_dependencies 原样带入 prompt 依赖段。
4. R00 prompt 必须明确禁止人物、火柴人、完整场景、道具集合和符号散点表。
5. 编译完成后只允许进入语义 Lint。

## 7. 质量门禁
- 没有 compiled_prompt 不得生成试产任务。
- compiled_prompt 不得包含互相矛盾的允许项和禁止项。
- 不得调用外部出图工具。

## 8. machine_state 更新规则
- 成功：写入 `current_state=source_prompt_compiled`、`gate_result=passed`、`next_allowed_action=run_source_prompt_semantic_lint`。
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
- 下游入口只开放 `run_source_prompt_semantic_lint`。

## 12. 返回报告格式
- 是否完成：是/否
- 当前状态：source_prompt_compiled
- 下一允许动作：run_source_prompt_semantic_lint
- 已读取文件：列出实际读取路径
- 已创建或更新文件：列出实际路径
- 门禁结果：passed/rework_required/blocked
- blocked_actions：列出当前阻断动作
- 失败回退位置：如无则写“无”
- 残余风险：如无则写“无”
