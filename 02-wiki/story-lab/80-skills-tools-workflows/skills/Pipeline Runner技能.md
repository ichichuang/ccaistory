---
type: skill_card
id: "Pipeline Runner技能"
title_zh: Pipeline Runner技能
title_en: Pipeline Runner Skill
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [skill, story-lab]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
skill_category: runtime_maintenance
runtime_commands: ["pipeline-plan", "pipeline-run", "pipeline-status", "pipeline-resume", "can-run"]
runtime_support_status: runtime
input_layer: "02-wiki"
output_layer: "runtime-cache"
human_gate: no
qa_gate: no
workflow_dependencies: []
replacement_for: ""
deprecated_by: ""
---
# Pipeline Runner技能

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。下文凡提及“写入 story_core / 故事核心.json / 派生视图”，一律按本卡 frontmatter 的 `input_layer`/`output_layer` 落地：操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。runtime 与 Artifact Registry 仅为派生缓存。

## 1. 技能目的
使用 Pipeline Runner 规划、阻断、恢复和审计故事生产阶段，让状态推进由 contracts、状态机和质量门禁共同控制。

## 2. 输入
- 可选项目路径。
- 可选 `story_core.json` 或 `故事核心.json`。
- `runtime/contracts/pipeline_actions.json`
- `runtime/contracts/state_machine.json`
- `runtime/contracts/quality_gates.json`

## 3. 输出
- pipeline plan
- run_manifest
- checkpoint
- recovery status
- JSON CLI 输出

## 4. 允许行为
- 读取 contracts。
- 读取项目 `story_core`。
- 生成 dry-run 计划。
- 在 `runtime/.runs/{run_id}/` 写入 run manifest 和 checkpoint。
- 根据 checkpoint 判断是否可 resume。

## 5. 禁止行为
- 不创建故事项目。
- 不创建新故事。
- 不生成图片。
- 不调用 WebGPT 或外部出图工具。
- 不生成源插图试产任务清单实例。
- 不生成执行包。
- 不生成发布包。
- 不自动越过人工批准点。

## 6. 门禁
所有阶段必须通过 `state_machine` 与 `quality_gates`。若 action 被 `blocked_actions` 阻断，必须返回 blocked。若 required inputs 缺失，必须返回 missing inputs。

外部出图阶段必须停止并等待人工执行。accepted/rejected 前必须有 telemetry 与 asset QA。

## 7. 下游入口
Pipeline Runner 通过后可进入 Phase 3 Skill Executor，但仍必须保持人工审美批准与外部出图人工执行边界。
