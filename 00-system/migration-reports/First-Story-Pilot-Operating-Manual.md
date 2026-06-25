# AI+Story First Story Pilot Operating Manual

> ANALYSIS / OPERATING MANUAL ONLY. This document describes how to operate the existing system. It does **not** redesign the architecture, generate a real story, generate images, or create any real Character / Scene / VisualStyle / PromptRecipe / ImageExecutionPackage / GenerationRun / RepairNote / ReferenceAsset / final-package cards. Every concrete reference is a placeholder (`<project-id>`, `<package-id>`, `<image-id>`, `<run-id>`, `EXAMPLE_VALUE`).
>
> Generated: 2026-06-25 · Branch: `main` · Base commit: `bdedae4` · Status: uncommitted analysis report.

---

## 0. Executive summary

AI+Story is an **Obsidian-based story-illustration production system** with a **Python runtime tool layer**. It turns one user-supplied story into a fully illustrated, publishing-ready package through **12 sequential workflows (A–L)**, **three operating surfaces** (WebGPT planning window, Codex local executor, WebGPTImage generation window), and **three human approval gates** (plan approved → release to generate → asset accepted).

The governing doctrine is strict and must be respected by every operator:

1. **Markdown is canonical.** The source of truth is the Markdown cards under `02-wiki/story-lab/`. Everything the runtime produces is **derived, disposable cache**.
2. **Runtime is a tool layer.** `runtime/aistory.py` validates, compiles, lints, and QA-checks. It **never** creates story projects, **never** generates images, and **never** calls an external image tool.
3. **The Artifact Registry is cache.** `runtime/.artifacts/` is gitignored and rebuildable; it is **not** the canonical asset registry.
4. **Two windows are isolated.** The WebGPT planning window designs and reviews but never generates final images. The WebGPTImage window only receives one controlled execution sheet at a time and **never sees the whole repository**.
5. **Acceptance requires a three-piece evidence set:** execution telemetry + human image review + asset QA. No piece, no acceptance.
6. **Binary images are never committed by default.** Cards record the image's location and provenance; the bytes live outside git.

**The single most important operational fact:** when you provide a story, the system does **not** immediately make pictures. It first builds a canonical knowledge base (project → characters/scenes → visual style/recipes → execution packages), compiles and lints each image spec, and only then hands a tightly-scoped execution sheet to a separate image window. Everything after generation is evidence collection and human acceptance.

---

## 1. System state assumptions

Verified at the start of this analysis:

- Branch `main`, working tree clean.
- Latest commits include `bdedae4 chore: remove deprecated legacy operator content` and `f372acf fix: align operator layer with Obsidian production doctrine` (the P0 remediation + hard-cleanup commits).
- Remote is `https://github.com/ichichuang/ccaistory.git`.
- The repository was hard-cleaned (see `00-system/migration-reports/Hard-Cleanup-Final-Report.md`): 89 files deleted, legacy operator/prompt-lock/template directories removed. The active system is the Obsidian Story-Production Wiki (`02-wiki/story-lab/`) + the runtime tool layer (`runtime/`).
- `01-raw/`, `50-agent-work/`, `90-archive/` currently contain only README + `.gitkeep` skeletons. **No real story, card, run, or asset exists yet.** A first pilot starts from empty.

Top-level layout:

| Layer | Path | Role | Git |
| --- | --- | --- | --- |
| System doctrine | `00-system/` | Architecture, runtime-boundary, codex-instructions, migration reports | tracked |
| Raw inputs | `01-raw/story-lab/` | Immutable raw inputs + first landing of generated images | skeleton tracked; content ignored |
| Canonical knowledge | `02-wiki/story-lab/` | Canonical Markdown cards (source of truth) | fully tracked |
| Agent work | `50-agent-work/story-lab/` | Operational records: runs, compiled prompts, lint, QA, review forms, repair notes | skeleton tracked; content ignored |
| Archive | `90-archive/story-lab/` | Rejected / deprecated / retired / legacy material | skeleton tracked; content ignored |
| Runtime tool layer | `runtime/` | Validator / compiler / linter / QA helper + caches | source tracked; `.runs/` + `.artifacts/` ignored |

---

## 2. From user story to final illustrated package: full flow

```
USER STORY
  │
  ▼
[A] Raw Story Intake ──► 01-raw user story + StoryProject card (02-wiki)
  │  (Human Gate: copyright/adaptation boundary)
  ▼
[B] Story Analysis ──► story core, graph, page-count, technique plan (runtime analyzers)
  │  (Human Gate: story-core & page-count confirmed)
  ├──────────────┐
  ▼              ▼
[C] Character &  [D] Visual Style &
   Scene          PromptRecipe
   cards          cards
  │  (Human:      (Human: visual style signed off)
  │   canon signed off)
  └──────┬───────┘
         ▼
[E] ImageExecutionPackage (the ONLY entry that creates a package)
  │  (Human Gate 1: plan/package reviewed)  ──► uses [F] internally
  ▼
[F] Prompt Compile + Semantic Lint (HARD GATE: no compiled_prompt → no image)
  │  ──► compiled-prompt + semantic-lint records (50-agent-work)
  ▼
[G] WebGPTImage Manual Handoff
  │  (Human Gate 2: release to generate)
  │  ──► controlled execution sheet → WebGPTImage window → raw candidates → 01-raw/generated-raw
  ▼
[H] GenerationRun Backfill ──► GenerationRun card + image-review-form (50-agent-work)
  ▼
[I] Image QA & Repair (HARD: mandatory human review)
  │  ├─ pass    → [J]
  │  ├─ rework  → RepairNote → back to E/F/G (regenerate; never edit the candidate)
  │  └─ reject  → 90-archive/rejected-assets
  ▼
[J] ReferenceAsset Acceptance
  │  (Human Gate 3: asset accepted; trio = telemetry + image review + asset QA)
  │  ──► accepted ReferenceAsset card (02-wiki/reference-assets)
  ▼   (loop E→J per required asset until accepted_asset_count >= required_asset_count)
[K] Final Illustrated Story Package Assembly
  │  (Human: approval before final_package_status: ready)
  │  ──► StoryProject Final Package section + assembly record
  ▼
[L] Publishing Readiness
     (Human: full read + final publishing sign-off)
     ──► publishing_readiness_status: ready
```

