# Skill Runtime验收清单

状态：活动

## 必查项

- [ ] `runtime/skill_runtime/` 存在。
- [ ] evaluator 可评估单个 node。
- [ ] patch generator 可生成结构化 patch。
- [ ] patch applier 支持 dry-run。
- [ ] repair loop 可遍历 story_graph.nodes。
- [ ] invalid graph 能生成 repair_plan。
- [ ] valid graph 能通过 repair_loop。
- [ ] 新增 CLI 命令输出 JSON。
- [ ] 12 个 skill 可加载。
- [ ] JSON fixture 可解析。
- [ ] smoke-test 通过。
- [ ] 未创建故事项目。
- [ ] 未生成图片。
- [ ] 未生成执行包。
- [ ] 未生成发布包。

## 硬失败

- [ ] Skill Runtime 直接改写正式正文。
- [ ] Patch Generator 生成文学正文而不是结构化修复指令。
- [ ] invalid graph 无 repair_plan。
- [ ] valid graph 被错误阻断。
- [ ] dry-run 修改输入文件。
- [ ] 新增故事、图片、执行包或发布包。
