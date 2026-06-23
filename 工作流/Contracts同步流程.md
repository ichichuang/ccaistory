# Contracts 同步流程

状态：活动

## 原则

`runtime/contracts/` 是机器事实源。Markdown 是说明层。runtime 优先读取 contracts；若 Markdown 与 contracts 冲突，以 contracts 为准。

## 修改流程

1. 修改对应 contract JSON。
2. 更新 runtime 读取逻辑或校验脚本。
3. 同步相关 Markdown 说明。
4. 更新或补充 smoke test。
5. 运行：

```bash
python runtime/aistory.py validate-contracts
python runtime/aistory.py check-contract-drift
python runtime/aistory.py smoke-test
```

## 漂移处理

- Python 常量与 contracts 冲突：改 Python 读取 contracts。
- Markdown 与 contracts 冲突：改 Markdown 说明层。
- `skills.json` 与 `skill_definitions.json` 冲突：先确认 contract，再同步 registry 或 contract。

