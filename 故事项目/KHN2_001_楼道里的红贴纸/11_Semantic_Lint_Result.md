# 11 Semantic Lint Result

本文件为派生视图。
唯一事实源：故事核心.json。
如内容冲突，以故事核心.json 为准。

## 1. Lint 对象

- 项目：KHN2_001
- 故事：故事0001
- 输入：故事项目/KHN2_001_楼道里的红贴纸/10_Compiled_Prompts.json
- Prompt 数量：11

## 2. 总体结果

- lint_status：pass
- passed_count：11
- failed_count：0
- next_allowed_action_if_pass：generate_source_pilot_task_list
- next_allowed_action_if_fail：repair_compiled_prompts_or_visual_asset_specs

## 3. 11 个资产逐项结果

| asset_id | asset_type | lint_status | failed_rules | semantic_lint_artifact_id |
|---|---|---|---|---|
| R00_KHN2_001_paper_mark_anchor | R00_PAPER_MARK_ANCHOR | pass | - | KHN2_001_semantic_lint_result_R00_KHN2_001_paper_mark_anchor |
| R01_KHN2_001_lin_xiaomu_anchor | R01_CHARACTER_ANCHOR | pass | - | KHN2_001_semantic_lint_result_R01_KHN2_001_lin_xiaomu_anchor |
| R02_KHN2_001_corridor_door_prop_anchor | R02_SCENE_PROP_ANCHOR | pass | - | KHN2_001_semantic_lint_result_R02_KHN2_001_corridor_door_prop_anchor |
| P01_KHN2_001_platform_layout_sample | P01_PLATFORM_LAYOUT_SAMPLE | pass | - | KHN2_001_semantic_lint_result_P01_KHN2_001_platform_layout_sample |
| S01_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S01_KHN2_001_source_illustration |
| S02_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S02_KHN2_001_source_illustration |
| S03_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S03_KHN2_001_source_illustration |
| S04_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S04_KHN2_001_source_illustration |
| S05_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S05_KHN2_001_source_illustration |
| S06_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S06_KHN2_001_source_illustration |
| S07_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | pass | - | KHN2_001_semantic_lint_result_S07_KHN2_001_source_illustration |

## 4. hard failure 汇总

- 无。

## 5. risky terms 汇总

- 无。

## 6. missing fields 汇总

- 无。

## 7. asset_scope_conflicts 汇总

- 无。

## 8. repair_suggestions 汇总

- 无需修复。

## 9. Artifact Registry 登记摘要

- 登记类型：semantic_lint_result
- 登记数量：11
- 每条 semantic_lint_result 均依赖对应 compiled_prompt artifact。
- KHN2_001_semantic_lint_result_R00_KHN2_001_paper_mark_anchor
- KHN2_001_semantic_lint_result_R01_KHN2_001_lin_xiaomu_anchor
- KHN2_001_semantic_lint_result_R02_KHN2_001_corridor_door_prop_anchor
- KHN2_001_semantic_lint_result_P01_KHN2_001_platform_layout_sample
- KHN2_001_semantic_lint_result_S01_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S02_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S03_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S04_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S05_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S06_KHN2_001_source_illustration
- KHN2_001_semantic_lint_result_S07_KHN2_001_source_illustration

## 10. 下一步建议

运行 `python runtime/aistory.py can-run --project '故事项目/KHN2_001_楼道里的红贴纸' --action generate_source_pilot_task_list`。

## 11. 禁止输出声明

- 未生成图片。
- 未调用 WebGPT。
- 未生成 source pilot task list。
- 未生成执行包。
- 未生成发布包。
