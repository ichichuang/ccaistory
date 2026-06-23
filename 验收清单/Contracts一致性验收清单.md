# Contracts 一致性验收清单

状态：活动

## 必查项

- [ ] `runtime/contracts/` 存在。
- [ ] 5 个 contract JSON 全部可解析。
- [ ] `visual_assets.json` 定义 R00、R01、R02、P01、S。
- [ ] R00 QA 为 14 项。
- [ ] R00 QA 来自 `visual_assets.json`。
- [ ] R00 语义 Lint 禁止项来自 `visual_assets.json`。
- [ ] `skill_definitions.json` 与 `skills.json` 的 12 个 skill 一致。
- [ ] `validate-contracts` 通过。
- [ ] `check-contract-drift` 通过。
- [ ] `smoke-test` 通过。
- [ ] 没有创建故事项目、图片、执行包或发布包。

## 硬失败

- contracts 缺失或 JSON 不可解析。
- R00 QA 数量不是 14。
- runtime 静默降级到 Markdown 或 Python 硬编码规则。
- skill contract 与 registry 不一致。

