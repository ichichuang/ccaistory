# 规范资产模型 / Canonical Asset Model

> ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 本文件只定义资产类型、字段与关系，不实例化任何真实资产。引用一律使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

## 1. 概览 / Overview

本仓库定义 **11 类规范资产（canonical asset types）**。每一类在 `02-wiki/story-lab/` 下有固定的文件夹归属，并以 Obsidian Markdown 卡片承载。卡片是 **长期事实来源**；runtime 产物只是派生缓存。

## 2. 资产类型表 / Asset Type Table

| 资产类型 / Asset | `type:` 值 | 所在文件夹 / Folder | 说明 / Purpose |
| --- | --- | --- | --- |
| 故事项目 / Story Project | `story_project` | `02-wiki/story-lab/10-projects/` | 一个故事的根节点，聚合所有下游资产 |
| 世界观 / World | （世界观卡片） | `02-wiki/story-lab/20-worlds/` | 世界设定、规则、基调 |
| 角色 / Character | `character` | `02-wiki/story-lab/30-characters/` | 角色定义与可视化约束 |
| 场景 / Scene | `scene` | `02-wiki/story-lab/40-scenes/` | 场景定义与构图意图 |
| 视觉风格 / Visual Style | `visual_style` | `02-wiki/story-lab/50-visual-styles/` | 风格规范、色板、禁忌 |
| 提示配方 / Prompt Recipe | `prompt_recipe` | `02-wiki/story-lab/60-prompts/` | 可复用提示结构（与执行包分离） |
| 图像执行包 / Image Execution Package | `image_execution_package` | `02-wiki/story-lab/70-execution-packages/` | 单次受控生成的完整指令包 |
| 参考资产 / Reference Asset | `reference_asset` | `02-wiki/story-lab/reference-assets/` | 已接受、可被引用复用的资产卡片 |
| 生成运行 / Generation Run | `generation_run` | `50-agent-work/story-lab/runs/` | 一次真实生成的运行记录 |
| 修复记录 / Repair Note | `repair_note` | `50-agent-work/story-lab/repair-notes/` | 失败运行的根因与修复方案 |
| 技能卡 / Skill Card | `skill_card` | `02-wiki/story-lab/80-skills-tools-workflows/` | 一个可复用能力的说明卡 |
| 工作流卡 / Workflow Card | `workflow_card` | `02-wiki/story-lab/80-skills-tools-workflows/` | 一个端到端流程的说明卡 |

> 说明：`generation_run` 与 `repair_note` 属于第 3 层 `50-agent-work/`（真实工作产物）；其余 9 类规范卡片属于第 2 层 `02-wiki/`。`world` 卡片与项目/角色/场景一同构成项目知识骨架。

## 3. 通用前置元数据字段 / Common Frontmatter Fields

每张规范卡片在 YAML frontmatter 中至少携带以下字段（值均为占位示意）：

```yaml
---
type: <one-of-canonical-types>      # 例如 story_project / character / scene ...
id: <asset-id>                      # 全局唯一标识，占位
title_zh: 占位中文标题
title_en: EXAMPLE_VALUE
status: draft                       # 见第 6 节生命周期
project_id: <project-id>            # 归属项目
related_assets:                     # 关联资产 id 列表
  - <asset-id>
source_paths:                       # 指向 01-raw / 50-agent-work 的来源路径
  - 01-raw/story-lab/user-inputs/<placeholder>
tags:
  - 占位
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 0.1.0
canonical: true                     # 标记本卡片是该资产的规范事实来源
---
```

字段语义要点：
- `canonical: true` 表示该 Markdown 卡片是该资产的 **规范事实来源**；runtime 缓存中的同名条目均为派生。
- `source_paths` 用于回溯到 `01-raw/`（原料）或 `50-agent-work/`（运行/QA），实现血缘可追溯。
- `related_assets` 承载跨卡片关系，配合下方关系表使用。

## 4. 关系表 / Relationship Table

| 来源 / From | 关系 / Relation | 目标 / To |
| --- | --- | --- |
| `story_project` | 拥有 / owns | `character`、`scene`、`visual_style`、`world` |
| `story_project` | 聚合 / aggregates | `image_execution_package` |
| `image_execution_package` | 绑定 / binds | `character`、`scene`、`visual_style`、`prompt_recipe`、`reference_asset` |
| `prompt_recipe` | 被引用于 / referenced by | `image_execution_package` |
| `image_execution_package` | 产生 / produces | `generation_run` |
| `generation_run` | 失败时触发 / on-failure opens | `repair_note` |
| `generation_run` | 接受时写回 / on-accept writes | `reference_asset` |
| `repair_note` | 链接回 / links back to | `generation_run`、`image_execution_package` |
| `reference_asset` | 被绑定于 / bound by | `image_execution_package` |
| `skill_card` / `workflow_card` | 描述 / documents | 上述生产步骤 |

关系链概述（占位）：

```
story_project
   └─ characters / scenes / visual_styles (/ world)
         └─ image_execution_package  (绑定 prompt_recipe + reference_assets)
               └─ generation_run
                     ├─ (失败) repair_note
                     └─ (接受) reference_asset
```

## 5. 资产卡片之间如何引用 / Cross-Referencing

- 卡片之间通过 `related_assets`（id 列表）与标准 Markdown 链接互相引用。
- **不使用 Obsidian 双方括号 wikilink**；统一使用相对路径 Markdown 链接或反引号路径，例如 `02-wiki/story-lab/70-execution-packages/<asset-id>.md`。

## 6. 生命周期 / 状态总览 / Lifecycle & Status

规范卡片的 `status` 字段建议取值（占位约定）：

| status | 含义 / Meaning | 典型层 / Typical layer |
| --- | --- | --- |
| `draft` | 起草中，尚未通过校验 | `02-wiki` |
| `ready` | 已通过 compile/lint，可进入生产 | `02-wiki` |
| `in_production` | 正在被某个 generation_run 使用 | `02-wiki` + `50-agent-work` |
| `accepted` | 输出通过全部 QA，已写回参考资产 | `02-wiki` |
| `needs_repair` | 运行失败，已开 repair_note | `50-agent-work` |
| `archived` | 被拒绝/废弃/退役/遗留 | `90-archive` |

状态流转的治理规则见 [Image-Production-Governance.md](./Image-Production-Governance.md)；持久决策必须写回规范卡片，参见 [../runtime-boundary/Markdown-Is-Canonical.md](../runtime-boundary/Markdown-Is-Canonical.md)。

## 7. 模板与字段 Schema / Templates & Field Schema

- 资产模板目录：`02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/`
- 字段 schema 目录：`02-wiki/story-lab/80-skills-tools-workflows/metadata-fields/`

新建任何卡片前，先从上述模板目录复制对应模板，并按字段 schema 校对 frontmatter。
