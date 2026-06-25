---
type: workflow_card
id: "B-Story-Analysis-and-Canonical-Card-Workflow"
title_zh: B 故事分析与规范卡工作流
title_en: B. Story Analysis and Canonical Card Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, analysis]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: story_analysis
trigger: "StoryProject 卡已创建"
input_layer: "02-wiki, 01-raw"
output_layer: "02-wiki, 50-agent-work"
required_cards: ["StoryProject"]
runtime_commands: ["analyze-story", "analyze-graph", "classify-story", "estimate-pages", "check-graph"]
human_gates: yes
qa_gates: no
stop_conditions: ["story_analyzer 高风险", "页数/连贯性不合理"]
replacement_for: ""
deprecated_by: ""
---
# B 故事分析与规范卡工作流 / Story Analysis and Canonical Card Workflow

> Doctrine：canonical 决策回填 `02-wiki` 卡；诊断/分析的 JSON 是 `50-agent-work` 或 runtime 派生缓存，不是事实源。

## Workflow Purpose / 工作流目的
对已接入的故事做内容感知分析，沉淀故事核心、故事图、技法计划，并驱动下游 C/D 抽取角色/场景/视觉/技法卡。

## Trigger / 触发
`02-wiki/story-lab/10-projects/<project-id>.md` 存在。

## Inputs / 输入
- StoryProject 卡 + `01-raw` 原始输入。

## Steps / 步骤
1. 运行 `analyze-story` / `classify-story` 诊断故事类型、核心冲突、结局类型。
2. 运行 `estimate-pages` 评估页数合理性（长故事进入 `skills/长故事页数合理性审查技能.md`）。
3. 构建/审查 story_graph，运行 `analyze-graph` / `check-graph`（钩子、连贯性、线索回收、张力）。
4. 把诊断结果（recommended_skill_plan / repair_priority）写入 `50-agent-work/story-lab/runs/` 派生记录。
5. 把故事核心/故事图的持久决策回填 StoryProject 卡（Story Core / Production Status 区）。
6. 触发 C（角色/场景抽取）与 D（视觉/技法）。

## Outputs / 输出
- StoryProject 卡的 Story Core / Production Status 区更新（`02-wiki`）。
- 诊断派生记录（`50-agent-work/story-lab/runs/`）。

## Runtime Commands / Runtime 命令
- `analyze-story`、`classify-story`、`estimate-pages`、`analyze-graph`、`check-graph`。

## Human Approval Gates / 人工批准门禁
- 故事核心与页数合理性结论确认。

## QA Gates / QA 门禁
- story_analyzer 高风险时停在 `story_analyzer_gate`，返修后再继续。

## Stop Conditions / 停止条件
- 高风险诊断或页数/连贯性不合理 → 返修 story_graph。

## Related Skills / 关联技能
- `skills/Story Analyzer技能.md`、`skills/故事图扩展与连贯性审查技能.md`、`skills/故事钩子强化技能.md`、`skills/长故事页数合理性审查技能.md`、`skills/故事极简化与最小可行故事评估技能.md`
