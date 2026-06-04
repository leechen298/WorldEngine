# WorldEngine Full Lifecycle Autonomous Validation Rerun

Status: PASS
Mode: live full lifecycle validation plus saved-result checker
Date: 2026-06-04

Chinese mirror: `2026-06-04-worldengine-full-lifecycle-validation-rerun.zh.md`.

## Scope

This record captures the fresh rerun after
`0.8.9.2-director-guidance-public-redaction-repair` removed private/internal
marker wording from the public director guidance response and strengthened the
full lifecycle saved-result checker.

This is a testing result, not an iteration package. It does not rewrite the
earlier failed result in
`2026-06-04-worldengine-full-lifecycle-validation.md`.

## Scenario

Authoritative scenario:

- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`

Checker:

- `tools/testing/validate_agent_autonomous_result.py`

Result directory:

- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/`

Earlier confirmation result directory:

- `test-results/agent-autonomous/20260604T191709+0800-worldengine-full-lifecycle/`

Validation Client artifact source:

- `/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/validation-runs/playwright-artifacts/v0.7-ui-smoke-v0-7-browser-b9045-s-evidence-for-Agent-review/`

## Commands

```bash
PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/app/tests/test_public_handoff_contract_api.py -q
```

Result: `6 passed`.

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
```

Result: `19 passed`.

```bash
PYTHONPATH=backend backend/.venv/bin/python -m pytest backend/app/tests/test_world_generation_schema.py backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Result: `20 passed`.

```bash
WORLDENGINE_API_BASE=http://127.0.0.1:8000 VALIDATION_CLIENT_API_BASE=http://127.0.0.1:8765 pnpm --dir apps/web test:e2e
```

Result: `1 passed`.

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

Result:

```text
PASS: validated agent autonomous result at test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

## Covered Evidence

The rerun covered the required lifecycle surfaces:

- WorldEngine-backed world creation through the Validation Client.
- Public world id: `world-16df0fbcaa35`.
- Runtime progression: tick `0` to tick `10`.
- Events observed: `42`.
- Snapshots observed: `1`.
- WorldEngine-backed Agent action event observed: `1`, action type
  `params.applied`.
- Director guidance accepted through the public surface.
- Validation Client evidence bundle exported.
- Scorecard source: `scorecard_checker`, with six score items all `pass`.
- Validation Client redaction flags:
  `llm_keys_included=false`, `private_worldengine_internals_included=false`.

Supporting artifacts:

- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/result.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/world-lifecycle-summary.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/scorecard-summary.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/api-summary.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/validation-client-evidence-bundle.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/raw/worldengine-events.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/raw/worldengine-snapshots.json`
- `test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle/raw/validation-client-api-summary.json`

## Boundary

This PASS means the saved-result checker accepted the fresh full lifecycle
evidence for the documented scenario. It does not claim product readiness,
human validation PASS, LLM quality PASS, or external consumer certification.

Direct public API evidence is recorded in `api-summary.json`; no direct public
API call is recorded as an Agent operation-log CLI step.
