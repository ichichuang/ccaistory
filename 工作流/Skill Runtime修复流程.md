# Skill Runtime修复流程

状态：活动  
生产体系：平台图文故事主线生产体系

## 1. 入口
入口来自已选择 skill 的 story_graph。Skill Orchestrator 已完成 skill selection 后，Skill Runtime 才能运行。

## 2. 流程
1. 读取 story_graph.nodes。
2. 对每个 node 运行 evaluator。
3. evaluator 读取 node.applied_skills，并根据 `skills.json` 检查 validation_questions、hard_failures 和关键字段。
4. 未通过节点交给 Patch Generator。
5. Patch Generator 使用 repair_actions 生成结构化 patch，不生成文学正文。
6. Patch Applier 以 dry-run 或建议写入方式把 patch 记录到 repair_suggestions、technique_notes、required_rewrite_fields。
7. Repair Loop 汇总 graph_repair_plan。
8. 根据结果设置 next_action。

## 3. next_action 规则
- 任一节点失败：`repair_story_graph_with_skill_patches`
- 全部节点通过：`proceed_to_visual_manifest_or_next_gate`

## 4. 失败回退
- 缺关键字段：回退到 story_graph 修复。
- applied_skills 为空：回退到 Skill Orchestrator。
- 结尾缺 opening_callback：回退到结尾回收修复。
- middle_escalation 缺 threat_delta 或升级说明：回退到递进结构修复。

## 5. 产物边界
本流程只产生 JSON 输出和节点级修复建议。不得创建故事项目、图片、执行包、发布包、备份或复盘归档。
