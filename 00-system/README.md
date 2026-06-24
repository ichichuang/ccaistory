# 00-system — 系统级文档层 / System Documentation Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本层只描述结构、边界与流程，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

`00-system` 是 AI+Story 仓库的 **系统级文档层**：它承载架构 doctrine、runtime 边界规范、面向 Codex 的执行指令，以及迁移 / 验收报告。它**不放任何生产内容**（故事、世界观、角色、资产卡片等都属于 `02-wiki`）。

返回根说明：[../README.md](../README.md)。

## 包含的子目录 / Subfolders

| 子目录 / Subfolder | 用途 / Purpose |
| --- | --- |
| [architecture/](architecture/) | 架构 doctrine：总体分层模型、资产本体与治理、Markdown 与图像资产的关系等结构性文档。 |
| [runtime-boundary/](runtime-boundary/) | runtime 边界文档：明确 runtime 作为 validator / compiler / linter / QA helper 的职责边界，以及它**不做**什么（不创建项目、不生成图像、不创建执行包）。 |
| [codex-instructions/](codex-instructions/) | 面向 Codex 的分步执行指令（step-by-step），描述各类操作流程如何在本仓库结构内进行。 |
| [migration-reports/](migration-reports/) | 迁移与清理 / 验收报告：记录结构重构、目录迁移与清理过程的可追溯文档。 |

## 应放在这里的内容 / What goes here

- 架构与边界的 **结构性文档**（doctrine、规范、约束）。
- Codex / agent 的执行指令模板与流程说明。
- 迁移、重构、清理的报告。

## 不应放在这里的内容 / What must NOT go here

- 真实故事、世界观、角色、场景、视觉风格、提示词或资产内容（→ `02-wiki`）。
- 原始输入或生成原料（→ `01-raw`）。
- agent 运行记录、QA、修复笔记（→ `50-agent-work`）。
- 废弃 / 退役材料（→ `90-archive`）。
- runtime 缓存或派生产物（→ `runtime` 的忽略目录）。

## 写入与跟踪规则 / Write & tracking rules

- 本层文档**受版本管理跟踪（tracked）**。
- 机器规则的事实源在 `runtime/contracts`；若本层文档描述与 contracts 冲突，**以 contracts 为准**，并应更新文档使其同步。
- 文档应保持架构层面，避免写入任何会过期的真实样例。

## 关键邻居文档 / Key sibling docs

- [01-raw 原始层](../01-raw/README.md)
- [02-wiki 规范知识层](../02-wiki/README.md)
- [50-agent-work 操作记录层](../50-agent-work/README.md)
- [90-archive 归档层](../90-archive/README.md)
- [runtime 工具层](../runtime/README.md)
