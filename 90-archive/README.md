# 90-archive — 归档层 / Archive Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本层只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

`90-archive` 是 AI+Story 的 **第 4 层：归档（archive）**。它保存被拒绝、废弃、退役或遗留的材料（rejected / deprecated / retired / legacy），作为历史留存与可追溯证据，但不再参与现行生产。

返回根说明：[../README.md](../README.md)。

## 应放在这里的内容 / What goes here

- 被拒绝的资产与结果（rejected）。
- 已废弃的内容（deprecated）。
- 已退役的卡片 / 包（retired）。
- 遗留材料（legacy）。

详见子目录说明：[story-lab 归档](story-lab/README.md)。

## 不应放在这里的内容 / What must NOT go here

- 现行的规范卡片（→ `02-wiki`）。
- 原始输入或生成原料（→ `01-raw`）。
- 活动中的 agent 运行记录、QA、修复笔记（→ `50-agent-work`）。
- 架构 / 边界 / 指令文档（→ `00-system`）。

## 写入规则 / Write rules

- 归档层 **只入不改（append-only）**：材料从其他层移入后作为历史留存，不再就地编辑。
- 被拒绝 / 废弃 / 退役的资产**不得**再被现行生产作为参考依赖使用（与 Artifact Registry 对 rejected / deprecated 资产的约束一致）。
- 整个 `90-archive/` 在 `.gitignore` 中被忽略；目录骨架靠 README 与 `.gitkeep` 维持。

## 关键邻居文档 / Key sibling docs

- [story-lab 归档](story-lab/README.md)
- [02-wiki 规范知识层](../02-wiki/README.md)
- [50-agent-work 操作记录层](../50-agent-work/README.md)
- [01-raw 原始层](../01-raw/README.md)
