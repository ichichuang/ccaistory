# Skill Runtime技能

状态：活动  
生产体系：平台图文故事主线生产体系  
唯一事实源：story_graph node

## 1. 技能目的
检查创作者技法库的 skill 是否真实落到 story_graph 节点上，并把未通过位置转换为结构化修复建议。

## 2. 输入
- story_graph node JSON
- story_graph JSON
- `runtime/skill_registry/skills.json`

## 3. 输出
- node evaluation
- structured skill patch
- graph_repair_plan
- next_action

## 4. 职责划分
- Skill Orchestrator 负责选择 skill。
- Skill Runtime 负责评估 skill 是否真正作用到节点。
- Patch Generator 负责生成结构化修复建议。
- Patch Applier 默认只写入建议字段，不直接改写正文。
- Repair Loop 负责决定是否进入下一门禁。

## 5. 允许行为
- 读取 node 或 story_graph JSON。
- 读取 `skills.json` 的 validation_questions、hard_failures、repair_actions。
- 输出 JSON 评估、patch 和 repair_plan。
- dry-run 方式模拟 patch 写入。

## 6. 禁止行为
- 不创建故事项目。
- 不创建新故事。
- 不生成图片。
- 不生成源插图试产任务清单实例。
- 不生成执行包或发布包。
- 不调用 WebGPT 或外部出图工具。
- 不伪造正式故事正文。

## 7. 门禁
- invalid graph 必须生成 repair_plan。
- valid graph 必须通过 repair_loop。
- patch applier dry-run 不得修改输入文件。
- JSON fixture、schema 和 skill registry 必须可解析。
- 12 个 skill 必须可加载。

## 8. 下游入口
通过后进入视觉资产本体或下一门禁：
`proceed_to_visual_manifest_or_next_gate`

未通过时进入受控修复：
`repair_story_graph_with_skill_patches`
