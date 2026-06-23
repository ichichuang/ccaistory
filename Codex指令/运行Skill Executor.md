# 运行Skill Executor

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：story_graph JSON

## 1. 任务定位
运行 Skill Executor，基于 Skill Runtime 的检查结果生成候选改写、评分、冲突解决和 proposed_changes。

## 2. 前置要求
- `runtime/aistory.py` 存在。
- `runtime/skill_executor/` 存在。
- `runtime/skill_registry/skills.json` 可加载。
- `runtime/contracts/` 可加载。
- story_graph JSON 或 node JSON 已存在。

## 3. 命令
```bash
python runtime/aistory.py execute-skill-node --node <node_json_path>
python runtime/aistory.py execute-skill-graph --graph <story_graph_json_path>
python runtime/aistory.py score-skill-candidate --candidate <candidate_json_path>
python runtime/aistory.py resolve-skill-conflicts --candidates <candidates_json_path>
```

## 4. 禁止行为
- 不创建新故事。
- 不创建故事项目。
- 不生成图片。
- 不生成源插图试产任务清单实例。
- 不生成执行包。
- 不生成发布包。
- 不调用 WebGPT 或外部出图工具。
- 不直接改写正式 story_graph 字段。

## 5. 通过条件
- invalid node 输出 `proposed_changes`。
- valid node 不输出无意义 `proposed_changes`。
- invalid candidate 被阻断。
- conflict resolver 输出 `resolution_plan`。
- `proposed_changes` 全部要求人工批准。
- Pipeline Runner 规划 `review_skill_executor_proposed_changes` 为人工批准阶段。
