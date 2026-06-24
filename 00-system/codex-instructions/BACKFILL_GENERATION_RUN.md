# Codex 指令：回填生成运行 / BACKFILL GENERATION RUN

> PROCEDURE ONLY. 本文件只描述记录与回填过程，不实例化任何真实图像、提示或资产。一律使用占位符（`<run-id>`、`<package-id>`、`<asset-id>`、`<scene-id>`、`<character-id>`、EXAMPLE_VALUE、占位）。

## 0. 适用范围 / Scope

指导 Codex 在一次 **外部生成（external generation）** 之后：记录 GenerationRun、运行遥测/图像评审/QA、并将 **持久决策回填到 `02-wiki` 规范卡片**。强调：**runtime 输出是缓存，规范记录是 Markdown（the canonical record is Markdown）**。

## 1. 前置：输出已落地 / Precondition

- 外部单图生成的产物应已 **首次落地** 在 `01-raw/story-lab/user-inputs/<project-id>/`（不可重写）。
- 来源执行包为 `02-wiki/story-lab/70-execution-packages/<package-id>.md`。

## 2. 记录 GenerationRun / Record the Run

1. 在 `50-agent-work/story-lab/runs/` 新建 `<run-id>.md`。
2. frontmatter（占位）：

```yaml
---
type: generation_run
id: <run-id>
title_zh: 占位运行记录
title_en: EXAMPLE_VALUE
status: in_production
project_id: <project-id>
related_assets:
  - <package-id>
  - <scene-id>
  - <character-id>
source_paths:
  - 01-raw/story-lab/user-inputs/<project-id>/
tags: [占位]
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 0.1.0
canonical: false      # 运行记录是工作产物，非长期规范来源
---
```

> 正文记录：使用的执行包、生成参数指针、候选位置（指向 `01-raw/`）、人工执行点说明。

## 3. 运行 runtime 校验 / Run Runtime Checks

在 `50-agent-work/` 内运行（占位命令名）：

- `validate-telemetry` — 校验执行遥测是否完整有效（**无遥测不得接受候选**）。
- 图像评审表单 / image review forms — 记录图像 QA。
- `qa-asset` — 产出 `qa_result` 缓存，记录资产 QA。

QA 记录写入 `50-agent-work/story-lab/qa/`，日志/遥测原文写入 `50-agent-work/story-lab/logs/`。

## 4. 判定与分流 / Decide & Route

- **接受 / accept**：进入第 5 步回填规范参考资产卡片。
- **拒绝 / reject**：开 RepairNote（见 `REPAIR_FAILED_IMAGE_RUN.md`），并按需将候选移入 `90-archive/`。

## 5. 回填到规范卡片 / Backfill to Canonical

接受时，把 **持久决策** 写回 `02-wiki`：

1. 写/更新参考资产卡片：`02-wiki/story-lab/reference-assets/<asset-id>.md`（`type: reference_asset`）。
2. 绑定 `package_id` / `scene_id` / `character_id` / `reference_assets`（accepted output binds these）。
3. 在参考资产卡片记录：被接受来源、QA 证据指针、文件位置与来源（二进制图像不入 git）。
4. 更新 GenerationRun 的 `status: accepted`，并在 `related_assets` 链接新参考资产卡片。

> 提醒：Artifact Registry 中的同名条目仅是缓存/血缘便利；**持久记录是 Markdown 卡片**。

## 6. 完成判定 / Done Criteria

- GenerationRun 已记录，遥测/图像 QA/资产 QA 已运行。
- 接受的候选已在 `02-wiki` 写规范参考资产卡片并完成绑定。
- runtime 产物被视为派生缓存，未作为长期事实来源。

## 7. 明确声明 / Explicit Statement

**本指令仅为记录与回填过程（procedure only），使用占位符，不实例化真实资产。**

## 8. 相关文档 / Related Docs

- Markdown 是规范来源：[../runtime-boundary/Markdown-Is-Canonical.md](../runtime-boundary/Markdown-Is-Canonical.md)
- Artifact Registry 是缓存：[../runtime-boundary/Artifact-Registry-Is-Cache.md](../runtime-boundary/Artifact-Registry-Is-Cache.md)
- 接受参考资产：`00-system/codex-instructions/ACCEPT_REFERENCE_ASSET.md`
- 修复失败运行：`00-system/codex-instructions/REPAIR_FAILED_IMAGE_RUN.md`
