# 0.8.9 Planning Readiness Checklist

英文镜像：`planning-readiness-checklist.md`。

状态：PLAN_READY_FOR_REVIEW
类型：documentation-only planning evidence
implementation_authorized: no
evidence_execution_authorized: no

用途：证明 0.8.9 WorldEngine public contract package 已经具备后续实现聊天需要的
计划文档。本文不证明 WorldEngine public contract 已实现。

## 0. 结论

```text
PLAN_READY_FOR_REVIEW
```

一句话原因：

```text
0.8.9 package 已定义 intent、contract、technical design、test plan、implementation
task plan、external validation gate matrix、contract readiness checklist 和
future-chat prompt。
```

## 1. 当前允许的下一步

唯一允许的下一步：

```text
用户 review 本 package，然后在后续实现聊天中实现 Gate 1 public contract。
```

不允许：

- 在本 planning package 中修改 runtime、API、schema、test 或 provider code。
- 声明 `WORLDENGINE_CONTRACT_READY`。
- 声明 Validation Client autonomous validation PASS。
- 声明 human validation PASS。

## 2. 必备文档

必须存在：

```text
README.zh.md
intent.zh.md
contract.zh.md
technical-design.zh.md
test-plan.zh.md
plan.zh.md
validation-client-contract-handoff.zh.md
implementation-task-plan.zh.md
external-validation-gate-matrix.zh.md
contract-readiness-checklist.zh.md
implementation-handoff-prompt.zh.md
review.zh.md
planning-readiness-checklist.zh.md
```

## 3. 覆盖项

本 package 已覆盖：

- `GET /manifest` public handoff manifest。
- OpenAPI 可发现 world creation endpoint，优先 `POST /worlds`。
- public world creation response。
- 可选 director guidance public endpoint。
- provider readiness redaction。
- Validation Client compatibility probe。
- `WORLDENGINE_CONTRACT_READY` 结论边界。
- WorldEngine 不实现 Validation Client operation log、E2E、Codex browser run、
  第二 Agent 复核或 human validation。

## 4. 当前 blocker

当前仍阻塞外部验证：

- 当前 WorldEngine public API 缺 `/manifest`。
- 当前 WorldEngine OpenAPI 缺 Validation Client 可发现的 world creation
  endpoint。
- Validation Client 仍不能创建 WorldEngine-backed session。

这些 blocker 只能由后续 implementation package 或实现聊天解决。

## 5. 后续实现完成条件

未来实现聊天只有在满足以下条件时，才能写 `WORLDENGINE_CONTRACT_READY`：

- `/health` 200。
- `/manifest` 200，且只包含 public redacted fields。
- `/openapi.json` 暴露可发现 world creation endpoint。
- `POST /worlds` 成功返回 public world id、status、public state 和 visualization。
- director guidance endpoint 可用，或 manifest 记录 public unavailable reason。
- provider readiness 不泄漏 secret、private prompt 或 provider raw trace。
- Validation Client `/health/worldengine` 报告 `world_creation: available`。
- Validation Client `POST /sessions/worldengine` 成功。
- `contract-readiness-checklist.zh.md` 已记录证据。

## 6. Stop Rules

未来实现聊天必须停止并记录非 ready 结论的情况：

- public response 包含 key、authorization header、private prompt、provider raw
  trace 或 Agent private state。
- world creation 需要 Validation Client 读取 private path。
- 需要修改 Validation Client 才能通过 Gate 1。
- provider readiness 伪装为 ready。
- 实现引入 demo-world content 或 external validator behavior。

## 7. Handoff Prompt

当前交接状态：

```text
handoff-status.zh.md
```

后续实现使用：

```text
implementation-handoff-prompt.zh.md
```
