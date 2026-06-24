# AI+Story — Obsidian Story Production Wiki + Runtime Tool Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本仓库的所有 README 只描述结构与流程，不实例化任何真实故事、世界观、角色、场景、视觉风格、提示词或资产内容。一切示例一律使用占位符（例如 `<project-id>`、`<asset-id>`、`<run-id>`、`EXAMPLE_VALUE`、占位）。

AI+Story 已重构为一个 **Obsidian Story Production Wiki（故事生产维基）** 加上一个 **runtime 工具层（runtime tool layer）**。

- **Wiki 部分**：以 Obsidian Markdown **规范卡片（canonical cards）** 作为故事、世界观、角色、场景、视觉风格、提示配方、图像执行包、参考资产、技能 / 工具 / 工作流的 **长期、人类可读的事实来源（long-term human-readable source of truth）**，全部位于 `02-wiki`。
- **runtime 部分**：作为可执行的 **校验 / 编译 / lint / QA helper + 缓存生产者（validator / compiler / linter / QA helper + cache producer）**。它**不是主资产管理系统（NOT the main asset management system）**，只负责验证规则与派生缓存。

核心立场 / Core stance：**图像文件是资产（assets），Markdown 才是可维护的知识层（the maintainable knowledge layer）。** 任何持久的生产决策都必须写回 `02-wiki` 中对应的规范卡片。

## 1. 分层模型 / Layer Model

| 层 / Layer | 角色 / Role | 可变性 / Mutability |
| --- | --- | --- |
| `00-system` | 架构文档（architecture doctrine）、runtime 边界（runtime-boundary）文档、codex-instructions、迁移报告（migration-reports） | 受版本管理跟踪 |
| `01-raw` | 不可变原始输入：用户故事、参考输入、截图、原始生成产物、原始模型输出 | **永不重写 / NEVER rewritten** |
| `02-wiki` | 规范 Markdown 生产知识（canonical）：projects / worlds / characters / scenes / visual-styles / prompts / execution-packages / skills-tools-workflows / indexes / maps / reference-assets / dashboards | 可演进，但以规范卡片为准 |
| `50-agent-work` | 真实 agent 运行、编译后提示、semantic-lint 结果、QA 结果、image-review 表单、修复笔记 —— 生成的操作记录（operational records） | 生成物，多数不提交 |
| `90-archive` | 被拒绝 / 废弃 / 退役 / 遗留材料（rejected / deprecated / retired / legacy） | 只入不改 |
| `runtime` | **validator / compiler / linter / QA helper + cache producer**，位于仓库根 | 工具层，不持有规范知识 |

数据的典型流动 / Typical data flow：

1. 外部或人工原始输入 → 落入 `01-raw`（首次落地，永不重写）。
2. 经过规划与编写 → 在 `02-wiki` 形成规范卡片。
3. 真实 agent 运行、生成中间物、QA 记录、修复笔记 → 写入 `50-agent-work`。
4. 被接受的知识 → 写回 `02-wiki`；被拒绝 / 废弃 / 退役 / 遗留 → 移入 `90-archive`。
5. `runtime` 横向服务于第 2–4 步，提供校验、编译、lint、QA、缓存能力，但不拥有规范知识。

关于 runtime 与缓存 / runtime and caches：

- `runtime/contracts` = **验证规则（validation rules only）**，是机器可读的事实源。
- runtime 输出 + Artifact Registry = **派生缓存（derived caches）**，可随时重建。
- 持久的生产决策必须写回 `02-wiki` 规范卡片，而不是停留在缓存里。

## 2. 目录树 / Directory Tree

