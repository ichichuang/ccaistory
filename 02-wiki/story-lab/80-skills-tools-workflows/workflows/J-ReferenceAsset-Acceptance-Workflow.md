---
type: workflow_card
id: "J-ReferenceAsset-Acceptance-Workflow"
title_zh: J 参考资产接受工作流
title_en: J. ReferenceAsset Acceptance Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, reference-asset-acceptance]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: reference_asset_acceptance
trigger: "图像 QA 决策为 pass（I 完成）"
input_layer: "50-agent-work/story-lab/qa-results"
output_layer: "02-wiki/story-lab/reference-assets"
required_cards: ["GenerationRun", "ReferenceAsset"]
runtime_commands: ["register-image-qa-artifact", "artifact-validate", "artifact-lineage"]
human_gates: yes
qa_gates: yes
stop_conditions: ["缺遥测/复核表单/资产 QA 之一", "缺人工接受人"]
replacement_for: ""
deprecated_by: ""
---
# J 参考资产接受工作流 / ReferenceAsset Acceptance Workflow

> Doctrine：accepted ReferenceAsset 是 canonical 卡，落 `02-wiki/story-lab/reference-assets/`。接受需三件套：遥测 + 人工图像复核 + 资产 QA，缺一不得 accepted。Artifact Registry 仅为派生缓存，**不是** canonical 资产库。

## Workflow Purpose / 工作流目的
把通过 QA 的候选图升级为 accepted ReferenceAsset canonical 卡，闭合可追溯链，并保护下游依赖。

## Trigger / 触发
I 工作流给出 `decision == pass`。

## Inputs / 输入
- GenerationRun + image_review_form + asset_qa_result（均在 `50-agent-work`）。

## Steps / 步骤
1. 校验三件套齐全且通过：`source_generation_run`、`source_image_review_form`、`source_asset_qa_result`。
2. 运行 `register-image-qa-artifact` + `artifact-validate` + `artifact-lineage`（派生缓存的血缘校验；0 断链）。
3. 按 `templates/canonical-assets/ReferenceAsset.md` 在 `reference-assets/` 建卡：`status: candidate → accepted`；填 `source_*` 链接、`accepted_by` / `accepted_at`、`allowed_usage` / `forbidden_usage`；若为 R00 填 `r00_anchor_scope`。
4. 回填 StoryProject 的 `accepted_asset_count`；在执行包卡 `output_assets` 登记。
5. rejected/deprecated 资产永不作为依赖。

## Outputs / 输出
- `02-wiki/story-lab/reference-assets/<id>.md`（accepted）。
- StoryProject `accepted_asset_count` 更新。

## Runtime Commands / Runtime 命令
- `register-image-qa-artifact`、`artifact-validate`、`artifact-lineage`。

## Human Approval Gates / 人工批准门禁
- 人工接受签收（`accepted_by` + `accepted_at`）。

## QA Gates / QA 门禁
- 遥测 + 人工图像复核 + 资产 QA 三件套齐全且通过。

## Stop Conditions / 停止条件
- 三件套缺一或缺人工接受人 → 阻断，停在 candidate。

## Related Skills / 关联技能
- `skills/ReferenceAsset-Acceptance-Skill.md`、`skills/Rejected-Asset-Archive-Skill.md`
- 下游：`workflows/K-Final-Illustrated-Story-Package-Assembly-Workflow.md`（见 `Final Illustrated Story Package Assembly Workflow.md`）
- 对应 codex 指令：`00-system/codex-instructions/ACCEPT_REFERENCE_ASSET.md`
