# 证据索引

状态：audit complete

范围：截至 final closeout repair 的 v0.4 已评审实现和文档证据。

## 当前证据边界

本索引只记录当前会话 v0.4 证据。历史 v0.3 证据只作为 handoff context，不计入 v0.4 pass claim。

## Package Evidence

| Package | 类型 | 状态 | 证据 |
| --- | --- | --- | --- |
| `0.4.0-v0.4-planning-and-compatibility-baseline` | documentation-only | review complete | 已完成 documentation evaluator 和 closeout consistency review；未修改实现文件；package review 已记录文档检查。 |
| `0.4.1-agent-in-world-loop-contract` | documentation-only | review complete | 已完成 contract review closeout；未修改 runtime、schema、API 或 test implementation；package review 已记录文档检查。 |
| `0.4.2-agent-perception-and-schemas` | mixed/code | review complete | missing perception module red test；最终 perception tests `4 passed in 0.06s`；聚焦命令 `25 passed in 0.07s`；全 backend 回归 `119 passed in 0.75s`；evaluator P1/P2 已在 closeout 前修复。 |
| `0.4.3-action-intent-validation-and-result-adapter` | mixed/code | review complete | missing action adapter red test；empty patch regression 已修复；最终 adapter tests `6 passed in 0.09s`；聚焦命令 `25 passed in 0.44s`；全 backend 回归 `125 passed in 0.82s`；evaluator P1/P2 已在 closeout 前修复。 |
| `0.4.4-minimal-agent-loop-orchestration-and-api` | mixed/code | review complete | missing loop service red test；最终 loop service/API tests `9 passed in 0.23s`；final repair 聚焦 backend/API 命令 `35 passed in 0.55s`；final repair 全 backend 回归 `139 passed in 0.98s`；review findings 后补充 route-level invalid `params.patch` 和 nested patch-item extra 覆盖。 |

## Latest Command Evidence

最新 backend 实现证据：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
9 passed in 0.23s

cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
35 passed in 0.55s

cd backend && .venv/bin/python -m pytest app/tests tests -q
139 passed in 0.98s
```

最新文档/范围证据：

```text
git diff --check
passed

required docs/mirrors check for 0.4.5, including evidence index and compatibility audit
missing=0

changed-file scope guard
out_of_scope=0
```

## API Evidence

`backend/app/tests/test_agent_loop_api.py` 是 `POST /world/agent/loop/step` 的 FastAPI TestClient smoke。

已覆盖 API 行为：

- 无 intent 的默认请求返回 deterministic `noop`；
- accepted `params.patch` 应用 params，并产生 `source="agent.loop"` 的 `params.applied`；
- unsupported action 以 HTTP 200 和 rejected `ActionResult` 返回；
- invalid `params.patch` 以 HTTP 200 和 rejected `ActionResult` 返回，不修改状态，也不产生 `params.applied` event；
- request schema error 保持既有 422 API envelope；
- nested patch-item unknown fields 保持既有 422 API envelope，且不修改
  params、不产生 `params.applied`；
- 既有 `/world/agent/params/propose-and-apply` 仍能应用默认 mock patch。

## 未运行命令

v0.4 截至本审计未运行 frontend、browser E2E、Agent smoke、build、fixture、migration 或 external validation runner 命令，因为实现包未授权或触及这些 surface。

## Open Findings

- P1：none。
- P2：none。
- P3：none blocking at this audit boundary。

## Handoff

本 evidence index 基于已评审的 0.4.5 audit record，支撑 `0.4.6-v0.4-release-candidate-bundle` 准备。
