# Character 字段定义 / Field Schema

fileClass：`Character`（`type: character`）。卡模板：`../templates/canonical-assets/Character.md`。卡片位置：`02-wiki/story-lab/30-characters/`。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `character` | character | 固定值 |
| id | text | kebab-case，唯一 | `<character-id>` | 与文件名一致 |
| title_zh | text | — | 占位角色 | 中文名 |
| title_en | text | — | Placeholder Character | 英文名 |
| status | select | draft / in-review / verified / archived | draft | 一致性锁定状态 |
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
| cover_image | text | 文件路径（不入 git） | "" | 角色封面图位置；二进制不提交 |
| visual_style | text | visual_style id | `<visual-style-id>` | 主视觉风格 |
| visual_lock | list | — | [] | 必须保持不变的视觉特征 |
| reference_assets | list | reference_asset id | [] | 锚图 |
| forbidden_changes | list | — | [] | 禁止改动项 |
| last_used | date | YYYY-MM-DD | "" | 最近使用 |
| failure_count | number | ≥0 | 0 | 失败次数（看板用） |

## Validation notes / 校验说明

- `type` 必须为 `character`；`canonical=true`。
- `visual_lock` 与 `forbidden_changes` 建议非空以锁定一致性。
- `cover_image` 仅记录路径；图像二进制由 `.gitignore` 忽略，不入库。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, visual_style, failure_count FROM "02-wiki/story-lab/30-characters" WHERE type = "character" SORT failure_count DESC`
- Bases：`../../00-dashboard/bases/character-gallery.base`（cards 视图，cover_image 作图）。
