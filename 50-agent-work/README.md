# 50-agent-work — 操作记录层 / Agent-Work Operational Records Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本层只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<run-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

`50-agent-work` 是 AI+Story 的 **第 3 层：agent 生成的操作记录（generated operational records）**。它保存真实 agent 运行、编译后提示、semantic-lint 结果、QA 结果、image-review 表单与修复笔记 —— 即生产过程中产生的中间物与可追溯记录。

返回根说明：[../README.md](../README.md)。

## 应放在这里的内容 / What goes here

- 真实 agent 运行记录（run records）。
- 编译后的提示（compiled prompts）与中间物（intermediates）。
- semantic-lint 结果、QA 结果。
- image-review 表单与修复笔记（repair notes）。

详见子目录说明：[story-lab 运行记录](story-lab/README.md)。

## 不应放在这里的内容 / What must NOT go here

- 规范卡片（→ `02-wiki`）：被接受的结论应**写回** `02-wiki`，而非停留于此。
- 原始输入或生成原料（→ `01-raw`）。
- 架构 / 边界 / 指令文档（→ `00-system`）。
- 废弃 / 退役材料（→ `90-archive`）。

## 写入与提交规则 / Write & commit rules

- 本层是 **生成物（generated）**：是操作记录，不是事实来源。持久的生产决策必须写回 `02-wiki` 规范卡片。
- runtime 输出与 Artifact Registry 属于 **派生缓存（derived caches）**，可重建。
- 整个 `50-agent-work/` 在 `.gitignore` 中被忽略；**多数内容不提交（mostly gitignored）**，仅跟踪 README 与 `.gitkeep` 以维持目录骨架。
- 二进制资产（图片、压缩包、视频等）同样被忽略。

## 关键邻居文档 / Key sibling docs

- [story-lab 运行记录](story-lab/README.md)
- [02-wiki 规范知识层](../02-wiki/README.md)
- [01-raw 原始层](../01-raw/README.md)
- [90-archive 归档层](../90-archive/README.md)
- [runtime 工具层](../runtime/README.md)
