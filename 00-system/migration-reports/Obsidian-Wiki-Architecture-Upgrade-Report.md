# Obsidian Story Production Wiki 架构升级报告

## 1. 执行概要 / Execution summary

| 项目 | 值 |
|---|---|
| 执行时间 | 2026-06-24 18:36 CST |
| 仓库 | ichichuang/ccaistory |
| 工作分支 | `main`（用户指令：完全在 main 重构，不创建新分支，自动提交并推送） |
| 任务类型 | 架构升级（迁移 + 新架构搭建，**不生成任何故事/图片/Prompt/执行包实例**） |
| 结果 | 通过：底层系统迁移完整、runtime 全门禁通过、无破坏性改动 |

> 边界说明：任务规范第 0.3–0.5 节原要求新建分支 `refactor/obsidian-story-production-wiki` 且不推送。用户在执行前明确改为「完全在 main 分支重构，不产生任何新分支，自动提交并推送」，与持久记忆「work on main, no branches」一致。本报告据此在 `main` 执行并推送。

## 2. 架构变更摘要 / Summary of architecture changes

- 仓库从「以 runtime/contracts 为唯一机器事实源、Markdown 为说明层」的形态，升级为 **Obsidian Story Production Wiki + runtime 工具层**。
- 建立 4 层 + 工具层结构：`01-raw`（不可变原始输入）→ `02-wiki`（canonical Markdown 生产知识）→ `50-agent-work`（agent 运行/中间产物/QA/返修记录）→ `90-archive`（拒绝/弃用/退役/历史），`runtime/` 作为 root 可执行工具层。
- 9 个底层中文目录全部迁入新架构（207 个文件以 git rename 迁移，历史保留）。
- 翻转 doctrine：**Markdown canonical 卡是生产知识长期事实源**；contracts 仅是**校验规则**事实源；runtime 产物与 Artifact Registry 是派生缓存；持久决策必须回写 canonical 卡。
- 新增 canonical 资产模板、字段定义、看板、索引、Base 规格、map、架构文档、Codex 指令、各层 README。

## 3. 迁移目录映射 / Moved directory map

| 旧路径（根目录） | 新路径 | 文件数 |
|---|---|---|
| `总控/` | `02-wiki/story-lab/00-dashboard/legacy-control/` | 10 |
| `Codex指令/` | `00-system/codex-instructions/` | 26 |
| `工作流/` | `02-wiki/story-lab/80-skills-tools-workflows/workflows/` | 18 |
| `生产技能/` | `02-wiki/story-lab/80-skills-tools-workflows/skills/` | 32 |
| `提示词库/` | `02-wiki/story-lab/60-prompts/legacy-prompt-library/` | 27 |
| `结构规范/` | `02-wiki/story-lab/80-skills-tools-workflows/structure-specs/` | 25 |
| `验收清单/` | `02-wiki/story-lab/80-skills-tools-workflows/acceptance-checklists/` | 29 |
| `模板/` | `02-wiki/story-lab/80-skills-tools-workflows/legacy-templates/` | 14 |
| `创作者技法库/` | `02-wiki/story-lab/80-skills-tools-workflows/creator-techniques/` | 25 |
| `清理验收报告.md` | `00-system/migration-reports/清理验收报告.md` | 1 |

合计 **207** 个文件，全部以 `git mv`（rename）迁移；git 识别为 188 纯 rename + 19 rename+modify（被链接重写/doctrine 更新触及）。

- **链接修复**：271 个旧目录前缀 wikilink（`旧目录/文件` 形式的双链）全部按目录前缀重写为新路径（272 处替换 / 15 文件），重写后 0 残留旧前缀。所有 wikilink 经 runtime 链接检查器验证可解析（broken_link_count = 0）。
- **runtime 路径同步**：`runtime/contracts/sync_docs_check.py` 的 `R00_MARKDOWN_FILES` 5 个硬编码文档路径更新到迁移后位置（仅路径，未改校验逻辑）。

## 4. 新目录树 / New directory tree

