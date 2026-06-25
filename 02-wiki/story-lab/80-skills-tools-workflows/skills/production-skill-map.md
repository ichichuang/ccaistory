# 生产技能映射 / Production Skill Map

> 机器可读映射：区分**叙事技法 skill**（runtime 注册）与**生产工作流 skill**（02-wiki 技能卡），并标注每个生产 skill 的 runtime 命令、落地层、人工/QA 门禁与状态。canonical 技能知识在各 `skills/*.md` 卡；本文件是导航索引。runtime/contracts 仅校验规则。

## 1. 叙事技法 skill（narrative-technique skills，runtime 注册）

来源：`runtime/skill_registry/skills.json`（= `runtime/contracts/skill_definitions.json`，共 12 个）。对应 `creator-techniques/技法模块/` 的抽象技法模块。这些是 runtime 可加载、可在 story_graph 节点上校验落地的技法，**不是**生产工作流 skill。

| skill_id | 技法 | 对应技法模块 |
|---|---|---|
| page_turn_hook | 翻页钩子 | 技法模块/翻页钩子技能.md |
| horror_escalation | 恐怖递进 | 技法模块/恐怖递进技能.md |
| everyday_anomaly | 日常异常化 | 技法模块/日常异常化技能.md |
| rule_horror | 规则怪谈 | 技法模块/规则怪谈技能.md |
| child_perspective_wonder | 儿童视角奇观 | 技法模块/儿童视角奇观技能.md |
| strange_tale_twist | 志怪转折 | 技法模块/志怪转折技能.md |
| fate_loop | 命运闭环 | 技法模块/命运闭环技能.md |
| misdirection_disproof | 误导与反证 | 技法模块/误导与反证技能.md |
| emotional_pull | 情绪牵引 | 技法模块/情绪牵引技能.md |
| world_compression | 世界感压缩 | 技法模块/世界感压缩技能.md |
| platform_completion_rate | 平台完读率 | 技法模块/平台完读率技能.md |
| child_safe_adaptation | 儿童化改编 | 技法模块/儿童化改编技能.md |

> 设计说明：生产工作流 skill 卡**未**加入 `skills.json`，因为该注册表 schema 仅描述叙事技法（节点级校验）。生产 skill 通过本映射 + 各卡 frontmatter（`runtime_commands` / `runtime_support_status`）machine-readable，状态为 `runtime` 或 `manual_only`。

## 2. 生产工作流 skill（production workflow skills，02-wiki 技能卡）

落在 `skills/*.md`。`support` = frontmatter `runtime_support_status`；`status` = frontmatter `status`。

| skill 卡 | 类别 skill_category | runtime_commands | support | status |
|---|---|---|---|---|
| 故事输入与版权改编技能 | story_intake | — | manual_only | active |
| 故事核心状态机技能 | system_maintenance | status, can-run | runtime | active |
| 故事极简化与最小可行故事评估技能 | story_analysis | classify-story, estimate-pages | runtime | active |
| 故事图扩展与连贯性审查技能 | story_rewrite | check-graph, analyze-graph | runtime | active |
| 故事钩子强化技能 | story_rewrite | analyze-graph, analyze-tension | runtime | active |
| 长故事页数合理性审查技能 | story_analysis | estimate-pages | runtime | active |
| Story Analyzer技能 | story_analysis | analyze-story, analyze-graph, … | runtime | active |
| Skill Runtime技能 | story_analysis | evaluate-node, repair-skill-graph, … | runtime | active |
| Skill Executor技能 | repair | score-skill-candidate, execute-skill-graph | runtime | active |
| 图文分镜与图读测试技能 | story_analysis | — | manual_only | active |
| 平台图文故事编排技能 | story_rewrite | — | manual_only | active |
| Character-Extraction-Skill | character_scene_extraction | — | manual_only | active |
| Scene-Extraction-Skill | character_scene_extraction | — | manual_only | active |
| 视觉设定技能 | visual_style | — | manual_only | active |
| 视觉资产本体技能 | image_execution_package | — | manual_only | active |
| PromptRecipe-Authoring-Skill | prompt_recipe | lint-prompt | runtime | active |
| ImageExecutionPackage-Creation-Skill | image_execution_package | compile-asset, lint-asset | runtime | active |
| 源插图Prompt编译技能 | prompt_compile | compile-asset | runtime | active |
| 源插图语义Lint技能 | semantic_lint | lint-asset, lint-prompt | runtime | active |
| 提示词巡检与任务清单技能 | prompt_compile | — | manual_only | active |
| 出图执行技能 | generation_handoff | — | manual_only | active |
| 图像执行遥测技能 | generation_run_backfill | validate-telemetry | runtime | active |
| Multimodal QA技能 | image_qa | generate-image-review-form, validate-image-review, merge-image-qa | runtime | active |
| 资产级细粒度验收技能 | image_qa | qa-asset | runtime | active |
| 资产验收与返修技能 | repair | — | manual_only | active |
| ReferenceAsset-Acceptance-Skill | reference_asset_acceptance | register-image-qa-artifact, artifact-validate, artifact-lineage | runtime | active |
| Rejected-Asset-Archive-Skill | archive | — | manual_only | active |
| Final Illustrated Story Package Assembly Skill | final_assembly | artifact-check-registry, artifact-lineage | runtime | active |
| 平台发布页合成技能 | publishing_readiness | — | manual_only | active |
| 人工完整阅读技能 | publishing_readiness | — | manual_only | active |
| Publishing-Readiness-Skill | publishing_readiness | status | runtime | active |
| 创作者技法蒸馏技能 | story_analysis | — | manual_only | active |
| Artifact Registry技能 | system_maintenance | artifact-register, artifact-validate, artifact-lineage | runtime | active |
| Pipeline Runner技能 | runtime_maintenance | pipeline-plan, pipeline-run, … | runtime | active |
| 机器事实源Contracts技能 | system_maintenance | validate-contracts, check-contract-drift | runtime | active |

## 3. 已 deprecated / needs_fix 的 skill（指向替代）

| skill 卡 | status | 替代/去向（deprecated_by） |
|---|---|---|
| 总控编排技能 | deprecated | Pipeline Runner技能 |
| 提示词生成技能 | deprecated | 源插图Prompt编译技能 / PromptRecipe-Authoring-Skill |
| 视觉候选失败复盘技能 | deprecated | 资产验收与返修技能 |
| 发布编排技能 | deprecated | 平台发布页合成技能 |
| 发布后数据回收技能 | needs_fix | 试点后再实现（off 关键插图路径） |

## 4. 映射到生产阶段（A–L 工作流）

intake→`A`；分析→`B`；角色/场景→`C`；视觉/技法→`D`；执行包→`E`；编译/Lint→`F`；出图交接→`G`；GenerationRun 回填→`H`；图像 QA/返修→`I`；参考资产接受→`J`；成品装配→`Final Illustrated Story Package Assembly Workflow`；发布就绪→`L`。
