---
type: acceptance_checklist
id: "源插图语义Lint验收清单"
status: active
stage: semantic_lint
target_layer: "50-agent-work/story-lab/semantic-lint-results"
related_runtime_commands: ["lint-asset", "lint-prompt"]
related_templates: ["ImageExecutionPackage", "PromptRecipe"]
owner: ichichuang
updated_at: 2026-06-25
---
# 源插图语义 Lint 验收清单 / Semantic Lint Acceptance Checklist

## Purpose / 目的
对 compiled_prompt 做出图前静态语义 Lint，拦截缺项、矛盾、禁项、作用域冲突与依赖缺失。

## Required Inputs / 必需输入
- compiled_prompt（`50-agent-work/story-lab/compiled-prompts/`）。
- 执行包卡的 `forbidden_content`、`negative_constraints`、`required_reference_assets`、`asset_type`。
- p02 及之后：`previous_page_reference`、前页/当前页场景摘要、`continuity_from_previous_page`、`scene_delta_from_previous_page`、`allowed_progression_delta`、`forbidden_continuity_breaks`、`page_hook_question`、`hook_visual_target`、`hook_annotation_guidance`、`escalation_level`。

## Pass Criteria / 通过标准
- [ ] 必需字段齐全：`visual_center`、`density_range`、`composition_mode`、`paper_policy`、`style_policy`。
- [ ] 资产作用域正确（R00=纸张笔触；R01=角色；R02=场景/道具；S=源插图；P01=平台版式）。
- [ ] 正向 prompt 不含被禁内容；`reference_dependencies` 均存在且为 accepted。
- [ ] p02 及之后通过 R00 视觉连续性、前页场景连续性、受控递进和页面 hook 检查。
- [ ] 对存在易误读线索的页面，`symbol_semantics_target` 与 `symbol_misread_to_avoid` 成组存在，且能阻断错误物体类别（例如 eyes vs lamps）。
- [ ] 返修类页面有 `repair_guardrails`、`progression_budget_from_previous_page`、`overcorrection_guardrail`、`composition_priority_order`。

## Fail Criteria（硬失败 / Hard Failures）
- [ ] R00 含人物 / 火柴人 / 完整场景 / 道具集合 / 符号散点表。
- [ ] R01 携带完整剧情 / 主线事件；R02 携带完整角色系统。
- [ ] S 页含长手写正文；P01 非 9:16。
- [ ] 缺 `visual_center`；使用作者姓名作为风格指令。
- [ ] p02+ 缺前页引用 / 场景差量 / 允许递进 / 禁止断裂 / 本页钩子 / 标注目标。
- [ ] 当前页过早跳到后页强度，或突然新增未说明的道具、人物、建筑、车辆、灯、标牌等基础设施。
- [ ] hook 只描述气氛而没有具体视觉问题；红笔标注不指向本页不确定性。
- [ ] 线索语义含混且缺误读防护；修复一个钩子问题却制造更强前页连续性断裂。
- [ ] hook 过早成为整页主视觉，压过上一页场景连续性和叙事节奏。

## Blocking Conditions / 阻断条件
- 任一硬失败 → `fail`，阻断出图。
- 无 compiled_prompt → 阻断（没有 compiled_prompt 不得出图）。

## Required Evidence / 必需证据
- `50-agent-work/story-lab/semantic-lint-results/<id>.json`（`lint_result`、`failed_rules`、`risky_terms`、`repair_suggestions`）。

## Output Decision / 输出决策
- `pass` → 进入出图任务清单 / G 工作流；`fail` → 返修 compiled_prompt（回 F/E）。

## Target Layer / 落地层
- `50-agent-work/story-lab/semantic-lint-results/`（操作记录；canonical 规则在 `runtime/contracts/visual_assets.json`）。

## Related Templates & Runtime / 关联模板与命令
- 模板：`ImageExecutionPackage`、`PromptRecipe`。命令：`lint-asset`、`lint-prompt`。
