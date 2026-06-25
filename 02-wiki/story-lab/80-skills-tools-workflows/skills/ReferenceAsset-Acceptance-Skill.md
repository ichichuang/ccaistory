---
type: skill_card
id: "ReferenceAsset-Acceptance-Skill"
title_zh: 参考资产接受技能
title_en: ReferenceAsset Acceptance Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, reference-asset-acceptance]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: reference_asset_acceptance
runtime_commands: ["register-image-qa-artifact", "artifact-validate", "artifact-lineage"]
runtime_support_status: runtime
input_layer: "50-agent-work"
output_layer: "02-wiki"
human_gate: yes
qa_gate: yes
workflow_dependencies: ["J-ReferenceAsset-Acceptance-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 参考资产接受技能 / ReferenceAsset Acceptance Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
把通过 QA 的候选图升级为 accepted ReferenceAsset canonical 卡，作为单一接受权威（统一收编 `资产级细粒度验收` 的判定与 `Multimodal QA` 的人工复核）。

## Inputs / 输入
- GenerationRun + image_review_form + asset_qa_result（均在 `50-agent-work`）。

## Outputs / 输出
- `02-wiki/story-lab/reference-assets/<id>.md`，`status: candidate → accepted`，含 `source_generation_run`、`source_image_review_form`、`source_asset_qa_result`、`accepted_by`、`accepted_at`、`allowed_usage`、`forbidden_usage`。

## Preconditions / 前置条件
- 三件套齐全且通过：遥测 + 人工图像复核 + 资产 QA。

## Runtime Support / Runtime 支撑
- `register-image-qa-artifact`、`artifact-validate`、`artifact-lineage`（派生缓存血缘校验）。

## Human Review Gate / 人工复核门禁
- 人工接受签收（`accepted_by` + `accepted_at`）；缺人工复核不得 accepted。

## Failure Modes / 失败模式
- 三件套缺一仍接受（QA 旁路）/ 用 rejected 资产作依赖 / 接受未记录溯源。回退到 I 工作流。

## Related Workflows / 关联工作流
- `workflows/J-ReferenceAsset-Acceptance-Workflow.md`；codex：`00-system/codex-instructions/ACCEPT_REFERENCE_ASSET.md`
