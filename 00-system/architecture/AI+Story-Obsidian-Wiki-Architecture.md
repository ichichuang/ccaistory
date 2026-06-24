# AI+Story Obsidian Story Production Wiki — 总体架构 / Architecture Overview

> ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 本文件只描述结构与流程，不实例化任何真实故事、角色、场景、图像提示或资产。所有引用一律使用占位符（例如 `<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

## 1. 目的 / Purpose

本仓库已重构为一个 **Obsidian Story Production Wiki（故事生产维基）** 加上一个 **runtime 工具层（runtime tool layer）**。

- **Wiki 部分**：以 Obsidian Markdown 规范卡片（canonical cards）作为故事、世界观、角色、场景、视觉风格、提示配方、图像执行包、参考资产、生成运行、修复记录、技能/工作流的 **长期、人类可读的事实来源（long-term human-readable source of truth）**。
- **runtime 部分**：作为可执行的校验 / lint / 编译 / QA / 缓存工具层，**只负责验证规则与派生产物（derived artifacts）**，不拥有规范生产知识。

核心立场：**图像文件是资产（assets），Markdown 才是可维护的知识层（the maintainable knowledge layer）。** 任何持久的生产决策都必须写回 `02-wiki` 中对应的 Markdown 规范卡片。

## 2. 四层模型 + runtime 工具层 / Four-Layer Model + Runtime Tool Layer

```
01-raw/        →  02-wiki/        →  50-agent-work/   →  90-archive/
(不可变原料)      (规范知识)          (真实执行/中间物)     (废弃/退役/遗留)
        \_____________________________________________________/
                              runtime/
                   (可执行工具层，位于仓库根)
```

数据的典型流动：

1. 外部/人工原始输入 → 落入 `01-raw/`（首次落地，永不重写）。
2. 经过规划与编写 → 在 `02-wiki/` 形成规范卡片（canonical cards）。
3. 真实 agent 运行、生成中间物、QA 记录、修复笔记、日志 → 写入 `50-agent-work/`。
4. 被接受的知识 → 写回 `02-wiki/`；被拒绝/废弃/退役/遗留 → 移入 `90-archive/`。
5. `runtime/` 横向服务于 2–4 步，提供校验、lint、编译、QA、缓存等能力，但不持有规范知识。

## 3. 目录树 / Directory Tree

```
AI+Story/
├── 00-system/                         # 系统级文档：架构、边界、Codex 指令
│   ├── architecture/                  # 架构与资产模型与治理文档
│   ├── runtime-boundary/              # runtime 边界与 Markdown 规范性文档
│   └── codex-instructions/            # 面向 Codex 的分步执行指令
│
├── 01-raw/                            # 第 1 层：不可变原始输入（NEVER rewritten）
│   └── story-lab/
│       └── user-inputs/               # 原始用户输入、外部生成产物首次落地
│
├── 02-wiki/                           # 第 2 层：规范 Markdown 知识（canonical）
│   └── story-lab/
│       ├── 10-projects/               # StoryProject 卡片 + project-index
│       ├── 20-worlds/                 # 世界观卡片
│       ├── 30-characters/             # Character 卡片
│       ├── 40-scenes/                 # Scene 卡片
│       ├── 50-visual-styles/          # VisualStyle 卡片
│       ├── 60-prompts/                # PromptRecipe 卡片（与执行包分离）
│       ├── 70-execution-packages/     # ImageExecutionPackage 卡片
│       ├── reference-assets/          # ReferenceAsset 卡片（已接受资产）
│       └── 80-skills-tools-workflows/ # SkillCard / WorkflowCard + 模板与字段
│           ├── templates/canonical-assets/
│           └── metadata-fields/
│
├── 50-agent-work/                     # 第 3 层：真实 agent 工作产物
│   └── story-lab/
│       ├── runs/                      # GenerationRun 记录
│       ├── repair-notes/              # RepairNote 修复记录
│       ├── qa/                        # 图像 QA / 资产 QA 记录
│       └── logs/                      # 运行日志、遥测原文
│
├── 90-archive/                       # 第 4 层：被拒绝/废弃/退役/遗留
│   └── story-lab/
│
└── runtime/                          # 工具层（位于仓库根）
    ├── contracts/                    # 校验规则（state machine / visual / skills / gates / pipeline）
    ├── .artifacts/                   # Artifact Registry 缓存（gitignored）
    └── (compiled_prompt / semantic_lint / qa_result / runs ...)  # 派生产物缓存
