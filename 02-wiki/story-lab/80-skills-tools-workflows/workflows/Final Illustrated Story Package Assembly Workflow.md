---
type: workflow_card
id: "Final-Illustrated-Story-Package-Assembly-Workflow"
title_zh: K 最终插图故事成品装配工作流
title_en: Final Illustrated Story Package Assembly Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, final-assembly]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: final_assembly
trigger: "项目所需 accepted 资产全部就绪"
input_layer: "02-wiki/story-lab/reference-assets, 02-wiki/story-lab/70-execution-packages"
output_layer: "02-wiki/story-lab/10-projects, 50-agent-work/story-lab/runs"
required_cards: ["StoryProject", "Scene", "Character", "VisualStyle", "PromptRecipe", "ImageExecutionPackage", "ReferenceAsset", "GenerationRun"]
runtime_commands: ["artifact-check-registry", "artifact-lineage"]
human_gates: yes
qa_gates: yes
stop_conditions: ["accepted_asset_count < required_asset_count", "存在未过 QA 的必需资产", "缺发布就绪检查"]
replacement_for: "源插图到平台发布页流程（成品部分）"
deprecated_by: ""
---
# K 最终插图故事成品装配工作流 / Final Illustrated Story Package Assembly Workflow

> Doctrine：成品装配计划是 canonical，落 `02-wiki`（StoryProject + 装配计划区）；操作装配记录落 `50-agent-work`。**图像二进制默认不入 git。** 这是新 doctrine 此前缺失的"最终成品"环节（见 `00-system/codex-instructions/ASSEMBLE_FINAL_ILLUSTRATED_STORY_PACKAGE.md` 与 `maps/final-illustrated-story-package-map.md`）。

## Workflow Purpose / 工作流目的
在所有必需 accepted 资产与故事资产就绪后，把它们装配成一个完整的插图故事成品包（canonical 计划 + 操作记录），并经人工批准达到发布就绪。

## Trigger / 触发
J 工作流持续产出 accepted ReferenceAsset，直到 `accepted_asset_count >= required_asset_count`。

## Inputs / 输入
- StoryProject、所有 Scene/Character/VisualStyle/PromptRecipe/ImageExecutionPackage 卡。
- 所有 accepted ReferenceAsset + 对应 GenerationRun + QA 结果（+ RepairNote 若经返修）。

## Steps / 步骤
1. 核对 StoryProject `required_asset_count` 与每个必需场景/资产的 QA 状态；任一必需资产未 accepted → 阻断。
2. 运行 `artifact-check-registry` + `artifact-lineage`（派生缓存血缘自检，0 断链）。
3. 装配：按页/场景把 accepted ReferenceAsset 与故事文字层组织成**成品包计划**，写入 StoryProject 的 Final Package 区（canonical）。
4. 操作装配记录（页序、资产映射、版本）落 `50-agent-work/story-lab/runs/`。
5. 设置 StoryProject `final_package_status: assembling → ready`（人工批准后）；进入 L 做发布就绪检查。
6. 图像二进制不入 git（`.gitignore` 忽略），成品包以 canonical 卡 + 路径引用表达。

## Outputs / 输出
- StoryProject 卡 Final Package 区（canonical 成品计划）。
- `50-agent-work/story-lab/runs/` 装配操作记录。

## Runtime Commands / Runtime 命令
- `artifact-check-registry`、`artifact-lineage`。

## Human Approval Gates / 人工批准门禁
- 成品装配前人工批准（`final_package_status: ready` 前）。

## QA Gates / QA 门禁
- 所有必需场景/资产通过 QA；`accepted_asset_count >= required_asset_count`。

## Stop Conditions / 停止条件
- 必需资产未过 QA、数量不足、或缺发布就绪检查 → 阻断。

## Related Skills / 关联技能
- `skills/Final Illustrated Story Package Assembly Skill.md`、`skills/平台发布页合成技能.md`、`skills/平台图文故事编排技能.md`
- 下游：`workflows/L-Publishing-Readiness-Workflow.md`
- 验收清单：`acceptance-checklists/Final Illustrated Story Package Readiness Checklist.md`
