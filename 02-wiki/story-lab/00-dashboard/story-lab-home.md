# Story Lab 首页 / Story Lab Home

> 黑曜石故事生产 Wiki 的中央枢纽。所有看板、索引与制作卡片的入口。
> Central hub for the Obsidian Story Production Wiki. Entry point to all boards, indexes, and production cards.

## Purpose / 用途

- 中文：作为故事生产 Wiki 的主入口，汇集各类看板与索引，帮助创作者快速跳转到活跃项目、执行包、修复队列、待办场景、高复用提示词、角色画廊与视觉风格。
- English: Serve as the main entry point of the Story Production Wiki, gathering boards and indexes so creators can jump to active projects, execution packages, the repair queue, pending scenes, high-reuse prompt recipes, the character gallery, and visual styles.

This page is **scaffolding**. The folders it links to may currently be empty — that is expected. Cards in `02-wiki/story-lab/` are the canonical source of truth; runtime outputs under `50-agent-work/` are derived caches.

## Data Source Path / 数据源路径

- 主目录 / Root: `02-wiki/story-lab/`
- 各资产目录见下方导航与各专属看板。
- The full asset folder map is in the navigation below and inside each dedicated board.

## Filters / 筛选

- 本页不直接筛选数据；它仅作为导航枢纽。
- This page does not filter data directly; it is a navigation hub only.
- 下方的「活跃项目」聚合块按 `type = "story_project"` 且 `status` 非 `archived` 过滤。
- The "Active projects" block below filters by `type = "story_project"` and `status` not `archived`.

## Sorting / 排序

- 活跃项目聚合块按 `updated_at` 倒序排列（最近更新优先）。
- The active-projects block sorts by `updated_at` descending (most recently updated first).

## Display Fields / 展示字段

- 活跃项目聚合块展示：`title_zh`、`status`、`updated_at`。
- The active-projects block shows: `title_zh`, `status`, `updated_at`.

## 导航 / Navigation

资产目录直达 / Asset folders:

- 活跃项目 / Active projects: [10-projects](../10-projects/) · 索引 [project-index](../90-indexes-zh/project-index.md)
- 最近执行包 / Recent execution packages: [70-execution-packages](../70-execution-packages/) · 看板 [image-package-board](image-package-board.md)
- 修复队列 / Repair queue: [repair-queue](repair-queue.md) (数据在 `50-agent-work/story-lab/repair-notes/`)
- 待办场景 / Pending scenes: [40-scenes](../40-scenes/) · 看板 [scene-board](../90-indexes-zh/scene-board.md)
- 高复用提示词 / High-reuse prompt recipes: [60-prompts](../60-prompts/) · 索引 [prompt-recipe-index](../90-indexes-zh/prompt-recipe-index.md)
- 角色画廊 / Character gallery: [30-characters](../30-characters/) · 索引 [character-gallery](../90-indexes-zh/character-gallery.md)
- 视觉风格索引 / Visual style index: [50-visual-styles](../50-visual-styles/) · 索引 [visual-style-index](../90-indexes-zh/visual-style-index.md)
- 参考素材 / Reference assets: [reference-assets](../reference-assets/) · 画廊 [reference-asset-gallery](reference-asset-gallery.md)
- 技能 / 工具 / 工作流 / Skills, tools, workflows: [80-skills-tools-workflows](../80-skills-tools-workflows/) · 索引 [workflow-skill-index](../90-indexes-zh/workflow-skill-index.md)

其他看板 / Other dashboards:

- 图像执行包看板 / Image package board: [image-package-board](image-package-board.md)
- 修复队列 / Repair queue: [repair-queue](repair-queue.md)
- 生成运行日志 / Generation run log: [generation-run-log](generation-run-log.md)
- 参考素材画廊 / Reference asset gallery: [reference-asset-gallery](reference-asset-gallery.md)

中文索引区 / Chinese index area:

- 索引总目录 / Index folder: [90-indexes-zh](../90-indexes-zh/)
- 项目索引 / Project index: [project-index](../90-indexes-zh/project-index.md)
- 角色画廊 / Character gallery: [character-gallery](../90-indexes-zh/character-gallery.md)
- 场景看板 / Scene board: [scene-board](../90-indexes-zh/scene-board.md)
- 视觉风格索引 / Visual style index: [visual-style-index](../90-indexes-zh/visual-style-index.md)
- 提示词配方索引 / Prompt recipe index: [prompt-recipe-index](../90-indexes-zh/prompt-recipe-index.md)
- 工作流与技能索引 / Workflow & skill index: [workflow-skill-index](../90-indexes-zh/workflow-skill-index.md)

## 活跃项目聚合 / Active Projects (Dataview)

```dataview
TABLE title_zh AS "标题", status AS "状态", updated_at AS "更新时间"
FROM "02-wiki/story-lab/10-projects"
WHERE type = "story_project" AND status != "archived"
SORT updated_at DESC
```

## Manual Fallback / 手动回退

当未安装 Dataview 插件时：
When the Dataview plugin is not installed:

1. 在文件浏览器中打开 `02-wiki/story-lab/10-projects/` 浏览全部项目卡片。
   Open `02-wiki/story-lab/10-projects/` in the file explorer to browse all project cards.
2. 逐张打开卡片，读取 frontmatter 中的 `title_zh`、`status`、`updated_at` 字段判断活跃度。
   Open each card and read the `title_zh`, `status`, `updated_at` frontmatter fields to judge activity.
3. 其他资产目录同理：直接浏览本页「导航」列出的文件夹，读取每张卡片的 `type` 与 `status` frontmatter。
   For other assets, browse the folders listed under "Navigation" above and read the `type` and `status` frontmatter of each card.
4. 各专属看板与索引页（链接见上）也都包含各自的手动回退说明。
   Each dedicated board and index page (linked above) also includes its own manual-fallback instructions.
