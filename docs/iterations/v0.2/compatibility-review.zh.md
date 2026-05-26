# v0.2 Compatibility Review

状态：0.2.10 compatibility evidence

本文把 v0.1 runtime scaffold compatibility 映射到 v0.2 foundation work。它区分
documented baseline、reviewed evidence、current-session path checks、planned
future work、not implemented behavior、legacy code 和 findings。本文不改变代码。

## 状态说明

- `documented`：由 current implementation、backend、API、architecture、contract
  或 boundary docs 描述。
- `reviewed`：由已完成 package review evidence 覆盖。
- `current-session verified`：在本 0.2.10 session 中通过 read-only commands 检查。
- `planned`：future roadmap 或 package scope。
- `not implemented`：明确不属于当前 implementation。
- `legacy`：只存在于 active wiring 之外。
- `finding`：记录在 `docs/iterations/v0.2/findings.md` 的未解决风险。

## Evidence Inputs

- `AGENTS.md`
- `CLAUDE.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/architecture.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- completed v0.2 package reviews through 0.2.9
- 对 `backend/app/`、`frontend/` 和 `backend/worldengine/` 的 current-session
  path checks

## Compatibility Matrix

| Surface | Compatibility claim | Evidence | Status | 0.2.10 result |
|---|---|---|---|---|
| Active backend path | `backend/app/` 仍是 active backend。 | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`; current-session file listing。 | documented / reviewed / current-session verified | Preserved。未改变 backend files。 |
| Runtime state | Runtime 保持 `tick_id`、`world_time_seconds`、`step_seconds` 和 `updated_at` 作为当前 scaffold state。 | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`; completed code-package reviews。 | documented / reviewed | 作为 documented baseline 保持。docs-only package 未重新运行。 |
| Runtime step behavior | `/runtime/step` 手动推进一步，追加 `tick.advanced`，运行 modules，可能触发 archive callbacks，并返回 runtime state。 | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`。 | documented / reviewed | Preserved。未改变 runtime implementation。 |
| Event timeline | `/world/events` 和 `/world/event-steps` 保持当前 newest-first pagination 和 grouped tick behavior。 | `docs/api-reference-v0.1.md`, `docs/backend-implementation.md`, 0.2.3 和 0.2.8 event compatibility reviews。 | documented / tested / reviewed | Preserved。v0.2 event refs 仍是 optional additive schema data。 |
| World params | `/world/params` 和 `/world/params/apply` 保持当前 writable path、reserved prefix、static validation、dry-run validation 和 event behavior。 | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`。 | documented / reviewed | Preserved。未改变 params code 或 tests。 |
| Params-agent scaffold | `/world/agent/params/propose-and-apply` 仍是 params proposal and validation loop，不是 agent-in-world cognition loop。 | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`。 | documented / reviewed | Preserved。Agent pseudo-self 和 memory 仍是 future scope。 |
| Archive snapshots and summaries | Archive 仍是 callback-driven，并使用 in-memory snapshot 和 summary stores。 | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`。 | documented / reviewed | Preserved。未改变 archive implementation。 |
| API envelope | 成功响应保持 `{ "code": 0, "data": ..., "msg": "ok" }`；error mappings 保持 documented v0.1 behavior。 | `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`。 | documented | 作为 documented baseline 保持。未运行 current-session endpoint smoke。 |
| Frontend expectations | Dashboard 消费 health、runtime state、grouped event steps、world params、params-agent flow、placeholder agent state 和 latest summary。 | `docs/current-implementation.md`; current-session `frontend/` path check。 | documented / current-session verified | Preserved。未改变 frontend files。 |
| Schema foundations | EntityRef、WorldCell 和 WorldSpec 是 additive schema contracts，不是 runtime loading behavior。 | `docs/contracts/entity-ref-contract.md`, `docs/contracts/worldcell-contract.md`, `docs/contracts/worldspec-contract.md`, 0.2.7 review。 | implemented / documented / tested / reviewed | Preserved。未改变 schema files。 |
| Event reference foundations | EventRef 和 optional `Event.refs` 仍是 additive event-local references。 | `docs/contracts/event-ref-contract.md`, 0.2.3 和 0.2.8 reviews。 | implemented / documented / tested / reviewed | Preserved。未添加 resolver、causality engine 或 runtime binding。 |
| Legacy backend | `backend/worldengine/` 仍是 legacy 且 unwired。 | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/architecture.md`; current-session path check。 | documented / legacy / current-session verified | Preserved。未改变 legacy files。 |
| Placeholder infrastructure | `backend/app/infra/ports` 和 `backend/app/infra/sqlite` 仍是 placeholder repository infrastructure。 | `docs/backend-implementation.md`; current-session path check。 | documented / current-session verified | Preserved。不是 active persistence。 |
| External fixtures | Concrete external fixture 和 validation worlds 仍在 core 之外。 | `docs/external-fixture-boundary.md`, 0.2.5 review, 0.2.9 boundary audit。 | documented / reviewed / tested | Preserved。未增加 external repository 或 fixture internals。 |

## v0.3 Handoff Constraints

未来 bridge work 不得把 v0.2 contracts 当作 implicit runtime behavior。v0.3
loader 或 bridge package 必须明确覆盖：

- WorldSpec loading entry points 和 failure behavior。
- Runtime state compatibility 和 migration rules。
- API envelope 和 endpoint compatibility。
- Event append、storage、pagination、grouping 和 optional refs compatibility。
- World params coexistence 或 migration behavior。
- Archive snapshot 和 summary compatibility。
- Frontend-facing behavior 和 dashboard regression evidence。
- Legacy `backend/worldengine/` handling。
- 如果 placeholder infrastructure 变为 active，需要说明 persistence expectations。

本 docs-only review 没有运行 backend、frontend、API 或 E2E tests。该 evidence gap
作为 `v0.2-P3-003` 记录，目标是第一个提出 behavior changes 的 v0.3 bridge package。

## Compatibility Assessment

0.2.10 通过 documentation-only changes 保持 v0.1 compatibility。它不编辑
runtime、schema、API、frontend、fixture、migration、test 或 legacy implementation
files。

Current-session verification 仅限 documentation checks 和 read-only path
inspection。Runtime 和 frontend behavior 仍是 documented and previously
reviewed，但本 package 未重新执行。

## Scope Assessment

本 package 保持在 v0.2 Recursive World Foundation scope 内：

- active runtime behavior 仍是 v0.1 scaffold behavior。
- v0.2 schema 和 event contracts 仍是 additive。
- `backend/worldengine/` 仍是 legacy。
- v0.3 bridge work 仍是 planned and unimplemented。
- 未引入 concrete external-world anchors。
