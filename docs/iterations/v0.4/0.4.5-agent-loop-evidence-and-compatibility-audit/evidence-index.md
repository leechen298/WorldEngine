# Evidence Index

Status: audit complete

Scope: v0.4 reviewed implementation and documentation evidence through final closeout repair.

## Current Evidence Boundary

This index records only current-session v0.4 evidence. Historical v0.3 evidence remains handoff context and is not counted as a v0.4 pass claim.

## Package Evidence

| Package | Type | Status | Evidence |
| --- | --- | --- | --- |
| `0.4.0-v0.4-planning-and-compatibility-baseline` | documentation-only | review complete | Documentation evaluator and closeout consistency review completed; no implementation files changed; documentation checks recorded in package review. |
| `0.4.1-agent-in-world-loop-contract` | documentation-only | review complete | Contract review closeout completed; no runtime, schema, API, or test implementation changes; documentation checks recorded in package review. |
| `0.4.2-agent-perception-and-schemas` | mixed/code | review complete | Red test for missing perception module; final perception tests `4 passed in 0.06s`; focused command `25 passed in 0.07s`; full backend regression `119 passed in 0.75s`; evaluator P1/P2 fixed before closeout. |
| `0.4.3-action-intent-validation-and-result-adapter` | mixed/code | review complete | Red test for missing action adapter; empty patch regression fixed; final adapter tests `6 passed in 0.09s`; focused command `25 passed in 0.44s`; full backend regression `125 passed in 0.82s`; evaluator P1/P2 fixed before closeout. |
| `0.4.4-minimal-agent-loop-orchestration-and-api` | mixed/code | review complete | Red test for missing loop service; final loop service/API tests `9 passed in 0.23s`; final repair focused backend/API command `35 passed in 0.55s`; final repair full backend regression `139 passed in 0.98s`; route-level invalid `params.patch` and nested patch-item extra coverage added after review findings. |

## Latest Command Evidence

Latest backend implementation evidence:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
9 passed in 0.23s

cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
35 passed in 0.55s

cd backend && .venv/bin/python -m pytest app/tests tests -q
139 passed in 0.98s
```

Latest documentation/scope evidence:

```text
git diff --check
passed

required docs/mirrors check for 0.4.5, including evidence index and compatibility audit
missing=0

changed-file scope guard
out_of_scope=0
```

## API Evidence

`backend/app/tests/test_agent_loop_api.py` is the FastAPI TestClient smoke for `POST /world/agent/loop/step`.

Covered API behaviors:

- default request without intent returns deterministic `noop`;
- accepted `params.patch` applies params and emits `params.applied` with `source="agent.loop"`;
- unsupported action returns HTTP 200 with rejected `ActionResult`;
- invalid `params.patch` returns HTTP 200 with rejected `ActionResult`, no mutation, and no `params.applied` event;
- request schema error keeps the existing 422 API envelope;
- nested patch-item unknown fields keep the existing 422 API envelope and do
  not mutate params or emit `params.applied`;
- existing `/world/agent/params/propose-and-apply` still applies the default mock patch.

## Commands Not Run

Frontend, browser E2E, Agent smoke, build, fixture, migration, and external validation runner commands were not run for v0.4 through this audit because the implementation packages did not authorize or touch those surfaces.

## Open Findings

- P1: none.
- P2: none.
- P3: none blocking at this audit boundary.

## Handoff

This evidence index supports `0.4.6-v0.4-release-candidate-bundle` preparation from the reviewed 0.4.5 audit record.
