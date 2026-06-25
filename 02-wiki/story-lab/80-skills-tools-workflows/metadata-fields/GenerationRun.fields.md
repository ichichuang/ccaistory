# GenerationRun 字段定义 / Field Schema

fileClass：`GenerationRun`（`type: generation_run`）。卡模板：`../templates/canonical-assets/GenerationRun.md`。卡片位置：`50-agent-work/story-lab/runs/`。记录一次真实生成；持久决策回填到 `02-wiki` canonical 卡。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `generation_run` | generation_run | 固定值 |
| id | text | kebab-case，唯一 | `<run-id>` | 与文件名一致 |
| title_zh | text | — | 占位生成记录 | 中文标题 |
| title_en | text | — | Placeholder Generation Run | 英文标题 |
| status | select | planned / running / passed / failed / accepted / rejected | planned | run 状态 |
| project_id | text | story_project id | `<story-project-id>` | 所属项目 |
| canonical | boolean | true / false | true | 操作记录亦登记为卡 |
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
| package_id | text | image_execution_package id | `<package-id>` | 输入执行包 |
| image_execution_package | text | image_execution_package id | `<package-id>` | 输入执行包（= package_id，可读别名） |
| model | text | 模型名 | "" | 实际出图模型 |
| output_assets | list | reference_asset id | [] | 输出资产（accepted 后回填） |
| output_candidates | list | 01-raw 候选路径引用 | [] | 候选输出（原图落 01-raw/generated-raw，不入 git） |
| image_review_form | text | image_review_form id | "" | 人工图像复核表单（50-agent-work） |
| asset_qa_result | text | asset_qa_result id | "" | 资产 QA 结论（50-agent-work） |
| failure_types | list | — | [] | 失败分类 |
| decision | select | accepted / rejected / repair | "" | 运行级决策 |
| final_decision | select | accepted / rejected / repair | "" | 终审决策（回填 reference_asset 的依据） |
| repair_note | text | repair_note id | "" | 关联返修（原 `repair_package` 已重命名） |
| backfill_status | select | pending / backfilled / blocked | "" | 回填状态 |
| human_approval | text | — | "" | 人工批准记录 |

## Validation notes / 校验说明

- `type` 必须为 `generation_run`。
- runtime 的 run/telemetry 产物是派生缓存；`final_decision=accepted` 必须回填到对应 reference_asset / execution package canonical 卡。
- `accepted` 前必须有 telemetry、`image_review_form`（人工图像复核）与 `asset_qa_result`，且有 `human_approval`。
- `repair_note` 替代旧字段 `repair_package`，指向 `50-agent-work/story-lab/repair-notes/` 下的 RepairNote。
- `output_candidates` 仅记录 `01-raw/story-lab/generated-raw/` 中候选路径引用；二进制不入 git。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE package_id, model, status, final_decision, failure_types, created_at FROM "50-agent-work/story-lab/runs" WHERE type = "generation_run" SORT created_at DESC`
- Bases：`../../00-dashboard/bases/generation-run-log.base`；看板：`../../00-dashboard/generation-run-log.md`。
