# Story Analyzer 分析报告

本文件为派生视图。  
唯一事实源：故事核心.json。  
如内容冲突，以故事核心.json 为准。

## 1. 分析对象

项目编号：KHN2_001  
故事编号：故事0001  
标题：楼道里的红贴纸  
分析命令：`python runtime/aistory.py analyze-story --story-core '故事项目/KHN2_001_楼道里的红贴纸/故事核心.json'`

## 2. story_type 判断

Story Analyzer 判断为：`platform_horror`  
confidence：0.66  
reason_codes：`platform_horror_signal`  
recommended_global_skills：`page_turn_hook`、`platform_completion_rate`、`horror_escalation`

## 3. 页数建议

recommended_pages：8  
minimum_pages：6  
maximum_pages：8  
reason_codes：`single_anomaly_single_callback_micro_story`  
risk_if_shortened：无

## 4. 风险判断

整体结果：pass  
高风险：否  
repair_priority：空  
线索 ledger：无 failure，`red_sticker_arrow`、`unused_door`、`wrong_recipient_misdirection` 均已 payoff。  
张力曲线：无 failure，midpoint_status 为 `upgrading`。  
角色牵引：通过，无 missing_stakes，无 weak_nodes。

## 5. 推荐 skill plan

selected_skill_set：`page_turn_hook`、`platform_completion_rate`、`horror_escalation`

| 节点 | 页码 | 推荐技能 |
|---|---:|---|
| S01 | 1 | everyday_anomaly, page_turn_hook, emotional_pull |
| S02 | 2 | horror_escalation, misdirection_disproof, page_turn_hook |
| S03 | 3 | horror_escalation, child_perspective_wonder, page_turn_hook |
| S04 | 4 | misdirection_disproof, horror_escalation, page_turn_hook |
| S05 | 5 | horror_escalation, misdirection_disproof, platform_completion_rate |
| S06 | 6 | strange_tale_twist, horror_escalation, page_turn_hook |
| S07 | 7 | fate_loop, strange_tale_twist, emotional_pull |

required_graph_fields：`applied_skills`、`final_hook_sentence`、`next_page_question`、`reader_retention_goal`、`technique_notes`、`typed_hook`

## 6. 是否允许进入 Skill Executor

允许。Analyzer 输出 `passed=true`，无阻断问题，下一步可执行 `execute_skill_graph`。

## 7. 是否存在阻断问题

不存在。  
当前仍阻断图片、Prompt 包、WebGPT 执行包、完整生成、发布包、发布和发布计划。

## 8. 下一步建议

运行 Skill Executor dry-run：

```bash
python runtime/aistory.py execute-skill-graph --graph '故事项目/KHN2_001_楼道里的红贴纸/故事核心.json'
```
