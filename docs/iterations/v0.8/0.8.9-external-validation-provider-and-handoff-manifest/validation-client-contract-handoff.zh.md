# Validation Client 契约交接清单

英文镜像：`validation-client-contract-handoff.md`。

## 目的

本文定义外部 Validation Client 进入 Codex 自主验证和人工验证交接前，WorldEngine
必须提供的最小 public contract。

本文只是 planning document。不授权 runtime、API、schema、frontend、test、
fixture、migration 或 provider implementation。

## 当前实测缺口

截至 2026-06-04，本地检查结果：

- WorldEngine 可以本地启动。
- `GET /health` 返回 200。
- `GET /openapi.json` 返回 200。
- `GET /world/params` 返回 200。
- `GET /manifest` 返回 404。
- `GET /world/generation/readiness` 返回 404。
- Validation Client 可以调用 `GET /health/worldengine`。
- Validation Client 报告 `reachable: true` 和 `openapi_available: true`。
- Validation Client 报告 `world_creation: unknown`。
- Validation Client `POST /sessions/worldengine` 返回 502：
  `WorldEngine public world creation endpoint not found`。

这说明 Validation Client 能发现 WorldEngine，但不能创建 WorldEngine-backed
session。Codex 浏览器自主验证必须在该 contract gap 修复后才能继续。

## 必需 Public Surfaces

### `GET /manifest`

用途：

- 暴露 public validation-readiness 信息。
- 暴露 provider readiness，但不暴露 secrets。
- 暴露 external consumer 可用的 public surface ids。
- 暴露 redaction flags、blockers 和 warnings。

最小 response shape：

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
    "private_validator_details_included": false
  },
  "blockers": [],
  "warnings": []
}
```

### Public world creation endpoint

当前 Validation Client 会从 OpenAPI 自动发现 public creation endpoint。它能识别：

- POST path 以 `/worlds` 结尾。
- 或 POST operation id 等于 `createWorld` / `create_world`。
- 或 POST operation tag 包含 `worlds`，且 operation id 包含 `create`。

推荐 endpoint：

```text
POST /worlds
```

最小 request：

```json
{
  "world_prompt": "一个可观察的小型像素世界"
}
```

最小 response：

```json
{
  "world_id": "world-001",
  "status": "created",
  "public_initial_state": {
    "summary": "public summary",
    "public_agents": [
      {
        "agent_id": "agent-1",
        "display_name": "Ada",
        "location": "market",
        "public_status": "observing",
        "visible_action": "opens a stall"
      }
    ]
  },
  "visualization": {
    "tiles": [],
    "entities": []
  }
}
```

### Public director guidance endpoint

完整 v0.7 Validation Client 自主验证需要该能力。

推荐 endpoint：

```text
POST /worlds/{world_id}/director-guidance
```

最小 request：

```json
{
  "instruction_text": "让接下来的事件倾向和平互动",
  "branch_id": "branch-public-id",
  "tick": 0,
  "public_context": {}
}
```

最小 response：

```json
{
  "status": "accepted|applied|blocked",
  "public_explanation": "public summary only",
  "applied_event_id": "event-public-id",
  "error_message": null
}
```

## 禁止公开的数据

以下内容不得出现在 public responses、manifest、evidence、OpenAPI examples 或
Validation Client logs：

```text
api_key
authorization
credential
password
provider secret
private prompt
provider raw trace
private validator oracle
Agent private memory
Agent private goal
Agent self_state
hidden_context
private filesystem path
```

## 验证命令

未来 implementation package 添加 contract 后，先运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

另一个 shell 运行：

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8000/worlds
```

再验证 Validation Client：

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

## Acceptance Criteria

只有满足以下条件，WorldEngine contract 才可以支持 Validation Client 自主验证：

- `/manifest` 返回脱敏 public readiness document。
- OpenAPI 暴露 Validation Client 可发现的 world creation endpoint。
- world creation 返回 public `world_id`、`status`、state 和 visualization。
- provider readiness 公开，但 secrets 不公开。
- Validation Client `/health/worldengine` 报告 `world_creation: available`。
- Validation Client `POST /sessions/worldengine` 成功。

## Stop Rules

- `/manifest` 缺失时，Codex 自主验证不得声明 provider readiness。
- world creation 不能被 Validation Client 发现时，浏览器自主验证必须在 UI flow
  前停止。
- public responses 泄漏 secrets 或 private prompts 时，结果为 FAIL。
- director guidance 缺失时，可以 PARTIAL，但不得写完整
  ready-for-human-validation PASS。
