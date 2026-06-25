---
type: codex_instruction
id: "CREATE_IMAGE_EXECUTION_PACKAGE"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "02-wiki/70-execution-packages"
related_templates: ["ImageExecutionPackage", "PromptRecipe"]
related_workflows: ["E-ImageExecutionPackage-Creation-Workflow"]
human_gate: yes
runtime_role: "tool-layer assist: runtime validate/compile/lint/qa only; canonical writes go to 02-wiki cards, never runtime"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
# Codex 指令：创建图像执行包 / CREATE IMAGE EXECUTION PACKAGE

> PROCEDURE ONLY. 本文件只描述编写图像执行包卡片的过程，不实例化任何真实图像、提示或资产。一律使用占位符（`<package-id>`、`<scene-id>`、`<character-id>`、`<visual-style-id>`、`<prompt-recipe-id>`、`<asset-id>`、EXAMPLE_VALUE、占位）。

## 0. 适用范围 / Scope

指导 Codex 在 `02-wiki/story-lab/70-execution-packages/` 编写一个 **独立 `.md` 的图像执行包卡片（image_execution_package）**。执行包是单次受控生成的完整指令包。**提示配方与执行包分离**：配方在 `60-prompts/`，执行包在 `70-execution-packages/`。

## 1. 从模板创建 / Create From Template

1. 复制模板：`02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/`（取 image_execution_package 模板）。
2. 新建：`02-wiki/story-lab/70-execution-packages/<package-id>.md`。
3. frontmatter（占位）：

```yaml
---
type: image_execution_package
id: <package-id>
title_zh: 占位执行包标题
title_en: EXAMPLE_VALUE
status: draft
project_id: <project-id>
related_assets:
  - <scene-id>
  - <character-id>
  - <visual-style-id>
  - <prompt-recipe-id>
  - <asset-id>          # reference asset 占位
source_paths: []
tags: [占位]
created_at: 2026-06-24
updated_at: 2026-06-24
owner: EXAMPLE_VALUE
version: 0.1.0
canonical: true
---
```

## 2. 绑定目标与依赖 / Bind Target & Dependencies

在卡片正文中显式绑定（均为占位引用，使用反引号路径或标准 Markdown 链接）：

- **目标资产 / target asset**：本次要产出的资产 `<asset-id>`。
- **场景 / scene**：`02-wiki/story-lab/40-scenes/<scene-id>.md`
- **角色 / characters**：`02-wiki/story-lab/30-characters/<character-id>.md`
- **视觉风格 / visual style**：`02-wiki/story-lab/50-visual-styles/<visual-style-id>.md`
- **提示配方 / prompt recipe**：`02-wiki/story-lab/60-prompts/<prompt-recipe-id>.md`
- **参考资产 / reference assets**：`02-wiki/story-lab/reference-assets/<asset-id>.md`

## 3. 定义受控内容 / Define Controlled Content

在执行包中给出（占位结构）：

- **允许内容 / allowed content**：占位清单。
- **禁止内容 / forbidden content**：占位清单（例如：禁止把排版旁白烧录进源插图）。
- **生成顺序 / generation order**：占位步骤序列。
- **手动执行说明 / manual execution instructions**：交给独立 WebGPTImage 窗口的受控执行单要点；强调由人在执行点（human execution point）触发单图生成，runtime 不调用外部工具。
- **QA 接受标准 / QA acceptance criteria**：占位的图像 QA + 资产 QA 通过条件。
- **修复触发条件 / repair triggers**：占位的失败信号 → 触发 RepairNote。

## 4. 编译与 lint / Compile & Lint Before Ready

在把 `status` 从 `draft` 升级为 `ready` 之前，运行（占位命令名）：

- `compile-asset` — 产出派生的 `compiled_prompt` 缓存。
- `lint-asset` / `lint-prompt` — 产出 `semantic_lint` 缓存，确保语义合规。

> 这些产物是派生缓存；执行包卡片本身是规范事实来源。

## 5. 完成判定 / Done Criteria

- 执行包为 **独立 `.md`**，绑定齐全（目标/场景/角色/风格/配方/参考资产）。
- 允许/禁止内容、生成顺序、手动执行说明、QA 标准、修复触发齐备。
- `compile-asset` 与 `lint-asset`/`lint-prompt` 通过后，`status: ready`。

## 6. 明确声明 / Explicit Statement

**本指令仅为编写过程（procedure only），使用占位符，不实例化真实图像、提示或资产。**

## 7. 相关文档 / Related Docs

- 图像生产治理：[../architecture/Image-Production-Governance.md](../architecture/Image-Production-Governance.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
- 回填生成运行：`00-system/codex-instructions/BACKFILL_GENERATION_RUN.md`
