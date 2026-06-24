# Skill Executor技能

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：Skill Runtime repair_plan

## 1. 技能目的
把 Skill Runtime 发现的问题转为可审查的候选改写指令，完成评分、冲突识别和 `proposed_changes` 汇总。

## 2. 输入
- story_graph node JSON
- story_graph JSON
- Skill Runtime evaluation
- Skill Runtime patch 或 repair_plan
- `runtime/skill_registry/skills.json`
- `runtime/contracts/`

## 3. 输出
- candidates
- candidate scores
- resolution_plan
- proposed_changes
- next_action

## 4. 职责划分
- Skill Orchestrator 负责选择 skill。
- Skill Runtime 负责发现问题和生成 patch。
- Skill Executor 负责生成候选、评分、解决冲突、形成 proposed_changes。
- Pipeline Runner 负责把 proposed_changes 阶段规划为人工批准门禁。

## 5. 允许行为
- dry-run 读取 node 或 graph。
- 生成结构化候选改写指令。
- 对候选做规则评分。
- 标记冲突和人工审查需求。
- 输出 JSON。

## 6. 禁止行为
- 不直接改写 `typed_hook`、`typed_narration`、`final_hook_sentence` 等正式字段。
- 不允许作者风格模仿。
- 不允许为了钩子牺牲清晰度和儿童安全。
- 不创建故事项目、图片、执行包或发布包。

## 7. 门禁
- invalid node 必须生成 `proposed_changes`。
- valid node 不得生成无意义 `proposed_changes`。
- invalid candidate 必须被阻断。
- 所有 `proposed_changes` 必须 `human_approval_required=true`。
