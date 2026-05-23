# Test Plan

## Verification Scope

This is a documentation-only package. Verification checks that:

- required scenario documents exist.
- key verdict-source and operation-boundary terms are present.
- the diff is limited to `docs/`.
- whitespace checks pass.

## Commands

Run:

```bash
git status --short --branch
git diff --check
find docs/testing/e2e-scenarios -maxdepth 1 -type f | sort
find docs/testing/agent-smoke/scenarios -maxdepth 1 -type f | sort
find docs/testing/agent-autonomous -maxdepth 2 -type f | sort
rg -n "direct API|verdict_source|deterministic_checker|operation-log|Playwright assertion|full Agent autonomous|curl smoke|scorecard" docs/testing docs/iterations/v0.1/0.1.6-current-code-test-case-expansion
git diff --name-only | rg -v '^(docs/)'
```

The final command must have no output. If it has output, the package violated
the docs-only boundary and must stop for correction.

## Commands Not Run

Do not run as part of 0.1.6:

- backend tests.
- frontend unit tests.
- `make test-e2e`.
- live Agent smoke.
- Codex/test-runner autonomous tests.
- API curl smoke.

## PASS Criteria

- All documentation verification commands pass.
- Scenario file listings include the expected files.
- Required terms appear in the new and updated docs.
- The docs-only boundary command has no output.
- `review.md` records that no new E2E, live Agent smoke, or Codex autonomous
  test was run or reported as passed.
