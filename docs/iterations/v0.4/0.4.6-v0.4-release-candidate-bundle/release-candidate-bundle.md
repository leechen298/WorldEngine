# Release Candidate Bundle

Status: release-candidate bundle complete

Scope: v0.4 release-candidate evidence package. This document does not declare final release or final closeout.

## Candidate Summary

v0.4 implements the minimal request-driven Agent-in-World loop:

- bounded perception from runtime state, recent events, world params, and optional runtime context summary;
- inspectable `ActionIntent` and `ActionResult` schemas;
- supported actions: `noop` and validated `params.patch`;
- request-scoped loop service;
- additive API route: `POST /world/agent/loop/step`;
- compatibility-preserving reuse of existing world params validation, dry-run, apply, event log, runtime state, and API envelope patterns.

## Package Statuses

| Package | Status | Release-Candidate Input |
| --- | --- | --- |
| `0.4.0-v0.4-planning-and-compatibility-baseline` | review complete | v0.4 plan, campaign controls, compatibility baseline. |
| `0.4.1-agent-in-world-loop-contract` | review complete | public concepts, implementation authorization rules, API/error/event boundaries. |
| `0.4.2-agent-perception-and-schemas` | review complete | `PerceptionFrame`, runtime/context summary schemas, `PerceptionBuilder`, focused/backend evidence. |
| `0.4.3-action-intent-validation-and-result-adapter` | review complete | `ActionIntent`, `ActionResult`, `ActionResultAdapter`, validated action results, focused/backend evidence. |
| `0.4.4-minimal-agent-loop-orchestration-and-api` | review complete | `AgentLoopService`, loop-step API route, app factory wiring, focused/API/backend evidence. |
| `0.4.5-agent-loop-evidence-and-compatibility-audit` | review complete | evidence index, compatibility audit, docs-only scope evidence. |

## Current Evidence Snapshot

Latest implementation evidence:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
9 passed in 0.23s

cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
35 passed in 0.55s

cd backend && .venv/bin/python -m pytest app/tests tests -q
139 passed in 0.98s
```

Latest documentation-only evidence for audit packaging:

```text
git diff --check
passed

0.4.5 required docs/mirrors check, including evidence index and compatibility audit
missing=0

changed-file scope guard
out_of_scope=0
```

## Public Interface Candidate

Schemas:

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- `LoopStepRequest`
- `LoopStepResponse`

API:

- `POST /world/agent/loop/step`

Compatibility-sensitive existing API:

- `/world/agent/params/propose-and-apply` remains available and unchanged.

## Compatibility Claims

The release candidate carries these reviewed claims:

- schema additions are additive;
- runtime tick/time behavior remains compatible;
- event route compatibility remains covered;
- world params validation/apply behavior remains compatible;
- successful loop `params.patch` emits `params.applied` with `source="agent.loop"`;
- rejected actions and no-op actions do not emit events;
- unsupported or invalid loop actions return HTTP 200 with rejected `ActionResult`;
- invalid request bodies keep the existing 422 API envelope;
- archive, frontend, fixture, migration, and legacy `backend/worldengine/` surfaces remain unchanged.

## Commands Not Run For 0.4.6

Backend, frontend, API smoke, E2E, Agent smoke, runtime behavior, build, schema execution, fixture, migration, and test implementation commands were not run for this package because `0.4.6` is documentation-only and does not modify implementation files.

## Open Findings

- P1: none.
- P2: none.
- P3: none blocking at release-candidate packaging boundary.

## Final Review Questions For 0.4.7

Before final closeout, `0.4.7` must confirm:

1. Are `0.4.0` through `0.4.6` all `review complete`?
2. Does the latest backend implementation evidence still support v0.4 pass claims?
3. Do documentation-only checks still pass after the final bundle is written?
4. Are there any unresolved P1 or P2 findings?
5. Are frontend/E2E/build/fixture/migration commands still correctly recorded as not run because no corresponding surface changed?
6. Do the Chinese mirrors match the final closeout status and evidence?
7. Does final closeout avoid declaring v0.5 memory, v0.6 generation, v0.7 external validation, v0.8 projection, or concrete world/demo readiness?

## Handoff

This release-candidate bundle is ready for `0.4.7-v0.4-final-closeout` review. Final release or closeout must be declared only by `0.4.7`.
