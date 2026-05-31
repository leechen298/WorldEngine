# Release Candidate Bundle

状态：release-candidate bundle complete

范围：v0.4 release-candidate evidence package。本文件不声明 final release 或 final closeout。

## Candidate Summary

v0.4 实现最小 request-driven 世界内 Agent 闭环：

- 从 runtime state、recent events、world params 和可选 runtime context summary 形成有界 perception；
- 可审查的 `ActionIntent` 与 `ActionResult` schemas；
- 支持 actions：`noop` 和经过校验的 `params.patch`；
- request-scoped loop service；
- additive API route：`POST /world/agent/loop/step`；
- 兼容性保留地复用既有 world params validation、dry-run、apply、event log、runtime state 和 API envelope patterns。

## Package Statuses

| Package | 状态 | Release-Candidate Input |
| --- | --- | --- |
| `0.4.0-v0.4-planning-and-compatibility-baseline` | review complete | v0.4 plan、campaign controls、compatibility baseline。 |
| `0.4.1-agent-in-world-loop-contract` | review complete | public concepts、implementation authorization rules、API/error/event boundaries。 |
| `0.4.2-agent-perception-and-schemas` | review complete | `PerceptionFrame`、runtime/context summary schemas、`PerceptionBuilder`、focused/backend evidence。 |
| `0.4.3-action-intent-validation-and-result-adapter` | review complete | `ActionIntent`、`ActionResult`、`ActionResultAdapter`、validated action results、focused/backend evidence。 |
| `0.4.4-minimal-agent-loop-orchestration-and-api` | review complete | `AgentLoopService`、loop-step API route、app factory wiring、focused/API/backend evidence。 |
| `0.4.5-agent-loop-evidence-and-compatibility-audit` | review complete | evidence index、compatibility audit、docs-only scope evidence。 |

## Current Evidence Snapshot

最新实现证据：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
9 passed in 0.23s

cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
35 passed in 0.55s

cd backend && .venv/bin/python -m pytest app/tests tests -q
139 passed in 0.98s
```

审计打包的最新 documentation-only 证据：

```text
git diff --check
passed

0.4.5 required docs/mirrors check, including evidence index and compatibility audit
missing=0

changed-file scope guard
out_of_scope=0
```

## Public Interface Candidate

Schemas：

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- `LoopStepRequest`
- `LoopStepResponse`

API：

- `POST /world/agent/loop/step`

兼容性敏感 existing API：

- `/world/agent/params/propose-and-apply` 仍可用且未改变。

## Compatibility Claims

Release candidate 承载以下已评审 claims：

- schema additions are additive；
- runtime tick/time behavior remains compatible；
- event route compatibility remains covered；
- world params validation/apply behavior remains compatible；
- successful loop `params.patch` emits `params.applied` with `source="agent.loop"`；
- rejected actions and no-op actions do not emit events；
- unsupported or invalid loop actions return HTTP 200 with rejected `ActionResult`；
- invalid request bodies keep the existing 422 API envelope；
- archive、frontend、fixture、migration 和 legacy `backend/worldengine/` surfaces remain unchanged。

## 0.4.6 未运行命令

Backend、frontend、API smoke、E2E、Agent smoke、runtime behavior、build、schema execution、fixture、migration 和 test implementation commands 未在本包运行，因为 `0.4.6` 是 documentation-only，且不修改 implementation files。

## Open Findings

- P1：none。
- P2：none。
- P3：none blocking at release-candidate packaging boundary。

## 0.4.7 Final Review Questions

Final closeout 前，`0.4.7` 必须确认：

1. `0.4.0` 到 `0.4.6` 是否全部为 `review complete`？
2. 最新 backend implementation evidence 是否仍支持 v0.4 pass claims？
3. final bundle 写入后 documentation-only checks 是否仍通过？
4. 是否存在未解决 P1 或 P2 findings？
5. frontend/E2E/build/fixture/migration 命令是否仍正确记录为 not run，且原因是没有对应 surface change？
6. 中文镜像是否匹配最终 closeout status 和 evidence？
7. final closeout 是否避免声明 v0.5 memory、v0.6 generation、v0.7 external validation、v0.8 projection 或 concrete world/demo readiness？

## Handoff

本 release-candidate bundle 已可交接给 `0.4.7-v0.4-final-closeout` review。Final release 或 closeout 只能由 `0.4.7` 声明。
