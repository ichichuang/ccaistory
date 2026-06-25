---
type: reference_asset
id: "<reference-asset-id>"
title_zh: 占位参考资产
title_en: Placeholder Reference Asset
status: candidate
project_id: "<story-project-id>"
visual_role: ""
quality_status: candidate
superseded_by: ""
used_by: []
file_location: ""
qa_evidence: []
source_run: ""
source_generation_run: ""
source_image_review_form: ""
source_asset_qa_result: ""
source_repair_note: ""
accepted_by: ""
accepted_at: ""
qa_required: true
allowed_usage: []
forbidden_usage: []
r00_anchor_scope: ""
related_assets: []
source_paths: []
tags: []
created_at: 2026-06-24
updated_at: 2026-06-24
owner: "<owner>"
version: v0
canonical: true
---

# 占位参考资产 / Placeholder Reference Asset

> 模板说明：**ReferenceAsset** canonical 卡模板。复制到 `02-wiki/story-lab/reference-assets/`。图像二进制文件默认不入库（被 .gitignore 忽略）；本 Markdown 卡才是 canonical 知识层，记录资产的位置与来源。字段定义见 `../../metadata-fields/ReferenceAsset.fields.md`。

## Asset Summary / 资产概要

<!-- 这张参考图是什么、用途。占位。 -->

## Accepted Source / 接受来源

<!-- 来源的 GenerationRun / 外部来源；accepted 必须可追溯。占位。 -->

## Visual Role / 视觉角色

<!-- 角色锚图 / 场景锚图 / 风格图 / 构图图等。占位。 -->

## Allowed Usage / 允许用途

<!-- 允许作为哪些依赖使用。占位。 -->

## Forbidden Usage / 禁止用途

<!-- 不允许的用途。占位。 -->

## Dependency Use / 依赖使用

<!-- 被哪些执行包作为依赖引用。占位。 -->

## Quality Status / 质量状态

<!-- accepted / candidate / rejected / deprecated。占位。 -->

## Superseded By / 被取代

<!-- 若被新版本取代，指向新 reference_asset。占位。 -->

## Used By / 被使用

<!-- 引用本资产的 character / scene / package 卡。占位。 -->

## QA Evidence / QA 证据

<!-- 关联的 telemetry / image QA / asset_qa_result（记录在 50-agent-work）。占位。 -->

## File Location Policy / 文件位置策略

<!-- 二进制文件存放位置与命名（不入 git）；本卡记录路径与 hash 引用。占位。 -->

## Accepted Provenance / 接受溯源

<!-- accepted 必须可溯源：source_generation_run（生成 run）、source_image_review_form（人工复核表单）、source_asset_qa_result（资产 QA 结论）、source_repair_note（若经返修）、accepted_by + accepted_at（人工接受人/时间）。证据落 50-agent-work，结论回填本卡。占位。 -->

## R00 Anchor Scope / R00 锚图作用域

<!-- 若 visual_role 为 paper-stroke-anchor（R00）：用 r00_anchor_scope 声明本锚图仅承载的狭窄视觉属性（如纸张质感与笔触）。不得承载完整角色系统、完整场景、道具集合、符号散点表或分镜。下游执行包必须在其 r00_dependency_policy 声明具体借用哪一项属性。R00 未 accepted 时阻断依赖它的执行包。占位。 -->
