# Story Analyzer 结构规范

## 定位

Story Analyzer 是 `runtime/story_analyzer/` 下的内容感知诊断层。它读取 `story_core` 或 `story_graph`，输出结构化诊断、skill 调度建议和修复优先级。

Analyzer 不创建故事项目，不生成图片，不生成执行包，不生成发布包，不改写 `story_graph` 正文字段。

## 输入

- `story_core`：故事 premise、source_type、target_mode、constraints、tags、页数估算字段和可选 `story_graph`。
- `story_graph`：`nodes`、`edges`、线索字段、张力字段、角色牵引字段。

## 输出

```json
{
  "passed": true,
  "story_type": {},
  "page_count": {},
  "node_diagnostics": [],
  "clue_ledger": {},
  "tension_curve": {},
  "character_stakes": {},
  "recommended_skill_plan": {},
  "repair_priority": [],
  "next_action": "proceed_to_skill_executor_or_next_gate"
}
```

高风险时：

```json
{
  "passed": false,
  "next_action": "repair_story_graph_before_skill_executor"
}
```

## 子模块

- `story_type_classifier.py`：识别 micro_horror、platform_horror、classic_adaptation、rule_horror、folk_strange_tale、child_safe_mystery、emotional_suspense、unknown。
- `page_count_estimator.py`：估算 recommended_pages、minimum_pages、maximum_pages。
- `node_diagnostics.py`：检查单节点钩子、翻页问题、情绪牵引、信息增量、视觉记忆点、悬念类型、payoff 目标。
- `clue_ledger.py`：提取 introduction、repeat、payoff，阻断 orphan、unpaid、repeated_without_escalation。
- `tension_curve.py`：计算 threat_level、uncertainty、emotional_pressure、information_gain、next_page_pull。
- `character_stakes.py`：检查 protagonist_want、protagonist_fear、reader_care_reason、relationship_signal、emotional_turn。
- `analyzer.py`：聚合诊断、输出 recommended_skill_plan、repair_priority、next_action。

## 调度边界

- Skill Orchestrator 负责根据 Analyzer 的 `recommended_skill_plan` 优先调度 skill。
- Skill Runtime 和 Skill Executor 在 Analyzer 高风险时不得继续进入候选修复阶段。
- 内容改写仍由 Skill Executor 生成 `proposed_changes`，再由人工批准后应用。
