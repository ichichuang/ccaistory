# 10 Compiled Prompts

本文件为派生视图。  
唯一事实源：故事核心.json。  
如内容冲突，以故事核心.json 为准。

## 1. 编译对象

- project_id：KHN2_001
- story_id：故事0001
- source_visual_asset_spec：故事项目/KHN2_001_楼道里的红贴纸/09_视觉资产规格.json
- compiled_at：2026-06-24T00:00:00+08:00
- compile_status：pass
- prompt_count：11
- next_required_gate：semantic_lint

## 2. 资产清单

| asset_id | asset_type | canvas_ratio | compile_status | next_required_gate |
|---|---|---:|---|---|
| R00_KHN2_001_paper_mark_anchor | R00_PAPER_MARK_ANCHOR | 9:16 | pass | semantic_lint |
| R01_KHN2_001_lin_xiaomu_anchor | R01_CHARACTER_ANCHOR | 9:16 | pass | semantic_lint |
| R02_KHN2_001_corridor_door_prop_anchor | R02_SCENE_PROP_ANCHOR | 9:16 | pass | semantic_lint |
| P01_KHN2_001_platform_layout_sample | P01_PLATFORM_LAYOUT_SAMPLE | 9:16 | pass | semantic_lint |
| S01_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S02_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S03_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S04_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S05_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S06_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |
| S07_KHN2_001_source_illustration | S_SOURCE_ILLUSTRATION | 3:4 | pass | semantic_lint |

## 3. 每个 asset 的编译摘要

### R00_KHN2_001_paper_mark_anchor

Asset type: R00_PAPER_MARK_ANCHOR. Visual center: 单张红箭头贴纸贴在清洁白色作业本纸面上，旁边只有短铅笔线索样本。. Allowed content: clean white exercise paper; blue guide lines and red margin; controlled short child-handwriting clue samples; red arrow sticker; red circle, question mark, underline, pencil pressure, eraser marks. Density: low_to_medium. Composition: single ordered visual center, no symbol sheet. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'allowed_short_clues': ['别跟错箭头', '别替我贴', '终于看见了', '这次没有走错'], 'child_note_max_chars': 8}. Paper policy: {'surface': 'single clean white paper surface', 'ratio': '9:16', 'orientation': 'portrait'}. Style policy: {'line_quality': 'controlled childlike pencil and sticker marks', 'forbidden': ['author style', 'dirty horror texture', 'old yellow paper']}. Canvas ratio: 9:16. Reference dependencies: 无. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### R01_KHN2_001_lin_xiaomu_anchor

Asset type: R01_CHARACTER_ANCHOR. Visual center: 林小沐的学生角色锚定：书包、校服外套、钥匙扣，谨慎但不惊恐的站姿。. Allowed content: single student protagonist reference; middle-school age silhouette; school jacket, backpack, keychain; controlled childlike drawing treatment. Density: medium. Composition: single character reference sheet without story scene payload. Text policy: {'typed_narration_in_image': False, 'labels_only_if_needed': True, 'child_note_layer_only': False}. Paper policy: {'requires_r00_texture': True}. Style policy: {'line_quality': 'simple safe student character anchor', 'forbidden': ['adult crime mood', 'author style', 'ending reveal']}. Canvas ratio: 9:16. Reference dependencies: R00_KHN2_001_paper_mark_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### R02_KHN2_001_corridor_door_prop_anchor

Asset type: R02_SCENE_PROP_ANCHOR. Visual center: 白色楼道墙面与走廊尽头无人门的空间锚定，红箭头贴纸作为唯一异常物。. Allowed content: corridor spatial relationship; unused door at corridor end; red arrow sticker placement; fire hydrant, phone photo timeline, keychain scale facts; material and placement facts. Density: medium. Composition: scene and prop anchor without character action payload. Text policy: {'typed_narration_in_image': False, 'short_anchor_notes_only': True}. Paper policy: {'requires_r00_texture': True}. Style policy: {'line_quality': 'clean corridor geometry with child-safe unease', 'forbidden': ['crime scene', 'body horror', 'author style']}. Canvas ratio: 9:16. Reference dependencies: R00_KHN2_001_paper_mark_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### P01_KHN2_001_platform_layout_sample

