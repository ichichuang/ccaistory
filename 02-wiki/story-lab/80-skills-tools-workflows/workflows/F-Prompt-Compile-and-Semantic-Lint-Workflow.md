---
type: workflow_card
id: "F-Prompt-Compile-and-Semantic-Lint-Workflow"
title_zh: F 提示词编译与语义 Lint 工作流
title_en: F. Prompt Compile and Semantic Lint Workflow
status: active
project_id: ""
related_assets: []
source_paths: []
tags: [workflow, story-lab, prompt-compile, semantic-lint]
created_at: 2026-06-25
updated_at: 2026-06-25
owner: ichichuang
version: v1
canonical: true
workflow_category: prompt_compile
trigger: "ImageExecutionPackage 已绑定本体（E 进行中）"
input_layer: "02-wiki"
output_layer: "50-agent-work/story-lab/compiled-prompts, 50-agent-work/story-lab/semantic-lint-results"
required_cards: ["ImageExecutionPackage"]
runtime_commands: ["compile-asset", "lint-asset", "lint-prompt"]
human_gates: no
qa_gates: yes
stop_conditions: ["缺 paper_policy/style_policy", "lint hard-fail", "无 compiled_prompt 不得出图"]
replacement_for: ""
deprecated_by: ""
---
# F 提示词编译与语义 Lint 工作流 / Prompt Compile and Semantic Lint Workflow

> Doctrine：编译产物与 lint 结果是操作记录，落 `50-agent-work`；runtime 的 compile/lint 缓存是派生缓存。canonical 决策（如锁定某 compiled_prompt 版本）回填执行包卡。

## Workflow Purpose / 工作流目的
把视觉资产本体编译为 compiled_prompt 并做语义 Lint，作为出图前的硬门禁。

## Trigger / 触发
E 工作流中执行包绑定本体后、`status: ready` 前。

## Inputs / 输入
- ImageExecutionPackage 卡 + 视觉资产本体（asset ontology）。

## Steps / 步骤
1. 运行 `compile-asset` 把本体编译为 compiled_prompt；写入 `50-agent-work/story-lab/compiled-prompts/`。
2. 运行 `lint-asset` / `lint-prompt` 做语义 Lint；写入 `50-agent-work/story-lab/semantic-lint-results/`。
3. hard-fail（R00 含人物/火柴人/完整场景/道具集合/符号散点表、P01 非 9:16、缺 visual_center/paper_policy/style_policy、作者风格指令）→ 阻断并返修。
4. 在执行包卡登记 `recipe_hash` 比对结果（prompt 配方漂移检测）。
5. p02 及之后追加 Series Continuity + Page Hook 语义 Lint：
   - 缺 `previous_page_reference`、前页/当前页场景摘要、场景差量、允许递进、禁止断裂、`page_hook_question`、`hook_visual_target`、`hook_annotation_guidance` → block。
   - 当前页与前页过于复制、或 `scene_delta_from_previous_page` 为空 → block。
   - 环境强度突然跳太远（例如过早进入高密度、高黑暗、高雾、高灯光/基础设施、后页怪异强度）→ block。
   - 新增未在包内说明的道具、人物、建筑、车辆、灯、标牌等基础设施 → block。
   - hook 缺失、过泛、只描述 mood 而没有具体视觉问题 → block 或 warn；若无法形成翻页问题则 block。
   - 红笔标注不指向本页具体不确定性 → block。
   - R00 被当作故事内容、地点、道具或构图来源，而不是视觉/角色/比例连续性来源 → block。
6. p02 专项回归：未来 lint 应拦截“过早深密林”“灯/基础设施突然过多”“黑暗强度跳太大”“hook 只有泛泛情绪标签”等问题；这些是 pilot-001 示例，不是全局风格公式。
7. 通过后回到 E 把执行包 `status: ready`。

## Outputs / 输出
- `50-agent-work/story-lab/compiled-prompts/<id>.json`、`50-agent-work/story-lab/semantic-lint-results/<id>.json`。

## Runtime Commands / Runtime 命令
- `compile-asset`、`lint-asset`、`lint-prompt`。

## Human Approval Gates / 人工批准门禁
- 无（自动编译/lint；人工在 E 的执行包复核）。

## QA Gates / QA 门禁
- 语义 Lint 必须 pass；**没有 compiled_prompt 不得出图**。

## Stop Conditions / 停止条件
- 缺 `paper_policy`/`style_policy`、p02+ 缺连续性/钩子字段、lint hard-fail、或 recipe 漂移 → 阻断。

## Related Skills / 关联技能
- `skills/源插图Prompt编译技能.md`、`skills/源插图语义Lint技能.md`、`skills/提示词巡检与任务清单技能.md`
- 下游：`workflows/G-WebGPTImage-Manual-Generation-Handoff-Workflow.md`
