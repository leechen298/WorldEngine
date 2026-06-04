# Plan

英文源文件：`plan.md`。

## Objective

用户 review 并显式授权实现后，实现 0.8.9 父包要求的 WorldEngine public handoff manifest 和 world creation contract。

## Tasks

### 1. Gate Confirmation

- 确认本包已获准实现。
- 确认不会修改或 stage 无关 dirty files。
- 保留已有用户变更。

### 2. Public Schemas

- 添加或扩展 manifest、provider readiness、redaction、world creation、director guidance 的 public schema models。
- 确保适当位置 forbid extra private fields。
- 添加 schema serialization tests。

### 3. Public Manifest Route

- 添加 `GET /manifest`。
- 返回 public provider readiness、public surfaces、redaction flags、blockers、warnings。
- 不执行 live provider calls。
- 不暴露 secrets、private prompts、raw traces 或 private validator details。

### 4. Public World Creation Route

- 添加 OpenAPI 可发现的 `POST /worlds`，operation id 为 `create_world`。
- 接受 `world_prompt`。
- 返回顶层 public `world_id`、`status`、`public_initial_state`、`visualization`。
- 复用现有 generic generation helpers，不添加 demo content。

### 5. Director Guidance Status

- 如果能保持 public 且不涉及 private state，添加 `POST /worlds/{world_id}/director-guidance`。
- 否则在 `/manifest` 中记录 director guidance unavailable。

### 6. Redaction And Compatibility Tests

- 添加 focused tests，覆盖 manifest shape、OpenAPI discoverability、world creation response shape、forbidden private data absence。
- 保持现有 endpoint behavior。

### 7. Runtime And Optional Client Probe

- 运行 focused backend tests。
- 运行 full backend tests。
- 启动 WorldEngine，探测 `/health`、`/manifest`、`/openapi.json`、`/worlds`。
- 如可用，运行 Validation Client `/health/worldengine` 和 `/sessions/worldengine` compatibility probes。

### 8. Review Closeout

- 更新 `review.md` 和 `review.zh.md`。
- 如条件通过，只记录 `WORLDENGINE_CONTRACT_READY`。
- 不声明 external validation PASS、Codex autonomous PASS 或 human validation PASS。

## Out Of Scope

- Validation Client implementation。
- provider runtime calls。
- provider credential storage。
- application-specific worlds 或 fixtures。
- hidden reset APIs。
- frontend changes。
- migrations。
- `backend/worldengine/`。
