---
type: workflow_card
id: "Artifact Registry产物登记流程"
title_zh: Artifact Registry产物登记流程
title_en: Artifact Registry Flow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: runtime_maintenance
trigger: ""
input_layer: "50-agent-work"
output_layer: "runtime-cache"
required_cards: []
runtime_commands: ["artifact-register", "artifact-validate", "artifact-lineage"]
human_gates: no
qa_gates: no
stop_conditions: []
replacement_for: ""
deprecated_by: ""
---
# Artifact Registry产物登记流程

> 事实源声明（canonical doctrine）：本工作流的产物按 frontmatter 的 `input_layer`/`output_layer` 落地——原始输入 `01-raw`、canonical 卡 `02-wiki`、运行/编译/lint/QA/复核/返修记录 `50-agent-work`、被拒材料 `90-archive`、执行包 `02-wiki/story-lab/70-execution-packages`、接受的参考资产 `02-wiki/story-lab/reference-assets`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口生产模型：WebGPT 指令窗规划/复核，WebGPTImage 生成窗仅按受控执行单出图。

1. 生成或接收 artifact payload。
2. 计算内容 hash 或 source hash。
3. 校验 artifact schema。
4. 校验父级与依赖 artifact 是否存在。
5. 校验类型和状态规则。
6. 写入 `runtime/.artifacts/registry.json`。
7. 需要 accepted 前，运行 lineage 校验。

## accepted 前置

accepted reference asset 必须同时具备：

- `external_generation_candidate`
- `execution_telemetry`
- `asset_qa_result`
- `qa_passed`
- 可追溯到 `compiled_prompt`

缺 telemetry 或 QA 时必须阻断 accepted。

## 下游引用

- 只有 `accepted` 的 reference asset 可作为 reference dependency。
- `rejected` asset 不解锁下游资产。
- `deprecated` asset 不得作为 reference asset。
