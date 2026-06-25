---
type: codex_instruction
id: "运行Story Analyzer"
status: active
canonical: false
doctrine: obsidian-wiki-canonical
target_layer: "runtime-cache"
related_templates: []
related_workflows: []
human_gate: yes
runtime_role: "tool-layer runner: invoke runtime CLI (validate/compile/lint/qa/cache); never canonical, never external image generation"
owner: ichichuang
updated_at: 2026-06-25
---

> ✅ ACTIVE / 现行：遵循 Obsidian Story Production Wiki 4 层 canonical 卡片模型。Scope / allowed inputs / allowed outputs / stop-condition / forbidden-actions 见正文。canonical 知识落 02-wiki，操作记录落 50-agent-work，原始输入落 01-raw，被拒材料落 90-archive；runtime/contracts 仅定义校验规则，runtime 产物为派生缓存。
# 运行 Story Analyzer

## 单项诊断

```bash
python runtime/aistory.py classify-story --story-core <story_core_json_path>
python runtime/aistory.py estimate-pages --story-core <story_core_json_path>
python runtime/aistory.py analyze-clues --graph <story_graph_json_path>
python runtime/aistory.py analyze-tension --graph <story_graph_json_path>
python runtime/aistory.py analyze-stakes --graph <story_graph_json_path>
```

## 聚合诊断

```bash
python runtime/aistory.py analyze-story --story-core <story_core_json_path>
python runtime/aistory.py analyze-graph --graph <story_graph_json_path>
```

## 判定

- `passed = true`：可进入 Skill Executor 或下一门禁。
- `passed = false` 且 `next_action = repair_story_graph_before_skill_executor`：先修复 story_graph，不进入 Skill Executor。

## 禁止

- 不创建新故事。
- 不创建故事项目。
- 不生成图片。
- 不生成源插图试产任务清单。
- 不生成执行包。
- 不生成发布包。
- 不自动改写 `story_graph`。
