# 运行Skill Runtime检查

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：story_graph JSON

## 1. 任务定位
运行 Skill Runtime v0.2 检查，验证已选择 skill 是否真实作用到 story_graph 节点，并在失败时输出结构化 repair_plan。

## 2. 前置要求
- `runtime/skill_registry/skills.json` 可加载。
- story_graph JSON 已存在。
- story_graph.nodes 至少包含 node_id、page_role、applied_skills 和正文结构字段。

## 3. 命令
```bash
python runtime/aistory.py evaluate-node --node <node_json_path>
python runtime/aistory.py generate-skill-patch --node <node_json_path>
python runtime/aistory.py check-skill-graph --graph <story_graph_json_path>
python runtime/aistory.py repair-skill-graph --graph <story_graph_json_path> --dry-run
```

## 4. 禁止行为
- 不创建新故事。
- 不创建故事项目。
- 不生成图片。
- 不生成源插图试产任务清单实例。
- 不生成执行包。
- 不生成发布包。
- 不调用 WebGPT 或外部出图工具。

## 5. 通过条件
- valid node 的 evaluator 输出 `passed=true`。
- invalid node 的 evaluator 输出 `passed=false` 且包含 repair_targets。
- invalid graph 输出 repair_plan。
- valid graph 输出 `next_action=proceed_to_visual_manifest_or_next_gate`。
- repair dry-run 不修改输入文件。

## 6. 返回报告格式
- 是否完成：是/否
- evaluator 是否可用：是/否
- patch generator 是否可用：是/否
- patch applier 是否可用：是/否
- repair loop 是否可用：是/否
- invalid graph 是否能生成 repair_plan：是/否
- valid graph 是否能通过：是/否
- 残余风险：如无则写“无”
