# 图像执行包看板 / Image Package Board

> 跟踪全部 `image_execution_package` 卡片的状态、目标模型与质检结果。
> Track status, target model, and QA results across all `image_execution_package` cards.

## Purpose / 用途

- 中文：集中查看所有图像执行包，了解每个包绑定的项目、场景、目标模型、版本、最近运行与质检结果，作为图像生成排产的主控视图。
- English: Provide a single view of all image execution packages — the project and scene they bind to, their target model, version, last run, and QA result — as the master control view for image generation scheduling.

执行包卡片为权威来源；运行产物（`generation_run`）是派生缓存。
Execution-package cards are canonical; generation runs are derived caches.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/70-execution-packages/`
- 类型 / Type value: `image_execution_package`

## Filters / 筛选

- 仅 `type = "image_execution_package"`。
- Only `type = "image_execution_package"`.
- 可选：按 `status`（如 `draft`、`ready`、`running`、`done`、`blocked`）或 `target_model` 进一步筛选。
- Optional: further filter by `status` (e.g. `draft`, `ready`, `running`, `done`, `blocked`) or `target_model`.
- 可选：按 `project_id = "<project-id>"` 限定单个项目。
- Optional: limit to one project with `project_id = "<project-id>"`.

## Sorting / 排序

- 默认按 `status` 升序，再按 `last_run` 倒序。
- Default: sort by `status` ascending, then `last_run` descending.

## Display Fields / 展示字段

- `id` / `package_id`
- `title_zh`
- `project_id`
- `scene_id`
- `target_model`
- `status`
- `version`
- `created_at`
- `last_run`
- `qa_result`

## Dataview

```dataview
TABLE
  package_id AS "包ID",
  title_zh AS "标题",
  project_id AS "项目",
  scene_id AS "场景",
  target_model AS "目标模型",
  status AS "状态",
  version AS "版本",
  created_at AS "创建",
  last_run AS "最近运行",
  qa_result AS "质检"
FROM "02-wiki/story-lab/70-execution-packages"
WHERE type = "image_execution_package"
SORT status ASC, last_run DESC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/70-execution-packages/` 浏览所有执行包卡片。
   Open `02-wiki/story-lab/70-execution-packages/` and browse all execution-package cards.
2. 逐张读取 frontmatter：`package_id`、`title_zh`、`project_id`、`scene_id`、`target_model`、`status`、`version`、`created_at`、`last_run`、`qa_result`。
   Read each card's frontmatter: `package_id`, `title_zh`, `project_id`, `scene_id`, `target_model`, `status`, `version`, `created_at`, `last_run`, `qa_result`.
3. 按 `status` 人工分组，优先处理 `blocked` 与 `ready` 的包。
   Group by `status` manually; prioritize `blocked` and `ready` packages.
4. 如需追踪某包的运行历史，根据 `package_id` 在生成运行日志 [generation-run-log](generation-run-log.md) 中查找对应运行。
   To trace a package's run history, look up the matching runs by `package_id` in the [generation-run-log](generation-run-log.md).
