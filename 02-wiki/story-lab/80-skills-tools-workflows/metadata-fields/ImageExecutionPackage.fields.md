# ImageExecutionPackage 字段定义 / Field Schema

fileClass：`ImageExecutionPackage`（`type: image_execution_package`）。卡模板：`../templates/canonical-assets/ImageExecutionPackage.md`。卡片位置：`02-wiki/story-lab/70-execution-packages/`。每个完整执行包必须独立成一个 `.md`。

## Common required fields / 通用必填字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| type | select | `image_execution_package` | image_execution_package | 固定值 |
| id | text | kebab-case，唯一 | `<package-id>` | 与文件名一致 |
| title_zh | text | — | 占位图像执行包 | 中文标题 |
| title_en | text | — | Placeholder Image Execution Package | 英文标题 |
| status | select | draft / ready / generating / accepted / rejected / archived | draft | 执行包状态 |
| project_id | text | story_project id | `<story-project-id>` | 所属项目 |
| canonical | boolean | true / false | true | 固定 `true` |
| created_at | date | YYYY-MM-DD | 2026-06-24 | — |
| updated_at | date | YYYY-MM-DD | 2026-06-24 | — |
| owner | text | — | `<owner>` | — |
| version | text | `v\d+` | v0 | — |
| tags | list | — | [] | — |
| related_assets | list | — | [] | — |
| source_paths | list | 01-raw 路径 | [] | — |

## Type-specific fields / 专有字段

| field | type | allowed values | example | notes |
|---|---|---|---|---|
| scene_id | text | scene id | `<scene-id>` | 目标场景 |
| characters | list | character id | [] | 涉及角色 |
| visual_style | list | visual_style id | [] | 视觉风格 |
| prompt_recipe | text | prompt_recipe id | `<prompt-recipe-id>` | 绑定技法 |
| target_model | text | 模型名 | "" | 目标出图模型 |
| aspect_ratio | text | 如 `1:1` `16:9` | "1:1" | 比例（带冒号需引号） |
| reference_assets | list | reference_asset id | [] | 绑定参考图 |
| required_reference_assets | list | reference_asset id | [] | 必需的参考资产依赖（缺失则不得 ready） |
| prohibited_reference_assets | list | reference_asset id | [] | 禁止用作依赖的资产（含 rejected / deprecated） |
| output_assets | list | reference_asset id | [] | 产出资产（accepted 后回填） |
| generation_run_ids | list | generation_run id | [] | 历次生成 run |
| last_run | text | generation_run id | "" | 最近一次 run |
| qa_result | select | pending / passed / failed | "" | 最近 QA 结论 |
| r00_dependency_policy | text | — | "" | 本包从 R00 借用的具体视觉属性（不得借用整套角色/场景） |
| maximum_anchor_reuse_policy | text | — | "" | 单一锚图（尤其 R00）最大复用约束 |
| final_assembly_dependency | text | story_project / package id | "" | 最终成品装配依赖 |
| previous_page_reference | text | ImageExecutionPackage id | "" | p02 及之后必填；上一张已接受页面或页面包 |
| previous_page_scene_summary | text | — | "" | 上一页可见场景摘要 |
| current_page_scene_summary | text | — | "" | 当前页可见场景摘要 |
| r00_reference_asset | text | ReferenceAsset id | "" | 系列主锚；只控制视觉、角色、比例、纸张和红笔语言 |
| continuity_from_previous_page | list | — | [] | 必须从前页继承的场景/位置/人物状态 |
| scene_delta_from_previous_page | list | — | [] | 当前页相对前页允许改变的场景差量 |
| allowed_progression_delta | list | — | [] | 当前页允许的强度/光线/距离/怪异程度递进 |
| forbidden_continuity_breaks | list | — | [] | 禁止的突跳、过早元素、构图复制或未解释新增物 |
| page_hook_question | text | — | "" | 本页明确视觉问题 / 翻页问题 |
| hook_visual_target | text | — | "" | 红笔标注应指向的具体不确定性 |
| hook_annotation_guidance | text | — | "" | 1-3 个短、童稚、页内具体的中文标注候选或规则 |
| hook_failure_mode_to_avoid | list | — | [] | 本页钩子最容易失败的读法，例如眼睛被误读成路灯 |
| symbol_semantics_target | text | — | "" | 线索应被读成的语义类别，例如“隐藏活物的反光眼睛” |
| symbol_misread_to_avoid | text | — | "" | 线索不得被读成的物体类别，例如“路灯 / 灯泡 / 固定光源” |
| repair_guardrails | list | — | [] | 返修时必须保留的连续性、空间逻辑和构图边界 |
| progression_budget_from_previous_page | text | — | "" | 相对上一页允许推进的最大幅度 |
| overcorrection_guardrail | text | — | "" | 防止修正一个问题时制造更强连续性断裂的规则 |
| composition_priority_order | list | — | [] | 读图顺序：第一眼应读到连续场景，第二眼才发现线索 |
| escalation_level | text | story-stage label | "" | 本页在故事递进曲线中的强度位置 |
| continuity_qa_required | boolean | true / false | true | p02 及之后必须为 true |
| hook_qa_required | boolean | true / false | true | p02 及之后必须为 true |

## Validation notes / 校验说明

- `type` 必须为 `image_execution_package`；`canonical=true`。
- `status: ready` 前必须通过 runtime `compile-asset` 与 `lint-asset` / `lint-prompt`（runtime 校验语义不变）。
- `aspect_ratio` 含冒号，YAML 中必须加引号。
- `output_assets` 只在 accepted 后回填，并绑定 `package_id` / `scene_id` / `characters` / `reference_assets`。
- **R00 过载防护**：`prohibited_reference_assets` 不得为空白地默认；依赖 R00 时必须在 `r00_dependency_policy` 声明仅借用的属性；需要角色/场景连续性时绑定 R01/R02 或具体 accepted reference_asset，而非泛化 R00；`required_reference_assets` 不得包含 rejected / deprecated 资产。
- p02 及之后必须填写 `previous_page_reference`、`previous_page_scene_summary`、`current_page_scene_summary`、`r00_reference_asset`、`continuity_from_previous_page`、`scene_delta_from_previous_page`、`allowed_progression_delta`、`forbidden_continuity_breaks`、`page_hook_question`、`hook_visual_target`、`hook_annotation_guidance`、`escalation_level`，且 `continuity_qa_required=true`、`hook_qa_required=true`。
- 当本页钩子存在语义误读风险或经历返修时，应填写 `hook_failure_mode_to_avoid`、`symbol_semantics_target`、`symbol_misread_to_avoid`、`repair_guardrails`、`progression_budget_from_previous_page`、`overcorrection_guardrail`、`composition_priority_order`；lint 会检查这些字段成组完整性和读图顺序。
- R00 只控制视觉连续性；上一页只控制场景连续性与递进。不得把 R00 当作后续页面的故事内容来源。

## Dataview / Bases usage / 查询用法

- Dataview：`TABLE title_zh, project_id, scene_id, target_model, status, version, last_run, qa_result FROM "02-wiki/story-lab/70-execution-packages" WHERE type = "image_execution_package" SORT status ASC`
- Bases：`../../00-dashboard/bases/image-package-board.base`；看板：`../../00-dashboard/image-package-board.md`。
