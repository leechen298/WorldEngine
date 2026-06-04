# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Mode

This package uses focused backend regression plus saved-result checker
verification. Full lifecycle autonomous validation is required for a full PASS
claim only when the external Validation Client environment is available.

## RED Test

Before changing runtime code, update or add the focused public handoff API test
so it fails against the current implementation:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

Expected RED failure: director guidance `public_explanation` contains forbidden
public evidence markers or protected private/internal wording.

## Focused Backend Tests

After implementation, run:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

Expected result: pass.

Then run the related 0.8.9.1 regression set:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_world_generation_schema.py backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Expected result: pass.

## Full Backend Regression

Run:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests -q
```

Expected result: pass, unless a failure is unrelated and recorded with exact
evidence and scope rationale.

## Saved-Result Checker

First, keep the historical failed result honest:

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle
```

Expected result before a new rerun: fail with the known redaction failure. Do
not rewrite old artifacts to pass.

After package review explicitly records both `implementation_authorized: yes`
and `evidence_execution_authorized: yes`, and after a new full lifecycle run
creates a fresh result directory, run:

```bash
make validate-agent-autonomous-result RESULT_DIR=<new-result-dir>
```

Expected result for full closeout: pass.

If `evidence_execution_authorized: yes` is not recorded, do not start a live
full lifecycle rerun. Record the rerun as not authorized and limit closeout to
focused repair evidence.

## Optional Runtime Probe

If implementation changes are complete and local services can be started, run:

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project uvicorn app.main:app --host 127.0.0.1 --port 8000
curl -s -o /tmp/we-director-0.8.9.2.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"instruction_text":"public world guidance"}' http://127.0.0.1:8000/worlds/world-public/director-guidance
rg -n "api_key|apikey|authorization|credential|hidden_context|private_prompt|provider_secret|raw_request|raw_response|self_state|private memory|private goal|relationship internals|hidden context" /tmp/we-director-0.8.9.2.json
```

Expected result: HTTP `200`; forbidden-marker scan has no matches.

## Documentation Checks

Run:

```bash
git diff --check
rg -n "implementation_authorized: yes|Status: implementation complete|Status: review complete|PASS_READY_FOR_HUMAN_VALIDATION|Codex autonomous validation PASS|human validation PASS|external validation PASS" docs/iterations/v0.8/0.8.9.2-director-guidance-public-redaction-repair docs/iterations/v0.8/README.md docs/iterations/v0.8/README.zh.md docs/iterations/v0.8/CURRENT_STATE.md docs/iterations/v0.8/CURRENT_STATE.zh.md
```

During documentation stage, expected result: no implementation or PASS claims
except quoted forbidden search terms in `test-plan.md` or `review.md`.

## Not Run

During documentation-stage package creation, do not run backend or autonomous
validation as PASS evidence. Runtime implementation is not authorized yet.
