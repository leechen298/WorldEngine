# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 required-file completeness check
rg -n "^implementation_authorized: yes|^evidence_execution_authorized: yes|^provider_live_call_authorized: yes|^external_validation_authorized: yes" docs/iterations/v0.12/0.12.5-full-lifecycle-checker-and-autonomous-validation docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
python3 package whitespace check
```

Expected results:

- `git diff --check` exits `0` with no output.
- package completeness returns `{'missing': [], 'empty': []}`.
- active yes authorization scan exits `1` before review authorization.
- package whitespace check returns an empty `problems` list.

## Checker Verification After Authorization

Run only after documentation review passes and
`evidence_execution_authorized: yes` is recorded:

```bash
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=tools/testing/fixtures/agent-autonomous/valid-worldengine-full-lifecycle
git diff --check
```

Expected results:

- fixture checker command exits `0`.
- full lifecycle fixture checker command exits `0`.
- invalid fixtures fail as expected through the fixture command.
- `git diff --check` exits `0`.

## Fresh External Validation Decision

If a current v0.12 external Validation Client result directory exists, run:

```bash
make validate-agent-autonomous-result RESULT_DIR=<current-v0.12-result-dir>
```

If no current result directory exists, record `fresh_external_validation_status:
BLOCKED` and do not claim v0.12 MVP PASS.

## Commands Not Run Unless Later Authorized

- Provider live calls: not authorized.
- External Validation Client implementation: forbidden in this repository.
- Frontend/E2E: not in this package.
- Complete MVP closeout: belongs to `0.12.6`.

## No-Unverified-Claims Rule

Do not claim fresh autonomous validation, provider live PASS, external
Validation Client PASS, or complete MVP PASS unless a current result directory
was checked in this session and the result is recorded.
