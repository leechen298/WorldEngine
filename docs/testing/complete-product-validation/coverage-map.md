# Complete Product Validation Coverage Map

Status: planned coverage map

Chinese mirror: `coverage-map.zh.md`.

## Source Of Truth

Coverage is derived from:

- `docs/project-north-star.md`.
- `docs/product-model.md`.
- `docs/scope-boundaries.md`.
- `docs/roadmap.md`.
- current `docs/testing/` scenario contracts and playbooks.

The map is intentionally product-wide. A specific validation run may mark some
areas `out_of_scope`, but it must not silently omit them when claiming complete
product validation.

## Capability Taxonomy

| ID | Capability area | What must eventually be testable | Primary evidence types |
| --- | --- | --- | --- |
| CPV-01 | Governance and scope boundary | Work stays aligned with North Star, active code path, iteration gates, no demo-specific core data, no external validation internals in core. | docs audit, scope guard, review evidence. |
| CPV-02 | Recursive world schema | `WorldCell`, `WorldSpec`, refs, additive event references, schema compatibility, invalid payload rejection. | unit tests, schema smoke, contract docs. |
| CPV-03 | WorldSpec loader and runtime bridge | Valid generic world specs can load into runtime context without breaking v0.1 runtime compatibility. | backend focused tests, API summaries. |
| CPV-04 | World generation | Deterministic templates, structured generation plans, import boundaries, preview, regeneration, runtime-readiness, LLM-backed generation when implemented. | backend tests, E2E, generation summaries, LLM redacted evidence. |
| CPV-05 | Runtime progression | Ticks advance time, rules are evaluated, state changes are applied, and runtime does not rely on hidden side effects. | backend tests, events, snapshots, lifecycle summaries. |
| CPV-06 | Event spine and timeline | Events are appendable, queryable, typed, redacted, reference-capable, and usable as the system spine. | event API tests, timeline E2E, API summary, event artifacts. |
| CPV-07 | Snapshots, replay, and recovery | Snapshots are produced, replay can inspect historical state, and branch-like worldlines can be tracked without app-specific assumptions. | snapshot artifacts, replay summaries, E2E, Validation Client evidence. |
| CPV-08 | Parameters and state diffs | Params validate, apply, reject invalid/reserved paths, and produce reviewable diffs. | backend tests, params-flow E2E, Agent smoke. |
| CPV-09 | Agent minimal loop | Agents perceive events, produce action intents, execute supported actions, and receive results through public contracts. | backend tests, API tests, Agent loop E2E. |
| CPV-10 | Agent memory substrate | Working memory, episodic memory, memory context, isolation, and read-only perception boundaries work. | backend tests, memory summaries, archive summaries. |
| CPV-11 | Agent self-continuity and pseudo-self | Public evidence can show identity continuity, self-summary, relationship history, personality drift signals, intent, reflection, and behavior over time when implemented. | Agent autonomy summaries, snapshots, second-Agent review. |
| CPV-12 | LLM provider integration | Provider env readiness and minimal live calls work through WorldEngine, not the client, with redacted evidence. | provider live summary, checker output. |
| CPV-13 | LLM-backed world creation and evolution | User premise creates system-digestible public state, parameters, rules, legality constraints, and rule-driven evolution. | LLM-backed lifecycle summaries, scorecard, checker. |
| CPV-14 | Event legality and external guidance | Random events and user direction affect only external environment, and outcomes are adjudicated by world rules. | event legality summaries, diffs, snapshots. |
| CPV-15 | Projection and read models | Public consumers can inspect bounded read-only projections without private app state or write capability. | projection schema/checker, API summary, external reports. |
| CPV-16 | Dashboard and local UI | Dashboard runtime, params, timeline, archive summary, Agent tools, and generation preview remain usable. | frontend unit tests, build, Playwright E2E. |
| CPV-17 | External Validation Client handoff | External client can consume public APIs/contracts, log operations, export evidence, and avoid owning engine logic. | cross-repo evidence bundle, public API summary, operation log. |
| CPV-18 | Agent-assisted testing | Agent smoke and autonomous saved-result validation use allowed operations and checker-controlled PASS sources. | operation logs, result.json, scorecard, checker output. |
| CPV-19 | Evidence, redaction, and reports | Evidence records are complete, redacted, durable, and reviewable; secrets/private internals never leak. | redaction scan, evidence bundle, result summaries. |
| CPV-20 | Reliability, compatibility, and regressions | Focused tests and broad regressions protect old versions, APIs, schemas, dashboard behavior, and testing tools. | command matrix, full backend/frontend/E2E outputs. |

## Complete Validation Layers

| Layer | Name | Covers |
| --- | --- | --- |
| L0 | Documentation and scope audit | CPV-01, current state, claim boundaries. |
| L1 | Schema and contract validation | CPV-02, CPV-15, CPV-19. |
| L2 | Backend unit and API compatibility | CPV-03 through CPV-10, CPV-20. |
| L3 | Generation and import validation | CPV-04, CPV-13 preconditions. |
| L4 | Runtime lifecycle validation | CPV-05 through CPV-08. |
| L5 | Agent loop and memory validation | CPV-09 through CPV-11. |
| L6 | Frontend and dashboard E2E | CPV-16. |
| L7 | Agent smoke validation | CPV-18 focused smoke. |
| L8 | Autonomous saved-result validation | CPV-17 through CPV-19 recorded evidence. |
| L9 | LLM-backed lifecycle validation | CPV-12 through CPV-14 plus CPV-11. |
| L10 | External client evidence review | CPV-17 through CPV-19. |
| L11 | Final verdict audit | All in-scope CPV items. |

## Minimum Complete-Run Requirement

A future "complete product validation" run must produce a matrix with every
CPV row and one of:

- `pass`.
- `fail`.
- `blocked`.
- `skipped`.
- `out_of_scope`.

No row may be omitted. If a capability is future roadmap scope, mark it
`out_of_scope` and explain why. If it is expected current scope but unsupported,
mark it `fail` or `blocked`, not `pass`.
