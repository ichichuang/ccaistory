# 源插图 Prompt 编译结构规范

## 目的
Prompt 编译器把视觉资产本体转换为外部出图提示词。禁止直接从视觉清单拼接长 prompt。

## 输入字段
asset_id、asset_type、asset_scope、story_context、allowed_content、forbidden_content、visual_center、density_range、composition_mode、text_policy、paper_policy、style_policy、reference_dependencies、acceptance_questions、repair_policy。

## 输出字段
compiled_prompt、prompt_sections、positive_constraints、negative_constraints、asset_specific_acceptance_criteria、semantic_lint_result。

## 固定段落
ASSET METADATA；ASSET PURPOSE；OUTPUT TYPE AND CANVAS；VISUAL CENTER；COMPOSITION AND DENSITY；ALLOWED CONTENT；FORBIDDEN CONTENT；TEXT POLICY；PAPER AND MATERIAL POLICY；STYLE POLICY；REFERENCE DEPENDENCIES；NEGATIVE CONSTRAINTS；ACCEPTANCE CRITERIA。

## 编译前硬阻断
asset_type 与 asset_id 不匹配；R00 含人物/场景/道具集合/符号表；R01 含完整剧情；R02 含主线故事推进；S 页含长手写正文；P01 不是 9:16；缺 reference_dependencies、visual_center、density_range、composition_mode、paper_policy 或 style_policy。
