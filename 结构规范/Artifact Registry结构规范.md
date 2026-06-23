# Artifact Registry结构规范

Artifact Registry 是所有生产物的身份、hash、血缘和状态登记层。

## 存储位置

- 运行模块：`runtime/artifact_registry/`
- 默认 registry：`runtime/.artifacts/registry.json`
- 默认 registry 只登记 artifact 元数据，不保存图片、执行包、发布包或故事项目。

## Artifact 类型

- `story_core`
- `story_graph`
- `story_analysis_result`
- `skill_executor_result`
- `visual_asset_spec`
- `compiled_prompt`
- `semantic_lint_result`
- `source_pilot_task_list`
- `external_generation_candidate`
- `execution_telemetry`
- `asset_qa_result`
- `accepted_reference_asset`
- `platform_page_layout`
- `publish_package`

## 必填字段

- `artifact_id`
- `artifact_type`
- `project_id`
- `story_id`
- `asset_id`
- `run_id`
- `candidate_id`
- `source_path`
- `content_hash`
- `source_hash`
- `parent_artifact_ids`
- `dependency_artifact_ids`
- `created_at`
- `status`
- `metadata`

## 状态

- `draft`
- `compiled`
- `lint_passed`
- `lint_failed`
- `generated`
- `telemetry_recorded`
- `qa_pending`
- `qa_passed`
- `qa_failed`
- `accepted`
- `rejected`
- `deprecated`

## 强制规则

- 不允许同名候选覆盖：重复 `artifact_id` 必须阻断。
- `compiled_prompt` 必须有 `visual_asset_spec` 父级。
- `semantic_lint_result` 必须有 `compiled_prompt` 父级。
- `external_generation_candidate` 必须依赖 `compiled_prompt` 和 `semantic_lint_result`。
- `accepted_reference_asset` 必须能追溯到 `compiled_prompt`、`external_generation_candidate`、`execution_telemetry` 和 `asset_qa_result`。
- 不允许无 telemetry accepted。
- 不允许无 QA accepted。
- `rejected` / `deprecated` asset 不得作为参考依赖。