```
AI+Story/
  00-system/{architecture, codex-instructions, runtime-boundary, migration-reports}/
  01-raw/story-lab/{user-inputs, reference-inputs, screenshots, generated-raw, model-raw-outputs}/
  02-wiki/story-lab/
    00-dashboard/{bases/, legacy-control/}
    10-projects/  20-worlds/  30-characters/  40-scenes/  50-visual-styles/
    60-prompts/{legacy-prompt-library/}
    70-execution-packages/
    80-skills-tools-workflows/{templates/canonical-assets/, metadata-fields/,
      workflows/, skills/, structure-specs/, acceptance-checklists/,
      legacy-templates/, creator-techniques/}
    90-indexes-zh/  maps/  reference-assets/
  50-agent-work/story-lab/{runs, compiled-prompts, semantic-lint-results,
    qa-results, image-review-forms, repair-notes}/
  90-archive/story-lab/{legacy-projects, deprecated-prompts, old-runs,
    rejected-assets, retired-execution-packages}/
  runtime/  (工具层，原样保留)
```

## 5. 新建 canonical 模板 / Created templates (11)

`02-wiki/story-lab/80-skills-tools-workflows/templates/canonical-assets/`：
StoryProject、Character、Scene、VisualStyle、PromptRecipe、ImageExecutionPackage、ReferenceAsset、GenerationRun、RepairNote、SkillCard、WorkflowCard（均含统一 frontmatter：type/id/title_zh/title_en/status/project_id/related_assets/source_paths/tags/created_at/updated_at/owner/version/canonical + 类型专有字段 + 固定正文章节）。

## 6. 新建字段定义 / Metadata field schemas (11)

`02-wiki/story-lab/80-skills-tools-workflows/metadata-fields/`：每个 canonical 类型 1 个 `*.fields.md`，含必填/可选字段、类型、允许值、占位示例、校验说明、Dataview/Bases 用法。

## 7. 新建看板与索引 / Dashboards & indexes

- 看板（5，`02-wiki/story-lab/00-dashboard/`）：story-lab-home、image-package-board、repair-queue、generation-run-log、reference-asset-gallery。
- 中文索引（6，`02-wiki/story-lab/90-indexes-zh/`）：prompt-recipe-index、workflow-skill-index、character-gallery、scene-board、visual-style-index、project-index。
- 每个看板/索引含：用途、数据源路径、筛选、排序、展示字段、Dataview 查询块、手动回退说明。

## 8. 新建 Base 规格 / Base specifications (6)

`02-wiki/story-lab/00-dashboard/bases/`：image-package-board、character-gallery、scene-board、repair-queue、reference-asset-gallery、generation-run-log（保守 YAML，首行注明「需在 Obsidian 内验证后使用」；含源文件夹、type 过滤、status 过滤、排序、展示属性、视图类型）。

## 9. 新建 map 与系统文档 / Maps & system docs

- map（4，`02-wiki/story-lab/maps/`）：story-production-system-map、image-production-lineage-map、runtime-tool-boundary-map、webgpt-two-window-workflow-map（含 Mermaid 流程图）。
- 架构文档（3，`00-system/architecture/`）：AI+Story-Obsidian-Wiki-Architecture、Canonical-Asset-Model、Image-Production-Governance。
- runtime 边界（3，`00-system/runtime-boundary/`）：Runtime-Is-Tool-Layer、Artifact-Registry-Is-Cache、Markdown-Is-Canonical。
- Codex 指令（5 新，`00-system/codex-instructions/`）：START_NEW_STORY_OBSIDIAN_WIKI、CREATE_IMAGE_EXECUTION_PACKAGE、BACKFILL_GENERATION_RUN、REPAIR_FAILED_IMAGE_RUN、ACCEPT_REFERENCE_ASSET。
- README（10）：根 + 00-system + 01-raw(×2) + 02-wiki(×2) + 50-agent-work(×2) + 90-archive(×2)。

## 10. runtime 边界变更 / Runtime boundary changes

- doctrine 在 5 处更新：`00-system/codex-instructions/校验机器事实源Contracts.md`、`.../workflows/Contracts同步流程.md`、`.../legacy-control/总索引.md`、`.../skills/机器事实源Contracts技能.md`、`.../structure-specs/机器事实源Contracts结构规范.md`。新口径：contracts 仅为**校验规则**（状态机/视觉资产/skill/质量门禁/pipeline action）事实源；生产知识 canonical 在 `02-wiki` Markdown；runtime 产物 + Artifact Registry 为派生缓存；Artifact Registry **不是** canonical 资产登记表；持久决策回写 Markdown。
- **唯一 runtime 代码改动**：`runtime/contracts/sync_docs_check.py` 的 `R00_MARKDOWN_FILES` 路径同步（迁移导致，未改校验语义）。runtime 工具逻辑、contracts、schemas、tests 其余均未改动。
- `故事核心.json` 等「per-run 机器输入」属 runtime 工作文件语义，按设计保留，不与 canonical Markdown doctrine 冲突。

