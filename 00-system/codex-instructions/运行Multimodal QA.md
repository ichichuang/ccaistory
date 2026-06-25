---
type: codex_instruction
id: "运行Multimodal QA"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "runtime-cache"
related_templates: []
related_workflows: []
human_gate: yes
runtime_role: "tool-layer runner: invoke runtime CLI (validate/compile/lint/qa/cache); never canonical, never external image generation"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
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
