---
type: skill_card
id: "PromptRecipe-Authoring-Skill"
title_zh: 提示词技法编写技能
title_en: PromptRecipe Authoring Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, prompt-recipe]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: prompt_recipe
runtime_commands: ["lint-prompt"]
runtime_support_status: runtime
input_layer: "02-wiki"
output_layer: "02-wiki"
human_gate: yes
qa_gate: no
workflow_dependencies: ["D-Visual-Style-and-PromptRecipe-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 提示词技法编写技能 / PromptRecipe Authoring Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
创建/选择可复用的 PromptRecipe canonical 卡，与具体执行包分离；统一收编旧的 `提示词生成技能`（已 deprecated）。

## Inputs / 输入
- VisualStyle 卡、`60-prompts/legacy-prompt-library/` 参考、负面约束。

## Outputs / 输出
- `02-wiki/story-lab/60-prompts/<id>.md`（按 `templates/canonical-assets/PromptRecipe.md`），含 `applicable_asset_types`、`recipe_hash`、`drift_check_policy`。

## Preconditions / 前置条件
- VisualStyle 已签收（D 工作流）。

## Runtime Support / Runtime 支撑
- `lint-prompt`（对 recipe 片段做静态约束检查）。

## Human Review Gate / 人工复核门禁
- recipe 人工复核：不含某次执行的真实 prompt 实例、不含作者姓名风格指令。

## Failure Modes / 失败模式
- recipe 与执行混写 / 缺 `recipe_hash` 导致漂移不可检测 / 复制作者表达。回退到 D 工作流。

## Related Workflows / 关联工作流
- `workflows/D-Visual-Style-and-PromptRecipe-Workflow.md`
