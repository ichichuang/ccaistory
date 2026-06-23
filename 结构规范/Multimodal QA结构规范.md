# Multimodal QA结构规范

## 目的

Multimodal QA v0.1 不自动识图，只生成结构化图像复核表单。外部出图候选必须经过人工填写 `image_review_form`、runtime 校验、合并为 `asset_qa_result`，再登记到 Artifact Registry。

## image_review_form

```json
{
  "review_id": "",
  "artifact_id": "",
  "asset_id": "",
  "asset_type": "",
  "candidate_id": "",
  "image_path": "",
  "expected_canvas_ratio": "",
  "actual_canvas_ratio": "",
  "expected_reference_dependencies": [],
  "available_reference_dependencies": [],
  "questions": [],
  "manual_evidence": {},
  "machine_assist": {},
  "reviewer": "",
  "reviewed_at": "",
  "decision": "pending",
  "failure_reasons": [],
  "repair_suggestions": []
}
```

`decision` 只能是 `pending`、`pass`、`fail`、`conditional_pass`。

## question

```json
{
  "question_id": "",
  "question": "",
  "expected_answer": "yes",
  "actual_answer": "",
  "required": true,
  "hard_fail_if_mismatch": true,
  "evidence": ""
}
```

`expected_answer` 只能是 `yes`、`no`、`value`。必填项缺失时 review 必须停在 `pending`。硬失败不匹配时 review 必须是 `fail`。

## R00

`R00_PAPER_MARK_ANCHOR` 自动从 `runtime/contracts/visual_assets.json` 生成 14 个 contract QA，并追加 4 个通用问题：

- 实际比例是否正确？
- `reference_dependencies` 是否满足？
- 是否有长正文？
- 是否可作为 `accepted reference`？

R00 硬失败包括人物、火柴人、完整场景、道具集合、符号散点表、UI/流程图、乱涂垃圾纸、非清洁白纸、泛黄旧纸、无可控儿童笔迹样本、短线索数量不合理、长正文、无视觉中心或秩序、不可作为后续 reference asset。

## Registry约束

`accepted_reference_asset` 必须同时具备：

- `external_generation_candidate`
- `execution_telemetry`
- 来自 `image_review_form` 的 `asset_qa_result`
- `asset_qa_result.status == qa_passed`
- `image_review_decision == pass`

缺 image QA、pending image QA、fail image QA 都不得 accepted。后续 v0.2 可接入自动图像识别，但本次不做。
