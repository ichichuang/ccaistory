# PromptRecipe 字段定义 / Field Schema

fileClass：`PromptRecipe`（`type: prompt_recipe`）。卡模板：`../templates/canonical-assets/PromptRecipe.md`。卡片位置：`02-wiki/story-lab/60-prompts/`（历史提示词库在 `60-prompts/legacy-prompt-library/`）。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `prompt_recipe` | prompt_recipe | 固定值 |
| id | text | kebab-case，唯一 | `<prompt-recipe-id>` | 与文件名一致 |
| title_zh | text | — | 占位提示词技法 | 中文标题 |
| title_en | text | — | Placeholder Prompt Recipe | 英文标题 |
| status | select | draft / verified / deprecated | draft | 技法状态 |
| project_id | text | story_project id 或空 | `<story-project-id>` | 可复用则留空 |
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
| target_media | select | image / video / ui / text | "" | 目标媒介 |
| usable_for | list | — | [] | 适用场景 |
| applicable_asset_types | list | canonical type 值 | [] | 适用资产类型 |
| compatible_asset_types | list | canonical type 值 | [] | 兼容资产类型（与 applicable_asset_types 同域，查询别名） |
| recipe_hash | text | sha256 短哈希 | "" | 技法内容哈希（漂移检测用） |
| drift_check_policy | text | — | "" | 漂移检测策略（何时重算 recipe_hash 并与 compiled_prompt 比对） |

## Validation notes / 校验说明

- `type` 必须为 `prompt_recipe`；`canonical=true`。
- Prompt recipe 必须与具体执行包分离：不得在本卡写入某一次执行的真实 prompt 实例。
- `applicable_asset_types` 取 canonical 资产 `type` 值（character / scene / visual_style / image_execution_package …）。
- `recipe_hash` + `drift_check_policy` 用于检测 prompt 配方漂移：编译时若 compiled_prompt 与登记的 recipe_hash 不一致，必须阻断并复核。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, target_media, status, version FROM "02-wiki/story-lab/60-prompts" WHERE type = "prompt_recipe" SORT status ASC`
- 索引：`../../90-indexes-zh/prompt-recipe-index.md`。
