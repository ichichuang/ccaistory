---
type: skill_card
id: "ImageExecutionPackage-Creation-Skill"
title_zh: 图像执行包创建技能
title_en: ImageExecutionPackage Creation Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, execution-package]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: image_execution_package
runtime_commands: ["compile-asset", "lint-asset"]
runtime_support_status: runtime
input_layer: "02-wiki"
output_layer: "02-wiki"
human_gate: yes
qa_gate: yes
workflow_dependencies: ["E-ImageExecutionPackage-Creation-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 图像执行包创建技能 / ImageExecutionPackage Creation Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
把场景/角色/风格/技法/参考资产组合成 canonical ImageExecutionPackage 卡——系统中**唯一**创建执行包的技能。

## Inputs / 输入
- Scene、Character、VisualStyle、PromptRecipe 卡；适用时的 accepted ReferenceAsset 锚图。

## Outputs / 输出
- `02-wiki/story-lab/70-execution-packages/<package-id>.md`（按 `templates/canonical-assets/ImageExecutionPackage.md`）。

## Preconditions / 前置条件
- 依赖卡齐全；R00 依赖必须以 `r00_dependency_policy` 声明仅借用属性。
- p02 及之后必须有上一页引用、上一页/当前页场景摘要、受控场景差量、允许递进、禁止断裂、本页翻页问题、钩子视觉目标、红笔标注指导和故事强度位置。

## Runtime Support / Runtime 支撑
- `compile-asset`、`lint-asset`（ready 前必须通过）。

## Human Review Gate / 人工复核门禁
- 执行包内容（allowed/forbidden、依赖、R00 策略、`maximum_anchor_reuse_policy`）人工复核后才 `status: ready`。
- p02 及之后必须人工确认：R00 只控制视觉连续性；上一 accepted 页控制场景连续性和递进；本页 hook 是具体视觉问题而不是泛泛 mood label。

## Failure Modes / 失败模式
- R00 过载（把整套角色/场景压到一张 R00）/ 绑定了 rejected/deprecated 资产 / 缺 paper_policy。回退到 E 工作流或 D。
- 连续性层缺失、场景突跳、过早升级到后页强度、复制前页构图、红笔标注未指向本页不确定性。回退到 E 工作流。

## Related Workflows / 关联工作流
- `workflows/E-ImageExecutionPackage-Creation-Workflow.md`；codex：`00-system/codex-instructions/CREATE_IMAGE_EXECUTION_PACKAGE.md`