Asset type: P01_PLATFORM_LAYOUT_SAMPLE. Visual center: 上方源插图区、下方 typed_narration 区、角落短 child note layer 的版式样张。. Allowed content: 9:16 platform page layout; image and text region sample; safe spacing and reading order; placeholder text only. Density: low_to_medium. Composition: layout sample only, not a complete story image. Text policy: {'placeholder_text_only': True, 'typed_narration_in_image': False, 'no_final_body_copy': True}. Paper policy: {'requires_r00_texture': True}. Style policy: {'layout': 'readable mobile graphic story page', 'forbidden': ['full story illustration', 'final platform body text', 'author style']}. Canvas ratio: 9:16. Reference dependencies: R00_KHN2_001_paper_mark_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S01_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 电梯旁白墙上的第一张红箭头贴纸，学生主角只作为轻量观察者。. Allowed content: single page story action; student sees first red arrow sticker; clean corridor wall; visual_memory_point from S01; short child note layer if needed. Density: medium. Composition: single page source illustration, no platform text body. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S02_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 消防栓旁第二张红贴纸和短线索“别跟错箭头”。. Allowed content: second red arrow sticker near fire hydrant; unused door direction; short child note layer; clean corridor wall. Density: medium. Composition: single page source illustration, clue-forward composition. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'allowed_short_clue': '别跟错箭头', 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S03_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 家门口地脚线上的低位红箭头贴纸，暗示路线从主角门口开始。. Allowed content: low sticker on baseboard; student apartment door threshold; safe student protagonist; route starts near home door. Density: medium. Composition: low-angle clue composition. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S04_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 新红贴纸压住旧贴纸边角，旁边是短线索“别替我贴”。. Allowed content: new red sticker covering moved sticker corner; short note clue; student hand near wall; clean wall and sticker edge. Density: medium. Composition: close-up clue feedback. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'allowed_short_clue': '别替我贴', 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S05_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 手机照片时间线对齐墙面缺口，第五张红贴纸补上空白处。. Allowed content: phone photo timeline; new red sticker on blank wall gap; short clue note; clean corridor wall. Density: medium_to_high. Composition: phone evidence close-up with one clear sticker focus. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'allowed_short_clue': '终于看见了', 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S06_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 钥匙扣背面的小红箭头贴纸，箭头指向家门钥匙。. Allowed content: keychain back with tiny red arrow sticker; student hand holding keys; unused door visible as direction target; personal route reveal. Density: medium. Composition: keychain close-up with corridor depth hint. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

### S07_KHN2_001_source_illustration

Asset type: S_SOURCE_ILLUSTRATION. Visual center: 门内白墙上的七张红贴纸路线，最后一张指向主角站位。. Allowed content: inside unused door with clean white wall; seven red stickers matching route; short clue note; blank red sticker callback near home door. Density: medium_to_high. Composition: ending callback composition with ordered sticker route. Text policy: {'typed_narration_in_image': False, 'child_note_layer_only': True, 'allowed_short_clue': '这次没有走错', 'child_note_max_chars': 8}. Paper policy: {'paper_surface': 'clean white notebook paper', 'line_style': 'subtle school notebook lines allowed', 'cleanliness': 'white, clean, not yellowed, not aged, not archival', 'allowed_marks': ['light pencil pressure marks', 'eraser traces', 'small red circles', 'small arrows', 'question marks', 'short child note marks'], 'forbidden_paper': ['yellowed old paper', 'dirty paper', 'archive document texture', 'parchment', 'burned edge', 'large blank test sheet']}. Style policy: {'visual_style': 'child-safe horror notebook source illustration', 'drawing_age_feel': 'authentic 9-12 year old child drawing influence, but readable', 'line_quality': 'slightly crooked pencil and ballpoint lines, imperfect but controlled', 'color_policy': 'mostly pencil/ballpoint with restrained red sticker accents and limited crayon texture', 'rendering_policy': 'source illustration only, not final platform page, not polished poster, not UI screenshot', 'anti_ai_policy': ['avoid polished digital concept art', 'avoid generic AI horror composition', 'avoid fake printed handwriting', 'avoid over-rendered cinematic lighting'], 'text_policy_summary': 'no typed narration inside image; Chinese child note only 2-8 characters if present'}. Canvas ratio: 3:4. Reference dependencies: R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor. Output is a source illustration or anchor spec only; do not generate final platform page UI.

