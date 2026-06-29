---
type: visual_style
id: "vs-pilot-001-child-horror-notebook"
title_zh: pilot-001 儿童手绘怪谈作业本风格
title_en: pilot-001 Child-Drawn Horror Notebook Style
status: draft
project_id: "pilot-001"
reference_assets: []
related_recipes:
  - pr-pilot-001-child-horror-notebook
related_assets: []
source_paths: []
tags:
  - story-lab
  - pilot-001
  - visual-style
  - child-horror-notebook
  - supernatural-allowed
created_at: 2026-06-26
updated_at: 2026-06-26
owner: ichichuang
version: v0
canonical: true
---

# pilot-001 儿童手绘怪谈作业本风格 / Child-Drawn Horror Notebook Style

> Clean active VisualStyle for `pilot-001` GPTImage production (visual pipeline reset 2026-06-26). This card defines visual rules only — it does not generate images, create execution packages, create ReferenceAssets, or authorize a GPTImage handoff. `status: draft` because the VisualStyle schema has no `accepted`/`active`. An earlier warm-safe night-picture-book visual system was removed from the project; its failed p01 manual attempt is not accepted and must never be used as a reference.

## Production Gate / 生产门禁

Active visual system for `pilot-001` clean GPTImage production-handoff preparation. Defines drawing method and atmosphere only. Image generation stays **manual and blocked** until a human operator uses the clean GPTImage prompt; this card authorizes no automated image generation, GenerationRun, ReferenceAsset, or final package.

## Style Summary / 风格概要

像 9–12 岁小孩在横线作业本上画下的"怪谈记录页"。粗糙的黑色铅笔/圆珠笔线条、彩铅与蜡笔涂色、可见橡皮擦痕、红笔圈选与问号、箭头、少量幼稚的手写中文标题。纸面有折痕、压痕、污点、边角磨损、轻微发黄的旧纸/扫描质感。透视不准、比例幼稚，家具和人物像孩子画出来的，但画面内容带有怪谈、灵异、未解释的气氛。**恐怖来自"孩子画出来的吓人"，不是写实恐怖片。**

A page from a 9–12-year-old child's "scary-story notebook." Rough black pencil/ballpoint outlines, colored-pencil and crayon fill, visible eraser marks, red-pen circles and question marks, arrows, a little childish Chinese handwriting. The paper shows creases, pressure marks, smudges, worn corners, and a faintly yellowed old / scanned look. Perspective is off, proportions are childish, furniture and people look hand-drawn by a kid — but the content carries a creepy, supernatural, partly-unexplained folk-tale mood. **The fear is "scary as a child would draw it," not a realistic horror film.**

## Visual System Scope / 视觉系统职责边界

> **Style is reusable; story content is variable. This visual system controls drawing method and atmosphere only. It must not inject wardrobes, door gaps, eyes, ghosts, or any example motif unless the current package asks for them.**

**Style is reusable; story content is variable.** This visual system controls **drawing method and atmosphere only** — paper, line quality, childish drawing, red-pen annotation behavior, the creepy notebook mood, and supernatural *permission*. It must **not** overwrite scene content and must **not** hard-code any fixed set of horror motifs as mandatory content.

For every generated image, the strange event, location, characters, props, and emotional beat must come from the approved `ImageExecutionPackage` (and the canonical StoryProject / Scene / Character cards it binds). The visual system never injects its own scene events; each compiled image renders only the specific scene event approved for that package.

**Series continuity (serialized production).** Once a p01 image is accepted, it is the series master anchor: every later page must match it on style, paper, line quality, red-pen annotation language, matte texture, square format, character design, and proportions — only the scene event changes per page. See the project card's "Series Continuity & Master Anchor" section and the recipe's "Series Continuity Prefix." (No image is accepted yet; the anchor activates only on a genuine acceptance — never a failed candidate.)

风格可复用，故事内容可变。本视觉系统**只**控制绘制方法与气氛（纸张、线条、儿童手绘、红笔批注方式、作业本怪谈氛围、超自然「许可」），**不得**覆盖场景内容，**不得**把任何一组固定怪谈母题写成强制内容。每张图的奇异事件、地点、角色、道具与情绪节拍，都必须来自获批的 `ImageExecutionPackage`（及其绑定的 StoryProject / Scene / Character 规范卡）。视觉系统绝不自行注入场景事件；每张编译出的图只渲染其执行包获批的那一个具体场景事件。

## Mandatory Positive Style Core / 强制正向风格核心

Bind this verbatim as the positive style anchor in every compiled prompt for this project:

> Chinese child-drawn horror notebook page, lined school notebook paper, rough pencil and ballpoint outlines, colored-pencil and crayon fill, visible eraser marks, red pen circles and arrows, childish Chinese handwriting, uneven proportions, imperfect hand-drawn perspective, matte scanned paper texture, creepy but child-drawn, supernatural mystery atmosphere, one clear strange event on the page.

