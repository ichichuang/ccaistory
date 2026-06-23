# Multimodal QA技能

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
