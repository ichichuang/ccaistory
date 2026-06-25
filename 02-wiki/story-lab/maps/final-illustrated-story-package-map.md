# 最终插图故事成品 map / Final Illustrated Story Package Map

> 补齐新 doctrine 此前缺失的"装配最终成品"环节。此前系统地图止于"单张 accepted ReferenceAsset"；本图定义从多张 accepted 资产 + 故事资产到一个完整插图故事成品包的装配与发布就绪路径。canonical 计划落 `02-wiki`，操作记录落 `50-agent-work`，图像二进制不入 git。

## 1. 前置：单资产链路（已存在）

每张图都先走完：
`ImageExecutionPackage (02-wiki/70-execution-packages)` → 编译/Lint (50-agent-work) → WebGPTImage 受控出图 → 候选 (01-raw/generated-raw) → `GenerationRun` (50-agent-work/runs) → 人工图像复核 + 资产 QA (50-agent-work) → **accepted `ReferenceAsset` (02-wiki/reference-assets)** / 拒绝 → 90-archive。

详见 `image-production-lineage-map.md` 与工作流 `E → F → G → H → I → J`。

## 2. 成品装配链路（本图新增）

```
StoryProject (required_asset_count)
        │
        ▼
所有必需 Scene/Character/VisualStyle 卡就绪
        │
        ▼
所有必需 ImageExecutionPackage 均产出 accepted ReferenceAsset
（accepted_asset_count >= required_asset_count）
        │
        ▼  K: Final Illustrated Story Package Assembly Workflow
装配：按页/场景把 accepted ReferenceAsset + 故事文字层
组织为「成品包计划」→ 回填 StoryProject.Final Package 区（canonical）
操作装配记录 → 50-agent-work/story-lab/runs/
（图像二进制不入 git；以 canonical 卡 + 路径引用表达）
        │
        ▼  人工批准 → StoryProject.final_package_status = ready
        │
        ▼  L: Publishing Readiness Workflow
发布就绪检查清单 (50-agent-work/qa-results) + 人工完整阅读
        │
        ▼
StoryProject.publishing_readiness_status = ready
最终发布决策（canonical）
```

## 3. 硬门禁（不得跳过）

- 任一必需场景/资产未 accepted → 阻断装配。
- `accepted_asset_count < required_asset_count` → 阻断。
- 缺人工批准 → 不得 `final_package_status: ready`。
- 缺人工完整阅读或存在阻断项 → 不得 `publishing_readiness_status: ready`。
- 图像二进制默认不提交（`.gitignore` 忽略）。

## 4. 两窗口与 runtime 角色

- WebGPT 指令窗：规划装配、复核、产出本地装配指令；不出图。
- Codex/Claude：在本地文件系统执行装配，写 canonical 卡与 50-agent-work 记录。
- runtime：仅 `artifact-check-registry` / `artifact-lineage` 做派生缓存血缘自检；不持有成品 canonical。
- WebGPTImage：不参与装配（装配阶段无新出图）。

## 5. 关联

- codex 指令：`00-system/codex-instructions/ASSEMBLE_FINAL_ILLUSTRATED_STORY_PACKAGE.md`
- 工作流：`workflows/Final Illustrated Story Package Assembly Workflow.md`、`workflows/L-Publishing-Readiness-Workflow.md`
- 技能：`skills/Final Illustrated Story Package Assembly Skill.md`、`skills/Publishing-Readiness-Skill.md`
- 验收清单：`acceptance-checklists/Final Illustrated Story Package Readiness Checklist.md`
- 模板：`templates/canonical-assets/StoryProject.md`（`final_package_status` / `required_asset_count` / `accepted_asset_count` / `publishing_readiness_status`）
