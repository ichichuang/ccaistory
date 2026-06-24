# runtime/ 是工具层 / Runtime Is a Tool Layer

> ARCHITECTURE / WORKFLOW INSTRUCTIONS ONLY. 本文件只定义边界与职责，不实例化任何真实资产。引用一律使用占位符（`<asset-id>`、`<package-id>`、EXAMPLE_VALUE、占位）。

## 1. 立场 / Position

`runtime/` 是一个 **校验器 / linter / 编译器 / QA 助手 / 缓存生产者（validator / linter / compiler / QA-helper / cache-producer）**，**不是规范资产管理系统（NOT the canonical asset management system）**。

规范生产知识（canonical production knowledge）位于 `02-wiki/` 的 Obsidian Markdown 卡片；runtime 只负责把这些知识 **验证、编译、检查、缓存** 为可机器消费的派生产物。

## 2. runtime 做什么 / What Runtime DOES

| 能力 / Capability | 说明 / Description | 输出性质 / Output |
| --- | --- | --- |
| `validate-contracts` | 校验 contracts 内的规则定义是否自洽 | 校验结果 |
| `check-contract-drift` | 检查 contracts 与实际使用是否漂移 | 漂移报告 |
| `smoke-test` | 对工具链做冒烟测试 | 测试结果 |
| `compile-asset` | 将卡片/配方编译为 `compiled_prompt` | 派生缓存 |
| `lint-asset` / `lint-prompt` | 语义 lint，产出 `semantic_lint` | 派生缓存 |
| `qa-asset` | 资产 QA，产出 `qa_result` | 派生缓存 |
| `validate-telemetry` | 校验生成遥测是否完整有效 | 校验结果 |
| 图像评审表单 / image review forms | 提供受控的图像评审表单结构 | 表单/记录 |
| 流水线试运行 / pipeline dry-run | 不触发外部工具的流程演练 | 演练结果 |
| Artifact Registry | 缓存 + 血缘/身份/哈希/状态助手 | 缓存（gitignored） |

所有上述输出（`compiled_prompt`、`semantic_lint`、`qa_result`、`runs` 等）都是 **派生产物 / 运行缓存（derived artifacts / run caches）**。

## 3. runtime 绝不拥有什么 / What Runtime MUST NOT Own

- **规范生产知识**：故事、世界观、角色、场景、视觉风格、提示配方、执行包、参考资产、QA 结论、修复记录的 **长期事实** —— 这些一律属于 `02-wiki/` 的 Markdown 卡片。
- **规范资产登记表**：Artifact Registry 只是缓存；规范登记是 `02-wiki` 中的参考资产卡片 + 执行包卡片集合（见 [Artifact-Registry-Is-Cache.md](./Artifact-Registry-Is-Cache.md)）。
- **持久生产决策**：任何“接受/拒绝/采用/退役”的最终决定都不能只存在于 runtime 缓存里。

## 4. 边界规则 / Boundary Rules

1. **contracts = 验证规则（VALIDATION RULES ONLY）**：状态机、视觉资产规则、技能规则、质量门、流水线动作。
2. **runtime 输出 = 派生缓存**：可被重新生成、可被清理，不作为事实来源。
3. **runtime 永不调用外部图像工具**：流程停在人工执行点（human execution point）。
4. **runtime 不持有规范知识**：它读取 `02-wiki`、写派生缓存，但规范事实回到 `02-wiki`。

## 5. 持久决策如何流回 Markdown / How Durable Decisions Flow Back

```
runtime 产出派生缓存 (compiled_prompt / semantic_lint / qa_result / registry 条目)
        │
        ▼
人工/Codex 评审 → 形成持久决策（接受/拒绝/采用/退役）
        │
        ▼
写回 02-wiki 规范卡片  (reference_asset / image_execution_package / ...)
        │
        ▼
runtime 缓存可随时重建，规范事实长存于 Markdown
```

规则：**任何要长期保留的生产决策都必须回填到对应的 `02-wiki` 规范卡片**。详见 [Markdown-Is-Canonical.md](./Markdown-Is-Canonical.md)。

## 6. 相关文档 / Related Docs

- Artifact Registry 是缓存：[Artifact-Registry-Is-Cache.md](./Artifact-Registry-Is-Cache.md)
- Markdown 是规范来源：[Markdown-Is-Canonical.md](./Markdown-Is-Canonical.md)
- 总体架构：[../architecture/AI+Story-Obsidian-Wiki-Architecture.md](../architecture/AI+Story-Obsidian-Wiki-Architecture.md)
