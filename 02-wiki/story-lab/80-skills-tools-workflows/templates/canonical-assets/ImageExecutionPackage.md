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
output_assets: []
related_assets: []
source_paths: []
last_run: ""
qa_result: ""
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

## Repair Triggers / 修复触发条件

<!-- 触发返修的失败类型。占位。 -->

## Result Backfill Procedure / 结果回填流程

<!-- 生成后如何把 GenerationRun 记录到 50-agent-work，并把 accepted 决策回填到 canonical reference asset 卡（runtime 产物只是缓存）。占位。 -->
