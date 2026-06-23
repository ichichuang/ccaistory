# Multimodal QA验收清单

- `runtime/multimodal_qa/` 存在。
- `generate-image-review-form` 可生成 R00 的 14 个 contract QA + 4 个通用问题。
- `validate-image-review` 可校验人工证据、必填项、硬失败和 decision 一致性。
- `merge-image-qa` 可输出 `asset_qa_result`。
- `register-image-qa-artifact` 可生成并登记 image QA artifact payload。
- passed review 可 merge 且 `allow_accepted=true`。
- missing required review 停在 pending 并阻断。
- stick figure fail 阻断。
- symbol sheet fail 阻断。
- wrong ratio fail 阻断。
- pending review 不得 accepted。
- Artifact Registry 拒绝缺 image QA 的 `accepted_reference_asset`。
- Pipeline Runner 已接入 `generate_image_review_form`、`validate_image_review`、`merge_image_qa`、`register_image_qa_artifact`、`review_asset_for_acceptance`。
- runtime 不创建故事项目。
- runtime 不生成图片。
- runtime 不生成执行包。
- runtime 不生成发布包。
