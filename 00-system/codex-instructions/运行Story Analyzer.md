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