R00/R01/R02/S dependency ordering runs **inside** the E→J loop: the **R00 paper/brushstroke anchor must be accepted first**; R01 (character) / R02 (scene-prop) / S (source illustration) packages that depend on it are blocked until R00 is accepted.

---

## 3. A–L workflow walkthrough

All workflow files live in `02-wiki/story-lab/80-skills-tools-workflows/workflows/`. Runtime commands below are the bare subcommand names exactly as the workflow frontmatter lists them; the full invocation form is `python runtime/aistory.py <subcommand> ...` (only workflow A spells out the full form in its body).

### A. Raw Story Intake Workflow
- **File:** `A-Raw-Story-Intake-Workflow.md`
- **Purpose:** Admit a user story as an immutable raw input and initialize the StoryProject card.
- **Trigger:** User provides a new story (genre, target platform, copyright boundary) in the WebGPT window.
- **Required inputs:** Story text, copyright boundary, target platform.
- **Human decision point:** Copyright-and-adaptation-boundary confirmation. No confirmation → no StoryProject.
- **Runtime commands:** `status`.
- **Canonical cards:** StoryProject created at `02-wiki/story-lab/10-projects/<project-id>.md`; registered in `90-indexes-zh/project-index.md`. `source_paths` points back to the raw input.
- **Operational records:** none.
- **Output paths:** `01-raw/story-lab/user-inputs/<project-id>/` (immutable); `02-wiki/story-lab/10-projects/<project-id>.md`.
- **Stop condition:** StoryProject created + project registered.
- **Failure condition:** No legitimate input, or copyright boundary not confirmed → block.
- **Next:** B. (Codex instruction: `START_NEW_STORY_OBSIDIAN_WIKI.md`.)

### B. Story Analysis and Canonical Card Workflow
- **File:** `B-Story-Analysis-and-Canonical-Card-Workflow.md`
- **Purpose:** Diagnose story core, story graph, story type, and page-count reasonableness; produce a technique plan that drives C and D.
- **Trigger:** StoryProject card exists.
- **Required inputs:** StoryProject card + raw input.
- **Human decision point:** Confirm story-core and page-count conclusions.
- **Runtime commands:** `analyze-story`, `analyze-graph`, `classify-story`, `estimate-pages`, `check-graph`.
- **Canonical cards:** StoryProject "Story Core" / "Production Status" sections updated.
- **Operational records:** diagnostic records (recommended_skill_plan / repair_priority) under `50-agent-work/story-lab/runs/`.
- **Output paths:** StoryProject sections (`02-wiki`); `50-agent-work/story-lab/runs/`.
- **Stop condition:** Story core + page-count confirmed; C and D triggered.
- **Failure condition:** `story_analyzer` high risk (stops at `story_analyzer_gate`), or unreasonable page count / coherence → rework the story graph.
- **Next:** C **and** D (fan-out).

