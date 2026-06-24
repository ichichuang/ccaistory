# Skill Executor验收清单

状态：活动

## 必查项

- [ ] `runtime/skill_executor/` 存在。
- [ ] candidate generator 可生成结构化 candidates。
- [ ] candidate scorer 可输出 8 项评分。
- [ ] invalid author style candidate 被阻断。
- [ ] invalid empty scare candidate 被阻断。
- [ ] conflict resolver 输出 resolution_plan。
- [ ] invalid node 生成 proposed_changes。
- [ ] valid node 不生成无意义 proposed_changes。
- [ ] invalid graph 生成 proposed_changes。
- [ ] valid graph 通过。
- [ ] 所有 proposed_changes 标记 `human_approval_required=true`。
- [ ] Pipeline Runner 可规划 Skill Executor 阶段。
- [ ] 未批准 proposed_changes 不得进入下一门禁。
- [ ] smoke-test 通过。
- [ ] validate-contracts 通过。
- [ ] check-contract-drift 通过。
- [ ] 未创建故事项目。
- [ ] 未生成图片。
- [ ] 未生成执行包。
- [ ] 未生成发布包。

## 硬失败

- [ ] Skill Executor 直接写正式 story_graph 字段。
- [ ] Candidate Generator 调用外部 LLM。
- [ ] Candidate Scorer 放行作者风格指令。
- [ ] Proposed Changes 缺人工批准标记。
- [ ] Pipeline Runner 跳过人工批准门禁。
