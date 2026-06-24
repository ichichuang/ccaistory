本文件为派生视图。
唯一事实源：故事核心.json。
如内容冲突，以故事核心.json 为准。

# 08 story_graph 精修验收

## 1. 状态机一致性检查

07_Skill_Executor_结果.md 记录 Skill Executor 已通过：

- failed_nodes = []
- proposed_changes = []
- manual_approval_required = false
- next_action = build_visual_asset_specs

故事核心已同步：

- current_state = skill_executor_passed
- gate_result = pass
- gate_result_label = pass
- last_gate_passed = skill_executor_passed
- next_allowed_action = build_visual_asset_specs

继续阻断：generate_images、generate_prompt_package、generate_webgpt_execution_package、full_generation、create_publish_package、publish、create_release_plan。

## 2. 页数一致性判断

Story Analyzer 原始建议：

- recommended_pages = 8
- minimum_pages = 6
- maximum_pages = 8

当前 story_graph.nodes = 7，位于允许范围内。

决策：保留 7 页，decision = accepted_with_reason。

原因：当前故事是单一异常、单一门后回扣的微型平台怪谈，7 页已完成引入、递进、反证、随身物揭示和终局回扣。扩为 8 页主要会增加一轮重复贴纸，收益低于节奏稀释风险。

风险：S05 照片证据与 S06 钥匙扣揭示承担较高信息量，后续视觉资产规格需保留照片时间线和钥匙扣特写。

## 3. edge 补强结果

story_graph.edges 保持 6 条顺序边，并已全部补齐：

- from
- to
- edge_type
- cause
- question_from_previous
- answer_in_current
- new_question_created
- clue_carried_forward
- payoff_deadline
- tension_delta

验收结果：通过。

## 4. 线索账本

| clue_id | introduced_at | repeated_at | paid_off_at | status | risk |
|---|---|---|---|---|---|
| red_sticker_arrow | S01 | S02, S03, S04, S05, S06 | S07 | paid_off | low |
| unused_door | S02 | S03, S05, S06 | S07 | paid_off | low |
| wrong_recipient_misdirection | S01 | S02, S03, S04 | S06 | paid_off | low |
| keychain_sticker | S06 |  | S07 | paid_off | low |
| blank_red_sticker | S07 |  | S07 | loop_hook_paid_off_by_callback | low |

critical_unpaid_clues = []。

## 5. “别走错层”风险处理

处理结果：已处理。

原文“别走错层”会引入楼层错位规则，但主机制没有建立楼层错位，也没有计划回收该规则。已改为“别跟错箭头”，使短线索直接服务红贴纸路线机制。

## 6. 主角身份一致性

identity_mode = 中学生/学生主角 + 儿童安全怪谈视觉体系。

已做文本调整：

- S03：“下班回来”改为“补习班回来”。
- S02：“别走错层”改为“别跟错箭头”。

结论：主角身份已统一；视觉层继续使用儿童安全手账体系，不再与成人“下班”身份冲突。

## 7. Story Analyzer 复跑结果

命令：

```bash
python runtime/aistory.py analyze-graph --graph '故事项目/KHN2_001_楼道里的红贴纸/故事核心.json'
```

结果：

- passed = true
- repair_priority = []
- clue_failures = []
- tension_failures = []
- character_stakes.passed = true

说明：analyze-graph 使用 graph-only 输入时给出通用页数估算，不覆盖故事核心中已登记的 Story Analyzer 6-8 页建议。

## 8. Skill Executor 复跑结果

命令：

```bash
python runtime/aistory.py execute-skill-graph --graph '故事项目/KHN2_001_楼道里的红贴纸/故事核心.json'
```

结果：

- status = pass
- passed = true
- failed_nodes = []
- proposed_changes = []
- manual_approval_required = false

## 9. 是否允许进入 build_visual_asset_specs

允许进入 build_visual_asset_specs。

未生成图片、执行包、发布包、发布计划或源插图试产任务清单。

残余风险处理：已在 2026-06-24 修复 runtime contracts 主路径命名；pipeline-plan 现可从 `skill_executor_passed` 进入 `build_visual_asset_specs`，不再依赖 `build_visual_manifest/visual_manifest_ready`。
