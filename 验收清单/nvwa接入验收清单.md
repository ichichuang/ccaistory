# nvwa接入验收清单

状态：活动

## 必检项

- [ ] 已登记 `nvwa.skill` 或 `huashu-nuwa` 路径。
- [ ] 未复制原技能正文。
- [ ] 输出为适配层字段。
- [ ] 已填写 `forbidden_copy_boundary`。
- [ ] 已填写 `story_graph_fields_affected`。
- [ ] 未生成图片。
- [ ] 未生成 prompt 任务清单。
- [ ] 未生成发布材料。

## 硬失败

- 覆盖或破坏原 `nvwa.skill`。
- 把蒸馏结果直接转为作者风格 prompt。
- 输出无法作用于 `story_graph`。
- 保存完整访谈、完整作品或付费内容全文。

