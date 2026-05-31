# 兼容性审计

状态：audit complete

范围：截至 `0.4.4-minimal-agent-loop-orchestration-and-api` 的 v0.4 实现。

## 摘要

v0.4 新增最小 request-driven 世界内 Agent 闭环，但不添加后台自治、记忆、生成、外部验证就绪、投影就绪或具体世界内容。

兼容性状态：

- Runtime tick/time behavior：preserved。
- Event API pagination 和 optional refs behavior：preserved。
- World params validation、dry-run、apply behavior：preserved and reused。
- 既有 params-agent route：preserved。
- API envelope：preserved；action validation rejection 保持在 HTTP 200 loop result 内，request schema errors 仍使用 422 envelope。
- Schema changes：additive。
- Frontend、fixture、migration、legacy `backend/worldengine/`：unchanged。

## Surface Audit

| Surface | v0.4 变化 | 兼容性评估 | 证据 |
| --- | --- | --- | --- |
| Runtime state and stepping | Read-only perception 使用 `RuntimeEngine.get_state()`；loop action adapter 读取 runtime state 作为 event tick/time。 | 未改变 tick/time semantics。 | `test_runtime_step.py` 包含在聚焦 backend/API 命令中；最终全 backend `139 passed`。 |
| Runtime context bridge | Perception 可选摘要 runtime context，不暴露完整 root object。 | Additive read-only summary；不修改 runtime context。 | `test_runtime_context_bridge.py` 包含在 0.4.2 聚焦命令中。 |
| Event log and event APIs | loop `params.patch` 产生 `source="agent.loop"` 的 `params.applied`；perception 通过 `list_page(limit=N)` 读取 newest-first events。 | Event schema 保持兼容；既有 event routes 仍有覆盖。 | `test_event_schema_compat.py`、`test_event_api_compat.py`、`test_agent_loop_api.py`。 |
| World params | loop `params.patch` 使用严格 `ActionParamPatchItem` schema，保持与 `ParamPatchItem` 兼容，然后复用 `ParamValidator`、`ParamDryRunValidator` 和 `WorldState.apply_patch()`。 | 既有 validation/apply semantics preserved；loop patch-item extras 现在会在 mutation 前使用既有 422 envelope 失败。 | `test_agent_action_adapter.py`、`test_param_validator.py`、`test_dry_run_validation.py`、`test_world_params.py`、`test_agent_loop_api.py`。 |
| Existing ParamsAgent route | `/world/agent/params/propose-and-apply` 被保留。 | 既有 endpoint behavior preserved。 | `test_params_agent.py`；0.4.4 API smoke 包含 existing route。 |
| New loop route | 新增 `POST /world/agent/loop/step`。 | Additive API route；未替换既有 route。 | `test_agent_loop_api.py`。 |
| API error model | Action rejections 返回 HTTP 200 和 `ActionResult(status="rejected")`；invalid request bodies 返回既有 422 envelope。 | 与既有 API envelope rules 兼容。 | `test_agent_loop_api.py`。 |
| Archive service | App factory wiring 保持 archive callback 不变。 | 无 archive behavior change。 | 全 backend 回归。 |
| Frontend / browser E2E | 无 frontend changes。 | Not applicable。 | `git status --short --branch`；命令记录为 not run。 |
| Fixtures / migrations | 无 fixture 或 migration changes。 | Not applicable。 | Scope guard `out_of_scope=0`。 |
| Legacy backend | `backend/worldengine/` 下无变更。 | Preserved。 | Scope guard `out_of_scope=0`。 |

## Additive Schema Inventory

`backend/app/schemas/agent_loop.py` 中新增或扩展的 models：

- `RuntimeStateSummary`
- `RuntimeContextSummary`
- `PerceptionFrame`
- `ActionParamPatchItem`
- `ActionIntent`
- `ActionResult`
- `LoopStepRequest`
- `LoopStepResponse`

这些 models 不替换既有 response models。它们由新的 loop service/API route 和聚焦测试使用。

## Event Semantics

loop 对成功 param patch 继续使用既有 `params.applied` event type，并通过 `source="agent.loop"` 区分 route。

Rejected actions 和 no-op actions 不产生 event。

## 已确认范围排除

v0.4 不实现：

- memory、episodic memory、relationship state、self-summary、reflection 或 personality drift；
- world generation；
- external validation runner readiness 或 report automation；
- projection application readiness；
- 具体 world names、maps、characters、locations、resources、story rules、seed data、UI-specific app behavior 或 private validation oracle behavior；
- `backend/worldengine/` 下的新 runtime features。

## Residual Risk

本审计边界没有未解决 P1/P2 risk。

剩余非阻塞风险：

- v0.4 是 request-driven；缺省 intent 使用 deterministic noop；它不是 autonomous agent runtime。
- v0.4 只暴露最小 action vocabulary：`noop` 和 `params.patch`。
- 未运行 frontend 和 browser E2E，因为没有 frontend surface 变化。

## Handoff

本审计基于已评审的 0.4.5 documentation-only scope、mirror、command-evidence 和 finding record，支撑 `0.4.6` 准备 release-candidate bundle。
