# nvwa.skill 适配规范

状态：活动  
适配目标：把 `nvwa.skill` / `huashu-nuwa` 的蒸馏结果转为平台图文故事技法模块

## 路径登记

| 项 | 当前值 |
| --- | --- |
| 独立 `nvwa.skill` | 未找到，待人工补充路径 |
| 本地可用替代 | `/Users/cc/.ai/skill-modules/07-knowledge-research/huashu-nuwa` |
| 项目适配层 | `创作者技法库/nvwa接入/` |

## 适配输入

```yaml
distillation_target:
  type: person_or_theme
  purpose: narrative_technique_only
  allowed_sources: public_short_summary_only
  forbidden_outputs:
    - author_style_prompt
    - copied_text
    - copied_visual_style
    - image_generation
    - publish_package
```

## 适配输出

```yaml
technique_adapter_output:
  source_summary: ""
  observed_pattern: ""
  abstract_principle: ""
  usable_skill: ""
  forbidden_copy_boundary: ""
  story_graph_fields_affected: []
  validation_questions: []
  repair_actions: []
```

## 转换规则

- 人名、作品名和来源名只保留在研究索引。
- `observed_pattern` 必须改写为无作者名的 `abstract_principle`。
- `usable_skill` 必须能直接修改 `story_graph.nodes` 或 `story_graph.edges`。
- 如果蒸馏结果只能描述风格相似度，则判定为失败。
- 如果输出无法写入 `validation_questions` 和 `repair_actions`，不得入库。

## story_graph 接口

适配层允许写入：

- `applied_skills`
- `typed_hook`
- `next_page_question`
- `answer_delay`
- `suspense_type`
- `emotional_turn`
- `visual_memory_point`
- `rule_pressure`
- `contradiction`
- `final_hook_sentence`
- `payoff_target`
- `technique_notes`

适配层不得写入：

- 作者名风格指令。
- 画风模仿指令。
- 完整 prompt。
- 图像生成参数。

