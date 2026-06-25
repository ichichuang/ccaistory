# 项目索引 / Project Index

> 全部 `story_project` 故事项目卡片的中文索引。
> Chinese-facing index of all `story_project` cards.

## Purpose / 用途

- 中文：集中检索所有故事项目，了解每个项目的状态、主要角色、采用的视觉风格与关联的执行包，作为项目层面的总览入口。
- English: Index all story projects — their status, main characters, visual styles in use, and related execution packages — as the project-level overview entry point.

项目卡片为权威来源。
Project cards are canonical.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/10-projects/`
- 类型 / Type value: `story_project`

## Filters / 筛选

- 仅 `type = "story_project"`。
- Only `type = "story_project"`.
- 可选：按 `status`（如 `active`、`paused`、`archived`）过滤。
- Optional: filter by `status` (e.g. `active`, `paused`, `archived`).

## Sorting / 排序

- 按 `status` 升序，再按 `updated_at` 倒序。
- Sort by `status` ascending, then `updated_at` descending.

## Display Fields / 展示字段

- `title_zh`
- `status`
- 主要角色 / main_characters
- 视觉风格 / visual_styles
- 关联执行包 / related_packages（如 `related_assets` 或 `related_packages`）

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  status AS "状态",
  main_characters AS "主要角色",
  visual_styles AS "视觉风格",
  related_packages AS "关联执行包"
FROM "02-wiki/story-lab/10-projects"
WHERE type = "story_project"
SORT status ASC, updated_at DESC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/10-projects/` 浏览所有项目卡片。
   Open `02-wiki/story-lab/10-projects/` and browse all project cards.
2. 逐张读取 frontmatter：`title_zh`、`status`、`main_characters`、`visual_styles`、`related_packages`（或 `related_assets`）。
   Read each card's frontmatter: `title_zh`, `status`, `main_characters`, `visual_styles`, `related_packages` (or `related_assets`).
3. 从某项目卡片出发，可跳转到 [character-gallery](character-gallery.md)、[visual-style-index](visual-style-index.md) 与 [image-package-board](../00-dashboard/image-package-board.md) 查看其下资产。
   From a project card, jump to [character-gallery](character-gallery.md), [visual-style-index](visual-style-index.md), and [image-package-board](../00-dashboard/image-package-board.md) to view its assets.

## Manual Project Links

- [AI+Story Pilot 001](../10-projects/pilot-001.md) — status: draft; workflow: A Raw Story Intake; source: YouTube transcript; source metadata: incomplete; adaptation: inspiration-only.
