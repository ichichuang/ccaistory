# 01-raw / story-lab — 故事实验室原始输入 / Story-Lab Raw Inputs

> ARCHITECTURE / WORKFLOW DOCUMENTATION ONLY. 本目录只描述结构与规则，不实例化任何真实故事、角色、场景、视觉风格、提示词或资产内容。一切示例使用占位符（`<input-id>`、`<asset-id>`、`EXAMPLE_VALUE`、占位）。

本目录是 `01-raw` 原始层下的 **story-lab 原始输入区**。它是各类原始材料**首次落地（land FIRST）** 的地方，尤其是 **来自生成的原始输出会先落在这里（raw outputs from generation land here FIRST）**，之后才进入 `50-agent-work` 处理或在 `02-wiki` 形成规范卡片。

返回上层：[../README.md](../README.md) ｜ 返回根：[../../README.md](../../README.md)。

## 子目录 / Subfolders

| 子目录 / Subfolder | 用途 / Purpose |
| --- | --- |
| `user-inputs/` | 原始用户输入：用户提供的故事、需求、设定描述的首次落地。 |
| `reference-inputs/` | 参考输入：外部参考材料、灵感来源、引用素材的原始副本。 |
| `screenshots/` | 截图：界面、参考画面或来源证据的原始截图。 |
| `generated-raw/` | 原始生成产物：生成流程产出的原始结果**首次落地**于此。 |
| `model-raw-outputs/` | 原始模型输出：模型返回的未加工原始输出。 |

## 写入与不可变规则 / Write & immutability rules

- 所有内容 **永不重写、永不翻译、永不覆盖**。需要更正时在下游层新建，不改原文。
- 来自生成的原始输出 **必须先落在本目录（land FIRST）**，再由 `50-agent-work` 形成运行记录，或在 `02-wiki` 写成规范卡片。
- 二进制资产（图片、压缩包、视频等）被 `.gitignore` 忽略；本目录在 `.gitignore` 中整体忽略，骨架靠 README 与 `.gitkeep` 维持。

## 不应放在这里的内容 / What must NOT go here

- 规范化后的知识（→ `02-wiki/story-lab`）。
- 运行记录、QA、修复笔记（→ `50-agent-work/story-lab`）。
- 废弃 / 退役材料（→ `90-archive/story-lab`）。

## 关键邻居文档 / Key sibling docs

- [01-raw 原始层](../README.md)
- [02-wiki / story-lab 规范维基](../../02-wiki/story-lab/README.md)
- [50-agent-work / story-lab 运行记录](../../50-agent-work/story-lab/README.md)
