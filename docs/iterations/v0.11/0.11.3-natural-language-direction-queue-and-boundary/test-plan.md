# Test Plan

Chinese mirror: `test-plan.zh.md`.

Status: documentation drafted / review pending

## Exact Commands To Run

Documentation gate:

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" \
  docs/iterations/v0.11/0.11.3-natural-language-direction-queue-and-boundary \
  docs/iterations/v0.11/CURRENT_STATE.md \
  docs/iterations/v0.11/README.md \
  docs/iterations/v0.11/review.md
```

Implementation verification after authorization:

```bash
python3 -m pytest app/tests/test_session_direction_queue_api.py app/tests/test_world_direction_boundary.py app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

## Expected Results

- Documentation completeness returns no missing or empty package files.
- Authorization scan finds no premature implementation/live/external yes before
  the review gate.
- Focused backend tests pass.
- Accepted lightning-risk guidance returns queued external pressure or another
  allowed public category and does not mutate state.
- Direct final-fact guidance such as "kill this Agent now" is rejected and does
  not create a queued item.
- Private markers are rejected or redacted without public echo.
- Existing world-direction endpoint tests continue to pass.
- Manifest/discovery exposes session direction endpoints.
- Accepted and rejected session directions create replayable public operation
  evidence, such as event-log records, without raw instruction echo.
- Client-readable status/classification fields distinguish queued, rejected,
  allowed category, forbidden category, and `direct_state_mutation_applied:
  false`.

## Commands Not Run And Why

- Provider live smoke is not authorized for this package.
- External Validation Client automation is not authorized for this package.
- Frontend E2E is not planned unless implementation changes dashboard code.
- Autonomous Agent validation is out of v0.11.3 scope.

## Blocker Recording Rule

If a command fails, first repair issues inside this package contract. Record
`BLOCKED` only for external environment, provider authorization, Validation
Client/checker capability, or scope that belongs to another package.

## No Unverified Claims Rule

`review.md` may record only commands actually run in the current session. Do
not claim provider live, external validation, E2E, autonomous Agent, or full MVP
PASS from this package.
