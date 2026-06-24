# 02-wiki / story-lab — 故事实验室规范维基 / Story-Lab Canonical Wiki

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本目录只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

本目录是 `02-wiki` 规范层下的 **story-lab 规范维基**，以编号子目录组织全部规范卡片（canonical cards）。它是故事生产知识的人类可读事实来源。

返回上层：[../README.md](../README.md) ｜ 返回根：[../../README.md](../../README.md)。

## 编号子目录 / Numbered folders

| 文件夹 / Folder | 承载内容 / Holds |
| --- | --- |
| `00-dashboard/` | 仪表盘与看板（dashboards）：全局状态、base 规格、控制视图。 |
| `10-projects/` | 项目卡片（StoryProject）与 project-index。 |
| `20-worlds/` | 世界观卡片（World）。 |
| `30-characters/` | 角色卡片（Character）。 |
| `40-scenes/` | 场景卡片（Scene）。 |
| `50-visual-styles/` | 视觉风格卡片（VisualStyle）。 |
| `60-prompts/` | 提示配方卡片（PromptRecipe），与执行包分离。 |
| `70-execution-packages/` | 图像执行包卡片（ImageExecutionPackage）。 |
| `80-skills-tools-workflows/` | 技能 / 工具 / 工作流卡片（SkillCard / WorkflowCard），含模板与字段 schema。 |
| `90-indexes-zh/` | 中文索引（indexes）：跨卡片检索与汇总。 |
| `maps/` | 关系地图（maps）：实体之间的导航与全局视图。 |
| `reference-assets/` | 参考资产卡片（ReferenceAsset，已接受资产的规范记录）。 |

## 模板与字段 schema / Templates & field schemas

- **模板（templates）** 位于 `80-skills-tools-workflows/templates/canonical-assets/`：规范资产卡片的结构模板。
- **字段 schema（field schemas / metadata-fields）** 位于 `80-skills-tools-workflows/metadata-fields/`：规范卡片的元数据字段定义。
- 模板、字段 schema、索引、仪表盘与 base 规格 **会被版本管理跟踪**。

## 关键约定 / Key conventions

- **完整的图像执行包必须是它自己的独立 `.md` 文件（the complete image execution package must be its own `.md` file）**，置于 `70-execution-packages/`，并与 `60-prompts/` 中的提示配方保持分离。
- 提示配方（PromptRecipe）与执行包（ImageExecutionPackage）**分层管理**：配方描述可复用的提示策略，执行包描述一次完整的图像执行。
- 持久生产决策写回本层卡片；runtime 输出与 Artifact Registry 仅为派生缓存。

## 不应放在这里的内容 / What must NOT go here

- 原始输入或生成原料（→ `01-raw/story-lab`）。
- 运行记录、QA、修复笔记（→ `50-agent-work/story-lab`）。
- 废弃 / 退役材料（→ `90-archive/story-lab`）。

## 关键邻居文档 / Key sibling docs

- [02-wiki 规范知识层](../README.md)
- [01-raw / story-lab 原始输入](../../01-raw/story-lab/README.md)
- [50-agent-work / story-lab 运行记录](../../50-agent-work/story-lab/README.md)
- [90-archive / story-lab 归档](../../90-archive/story-lab/README.md)
