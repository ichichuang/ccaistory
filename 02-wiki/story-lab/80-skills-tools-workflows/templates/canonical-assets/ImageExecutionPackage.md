---
type: image_execution_package
id: "<package-id>"
title_zh: 占位图像执行包
title_en: Placeholder Image Execution Package
status: draft
project_id: "<story-project-id>"
scene_id: "<scene-id>"
characters: []
visual_style: []
prompt_recipe: "<prompt-recipe-id>"
target_model: ""
aspect_ratio: "1:1"
reference_assets: []
required_reference_assets: []
prohibited_reference_assets: []
output_assets: []
generation_run_ids: []
related_assets: []
source_paths: []
last_run: ""
qa_result: ""
r00_dependency_policy: ""
maximum_anchor_reuse_policy: ""
final_assembly_dependency: ""
previous_page_reference: ""
previous_page_scene_summary: ""
current_page_scene_summary: ""
r00_reference_asset: ""
continuity_from_previous_page: []
scene_delta_from_previous_page: []
allowed_progression_delta: []
forbidden_continuity_breaks: []
page_hook_question: ""
hook_visual_target: ""
hook_annotation_guidance: ""
hook_failure_mode_to_avoid: []
symbol_semantics_target: ""
symbol_misread_to_avoid: ""
repair_guardrails: []
progression_budget_from_previous_page: ""
overcorrection_guardrail: ""
composition_priority_order: []
escalation_level: ""
continuity_qa_required: true
hook_qa_required: true
tags: []
created_at: 2026-06-24
updated_at: 2026-06-24
owner: "<owner>"
version: v0
canonical: true
---

# 占位图像执行包 / Placeholder Image Execution Package

> 模板说明：**ImageExecutionPackage** 是最需要标准化的核心 canonical 卡。每个完整图像执行包必须独立成一个 `.md` 文件，存于 `02-wiki/story-lab/70-execution-packages/`。本卡 ready 前必须通过 runtime `compile-asset` 与 `lint-asset` / `lint-prompt`。字段定义见 `../../metadata-fields/ImageExecutionPackage.fields.md`。

## Package Summary / 执行包概要

<!-- 本次出图的目标与一句话定位。占位。 -->

## Target Asset / 目标资产

<!-- 要生成的资产类型与其 canonical 卡（reference_asset / scene 等）。占位。 -->

## Dependency Graph / 依赖图

<!-- 依赖的角色、场景、视觉风格、参考图、前置锚图。占位。 -->

## Previous Page Continuity / 前页连续性

<!-- p02 及之后必填：previous_page_reference、previous accepted image/candidate reference、previous_page_scene_summary、current_page_scene_summary。R00 只控制视觉连续性；前一页控制场景连续性与递进。p01 可说明为 series master / no previous page。 -->

## Scene Delta From Previous Page / 相对前页的场景变化

<!-- 说明从前一页到本页只改变什么；每页只推进一到两个可见变化。占位。 -->

## Allowed Progression / 允许递进

<!-- 说明本页允许变暗、变近、变静、变怪、变亮或变安全的范围，必须符合 Story Graph 与当前页位置。占位。 -->

## Forbidden Continuity Breaks / 禁止连续性断裂

<!-- 说明不得突然出现的地点、密度、灯光、道具、人物、建筑、交通工具、构图复制或后页强度。占位。 -->

## Page Hook / Page-Turn Question / 本页钩子与翻页问题

<!-- 一句明确的视觉问题，来自 Story Graph / Scene / 本执行包。避免只写 mood label。占位。 -->

## Hook Annotation Guidance / 钩子标注指导

<!-- 红笔圈、箭头、问号或短中文标注应指向本页不确定性；给 1-3 个短、童稚、页内具体的中文标注候选。占位。 -->

## Hook Semantics and Repair Guardrails / 钩子语义与返修护栏

<!-- p02 及之后推荐填写；当本页有易误读线索时必填：
- hook_failure_mode_to_avoid：本页钩子最容易失败的读法。
- symbol_semantics_target：线索应该被读成什么。
- symbol_misread_to_avoid：线索不得被读成什么物体类别。
- repair_guardrails：返修时必须保留的连续性与构图边界。
- progression_budget_from_previous_page：相对上一页只允许推进多少。
- overcorrection_guardrail：不得为了修正单点问题而破坏上一页连续性。
- composition_priority_order：第一眼读什么，第二眼才发现什么。占位。 -->

## Allowed Content / 允许内容

<!-- 画面允许出现的内容。占位。 -->

## Forbidden Content / 禁止内容

<!-- 画面禁止出现的内容（含禁止把 typed_narration 写进源插图）。占位。 -->

## Prompt Recipe Binding / Prompt 技法绑定

<!-- 绑定的 prompt_recipe 卡（指向 60-prompts/）。占位。 -->

## Reference Asset Binding / 参考资产绑定

<!-- 绑定的 reference_asset 卡清单。占位。 -->

## Canvas and Output Rules / 画布与输出规则

<!-- 尺寸、比例、画布、命名与输出目标（原始输出落 01-raw）。占位。 -->

## Generation Order / 生成顺序

<!-- 多资产/多帧的生成先后顺序。占位。 -->

## Manual Execution Instructions / 人工执行说明

<!-- 在独立 WebGPTImage 窗口的人工执行点如何操作（runtime 不调用外部出图工具）。占位。 -->

## QA Acceptance Criteria / QA 验收标准

<!-- accepted 前必须满足的 telemetry / image QA / asset QA 标准。占位。 -->

## Continuity QA Criteria / 连续性 QA 标准

<!-- p02 及之后必须同时通过 R00 视觉连续性、前页场景连续性、递进控制、禁止跳跃检查。占位。 -->

## Hook QA Criteria / 钩子 QA 标准

<!-- 检查 page_hook_question、hook_visual_target、hook_annotation_guidance 是否具体、页内有效，并能形成翻页问题。占位。 -->

## Repair Triggers / 修复触发条件

<!-- 触发返修的失败类型。占位。 -->

## Result Backfill Procedure / 结果回填流程

<!-- 生成后如何把 GenerationRun 记录到 50-agent-work，并把 accepted 决策回填到 canonical reference asset 卡（runtime 产物只是缓存）。占位。 -->

## R00 Anchor Dependency Policy / R00 锚图依赖策略

<!-- R00 过载防护（canonical 规则）：
- R00 不得作为所有资产的全局父锚；只能锚定狭窄视觉属性（如纸张质感 + 笔触）。
- 本执行包必须在 frontmatter `r00_dependency_policy` 明确声明从 R00 借用的具体属性。
- 需要角色/场景连续性时，依赖 R01/R02 或具体 accepted reference_asset，而非泛化 R00。
- `maximum_anchor_reuse_policy` 约束单一锚图被多少执行包复用。
- `prohibited_reference_assets` 不得包含 rejected / deprecated 资产；R00 未通过 QA 时阻断依赖它的执行包。占位。 -->
