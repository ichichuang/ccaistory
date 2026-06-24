# WorkflowCard 字段定义 / Field Schema

fileClass：`WorkflowCard`（`type: workflow_card`）。卡模板：`../templates/canonical-assets/WorkflowCard.md`。卡片位置：`02-wiki/story-lab/80-skills-tools-workflows/`（历史工作流在 `workflows/`）。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `workflow_card` | workflow_card | 固定值 |
| id | text | kebab-case，唯一 | `<workflow-card-id>` | 与文件名一致 |
| title_zh | text | — | 占位工作流卡 | 中文标题 |
| title_en | text | — | Placeholder Workflow Card | 英文标题 |
| status | select | draft / active / deprecated | draft | 工作流状态 |
| project_id | text | story_project id 或空 | "" | 可复用则留空 |
| canonical | boolean | true / false | true | 固定 `true` |
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
| trigger | text | — | "" | 触发条件 |
| inputs | list | — | [] | 输入 |
| outputs | list | — | [] | 输出 |
| runtime_commands | list | runtime 命令 | [] | 涉及命令 |
| related_skills | list | skill_card id | [] | 关联技能 |

## Validation notes / 校验说明

- `type` 必须为 `workflow_card`。
- `runtime_commands` 必须真实存在于 `runtime/aistory.py`。
- 工作流卡必须在外部出图等人工执行点显式标注「停止条件」。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, trigger, related_skills FROM "02-wiki/story-lab/80-skills-tools-workflows" WHERE type = "workflow_card" SORT status ASC`
- 索引：`../../90-indexes-zh/workflow-skill-index.md`。
