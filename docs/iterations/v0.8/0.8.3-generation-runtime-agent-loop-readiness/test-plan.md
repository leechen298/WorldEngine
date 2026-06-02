# Test Plan

## Documentation Gate

```bash
git diff --check
```

Expected result: no output.

```bash
python3 -c '<0.8.3 required child docs and mirrors check>'
```

Expected result: `0.8.3-generation-runtime-agent-loop-readiness missing_child_docs=0`.

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result: `status_check_failures=0`.

```bash
python3 -c '<docs-only changed-file scope guard before implementation>'
```

Expected result: changed files are limited to `docs/iterations/v0.8/**` while
implementation remains unauthorized.

## Red Tests Before Implementation

After `implementation_authorized: yes`, add failing tests first:

- schema test for accepting exactly one of `worldspec` or `preview_request`.
- core test for successful candidate `WorldSpec` probe:
  - runtime readiness passed.
  - isolated runtime advances exactly once.
  - default Agent loop intent is `noop`.
  - result is not applied.
  - app runtime is not mutated.
- API test for `POST /world/generation/core-readiness`.
- API validation test for forbidden extra fields using existing 422 envelope.
- failure-path test where invalid preview or invalid `WorldSpec` returns
  diagnostics and no runtime/Agent success evidence.
- redaction test proving prompts/provider traces/secrets/private fields do not
  appear in returned evidence.

## Focused Implementation Verification

Run focused tests named by the implementation. Expected candidates:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Adjacent compatibility:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_runtime_step.py -q
```

## Scope and Claim Guards

```bash
python3 -c '<changed-file scope guard for approved code paths>'
```

Allowed paths after implementation:

- `docs/iterations/v0.8/**`
- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/tests/test_generation_core_readiness.py`
- `backend/app/tests/test_generation_core_readiness_api.py`

```bash
rg -n 'backend/worldengine|frontend|migrations|provider SDK|api_key|secret|raw_prompt|provider_trace|external validator|UI selector' <changed code files>
```

Expected result: no forbidden implementation hits except explicit rejection
tests or documentation non-claim text.

## Broad Regression Trigger

Run broader backend regression only if implementation changes shared behavior
outside the named route/helper/schema path or if adjacent focused tests fail in
a way that indicates shared API envelope or runtime behavior risk.
