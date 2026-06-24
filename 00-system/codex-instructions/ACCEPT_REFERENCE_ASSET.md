# Codex 指令：接受参考资产 / ACCEPT REFERENCE ASSET

> PROCEDURE ONLY. 本文件只描述接受参考资产的过程，不实例化任何真实图像、提示或资产。一律使用占位符（`<asset-id>`、`<run-id>`、`<package-id>`、`<scene-id>`、`<character-id>`、EXAMPLE_VALUE、占位）。

## 0. 适用范围 / Scope

指导 Codex 把一个候选 **接受为参考资产（reference_asset）**：先核验 `50-agent-work/` 中的遥测 + 图像 QA + 资产 QA 已通过，再在 `02-wiki/story-lab/reference-assets/` 写/更新规范 ReferenceAsset 卡片。**二进制图像保持在 git 之外；卡片记录其位置与来源（provenance）。**

## 1. 前置核验 / Precondition Verification

确认在 `50-agent-work/story-lab/` 中：

- **遥测 / telemetry** 已通过 `validate-telemetry`（无遥测不得接受）。
- **图像 QA / image QA** 已记录并通过。
- **资产 QA / asset QA** 已通过（`qa_result` 缓存存在且合格）。
- 对应 GenerationRun：`50-agent-work/story-lab/runs/<run-id>.md` 状态可进入接受。

## 2. 写/更新 ReferenceAsset 卡片 / Write or Update the Card

1. 从模板复制：`02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/`（取 reference_asset 模板）。
2. 在 `02-wiki/story-lab/reference-assets/` 写/更新 `<asset-id>.md`。
3. frontmatter（占位）：

```yaml
---
type: reference_asset
id: <asset-id>
title_zh: 占位参考资产
title_en: EXAMPLE_VALUE
status: accepted
project_id: <project-id>
related_assets:
  - <package-id>
  - <run-id>
  - <scene-id>
  - <character-id>
source_paths:
  - 50-agent-work/story-lab/runs/<run-id>.md
tags: [占位]
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 1.0.0
canonical: true
---
```

## 3. 卡片正文必填内容 / Required Body Content

- **接受来源 / accepted source**：指向该候选的来源（执行包 + 运行 + 落地于 `01-raw/` 的产物位置）。
- **允许用途 / allowed usage**：占位清单。
- **禁止用途 / forbidden usage**：占位清单。
- **被谁使用 / used-by**：占位（引用使用该资产的执行包等）。
- **QA 证据 / QA evidence**：指向 `50-agent-work/` 中遥测/图像 QA/资产 QA 记录的路径。
- **文件位置策略 / file-location policy**：二进制图像 **不入 git**；卡片记录其存放位置 + 来源（provenance）。

## 4. 绑定与一致性 / Bind & Reconcile

- 绑定 `package_id` / `scene_id` / `character_id` / `reference_assets`（accepted output binds these）。
- 更新相关执行包卡片的 `used-by` / `related_assets`，并把 GenerationRun 标为 `accepted`。
- Artifact Registry 中的同名条目仅作缓存/血缘镜像；**规范登记是本 Markdown 卡片**。

## 5. 完成判定 / Done Criteria

- 遥测 + 图像 QA + 资产 QA 三者均已通过并被引用。
- ReferenceAsset 规范卡片已写入 `02-wiki`，绑定齐全。
- 文件位置策略明确：二进制图像在 git 外，卡片记录位置与来源。

## 6. 明确声明 / Explicit Statement

**本指令仅为接受过程（procedure only），使用占位符，不实例化真实资产。**

## 7. 相关文档 / Related Docs

- 回填生成运行：`00-system/codex-instructions/BACKFILL_GENERATION_RUN.md`
- Markdown 是规范来源：[../runtime-boundary/Markdown-Is-Canonical.md](../runtime-boundary/Markdown-Is-Canonical.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
