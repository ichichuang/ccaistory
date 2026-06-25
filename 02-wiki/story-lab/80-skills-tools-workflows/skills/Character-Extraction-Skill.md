---
type: skill_card
id: "Character-Extraction-Skill"
title_zh: 角色抽取技能
title_en: Character Extraction Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, extraction]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: character_scene_extraction
runtime_commands: []
runtime_support_status: manual_only
input_layer: "02-wiki"
output_layer: "02-wiki"
human_gate: yes
qa_gate: no
workflow_dependencies: ["C-Character-and-Scene-Extraction-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 角色抽取技能 / Character Extraction Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
把稳定的故事图拆解为可独立维护的 Character canonical 卡，填补此前缺失的角色抽取环节。

## Inputs / 输入
- StoryProject 卡、稳定 story_graph、`01-raw` 原始输入（仅参考）。

## Outputs / 输出
- `02-wiki/story-lab/30-characters/<id>.md`（按 `templates/canonical-assets/Character.md`），含 `project_id`、`visual_lock`、`forbidden_changes`。

## Preconditions / 前置条件
- StoryProject 与 story_graph 已稳定（B 工作流完成）。

## Runtime Support / Runtime 支撑
- manual_only（可用 Story Analyzer 的诊断结果辅助；runtime 不创建角色卡）。

## Human Review Gate / 人工复核门禁
- 抽取出的角色 canon 必须人工复核签收：与故事图一致、无遗漏、无冲突。

## Failure Modes / 失败模式
- 角色定义与故事图冲突 / 视觉锁缺失 / 把同一角色拆成多卡。回退到 C 工作流或 B 重审故事图。

## Related Workflows / 关联工作流
- `workflows/C-Character-and-Scene-Extraction-Workflow.md`
