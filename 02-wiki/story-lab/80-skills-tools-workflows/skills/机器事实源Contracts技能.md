# 机器事实源 Contracts 技能

状态：活动

## 技能目的

维护 `runtime/contracts/`，保证状态机、视觉资产、skill、质量门禁和 pipeline action 等**校验规则**只有一个机器可读事实源（contracts）。生产知识的 canonical 事实源是 `02-wiki/story-lab/` 的 Obsidian Markdown 卡，runtime 产物为派生缓存。

## 输入

- `runtime/contracts/*.json`
- `runtime/skill_registry/skills.json`
- runtime 校验脚本
- 需要同步的 Markdown 结构规范（镜像校验规则）

## 输出

- 更新后的 contracts
- 通过的 `validate-contracts`
- 通过的 `check-contract-drift`
- 同步后的说明文档和测试

## 禁止行为

- 不创建故事项目。
- 不生成图片。
- 不生成执行包或发布包。
- 不把 Markdown 当作 runtime 规则事实源。
- 不在 `skill_definitions.json` 中加入具体历史故事名或正向作者风格指令。

## 门禁

- contracts JSON 全部可解析。
- R00 QA 数量为 14。
- R00 Lint 和 QA 均从 `visual_assets.json` 读取。
- skill contract 与 `skills.json` 数量、`skill_id`、`input_fields`、`output_fields`、`hard_failures`、`repair_actions` 一致。

