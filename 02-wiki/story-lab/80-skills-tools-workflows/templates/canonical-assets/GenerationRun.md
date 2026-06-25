---
type: generation_run
id: "<run-id>"
title_zh: 占位生成记录
title_en: Placeholder Generation Run
status: planned
project_id: "<story-project-id>"
package_id: "<package-id>"
image_execution_package: "<package-id>"
model: ""
output_assets: []
output_candidates: []
image_review_form: ""
asset_qa_result: ""
failure_types: []
decision: ""
final_decision: ""
repair_note: ""
backfill_status: ""
human_approval: ""
related_assets: []
source_paths: []
tags: []
created_at: 2026-06-24
updated_at: 2026-06-24
owner: "<owner>"
version: v0
canonical: true
---

# 占位生成记录 / Placeholder Generation Run

> 模板说明：**GenerationRun** 记录一次真实生成，存于 `50-agent-work/story-lab/runs/`，不污染 canonical 执行包。它是操作记录；持久决策（accepted 资产）必须回填到 `02-wiki` 的 canonical 卡。runtime 的 run/telemetry 产物是派生缓存。字段定义见 `../../metadata-fields/GenerationRun.fields.md`。

## Run Summary / 运行概要

<!-- 本次生成的目标与结果一句话。占位。 -->

## Operator and Tool / 操作者与工具

<!-- 人工操作者 + 使用的外部出图工具/模型。占位。 -->

## Input Package / 输入执行包

<!-- 对应的 image_execution_package 卡（package_id）。占位。 -->

## Actual Prompt Source / 实际 Prompt 来源

<!-- 实际使用的 compiled_prompt 来源（runtime 缓存路径，backtick）。占位。 -->

## Output Files / 输出文件

<!-- 原始输出位置（01-raw/story-lab/generated-raw/，二进制不入 git）。占位。 -->

## QA Result / QA 结果

<!-- telemetry / image QA / asset_qa_result 摘要。占位。 -->

## Decision / 决策

<!-- accepted / rejected / repair。占位。 -->

## Failure Types / 失败类型

<!-- 失败分类（如 body-proportion-off、camera-shift）。占位。 -->

## Repair Link / 返修链接

<!-- 关联的 RepairNote（指向 repair-notes/）。占位。 -->

## Next Action / 下一步

<!-- 下一步动作。占位。 -->

## Runtime Trace / Runtime 痕迹

<!-- runtime run_id、artifact id、lineage（均为派生缓存）。占位。 -->

## Human Approval / 人工批准

<!-- 人工审美批准记录（accepted/rejected 前必须）。占位。 -->
