# 视觉风格索引 / Visual Style Index

> 全部 `visual_style` 视觉风格卡片的中文索引。
> Chinese-facing index of all `visual_style` cards.

## Purpose / 用途

- 中文：集中检索所有视觉风格定义，了解其状态与归属项目，便于角色、场景与执行包统一引用同一风格基线。
- English: Index all visual-style definitions — their status and owning project — so characters, scenes, and execution packages reference a consistent style baseline.

视觉风格卡片为权威来源。
Visual-style cards are canonical.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/50-visual-styles/`
- 类型 / Type value: `visual_style`

## Filters / 筛选

- 仅 `type = "visual_style"`。
- Only `type = "visual_style"`.
- 可选：按 `project_id = "<project-id>"` 或 `status`（如 `draft`、`approved`、`deprecated`）过滤。
- Optional: filter by `project_id = "<project-id>"` or `status` (e.g. `draft`, `approved`, `deprecated`).

## Sorting / 排序

- 按 `status` 升序，再按 `title_zh` 升序。
- Sort by `status` ascending, then `title_zh` ascending.

## Display Fields / 展示字段

- `title_zh`
- `project_id`
- `status`
- `version`
- `updated_at`

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  project_id AS "项目",
  status AS "状态",
  version AS "版本",
  updated_at AS "更新时间"
FROM "02-wiki/story-lab/50-visual-styles"
WHERE type = "visual_style"
SORT status ASC, title_zh ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/50-visual-styles/` 浏览所有视觉风格卡片。
   Open `02-wiki/story-lab/50-visual-styles/` and browse all visual-style cards.
2. 逐张读取 frontmatter：`title_zh`、`project_id`、`status`、`version`、`updated_at`。
   Read each card's frontmatter: `title_zh`, `project_id`, `status`, `version`, `updated_at`.
3. 优先采用 `status = "approved"` 的风格作为角色与场景的统一基线。
   Prefer styles with `status = "approved"` as the unified baseline for characters and scenes.
