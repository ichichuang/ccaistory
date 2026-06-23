# Skill Executor候选修复流程

状态：活动  
生产体系：平台图文故事主线生产体系

## 1. 入口
入口来自已运行 Skill Runtime 的 node 或 story_graph。Skill Runtime 负责发现问题并生成 patch，Skill Executor 只处理候选修复和人工批准前的 proposed_changes。

## 2. 流程
1. 读取 node 或 story_graph。
2. 调用 Skill Runtime evaluator。
3. 调用 patch_generator 生成结构化 patch。
4. Candidate Generator 基于规则生成 candidates。
5. Candidate Scorer 对 candidates 评分并阻断硬失败。
6. Conflict Resolver 输出 resolution_plan。
7. Proposed Changes 汇总最高分候选。
8. 输出 next_action。

## 3. next_action 规则
- 有 `proposed_changes`：`review_skill_executor_proposed_changes`
- 无问题：`proceed_to_next_gate`

## 4. 人工批准
所有 `proposed_changes` 必须人工批准后才能应用。未批准不得进入 graph integrity gate，也不得生成视觉资产、图片、执行包或发布包。

## 5. 安全边界
- 不允许作者风格模仿。
- 不允许空泛吓人。
- 不允许血腥或成人危险细节。
- 不允许为了钩子牺牲清晰度和儿童安全。
- 默认 dry-run，不写正式 story_graph 字段。
