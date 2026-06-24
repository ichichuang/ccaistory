# Artifact Registry产物登记流程

1. 生成或接收 artifact payload。
2. 计算内容 hash 或 source hash。
3. 校验 artifact schema。
4. 校验父级与依赖 artifact 是否存在。
5. 校验类型和状态规则。
6. 写入 `runtime/.artifacts/registry.json`。
7. 需要 accepted 前，运行 lineage 校验。

## accepted 前置

accepted reference asset 必须同时具备：

- `external_generation_candidate`
- `execution_telemetry`
- `asset_qa_result`
- `qa_passed`
- 可追溯到 `compiled_prompt`

缺 telemetry 或 QA 时必须阻断 accepted。

## 下游引用

- 只有 `accepted` 的 reference asset 可作为 reference dependency。
- `rejected` asset 不解锁下游资产。
- `deprecated` asset 不得作为 reference asset。
