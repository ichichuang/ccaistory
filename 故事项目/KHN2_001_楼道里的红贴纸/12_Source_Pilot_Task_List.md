# 12 Source Pilot Task List

本文件为派生视图。
唯一事实源：故事核心.json。
如内容冲突，以故事核心.json 为准。

## 1. 生成对象

- project_id：KHN2_001
- story_id：故事0001
- 阶段：generate_source_pilot_task_list
- 输入：故事项目/KHN2_001_楼道里的红贴纸/10_Compiled_Prompts.json；故事项目/KHN2_001_楼道里的红贴纸/11_Semantic_Lint_Result.json

## 2. 总体结果

- task_list_status：ready_for_manual_external_generation
- total_task_count：11
- ready_task_count：1
- blocked_task_count：10
- 下一人工步骤：人工外部生成 R00，并在生成后补 telemetry 与 image review form。

## 3. 波次说明

| Wave | 规则 | Ready | Blocked |
|---|---|---|---|
| Wave 1 | No accepted reference dependency required; R00 only. | R00_KHN2_001_paper_mark_anchor | 无 |
| Wave 2 | Open only after R00 accepted. | 无 | R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor, P01_KHN2_001_platform_layout_sample |
| Wave 3 | Open only after R00, R01 and R02 accepted. | 无 | S01_KHN2_001_source_illustration, S02_KHN2_001_source_illustration, S03_KHN2_001_source_illustration, S04_KHN2_001_source_illustration, S05_KHN2_001_source_illustration, S06_KHN2_001_source_illustration, S07_KHN2_001_source_illustration |

## 4. ready task

- R00_KHN2_001_paper_mark_anchor
  - task_id：R00_KHN2_001_paper_mark_anchor_source_pilot_task
  - asset_type：R00_PAPER_MARK_ANCHOR
  - canvas_ratio：9:16
  - compiled_prompt_artifact_id：KHN2_001_compiled_prompt_R00_KHN2_001_paper_mark_anchor
  - semantic_lint_artifact_id：KHN2_001_semantic_lint_result_R00_KHN2_001_paper_mark_anchor

## 5. blocked task

| asset_id | wave | status | reference_dependencies |
|---|---|---|---|
| R01_KHN2_001_lin_xiaomu_anchor | Wave 2 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor |
| R02_KHN2_001_corridor_door_prop_anchor | Wave 2 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor |
| P01_KHN2_001_platform_layout_sample | Wave 2 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor |
| S01_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S02_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S03_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S04_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S05_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S06_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S07_KHN2_001_source_illustration | Wave 3 | blocked_by_reference_dependencies | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |

## 6. R00 手动外部生成提示词摘要

- 保留 compiled prompt：单张红箭头贴纸贴在清洁白色作业本纸面上，旁边只有短铅笔线索样本。
- 追加边界：禁止人物、火柴人、完整场景、道具集合、符号散点表、UI / 流程图、长正文、泛黄旧纸、脏纸、档案纸、羊皮纸。
- 必须满足：清洁白色作业本纸、一个明确视觉中心、图内中文仅 2-8 字短线索、可作为后续 reference asset。

## 7. R00 负面约束摘要

- Do not include: 人物
- 火柴人
- 完整场景
- 道具集合
- 符号散点表
- UI/流程图
- dirty scrap paper
- yellowed old paper
- long handwritten body
- 制作说明
- typed narration inside image
- 泛黄旧纸
- 脏纸
- 档案纸
- 羊皮纸
- full scene
- prop collection
- symbol scatter sheet
- UI
- flowchart
- long body text

## 8. R00 验收问题

- 是否没有人物？
- 是否没有火柴人？
- 是否不是完整场景？
- 是否不是道具集合？
- 是否不是符号散点表？
- 是否不是 UI / 流程图？
- 是否没有长正文？
- 是否是清洁白色作业本纸？
- 是否没有泛黄旧纸？
- 是否有明确视觉中心？
- 是否儿童短线索为 2-8 字？
- 是否可作为后续 reference asset？

## 9. 后续必须补 telemetry 与 image review form

- R00 外部人工生成后，必须记录 execution telemetry。
- 必须填写并校验 image review form。
- 必须经 merge_image_qa、qa_asset 与 Artifact Registry 血缘校验后，才可进入 accepted reference asset。

## 10. 明确未执行事项

- 未生成图片。
- 未调用 WebGPT。
- 未生成 WebGPT 执行包。
- 未记录 telemetry。
- 未运行 QA。
- 未生成发布包。
