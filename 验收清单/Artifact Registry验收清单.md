# Artifact Registry验收清单

- [ ] `runtime/artifact_registry/` 存在。
- [ ] `runtime/.artifacts/registry.json` 可解析。
- [ ] hash utils 可对文件、JSON、字符串生成 sha256。
- [ ] 空输入明确失败。
- [ ] registry 可注册 artifact。
- [ ] 重复 `artifact_id` 被阻断。
- [ ] 缺失依赖被阻断。
- [ ] accepted reference asset 有 telemetry + QA 时通过。
- [ ] accepted reference asset 缺 QA 时被阻断。
- [ ] rejected asset 不可作为 reference dependency。
- [ ] deprecated asset 不可作为 reference dependency。
- [ ] lineage 可追踪到 compiled_prompt。
- [ ] registry check 断链为 0。
- [ ] 不创建故事项目。
- [ ] 不生成图片。
- [ ] 不生成执行包。
- [ ] 不生成发布包。
