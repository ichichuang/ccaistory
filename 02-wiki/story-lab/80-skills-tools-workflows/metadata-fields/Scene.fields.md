# Scene 字段定义 / Field Schema

fileClass：`Scene`（`type: scene`）。卡模板：`../templates/canonical-assets/Scene.md`。卡片位置：`02-wiki/story-lab/40-scenes/`。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `scene` | scene | 固定值 |
| id | text | kebab-case，唯一 | `<scene-id>` | 与文件名一致 |
| title_zh | text | — | 占位场景 | 中文标题 |
| title_en | text | — | Placeholder Scene | 英文标题 |
| status | select | draft / in-review / ready / archived | draft | 场景状态 |
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
| characters | list | character id | [] | 出场角色 |
| props | list | — | [] | 关键道具 |
| output_targets | list | image / video / ui | [] | 出图目标媒介 |
| linked_packages | list | image_execution_package id | [] | 关联执行包 |

## Validation notes / 校验说明

- `type` 必须为 `scene`；`canonical=true`。
- `characters` 中的 id 必须能在 `30-characters/` 找到对应 canonical 卡。
- `output_targets` 仅取枚举值。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, characters, output_targets FROM "02-wiki/story-lab/40-scenes" WHERE type = "scene" SORT status ASC`
- Bases：`../../00-dashboard/bases/scene-board.base`（table 视图）。
