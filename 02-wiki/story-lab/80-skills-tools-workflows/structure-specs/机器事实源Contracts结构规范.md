# 机器事实源 Contracts 结构规范

状态：活动

## 目的

`runtime/contracts/` 是**校验规则**（状态机、视觉资产、skill、质量门禁、pipeline action）的机器可读事实源；镜像这些规则的 Markdown 结构规范不作为 runtime **校验规则**来源（校验规则以 contracts 为准）。

但**生产知识**（故事、角色、场景、视觉风格、prompt recipe、执行包、生成记录、QA、返修）的长期 canonical 事实源是 `02-wiki/story-lab/` 的 Obsidian Markdown 卡；runtime 产物（compiled_prompt、semantic_lint、qa_result、Artifact Registry、runs）是派生缓存，持久生产决策必须回写 Markdown canonical 卡。

## 文件

- `runtime/contracts/state_machine.json`
- `runtime/contracts/visual_assets.json`
- `runtime/contracts/skill_definitions.json`
- `runtime/contracts/quality_gates.json`
- `runtime/contracts/pipeline_actions.json`

## 结构要求

- 所有 contracts 必须是可解析 JSON。
- `visual_assets.json` 必须定义 R00、R01、R02、P01、S 五类资产。
- R00 QA 必须为 14 项，并由 `asset_qa.py` 读取。
- R00 语义 Lint 禁止项必须由 `semantic_lint.py` 从 contract 读取。
- `skill_definitions.json` 必须与 `runtime/skill_registry/skills.json` 的 12 个 skill 保持一致。

## 优先级

规则冲突时以 `runtime/contracts/` 为准。新增或修改规则必须先改 contracts，再同步 Markdown 和测试。

