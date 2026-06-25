---
type: skill_card
id: "Final-Illustrated-Story-Package-Assembly-Skill"
title_zh: 最终插图故事成品装配技能
title_en: Final Illustrated Story Package Assembly Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, final-assembly]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: final_assembly
runtime_commands: ["artifact-check-registry", "artifact-lineage"]
runtime_support_status: runtime
input_layer: "02-wiki"
output_layer: "02-wiki, 50-agent-work"
human_gate: yes
qa_gate: yes
workflow_dependencies: ["Final-Illustrated-Story-Package-Assembly-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 最终插图故事成品装配技能 / Final Illustrated Story Package Assembly Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
在所有必需 accepted 资产就绪后，把它们与故事文字层装配成完整插图故事成品包（canonical 计划 + 操作记录）——填补新 doctrine 此前缺失的"最终成品"环节。

## Inputs / 输入
- StoryProject；全部 Scene/Character/VisualStyle/PromptRecipe/ImageExecutionPackage 卡；全部 accepted ReferenceAsset + GenerationRun + QA（+ RepairNote 若返修）。

## Outputs / 输出
- StoryProject 卡 Final Package 区（canonical 成品计划，`final_package_status`）。
- `50-agent-work/story-lab/runs/` 装配操作记录。**图像二进制不入 git。**

## Preconditions / 前置条件
- `accepted_asset_count >= required_asset_count`；每个必需场景/资产通过 QA。

## Runtime Support / Runtime 支撑
- `artifact-check-registry`、`artifact-lineage`（血缘自检，0 断链）。

## Human Review Gate / 人工复核门禁
- 成品装配前人工批准（`final_package_status: ready` 前）。

## Failure Modes / 失败模式
- 必需资产未过 QA 仍装配 / 数量不足 / 把二进制提交入库 / 用未接受资产。回退到 J 或对应上游。

## Related Workflows / 关联工作流
- `workflows/Final Illustrated Story Package Assembly Workflow.md`；`workflows/L-Publishing-Readiness-Workflow.md`；codex：`00-system/codex-instructions/ASSEMBLE_FINAL_ILLUSTRATED_STORY_PACKAGE.md`
