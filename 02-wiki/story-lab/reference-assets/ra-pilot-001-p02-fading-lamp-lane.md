---
type: reference_asset
id: ra-pilot-001-p02-fading-lamp-lane
title_zh: pilot-001 p02 灯火渐稀小路成图资产
title_en: pilot-001 p02 Fading-Lamp Lane Accepted Image Asset
status: accepted
project_id: pilot-001
canonical: true
visual_role: scene-anchor
quality_status: accepted
file_location: 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png
source_run: gr-pilot-001-p02-repair-01-20260630-154548-webgptimage
source_generation_run: gr-pilot-001-p02-repair-01-20260630-154548-webgptimage
source_image_review_form: review-pilot-001-p02-candidate-repair-01-20260630-154548
source_asset_qa_result: qa-pilot-001-p02-candidate-repair-01-20260630-154548
accepted_by: ichichuang
accepted_at: 2026-06-30
qa_required: true
superseded_by: ""
source_repair_note: ""
used_by:
  - iep-pilot-001-p02-fading-lamp-lane
qa_evidence:
  - 50-agent-work/story-lab/runs/gr-pilot-001-p02-repair-01-20260630-154548-webgptimage.md
  - 50-agent-work/story-lab/image-review-forms/review-pilot-001-p02-candidate-repair-01-20260630-154548.json
  - 50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md
allowed_usage:
  - "Use as the accepted p02 page image for pilot-001."
  - "Use as a continuity reference for p03 only as the immediately previous accepted page."
  - "Use as the previous-page scene continuity reference when creating the p03 package."
  - "Use as the visual comparison target for p03 progression and hook QA."
forbidden_usage:
  - "Do not use as R00 master anchor."
  - "Do not replace ra-pilot-001-r00-master-style-character-anchor."
  - "Do not use as global style reference for the whole series."
  - "Do not copy the p02 scene into later pages."
  - "Do not force later pages to include fading lamps, mist, or this lane layout unless their package requires it."
  - "Do not use outside pilot-001 without separate approval."
r00_anchor_scope: ""
related_assets:
  - iep-pilot-001-p02-fading-lamp-lane
  - gr-pilot-001-p02-repair-01-20260630-154548-webgptimage
  - ra-pilot-001-r00-master-style-character-anchor
  - scene-fading-lamp-lane
  - char-xiaohe
  - char-mama
  - vs-pilot-001-child-horror-notebook
  - pr-pilot-001-child-horror-notebook
source_paths:
  - 01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png
  - 50-agent-work/story-lab/runs/gr-pilot-001-p02-repair-01-20260630-154548-webgptimage.md
  - 50-agent-work/story-lab/image-review-forms/review-pilot-001-p02-candidate-repair-01-20260630-154548.json
  - 50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md
tags:
  - story-lab
  - pilot-001
  - reference-asset
  - p02
  - scene-anchor
  - page-level-reference
  - accepted
created_at: 2026-06-30
updated_at: 2026-06-30
owner: ichichuang
version: v0
---

# pilot-001 p02 灯火渐稀小路成图资产 / Fading-Lamp Lane Accepted Image Asset

## Asset Summary / 资产概要

This ReferenceAsset accepts the p02 fading-lamp lane candidate for `pilot-001` as the page-level accepted image asset. It is the canonical accepted record for the image at `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`.

This p02 ReferenceAsset represents the accepted p02 page image only. It may be used as the immediately previous accepted page reference for p03 scene continuity and progression checks. It does not control global style, character design, or series-wide proportions; those remain controlled by the p01 R00 master ReferenceAsset `ra-pilot-001-r00-master-style-character-anchor`.

## Accepted Source / 接受来源

- Project: `pilot-001`
- Source package: `iep-pilot-001-p02-fading-lamp-lane`
- Source GenerationRun: `50-agent-work/story-lab/runs/gr-pilot-001-p02-repair-01-20260630-154548-webgptimage.md`
- Source candidate: `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/pilot-001-p02-candidate-repair-01-20260630-154548.png`
- Candidate hash: `84d3478e2d77feac6f67be54bfc9d959e0a524b51b66ae0f90b03a97d765f083`
- Candidate dimensions: `1254x1254`

## Visual Role / 视觉角色

`scene-anchor`: accepted p02 page image for the fading-lamp lane scene. This role is page-level and previous-page-continuity only; it is not an R00 master anchor.

## Allowed Usage / 允许用途

- Use as the accepted p02 page image for `pilot-001`.
- Use as a continuity reference for p03 only as the immediately previous accepted page.
- Use as the previous-page scene continuity reference when creating the p03 package.
- Use as the visual comparison target for p03 progression and hook QA.

## Forbidden Usage / 禁止用途

- Do not use as R00 master anchor.
- Do not replace `ra-pilot-001-r00-master-style-character-anchor`.
- Do not use as global style reference for the whole series.
- Do not copy the p02 scene into later pages.
- Do not force later pages to include fading lamps, mist, or this lane layout unless their package requires it.
- Do not use outside `pilot-001` without separate approval.

## Dependency Use / 依赖使用

The p02 source package `iep-pilot-001-p02-fading-lamp-lane` records this ReferenceAsset as its accepted output asset. A future p03 package may use this asset only as the immediately previous accepted page reference for scene continuity and progression checks, while continuing to use `ra-pilot-001-r00-master-style-character-anchor` for global visual continuity.

## Quality Status / 质量状态

Accepted. Workflow I QA passed, and this Workflow J card records the human acceptance decision for the p02 page-level candidate.

## Superseded By / 被取代

None.

## Used By / 被使用

- `iep-pilot-001-p02-fading-lamp-lane`

## QA Evidence / QA 证据

- Image review form: `50-agent-work/story-lab/image-review-forms/review-pilot-001-p02-candidate-repair-01-20260630-154548.json`
- QA result: `50-agent-work/story-lab/qa-results/qa-pilot-001-p02-candidate-repair-01-20260630-154548.md`
- GenerationRun: `50-agent-work/story-lab/runs/gr-pilot-001-p02-repair-01-20260630-154548-webgptimage.md`

## File Location Policy / 文件位置策略

The binary image remains in `01-raw/story-lab/generated-raw/pilot-001/iep-pilot-001-p02-fading-lamp-lane/`. This Markdown card is the canonical accepted ReferenceAsset record and stores the file location, source run, QA evidence, acceptance decision, and usage constraints.

## Accepted Provenance / 接受溯源

- Accepted by: `ichichuang`
- Accepted at: `2026-06-30`
- Source run id: `gr-pilot-001-p02-repair-01-20260630-154548-webgptimage`
- Source image review form id: `review-pilot-001-p02-candidate-repair-01-20260630-154548`
- Source asset QA result id: `qa-pilot-001-p02-candidate-repair-01-20260630-154548`
- Source repair note: none

## R00 Anchor Scope / R00 锚图作用域

None. This asset is not R00, does not become the series master, and does not change the p01 R00 master reference. R00 scope remains with `ra-pilot-001-r00-master-style-character-anchor`.
