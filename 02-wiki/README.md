# 02-wiki — 规范知识层 / Canonical Knowledge Layer

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本层只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<project-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

`02-wiki` 是 AI+Story 的 **第 2 层：规范 Markdown 生产知识（canonical Markdown production knowledge）**。它是故事、世界观、角色、场景、视觉风格、提示配方、图像执行包、技能 / 工具 / 工作流、索引、地图、参考资产与仪表盘的 **长期、人类可读的事实来源（long-term human-readable source of truth）**。

核心立场 / Core stance：**图像文件是资产（assets），Markdown 才是可维护的知识层（the maintainable knowledge layer）。** 任何持久的生产决策都必须写回本层的规范卡片，而不是停留在 runtime 缓存或 Artifact Registry 中。

返回根说明：[../README.md](../README.md)。

## 应放在这里的内容 / What goes here

- **规范卡片（canonical cards）**：项目、世界观、角色、场景、视觉风格、提示配方、图像执行包、参考资产、技能 / 工作流。
- **索引、地图、仪表盘（indexes / maps / dashboards）**：用于导航与全局视图的规范文档。
- **模板与字段 schema（templates / field schemas）**：规范卡片的结构模板与元数据字段定义。

具体编排见子目录说明：[story-lab 规范维基](story-lab/README.md)。

## 不应放在这里的内容 / What must NOT go here

- 原始输入或生成原料（→ `01-raw`）。
- agent 运行记录、编译后提示、semantic-lint / QA 结果、image-review 表单、修复笔记（→ `50-agent-work`）。
- 架构 / 边界 / 指令文档（→ `00-system`）。
- 废弃 / 退役 / 遗留材料（→ `90-archive`）。
- runtime 缓存或派生产物（runtime 的忽略目录）。

## 写入与权威性规则 / Write & authority rules

- 本层是 **canonical（规范）**：被接受的生产决策应写回这里，覆盖派生缓存。
- runtime 输出与 Artifact Registry 只是 **派生缓存（derived caches）**，可重建；它们不替代本层卡片。
- 机器规则的事实源在 `runtime/contracts`；卡片描述若与 contracts 冲突，**以 contracts 为准**。
- **会被跟踪的内容**：README、`.gitkeep`、模板、仪表盘、索引、base 规格、字段 schema。
- **默认不提交**：生成图像与 runtime 缓存；二进制资产被 `.gitignore` 忽略（规范资产以 `.md` 卡片承载）。

## 关键邻居文档 / Key sibling docs

- [story-lab 规范维基](story-lab/README.md)
- [01-raw 原始层](../01-raw/README.md)
- [50-agent-work 操作记录层](../50-agent-work/README.md)
- [90-archive 归档层](../90-archive/README.md)
- [00-system 系统文档层](../00-system/README.md)
