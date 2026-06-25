---
type: workflow_card
id: "Skill Runtime修复流程"
title_zh: Skill Runtime修复流程
title_en: Skill Runtime Repair Flow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: repair
trigger: ""
input_layer: "runtime-cache"
output_layer: "50-agent-work"
required_cards: []
runtime_commands: ["evaluate-node", "generate-skill-patch", "repair-skill-graph"]
human_gates: no
qa_gates: no
stop_conditions: []
replacement_for: ""
deprecated_by: ""
---
# Skill Runtime修复流程

> 事实源声明（canonical doctrine）：本工作流的产物按 frontmatter 的 `input_layer`/`output_layer` 落地——原始输入 `01-raw`、canonical 卡 `02-wiki`、运行/编译/lint/QA/复核/返修记录 `50-agent-work`、被拒材料 `90-archive`、执行包 `02-wiki/story-lab/70-execution-packages`、接受的参考资产 `02-wiki/story-lab/reference-assets`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口生产模型：WebGPT 指令窗规划/复核，WebGPTImage 生成窗仅按受控执行单出图。

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
