# 校验机器事实源 Contracts

## 目标

校验 `runtime/contracts/` 是否仍是**校验规则**（状态机、视觉资产、skill、质量门禁、pipeline action）的机器可读事实源，并检查 runtime、镜像这些规则的 Markdown 结构规范与 skill registry 是否漂移。

> 边界：contracts 只是**校验规则**的事实源。故事、角色、场景、视觉风格、prompt recipe、执行包、生成记录、QA、返修等**生产知识的长期 canonical 事实源是 `02-wiki/story-lab/` 的 Obsidian Markdown 卡**。runtime 产物（compiled_prompt、semantic_lint、qa_result、Artifact Registry、runs）是派生缓存；任何持久生产决策都必须回写到对应的 Markdown canonical 卡。

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

