---
type: skill_card
id: "Multimodal QA技能"
title_zh: Multimodal QA技能
title_en: Multimodal QA Skill
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
skill_category: image_qa
runtime_commands: ["generate-image-review-form", "validate-image-review", "merge-image-qa", "register-image-qa-artifact"]
runtime_support_status: runtime
input_layer: "01-raw, 50-agent-work"
output_layer: "50-agent-work"
human_gate: yes
qa_gate: yes
workflow_dependencies: []
replacement_for: ""
deprecated_by: ""
---
# Multimodal QA技能

> 事实源声明（canonical doctrine）：本卡 canonical 知识存于 `02-wiki` Markdown；`runtime/contracts` 仅定义校验规则；执行期 JSON 属派生 runtime/agent 产物。下文凡提及“写入 story_core / 故事核心.json / 派生视图”，一律按本卡 frontmatter 的 `input_layer`/`output_layer` 落地：操作记录写入 `50-agent-work`，持久决策回填 `02-wiki` canonical 卡，原始输入留在 `01-raw`，被拒材料入 `90-archive`。runtime 与 Artifact Registry 仅为派生缓存。

## 职责

Multimodal QA v0.1 负责把外部出图结果转成可审计的人工复核数据。它不读取图片内容，不调用 WebGPT，不调用外部出图工具，不生成图片。

## 能力

- 生成 `image_review_form`。
- 校验人工填写的 required answers、硬失败和 decision 一致性。
- 将 `image_review_form` 合并为 `asset_qa_result`。
- 保留 `manual_evidence`、`machine_assist`、`failure_reasons`、`repair_suggestions`。
- 将通过校验的 image QA payload 接入 Artifact Registry。
- 阻断 pending、fail、wrong ratio、缺必填项进入 accepted。

## 边界

- 自动图像识别不在 v0.1 范围内。
- 人工复核必须填写 `actual_answer` 和必要证据。
- `conditional_pass` 不允许直接 accepted。
- `accepted_reference_asset` 必须有 telemetry、image QA 和 asset QA。
