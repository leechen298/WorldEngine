# Test Plan

## Verification Scope

This package is documentation-only. Verification focuses on document
presence, status consistency, release wording, mirror synchronization, scope
guardrails, and evidence traceability.

Backend, frontend, API smoke, E2E, Agent smoke, runtime, schema, fixture, and
migration tests are not required unless implementation files are changed. If
any such files change, stop and treat it as a contract violation.

## Required Checks

### Documentation Sanity

```bash
git diff --check
```

Expected result: exit `0`.

### Required File Presence

```bash
test -f docs/iterations/v0.2/v0.2-release-candidate-bundle.md
test -f docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md
test -f docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md
```

Expected result: all commands exit `0` after implementation.

### Package Mirror Presence

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/$f.md" &&
  test -f "docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/$f.zh.md" ||
  exit 1
done
```

Expected result: exit `0`.

### Status Consistency

```bash
rg -n '0\.2\.11-v0\.2-release-candidate-bundle|Status: ready for review|状态：`ready for review`|Status: review complete|状态：`review complete`' \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/README.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/README.zh.md
```

Expected result: exit `0`; statuses match the actual stage.

### Release-Status Wording Check

```bash
rg -n 'final release|not released|release candidate|release-candidate|0\.2\.12|final closeout' \
  docs/releases/v0.2.md \
  docs/releases/v0.2.zh.md \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.md \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md
```

Expected result: exit `0`; wording confirms candidate status and does not
claim final release.

### Evidence Traceability Check

```bash
rg -n '0\.2\.[1-9]|0\.2\.10|evidence-index|boundary-audit|compatibility-review|findings|review\.md|implemented|documented|tested|reviewed|planned|not implemented|historical artifact|finding' \
  docs/iterations/v0.2/v0.2-release-candidate-bundle.md \
  docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md
```

Expected result: exit `0`; release-candidate claims cite evidence and status
classes.

### Concrete Demo Anchor Sweep

Use a temporary untracked pattern file and record only abstract result
categories in `review.md`. Do not commit the concrete pattern list.

Expected result: no active-direction matches. Any residual matches must be
classified as historical package evidence, review-only text, or false
positive before final closeout proceeds.

### Changed-File Scope Guard

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/(releases/v0\.2|iterations/v0\.2/)'
```

Expected result: exit `1` with no output, meaning changed files are limited
to approved documentation paths.

## Tests Not Planned

- Backend tests are not planned because this package must not change backend
  implementation files.
- Frontend tests are not planned because this package must not change
  frontend implementation files.
- API smoke, E2E, Agent smoke, runtime, schema, fixture, and migration tests
  are not planned because this package is documentation-only.

## Failure Handling

- If a runtime, schema, API, frontend, fixture, migration, or test file
  changes, stop and revert only this package's out-of-scope edits with user
  approval.
- If a P1/P2 evidence gap appears, record it in `findings.md` and keep v0.2
  final closeout blocked.
- If release wording implies final status, correct the wording before review.
