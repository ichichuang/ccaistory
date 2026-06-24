# VisualStyle 字段定义 / Field Schema

fileClass：`VisualStyle`（`type: visual_style`）。卡模板：`../templates/canonical-assets/VisualStyle.md`。卡片位置：`02-wiki/story-lab/50-visual-styles/`。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `visual_style` | visual_style | 固定值 |
| id | text | kebab-case，唯一 | `<visual-style-id>` | 与文件名一致 |
| title_zh | text | — | 占位视觉风格 | 中文标题 |
| title_en | text | — | Placeholder Visual Style | 英文标题 |
| status | select | draft / verified / deprecated | draft | 风格状态 |
| project_id | text | story_project id 或空 | `<story-project-id>` | 可跨项目复用则留空 |
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
| reference_assets | list | reference_asset id | [] | 风格参考图 |
| related_recipes | list | prompt_recipe id | [] | 实现本风格的技法 |

## Validation notes / 校验说明

- `type` 必须为 `visual_style`；`canonical=true`。
- `deprecated` 的风格不得被新执行包绑定。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, version FROM "02-wiki/story-lab/50-visual-styles" WHERE type = "visual_style" SORT status ASC`
- 索引：`../../90-indexes-zh/visual-style-index.md`。
