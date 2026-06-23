# nvwa技能接入流程

状态：活动

## 目标

把本地 `nvwa.skill` 或 `huashu-nuwa` 能力作为技法蒸馏入口接入，不复制、不覆盖原技能。

## 流程

1. 搜索本地 `nvwa.skill`、`nuwa`、`女娲`、`huashu-nuwa`。
2. 找到时只读取接口说明、目录结构和可接入方式。
3. 找不到独立 `nvwa.skill` 时登记待补路径。
4. 使用 `创作者技法库/nvwa接入/nvwa技能适配规范.md` 转换输出。
5. 蒸馏结果必须进入 `source_summary`、`observed_pattern`、`abstract_principle`、`usable_skill`。
6. 最终只写入 `story_graph` 技法字段。

## 禁止

- 不复制原 skill 正文。
- 不覆盖原 skill。
- 不生成作者风格 prompt。
- 不生成图片、任务清单或发布材料。

