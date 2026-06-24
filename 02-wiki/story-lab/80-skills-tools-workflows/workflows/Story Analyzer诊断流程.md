# Story Analyzer 诊断流程

## 入口

```bash
python runtime/aistory.py analyze-story --story-core <story_core_json_path>
python runtime/aistory.py analyze-graph --graph <story_graph_json_path>
```

## 流程

1. Story Type Classifier 识别故事类型并给出全局 skill 建议。
2. Page Count Estimator 给出页数范围与压缩风险。
3. Node Diagnostics 检查每个 `story_graph node` 的内容弱点。
4. Clue Ledger 检查线索 introduction、repeat、payoff 是否闭合。
5. Tension Curve 检查开头、中段升级、结尾回扣。
6. Character Stakes 检查主角目标、恐惧、读者关心理由、关系信号和选择行为。
7. Analyzer Aggregator 汇总 `recommended_skill_plan`、`repair_priority`、`next_action`。

## Pipeline 接入

Pipeline Runner 在 `apply_skill_runtime` 后规划 `analyze_story_graph`。

- Analyzer 通过：进入 `execute_skill_graph` 或下一门禁。
- Analyzer 高风险：停止在 `story_analyzer_gate`，返回 `repair_story_graph_before_skill_executor`。

## 修复边界

Analyzer 只诊断和建议。正式内容修复仍由 Skill Executor 生成 `proposed_changes`，并要求人工批准后应用。
