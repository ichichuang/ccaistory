---
type: codex_instruction
id: "REPAIR_FAILED_IMAGE_RUN"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "50-agent-work/story-lab/repair-notes, 90-archive/story-lab/rejected-assets"
related_templates: ["RepairNote"]
related_workflows: ["I-Image-QA-and-Repair-Workflow"]
human_gate: yes
runtime_role: "tool-layer assist: runtime validate/compile/lint/qa only; canonical writes go to 02-wiki cards, never runtime"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
# Codex 指令：修复失败的图像运行 / REPAIR FAILED IMAGE RUN

> PROCEDURE ONLY. 本文件只描述修复记录与分流过程，不实例化任何真实图像、提示或资产。一律使用占位符（`<repair-id>`、`<run-id>`、`<package-id>`、`<asset-id>`、`<prompt-recipe-id>`、`<visual-style-id>`、EXAMPLE_VALUE、占位）。

## 0. 适用范围 / Scope

当某次 GenerationRun 失败时，指导 Codex 在 `50-agent-work/story-lab/repair-notes/` 开一条 **RepairNote（repair_note）**，捕获根因与各类增量（delta），链接失败运行，定义关闭条件与后续 QA，并在拒绝时把失败资产路由到 `90-archive/`。**每次失败都进入修复队列**（every failure enters the repair queue）。

## 1. 开 RepairNote / Open a Repair Note

1. 在 `50-agent-work/story-lab/repair-notes/` 新建 `<repair-id>.md`。
2. frontmatter（占位）：

```yaml
---
type: repair_note
id: <repair-id>
title_zh: 占位修复记录
title_en: EXAMPLE_VALUE
status: needs_repair
project_id: <project-id>
related_assets:
  - <run-id>
  - <package-id>
  - <asset-id>
source_paths:
  - 50-agent-work/story-lab/runs/<run-id>.md
tags: [占位]
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 0.1.0
canonical: false
---
```

## 2. 捕获修复要素 / Capture Repair Elements

在正文中记录（占位结构）：

- **根因 / root cause**：占位说明。
- **必须保留 / must-keep**：哪些已正确、不可改动的部分。
- **必须修复 / must-fix**：哪些必须改正。
- **提示增量 / prompt delta**：对 `<prompt-recipe-id>` 的修改要点。
- **参考增量 / reference delta**：对参考资产 `<asset-id>` 的增删。
- **视觉风格增量 / visual-style delta**：对 `<visual-style-id>` 的调整。
- **执行包增量 / execution-package delta**：对 `<package-id>` 的修改。

## 3. 链接失败运行 / Link the Failed Run

- 在 RepairNote 的 `related_assets` 与正文中链接 `50-agent-work/story-lab/runs/<run-id>.md`（标准 Markdown 链接或反引号路径，不使用双方括号 wikilink）。
- 在该 GenerationRun 卡片中反向标注 `status: needs_repair` 并链接本 RepairNote。

## 4. 关闭条件与后续 QA / Close Condition & Follow-up QA

- **关闭条件 / close condition**：占位，例如“新一轮运行通过遥测 + 图像 QA + 资产 QA，且 must-fix 全部解决”。
- **后续 QA / follow-up QA**：占位，指向重新运行 `validate-telemetry`、图像评审表单、`qa-asset`。
- 修复完成后，可将可复用结论回填到相关规范卡片（执行包/视觉风格/提示配方）。

## 5. 路由被拒资产 / Route Rejected Asset

- 若候选被拒，将失败资产记录与候选移入 `90-archive/story-lab/`（write-once for the record），并在 RepairNote 标注归档位置。
- `90-archive/` 用于隔离与追溯，不再修改。

## 6. 完成判定 / Done Criteria

- RepairNote 已建立，根因/各 delta/关闭条件/后续 QA 齐备。
- 已双向链接失败运行。
- 被拒资产已路由 `90-archive/`，或修复结论已回填规范卡片。

## 7. 明确声明 / Explicit Statement

**本指令仅为修复记录与分流过程（procedure only），使用占位符，不实例化真实资产。**

## 8. 相关文档 / Related Docs

- 回填生成运行：`00-system/codex-instructions/BACKFILL_GENERATION_RUN.md`
- 图像生产治理：[../architecture/Image-Production-Governance.md](../architecture/Image-Production-Governance.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
