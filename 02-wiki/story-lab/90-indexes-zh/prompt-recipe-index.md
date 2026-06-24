# 提示词配方索引 / Prompt Recipe Index

> 全部 `prompt_recipe` 提示词配方卡片的中文索引。
> Chinese-facing index of all `prompt_recipe` cards.

## Purpose / 用途

- 中文：集中检索所有提示词配方，了解其目标媒介、状态与版本，便于在新执行包中复用高质量配方。
- English: Index all prompt recipes — their target media, status, and version — so high-quality recipes can be reused in new execution packages.

提示词配方卡片为权威来源。
Prompt-recipe cards are canonical.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/60-prompts/`
- 类型 / Type value: `prompt_recipe`

## Filters / 筛选

- 仅 `type = "prompt_recipe"`。
- Only `type = "prompt_recipe"`.
- 可选：按 `status`（如 `draft`、`stable`、`deprecated`）或 `target_media` 过滤。
- Optional: filter by `status` (e.g. `draft`, `stable`, `deprecated`) or `target_media`.

## Sorting / 排序

- 按 `status` 升序（便于将 `stable` 与 `draft` 分组）。
- Sort by `status` ascending (groups `stable` and `draft` together).

## Display Fields / 展示字段

- `title_zh`
- `target_media`
- `status`
- `version`

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  target_media AS "目标媒介",
  status AS "状态",
  version AS "版本"
FROM "02-wiki/story-lab/60-prompts"
WHERE type = "prompt_recipe"
SORT status ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/60-prompts/` 浏览所有提示词配方卡片。
   Open `02-wiki/story-lab/60-prompts/` and browse all prompt-recipe cards.
2. 逐张读取 frontmatter：`title_zh`、`target_media`、`status`、`version`。
   Read each card's frontmatter: `title_zh`, `target_media`, `status`, `version`.
3. 优先选用 `status = "stable"` 且 `version` 较高的配方用于新执行包。
   Prefer recipes with `status = "stable"` and a higher `version` for new packages.
