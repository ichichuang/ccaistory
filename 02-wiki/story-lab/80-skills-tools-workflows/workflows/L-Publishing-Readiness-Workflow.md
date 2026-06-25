---
type: workflow_card
id: "L-Publishing-Readiness-Workflow"
title_zh: L 发布就绪工作流
title_en: L. Publishing Readiness Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, publishing-readiness]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: publishing_readiness
trigger: "成品包计划 ready（K 完成）"
input_layer: "02-wiki/story-lab/10-projects"
output_layer: "50-agent-work/story-lab/qa-results, 02-wiki/story-lab/10-projects"
required_cards: ["StoryProject"]
runtime_commands: []
human_gates: yes
qa_gates: yes
stop_conditions: ["人工完整阅读未过", "存在阻断项"]
replacement_for: "源插图到平台发布页流程（发布部分）"
deprecated_by: ""
---
# L 发布就绪工作流 / Publishing Readiness Workflow

> Doctrine：发布就绪检查清单落 `50-agent-work`，最终发布决策回填 `02-wiki` 的 StoryProject。

## Workflow Purpose / 工作流目的
对装配好的成品包做发布就绪检查与人工完整阅读，给出最终发布决策。

## Trigger / 触发
K 工作流把 `final_package_status` 置为 `ready`。

## Inputs / 输入
- StoryProject 成品包计划 + 全部 accepted 资产。

## Steps / 步骤
1. 执行发布就绪检查清单（`acceptance-checklists/Final Illustrated Story Package Readiness Checklist.md`），结果落 `50-agent-work/story-lab/qa-results/`。
2. 人工完整阅读成品（错序、遮挡、断裂、发布风险）。
3. 设置 StoryProject `publishing_readiness_status: ready`（无阻断项时）。
4. 在 StoryProject 记录最终发布决策（canonical）。

## Outputs / 输出
- `50-agent-work/story-lab/qa-results/` 发布就绪检查记录。
- StoryProject `publishing_readiness_status` 与最终决策（canonical）。

## Runtime Commands / Runtime 命令
- 无（人工阅读 + 清单；可用 `status` 复核 machine_state）。

## Human Approval Gates / 人工批准门禁
- 人工完整阅读 + 最终发布签收。

## QA Gates / QA 门禁
- 发布就绪检查清单全部通过；无阻断项。

## Stop Conditions / 停止条件
- 人工完整阅读未过或存在阻断项 → 阻断发布。

## Related Skills / 关联技能
- `skills/人工完整阅读技能.md`、`skills/Publishing-Readiness-Skill.md`、`skills/平台发布页合成技能.md`
