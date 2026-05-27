# Test Plan

## Verification Scope

This package is documentation-only. Verification focuses on document
presence, status consistency, release-candidate wording, mirror
synchronization, changed-file scope, unresolved findings visibility, and
evidence traceability.

Backend, frontend, API smoke, E2E, Agent smoke, runtime, schema, fixture,
migration, and build tests are not required unless implementation files are
changed. If any such file changes, stop and treat it as a contract violation.

## Required Checks

### Documentation Sanity

```bash
git diff --check
```

Expected result: exit `0`.

### Required File Presence

```bash
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.md
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
```

Expected result: all commands exit `0`.

### Package Mirror Presence

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.md" &&
  test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.zh.md" ||
  exit 1
done
```

Expected result: exit `0`.

### Status Consistency

```bash
rg -n '0\.3\.7-v0\.3-release-candidate-bundle|Status: ready for review|状态：待评审|状态：`待评审`' \
  docs/iterations/v0.3/README.md \
  docs/iterations/v0.3/README.zh.md \
  docs/iterations/v0.3/v0.3-plan.md \
  docs/iterations/v0.3/v0.3-plan.zh.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.zh.md
```

Expected result: exit `0`; statuses match documentation-stage review
readiness.

### Release-Status Wording Check

```bash
rg -n 'not final|not released|release candidate|release-candidate|0\.3\.8|final closeout|final release' \
  docs/releases/v0.3.md \
  docs/releases/v0.3.zh.md \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.md \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
```

Expected result: exit `0`; wording confirms candidate status and does not
claim final release.

### Evidence Traceability Check

```bash
rg -n '0\.3\.[0-7]|evidence-index|compatibility-audit|findings|review\.md|implemented|documented|tested|planned|not implemented|partial|historical|finding' \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
```

Expected result: exit `0`; release-candidate claims cite evidence and status
classes.

### Concrete Demo Anchor Sweep

Use a temporary untracked pattern file and record only abstract result
categories in `review.md`. Do not commit the concrete pattern list.

Expected result: no active-direction matches. Any residual matches must be
classified as historical package evidence, review-only text, or false
positive.

### Changed-File Scope Guard

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
```

Expected result: exit `1` with no output, meaning changed files are limited
to approved v0.3 iteration documentation paths.

## Tests Not Planned

- Backend tests are not planned because this package must not change backend
  implementation files.
- Frontend tests are not planned because this package must not change frontend
  implementation files.
- API smoke, E2E, Agent smoke, runtime, schema, fixture, migration, and build
  tests are not planned because this package is documentation-only.

## Failure Handling

- If an implementation file changes, stop and revert only this package's
  out-of-scope edits with user approval.
- If a P1/P2 evidence gap appears, record it visibly and keep final closeout
  blocked.
- If release wording implies final status, correct the wording before review.
