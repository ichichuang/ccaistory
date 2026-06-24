# 50-agent-work / story-lab — 故事实验室操作记录 / Story-Lab Agent-Work Records

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本目录只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<run-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

本目录是 `50-agent-work` 操作记录层下的 **story-lab 工作区**，按阶段组织 agent 生成的运行记录、中间物、QA 与修复材料。

返回上层：[../README.md](../README.md) ｜ 返回根：[../../README.md](../../README.md)。

## 子目录 / Subfolders

| 子目录 / Subfolder | 用途 / Purpose |
| --- | --- |
| `runs/` | 运行记录（run records）：每次生成的可追溯运行档案。 |
| `compiled-prompts/` | 编译后的提示（compiled prompts）：由提示配方编译产出的中间物。 |
| `semantic-lint-results/` | 语义 lint 结果（semantic-lint results）。 |
| `qa-results/` | QA 结果（QA results）。 |
| `image-review-forms/` | 图像评审表单（image-review forms）：人工填写的结构化评审。 |
| `repair-notes/` | 修复笔记（repair notes）：进入修复队列的问题与处置记录。 |

## 工作流约定 / Workflow rules

- **每一次生成都会在 `runs/` 产生一条运行记录（every generation produces a run-record here）。**
- **失败会进入修复队列（failures enter the repair queue）**，并在 `repair-notes/` 形成修复笔记，等待处置与重试。
- 这些都是 **操作记录（operational records）**：被接受的结论必须写回 `02-wiki` 规范卡片，本目录不是事实来源。

## 写入与提交规则 / Write & commit rules

- 内容为生成物；整个 `50-agent-work/` 被 `.gitignore` 忽略，**多数不提交**，仅跟踪 README 与 `.gitkeep`。
- 二进制资产（图片、压缩包、视频等）同样被忽略。

## 不应放在这里的内容 / What must NOT go here

- 规范卡片（→ `02-wiki/story-lab`）。
- 原始输入或生成原料（→ `01-raw/story-lab`）。
- 废弃 / 退役材料（→ `90-archive/story-lab`）。

## 关键邻居文档 / Key sibling docs

- [50-agent-work 操作记录层](../README.md)
- [02-wiki / story-lab 规范维基](../../02-wiki/story-lab/README.md)
- [01-raw / story-lab 原始输入](../../01-raw/story-lab/README.md)
- [90-archive / story-lab 归档](../../90-archive/story-lab/README.md)
