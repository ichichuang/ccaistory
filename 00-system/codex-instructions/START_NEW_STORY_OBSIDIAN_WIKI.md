---
type: codex_instruction
id: "START_NEW_STORY_OBSIDIAN_WIKI"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "01-raw, 02-wiki/10-projects"
related_templates: ["StoryProject"]
related_workflows: ["A-Raw-Story-Intake-Workflow", "B-Story-Analysis-and-Canonical-Card-Workflow"]
human_gate: yes
runtime_role: "tool-layer assist: runtime validate/compile/lint/qa only; canonical writes go to 02-wiki cards, never runtime"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
# Codex 指令：在 Obsidian Wiki 下启动新故事项目 / START NEW STORY (Obsidian Wiki)

> PROCEDURE ONLY. 本文件 **不创建真实故事**，只描述启动新项目的过程。所有标识与内容一律使用占位符（`<project-id>`、`<character-id>`、`<scene-id>`、`<visual-style-id>`、EXAMPLE_VALUE、占位）。本指令 **不生成任何故事内容**。

## 0. 适用范围 / Scope

本指令指导 Codex 在新架构下 **启动一个新故事项目的骨架**，不写任何剧情、对白、画面或资产。它只搭建文件与卡片占位，并运行校验。

## 1. 放置原始输入 / Place Raw Input

- 将用户的原始故事输入 **首次落地** 到：`01-raw/story-lab/user-inputs/<project-id>/`。
- 规则：`01-raw/` **只追加、永不重写**（append-only, never rewritten）。
- 不在此步做任何加工或改写；原料保持原样作为唯一“原始事实”。

## 2. 创建 StoryProject 规范卡片 / Create the StoryProject Card

1. 从模板复制：`02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/`（取 story_project 模板）。
2. 在 `02-wiki/story-lab/10-projects/` 新建 `<project-id>.md`。
3. 填写 frontmatter（占位）：

```yaml
---
type: story_project
id: <project-id>
title_zh: 占位项目标题
title_en: EXAMPLE_VALUE
status: draft
project_id: <project-id>
related_assets: []
source_paths:
  - 01-raw/story-lab/user-inputs/<project-id>/
tags: [占位]
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 0.1.0
canonical: true
---
```

> 注意：正文 **不写剧情**，仅放结构性占位小节（目标、范围、待办指针）。

## 3. 初始化下游占位卡片 / Initialize Downstream Placeholder Cards

为以下资产各创建 **占位卡片**（status: draft，正文留占位），并在各自卡片的 `project_id` 指向 `<project-id>`：

- 角色：`02-wiki/story-lab/30-characters/<character-id>.md`（`type: character`）
- 场景：`02-wiki/story-lab/40-scenes/<scene-id>.md`（`type: scene`）
- 视觉风格：`02-wiki/story-lab/50-visual-styles/<visual-style-id>.md`（`type: visual_style`）

将这些占位 id 写入 StoryProject 卡片的 `related_assets`。

## 4. 登记到项目索引 / Register in Project Index

- 在 `02-wiki/story-lab/10-projects/project-index`（项目索引）追加一行，指向 `<project-id>.md`（使用标准 Markdown 链接或反引号路径，不使用双方括号 wikilink）。

## 5. 运行 runtime 校验/状态 / Run Runtime Status & Validation

在不触发任何外部生成的前提下，运行（占位命令名）：

- `validate-contracts` — 确认 contracts 自洽。
- `check-contract-drift` — 检查规则漂移。
- `lint-asset`（对新建卡片）— 校验 frontmatter 与结构。
- `smoke-test` / `pipeline dry-run` — 流程演练，不调用外部图像工具。

> runtime 输出为派生缓存；本步只验证骨架是否合规。

## 6. 完成判定 / Done Criteria

- `01-raw/` 已落地原始输入（未改写）。
- StoryProject 卡片 + 占位的角色/场景/视觉风格卡片已建立，`related_assets` 互相引用。
- 已登记 project-index。
- runtime 校验通过，无漂移。

## 7. 明确声明 / Explicit Statement

**本指令仅为启动过程（procedure only），不创建真实故事，不生成任何剧情、画面或资产。** 真实内容由后续受控流程在人工审批下逐步产生。

## 8. 相关文档 / Related Docs

- 总体架构：[../architecture/AI+Story-Obsidian-Wiki-Architecture.md](../architecture/AI+Story-Obsidian-Wiki-Architecture.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
- 创建执行包：`00-system/codex-instructions/CREATE_IMAGE_EXECUTION_PACKAGE.md`
