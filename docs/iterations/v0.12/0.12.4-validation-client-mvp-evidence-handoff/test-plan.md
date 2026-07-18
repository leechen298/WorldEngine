# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.4-validation-client-mvp-evidence-handoff')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
    'mvp-evidence-artifact-contract.md', 'mvp-evidence-artifact-contract.zh.md',
    'validation-client-handoff-prompt.md', 'validation-client-handoff-prompt.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "^implementation_authorized: yes|^provider_live_call_authorized: yes|^external_validation_authorized: yes" docs/iterations/v0.12/0.12.4-validation-client-mvp-evidence-handoff docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Documentation Verification

Expected coverage:

- artifact contract names required MVP files.
- result directory shape is explicit.
- operation-log and API-log fields are explicit.
- status taxonomy includes PASS, PARTIAL, BLOCKED, and FAIL.
- redaction markers include private memory, raw thought, provider trace, raw
  provider response, secrets, and token-style markers.
- terminology separates in-world Agents from external validation agents.
- handoff prompt tells Validation Client not to implement code in WorldEngine.
- no provider live-call, external validation execution, checker PASS, or MVP
  closeout is claimed.

Expected command results:

- `git diff --check` exits `0` with no output.
- required-file completeness returns `{'missing': [], 'empty': []}`.
- the active yes-authorization `rg` scan exits `1` because no active yes
  authorization fields are present.
- package whitespace check returns an empty `problems` list.

## Blocker Recording Rule

If documentation review finds that required evidence export depends on missing
external client capability, checker assets, provider/environment credentials,
permissions, or external repository access, record the issue as
`BLOCKED`/`PARTIAL` in review evidence instead of claiming PASS or fabricating
validation evidence.

## No-Unverified-Claims Rule

Do not claim provider live calls, external validation automation, checker
classification, code tests, frontend/E2E, or MVP PASS unless that command or
flow was run in the current work session and recorded with evidence.

## Commands Not Run Unless Later Authorized

- Provider live calls: not authorized.
- External Validation Client automation: not authorized.
- Full lifecycle checker/autonomous validation: belongs to `0.12.5`.
- Frontend/E2E: not in this package.
- Code tests: not required unless this package later authorizes schema/checker
  support changes.
