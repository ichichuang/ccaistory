---
type: skill_card
id: "Skill Executor技能"
title_zh: Skill Executor技能
title_en: Skill Executor Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: repair
runtime_commands: ["score-skill-candidate", "resolve-skill-conflicts", "execute-skill-graph"]
runtime_support_status: runtime
input_layer: "runtime-cache"
output_layer: "50-agent-work"
human_gate: yes
qa_gate: no
workflow_dependencies: []
replacement_for: ""
deprecated_by: ""
---
# Skill Executor技能

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。下文凡提及“写入 story_core / 故事核心.json / 派生视图”，一律按本卡 frontmatter 的 `input_layer`/`output_layer` 落地：操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。runtime 与 Artifact Registry 仅为派生缓存。

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
