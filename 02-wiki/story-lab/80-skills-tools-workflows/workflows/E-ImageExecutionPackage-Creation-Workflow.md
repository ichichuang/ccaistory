---
type: workflow_card
id: "E-ImageExecutionPackage-Creation-Workflow"
title_zh: E 图像执行包创建工作流
title_en: E. ImageExecutionPackage Creation Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, execution-package]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: image_execution_package
trigger: "视觉风格与 PromptRecipe 就绪（D 完成）"
input_layer: "02-wiki"
output_layer: "02-wiki/story-lab/70-execution-packages"
required_cards: ["Scene", "Character", "VisualStyle", "PromptRecipe"]
runtime_commands: ["compile-asset", "lint-asset"]
human_gates: yes
qa_gates: yes
stop_conditions: ["依赖卡缺失", "R00 依赖未声明", "compile/lint 未过不得 ready"]
replacement_for: ""
deprecated_by: ""
---
# E 图像执行包创建工作流 / ImageExecutionPackage Creation Workflow

> Doctrine：ImageExecutionPackage 是 canonical 卡，落 `02-wiki/story-lab/70-execution-packages/`，每个执行包独立成一个 `.md`。**本工作流是系统中唯一允许创建执行包的入口**（旧工作流一律不得创建执行包的限制已在新 doctrine 下解除）。

## Workflow Purpose / 工作流目的
把场景/角色/风格/技法/参考资产组合成可执行、可校验的 ImageExecutionPackage 卡，作为交给 WebGPTImage 生成窗的受控对象。

## Trigger / 触发
D 工作流完成；某目标资产需要出图。

## Inputs / 输入
- Scene、Character、VisualStyle、PromptRecipe 卡；适用时的 ReferenceAsset 依赖（锚图）。
- p02 及之后：上一页 id、上一页 accepted image / candidate reference（如适用）、上一页场景摘要、当前页场景摘要、Story Graph 中本页允许的递进幅度。

## Steps / 步骤
1. 按 `templates/canonical-assets/ImageExecutionPackage.md` 在 `70-execution-packages/` 建卡。
2. 绑定 `scene_id` / `characters` / `visual_style` / `prompt_recipe`；填 `allowed_content` / `forbidden_content`。
3. 声明 `required_reference_assets`、`prohibited_reference_assets`（含 rejected/deprecated）。
4. **R00 过载防护**：若依赖 R00，必须在 `r00_dependency_policy` 声明仅借用的具体属性；需要角色/场景连续性时绑定 R01/R02 或具体 accepted ReferenceAsset，而非泛化 R00；填 `maximum_anchor_reuse_policy`。
5. p02 及之后必须填写 Series Continuity + Page Hook 层：
   - `previous_page_reference`、previous accepted image / candidate reference、`previous_page_scene_summary`、`current_page_scene_summary`。
   - `continuity_from_previous_page`：必须继承的场景/人物/位置状态。
   - `scene_delta_from_previous_page`：本页只改变什么。
   - `allowed_progression_delta`：什么可以稍微变暗、变怪、变近、变静、变亮或变安全。
   - `forbidden_continuity_breaks`：什么还不能出现，包含突然换地点、突然密集/深暗、未解释新道具或基础设施、构图复制、后页强度。
   - `page_hook_question`、`hook_visual_target`、`hook_annotation_guidance`、`escalation_level`。
6. p02 及之后，执行包创建必须同时比较当前页与 R00 主参考、以及上一张 accepted 页面：R00 控制视觉连续性；上一页控制场景连续性与递进。
7. 运行 `compile-asset` 与 `lint-asset`/`lint-prompt`（详见 F）；全部通过后才把 `status: draft → ready`。

## Outputs / 输出
- `02-wiki/story-lab/70-execution-packages/<package-id>.md`（status: draft → ready）。

## Runtime Commands / Runtime 命令
- `compile-asset`、`lint-asset` / `lint-prompt`（ready 前必须通过）。

## Human Approval Gates / 人工批准门禁
- 执行包内容（allowed/forbidden、依赖、R00 策略）人工复核后才 ready。

## QA Gates / QA 门禁
- compile + semantic lint 通过（见 F）才允许 ready。

## Stop Conditions / 停止条件
- 依赖卡缺失、R00 依赖未声明、p02+ 缺前页连续性 / 场景差量 / 本页钩子、或 compile/lint 未过 → 不得 ready。

## Related Skills / 关联技能
- `skills/ImageExecutionPackage-Creation-Skill.md`、`skills/视觉资产本体技能.md`
- 下游：`workflows/F-Prompt-Compile-and-Semantic-Lint-Workflow.md`
- 对应 codex 指令：`00-system/codex-instructions/CREATE_IMAGE_EXECUTION_PACKAGE.md`
