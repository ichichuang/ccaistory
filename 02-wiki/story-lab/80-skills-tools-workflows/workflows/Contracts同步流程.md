---
type: workflow_card
id: "Contracts同步流程"
title_zh: Contracts同步流程
title_en: Contracts Sync Flow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: system_maintenance
trigger: ""
input_layer: "runtime"
output_layer: "runtime"
required_cards: []
runtime_commands: ["validate-contracts", "check-contract-drift", "smoke-test"]
human_gates: no
qa_gates: no
stop_conditions: []
replacement_for: ""
deprecated_by: ""
---
# Contracts 同步流程

> 事实源声明（canonical doctrine）：本工作流的产物按 frontmatter 的 `input_layer`/`output_layer` 落地——原始输入 `01-raw`、canonical 卡 `02-wiki`、运行/编译/lint/QA/复核/返修记录 `50-agent-work`、被拒材料 `90-archive`、执行包 `02-wiki/story-lab/70-execution-packages`、接受的参考资产 `02-wiki/story-lab/reference-assets`。`runtime/contracts` 仅定义校验规则，runtime 产物为派生缓存。两窗口生产模型：WebGPT 指令窗规划/复核，WebGPTImage 生成窗仅按受控执行单出图。

## 原则

`runtime/contracts/` 是**校验规则**（状态机、视觉资产、skill、质量门禁、pipeline action）的机器可读事实源。runtime 优先从 contracts 读取这些规则；镜像规则的 Markdown 结构规范须与 contracts 保持一致——当**校验规则**的 Markdown 结构规范与 contracts 冲突时，以 contracts 为准。

但这只针对校验规则。生产知识（故事、角色、场景、视觉风格、prompt recipe、执行包、生成记录、QA、返修）的长期 canonical 事实源是 `02-wiki/story-lab/` 的 Obsidian Markdown 卡；runtime 产物（compiled_prompt、semantic_lint、qa_result、Artifact Registry、runs）是派生缓存。持久生产决策必须回写到对应 Markdown canonical 卡，不得只留在 runtime 缓存里。

## 修改流程

1. 修改对应 contract JSON。
2. 更新 runtime 读取逻辑或校验脚本。
3. 同步相关 Markdown 说明。
4. 更新或补充 smoke test。
5. 运行：

```bash
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
```

## 漂移处理

- Python 常量与 contracts 冲突：改 Python 读取 contracts。
- **校验规则**的 Markdown 结构规范与 contracts 冲突：改 Markdown 结构规范使其与 contracts 一致（校验规则以 contracts 为事实源）。
- `skills.json` 与 `skill_definitions.json` 冲突：先确认 contract，再同步 registry 或 contract。