## Mandatory Negative Style Core / 强制负向风格核心

Bind this verbatim as the negative style anchor in every compiled prompt for this project:

> no polished digital illustration, no commercial picture book finish, no fantasy animal characters, no anthropomorphic hedgehogs, no plush mascots, no 3D, no cinematic realism, no oil painting, no photorealism, no glossy gradients, no perfectly clean line art, no cute fairy tale animal cast, no over-rendered AI storybook style, no platform text, no prompt text.

注意：负向核心**不包含** "no supernatural" 与 "no horror / low fear"。禁止把"无超自然"或"低恐怖"写成全局规则（见 Forbidden Style Drift）。

## Line Quality / 线条

- 粗糙的黑色铅笔与圆珠笔线条；线条可以歪、抖、不准、幼稚，允许重复描线、涂改与橡皮痕。
- 允许铅笔、圆珠笔、彩铅、蜡笔、水彩、水粉混合痕迹同时出现在一页上。
- 不要光滑、对称、干净的矢量/数字线稿；不要专业插画师的精修描边。
- 人物可以有火柴人倾向，但不能退化成极简空白符号表——必须有儿童画的丰富度（衣服、表情、道具、涂色）。
- 角色身份必须清楚可读（谁是小孩、谁是大人、谁是怪东西），即使手脚比例不准、线条歪斜。

## Color Rules / 配色

- 彩铅、蜡笔、淡水彩/水粉的儿童涂色质感；允许涂出边界、留白、压重笔触。
- 红笔（圈选、问号、箭头、批注）是这套风格的标志性元素，鼓励使用，但不得拼出可读的长句正文。
- 旧作业纸的轻微发黄、灰蓝铅笔阴影、夜色的脏黑/深蓝都允许；黑暗、门缝里的纯黑、窗外的夜都允许。
- 不要电影级打光、glossy 渐变、高饱和商业绘本配色、3D 高光。

## Texture Rules / 材质

- 横线作业本纸或旧作业纸背景；纸面允许折痕、压痕、污点、边角磨损、订书孔、扫描噪点、轻微发黄。
- 哑光扫描纸质感（matte scanned paper），像把作业本平铺扫描或翻拍。
- 禁止照片写实、油画厚涂、3D 渲染、影视质感、glossy 数字光泽、过度 AI 渲染的绘本光感。
- 最终观感必须像"纸上手绘后被扫描"，而不是"屏幕里生成的精致插画"。

## Composition Rules / 构图

- 像儿童怪谈记录页：一个清晰的主要怪事画面 + 少量箭头/问号/红圈提示。
- 允许单图加批注的"作业本一页"布局；允许歪斜边框、随手画的分隔线。
- 透视可以不准、家具可以画歪、地面可以飘；这是特征不是缺陷。
- 不要专业绘本的居中精致构图、电影分镜感、写实景深。
- 可以出现少量幼稚手写中文标题（2–12 字短句）作为画内手写，而非排版文字。标题内容必须来自当前 `ImageExecutionPackage` / Scene 获批的具体事件；**不得**套用固定母题示例（如"衣柜在说话。""门缝里有东西。"——这些仅为示例，见「Example Motifs Only / 仅作示例的母题」），除非当前故事/包确有该内容。

## Content Safety Rules / 内容安全

本节是内容安全边界，**不是**降低恐怖或禁止超自然的规则。

- 允许（可用范围）：超自然、灵异、鬼怪、未知东西、未解释/半解释的民间怪谈气氛。
- 允许的具体奇异元素（**仅为示例，非必需内容**）：衣柜说话、门缝里的黑暗、夜里的窗户、桌下/床下/柜子里传来的声音、模糊影子、奇怪眼睛、红圈标注的异常处等，都只是「Example Motifs Only / 仅作示例的母题」中的示例，用于说明这套风格*能*画哪类怪事。**不得**在当前故事/包没有要求时注入画面；每张图的实际奇异事件必须来自获批的 `ImageExecutionPackage`。
- 允许：小孩害怕、发抖、疑惑、躲在灯旁等情绪表现。
- 仍然禁止（硬性内容安全线）：
  - 露骨血腥 gore、写实尸体。
  - 真实虐童、对儿童的严重身体伤害或明显创伤折磨的描绘。
  - 性内容、成人色情。
  - 真实犯罪案件细节复刻、令人误以为真实案件证据照的摄影写实风。
  - 任何平台 UI、prompt 文本、image id、WebGPTImage 说明文字出现在画面中。
