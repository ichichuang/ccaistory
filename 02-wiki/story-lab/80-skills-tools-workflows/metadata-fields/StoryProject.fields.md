# StoryProject 字段定义 / Field Schema

fileClass：`StoryProject`（`type: story_project`）。卡模板：`../templates/canonical-assets/StoryProject.md`。卡片位置：`02-wiki/story-lab/10-projects/`。供 Metadata Menu / Dataview / Bases 使用。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `story_project` | story_project | 固定值，决定 fileClass |
| id | text | kebab-case，唯一 | `<story-project-id>` | 与文件名一致 |
| title_zh | text | — | 占位故事项目 | 中文标题 |
| title_en | text | — | Placeholder Story Project | 英文标题 |
| status | select | draft / active / on-hold / done / archived | draft | 项目阶段 |
| project_id | text | kebab-case | `<story-project-id>` | StoryProject 中等于 id |
| canonical | boolean | true / false | true | canonical 卡固定 `true` |
| created_at | date | YYYY-MM-DD | 2026-06-24 | 创建日期 |
| updated_at | date | YYYY-MM-DD | 2026-06-24 | 最近更新 |
| owner | text | — | `<owner>` | 负责人 |
| version | text | `v\d+` | v0 | 版本 |
| tags | list | — | [] | 标签 |
| related_assets | list | 资产 id 或链接 | [] | 关联资产 |
| source_paths | list | 01-raw 路径 | [] | 不可变原始素材路径 |

## Type-specific fields / 专有字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| main_characters | list | character id | [] | 主要角色 |
| worlds | list | world id | [] | 世界观卡（可选；未建 World 卡则留空） |
| visual_styles | list | visual_style id | [] | 视觉风格 |
| related_packages | list | image_execution_package id | [] | 关联执行包 |
| final_package_status | select | not-started / assembling / ready / published | "" | 最终成品状态 |
| required_asset_count | number | 整数 | 0 | 成品所需 accepted 资产数 |
| accepted_asset_count | number | 整数 | 0 | 当前已 accepted 资产数 |
| publishing_readiness_status | select | blocked / pending / ready | "" | 发布就绪状态 |

## Validation notes / 校验说明

- `type` 必须为 `story_project`；`canonical` 必须为 `true`。
- `id` 必须唯一且与文件名一致；不得使用任何真实历史故事名。
- 日期字段使用 `YYYY-MM-DD`。
- 列表字段缺省为 `[]`，不要写真实故事数据（架构脚手架阶段）。
- `final_package_status: ready` 前提：`accepted_asset_count >= required_asset_count` 且 `publishing_readiness_status: ready`（见最终成品装配工作流）。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, main_characters, visual_styles FROM "02-wiki/story-lab/10-projects" WHERE type = "story_project" SORT status ASC`
- Bases：源文件夹 `02-wiki/story-lab/10-projects/`，filter `type == "story_project"`，视图见 `../../00-dashboard/bases/`（如有 project 看板）。
