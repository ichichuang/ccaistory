---
type: workflow_card
id: "C-Character-and-Scene-Extraction-Workflow"
title_zh: C 角色与场景抽取工作流
title_en: C. Character and Scene Extraction Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, extraction]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: character_scene_extraction
trigger: "故事图已稳定（B 完成）"
input_layer: "02-wiki"
output_layer: "02-wiki/story-lab/30-characters, 02-wiki/story-lab/40-scenes"
required_cards: ["StoryProject"]
runtime_commands: []
human_gates: yes
qa_gates: no
stop_conditions: ["故事图缺失", "角色/场景定义冲突"]
replacement_for: ""
deprecated_by: ""
---
# C 角色与场景抽取工作流 / Character and Scene Extraction Workflow

> Doctrine：角色/场景 canonical 卡落 `02-wiki/story-lab/30-characters` 与 `40-scenes`，由 `project_id` 连接 StoryProject。

## Workflow Purpose / 工作流目的
把稳定的故事图拆解为可独立维护、可被视觉链路引用的 Character 与 Scene canonical 卡（填补此前缺失的抽取环节）。

## Trigger / 触发
B 工作流完成、story_graph 稳定。

## Inputs / 输入
- StoryProject 卡 + 稳定 story_graph。

## Steps / 步骤
1. 抽取每个出场角色 → 按 `templates/canonical-assets/Character.md` 在 `30-characters/` 建卡；填 `project_id`、`visual_lock`、`forbidden_changes`。
2. 抽取每个场景 → 按 `templates/canonical-assets/Scene.md` 在 `40-scenes/` 建卡；填 `characters`、`props`、`continuity_constraints`、`linked_packages`（占位）。
3. 在 StoryProject 卡的 Characters / Scenes 区登记（markdown 链接，不用 `[[ ]]`）。
4. 人工复核：角色/场景 canon 是否与故事图一致、无遗漏、无冲突。

## Outputs / 输出
- `02-wiki/story-lab/30-characters/<id>.md`、`02-wiki/story-lab/40-scenes/<id>.md`。
- StoryProject 卡 Characters/Scenes 区更新。

## Runtime Commands / Runtime 命令
- 无（人工抽取；可用 B 的分析结果辅助）。

## Human Approval Gates / 人工批准门禁
- 抽取出的角色/场景 canon 人工复核签收。

## QA Gates / QA 门禁
- 无（结构正确性由后续视觉链路与图读测试间接保障）。

## Stop Conditions / 停止条件
- 故事图缺失或角色/场景定义冲突 → 回到 B。

## Related Skills / 关联技能
- `skills/Character-Extraction-Skill.md`、`skills/Scene-Extraction-Skill.md`
- 下游：`workflows/D-Visual-Style-and-PromptRecipe-Workflow.md`