## 11. .gitignore 变更 / .gitignore changes

- 移除对 `01-raw/ 50-agent-work/ 90-archive/` 的整目录屏蔽，改为 **allowlist**：默认忽略三层内容，但保留 `**/README.md` 与 `**/.gitkeep` 及目录骨架。
- 保留 runtime 缓存/产物屏蔽、二进制扩展名（png/jpg/jpeg/webp/gif/psd/ai/zip/mp4/mov）、Python 缓存、系统与 Obsidian 个人状态。
- 结果：架构骨架 + canonical 知识 + 模板 + 看板 + Base + 字段定义 + 架构文档**可提交**；原始/生成图像、视频、压缩包、runtime 运行缓存**不入库**。`.base` 文件正常跟踪。

## 12. 验收命令结果 / Validation results

| 命令 | 结果 |
|---|---|
| `python runtime/aistory.py status` | 正常返回状态 |
| `python runtime/aistory.py validate` | passed=true（skill_count=12） |
| `python runtime/aistory.py validate-contracts` | passed=true |
| `python runtime/aistory.py check-contract-drift` | passed=true，broken_link_count=0 |
| `python runtime/aistory.py smoke-test` | passed=true，failed_checks=[] |
| `python -m compileall -q runtime` | 通过 |

结构门禁：旧根目录与 `故事项目/资产库/输出归档/原始资料/runtime/.runs/runtime/.artifacts` 全部不存在；新架构 5 层目录齐备；11 模板 / 11 字段 / 5 看板 / 6 索引 / 6 Base / 4 map / 11 系统文档 / 10 README 全部就位；runtime 11 模块完整。

## 13. 禁止标识搜索结果 / Forbidden identifier search

| 标识 | 活动内容命中 | 说明 |
|---|---|---|
| KHN2_001 / 楼道里的红贴纸 / 红贴纸 / R00_人工外部生成操作单 / 六资产试产 / WebGPT试产 / manual_external_generation_r00 / CLEAN_WHITE_NOTEBOOK | **0（生产实例层）** | 仅出现在 `00-system/migration-reports/清理验收报告.md` 的**审计表格**中，记录「已删除、命中=0」，属历史审计痕迹，按设计保留，非任何真实故事实例。 |

引擎词汇（`compiled_prompt`、`semantic_lint`、`artifact_registry`、`source_pilot_ready`、`R00_PAPER_MARK_ANCHOR`）作为 runtime 代码/合同/schema/状态机固有词汇按设计保留。

## 14. 二进制资产扫描 / Binary asset scan

`git ls-files | grep -iE '\.(png|jpg|jpeg|webp|gif|psd|ai|zip|mp4|mov)$'` → **0 命中**。仓库不跟踪任何二进制图像/视频/压缩包/设计源文件。

## 15. 剩余风险 / Remaining risks

- `.base` 文件为保守 YAML 规格，需在 Obsidian（Bases 插件）内打开验证后再依赖。
- Obsidian 插件（Dataview / Metadata Menu / Templater / QuickAdd / Bases）未由本次重构配置；看板/索引均提供手动回退说明。
- runtime `smoke-test` / pipeline 命令每次运行会重新生成 `runtime/.runs` 缓存（已 gitignore，不影响提交）。
- 迁移后的历史文档保留历史分组标题（如 `## Codex指令`）；内部链接已全部指向新路径。
- `清理验收报告.md` 按设计保留禁止标识的审计痕迹（记录其已被删除）。

## 16. 人工后续项 / Manual follow-up

1. 在 Obsidian 内验证 6 个 `.base` 视图并按需调整。
2. 安装/启用 Dataview、Metadata Menu、Templater、QuickAdd、Bases 等插件。
3. （可选）将迁移文档的历史分组标题改名为新层级名。
4. 首个新故事试产请走 `00-system/codex-instructions/START_NEW_STORY_OBSIDIAN_WIKI.md`。

## 17. 就绪结论 / Readiness verdict

✅ **就绪**：仓库已成为可执行的 Obsidian Story Production Wiki + runtime 工具层，底层系统迁移完整、doctrine 已翻转、runtime 全门禁通过、无二进制污染、无破坏性改动。具备在新架构下进行**首个新故事试产**的前置条件（本次未创建任何真实故事/资产）。
