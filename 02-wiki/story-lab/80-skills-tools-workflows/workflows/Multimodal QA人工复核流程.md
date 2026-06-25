---
type: workflow_card
id: "Multimodal QA人工复核流程"
title_zh: Multimodal QA人工复核流程
title_en: Multimodal QA Human-Review Flow
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
workflow_category: image_qa
trigger: ""
input_layer: "50-agent-work"
output_layer: "50-agent-work"
required_cards: []
runtime_commands: ["generate-image-review-form", "validate-image-review", "merge-image-qa", "register-image-qa-artifact"]
human_gates: yes
qa_gates: yes
stop_conditions: []
replacement_for: ""
deprecated_by: ""
---
# Multimodal QA人工复核流程

> 事实源声明（canonical doctrine）：本工作流的产物按 frontmatter 的 `input_layer`/`output_layer` 落地——原始输入 `01-raw`、canonical 卡 `02-wiki`、运行/编译/lint/QA/复核/返修记录 `50-agent-work`、被拒材料 `90-archive`、执行包 `02-wiki/story-lab/70-execution-packages`、接受的参考资产 `02-wiki/story-lab/reference-assets`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口生产模型：WebGPT 指令窗规划/复核，WebGPTImage 生成窗仅按受控执行单出图。

## 流程

1. 外部出图完成后，登记 `external_generation_candidate` 和 `execution_telemetry`。
2. 运行 `generate-image-review-form` 生成结构化复核表单。
3. 人工查看图片并填写 `actual_answer`、`evidence`、`reviewer`、`reviewed_at`、`decision`。
4. 运行 `validate-image-review`。
5. 运行 `merge-image-qa` 生成 `asset_qa_result`。
6. 运行 `register-image-qa-artifact` 登记 QA payload。
7. 只有 `decision == pass` 且无硬失败、无缺必填时，才允许进入 `accept_asset`。

## 阻断

- required 问题未填：停在 `pending`。
- 硬失败不匹配：必须 `fail`。
- `pending`：不得 accepted。
- `fail`：不得 accepted。
- 画布比例错误：不得 accepted。
- 缺 telemetry：不得登记为可 accepted 的 image QA。

## 输出

Multimodal QA 输出 runtime 判定结果和 artifact payload，不生成故事项目、图片、执行包或发布包。