### C. Character and Scene Extraction Workflow
- **File:** `C-Character-and-Scene-Extraction-Workflow.md`
- **Purpose:** Decompose the stable story graph into independently maintainable Character and Scene cards.
- **Trigger:** B complete, story graph stable.
- **Required inputs:** StoryProject + stable story graph.
- **Human decision point:** Sign-off that extracted character/scene canon matches the graph with no omissions/conflicts.
- **Runtime commands:** none (human extraction; B's analysis assists).
- **Canonical cards:** Character cards at `02-wiki/story-lab/30-characters/<character-id>.md` (`visual_lock`, `forbidden_changes`); Scene cards at `02-wiki/story-lab/40-scenes/<scene-id>.md` (`characters`, `props`, `continuity_constraints`); StoryProject Characters/Scenes sections updated.
- **Operational records:** none.
- **Output paths:** `30-characters/`, `40-scenes/`, StoryProject card.
- **Stop condition:** Character/scene canon reviewed and signed off.
- **Failure condition:** Missing story graph or character/scene conflict → return to B.
- **Next:** D.

### D. Visual Style and PromptRecipe Workflow
- **File:** `D-Visual-Style-and-PromptRecipe-Workflow.md`
- **Purpose:** Define one unified VisualStyle and settle reusable PromptRecipe cards (with `recipe_hash` + `drift_check_policy`) for packages to bind.
- **Trigger:** C complete, character/scene cards ready.
- **Required inputs:** StoryProject, Character, Scene cards.
- **Human decision point:** Visual-style sign-off (sets the whole visual tone).
- **Runtime commands:** none (definition stage; compile/lint happen in F).
- **Canonical cards:** VisualStyle at `02-wiki/story-lab/50-visual-styles/<visual-style-id>.md` (`related_recipes`); PromptRecipe at `02-wiki/story-lab/60-prompts/<prompt-recipe-id>.md` (`applicable_asset_types`, `recipe_hash`, `drift_check_policy`, negative-prompt rules). PromptRecipe must **not** contain a specific execution's real prompt instance.
- **Operational records:** none.
- **Output paths:** `50-visual-styles/`, `60-prompts/`.
- **Stop condition:** VisualStyle + PromptRecipe created, style signed off, cross-refs registered.
- **Failure condition:** Style not signed off, or technique mixed with execution → block.
- **Next:** E.

### E. ImageExecutionPackage Creation Workflow
- **File:** `E-ImageExecutionPackage-Creation-Workflow.md`
- **Purpose:** Combine scene/character/style/recipe/reference-asset into one executable, verifiable ImageExecutionPackage — the controlled object later handed to WebGPTImage. **This is the only entry point in the system allowed to create an execution package.**
- **Trigger:** D complete; a target asset needs an image.
- **Required inputs:** Scene, Character, VisualStyle, PromptRecipe cards; applicable accepted ReferenceAsset (anchor) when relevant.
- **Human decision point:** Review package contents (allowed/forbidden content, dependencies, R00 policy) before `status: ready`. **(Approval Gate 1 — plan/package approved.)**
- **Runtime commands:** `compile-asset`, `lint-asset` (delegates to F).
- **Canonical cards:** ImageExecutionPackage at `02-wiki/story-lab/70-execution-packages/<package-id>.md` (one `.md` per package). Binds `scene_id`, `characters`, `visual_style`, `prompt_recipe`; fills `allowed_content` / `forbidden_content`; declares `required_reference_assets`, `prohibited_reference_assets`; R00 overload protection via `r00_dependency_policy` and `maximum_anchor_reuse_policy`. Status flips `draft → ready`.
- **Operational records:** compile/lint records produced in F.
- **Output paths:** `70-execution-packages/<package-id>.md`.
- **Stop condition:** compile + semantic lint pass **and** human review done → `status: ready`.
- **Failure condition:** Dependency card missing, R00 dependency not declared, or compile/lint not passed → must not become `ready`.
- **Next:** F. (Codex instruction: `CREATE_IMAGE_EXECUTION_PACKAGE.md`.)

### F. Prompt Compile and Semantic Lint Workflow
- **File:** `F-Prompt-Compile-and-Semantic-Lint-Workflow.md`
- **Purpose:** Compile the visual-asset ontology into a `compiled_prompt` and run semantic lint as a **hard gate** before any generation.
- **Trigger:** Inside E, after the package binds its ontology and before `status: ready`.
- **Required inputs:** ImageExecutionPackage + visual-asset ontology.
- **Human decision point:** none (automatic; human review is in E).
- **Runtime commands:** `compile-asset`, `lint-asset`, `lint-prompt`.
- **Canonical cards:** ImageExecutionPackage updated with `recipe_hash` comparison (recipe-drift detection); on pass, return to E to set `ready`.
- **Operational records:** `compiled_prompt` → `50-agent-work/story-lab/compiled-prompts/`; semantic-lint result → `50-agent-work/story-lab/semantic-lint-results/`.
- **Output paths:** the two record folders above.
- **Stop condition:** Semantic lint passes → return to E for `ready`.
- **Failure condition (hard-fail):** R00 containing people / stick figures / full scene / prop collection / scattered-symbol table; P01 not 9:16; missing `visual_center` / `paper_policy` / `style_policy`; author-style instruction; lint hard-fail; recipe drift. **Rule: no `compiled_prompt` → no image generation.**
- **Next:** G.

### G. WebGPTImage Manual Generation Handoff Workflow
- **File:** `G-WebGPTImage-Manual-Generation-Handoff-Workflow.md`
- **Purpose:** Turn a `ready` package into a controlled manual execution sheet, hand it to a separate WebGPTImage window for single-image generation, and bring candidates + execution facts back.
- **Trigger:** F passed; package `status: ready`.
- **Required inputs:** ImageExecutionPackage (ready) + lint-passed `compiled_prompt`.
- **Human decision point:** The external execution point — operator generates in the WebGPTImage window, constrained to not improvise outside the sheet. **(Approval Gate 2 — release to generate.)**
- **Runtime commands:** none (runtime never generates; telemetry validation happens in H).
- **Canonical cards:** none (this workflow never marks anything accepted).
- **Operational records:** execution-fact draft (passed to H), recording `actual_prompt_sent_to_external_tool`, tool, model, params.
- **Output paths:** candidate images → `01-raw/story-lab/generated-raw/<project-id>/` (binaries not in git, path-referenced); execution-fact draft → H.
- **Stop condition:** Candidates landed + execution facts recorded → H.
- **Failure condition:** No controlled execution sheet, improvising outside the package, or actual prompt not recorded → block.
- **Next:** H.

### H. GenerationRun Backfill Workflow
- **File:** `H-GenerationRun-Backfill-Workflow.md`
- **Purpose:** Record execution facts of one real generation as a GenerationRun card, validate telemetry, and generate the manual image-review form.
- **Trigger:** G returns candidate images + execution facts.
- **Required inputs:** candidate images + execution facts (actual prompt, tool, params).
- **Human decision point:** none (backfill; human review is in I).
- **Runtime commands:** `validate-telemetry`, `generate-image-review-form`.
- **Canonical cards:** ImageExecutionPackage updated — run registered in `generation_run_ids` / `last_run`. (GenerationRun itself is an operational record, `canonical: false`.)
- **Operational records:** GenerationRun at `50-agent-work/story-lab/runs/<run-id>.md` (`package_id`, `model`, `output_candidates`, actual-prompt source); image-review-form at `50-agent-work/story-lab/image-review-forms/<id>.json` (awaiting manual fill).
- **Output paths:** `runs/`, `image-review-forms/`.
- **Stop condition:** Telemetry validated + review form generated; run registered on the package.
- **Failure condition:** No `actual_prompt_sent_to_external_tool` or telemetry missing → block. **Rule: no telemetry → no acceptance.**
- **Next:** I. (Codex instruction: `BACKFILL_GENERATION_RUN.md`.)

### I. Image QA and Repair Workflow
- **File:** `I-Image-QA-and-Repair-Workflow.md`
- **Purpose:** Mandatory human image review + asset QA; issue accept / reject / rework; protect downstream dependencies.
- **Trigger:** H produced a GenerationRun + image-review-form.
- **Required inputs:** GenerationRun + unfilled image-review-form + candidate images.
- **Human decision point:** **Mandatory human image review** — operator fills each `actual_answer` with evidence; the model cannot auto-pass. This is the accept/reject/rework judgment.
- **Runtime commands:** `validate-image-review`, `merge-image-qa`, `qa-asset`.
- **Canonical cards:** none here (decisions flow to J).
- **Operational records:** `asset_qa_result` (via `merge-image-qa`) → `50-agent-work/story-lab/qa-results/`; RepairNote on fail/rework → `50-agent-work/story-lab/repair-notes/<repair-note-id>.md`.
- **Output paths:** `qa-results/`, `repair-notes/`, and `90-archive/story-lab/rejected-assets/` on reject.
- **Stop condition:** A decision is reached — **pass** → J; **fail/rework** → RepairNote, return to E/F/G to regenerate (never edit the candidate); **reject** → archive candidate + records.
- **Failure condition:** No human review, or continuing R01/R02/S while R00 is not yet accepted → block. `pending` / `fail` / wrong-ratio / missing-telemetry may never be accepted.
- **Next:** J (only when `decision == pass`). (Codex instruction: `REPAIR_FAILED_IMAGE_RUN.md`.)

### J. ReferenceAsset Acceptance Workflow
- **File:** `J-ReferenceAsset-Acceptance-Workflow.md`
- **Purpose:** Promote a QA-passed candidate into an accepted ReferenceAsset canonical card; close the traceable chain.
- **Trigger:** I returned `decision == pass`.
- **Required inputs:** the **three-piece set** — GenerationRun (telemetry) + image-review-form (human review) + asset_qa_result. None may be missing.
- **Human decision point:** Human acceptance sign-off (`accepted_by` + `accepted_at`). **(Approval Gate 3 — asset accepted.)**
- **Runtime commands:** `register-image-qa-artifact`, `artifact-validate`, `artifact-lineage`.
- **Canonical cards:** ReferenceAsset at `02-wiki/story-lab/reference-assets/<reference-asset-id>.md` (`status: candidate → accepted`; fills `source_generation_run`, `source_image_review_form`, `source_asset_qa_result`, `accepted_by`/`accepted_at`, `allowed_usage`/`forbidden_usage`, and `r00_anchor_scope` if R00). StoryProject `accepted_asset_count` backfilled. ImageExecutionPackage `output_assets` updated.
- **Operational records:** none new (consumes existing; runs artifact validate/lineage against the derived-cache registry).
- **Output paths:** `reference-assets/<reference-asset-id>.md`; StoryProject update.
- **Stop condition:** Three-piece set validated + human acceptance → card `accepted`.
- **Failure condition:** Any of the three pieces missing, or no human acceptor → block, stays `candidate`. Rejected/deprecated assets may never serve as dependencies.
- **Next:** K. (Codex instruction: `ACCEPT_REFERENCE_ASSET.md`.) Loop E→J per required asset.

### K. Final Illustrated Story Package Assembly Workflow
- **File:** `Final Illustrated Story Package Assembly Workflow.md` (no `K-` filename prefix; frontmatter `id: Final-Illustrated-Story-Package-Assembly-Workflow`).
- **Purpose:** When all required accepted assets are ready, assemble them + the story text layer into a complete illustrated-story package plan.
- **Trigger:** `accepted_asset_count >= required_asset_count`.
- **Required inputs:** StoryProject + all Scene/Character/VisualStyle/PromptRecipe/ImageExecutionPackage cards; all accepted ReferenceAssets + their GenerationRun + QA results (+ RepairNote if reworked).
- **Human decision point:** Human approval before `final_package_status: ready`.
- **Runtime commands:** `artifact-check-registry`, `artifact-lineage`.
- **Canonical cards:** StoryProject "Final Package" section gets the canonical assembly plan (per-page/per-scene mapping of accepted ReferenceAssets + story text); `final_package_status: assembling → ready` (after approval).
- **Operational records:** assembly operation record (page order, asset mapping, versions) → `50-agent-work/story-lab/runs/`.
- **Output paths:** StoryProject Final Package section; `50-agent-work/story-lab/runs/`. Image binaries excluded from git; package expressed as card + path-reference table.
- **Stop condition:** All required assets QA-passed, count satisfied, plan written, human approval → `final_package_status: ready`.
- **Failure condition:** Required asset not QA-passed, count insufficient, or missing readiness check → block.
- **Next:** L. (Codex instruction: `ASSEMBLE_FINAL_ILLUSTRATED_STORY_PACKAGE.md`; map: `maps/final-illustrated-story-package-map.md`; checklist: `acceptance-checklists/Final Illustrated Story Package Readiness Checklist.md`.)

### L. Publishing Readiness Workflow
- **File:** `L-Publishing-Readiness-Workflow.md`
- **Purpose:** Run the publishing-readiness checklist + a full human read; issue the final publishing decision.
- **Trigger:** K set `final_package_status: ready`.
- **Required inputs:** StoryProject final-package plan + all accepted assets.
- **Human decision point:** Full human read + final publishing sign-off (checks mis-ordering, occlusion, breakage, publishing risk).
- **Runtime commands:** none (`status` optional re-check only).
- **Canonical cards:** StoryProject `publishing_readiness_status: ready` + final publishing decision recorded.
- **Operational records:** readiness check record → `50-agent-work/story-lab/qa-results/`.
- **Output paths:** `qa-results/`; StoryProject update.
- **Stop condition:** Checklist passes, no blockers, human read passes → `publishing_readiness_status: ready`.
- **Failure condition:** Human read fails or blockers exist → block publishing.
- **Next:** none — terminal workflow.

---

## 4. Output inventory by layer

For a hypothetical project `<project-id>`, a real pilot creates the following. Folders marked *(skeleton-only in git)* have their content gitignored — the files exist locally but are not committed.

### 01-raw *(skeleton-only in git)*
- Original user story: `01-raw/story-lab/user-inputs/<project-id>/` (immutable, never rewritten).
- Reference inputs (if any): `01-raw/story-lab/reference-inputs/`.
- Generated raw image candidates (from WebGPTImage): `01-raw/story-lab/generated-raw/<project-id>/` — candidates land **here first**.
- (Also available: `screenshots/`, `model-raw-outputs/`.)

### 02-wiki *(fully tracked / committed)*
- StoryProject card: `02-wiki/story-lab/10-projects/<project-id>.md`.
- Character cards: `02-wiki/story-lab/30-characters/<character-id>.md`.
- Scene cards: `02-wiki/story-lab/40-scenes/<scene-id>.md`.
- VisualStyle cards: `02-wiki/story-lab/50-visual-styles/<visual-style-id>.md`.
- PromptRecipe cards: `02-wiki/story-lab/60-prompts/<prompt-recipe-id>.md`.
- ImageExecutionPackage cards: `02-wiki/story-lab/70-execution-packages/<package-id>.md`.
- ReferenceAsset cards (after acceptance): `02-wiki/story-lab/reference-assets/<reference-asset-id>.md`.
- Final illustrated story package plan: the **"Final Package" section of the StoryProject card** (not a separate file).
- Publishing readiness canonical decision: `publishing_readiness_status` + final decision in the StoryProject card.

### 50-agent-work *(skeleton-only in git)*
- Runtime/diagnostic run records: `50-agent-work/story-lab/runs/`.
- Compiled prompt record: `50-agent-work/story-lab/compiled-prompts/`.
- Semantic lint result: `50-agent-work/story-lab/semantic-lint-results/`.
- WebGPTImage execution sheet: assembled in workflow G from the package + `compiled_prompt`; staged under `50-agent-work/story-lab/runs/` (or the package's defined handoff location) — see §6.2.
- GenerationRun record: `50-agent-work/story-lab/runs/<run-id>.md`.
- Image review form: `50-agent-work/story-lab/image-review-forms/<id>.json`.
- Asset QA result: `50-agent-work/story-lab/qa-results/<id>.md`.
- RepairNote: `50-agent-work/story-lab/repair-notes/<repair-note-id>.md`.
- Final assembly operational record: `50-agent-work/story-lab/runs/`.
- Publishing readiness operational record: `50-agent-work/story-lab/qa-results/`.

### 90-archive *(skeleton-only in git)*
- Rejected image candidates: `90-archive/story-lab/rejected-assets/`.
- Deprecated prompt recipes: `90-archive/story-lab/deprecated-prompts/`.
- Retired execution packages: `90-archive/story-lab/retired-execution-packages/`.
- Old/failed runs (if policy archives them): `90-archive/story-lab/old-runs/`.
- Legacy projects: `90-archive/story-lab/legacy-projects/`.

### runtime *(source tracked; caches ignored)*
- `runtime/.runs/` — pipeline run cache, gitignored.
- `runtime/.artifacts/` — Artifact Registry cache, gitignored, rebuildable.
- Validation / lint / QA helper outputs — derived cache; durable conclusions must be **backfilled** into the relevant `02-wiki` card, otherwise they remain disposable.

---

## 5. User operating surfaces

You operate **three surfaces**. Keep their authority strictly separated.

### 5.1 WebGPT command / planning window
- **Purpose:** explain the story; ask for planning; review outputs; make human approval decisions; prepare the WebGPTImage handoff text; evaluate image results.
- **Allowed:** read `02-wiki` cards and `01-raw` material; propose plans, techniques, pacing, structure; flag items needing human approval.
- **Not allowed:** directly touch filesystem execution details (delegates to Codex); directly generate final images; bypass approval gates.

### 5.2 Claude / Codex local execution
- **Purpose:** create files/cards from templates; run runtime validation; compile/lint prompts; backfill GenerationRun, QA, RepairNote, ReferenceAsset; keep the repository clean.
- **Allowed:** read/write the local filesystem; call runtime `validate` / `lint` / `compile` / `qa`; cut the controlled execution sheet for the WebGPTImage window; file raw outputs, telemetry, QA, repair records into `01-raw` / `50-agent-work`.
- **Not allowed:** call any external image tool (it **stops at the human execution point**); create story projects or generate images on its own; skip upstream gates; treat derived cache as a second source of truth.

### 5.3 WebGPTImage generation window
- **Purpose:** consume only the controlled manual execution sheet; generate one requested `image_id` / package at a time; return candidates.
- **Allowed:** receive one controlled execution sheet; generate single candidate image(s) per that sheet.
- **Not allowed:** see the whole repository; read the canonical knowledge base or other projects; batch/auto-generate; improvise project facts; decide acceptance.

### 5.4 Who does what, when

| Phase | WebGPT planning | Codex local | WebGPTImage |
| --- | --- | --- | --- |
| A intake | explains story, confirms copyright | lands raw input, creates StoryProject | — |
| B analysis | confirms core/page-count | runs analyzers, updates cards | — |
| C/D cards | reviews & signs off canon/style | creates Character/Scene/VisualStyle/PromptRecipe | — |
| E package | reviews package (Gate 1) | creates ImageExecutionPackage | — |
| F compile/lint | — | runs compile-asset / lint-asset / lint-prompt | — |
| G handoff | approves release (Gate 2) | cuts the controlled execution sheet | generates single candidate |
| H backfill | — | validates telemetry, makes GenerationRun + review form | — |
| I QA/repair | **fills review form, decides** | runs validate-image-review / merge-image-qa / qa-asset; writes RepairNote | — |
| J acceptance | signs off acceptance (Gate 3) | writes ReferenceAsset, backfills counts | — |
| K assembly | approves final package | writes Final Package section + assembly record | — |
| L publishing | full read + final sign-off | runs readiness record | — |

---

## 6. How to use WebGPTImage

This section is the controlled-handoff protocol. **No real prompt is produced here** — only the procedure and a placeholder protocol (the fillable template is §7).

### 6.1 Which artifact is copied into WebGPTImage?
The **controlled manual execution sheet** derived from a single `ready` ImageExecutionPackage, **after** prompt compile and semantic lint pass. Nothing else.

### 6.2 Where does this artifact live?
It is assembled by Codex in workflow G from:
- the ImageExecutionPackage card `02-wiki/story-lab/70-execution-packages/<package-id>.md`, and
- the lint-passed `compiled_prompt` under `50-agent-work/story-lab/compiled-prompts/`.

The cut sheet is staged under `50-agent-work/story-lab/runs/` (workflow G's handoff output location). It is a derived artifact; the canonical facts remain in the package + compiled-prompt records.

### 6.3 What the WebGPTImage window must receive
Only the controlled fields (full fillable form in §7): `project_id`, `image_id`, `package_id`, target asset type, canvas ratio, allowed content, forbidden content, visual-style constraints, reference-asset bindings, the actual prompt, the negative prompt, generation count, return requirements, and the do-not-improvise rules.

### 6.4 What must NOT be sent to WebGPTImage
- The full private project wiki (if not needed).
- Unrelated story facts.
- Unapproved references.
- Rejected or deprecated assets.
- Vague style requests.
- Multiple conflicting image targets in one sheet.
- Any accept/reject decision authority.

### 6.5 What the user pastes back after candidates return
- Candidate files or links.
- The actual generated result description.
- Tool / model / settings, if available.
- Visible failures.
- User judgment notes.
(Structured form in §8.)

### 6.6 What happens after candidate images return
1. Candidates first land in `01-raw/story-lab/generated-raw/<project-id>/`.
2. A GenerationRun is created in `50-agent-work/story-lab/runs/` (workflow H).
3. The image review form is filled (workflow I; human, with evidence).
4. An asset QA result is created (`merge-image-qa` → `50-agent-work/story-lab/qa-results/`).
5. A RepairNote is created if needed (`50-agent-work/story-lab/repair-notes/`).
6. An accepted ReferenceAsset card is created **only after QA passes** (workflow J → `02-wiki/story-lab/reference-assets/`).
7. Rejected candidates go to `90-archive/story-lab/rejected-assets/`.

### 6.7 When can an image become an accepted reference?
All of the following must hold:
- A source ImageExecutionPackage.
- A GenerationRun with valid execution telemetry (`actual_prompt_sent_to_external_tool`).
- A completed human image review form.
- An asset QA result that passes.
- No blocking RepairNote.
- `allowed_usage` / `forbidden_usage` recorded.
- `accepted_by` / `accepted_at` recorded.
- If this is an R00 anchor: it must be accepted **before** any R01/R02/S package that depends on it can generate.

### 6.8 The correct loop if the image fails
- **Do not overwrite the candidate.**
- Create a RepairNote.
- Adjust the ImageExecutionPackage or PromptRecipe only if root cause demands it.
- Run compile / lint again (workflow F).
- Create a **new** GenerationRun (new generation, workflows G→H).
- Keep the failed candidate traceable.
- Archive rejected material in `90-archive/story-lab/rejected-assets/`.

---

## 7. WebGPTImage Controlled Handoff Format

> TEMPLATE ONLY — contains no real story prompt. Codex fills these placeholders from one `ready` ImageExecutionPackage + its lint-passed compiled_prompt, then this block (and nothing more) is pasted into the WebGPTImage window.

```
=== WEBGPTIMAGE CONTROLLED HANDOFF ===
PROJECT_ID:                  <project-id>
PACKAGE_ID:                  <package-id>
IMAGE_ID:                    <image-id>
TARGET_ASSET_TYPE:           <R00_PAPER_MARK_ANCHOR | R01_CHARACTER_ANCHOR | R02_SCENE_PROP_ANCHOR | P01_PLATFORM_LAYOUT_SAMPLE | S_SOURCE_ILLUSTRATION>
CANVAS_RATIO:                <e.g. 1:1 | 9:16 — must match the asset type's required canvas>
OUTPUT_COUNT:                <integer, single target>

SOURCE_IMAGE_EXECUTION_PACKAGE:  02-wiki/story-lab/70-execution-packages/<package-id>.md
SOURCE_PROMPT_RECIPE:            02-wiki/story-lab/60-prompts/<prompt-recipe-id>.md
SOURCE_VISUAL_STYLE:            02-wiki/story-lab/50-visual-styles/<visual-style-id>.md
SOURCE_REFERENCE_ASSETS:        [<accepted-reference-asset-id>, ...]   (accepted only)

ALLOWED_CONTENT:             <bullet list from package allowed_content>
FORBIDDEN_CONTENT:           <bullet list from package forbidden_content>
STYLE_CONSTRAINTS:           <from VisualStyle / paper_policy / style_policy>
COMPOSITION_CONSTRAINTS:     <visual_center, framing, occlusion rules>
CHARACTER_CONSTRAINTS:       <visual_lock / forbidden_changes for bound characters>
SCENE_CONSTRAINTS:           <continuity_constraints / props / spatial facts>
TEXT_IN_IMAGE_POLICY:        <e.g. no baked-in narration text; per required_text_policy>

ACTUAL_PROMPT_TO_USE:        <the compiled prompt string — verbatim from compiled_prompt>
NEGATIVE_PROMPT_TO_USE:      <the negative prompt — verbatim from compiled_prompt>

RETURN_REQUIREMENTS:         <candidate file(s)/link(s), the exact prompt used, tool/model/settings>

DO_NOT:
  - Do not change story facts.
  - Do not add unrequested characters.
  - Do not use rejected assets.
  - Do not mark the result accepted.
  - Do not create additional unrequested images.
  - Do not rewrite the execution package.

AFTER_GENERATION_RETURN:     <paste candidates + facts back using the §8 Result Backfill Format>
=== END HANDOFF ===
```

---

## 8. WebGPTImage Result Backfill Format

> TEMPLATE ONLY. After WebGPTImage returns candidates, the user pastes this back into the WebGPT command window or hands it to Claude/Codex. It feeds workflow H (GenerationRun backfill) and workflow I (QA).

```
=== WEBGPTIMAGE RESULT BACKFILL ===
PROJECT_ID:                  <project-id>
PACKAGE_ID:                  <package-id>
IMAGE_ID:                    <image-id>
GENERATION_RUN_ID:           <run-id>            (assigned at backfill, workflow H)
WEBGPTIMAGE_WINDOW:          <which generation window/session>
TOOL_OR_MODEL:               <tool / model name>
ACTUAL_PROMPT_USED:          <verbatim prompt actually sent — required; no value blocks acceptance>
NEGATIVE_PROMPT_USED:        <verbatim negative prompt actually used>
SETTINGS_USED:               <seed / steps / size / sampler / etc., if available>
CANDIDATE_FILES_OR_LINKS:    [01-raw/story-lab/generated-raw/<project-id>/<candidate-id>, ...]
CANDIDATE_COUNT:             <integer>
USER_VISIBLE_DESCRIPTION:    <what the candidate actually shows>
OBVIOUS_FAILURES:            <visible defects, ratio mismatch, forbidden content, drift>
USER_INITIAL_DECISION:       <pass | rework | reject — provisional human read>
REQUESTED_NEXT_ACTION:       <QA | repair | accept | reject | regenerate>
=== END BACKFILL ===
```

---

## 9. First Story Pilot Checklist

**Before starting**
- [ ] Repository clean (`git status` shows clean).
- [ ] Obsidian open on the vault.
- [ ] Dataview / Bases plugins available (optional, for dashboards).
- [ ] WebGPT command window open.
- [ ] WebGPTImage window ready (separate surface).
- [ ] Runtime validation passes (`status` / `validate` / `validate-contracts` / `check-contract-drift` / `smoke-test`).

**Story intake (A)**
- [ ] Raw story saved to `01-raw/story-lab/user-inputs/<project-id>/`.
- [ ] StoryProject card created in `10-projects/`.
- [ ] `project_id` assigned.
- [ ] `source_paths` recorded.
- [ ] Copyright / adaptation boundary confirmed.

**Story planning (B–D)**
- [ ] Story core extracted (`analyze-story`).
- [ ] Characters extracted → `30-characters/`.
- [ ] Scenes extracted → `40-scenes/`.
- [ ] Visual style defined → `50-visual-styles/`.
- [ ] Prompt recipe selected or created → `60-prompts/`.
- [ ] Acceptance gates reviewed.

**Image planning (E–F)**
- [ ] Image target list created.
- [ ] ImageExecutionPackage created → `70-execution-packages/`.
- [ ] Dependency graph checked (`check-graph`).
- [ ] R00 overload rule checked (`r00_dependency_policy`, `maximum_anchor_reuse_policy`).
- [ ] Prompt compiled (`compile-asset`).
- [ ] Semantic lint passed (`lint-asset` / `lint-prompt`).
- [ ] WebGPTImage execution sheet prepared (§7).

**Image generation (G–H)**
- [ ] Paste **only** the controlled sheet into WebGPTImage.
- [ ] Generate only the requested `image_id` / package.
- [ ] Record candidates (§8).
- [ ] Save raw candidates to `01-raw/story-lab/generated-raw/<project-id>/`.
- [ ] Backfill GenerationRun (`validate-telemetry`, `generate-image-review-form`).

**QA and repair (I–J)**
- [ ] Image review form completed (human, with evidence).
- [ ] Asset QA result completed (`merge-image-qa`, `qa-asset`).
- [ ] RepairNote written if failed.
- [ ] Accepted ReferenceAsset created **only if all gates pass**.
- [ ] Rejected candidates archived to `90-archive/story-lab/rejected-assets/`.
- [ ] R00 accepted before any dependent R01/R02/S generates.

**Final package (K–L)**
- [ ] All required scenes have accepted assets (`accepted_asset_count >= required_asset_count`).
- [ ] Final assembly package plan created (StoryProject Final Package section).
- [ ] Publishing readiness checklist passed + full human read done.
- [ ] No binaries committed unless explicitly approved.

---

## 10. Stop conditions and failure loops

**Hard gates that block forward motion**
- A: no copyright confirmation → no StoryProject.
- B: `story_analyzer` high risk or unreasonable page count → rework story graph.
- E: missing dependency card / undeclared R00 dependency / compile-lint not passed → package cannot become `ready`.
- F: **no `compiled_prompt` → no image generation** (hard-fail list in §3-F).
- G: no controlled sheet / improvisation / unrecorded actual prompt → no handoff.
- H: **no telemetry → no acceptance.**
- I: no human review, or R01/R02/S while R00 not accepted → block.
- J: missing any of telemetry + image review + asset QA, or no human acceptor → stays `candidate`.
- K: required asset not QA-passed or count insufficient → no assembly.
- L: human read fails or blockers exist → no publishing.

**Failure loop (image fails QA)**
```
candidate fails (I)
  → write RepairNote (50-agent-work/repair-notes)  [do NOT edit the candidate]
  → if root cause is spec/recipe: adjust ImageExecutionPackage / PromptRecipe
  → re-run compile + semantic lint (F)
  → re-handoff (G) → new GenerationRun (H)  [new run id; old candidate stays traceable]
  → re-QA (I)
  → reject path: archive candidate + records to 90-archive/rejected-assets
```
Rejected / deprecated assets may **never** be reused as a reference dependency.

---

## 11. What gets committed and what does not

| Item | Committed? |
| --- | --- |
| `00-system/` doctrine, `02-wiki/story-lab/` canonical cards | **Yes** — fully tracked source of truth |
| `01-raw/**`, `50-agent-work/**`, `90-archive/**` content | **No** — gitignored; only `README.md` + `.gitkeep` skeleton tracked |
| Binary images (`.png/.jpg/.webp/...`) anywhere | **No** — cards record location + provenance; bytes stay out of git |
| `runtime/` source, `runtime/contracts/`, `runtime/schemas/`, `runtime/tests/` | **Yes** |
| `runtime/.runs/`, `runtime/.artifacts/` | **No** — gitignored derived cache, rebuildable |
| Compiled prompts, semantic lint, QA results, runs (operational records) | **No** — disposable cache; durable conclusions are backfilled into `02-wiki` cards |

Confirmed in `.gitignore`: `runtime/.runs/`, `runtime/.artifacts/` (lines 2–3); `01-raw/**`, `50-agent-work/**`, `90-archive/**` with `!**/README.md` and `!**/.gitkeep` exceptions (lines 22–35). Canonical knowledge (`02-wiki`) and system docs (`00-system`) are explicitly fully tracked.

**Rule:** committing image binaries or treating gitignored cache as truth both violate doctrine. If a binary must be committed, that requires explicit human approval.

---

## 12. Remaining risks

| Risk | Blocks first pilot? |
| --- | --- |
| **Card creation is manual.** Every canonical card is hand-authored from a template; no generator enforces field completeness. | No — workable, but slow and error-prone. Discipline required. |
| **Runtime does not yet validate all 02-wiki cards.** `Runtime-Is-Tool-Layer.md` §7 lists lineage/consistency validators as documented-but-not-implemented (e.g. "required GenerationRun before acceptance," "StoryProject asset-count consistency"). Enforcement is by human gates + workflow design. | No — human gates cover the pilot; automate later for scale. |
| **QA gates rely on human discipline.** Image review forms are filled by humans; the runtime cannot read pixels. A careless reviewer can pass a bad image. | No — but it is the main quality risk; treat the review form as mandatory and evidence-based. |
| **WebGPTImage is a separate manual surface.** No automation links the execution sheet to the generation window; copy/paste is manual and can leak unintended context. | No — follow §7 strictly (paste only the controlled sheet). |
| **Binary/image files are intentionally not committed.** Provenance lives in cards; the bytes can be lost if the local store is not backed up separately. | No — but back up `01-raw/.../generated-raw/` independently. |
| **Bases/Dataview views need Obsidian validation.** Dashboards depend on plugins; queries are unverified against real cards (none exist yet). | No — dashboards are convenience, not gates. |
| **Scale production needs stronger validators.** Manual lineage/acceptance is fine for one story; many stories need the §7 validators implemented. | No for a single pilot; yes before bulk production. |
| **Minor naming inconsistency:** workflow J's downstream pointer cites `workflows/K-Final-Illustrated-Story-Package-Assembly-Workflow.md`, which does not exist; the same line parenthetically gives the real file `Final Illustrated Story Package Assembly Workflow.md`. Self-mitigated, not a broken link. | No — cosmetic; the real file is named in-line. |

None of the listed risks block the first pilot. The first pilot is gated by **human discipline**, not by missing capability.

---

## 13. Final answer

**When I provide a story, what happens?**
The system does not immediately draw. It runs workflow **A** (lands your story immutably in `01-raw/`, creates a StoryProject card in `02-wiki/`, confirms the copyright boundary), then **B** (runtime analyzers diagnose story core, graph, type, page count), then fans out to **C** (Character + Scene cards) and **D** (VisualStyle + PromptRecipe cards). Only then does image production begin.

**What workflows are used?**
The full A–L chain: **A** intake → **B** analysis → **C**/**D** extraction & style → **E** ImageExecutionPackage (the only package-creation entry) → **F** compile + semantic lint (hard gate) → **G** WebGPTImage handoff → **H** GenerationRun backfill → **I** image QA & repair → **J** ReferenceAsset acceptance (loop E→J per asset) → **K** final package assembly → **L** publishing readiness. Three human approval gates sit at E (plan), G (release), and J (accept), with a final read at L.

**What files/cards are produced?**
Canonical (committed, `02-wiki`): StoryProject (`10-projects/`), Character (`30-characters/`), Scene (`40-scenes/`), VisualStyle (`50-visual-styles/`), PromptRecipe (`60-prompts/`), ImageExecutionPackage (`70-execution-packages/`), ReferenceAsset (`reference-assets/`), plus the StoryProject's Final Package section and `publishing_readiness_status`. Operational (gitignored, `50-agent-work`): compiled prompts, semantic-lint results, GenerationRun records, image-review-forms, asset-QA results, RepairNotes, assembly + readiness records. Raw (gitignored, `01-raw`): your original story and the generated candidates. Rejected material (gitignored, `90-archive`).

**What do I copy into WebGPTImage?**
Only the **controlled manual execution sheet** (§7), derived by Codex from one `ready` ImageExecutionPackage **after** its prompt compiled and passed semantic lint. Never the wiki, never extra story facts, never rejected assets, never acceptance authority.

**What do I paste back after WebGPTImage returns images?**
The **Result Backfill block** (§8): project/package/image ids, the actual prompt + negative prompt + settings used, candidate files/links, candidate count, a description, obvious failures, your initial decision, and the requested next action. The `ACTUAL_PROMPT_USED` is mandatory — without it, acceptance is blocked.

**When is an image accepted?**
Only when the full three-piece evidence set exists and passes: execution telemetry (GenerationRun) + human image review form + asset QA result, with no blocking RepairNote, with `allowed_usage`/`forbidden_usage` and `accepted_by`/`accepted_at` recorded — and, for an R00 anchor, accepted before any dependent R01/R02/S generates. Acceptance is a **human** decision (Gate 3), written into a ReferenceAsset card in `02-wiki/`.

**What is produced at the end?**
A canonical **illustrated-story package plan** in the StoryProject card's Final Package section (accepted ReferenceAssets mapped to pages/scenes + the story text layer), an assembly record in `50-agent-work/`, and a `publishing_readiness_status: ready` final decision after the full human read. Image binaries are referenced by path and provenance, not committed.

---

*End of manual. This report is read-only analysis; it created no real story, card, prompt, or image, and remains uncommitted.*
