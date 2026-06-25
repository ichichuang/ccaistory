---
type: workflow_card
id: "G-WebGPTImage-Manual-Generation-Handoff-Workflow"
title_zh: G WebGPTImage 人工出图交接工作流
title_en: G. WebGPTImage Manual Generation Handoff Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, generation-handoff, two-window]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: generation_handoff
trigger: "执行包 ready 且 compiled_prompt 通过 Lint（F 完成）"
input_layer: "02-wiki/story-lab/70-execution-packages, 50-agent-work/story-lab/compiled-prompts"
output_layer: "01-raw/story-lab/generated-raw, 50-agent-work/story-lab/runs"
required_cards: ["ImageExecutionPackage"]
runtime_commands: []
human_gates: yes
qa_gates: no
stop_conditions: ["无受控执行单", "操作员在包外即兴改图", "未记录实际 prompt"]
replacement_for: ""
deprecated_by: ""
---
# G WebGPTImage 人工出图交接工作流 / WebGPTImage Manual Generation Handoff Workflow

> Doctrine 两窗口模型：**WebGPT 指令窗**只规划/复核并产出受控执行单，**永不直接出图**；**WebGPTImage 生成窗**只接收受控执行单、按单出图，**永不看到整个仓库**。runtime 永不调用外部出图工具。

## Workflow Purpose / 工作流目的
把一个 ready 的 ImageExecutionPackage 转成一张受控的人工执行单，交给独立的 WebGPTImage 生成窗单张出图，并把候选与执行事实带回。

## Trigger / 触发
F 工作流通过；执行包 `status: ready`。

## Inputs / 输入
- ImageExecutionPackage 卡（ready） + 通过 Lint 的 compiled_prompt（`50-agent-work/compiled-prompts/`）。

## Steps / 步骤
1. WebGPT 指令窗从执行包与 compiled_prompt 组装**受控执行单**（仅含本次出图所需信息：目标资产、prompt、参考图、画布比例、禁止项）。
2. 把执行单交给独立 **WebGPTImage 生成窗**。
3. 操作员在 WebGPTImage 窗**单张**出图，**不得在执行单/执行包之外即兴增删内容**。
4. 记录实际发送的 `actual_prompt_sent_to_external_tool`、工具、模型、参数。
5. 候选图落 `01-raw/story-lab/generated-raw/<project-id>/`（二进制不入 git）。
6. 进入 H 工作流做 GenerationRun 回填。**本工作流自身永不把资产标记为 accepted。**

## Outputs / 输出
- `01-raw/story-lab/generated-raw/<project-id>/` 候选图（路径引用）。
- 执行事实草稿（交给 H 落 `50-agent-work/story-lab/runs/`）。

## Runtime Commands / Runtime 命令
- 无（runtime 不参与外部出图；遥测校验在 H 用 `validate-telemetry`）。

## Human Approval Gates / 人工批准门禁
- 人工外部执行点（操作员在 WebGPTImage 窗执行）。

## QA Gates / QA 门禁
- 无（QA 在 I 工作流）。

## Stop Conditions / 停止条件
- 无受控执行单、包外即兴改图、或未记录实际 prompt → 阻断，不得进入回填。

## Related Skills / 关联技能
- `skills/出图执行技能.md`
- 下游：`workflows/H-GenerationRun-Backfill-Workflow.md`
- 对应 codex 指令：`00-system/codex-instructions/CREATE_IMAGE_EXECUTION_PACKAGE.md`
