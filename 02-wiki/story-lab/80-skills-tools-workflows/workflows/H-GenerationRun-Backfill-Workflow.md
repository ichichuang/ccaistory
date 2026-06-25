---
type: workflow_card
id: "H-GenerationRun-Backfill-Workflow"
title_zh: H 生成记录回填工作流
title_en: H. GenerationRun Backfill Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, generation-run-backfill]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: generation_run_backfill
trigger: "WebGPTImage 返回候选图（G 完成）"
input_layer: "01-raw/story-lab/generated-raw"
output_layer: "50-agent-work/story-lab/runs, 50-agent-work/story-lab/image-review-forms"
required_cards: ["ImageExecutionPackage", "GenerationRun"]
runtime_commands: ["validate-telemetry", "generate-image-review-form"]
human_gates: no
qa_gates: yes
stop_conditions: ["无 actual_prompt_sent_to_external_tool", "遥测缺失"]
replacement_for: "本地知识库回填手册"
deprecated_by: ""
---
# H 生成记录回填工作流 / GenerationRun Backfill Workflow

> Doctrine：GenerationRun 是操作记录，落 `50-agent-work/story-lab/runs/`（`canonical: false` 语义上的派生记录卡）。**没有遥测不得进入验收。**

## Workflow Purpose / 工作流目的
把一次真实外部出图的执行事实落成 GenerationRun 卡，校验遥测，并生成人工图像复核表单，作为验收的证据起点。

## Trigger / 触发
G 工作流返回候选图与执行事实。

## Inputs / 输入
- `01-raw/generated-raw/` 候选图 + 执行事实（actual prompt、工具、参数）。

## Steps / 步骤
1. 按 `templates/canonical-assets/GenerationRun.md` 在 `50-agent-work/story-lab/runs/` 建 GenerationRun 卡；填 `package_id` / `image_execution_package`、`model`、`output_candidates`、`actual prompt` 来源。
2. 运行 `validate-telemetry`：缺 `actual_prompt_sent_to_external_tool` 或遥测不完整 → 阻断（不得进入验收）。
3. 运行 `generate-image-review-form` 生成结构化人工图像复核表单 → `50-agent-work/story-lab/image-review-forms/`。
4. 在执行包卡 `generation_run_ids` / `last_run` 登记本次 run。

## Outputs / 输出
- `50-agent-work/story-lab/runs/<run-id>.md` GenerationRun 卡。
- `50-agent-work/story-lab/image-review-forms/<id>.json` 待人工填写的复核表单。

## Runtime Commands / Runtime 命令
- `validate-telemetry`、`generate-image-review-form`。

## Human Approval Gates / 人工批准门禁
- 无（回填阶段；人工复核在 I）。

## QA Gates / QA 门禁
- 遥测校验必须通过（无遥测不得继续）。

## Stop Conditions / 停止条件
- 无 `actual_prompt_sent_to_external_tool` 或遥测缺失 → 阻断。

## Related Skills / 关联技能
- `skills/图像执行遥测技能.md`
- 下游：`workflows/I-Image-QA-and-Repair-Workflow.md`
- 对应 codex 指令：`00-system/codex-instructions/BACKFILL_GENERATION_RUN.md`
