# SkillCard 字段定义 / Field Schema

fileClass：`SkillCard`（`type: skill_card`）。卡模板：`../templates/canonical-assets/SkillCard.md`。卡片位置：`02-wiki/story-lab/80-skills-tools-workflows/`（历史生产技能在 `skills/`）。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `skill_card` | skill_card | 固定值 |
| id | text | kebab-case，唯一 | `<skill-card-id>` | 与文件名一致 |
| title_zh | text | — | 占位技能卡 | 中文标题 |
| title_en | text | — | Placeholder Skill Card | 英文标题 |
| status | select | draft / active / deprecated | draft | 技能状态 |
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
| inputs | list | — | [] | 输入 |
| outputs | list | — | [] | 输出 |
| runtime_support | list | runtime 命令 | [] | 支撑命令 |
| related_workflows | list | workflow_card id | [] | 关联工作流 |

## Validation notes / 校验说明

- `type` 必须为 `skill_card`。
- `runtime_support` 引用的命令必须真实存在于 `runtime/aistory.py`。
- 技能卡描述能力，不内联具体故事数据。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, status, related_workflows FROM "02-wiki/story-lab/80-skills-tools-workflows" WHERE type = "skill_card" SORT status ASC`
- 索引：`../../90-indexes-zh/workflow-skill-index.md`。
