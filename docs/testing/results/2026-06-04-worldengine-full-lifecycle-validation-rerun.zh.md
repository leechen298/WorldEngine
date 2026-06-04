# WorldEngine 完整生命周期自主验证重跑

Status: PASS
Mode: live full lifecycle validation plus saved-result checker
Date: 2026-06-04

英文版本：`2026-06-04-worldengine-full-lifecycle-validation-rerun.md`。

## Scope

本文记录 `0.8.9.2-director-guidance-public-redaction-repair` 修复 public director
guidance response 中的 private/internal marker wording，并强化 full lifecycle
saved-result checker 后的 fresh rerun。

这是 testing result，不是 iteration package。它不改写之前的 failed result：
`2026-06-04-worldengine-full-lifecycle-validation.md`。

## Scenario

权威场景：

- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`

Checker：

- `tools/testing/validate_agent_autonomous_result.py`

Result directory：

- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/`

Validation Client artifact source：

- `/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/validation-runs/playwright-artifacts/v0.7-ui-smoke-v0-7-browser-b9045-s-evidence-for-Agent-review/`

## Commands

```bash
PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

结果：`6 passed`。

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
```

结果：`19 passed`。

```bash
PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/app/tests/test_world_generation_schema.py backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_generation_core_readiness_api.py -q
```

结果：`20 passed`。

```bash
WORLDENGINE_API_BASE=http://127.0.0.1:8000 VALIDATION_CLIENT_API_BASE=http://127.0.0.1:8765 pnpm --dir apps/web test:e2e
```

结果：`1 passed`。

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle
```

结果：

```text
PASS: validated agent autonomous result at test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle
```

## Covered Evidence

本次 rerun 覆盖了要求的 lifecycle surfaces：

- 通过 Validation Client 创建 WorldEngine-backed world。
- Public world id：`world-16df0fbcaa35`。
- Runtime progression：tick `0` 到 tick `10`。
- Events observed：`42`。
- Snapshots observed：`1`。
- WorldEngine-backed Agent action event observed：`1`，action type 为
  `params.applied`。
- Director guidance 通过 public surface accepted。
- Validation Client evidence bundle 已导出。
- Validation Client redaction flags：
  `llm_keys_included=false`，`private_worldengine_internals_included=false`。

Supporting artifacts：

- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/result.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/world-lifecycle-summary.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/scorecard-summary.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/api-summary.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/validation-client-evidence-bundle.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/worldengine-public-api-probe.json`
- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/validation-client-agent-run.jsonl`

## Boundary

这个 PASS 表示 documented scenario 的 fresh full lifecycle evidence 已被 saved-result
checker 接受。它不声明 product readiness、human validation PASS、LLM quality PASS
或 external consumer certification。

Direct public API evidence 记录在 `api-summary.json`；没有 direct public API call
被记录成 Agent operation-log CLI step。
