# 角色画廊 / Character Gallery

> 全部 `character` 角色卡片的中文画廊索引。
> Chinese-facing gallery index of all `character` cards.

## Purpose / 用途

- 中文：以画廊形式浏览所有角色，查看封面图、归属项目、视觉风格、参考素材、最近使用与历史失败次数，作为角色一致性管理的入口。
- English: Browse all characters as a gallery — cover image, owning project, visual style, reference assets, last used, and historical failure count — as the entry point for character-consistency management.

角色卡片为权威来源；封面图等二进制按位置策略管理。
Character cards are canonical; binaries like cover images follow the file-location policy.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/30-characters/`
- 类型 / Type value: `character`

## Filters / 筛选

- 仅 `type = "character"`。
- Only `type = "character"`.
- 可选：按 `project_id = "<project-id>"`、`status` 或 `visual_style` 过滤。
- Optional: filter by `project_id = "<project-id>"`, `status`, or `visual_style`.
- 可选：按 `failure_count` 阈值筛选需要重点关注的高失败角色。
- Optional: filter by a `failure_count` threshold to surface high-failure characters needing attention.

## Sorting / 排序

- 按 `project_id` 升序，再按 `last_used` 倒序。
- Sort by `project_id` ascending, then `last_used` descending.

## Display Fields / 展示字段

- `title_zh`
- `cover_image`
- `project_id`
- `status`
- `visual_style`
- `reference_assets`
- `last_used`
- `failure_count`

## Dataview

```dataview
TABLE
  cover_image AS "封面",
  title_zh AS "标题",
  project_id AS "项目",
  status AS "状态",
  visual_style AS "视觉风格",
  reference_assets AS "参考素材",
  last_used AS "最近使用",
  failure_count AS "失败次数"
FROM "02-wiki/story-lab/30-characters"
WHERE type = "character"
SORT project_id ASC, last_used DESC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/30-characters/` 浏览所有角色卡片。
   Open `02-wiki/story-lab/30-characters/` and browse all character cards.
2. 逐张读取 frontmatter：`title_zh`、`cover_image`、`project_id`、`status`、`visual_style`、`reference_assets`、`last_used`、`failure_count`。
   Read each card's frontmatter: `title_zh`, `cover_image`, `project_id`, `status`, `visual_style`, `reference_assets`, `last_used`, `failure_count`.
3. 封面图等二进制按位置策略存放（见 [reference-asset-gallery](../00-dashboard/reference-asset-gallery.md) 的文件位置策略）。
   Cover images and other binaries follow the file-location policy (see the policy in [reference-asset-gallery](../00-dashboard/reference-asset-gallery.md)).
4. 重点关注 `failure_count` 较高的角色，必要时补充参考素材。
   Pay attention to characters with a high `failure_count` and add reference assets as needed.
