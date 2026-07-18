# Test Plan

Chinese mirror: `test-plan.zh.md`.

Status: documentation drafted / review pending

## Exact Commands To Run

Documentation gate:

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.5-worldview-fidelity-and-v0.11-validation')
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
  docs/iterations/v0.11/0.11.5-worldview-fidelity-and-v0.11-validation \
  docs/iterations/v0.11/CURRENT_STATE.md \
  docs/iterations/v0.11/README.md \
  docs/iterations/v0.11/review.md
```

Evidence/implementation verification after authorization:

```bash
python3 -m pytest app/tests/test_worldview_fidelity_evaluation.py app/tests/test_session_rule_bound_evolution_api.py app/tests/test_rule_linked_evolution_legality.py app/tests/test_provider_worldview_preflight_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

## Expected Results

- Documentation completeness returns no missing or empty package files.
- Authorization scan finds no premature implementation/live/external yes before
  the review gate.
- Focused backend tests pass.
- Immediate fidelity passes only when public premise indicators are covered and
  no generic fallback/redaction failure exists.
- Bounded-run fidelity blocks when public run evidence is missing.
- Scorecard final status reflects immediate and bounded-run evidence.
- Redaction tests prove raw/private evidence is not echoed.
- v0.11 closeout records what was not run: provider live, external Validation
  Client, Agent autonomy, and complete MVP automation.

## Commands Not Run And Why

- Provider live smoke is not authorized for this package.
- External Validation Client automation is not authorized for this package.
- Frontend E2E is not planned because this package does not change frontend.
- Autonomous Agent validation is out of v0.11.5 scope.

## Blocker Recording Rule

If a command fails, first repair issues inside this package contract. Record
`BLOCKED` only for external environment, provider authorization, Validation
Client/checker capability, or scope that belongs to another package.

## No Unverified Claims Rule

`review.md` may record only commands actually run in the current session. Do
not claim provider live, external validation, frontend E2E, autonomous Agent,
v0.12 readiness, or full MVP PASS from this package.
