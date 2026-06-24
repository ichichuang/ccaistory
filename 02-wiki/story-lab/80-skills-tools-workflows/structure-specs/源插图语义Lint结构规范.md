# 源插图语义 Lint 结构规范

## 输出结构

```json
{
  "asset_id": "",
  "lint_result": "pass | fail",
  "failed_rules": [],
  "risky_terms": [],
  "asset_scope_conflicts": [],
  "missing_fields": [],
  "repair_suggestions": []
}
```

## 硬失败
R00 出现人物、火柴人、道具集合、场景清单、符号散点表；R01 承载剧情；R02 承载主线事件；S 页包含平台正文长手写；P01 不是 9:16；缺 visual_center 或 acceptance_questions；作者姓名作为风格指令。
