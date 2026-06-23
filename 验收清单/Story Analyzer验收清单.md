# Story Analyzer 验收清单

## Runtime

- [ ] `runtime/story_analyzer/` 存在。
- [ ] Story Type Classifier 可输出 story_type、confidence、reason_codes、recommended_global_skills。
- [ ] Page Count Estimator 可输出 recommended_pages、minimum_pages、maximum_pages。
- [ ] Node Diagnostics 可诊断 weak_opening_hook。
- [ ] Clue Ledger 可阻断 unpaid_clue。
- [ ] Tension Curve 可阻断 middle_without_escalation。
- [ ] Character Stakes 可阻断 reader_care_reason_missing 或 observer_without_choice。
- [ ] Analyzer Aggregator 可输出 recommended_skill_plan、repair_priority、next_action。

## Pipeline

- [ ] `pipeline_actions.json` 包含 `analyze_story_graph`。
- [ ] `quality_gates.json` 包含 `story_analyzer_gate`。
- [ ] 高风险 Analyzer 结果不得进入 Skill Executor。
- [ ] Skill Orchestrator 优先使用 Analyzer 的 `recommended_skill_plan`。

## 边界

- [ ] 不创建故事项目。
- [ ] 不生成图片。
- [ ] 不生成执行包。
- [ ] 不生成发布包。
- [ ] 不自动改写 `story_graph`。
- [ ] 内容改写仍通过 Skill Executor `proposed_changes` 和人工批准。

## 验证命令

```bash
python runtime/aistory.py validate
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
python runtime/aistory.py analyze-graph --graph runtime/tests/fixtures/story_graph_analyzer_valid.json
```