## 4. 每个 asset 的负面约束摘要

| asset_id | negative / forbidden guard |
|---|---|
| R00_KHN2_001_paper_mark_anchor | 人物; 火柴人; 完整场景; 道具集合; 符号散点表; UI/流程图; dirty scrap paper; yellowed old paper; long handwritten body; 制作说明; typed narration inside image |
| R01_KHN2_001_lin_xiaomu_anchor | complete plot; full scene; mainline event; ending reveal; author style instruction; typed narration inside image |
| R02_KHN2_001_corridor_door_prop_anchor | mainline event; ending reveal; complete plot; author style instruction; typed narration inside image |
| P01_KHN2_001_platform_layout_sample | complete story illustration; source illustration semantics; final publish copy; author style instruction; typed narration inside image |
| S01_KHN2_001_source_illustration | long handwritten body; setting sheet; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S02_KHN2_001_source_illustration | long handwritten body; setting sheet; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S03_KHN2_001_source_illustration | adult work identity; long handwritten body; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S04_KHN2_001_source_illustration | long handwritten body; full plot diagram; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S05_KHN2_001_source_illustration | long handwritten body; full evidence board; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S06_KHN2_001_source_illustration | long handwritten body; ending reveal inside door; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |
| S07_KHN2_001_source_illustration | gore; corpse; crime scene; long handwritten body; platform final body copy; author style instruction; typed narration inside image; yellowed old paper; dirty paper; archive document texture; parchment; burned edge; large blank test sheet; avoid polished digital concept art; avoid generic AI horror composition; avoid fake printed handwriting; avoid over-rendered cinematic lighting |

## 5. reference_dependencies 摘要

| asset_id | reference_dependencies |
|---|---|
| R00_KHN2_001_paper_mark_anchor | 无 |
| R01_KHN2_001_lin_xiaomu_anchor | R00_KHN2_001_paper_mark_anchor |
| R02_KHN2_001_corridor_door_prop_anchor | R00_KHN2_001_paper_mark_anchor |
| P01_KHN2_001_platform_layout_sample | R00_KHN2_001_paper_mark_anchor |
| S01_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S02_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S03_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S04_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S05_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S06_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |
| S07_KHN2_001_source_illustration | R00_KHN2_001_paper_mark_anchor, R01_KHN2_001_lin_xiaomu_anchor, R02_KHN2_001_corridor_door_prop_anchor |

## 6. paper_policy / style_policy 覆盖说明

- 11 个 compiled prompt 均包含 `paper_policy`。
- 11 个 compiled prompt 均包含 `style_policy`。
- S01-S07 均使用清洁白色 notebook paper 策略与 child-safe horror notebook source illustration 策略。
- typed_narration 不写入 image；如有中文儿童短笔记，仅限 2-8 字。

## 7. 下一个门禁

semantic_lint

## 8. 明确声明

- 未生成图片。
- 未生成执行包。
- 未调用 WebGPT。
- 未生成 source pilot task list。
- 未生成提示词包。
- 未生成发布包。
