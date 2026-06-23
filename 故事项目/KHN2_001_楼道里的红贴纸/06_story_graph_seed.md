本文件为派生视图。
唯一事实源：故事核心.json。
如内容冲突，以故事核心.json 为准。

# 06 story_graph seed

## 结论

未新建 8 页 story_graph seed。检查 `故事核心.json` 后，现有 `story_graph.nodes` 为 7 页，满足本阶段直接进入 Skill Executor 的条件：

- nodes 数量：7
- edges 数量：6
- 每个 node 均包含：`node_id`、`page_role`、`typed_hook`、`typed_narration`、`final_hook_sentence`、`next_page_question`、`applied_skills`
- 终页 `S07.next_page_question` 为空，符合终页例外

## 现有 story_graph 概览

| 页 | page_role | typed_hook | next_page_question | applied_skills |
|---|---|---|---|---|
| S01 | opening | 早上出门时，白墙上多了一张很新的红贴纸。 | 如果只是维修记号，为什么第二天会多出一张？ | everyday_anomaly, page_turn_hook, emotional_pull |
| S02 | middle_escalation | 第二张红贴纸贴在更里面，箭头还是指向同一扇门。 | 没人开的门，为什么每天都像有人在给它铺路？ | horror_escalation, misdirection_disproof, page_turn_hook |
| S03 | middle_escalation | 第三张贴纸没有贴在墙上，而是贴在她门口的地脚线上。 | 为什么这条路线偏偏从她家门口开始？ | horror_escalation, child_perspective_wonder, page_turn_hook |
| S04 | turning_point | 她把第三张贴纸挪开，晚上墙上多了一张新的。 | 贴纸怎么知道是她动过？ | misdirection_disproof, horror_escalation, page_turn_hook |
| S05 | middle_escalation | 第五张贴纸贴在她手机照片里没有出现过的位置。 | 如果路线一直完整，只是她以前没看见呢？ | horror_escalation, misdirection_disproof, platform_completion_rate |
| S06 | pre_ending | 第六张贴纸不在墙上，而在她的钥匙扣背面。 | 如果路线的终点是那扇门，她的钥匙为什么也在路线里？ | strange_tale_twist, horror_escalation, page_turn_hook |
| S07 | ending | 那扇没人开的门，用她家的钥匙打开了。 |  | fate_loop, strange_tale_twist, emotional_pull |

## 边说明

现有 `story_graph.edges` 为顺序边：

- S01 -> S02
- S02 -> S03
- S03 -> S04
- S04 -> S05
- S05 -> S06
- S06 -> S07

本阶段未扩写 edge 字段，因为任务要求在已有 6 到 8 页且 node 字段齐备时直接进入 Skill Executor。