```

> 注：上述路径中以 `<...>` 形式出现的均为占位结构示意，不代表已存在的真实项目。

## 4. 各层职责 / Layer Responsibilities

| 层 / Layer | 路径 / Path | 持有内容 / Holds | 写入与不可变规则 / Write & Immutability |
| --- | --- | --- | --- |
| 系统 / System | `00-system/` | 架构、边界、治理文档、Codex 指令 | 受控编辑；变更需评审；不存放生产数据 |
| 原料 / Raw | `01-raw/` | 不可变原始输入、外部生成产物首次落地 | **只追加（append-only）**；落地后永不重写；唯一的“原始事实” |
| 维基 / Wiki | `02-wiki/` | 规范 Markdown 卡片（11 类资产）、执行包、仪表盘、索引 | 长期事实来源；持久决策必须写到此处；通过 runtime 校验 |
| Agent 工作 / Agent-work | `50-agent-work/` | 真实运行、生成中间物、QA 记录、修复笔记、日志 | 可频繁追加；中间物可被清理/归档；不是长期事实来源 |
| 归档 / Archive | `90-archive/` | 被拒绝、废弃、退役、遗留内容 | 只进不改（write-once for the record）；用于追溯与隔离 |
| 工具 / Runtime | `runtime/` | 校验规则（contracts）+ 派生缓存 + Artifact Registry | contracts 是验证规则；其余输出是派生缓存；不持有规范知识 |

## 5. 规范卡片所在位置 / Where Canonical Cards Live

`02-wiki/story-lab/` 下按编号分区，便于在 Obsidian 中检索与组织：

- `10-projects/` — 故事项目卡片（`type: story_project`）与 `project-index`。
- `20-worlds/` — 世界观卡片。
- `30-characters/` — 角色卡片（`type: character`）。
- `40-scenes/` — 场景卡片（`type: scene`）。
- `50-visual-styles/` — 视觉风格卡片（`type: visual_style`）。
- `60-prompts/` — 提示配方卡片（`type: prompt_recipe`），**与执行包分离**。
- `70-execution-packages/` — 图像执行包卡片（`type: image_execution_package`）。
- `reference-assets/` — 已接受参考资产卡片（`type: reference_asset`）。
- `80-skills-tools-workflows/` — 技能卡（`type: skill_card`）、工作流卡（`type: workflow_card`），以及模板与字段 schema。

资产模型的完整定义见 [Canonical-Asset-Model.md](./Canonical-Asset-Model.md)。

## 6. runtime 作为工具层的关系 / How Runtime Relates as a Tool Layer

`runtime/` 留在仓库根，作为 **可执行工具层**，服务于 wiki 但不替代它：

- `runtime/contracts/` 持有 **校验规则（VALIDATION RULES ONLY）**：状态机（state machine）、视觉资产规则（visual assets）、技能规则（skills）、质量门（quality gates）、流水线动作（pipeline actions）。
- runtime 的其他输出（`compiled_prompt`、`semantic_lint`、`qa_result`、`runs` 等）是 **派生产物 / 运行缓存（derived artifacts / run caches）**。
- **Artifact Registry 是 runtime 缓存 + 血缘助手（lineage helper），不是规范资产登记表（NOT the canonical asset registry）。** 规范登记表是 `02-wiki` 中的参考资产卡片 + 执行包卡片集合。

详见：
- runtime 是工具层：[../runtime-boundary/Runtime-Is-Tool-Layer.md](../runtime-boundary/Runtime-Is-Tool-Layer.md)
- Artifact Registry 是缓存：[../runtime-boundary/Artifact-Registry-Is-Cache.md](../runtime-boundary/Artifact-Registry-Is-Cache.md)
- Markdown 是规范来源：[../runtime-boundary/Markdown-Is-Canonical.md](../runtime-boundary/Markdown-Is-Canonical.md)

## 7. 两窗口操作模型 / Two-Window Operating Model

- **WebGPT 命令/规划窗口**：设计与评审生产计划（plan & review），不直接触碰本地文件系统执行细节。
- **Codex（本地执行）**：执行本地文件系统操作与 runtime 任务（validate / lint / compile / qa）。
- **WebGPTImage 窗口（独立）**：只接收受控的执行单（controlled execution sheets），**永不看到整个仓库**，仅负责单图外部生成。

流向：生成产物先落 `01-raw/` → QA/修复进入 `50-agent-work/` → 被接受的知识写回 `02-wiki/` → 被拒绝/废弃进入 `90-archive/`。

图像生产治理细则见 [Image-Production-Governance.md](./Image-Production-Governance.md)。

## 8. 核心规则 / Core Rules

1. **完整的图像执行包必须是独立的 `.md` 文件**（complete image execution package must be its own `.md`），位于 `02-wiki/story-lab/70-execution-packages/`。
2. **每次生成都产生一条 run-record**（every generation produces a run-record），位于 `50-agent-work/story-lab/runs/`。
3. **被接受的输出必须绑定 `package_id` / `scene_id` / `character_id` / `reference_assets`**（accepted output binds these），并写回参考资产卡片。
4. **每次失败都进入修复队列**（every failure enters the repair queue），在 `50-agent-work/story-lab/repair-notes/` 开 RepairNote。
5. **提示配方与执行包分离**（prompt recipes are separate from execution packages）：配方在 `60-prompts/`，执行包在 `70-execution-packages/`。
6. **图像文件是资产，Markdown 是可维护的知识层**（image files are assets, Markdown is the maintainable knowledge layer）：二进制图像不进 git，卡片记录其位置与来源。
7. **任何持久生产决策必须写回 `02-wiki` 规范卡片**：runtime 产物只是派生缓存，不能作为长期事实来源。
8. **原料层只追加、永不重写**（`01-raw/` is append-only）；中间物属于 `50-agent-work/`；废弃物属于 `90-archive/`。
9. **runtime 永不调用外部图像工具**：它停在一个人工执行点（human execution point）。
