---
type: workflow_card
id: "A-Raw-Story-Intake-Workflow"
title_zh: A 原始故事接入工作流
title_en: A. Raw Story Intake Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, intake]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: story_intake
trigger: "用户提供一篇新故事"
input_layer: "01-raw"
output_layer: "01-raw, 02-wiki/story-lab/10-projects"
required_cards: ["StoryProject"]
runtime_commands: ["status"]
human_gates: yes
qa_gates: no
stop_conditions: ["无合法输入", "版权边界未确认"]
replacement_for: "新故事从输入到试产流程"
deprecated_by: ""
---
# A 原始故事接入工作流 / Raw Story Intake Workflow

> Doctrine：原始输入落 `01-raw`，canonical 卡落 `02-wiki`，操作记录落 `50-agent-work`，被拒材料落 `90-archive`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口模型：WebGPT 指令窗负责规划/复核并产出本地执行指令，WebGPTImage 生成窗只按受控执行单出图。

## Workflow Purpose / 工作流目的
把用户提供的故事安全接入系统：落地不可变原始输入，并初始化一个 StoryProject canonical 卡。

## Trigger / 触发
用户在 WebGPT 指令窗提供一篇故事（含题材、目标平台、版权边界）。

## Inputs / 输入
- 用户故事原文、版权边界、目标平台。

## Steps / 步骤
1. WebGPT 指令窗确认版权边界与改编策略（人工门禁）。
2. Codex/Claude 把原文写入 `01-raw/story-lab/user-inputs/<project-id>/`（不可变，永不重写）。
3. 按 `templates/canonical-assets/StoryProject.md` 在 `02-wiki/story-lab/10-projects/<project-id>.md` 创建 StoryProject 卡；`source_paths` 指向上述 `01-raw` 路径。
4. 运行 `python runtime/aistory.py status` 确认空状态/初始 machine_state。
5. 在 project-index（`02-wiki/story-lab/90-indexes-zh/project-index.md`）登记新项目。

## Outputs / 输出
- `01-raw/story-lab/user-inputs/<project-id>/` 原始输入（不入 git 的大文件除外）。
- `02-wiki/story-lab/10-projects/<project-id>.md` StoryProject canonical 卡。

## Runtime Commands / Runtime 命令
- `python runtime/aistory.py status`

## Human Approval Gates / 人工批准门禁
- 版权与改编边界确认（必须通过才能创建 StoryProject）。

## QA Gates / QA 门禁
- 无（接入阶段；QA 在后续图像链路）。

## Stop Conditions / 停止条件
- 无合法输入或版权边界未确认 → 阻断，不创建 StoryProject。

## Related Skills / 关联技能
- `skills/故事输入与版权改编技能.md`（story_intake）
- 下游：`workflows/B-Story-Analysis-and-Canonical-Card-Workflow.md`
