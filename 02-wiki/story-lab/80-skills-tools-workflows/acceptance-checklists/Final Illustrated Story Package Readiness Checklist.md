---
type: acceptance_checklist
id: "Final-Illustrated-Story-Package-Readiness-Checklist"
status: active
stage: final_assembly
target_layer: "02-wiki/story-lab/10-projects, 50-agent-work/story-lab/qa-results"
related_runtime_commands: ["artifact-check-registry", "artifact-lineage"]
related_templates: ["StoryProject", "ReferenceAsset"]
owner: ichichuang
updated_at: 2026-06-25
---
# 最终插图故事成品就绪验收清单 / Final Illustrated Story Package Readiness Checklist

## Purpose / 目的
在把项目宣布为"可发布的完整插图故事成品"之前的总验收：确认全部必需 accepted 资产与故事资产齐备、可追溯、经人工批准。

## Required Inputs / 必需输入
- StoryProject（`required_asset_count` / `accepted_asset_count`）。
- 全部必需 Scene/Character/VisualStyle/PromptRecipe/ImageExecutionPackage 卡。
- 全部必需 accepted ReferenceAsset + 对应 GenerationRun + QA 结果（+ RepairNote 若返修）。
- 发布就绪检查与人工完整阅读结果。

## Pass Criteria / 通过标准
- [ ] `accepted_asset_count >= required_asset_count`。
- [ ] 每个必需场景/资产都有 accepted ReferenceAsset，且三件套（遥测 + 人工图像复核 + 资产 QA）齐全。
- [ ] 每个 accepted 资产可经 `source_generation_run` / `source_image_review_form` / `source_asset_qa_result` 追溯。
- [ ] `artifact-check-registry` / `artifact-lineage` 0 断链。
- [ ] 人工完整阅读 `pass`；人工批准成品装配。
- [ ] 无图像二进制被提交入库。

## Fail Criteria / 失败标准
- [ ] 缺任一必需 accepted 资产；数量不足。
- [ ] 任一资产缺 QA 证据或不可追溯。
- [ ] 缺人工批准或人工完整阅读未过。

## Blocking Conditions / 阻断条件
- 任一必需资产未 accepted、数量不足、或缺人工批准 → 阻断，`final_package_status` 不得置 `ready`。

## Required Evidence / 必需证据
- accepted ReferenceAsset 卡 + 血缘自检结果；发布就绪检查记录，落 `50-agent-work/story-lab/qa-results/`。

## Output Decision / 输出决策
- `ready` → 置 StoryProject `final_package_status: ready` 且 `publishing_readiness_status: ready`；`blocked` → 回 K/J 或对应上游。

## Target Layer / 落地层
- canonical 决策回填 `02-wiki/story-lab/10-projects/`；验收记录落 `50-agent-work/story-lab/qa-results/`。

## Related Templates & Runtime / 关联模板与命令
- 模板：`StoryProject`、`ReferenceAsset`。命令：`artifact-check-registry`、`artifact-lineage`。
- 工作流：`workflows/Final Illustrated Story Package Assembly Workflow.md`、`workflows/L-Publishing-Readiness-Workflow.md`。
