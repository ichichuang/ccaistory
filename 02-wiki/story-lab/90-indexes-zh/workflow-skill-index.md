# 工作流与技能索引 / Workflow & Skill Index

> 全部 `skill_card` 与 `workflow_card` 的中文索引。
> Chinese-facing index of all `skill_card` and `workflow_card` entries.

## Purpose / 用途

- 中文：集中检索故事生产中的技能卡与工作流卡，了解每个技能/工作流的状态与用途，便于在制作时按需调用。
- English: Index skill cards and workflow cards used in story production — their status and purpose — so they can be invoked on demand during production.

技能卡与工作流卡为权威来源。
Skill and workflow cards are canonical.

## Data Source Path / 数据源路径

- 主文件夹 / Primary folder: `02-wiki/story-lab/80-skills-tools-workflows/`
- 类型 / Type values: `skill_card`、`workflow_card`
- 兼容旧目录 / Also covers legacy subfolders: `02-wiki/story-lab/80-skills-tools-workflows/skills/` 与 `02-wiki/story-lab/80-skills-tools-workflows/workflows/`（如存在，请一并浏览）。
- The legacy `skills/` and `workflows/` subfolders above should be browsed as well if present.

## Filters / 筛选

- `type = "skill_card"` 或 `type = "workflow_card"`。
- `type = "skill_card"` or `type = "workflow_card"`.
- 可选：按 `status`（如 `active`、`draft`、`deprecated`）过滤。
- Optional: filter by `status` (e.g. `active`, `draft`, `deprecated`).

## Sorting / 排序

- 按 `type` 升序，再按 `status` 升序。
- Sort by `type` ascending, then `status` ascending.

## Display Fields / 展示字段

- `title_zh`
- `type`
- `status`
- `version`

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  type AS "类型",
  status AS "状态",
  version AS "版本"
FROM "02-wiki/story-lab/80-skills-tools-workflows"
WHERE type = "skill_card" OR type = "workflow_card"
SORT type ASC, status ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/80-skills-tools-workflows/` 浏览所有技能卡与工作流卡。
   Open `02-wiki/story-lab/80-skills-tools-workflows/` and browse all skill and workflow cards.
2. 同时检查旧目录 `02-wiki/story-lab/80-skills-tools-workflows/skills/` 与 `02-wiki/story-lab/80-skills-tools-workflows/workflows/`（如存在）。
   Also check the legacy folders `02-wiki/story-lab/80-skills-tools-workflows/skills/` and `02-wiki/story-lab/80-skills-tools-workflows/workflows/` if present.
3. 逐张读取 frontmatter：`title_zh`、`type`、`status`、`version`，按 `type` 区分技能与工作流。
   Read each card's frontmatter: `title_zh`, `type`, `status`, `version`, and separate skills from workflows by `type`.
