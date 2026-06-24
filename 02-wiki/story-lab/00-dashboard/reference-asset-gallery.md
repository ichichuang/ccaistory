# 参考素材画廊 / Reference Asset Gallery

> 全部 `reference_asset` 参考素材卡片的画廊视图。
> Gallery view of all `reference_asset` cards.

## Purpose / 用途

- 中文：集中浏览所有参考素材（风格参考、姿势参考、构图参考等），查看其归属项目、质量状态与被引用情况。二进制文件本身不入库，卡片记录其位置。
- English: Browse all reference assets (style, pose, composition references, etc.), showing their owning project, quality status, and where they are used. Binary files are not committed; the card records their location.

## Data Source Path / 数据源路径

- 文件夹 / Folder: `02-wiki/story-lab/reference-assets/`
- 类型 / Type value: `reference_asset`

## Filters / 筛选

- 仅 `type = "reference_asset"`。
- Only `type = "reference_asset"`.
- 可选：按 `project_id = "<project-id>"`、`status` 或 `quality_status` 过滤。
- Optional: filter by `project_id = "<project-id>"`, `status`, or `quality_status`.

## Sorting / 排序

- 按 `project_id` 升序，再按 `status` 升序。
- Sort by `project_id` ascending, then `status` ascending.

## Display Fields / 展示字段

- `id`
- `title_zh`
- `project_id`
- `status`
- `used_by`
- `quality_status`

## 文件位置策略 / File Location Policy

- 中文：参考素材的二进制文件（图片/视频等）默认被 `.gitignore` 排除，不进入版本库。每张参考素材卡片必须在 frontmatter（如 `source_paths`）或正文中记录其实际存放位置，以便检索；卡片本身才是被追踪的权威记录。
- English: Reference-asset binaries (images/videos) are gitignored by default and never enter the repository. Each card must record the real storage location in frontmatter (e.g. `source_paths`) or body text so it can be located; the card itself is the tracked canonical record.

## Dataview

```dataview
TABLE
  title_zh AS "标题",
  project_id AS "项目",
  status AS "状态",
  used_by AS "被引用",
  quality_status AS "质量状态"
FROM "02-wiki/story-lab/reference-assets"
WHERE type = "reference_asset"
SORT project_id ASC, status ASC
```

## Manual Fallback / 手动回退

未安装 Dataview 时：
When Dataview is not installed:

1. 打开 `02-wiki/story-lab/reference-assets/` 浏览所有参考素材卡片。
   Open `02-wiki/story-lab/reference-assets/` and browse all reference-asset cards.
2. 逐张读取 frontmatter：`id`、`title_zh`、`project_id`、`status`、`used_by`、`quality_status`，以及记录二进制位置的 `source_paths`。
   Read each card's frontmatter: `id`, `title_zh`, `project_id`, `status`, `used_by`, `quality_status`, plus `source_paths` recording the binary location.
3. 由于二进制被 gitignore，请通过卡片记录的位置去对应目录或外部存储查看实际素材文件。
   Because binaries are gitignored, open the location recorded in the card to view the actual asset file in its directory or external storage.
4. 通过 `used_by` 反查哪些角色或执行包正在引用该素材。
   Use `used_by` to trace which characters or execution packages reference this asset.
