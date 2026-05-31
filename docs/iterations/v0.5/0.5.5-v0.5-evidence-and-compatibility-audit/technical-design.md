# Technical Design

Status: review complete

## Design Type

Documentation-only audit.

No runtime, schema, service, API, frontend, migration, fixture, or test
implementation is authorized.

## Audit Inputs

The audit reads:

- child package reviews for `0.5.1` through `0.5.4`.
- current git status and diff scope.
- current docs/mirror checks.
- current focused and broad backend test results when needed to refresh
  implementation evidence.

## Audit Model

Evidence is classified into four groups:

- contract evidence: docs-only concept and authorization checks.
- implementation evidence: TDD, tests, code review, validation evidence.
- compatibility evidence: adjacent and broad regression tests for touched
  surfaces.
- scope evidence: changed-file guards and forbidden-surface sentinels.

## Current Implementation Surface

`0.5.2` and `0.5.3` are the only implementation-bearing v0.5 child packages.

Current implementation files are:

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`

## Audit Output

The audit output lives in this package's `contract.md` and `review.md`. No
separate generated artifact is required for `0.5.5`.

`0.5.6` may use this audit as input for a release-candidate bundle.
