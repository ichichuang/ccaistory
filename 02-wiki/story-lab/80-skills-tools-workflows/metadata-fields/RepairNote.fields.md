# RepairNote 字段定义 / Field Schema

fileClass：`RepairNote`（`type: repair_note`）。卡模板：`../templates/canonical-assets/RepairNote.md`。卡片位置：`50-agent-work/story-lab/repair-notes/`。每个失败输出必须进入 repair 队列。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `repair_note` | repair_note | 固定值 |
| id | text | kebab-case，唯一 | `<repair-note-id>` | 与文件名一致 |
| title_zh | text | — | 占位返修记录 | 中文标题 |
| title_en | text | — | Placeholder Repair Note | 英文标题 |
| status | select | open / in-progress / closed | open | 返修生命周期状态（单一状态字段；旧 `repair_status` 已移除） |
| project_id | text | story_project id | `<story-project-id>` | 所属项目 |
| canonical | boolean | true / false | true | 登记为卡 |
| created_at | date | YYYY-MM-DD | 2026-06-24 | — |
| updated_at | date | YYYY-MM-DD | 2026-06-24 | — |
| owner | text | — | `<owner>` | — |
| version | text | `v\d+` | v0 | — |
| tags | list | — | [] | — |
| related_assets | list | — | [] | — |
| source_paths | list | 01-raw 路径 | [] | — |

## Type-specific fields / 专有字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| package_id | text | image_execution_package id | `<package-id>` | 相关执行包 |
| linked_run | text | generation_run id | `<run-id>` | 失败的 run |
| source_generation_run | text | generation_run id | `<run-id>` | 触发返修的 run（= linked_run，可读别名） |
| linked_image_review_form | text | image_review_form id | "" | 关联的人工复核表单 |
| failure_types | list | — | [] | 失败分类 |
| priority | select | low / medium / high / urgent | "" | 优先级 |
| next_action | text | — | "" | 下一步动作 |
| output_asset | text | reference_asset id | "" | 返修产出的资产（前向链接） |
| target_reference_asset | text | reference_asset id | "" | 返修目标参考资产 |
| close_status | select | resolved / superseded / abandoned | "" | 关闭结论（仅 `status: closed` 时填） |

## Validation notes / 校验说明

- `type` 必须为 `repair_note`。
- 单一状态字段 `status`（open/in-progress/closed）；`close_status` 仅在 `status: closed` 时记录关闭结论（旧 `repair_status` 已废除，避免双状态漂移）。
- `output_asset` / `target_reference_asset` 提供 RepairNote → ReferenceAsset 的前向链接，闭合追溯链。
- 关闭（`closed`）前必须满足卡内「Close Condition」并复跑「Follow-up QA」。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE package_id, failure_types, status, priority, next_action FROM "50-agent-work/story-lab/repair-notes" WHERE type = "repair_note" AND status != "closed" SORT priority DESC`
- Bases：`../../00-dashboard/bases/repair-queue.base`；看板：`../../00-dashboard/repair-queue.md`。
