# Artifact Registry 是缓存 / Artifact Registry Is a Cache

> ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 本文件只定义边界，不实例化任何真实资产。引用一律使用占位符（`<asset-id>`、`<hash>`、EXAMPLE_VALUE、占位）。

## 1. 立场 / Position

**Artifact Registry 是 runtime 的缓存 + 血缘/身份/哈希/状态助手（cache + lineage / identity / hash / status helper）**，写在 `runtime/.artifacts/` 下（**gitignored**），**不是规范资产登记表（NOT the canonical asset registry）**。

资产的 **规范登记表** 是 `02-wiki/` 中的 **参考资产卡片（reference-asset cards）+ 执行包卡片（execution-package cards）** 的集合。

## 2. Registry 持有什么 / What the Registry Holds

| 字段 / Field | 用途 / Use | 性质 / Nature |
| --- | --- | --- |
| `identity` / `id` | 工件身份标识 | 缓存便利 |
| `hash` | 内容哈希，用于去重/校验 | 缓存便利 |
| `lineage` | 工件血缘链（谁由谁派生） | 追溯便利 |
| `status` | 缓存内的临时状态 | 缓存便利 |
| 指向原料/运行的路径 | 指回 `01-raw/` 与 `50-agent-work/` | 追溯便利 |

Registry 中的 `lineage` 是 **可追溯性的便利（a convenience for traceability）**，**持久记录仍是 Markdown 卡片（the durable record is the Markdown card）**。

## 3. 什么可以只活在缓存里 / What MAY Live Only in the Cache

- 内容哈希、临时身份、去重索引。
- 中间血缘链、运行期状态、可重算的派生结果。
- 仅用于本地工具链加速的临时条目。

> 这些条目可被删除并由 runtime 重新生成，不影响规范事实。

## 4. 什么必须回填到 Markdown / What MUST Be Backfilled to Markdown

- **被接受的资产**：必须在 `02-wiki/story-lab/reference-assets/` 写规范参考资产卡片。
- **执行包定稿**：必须在 `02-wiki/story-lab/70-execution-packages/` 以独立 `.md` 留存。
- **任何持久生产决策**：接受/拒绝/采用/退役及其依据（QA 证据、来源、用途约束）。
- **可被人类长期检索/维护的血缘结论**：写入卡片的 `related_assets` 与 `source_paths`。

## 5. 规则 / Rules

1. **缓存可丢失（cache is disposable）**：删除 `runtime/.artifacts/` 不应丢失任何规范事实。
2. **规范事实在 Markdown**：Registry 是镜像/索引，不是真相源。
3. **回填优先（backfill first）**：任何持久决策先写 `02-wiki` 卡片，再让 Registry 作为缓存反映。
4. **不依赖 gitignored 内容作为真相**：因为 `runtime/.artifacts/` 不入库。

## 6. 相关文档 / Related Docs

- runtime 是工具层：[Runtime-Is-Tool-Layer.md](./Runtime-Is-Tool-Layer.md)
- Markdown 是规范来源：[Markdown-Is-Canonical.md](./Markdown-Is-Canonical.md)
- 资产模型：[../architecture/Canonical-Asset-Model.md](../architecture/Canonical-Asset-Model.md)
