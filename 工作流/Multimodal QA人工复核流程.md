# Multimodal QA人工复核流程

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
