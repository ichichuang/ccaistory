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

## 7. 待补校验器（Missing Validators — scope only / 仅定义范围，暂不实现）

当前 `runtime` 行为合规（只写自身缓存、阻断生成、人工门禁），但**尚无任何 runtime 校验强制执行新的 4 层 / Markdown-canonical doctrine**。以下校验器尚缺，先明确范围以便后续安全实现（本次 P0 不改动 runtime 逻辑、不削弱测试）：

| 校验器 / Validator | 应检查 / Should check | 当前状态 |
| --- | --- | --- |
| `validate-vault` | canonical 卡是否齐全、是否落在正确 02-wiki 子目录 | 缺（`validate` 仅校验 runtime/schemas + fixtures JSON） |
| wrong-layer write detector | 是否有产物写到错误的层（如把操作记录写进 02-wiki，或把 canonical 写进 50-agent-work） | 缺 |
| card ↔ runtime-cache reconciliation | runtime 缓存（compiled_prompt/qa/registry）是否与 02-wiki 卡一致 | 缺 |
| StoryProject asset-count consistency | `accepted_asset_count` 是否与实际 accepted ReferenceAsset 数一致；`>= required_asset_count` 才能成品 ready | 缺 |
| required GenerationRun before acceptance | 接受 ReferenceAsset 前必须存在对应 GenerationRun | 部分（artifact 层有，目录层无） |
| required image-review-form before accepted | 接受前必须有人工图像复核表单 | 部分（Multimodal QA 校验，但无目录级强制） |
| prompt recipe drift check | compiled_prompt 与登记的 `recipe_hash` 是否漂移 | 缺（hash 已存，未主动比对） |
| reference asset drift check | 参考资产内容与其 hash 是否漂移 | 缺（hash 已存，未主动比对） |
| story fact drift check | runtime story_core/story_graph JSON 是否与 02-wiki 故事卡一致 | 缺（无卡↔JSON 对账） |

> 另：现有 `runtime/tests/test_runtime_smoke.py` 的"does-not-generate"守卫仍指向已删除的旧根目录（`故事项目`/`资产库`/`执行包`/`发布包`），因此当前**空跑通过**。后续应把这些守卫改指向新 4 层（断言 runtime 从不写入 `02-wiki`/`01-raw`/`50-agent-work`/`90-archive`，仅写自身缓存），并新增 4 层 doctrine 的正向测试。本次不改动以免削弱测试。
