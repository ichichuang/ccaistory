---
type: skill_card
id: "Scene-Extraction-Skill"
title_zh: 场景抽取技能
title_en: Scene Extraction Skill
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
# 场景抽取技能 / Scene Extraction Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
把故事图拆解为可被视觉链路引用的 Scene canonical 卡，记录所需角色、道具与连续性约束。

## Inputs / 输入
- StoryProject 卡、稳定 story_graph、已抽取的 Character 卡。

## Outputs / 输出
- `02-wiki/story-lab/40-scenes/<id>.md`（按 `templates/canonical-assets/Scene.md`），含 `characters`、`props`、`continuity_constraints`、`linked_packages`（占位）。

## Preconditions / 前置条件
- 角色抽取已完成（同一 C 工作流内）。

## Runtime Support / Runtime 支撑
- manual_only。

## Human Review Gate / 人工复核门禁
- 场景 canon 人工复核：连续性约束完整、与角色卡一致。

## Failure Modes / 失败模式
- 场景遗漏 / 连续性约束缺失 / 把分镜误当场景。回退到 C 工作流。

## Related Workflows / 关联工作流
- `workflows/C-Character-and-Scene-Extraction-Workflow.md`