- 恐怖强度定位："儿童画出来的吓人"。可以诡异、不安、灵异，但通过儿童手绘的笨拙与红笔批注表达，而非写实恐怖摄影。

## Character Rules / 角色规则

- 如果故事角色是人类，必须画成人类，**不得动物化**。
- 小孩可以画得幼稚、像儿童涂鸦里的人，但不能变成动物、玩偶、吉祥物、刺猬、小熊、小兔等替代角色。
- 允许火柴人倾向与不准的手脚、歪线，但身份必须清楚；不得退化成极简空白符号表。
- pilot-001 人类角色锁定（身份不变，仅渲染风格改为儿童作业本怪谈）：
  - 小禾 / Xiao He：约 6–7 岁人类小孩，黄色连帽雨衣、红色雨靴、小圆背包；可画得幼稚、害怕、发抖，但仍是人类小孩。
  - 妈妈 / Mama：人类成年照护者，青色外套与围巾，比小禾高。
  - 守灯爷爷 / Lantern Grandpa：人类成年人；本风格下不再强制"温暖无害"，可带怪谈不确定性，但仍是人类。
  - 橘子 / Tangerine：一只猫；在本风格下其"发光的眼睛"可作为怪谈异常处（红圈/问号），不强制解释为普通反光。

## Horror Rules / 恐怖规则

- 允许超自然、允许未解释、允许半解释。
- 允许的恐怖元素范围广泛（黑暗、怪声、异常批注等均可）；但任何具体母题（柜门缝、奇怪眼睛、鬼影等）**仅为示例**，是否出现由当前故事/包决定，**不得**默认注入（见「Example Motifs Only / 仅作示例的母题」）。
- **不要求**所有恐怖都有普通自然解释；**不要求**把怪事改写成普通原因。
- 恐怖表达应像儿童画出的怪谈，不是成人恐怖电影。
- 写实 gore 与性内容仍然禁止（见 Content Safety Rules）。

## Example Motifs Only / 仅作示例的母题

The following are **examples of the visual language only** — they illustrate the *kind* of strange content this style *can* render. They are **not** required content and **must not** be injected into any story or image unless the current StoryProject, Scene card, Character cards, or approved `ImageExecutionPackage` actually call for them:

- a talking wardrobe / 会说话的衣柜
- darkness inside a door gap / 门缝里的黑暗
- a window at night / 夜里的窗户
- strange eyes / 奇怪的眼睛
- a blurry ghost shadow / 模糊的鬼影
- red-pen "anomaly" notes circling something odd / 红笔圈出的「异常」批注

These examples must never become a fixed checklist or required content. A page may contain none of them. Each compiled image renders only the specific scene event approved for its `ImageExecutionPackage`; the strange event, location, characters, props, and emotional beat come from that package and the canonical cards, not from this example list.

以上仅为视觉语言的**示例**，用于说明这套风格*能*画哪类怪事；它们**不是**必需内容，**不得**在当前故事/场景/角色/获批执行包没有要求时注入。示例不得变成固定清单或强制内容——某一页可以一个都不含。每张编译出的图只渲染其 `ImageExecutionPackage` 获批的那一个具体场景事件；奇异事件、地点、角色、道具与情绪节拍都来自该执行包与规范卡，而非本示例清单。

## Forbidden Style Drift / 禁止风格漂移

- 禁止精致商业绘本、梦幻童话风、过度漂亮的 AI 数字插画。
- 禁止动物拟人替代人类角色（刺猬、小熊、小兔、小动物主角化、玩偶、吉祥物）。
- 禁止 3D、电影感、写实摄影、油画厚涂、glossy 渐变、完美干净的矢量线稿、过度渲染的 AI 绘本光感。
- 禁止过度安全、过度温暖、过度理性解释的画面基调。
- **禁止把 "no supernatural" 作为全局规则。**
- **禁止把 "low fear" 作为全局规则。**
- 禁止把所有恐怖都改成普通自然原因。
- 禁止源视频的名称、地点、用词、包装、可辨识的恐怖画面或复刻镜头构图。
- 禁止任何画内平台 UI、prompt 文本、image id、WebGPTImage 说明文字。

## Reference Assets / 参考资产

None. This card does not create ReferenceAsset cards or image files. A future R00 paper/brushstroke style anchor or any reference asset must be accepted through the later ReferenceAsset workflow before use. The failed earlier p01 candidate must never be used as a reference.

## Related Prompt Recipes / 关联 Prompt Recipe

- `pr-pilot-001-child-horror-notebook`

## Removed History / 历史清理

- An earlier warm-safe night-picture-book visual system (over-safe / polished digital / animalized humans / no horror) was **removed** in the 2026-06-26 visual pipeline reset. It is not part of the active pipeline and must not be bound. This card is now the only active VisualStyle for `pilot-001`.
