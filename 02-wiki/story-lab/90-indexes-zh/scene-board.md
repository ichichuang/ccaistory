# 场景看板 / Scene Board

> 全部 `scene` 场景卡片的中文看板索引。
> Chinese-facing board index of all `scene` cards.

## Purpose / 用途

- 中文：集中查看所有场景，了解每个场景涉及的角色、状态、输出目标与关联的执行包，作为场景排产与覆盖检查的视图。
- English: View all scenes — the characters involved, status, output targets, and linked execution packages — as the view for scene scheduling and coverage checks.

场景卡片为权威来源。
Scene cards are canonical.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/40-scenes/`
- 类型 / Type value: `scene`

## Filters / 筛选

- 仅 `type = "scene"`。
- Only `type = "scene"`.
- 可选：按 `project_id = "<project-id>"` 或 `status`（如 `pending`、`ready`、`done`）过滤。
- Optional: filter by `project_id = "<project-id>"` or `status` (e.g. `pending`, `ready`, `done`).

## Sorting / 排序

- 按 `project_id` 升序，再按 `status` 升序。
- Sort by `project_id` ascending, then `status` ascending.

## Display Fields / 展示字段

- `title_zh`
- `project_id`
- `characters`
- `status`
- 输出目标 / output targets（如 `output_targets`）
- 关联执行包 / linked packages（如 `related_assets` 或 `linked_packages`）

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  project_id AS "项目",
  characters AS "角色",
  status AS "状态",
  output_targets AS "输出目标",
  related_assets AS "关联执行包"
FROM "02-wiki/story-lab/40-scenes"
WHERE type = "scene"
SORT project_id ASC, status ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/40-scenes/` 浏览所有场景卡片。
   Open `02-wiki/story-lab/40-scenes/` and browse all scene cards.
2. 逐张读取 frontmatter：`title_zh`、`project_id`、`characters`、`status`、`output_targets`、`related_assets`（或 `linked_packages`）。
   Read each card's frontmatter: `title_zh`, `project_id`, `characters`, `status`, `output_targets`, `related_assets` (or `linked_packages`).
3. 优先处理 `status = "pending"` 的场景；通过关联执行包字段跳转到 [image-package-board](../00-dashboard/image-package-board.md) 查看排产。
   Prioritize scenes with `status = "pending"`; jump via the linked-packages field to [image-package-board](../00-dashboard/image-package-board.md) for scheduling.
