# ImageExecutionPackage 字段定义 / Field Schema

fileClass：`ImageExecutionPackage`（`type: image_execution_package`）。卡模板：`../templates/canonical-assets/ImageExecutionPackage.md`。卡片位置：`02-wiki/story-lab/70-execution-packages/`。每个完整执行包必须独立成一个 `.md`。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `image_execution_package` | image_execution_package | 固定值 |
| id | text | kebab-case，唯一 | `<package-id>` | 与文件名一致 |
| title_zh | text | — | 占位图像执行包 | 中文标题 |
| title_en | text | — | Placeholder Image Execution Package | 英文标题 |
| status | select | draft / ready / generating / accepted / rejected / archived | draft | 执行包状态 |
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
| scene_id | text | scene id | `<scene-id>` | 目标场景 |
| characters | list | character id | [] | 涉及角色 |
| visual_style | list | visual_style id | [] | 视觉风格 |
| prompt_recipe | text | prompt_recipe id | `<prompt-recipe-id>` | 绑定技法 |
| target_model | text | 模型名 | "" | 目标出图模型 |
| aspect_ratio | text | 如 `1:1` `16:9` | "1:1" | 比例（带冒号需引号） |
| reference_assets | list | reference_asset id | [] | 绑定参考图 |
| output_assets | list | reference_asset id | [] | 产出资产（accepted 后回填） |
| last_run | text | generation_run id | "" | 最近一次 run |
| qa_result | select | pending / passed / failed | "" | 最近 QA 结论 |

## Validation notes / 校验说明

- `type` 必须为 `image_execution_package`；`canonical=true`。
- `status: ready` 前必须通过 runtime `compile-asset` 与 `lint-asset` / `lint-prompt`（runtime 校验语义不变）。
- `aspect_ratio` 含冒号，YAML 中必须加引号。
- `output_assets` 只在 accepted 后回填，并绑定 `package_id` / `scene_id` / `characters` / `reference_assets`。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, project_id, scene_id, target_model, status, version, last_run, qa_result FROM "02-wiki/story-lab/70-execution-packages" WHERE type = "image_execution_package" SORT status ASC`
- Bases：`../../00-dashboard/bases/image-package-board.base`；看板：`../../00-dashboard/image-package-board.md`。
