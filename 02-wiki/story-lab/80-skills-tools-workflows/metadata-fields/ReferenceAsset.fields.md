# ReferenceAsset 字段定义 / Field Schema

fileClass：`ReferenceAsset`（`type: reference_asset`）。卡模板：`../templates/canonical-assets/ReferenceAsset.md`。卡片位置：`02-wiki/story-lab/reference-assets/`。图像二进制不入 git；本 Markdown 卡是 canonical 知识层。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `reference_asset` | reference_asset | 固定值 |
| id | text | kebab-case，唯一 | `<reference-asset-id>` | 与文件名一致 |
| title_zh | text | — | 占位参考资产 | 中文标题 |
| title_en | text | — | Placeholder Reference Asset | 英文标题 |
| status | select | candidate / accepted / rejected / deprecated | draft | 资产状态 |
| project_id | text | story_project id | `<story-project-id>` | 所属项目 |
| canonical | boolean | true / false | true | 固定 `true` |
| created_at | date | YYYY-MM-DD | 2026-06-24 | — |
| updated_at | date | YYYY-MM-DD | 2026-06-24 | — |
| owner | text | — | `<owner>` | — |
| version | text | `v\d+` | v0 | — |
| tags | list | — | [] | — |
| related_assets | list | — | [] | — |
| source_paths | list | 01-raw 路径 | [] | — |

## Type-specific fields / 专有字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| visual_role | select | character-anchor / scene-anchor / style / composition | "" | 视觉角色 |
| quality_status | select | candidate / accepted / rejected / deprecated | "" | 质量结论 |
| superseded_by | text | reference_asset id | "" | 被取代为 |
| used_by | list | character / scene / package id | [] | 被引用 |
| file_location | text | 文件路径（不入 git） | "" | 二进制位置 |
| qa_evidence | list | run / qa id | [] | QA 证据 |

## Validation notes / 校验说明

- `type` 必须为 `reference_asset`；`canonical=true`。
- `accepted` 必须可追溯到 compiled_prompt、生成候选、execution_telemetry、image QA 与 asset_qa_result（证据落 `50-agent-work`，结论回填本卡）。
- `rejected` / `deprecated` 不得作为参考依赖被执行包绑定。
- `file_location` 仅记录路径；二进制由 `.gitignore` 忽略。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, project_id, quality_status, used_by FROM "02-wiki/story-lab/reference-assets" WHERE type = "reference_asset" SORT quality_status ASC`
- Bases：`../../00-dashboard/bases/reference-asset-gallery.base`（cards 视图）；看板：`../../00-dashboard/reference-asset-gallery.md`。
