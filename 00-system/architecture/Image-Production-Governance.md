# 图像生产治理 / Image Production Governance

> ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 本文件只描述受控流水线与禁令，不实例化任何真实图像、提示或资产。引用一律使用占位符（`<package-id>`、`<run-id>`、`<asset-id>`、EXAMPLE_VALUE、占位）。

## 1. 目的 / Purpose

图像生产被治理为一条 **受控流水线（controlled pipeline）**：从故事到被接受的参考资产，每一步都有明确的层归属、校验关口与人工审批点。runtime 永不直接调用外部图像工具——它停在一个 **人工执行点（human execution point）**。

## 2. 硬性流程 / Hard Flow

```
故事 (story, 02-wiki)
  → 规划/评审 (plan & review in WebGPT command window)
  → Codex 执行 runtime: validate → lint → compile
  → 图像执行包 (image_execution_package, 02-wiki/story-lab/70-execution-packages/)
  → 外部单图生成 (single-image generation in a SEPARATE WebGPTImage window
       at a human execution point)
  → 输出落地 (output → 01-raw/story-lab/user-inputs/)
  → 遥测 + 图像 QA + 资产 QA (telemetry + image QA + asset QA → 50-agent-work)
  → 接受: 写规范参考资产卡片 (accept → reference_asset card in 02-wiki)
     / 拒绝: 进入归档 (reject → 90-archive)
```

逐段说明：

1. **故事 / Story**：来源于 `02-wiki` 的项目/场景/角色规范卡片，绝不直接从原始故事文本出图。
2. **规划/评审 / Plan & Review**：在 WebGPT 命令窗口设计并评审生产计划。
3. **Codex 执行 / Execute**：Codex 调用 runtime 的 `validate` → `lint` → `compile`，产出派生的 `compiled_prompt`、`semantic_lint` 缓存。
4. **执行包 / Execution Package**：在 `02-wiki/story-lab/70-execution-packages/` 形成独立 `.md` 执行包卡片，绑定目标资产、场景、角色、视觉风格、提示配方、参考资产。
5. **外部单图生成 / External Single-Image Generation**：在 **独立的 WebGPTImage 窗口**，由人在执行点触发单图生成；该窗口只见受控执行单，不见整个仓库。
6. **输出落地 / Output**：生成产物 **首先落入 `01-raw/`**（首次落地、不可重写）。
7. **QA / QA**：遥测（telemetry）、图像 QA、资产 QA 记录写入 `50-agent-work/story-lab/`。
8. **接受或拒绝 / Accept or Reject**：接受 → 在 `02-wiki/story-lab/reference-assets/` 写规范参考资产卡片；拒绝 → 移入 `90-archive/`。

## 3. 流水线关口与层映射 / Stage-to-Layer Map

| 阶段 / Stage | 执行者 / Actor | 产物所在层 / Layer | 类型 / Type |
| --- | --- | --- | --- |
| 规划/评审 | WebGPT 命令窗口 | （计划文档，受控） | — |
| validate/lint/compile | Codex + runtime | runtime 派生缓存 | derived artifact |
| 执行包定稿 | Codex | `02-wiki/.../70-execution-packages/` | `image_execution_package` |
| 单图生成 | WebGPTImage 窗口（人触发） | `01-raw/.../user-inputs/` | 原始产物 |
| 遥测/图像 QA/资产 QA | Codex + runtime | `50-agent-work/story-lab/` | `generation_run` + QA |
| 接受 | 人工审批 + Codex | `02-wiki/.../reference-assets/` | `reference_asset` |
| 拒绝/废弃 | 人工审批 + Codex | `90-archive/story-lab/` | archived |

## 4. 硬性禁令 / Hard Prohibitions

1. **禁止从原始故事直接出图**（no image straight from raw story）：必须先经规划、执行包与编译。
2. **禁止跳过提示编译 + 语义 lint**（no skipping prompt compile + semantic lint）：`compile` 与 `semantic_lint` 是出图前的必经关口。
3. **禁止在没有执行遥测的情况下接受候选**（no accepting a candidate without execution telemetry）：无遥测即无接受依据。
4. **禁止把排版旁白烧录进源插图**（no typed narration baked into source illustrations）：文字旁白与源图分离。
5. **runtime 永不调用外部图像工具**（runtime never calls the external image tool）：它停在人工执行点，由人在 WebGPTImage 窗口触发。

## 5. 人工审批关口 / Human-Approval Gates

| 关口 / Gate | 触发时机 / When | 审批内容 / What is approved |
| --- | --- | --- |
| Gate A — 计划批准 | 执行包定稿前 | 生产计划、绑定关系、允许/禁止内容 |
| Gate B — 执行触发 | 外部出图前 | 在 WebGPTImage 窗口手动触发单图生成（human execution point） |
| Gate C — 接受/拒绝 | QA 完成后 | 候选是否接受为参考资产，或移入归档 |

只有三道关口全部满足，候选才能成为 `02-wiki` 中的规范参考资产。

## 6. 相关文档 / Related Docs

- 资产模型：[Canonical-Asset-Model.md](./Canonical-Asset-Model.md)
- 总体架构：[AI+Story-Obsidian-Wiki-Architecture.md](./AI+Story-Obsidian-Wiki-Architecture.md)
- runtime 边界：[../runtime-boundary/Runtime-Is-Tool-Layer.md](../runtime-boundary/Runtime-Is-Tool-Layer.md)
- 创建执行包：`00-system/codex-instructions/CREATE_IMAGE_EXECUTION_PACKAGE.md`
- 回填生成运行：`00-system/codex-instructions/BACKFILL_GENERATION_RUN.md`
