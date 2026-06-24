# Story Analyzer 技能

## 目标

在 Skill Runtime 与 Skill Executor 之间增加内容感知诊断，避免系统只按页码或 `page_role` 调度 skill。

Story Analyzer 负责发现故事层面的弱点：

- 开头钩子弱。
- 翻页问题缺失。
- 情绪牵引缺失。
- 信息增量不足。
- 视觉记忆点弱。
- 悬念类型不清。
- payoff 目标缺失。
- 页面过载。
- 儿童安全改编风险。
- 结尾无回扣。
- 线索无 payoff。
- 中段张力持平或下降。
- 角色只观察不选择。

## 输入要求

- `story_core` 应提供 premise、source_type、target_mode、constraints、tags 或 `story_type`。
- `story_graph.nodes` 应提供钩子、正文、结尾句、翻页问题、完读目标、视觉记忆点、情绪转折、悬念类型。
- 线索建议使用 `introduced_clues`、`repeated_clues`、`payoff_target`。
- 张力建议显式提供 `threat_level`、`uncertainty`、`emotional_pressure`、`information_gain`、`next_page_pull`。
- 角色牵引建议显式提供 `protagonist_want`、`protagonist_fear`、`reader_care_reason`、`relationship_signal`、`character_choice`。

## 输出使用

- `recommended_skill_plan.selected_skill_set` 交给 Skill Orchestrator 优先使用。
- `repair_priority` 交给人工或后续修复步骤排序处理。
- `next_action = repair_story_graph_before_skill_executor` 时，Pipeline Runner 必须阻断 Skill Executor。

## 禁止行为

- 不自动改写 `story_graph`。
- 不生成最终故事正文。
- 不跳过人工批准。
- 不调用外部出图工具。
- 不生成源插图试产任务清单。
- 不创建故事项目、执行包或发布包。
