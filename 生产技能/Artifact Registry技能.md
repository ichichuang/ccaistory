# Artifact Registry技能

## 目标

维护统一产物登记层，确保每个生产物都有稳定身份、hash、血缘和状态。

## 输入

- artifact JSON payload
- 依赖 artifact ID
- 父级 artifact ID
- registry 状态

## 输出

- artifact 注册结果
- artifact 查询结果
- lineage 校验结果
- registry 断链检查结果

## 操作边界

- 只写 `runtime/.artifacts/registry.json`。
- 不创建故事项目。
- 不生成图片。
- 不生成执行包。
- 不生成发布包。
- 不调用 WebGPT 或外部出图工具。

## 验收重点

- `artifact_id` 不可覆盖。
- `content_hash` 与 `source_hash` 必须存在并声明 `sha256`。
- accepted reference asset 必须能追溯到 compiled prompt、外部候选、执行遥测和资产 QA。
- `rejected` / `deprecated` asset 不得解锁下游 reference dependency。
