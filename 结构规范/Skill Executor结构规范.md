# Skill Executor结构规范

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：story_graph node 与 proposed_changes

## 1. 定位
Skill Orchestrator 负责选择 skill。Skill Runtime 负责发现问题并生成 patch。Skill Executor 负责基于 patch 生成候选改写指令、评分、解决冲突，并形成 `proposed_changes`。

Skill Executor 默认不直接写正式字段。所有 `proposed_changes` 必须人工批准后才能应用。

## 2. 模块
- `runtime/skill_executor/candidate_generator.py`：基于规则生成结构化 candidates，不调用外部 LLM。
- `runtime/skill_executor/candidate_scorer.py`：对 candidates 做规则评分并阻断硬失败。
- `runtime/skill_executor/conflict_resolver.py`：识别同一字段上的 skill 冲突并给出 resolution_plan。
- `runtime/skill_executor/proposed_changes.py`：选择最高分候选并汇总为 proposed_changes。
- `runtime/skill_executor/executor.py`：串联 evaluator、patch_generator、candidate_generator、candidate_scorer、conflict_resolver 和 proposed_changes。

## 3. Candidate 结构
```json
{
  "candidate_id": "",
  "node_id": "",
  "target_field": "",
  "skill_id": "",
  "repair_action": "",
  "candidate_type": "rewrite_instruction",
  "proposed_text": "",
  "rationale": "",
  "risk_flags": []
}
```

## 4. 评分维度
- clarity
- hook_strength
- next_page_pull
- emotional_pull
- skill_alignment
- safety
- originality
- platform_readability

每项 0-5。作者风格指令、空泛吓人、血腥或成人危险细节、长句过载、无 repair target、skill 不匹配均为硬失败。

## 5. proposed_changes 结构
```json
{
  "node_id": "",
  "proposed_changes": [
    {
      "field": "",
      "current_value": "",
      "recommended_candidate_id": "",
      "recommended_text": "",
      "scores": {},
      "reason": "",
      "human_approval_required": true
    }
  ]
}
```

## 6. 边界
- 不允许作者风格模仿。
- 不允许为了钩子牺牲清晰度和儿童安全。
- 不创建新故事、故事项目、图片、执行包、发布包、备份或复盘归档。
- 不调用 WebGPT 或外部出图工具。
