# Test Plan

## Verification Scope

This is a documentation-only package. Verification checks documentation
presence, status consistency, release wording, mirror synchronization, boundary
language, and changed-file scope.

Runtime, schema, API, frontend, fixture, migration, and test implementation
behavior are out of scope unless a reviewer explicitly asks for read-only
regression commands and those commands are run in the current 0.2.12 session.

## Required Documentation Checks

Run during documentation-stage preparation:

```bash
git diff --check
```

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.2/0.2.12-v0.2-final-closeout/$f.md" &&
  test -f "docs/iterations/v0.2/0.2.12-v0.2-final-closeout/$f.zh.md" ||
  exit 1
done
```

```bash
rg -n '0\.2\.12-v0\.2-final-closeout|Status: ready for review|状态：`ready for review`' \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.md \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.zh.md
```

```bash
rg -n 'final closeout|release-candidate|not final|P1|P2|P3|v0\.2-P3-003|v0\.3 handoff|human / ChatGPT' \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md
```

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.2/'
```

```bash
rg -n '[[:blank:]]$' \
  docs/iterations/v0.2/0.2.12-v0.2-final-closeout \
  docs/iterations/v0.2/README.md \
  docs/iterations/v0.2/README.zh.md \
  docs/iterations/v0.2/v0.2-plan.md \
  docs/iterations/v0.2/v0.2-plan.zh.md
```

## Required Implementation-Stage Checks

Run after review approval if final closeout is implemented:

- `git diff --check`
- required file presence check for package mirrors.
- status consistency grep across package README, milestone index, plan docs,
  and release docs.
- release-status wording check proving final status is present only when
  approval is recorded.
- blocker wording check proving unresolved P1/P2 findings are absent or
  explicitly resolved before final status.
- concrete demo anchor sweep over touched closeout docs.
- changed-file scope guard proving only approved documentation paths changed.

## Not Planned

- backend tests.
- frontend tests.
- API smoke.
- E2E tests.
- Agent smoke or autonomous tests.
- runtime behavior tests.
- schema execution tests.
- fixture or migration tests.

These remain not planned because 0.2.12 is documentation-only. If any
implementation file changes, this test plan is invalid and the package must
stop for review.

## Pass Criteria

- Documentation checks exit successfully or expected no-match checks are
  explained in `review.md`.
- Status wording is synchronized across English and Chinese mirrors.
- Final closeout remains gated on approval.
- No runtime, schema, API, frontend, fixture, migration, or test
  implementation files are modified.
