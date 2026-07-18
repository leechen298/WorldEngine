# Test Plan

英文版本：`test-plan.md`。

除非特别说明，从 `backend` 目录运行。

## Focused Tests

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

Required coverage：

- session run advances bounded ticks，并报告 public run evidence。
- session run rejects unbounded or over-guard requests。
- pause 在 resume 前阻塞 session run。
- session snapshot list 返回 bounded public snapshots。
- unknown sessions 返回现有 404 envelope。
- manifest 暴露 implemented session runtime/snapshot surfaces。
- 现有 `/runtime/*` tests 仍通过。
- public session run 和 snapshot payloads 不含 redaction markers。

## Expanded Focused Regression

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py
```

这用于在增加 session runtime wrappers 时保持 0.10.3 worldview-to-session behavior 兼容。

## Non-Run Tests

除非后续 contract 明确授权，本包不运行 live provider checks、browser E2E、Validation Client
checks 或 external checker suites。
