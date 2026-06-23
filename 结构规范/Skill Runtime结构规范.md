# Skill Runtime结构规范

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：story_graph node

## 1. 定位
Skill Orchestrator 负责选择 skill。Skill Runtime 负责评估 skill 是否真正作用到 story_graph 节点，并在未通过时生成结构化修复 patch。

Skill Runtime 不生成故事正文，不创建故事项目，不生成图片、执行包或发布包。

## 2. 模块
- `runtime/skill_runtime/evaluator.py`：评估节点字段、applied_skills、skill hard_failures 与 validation_questions。
- `runtime/skill_runtime/patch_generator.py`：根据 repair_targets 和 skills.json 的 repair_actions 生成结构化 patch。
- `runtime/skill_runtime/patch_applier.py`：默认只把 patch 写入建议字段，不直接改写正式正文。
- `runtime/skill_runtime/repair_loop.py`：遍历 story_graph.nodes，汇总 graph_repair_plan，并决定下一门禁。

## 3. Evaluator 输出
```json
{
  "passed": true,
  "node_id": "",
  "skill_failures": [],
  "missing_fields": [],
  "weak_fields": [],
  "repair_targets": []
}
```

## 4. 必查字段
- `typed_hook`
- `typed_narration`
- `next_page_question`
- `final_hook_sentence`
- `reader_retention_goal`
- `visual_memory_point`
- `technique_notes`
- `applied_skills`

## 5. 硬失败
- `typed_hook` 为空。
- `final_hook_sentence` 为空。
- 非终页 `next_page_question` 为空。
- `reader_retention_goal` 为空。
- `applied_skills` 为空或包含未知 skill。
- 结尾页缺 `opening_callback`。
- `middle_escalation` 页缺 `threat_delta` 或升级说明。

## 6. Patch 结构
```json
{
  "node_id": "",
  "patches": [
    {
      "field": "",
      "operation": "suggest_rewrite",
      "reason": "",
      "skill_id": "",
      "repair_action": "",
      "instruction": ""
    }
  ]
}
```

允许的 operation：
- `suggest_rewrite`
- `add_missing`
- `strengthen`
- `split`
- `remove`

## 7. Patch Applier 写入边界
Patch Applier 默认只写入：
- `node.repair_suggestions`
- `node.technique_notes`
- `node.required_rewrite_fields`

Patch Applier 不直接改写 `typed_narration`、`typed_hook`、`final_hook_sentence` 等正式正文。

## 8. Repair Loop 输出
- `passed`
- `failed_nodes`
- `repair_plan`
- `graph_repair_plan`
- `next_action`

任一节点失败时：
`next_action=repair_story_graph_with_skill_patches`

全部通过时：
`next_action=proceed_to_visual_manifest_or_next_gate`
