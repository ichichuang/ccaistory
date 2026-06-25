---
type: workflow_card
id: "Skill Executor候选修复流程"
title_zh: Skill Executor候选修复流程
title_en: Skill Executor Candidate-Repair Flow
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
runtime_commands: ["score-skill-candidate", "resolve-skill-conflicts", "execute-skill-graph"]
human_gates: yes
qa_gates: no
stop_conditions: []
replacement_for: ""
deprecated_by: ""
---
# Skill Executor候选修复流程

> 事实源声明（canonical doctrine）：本工作流的产物按 frontmatter 的 `input_layer`/`output_layer` 落地——原始输入 `01-raw`、canonical 卡 `02-wiki`、运行/编译/lint/QA/复核/返修记录 `50-agent-work`、被拒材料 `90-archive`、执行包 `02-wiki/story-lab/70-execution-packages`、接受的参考资产 `02-wiki/story-lab/reference-assets`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口生产模型：WebGPT 指令窗规划/复核，WebGPTImage 生成窗仅按受控执行单出图。

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
