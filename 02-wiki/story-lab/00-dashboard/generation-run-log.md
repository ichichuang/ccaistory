# 生成运行日志 / Generation Run Log

> 全部 `generation_run` 运行记录的时间线视图。
> Timeline view of all `generation_run` records.

## Purpose / 用途

- 中文：记录每一次图像生成运行的模型、状态、失败类型与输出产物，作为审计与回溯的依据，并连接到对应的执行包与修复任务。
- English: Log every image generation run — model, status, failure types, and output assets — as the audit and traceability trail, linking back to the source package and any repair task.

运行记录是派生缓存；权威配置在执行包卡片中。
Run records are derived caches; the canonical configuration lives in the execution-package card.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `50-agent-work/story-lab/runs/`
- 类型 / Type value: `generation_run`

## Filters / 筛选

- 仅 `type = "generation_run"`。
- Only `type = "generation_run"`.
- 可选：按 `status`（枚举 `planned`、`running`、`passed`、`failed`、`accepted`、`rejected`）或 `model` 过滤。
- Optional: filter by `status` (enum `planned`, `running`, `passed`, `failed`, `accepted`, `rejected`) or `model`.
- 可选：按 `package_id = "<package-id>"` 查看单个包的全部运行。
- Optional: filter by `package_id = "<package-id>"` to see all runs of one package.

## Sorting / 排序

- 按 `created_at` 倒序（最新运行在前）。
- Sort by `created_at` descending (most recent run first).

## Display Fields / 展示字段

- `id`（run id）
- `package_id`
- `model`
- `status`
- `failure_types`
- `output_assets`
- `created_at`

## Dataview

```dataview
TABLE
  id AS "运行ID",
  package_id AS "包ID",
  model AS "模型",
  status AS "状态",
  failure_types AS "失败类型",
  output_assets AS "输出产物",
  created_at AS "创建时间"
FROM "50-agent-work/story-lab/runs"
WHERE type = "generation_run"
SORT created_at DESC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `50-agent-work/story-lab/runs/` 浏览所有运行记录卡片。
   Open `50-agent-work/story-lab/runs/` and browse all run-record cards.
2. 逐张读取 frontmatter：`id`、`package_id`、`model`、`status`、`failure_types`、`output_assets`、`created_at`。
   Read each card's frontmatter: `id`, `package_id`, `model`, `status`, `failure_types`, `output_assets`, `created_at`.
3. 按文件名或 `created_at` 时间戳排序定位最新运行；失败运行可在 [repair-queue](repair-queue.md) 找到对应修复笔记（通过 `linked_run` 对应本运行 `id`）。
   Sort by filename or `created_at` to find the latest run; failed runs map to repair notes in [repair-queue](repair-queue.md) via `linked_run` matching this run's `id`.
4. 通过 `package_id` 回到 [image-package-board](image-package-board.md) 查看源执行包。
   Use `package_id` to return to the source package in [image-package-board](image-package-board.md).
