---
type: codex_instruction
id: "ASSEMBLE_FINAL_ILLUSTRATED_STORY_PACKAGE"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "02-wiki/story-lab/10-projects, 50-agent-work/story-lab/runs"
related_templates: ["StoryProject", "ReferenceAsset", "ImageExecutionPackage"]
related_workflows: ["Final-Illustrated-Story-Package-Assembly-Workflow", "L-Publishing-Readiness-Workflow"]
human_gate: yes
runtime_role: "tool-layer: artifact-check-registry / artifact-lineage 仅做派生缓存血缘自检；never canonical, never image generation"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。本指令补齐"装配最终插图故事成品"环节。

# ASSEMBLE FINAL ILLUSTRATED STORY PACKAGE / 装配最终插图故事成品

## Scope / 范围
当一个 StoryProject 的所有必需 accepted ReferenceAsset 与故事资产就绪后，把它们装配成一个完整的插图故事成品包（canonical 计划 + 操作记录）。不生成任何新图像；不创建真实故事内容（架构脚手架阶段）。

## Allowed inputs / 允许输入
- `02-wiki/story-lab/10-projects/<project-id>.md`（StoryProject，含 `required_asset_count`）。
- 全部必需 Scene/Character/VisualStyle/PromptRecipe/ImageExecutionPackage 卡。
- 全部 accepted `ReferenceAsset` + 对应 `GenerationRun` + QA 结果（+ `RepairNote` 若返修）。

## Allowed outputs / 允许输出
- StoryProject 卡的 **Final Package 区**（canonical 成品计划；`final_package_status`）。
- `50-agent-work/story-lab/runs/` 下的**装配操作记录**（页序、资产映射、版本）。

## Target layer / 落地层
- canonical：`02-wiki/story-lab/10-projects/`。
- 操作记录：`50-agent-work/story-lab/runs/`。
- 图像二进制：不入 git（`.gitignore` 忽略）。

## Steps / 步骤
1. 核对 `accepted_asset_count >= required_asset_count` 且每个必需场景/资产通过 QA；否则阻断。
2. 运行 `python runtime/aistory.py artifact-check-registry` 与 `artifact-lineage`（0 断链）。
3. 按页/场景把 accepted ReferenceAsset 与故事文字层组织为成品包计划，写入 StoryProject 的 Final Package 区。
4. 写装配操作记录到 `50-agent-work/story-lab/runs/`。
5. 人工批准后置 `final_package_status: ready`，移交 L 工作流做发布就绪检查。

## Stop condition / 停止条件
- 必需资产未过 QA、`accepted_asset_count < required_asset_count`、或缺人工批准 → 阻断，不得 `ready`。

## Human approval gate / 人工批准门禁
- 成品装配前人工批准（`final_package_status: ready` 前必须）。

## Runtime role / runtime 角色
- 仅 `artifact-check-registry` / `artifact-lineage` 做派生缓存血缘自检；runtime 不持有成品 canonical，不生成图像。

## Forbidden actions / 禁止
- 不提交图像二进制；不把未 accepted 资产纳入成品；不绕过人工批准与发布就绪检查；不创建真实故事实例。

## Related canonical templates / 关联模板
- `02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/StoryProject.md`、`ReferenceAsset.md`、`ImageExecutionPackage.md`。

## Related workflow cards / 关联工作流卡
- `workflows/Final Illustrated Story Package Assembly Workflow.md`、`workflows/L-Publishing-Readiness-Workflow.md`。
- map：`02-wiki/story-lab/maps/final-illustrated-story-package-map.md`。
