---
type: skill_card
id: "Publishing-Readiness-Skill"
title_zh: 发布就绪检查技能
title_en: Publishing Readiness Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, publishing-readiness]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: publishing_readiness
runtime_commands: ["status"]
runtime_support_status: runtime
input_layer: "02-wiki"
output_layer: "50-agent-work, 02-wiki"
human_gate: yes
qa_gate: yes
workflow_dependencies: ["L-Publishing-Readiness-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 发布就绪检查技能 / Publishing Readiness Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
对装配好的成品包做发布就绪检查与人工完整阅读，给出最终发布决策。

## Inputs / 输入
- StoryProject 成品包计划、全部 accepted 资产、人工完整阅读结果。

## Outputs / 输出
- `50-agent-work/story-lab/qa-results/` 发布就绪检查记录；StoryProject `publishing_readiness_status` 与最终决策（canonical）。

## Preconditions / 前置条件
- K 工作流把 `final_package_status` 置为 `ready`。

## Runtime Support / Runtime 支撑
- `status`（复核 machine_state）；其余为人工。

## Human Review Gate / 人工复核门禁
- 人工完整阅读 + 最终发布签收。

## Failure Modes / 失败模式
- 跳过完整阅读 / 带阻断项发布 / 成品与 accepted 资产不一致。回退到 K。

## Related Workflows / 关联工作流
- `workflows/L-Publishing-Readiness-Workflow.md`；验收清单：`acceptance-checklists/Final Illustrated Story Package Readiness Checklist.md`
