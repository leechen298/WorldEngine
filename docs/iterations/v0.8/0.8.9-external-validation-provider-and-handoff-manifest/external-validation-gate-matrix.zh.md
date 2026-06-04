# 外部验证门禁矩阵

英文镜像：`external-validation-gate-matrix.md`。

状态：planned / ready for review
类型：documentation-only gate plan
implementation_authorized: no
evidence_execution_authorized: no

用途：从 WorldEngine 视角记录外部 Validation Client v0.7 自主验证的跨仓库门禁。
本文不授权 runtime、API、schema、测试、provider 或 Validation Client 实现。

## 0. WorldEngine 在门禁中的责任

WorldEngine 只负责 Gate 1：

```text
WorldEngine public contract readiness
```

WorldEngine 不负责：

- Validation Client operation log。
- Validation Client E2E。
- Codex 浏览器自主验证。
- 第二 Agent 只读复核。
- 人工体验判断。
- 外部验证应用的存储、截图、报告和 UI。

WorldEngine 必须保证外部客户端只通过 public API 消费世界状态和证据，不需要读取
private path、provider key、private prompt、provider raw trace 或 Agent private
state。

## 1. 全链路门禁

| Gate | 名称 | Owner | WorldEngine 责任 | 进入下一关条件 |
| --- | --- | --- | --- | --- |
| Gate 0 | 文档计划门禁 | 规划聊天 | 提供 0.8.9 package | 两个仓库有可执行文档 |
| Gate 1 | WorldEngine public contract readiness | WorldEngine | 实现 public manifest、world creation、provider readiness redaction、contract checklist | `WORLDENGINE_CONTRACT_READY` |
| Gate 2 | Validation Client v0.7 implementation readiness | Validation Client | 只提供 public API，不修改客户端 | 客户端写出 `READY_FOR_CODEX_AUTONOMOUS_VALIDATION` |
| Gate 3 | Codex autonomous validation | Codex | 保持 API 可用和脱敏 | Codex 写出 `PASS_READY_FOR_HUMAN_VALIDATION` |
| Gate 4 | 第二 Agent 只读复核 | 另一个 Agent | 不参与 | Agent 写出 `READY_FOR_HUMAN_VALIDATION` |
| Gate 5 | 人工验证 | 人类 | 不参与 | 人类写出 `HUMAN_PASS` |

## 2. Gate 1 必须交付的 WorldEngine public surfaces

必须提供：

```text
GET /health
GET /manifest
GET /openapi.json
POST /worlds
```

完整 v0.7 自主验证建议提供：

```text
POST /worlds/{world_id}/director-guidance
```

如果 director guidance 暂不可用，`/manifest` 必须公开说明 unavailable reason。
这种情况可以是 `PARTIAL`，但不能作为完整 v0.7 自主验证的
`WORLDENGINE_CONTRACT_READY`。

## 3. `/manifest` 最小 public 字段

```json
{
  "schema_version": "0.8.x",
  "worldengine_version": "v0.8",
  "provider": {
    "provider_class": "mock|kimi_platform_api|deepseek_api|unknown",
    "provider_readiness": "ready|limited|blocked|unknown",
    "credential_source_class": "environment|not_configured|unknown",
    "model_label": "public-or-redacted-label"
  },
  "public_surfaces": [
    "/health",
    "/openapi.json",
    "/worlds",
    "/worlds/{world_id}/director-guidance"
  ],
  "redaction": {
    "secrets_included": false,
    "private_prompts_included": false,
    "provider_raw_traces_included": false,
    "private_agent_state_included": false
  },
  "blockers": [],
  "warnings": []
}
```

## 4. `POST /worlds` 最小 contract

Request：

```json
{
  "world_prompt": "一个可观察的小型像素世界"
}
```

Response 必须包含：

```json
{
  "world_id": "public-world-id",
  "status": "created|ready|limited",
  "public_initial_state": {},
  "visualization": {},
  "warnings": []
}
```

禁止返回：

- API key。
- authorization header。
- private prompt。
- provider raw trace。
- provider raw response。
- Agent private memory。
- Agent private goal。
- self_state。
- relationship private details。
- identity private details。
- hidden_context。
- internal helper path。

## 5. Validation Client compatibility probe

实现完成后必须启动 Validation Client API，并运行：

```bash
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

必须证明：

- Validation Client 报告 `world_creation: available`。
- Validation Client `POST /sessions/worldengine` 成功。
- Validation Client 不需要 provider key。
- Validation Client 不需要 WorldEngine private path。

## 6. Contract readiness 结论

`contract-readiness-checklist.zh.md` 结论只能选择：

```text
WORLDENGINE_CONTRACT_READY
PARTIAL
BLOCKED
FAIL
```

`WORLDENGINE_CONTRACT_READY` 只表示：

```text
WorldEngine public contract can be handed to Validation Client for Codex autonomous validation.
```

它不表示：

- external validation PASS。
- Codex autonomous validation PASS。
- second Agent review PASS。
- human validation PASS。

## 7. Stop Rules

WorldEngine 实现聊天必须停止并记录非 ready 结论的情况：

- `/manifest` 缺失。
- OpenAPI 没有客户端可发现的 world creation endpoint。
- `POST /worlds` 不能返回 public world id 和 public state。
- provider readiness 暴露 secret 或伪装 ready。
- public response 包含 private prompt、provider raw trace 或 Agent private state。
- Validation Client compatibility probe 失败。
- 需要修改 Validation Client 才能通过 Gate 1。

如果发现需要修改 Validation Client，WorldEngine 聊天只记录 downstream task，不得
跨仓库实现。

## 8. 下游文档入口

Validation Client 侧完整矩阵：

```text
/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/cross-repo-validation-gate-matrix.zh.md
```

WorldEngine 后续实现使用：

```text
implementation-task-plan.zh.md
contract-readiness-checklist.zh.md
implementation-handoff-prompt.zh.md
```
