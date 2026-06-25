---
type: skill_card
id: "Artifact Registry技能"
title_zh: Artifact Registry技能
title_en: Artifact Registry Skill
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
runtime_commands: ["artifact-register", "artifact-validate", "artifact-lineage", "artifact-check-registry"]
runtime_support_status: runtime
input_layer: "50-agent-work"
output_layer: "runtime-cache"
human_gate: no
qa_gate: no
workflow_dependencies: []
replacement_for: ""
deprecated_by: ""
---
# Artifact Registry技能

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。下文凡提及“写入 story_core / 故事核心.json / 派生视图”，一律按本卡 frontmatter 的 `input_layer`/`output_layer` 落地：操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。runtime 与 Artifact Registry 仅为派生缓存。

## 目标

维护统一产物登记层，确保每个生产物都有稳定身份、hash、血缘和状态。

## 输入

- artifact JSON payload
- 依赖 artifact ID
- 父级 artifact ID
- registry 状态

## 输出

- artifact 注册结果
- artifact 查询结果
- lineage 校验结果
- registry 断链检查结果

## 操作边界

- 只写 `runtime/.artifacts/registry.json`。
- 不创建故事项目。
- 不生成图片。
- 不生成执行包。
- 不生成发布包。
- 不调用 WebGPT 或外部出图工具。

## 验收重点

- `artifact_id` 不可覆盖。
- `content_hash` 与 `source_hash` 必须存在并声明 `sha256`。
- accepted reference asset 必须能追溯到 compiled prompt、外部候选、执行遥测和资产 QA。
- `rejected` / `deprecated` asset 不得解锁下游 reference dependency。
