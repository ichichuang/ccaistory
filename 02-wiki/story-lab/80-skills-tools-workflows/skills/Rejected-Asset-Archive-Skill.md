---
type: skill_card
id: "Rejected-Asset-Archive-Skill"
title_zh: 拒绝资产归档技能
title_en: Rejected Asset Archive Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab, archive]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: archive
runtime_commands: []
runtime_support_status: manual_only
input_layer: "50-agent-work"
output_layer: "90-archive"
human_gate: yes
qa_gate: no
workflow_dependencies: ["I-Image-QA-and-Repair-Workflow"]
replacement_for: ""
deprecated_by: ""
---
# 拒绝资产归档技能 / Rejected Asset Archive Skill

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。

## Skill Purpose / 技能目的
把被拒绝/废弃的候选与记录移入 `90-archive`，并保证它们永不再作为下游依赖。

## Inputs / 输入
- QA 决策为 reject 的候选、相关 GenerationRun 与 RepairNote。

## Outputs / 输出
- `90-archive/story-lab/rejected-assets/<id>/`（只入不改）；在来源记录登记 `rejected`。

## Preconditions / 前置条件
- I 工作流判定 reject。

## Runtime Support / Runtime 支撑
- manual_only（Artifact Registry 会阻止 rejected/deprecated 作为参考依赖被解锁）。

## Human Review Gate / 人工复核门禁
- 归档前确认拒绝理由；确认无下游卡仍引用该资产。

## Failure Modes / 失败模式
- rejected 资产泄漏为 accepted 依赖 / 归档后被改写。回退到 I 工作流。

## Related Workflows / 关联工作流
- `workflows/I-Image-QA-and-Repair-Workflow.md`；codex：`00-system/codex-instructions/REPAIR_FAILED_IMAGE_RUN.md`
