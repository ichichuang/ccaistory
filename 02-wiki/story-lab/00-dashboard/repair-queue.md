# 修复队列 / Repair Queue

> 按优先级排列的 `repair_note` 修复任务队列。
> Priority-ordered queue of `repair_note` repair tasks.

## Purpose / 用途

- 中文：集中展示所有待处理的修复笔记，按优先级排序，帮助操作者决定下一步先修哪个失败的执行包或运行。
- English: Surface all pending repair notes ordered by priority, helping the operator decide which failed execution package or run to fix next.

修复笔记记录失败类型与下一步动作；它指向具体的运行（`linked_run`）。
Repair notes record failure types and the next action; each points to a specific run via `linked_run`.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `50-agent-work/story-lab/repair-notes/`
- 类型 / Type value: `repair_note`

## Filters / 筛选

- 仅 `type = "repair_note"`。
- Only `type = "repair_note"`.
- 默认隐藏 `status = "closed"`（已关闭）以聚焦未决任务。（单一状态字段；旧 `repair_status` 已移除。）
- Default: hide `status = "closed"` to focus on open tasks. (Single status field; the old `repair_status` was removed.)
- 可选：按 `failure_types` 包含某值，或按 `package_id = "<package-id>"` 过滤。
- Optional: filter where `failure_types` contains a value, or by `package_id = "<package-id>"`.

## Sorting / 排序

- 按 `priority` 排序（枚举 `low` / `medium` / `high` / `urgent`；高优先级在前）。
- Sort by `priority` (enum `low` / `medium` / `high` / `urgent`; highest first).

## Display Fields / 展示字段

- `package_id`
- `failure_types`
- `status`
- `priority`
- `linked_run`
- `next_action`

## Dataview

```dataview
TABLE
  package_id AS "包ID",
  failure_types AS "失败类型",
  status AS "状态",
  priority AS "优先级",
  linked_run AS "关联运行",
  next_action AS "下一步"
FROM "50-agent-work/story-lab/repair-notes"
WHERE type = "repair_note" AND status != "closed"
SORT priority ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `50-agent-work/story-lab/repair-notes/` 浏览所有修复笔记。
   Open `50-agent-work/story-lab/repair-notes/` and browse all repair notes.
2. 逐张读取 frontmatter：`package_id`、`failure_types`、`status`、`priority`、`linked_run`、`next_action`。
   Read each note's frontmatter: `package_id`, `failure_types`, `status`, `priority`, `linked_run`, `next_action`.
3. 按 `priority` 手动排序，跳过 `status = "closed"` 的条目，从最高优先级开始处理。
   Sort by `priority` manually, skip entries with `status = "closed"`, and start from the highest priority.
4. 根据 `linked_run` 在 [generation-run-log](generation-run-log.md) 中定位失败运行，根据 `package_id` 在 [image-package-board](image-package-board.md) 中定位源执行包。
   Use `linked_run` to find the failed run in [generation-run-log](generation-run-log.md), and `package_id` to find the source package in [image-package-board](image-package-board.md).