```
AI+Story/
├── 00-system/                         # 系统级文档（architecture / runtime-boundary / codex-instructions / migration-reports）
│   ├── architecture/
│   ├── runtime-boundary/
│   ├── codex-instructions/
│   └── migration-reports/
├── 01-raw/                            # 第 1 层：不可变原始输入（NEVER rewritten）
│   └── story-lab/
│       ├── user-inputs/
│       ├── reference-inputs/
│       ├── screenshots/
│       ├── generated-raw/
│       └── model-raw-outputs/
├── 02-wiki/                           # 第 2 层：规范 Markdown 知识（canonical）
│   └── story-lab/
│       ├── 00-dashboard/
│       ├── 10-projects/
│       ├── 20-worlds/
│       ├── 30-characters/
│       ├── 40-scenes/
│       ├── 50-visual-styles/
│       ├── 60-prompts/
│       ├── 70-execution-packages/
│       ├── 80-skills-tools-workflows/
│       ├── 90-indexes-zh/
│       ├── maps/
│       └── reference-assets/
├── 50-agent-work/                     # 第 3 层：agent 生成的操作记录
│   └── story-lab/
│       ├── runs/
│       ├── compiled-prompts/
│       ├── semantic-lint-results/
│       ├── qa-results/
│       ├── image-review-forms/
│       └── repair-notes/
├── 90-archive/                        # 第 4 层：废弃 / 退役 / 遗留
│   └── story-lab/
│       ├── legacy-projects/
│       ├── deprecated-prompts/
│       ├── old-runs/
│       ├── rejected-assets/
│       └── retired-execution-packages/
└── runtime/                           # 工具层：validator / compiler / linter / QA helper + cache producer
```

## 3. 提交策略 / Commit Policy

- **默认不提交生成图像或 runtime 缓存（no generated images or runtime caches committed by default）。**
- 原始 / 生成的二进制资产（`*.png`、`*.jpg`、`*.webp`、`*.psd`、`*.zip`、`*.mp4` 等）与 `runtime/.runs/`、`runtime/.artifacts/` 等缓存目录均被 `.gitignore` 忽略。
- **会被跟踪（tracked）的内容**：README、`.gitkeep`、模板（templates）、仪表盘（dashboards）、索引（indexes）、base 规格（base specs）、字段 schema（field schemas）。
- 因此 `01-raw`、`50-agent-work`、`90-archive` 的目录骨架靠 README 与 `.gitkeep` 维持，而非其中的原料或运行产物。

## 4. 如何使用 / How to use（Quickstart）

1. **先读架构文档**：[00-system 架构与边界](00-system/README.md)，其中包含总体架构、runtime 边界、codex-instructions 与迁移报告。
2. **进入规范知识层**：[02-wiki 规范知识总览](02-wiki/README.md) 与 [story-lab 规范维基](02-wiki/story-lab/README.md)。
3. **查看仪表盘 / 索引**：规范的看板与索引位于 `02-wiki/story-lab/00-dashboard/`、`02-wiki/story-lab/90-indexes-zh/` 与 `02-wiki/story-lab/maps/`（通过 02-wiki story-lab README 导航）。
4. **原始输入只读**：任何原料先看 [01-raw 原始层](01-raw/README.md) 与 [story-lab 原始输入](01-raw/story-lab/README.md)，只读、不重写。
5. **查看运行与 QA 记录**：[50-agent-work 操作记录层](50-agent-work/README.md) 与 [story-lab 运行记录](50-agent-work/story-lab/README.md)。
6. **检索退役材料**：[90-archive 归档层](90-archive/README.md) 与 [story-lab 归档](90-archive/story-lab/README.md)。
7. **运行工具层**：见下方关键命令；详细说明见 [runtime/README.md](runtime/README.md)。

## 5. 关键 runtime 命令 / Key runtime commands

在仓库根目录运行：

```bash
python runtime/aistory.py status
python runtime/aistory.py validate
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
```

- `status`：报告 runtime 与 vault 的当前状态。
- `validate`：执行结构校验。
- `validate-contracts`：校验机器事实源 `runtime/contracts`。
- `check-contract-drift`：检测 contracts 与文档 / 测试之间的漂移。
- `smoke-test`：端到端冒烟测试。

> 规则约定：机器规则变更先改 `runtime/contracts`，再同步文档与测试；若 Markdown 与 contracts 冲突，**以 contracts 为准**。runtime 不创建故事项目、不生成图像、不创建执行包或发布包。
