# 90-archive / story-lab — 故事实验室归档 / Story-Lab Archive

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本目录只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

本目录是 `90-archive` 归档层下的 **story-lab 归档区**，按类型组织被拒绝、废弃、退役与遗留的材料。

返回上层：[../README.md](../README.md) ｜ 返回根：[../../README.md](../../README.md)。

## 子目录 / Subfolders

| 子目录 / Subfolder | 用途 / Purpose |
| --- | --- |
| `legacy-projects/` | 遗留项目（legacy projects）：旧结构或已停用的项目留存。 |
| `deprecated-prompts/` | 已废弃的提示（deprecated prompts）。 |
| `old-runs/` | 旧运行记录（old runs）：从 `50-agent-work` 退役的历史运行档案。 |
| `rejected-assets/` | 被拒绝的资产（rejected assets）。 |
| `retired-execution-packages/` | 已退役的图像执行包（retired execution packages）。 |

## 写入规则 / Write rules

- **只入不改（append-only）**：材料移入后作为历史留存，不再就地编辑。
- 这里的资产、提示与执行包**不得**再被现行生产作为参考依赖使用。
- 整个 `90-archive/` 被 `.gitignore` 忽略，骨架靠 README 与 `.gitkeep` 维持；二进制资产同样被忽略。

## 不应放在这里的内容 / What must NOT go here

- 现行规范卡片（→ `02-wiki/story-lab`）。
- 原始输入或生成原料（→ `01-raw/story-lab`）。
- 活动中的运行记录、QA、修复笔记（→ `50-agent-work/story-lab`）。

## 关键邻居文档 / Key sibling docs

- [90-archive 归档层](../README.md)
- [02-wiki / story-lab 规范维基](../../02-wiki/story-lab/README.md)
- [50-agent-work / story-lab 运行记录](../../50-agent-work/story-lab/README.md)
- [01-raw / story-lab 原始输入](../../01-raw/story-lab/README.md)
