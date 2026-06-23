# 运行Multimodal QA

## 命令

```bash
python runtime/aistory.py generate-image-review-form --asset-type R00_PAPER_MARK_ANCHOR --asset-id <asset_id> --candidate-id <candidate_id> --artifact-id <candidate_artifact_id>
python runtime/aistory.py validate-image-review --review <review_form_json_path>
python runtime/aistory.py merge-image-qa --review <review_form_json_path>
python runtime/aistory.py register-image-qa-artifact --review <review_form_json_path> --registry <registry_json_path>
```

## 规则

- v0.1 不自动识图，只生成结构化图像复核表单。
- 人工填写 `review_form` 后才能 validate。
- runtime 校验 `review_form`。
- `image_review_form` 可合并为 `asset_qa_result`。
- `asset_qa_result` 登记到 Artifact Registry。
- `accepted_reference_asset` 必须有 telemetry、image QA 和 asset QA。
- 后续 v0.2 可接入自动图像识别，本阶段不做。
