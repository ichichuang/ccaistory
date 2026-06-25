---
type: workflow_card
id: "D-Visual-Style-and-PromptRecipe-Workflow"
title_zh: D 视觉风格与提示词技法工作流
title_en: D. Visual Style and PromptRecipe Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, visual-style, prompt-recipe]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: visual_style
trigger: "角色/场景卡已建立（C 完成）"
input_layer: "02-wiki"
output_layer: "02-wiki/story-lab/50-visual-styles, 02-wiki/story-lab/60-prompts"
required_cards: ["StoryProject", "Character", "Scene"]
runtime_commands: []
human_gates: yes
qa_gates: no
stop_conditions: ["视觉风格未签收", "技法与执行混写"]
replacement_for: "视觉执行编译流程（前半）"
deprecated_by: ""
---
# D 视觉风格与提示词技法工作流 / Visual Style and PromptRecipe Workflow

> Doctrine：VisualStyle 卡落 `50-visual-styles`，PromptRecipe 卡落 `60-prompts`。Prompt recipe 必须与具体执行包分离——recipe 是可复用技法，不绑定某一次执行。

## Workflow Purpose / 工作流目的
为项目定义统一视觉风格，并沉淀可复用的 PromptRecipe 卡（带 `recipe_hash` + `drift_check_policy`），供执行包绑定。

## Trigger / 触发
C 工作流完成、角色/场景卡就绪。

## Inputs / 输入
- StoryProject、Character、Scene 卡。

## Steps / 步骤
1. 按 `templates/canonical-assets/VisualStyle.md` 在 `50-visual-styles/` 建 VisualStyle 卡（线条/色彩/质感/构图/儿童安全/禁止漂移）。
2. 按 `templates/canonical-assets/PromptRecipe.md` 在 `60-prompts/` 建/选 PromptRecipe 卡；填 `applicable_asset_types`、`recipe_hash`、`drift_check_policy`；不写入某次执行的真实 prompt 实例。
3. 历史提示词库 `60-prompts/legacy-prompt-library/` 仅作参考，不直接作为 recipe。
4. 在 VisualStyle 卡登记 `related_recipes`，在 PromptRecipe 卡登记 `compatible_asset_types`。

## Outputs / 输出
- `02-wiki/story-lab/50-visual-styles/<id>.md`、`02-wiki/story-lab/60-prompts/<id>.md`。

## Runtime Commands / Runtime 命令
- 无（定义阶段；编译/lint 在 F 工作流）。

## Human Approval Gates / 人工批准门禁
- 视觉风格人工签收（决定整套视觉基调）。

## QA Gates / QA 门禁
- 无（风格本身不出图）。

## Stop Conditions / 停止条件
- 视觉风格未签收或技法与执行混写 → 阻断。

## Related Skills / 关联技能
- `skills/视觉设定技能.md`、`skills/PromptRecipe-Authoring-Skill.md`、`skills/视觉资产本体技能.md`
- 下游：`workflows/E-ImageExecutionPackage-Creation-Workflow.md`
