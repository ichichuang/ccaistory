# 校验机器事实源 Contracts

## 目标

校验 `runtime/contracts/` 是否仍是机器事实源，并检查 runtime、Markdown 说明层和 skill registry 是否漂移。

## 命令

```bash
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
python -m compileall -q runtime
```

## 验收

- contracts JSON 全部可解析。
- R00 QA 为 14 项。
- semantic_lint 从 contract 读取 R00 禁止项。
- asset_qa 从 contract 读取 R00 QA。
- skill_definitions 与 skills.json 一致。
- 不创建故事项目、图片、执行包或发布包。

