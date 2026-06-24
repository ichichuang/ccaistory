# Markdown 是规范来源 / Markdown Is Canonical

> 核心立场文档 / Core doctrine. ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 不实例化任何真实资产；引用一律使用占位符（`<asset-id>`、`<package-id>`、EXAMPLE_VALUE、占位）。

## 1. 核心立场 / Core Doctrine

**Obsidian Markdown 规范卡片是长期生产知识的事实来源（the long-term production knowledge source of truth）。** 它们承载故事、世界观、角色、场景、视觉风格、提示配方、执行包、参考资产、QA 结论与修复记录的持久知识。

runtime 产物是 **派生缓存（derived caches）**。任何持久的生产决策都必须 **回填（backfill）** 到相关的规范卡片。

## 2. 两类事物的归属 / Two Kinds of Facts

| 维度 / Dimension | 验证规则 / Validation Rules | 生产知识 / Production Knowledge |
| --- | --- | --- |
| 拥有者 / Owner | `runtime/contracts` | `02-wiki` Markdown 规范卡片 |
| 内容 / Content | 状态机、视觉资产规则、技能规则、质量门、流水线动作 | 故事/角色/场景/风格/配方/执行包/参考资产/QA/修复的事实 |
| 性质 / Nature | 机器可执行的校验定义 | 人类可读、可长期维护的知识 |
| 派生产物 / Derived | `compiled_prompt`、`semantic_lint`、`qa_result`、`runs`、Registry 条目 | —（规范卡片本身不是派生物） |

**VALIDATION RULES（验证规则）由 runtime/contracts 拥有；PRODUCTION KNOWLEDGE（生产知识）由 Markdown 规范卡片拥有。**

## 3. 派生缓存与回填 / Derived Caches & Backfill

- runtime artifacts（`compiled_prompt` / `semantic_lint` / `qa_result` / `runs` / Artifact Registry 条目）是 **派生缓存**，可被重算、可被清理。
- **任何持久生产决策必须回填到对应的规范卡片**：接受 → 写 `reference_asset` 卡片；执行包定稿 → 写 `image_execution_package` 卡片；失败结论 → 写 `repair_note`（在 `50-agent-work/`）并把可复用结论回填到相关规范卡片。

回填判定（占位）：

```
这条信息是否需要被人类长期检索/维护？
   ├─ 是 → 写回 02-wiki 规范卡片（canonical）
   └─ 否 → 可只留在 runtime 派生缓存（disposable）
```

## 4. 与旧立场的差异 / What Changed From the Old Doctrine

> **旧立场（old）**：contracts 是唯一的机器事实来源（the only machine fact source），Markdown 仅是解释层（only an explanation layer）。

> **新立场（new）**：contracts 拥有 **验证规则**（state machine / visual / skills / gates / pipeline），Markdown 拥有 **生产知识**（故事/资产/执行包/QA/修复的持久事实）。runtime 输出降级为派生缓存，持久决策回填到 Markdown。

要点：知识的“真相源”从 contracts 迁移到了 `02-wiki` 的 Markdown 卡片；contracts 收敛为纯校验规则。

## 5. 相关文档 / Related Docs

- runtime 是工具层：[Runtime-Is-Tool-Layer.md](./Runtime-Is-Tool-Layer.md)
- Artifact Registry 是缓存：[Artifact-Registry-Is-Cache.md](./Artifact-Registry-Is-Cache.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
- 图像生产治理：[../architecture/Image-Production-Governance.md](../architecture/Image-Production-Governance.md)
