# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

```bash
git diff --check
python3 required-file completeness check
rg status consistency checks
rg authorization scans
```

Expected results:

- `git diff --check` exits `0` with no output.
- required files are present and non-empty.
- no active implementation/provider/external-validation authorization is
  opened.
- final closeout classification is PARTIAL, not PASS.
- complete MVP PASS is not claimed.

## Commands Not Run

- Provider live calls: not authorized.
- External Validation Client automation: not available in this repository and
  already BLOCKED by `0.12.5`.
- Frontend/E2E: not part of closeout.
- Code tests: not required because closeout changes documentation only.

## Blocker Rule

Missing current v0.12 external Validation Client export remains the blocker for
complete MVP PASS and must remain visible in final closeout.
