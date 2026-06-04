# Implementation Handoff Prompt

英文镜像：`implementation-handoff-prompt.md`。

在未来实现聊天中使用本 prompt。当前 package 仍是 documentation-only。

```text
/goal 实现 0.8.9-external-validation-provider-and-handoff-manifest 的 public handoff manifest 和 world creation contract。

必须先读取：
- AGENTS.md
- docs/project-north-star.md
- docs/product-model.md
- docs/scope-boundaries.md
- docs/roadmap.md
- docs/iterations/README.md
- docs/iterations/AGENTS.md
- docs/iterations/v0.8/README.zh.md
- docs/iterations/v0.8/CURRENT_STATE.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/external-validation-gate-matrix.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/planning-readiness-checklist.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/handoff-status.zh.md
- docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.zh.md

目标：
- 添加或实现 GET /manifest，返回脱敏 public readiness document。
- 添加 OpenAPI 可识别的 public world creation endpoint，优先 POST /worlds。
- world creation response 必须包含 public world_id、status、public state 和 visualization。
- 如可行，添加 POST /worlds/{world_id}/director-guidance。
- provider readiness 只能公开 provider class、readiness、credential source class 和 public model label。

边界：
- 不实现 Validation Client code。
- 不加入具体 demo-world content。
- 不把 external validator behavior 放进 WorldEngine。
- 不暴露 API keys、private prompts、provider raw traces、private Agent memory、private goals、self_state、hidden_context 或 private file paths。
- 不重新打开 v0.8 final closeout。0.8.9 是 post-closeout addendum。

验证：
- cd backend && .venv/bin/python -m pytest app/tests -q
- git diff --check
- 启动 WorldEngine 后验证 /health、/manifest、/openapi.json 和 POST /worlds。
- 启动 Validation Client API 后验证 /health/worldengine 报告 world_creation: available。
- 验证 Validation Client POST /sessions/worldengine 成功。

完成：
- 更新本 package 的 review.md 和 review.zh.md。
- 如 contract ready，按 contract-readiness-checklist.zh.md 记录证据。
- 结论只能说明 WorldEngine contract is ready for Validation Client autonomous validation。
- 不声明 external validation PASS 或 human validation PASS。
```

## Stop Rules

- 如果实现需要具体 demo-world content，停止。
- 如果 provider credentials 会出现在 public output，停止。
- 如果需要修改 Validation Client code，停止并记录为 downstream Validation Client task。
- 如果会改变 v0.8 final closeout 的含义，停止。
