---
type: skill_card
id: "机器事实源Contracts技能"
title_zh: 机器事实源Contracts技能
title_en: Contracts Machine Fact-Source Skill
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
skill_category: system_maintenance
runtime_commands: ["validate-contracts", "check-contract-drift"]
runtime_support_status: runtime
input_layer: "runtime"
output_layer: "runtime"
human_gate: no
qa_gate: no
workflow_dependencies: []
replacement_for: ""
deprecated_by: ""
---
# 机器事实源 Contracts 技能

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。下文凡提及“写入 story_core / 故事核心.json / 派生视图”，一律按本卡 frontmatter 的 `input_layer`/`output_layer` 落地：操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。runtime 与 Artifact Registry 仅为派生缓存。

## 技能目的

维护 `runtime/contracts/`，保证状态机、视觉资产、skill、质量门禁和 pipeline action 等**校验规则**只有一个机器可读事实源（contracts）。生产知识的 canonical 事实源是 `02-wiki/story-lab/` 的 Obsidian Markdown 卡，runtime 产物为派生缓存。

## 输入

- `runtime/contracts/*.json`
- `runtime/skill_registry/skills.json`
- runtime 校验脚本
- 需要同步的 Markdown 结构规范（镜像校验规则）

## 输出

- 更新后的 contracts
- 通过的 `validate-contracts`
- 通过的 `check-contract-drift`
- 同步后的说明文档和测试

## 禁止行为

- 不创建故事项目。
- 不生成图片。
- 不生成执行包或发布包。
- 不把 Markdown 当作 runtime 规则事实源。
- 不在 `skill_definitions.json` 中加入具体历史故事名或正向作者风格指令。

## 门禁

- contracts JSON 全部可解析。
- R00 QA 数量为 14。
- R00 Lint 和 QA 均从 `visual_assets.json` 读取。
- skill contract 与 `skills.json` 数量、`skill_id`、`input_fields`、`output_fields`、`hard_failures`、`repair_actions` 一致。

