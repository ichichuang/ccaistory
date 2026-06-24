# 01-raw — 不可变原始输入层 / Immutable Raw Input Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本层只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<input-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

`01-raw` 是 AI+Story 的 **第 1 层：不可变原始输入（immutable raw inputs）**。它保存进入系统的最原始材料：用户故事、参考输入、截图、原始生成产物、原始模型输出。这些材料是后续一切规范知识的源头。

返回根说明：[../README.md](../README.md)。

## 核心规则 / Core rule：永不重写 / NEVER rewritten

- 本层内容 **永不重写、永不翻译、永不覆盖（never rewritten / never translated / never overwritten）**。
- 原料一旦落地即视为历史事实。需要更正、清洗或结构化时，**新建条目或在 `02-wiki` 中产出规范卡片**，而不是修改原文。
- 任何持久的生产决策都应写回 `02-wiki` 规范卡片，`01-raw` 只作为可追溯的来源证据。

## 应放在这里的内容 / What goes here

- 原始用户输入（用户提供的故事 / 需求 / 描述）。
- 参考输入（外部参考材料）。
- 截图（screenshots）。
- 原始生成产物（generated-raw，生成过程的首次落地输出）。
- 原始模型输出（model raw outputs）。

详见子目录说明：[story-lab 原始输入](story-lab/README.md)。

## 不应放在这里的内容 / What must NOT go here

- 规范化、改写或结构化后的知识（→ `02-wiki`）。
- agent 的运行记录、QA、修复笔记（→ `50-agent-work`）。
- 架构 / 边界 / 指令文档（→ `00-system`）。
- 废弃 / 退役材料（→ `90-archive`）。

## 提交与二进制规则 / Commit & binary rules

- **二进制资产被 `.gitignore` 忽略（binaries gitignored）**：`*.png`、`*.jpg`、`*.jpeg`、`*.webp`、`*.gif`、`*.psd`、`*.zip`、`*.mp4`、`*.mov` 等不提交。
- 整个 `01-raw/` 目录在 `.gitignore` 中被忽略；目录骨架靠 README 与 `.gitkeep` 维持。
- 因此原始素材本身**默认不入库**，仓库只跟踪结构说明与占位文件。

## 关键邻居文档 / Key sibling docs

- [story-lab 原始输入](story-lab/README.md)
- [02-wiki 规范知识层](../02-wiki/README.md)
- [00-system 系统文档层](../00-system/README.md)
- [50-agent-work 操作记录层](../50-agent-work/README.md)
