---
type: workflow_card
id: "I-Image-QA-and-Repair-Workflow"
title_zh: I 图像 QA 与返修工作流
title_en: I. Image QA and Repair Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, image-qa, repair]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: image_qa
trigger: "GenerationRun 与复核表单就绪（H 完成）"
input_layer: "50-agent-work/story-lab/runs, 50-agent-work/story-lab/image-review-forms"
output_layer: "50-agent-work/story-lab/qa-results, 50-agent-work/story-lab/repair-notes, 90-archive/story-lab/rejected-assets"
required_cards: ["GenerationRun"]
runtime_commands: ["validate-image-review", "merge-image-qa", "qa-asset"]
human_gates: yes
qa_gates: yes
stop_conditions: ["未做人工图像复核", "R00 未 accepted 时继续 R01/R02"]
replacement_for: ""
deprecated_by: ""
---
# I 图像 QA 与返修工作流 / Image QA and Repair Workflow

> Doctrine：**接受前必须人工图像复核**。pending / fail / 比例错误 / 缺遥测 一律不得 accepted。失败进入 RepairNote 回到上游重出，**不直接改候选图**；被拒材料入 `90-archive`。

## Workflow Purpose / 工作流目的
对候选图做人工图像复核 + 资产 QA，给出 accepted / rejected / rework 决策，并保护下游依赖。

## Trigger / 触发
H 工作流生成了 GenerationRun 与 image_review_form。

## Inputs / 输入
- GenerationRun 卡 + 待填 image_review_form + 候选图。

## Steps / 步骤
1. 人工在 image_review_form 逐项填写 `actual_answer` 与证据（**强制人工复核**）。
2. 运行 `validate-image-review`：必答未答 → `pending`；hard-fail → `fail`。
3. 运行 `merge-image-qa` 合并为 `asset_qa_result`（落 `50-agent-work/story-lab/qa-results/`）；运行 `qa-asset` 做资产级判定。
4. 决策：
   - **pass** → 进入 J（ReferenceAsset 接受）。
   - **fail/rework** → 按 `templates/canonical-assets/RepairNote.md` 在 `50-agent-work/story-lab/repair-notes/` 建 RepairNote，回到上游 E/F/G 重出。
   - **reject** → 候选与记录入 `90-archive/story-lab/rejected-assets/`。
5. **R00 未 accepted 时阻断依赖它的 R01/R02/S 出图。**

## Outputs / 输出
- `50-agent-work/story-lab/qa-results/<id>.md`、`50-agent-work/story-lab/repair-notes/<id>.md`、`90-archive/story-lab/rejected-assets/`（拒绝时）。

## Runtime Commands / Runtime 命令
- `validate-image-review`、`merge-image-qa`、`qa-asset`。

## Human Approval Gates / 人工批准门禁
- 人工图像复核（必须，不可由模型自动通过）。

## QA Gates / QA 门禁
- 仅 `decision == pass` 才能进入接受；rejected/deprecated 资产不得作为依赖。

## Stop Conditions / 停止条件
- 未做人工复核、或 R00 未 accepted 时继续 R01/R02 → 阻断。

## Related Skills / 关联技能
- `skills/Multimodal QA技能.md`、`skills/资产级细粒度验收技能.md`、`skills/资产验收与返修技能.md`
- 下游：`workflows/J-ReferenceAsset-Acceptance-Workflow.md`
- 对应 codex 指令：`00-system/codex-instructions/REPAIR_FAILED_IMAGE_RUN.md`
