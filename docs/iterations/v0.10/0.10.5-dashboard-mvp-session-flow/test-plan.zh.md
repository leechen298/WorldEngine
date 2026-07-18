# Test Plan

英文版本：`test-plan.md`。

除非特别说明，从 `frontend` 目录运行。

## Frontend Unit Tests

```bash
pnpm test
```

Required coverage：

- API client methods 调用 public session endpoints 并 unwrap API payloads。
- dashboard renders session shell 和 existing status panels。
- create session action 展示 session id/status/generation summary。
- run action 展示 runtime/event/snapshot evidence，并刷新 runtime 和 timeline state。
- pause/resume actions 调用 session-scoped APIs。
- existing RuntimeControls one-step behavior 继续被覆盖，或明确适配。

## Frontend Build

```bash
pnpm build
```

## Targeted E2E

```bash
pnpm test:e2e -- dashboard.spec.ts
```

仅在当前环境可启动 backend 和 frontend dev server 时运行。如果不可用，按命令输出如实记录
BLOCKED/PARTIAL。

## Backend Compatibility

从 `backend` 运行：

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

本包不运行 live provider、Validation Client 或 external checker suites。
