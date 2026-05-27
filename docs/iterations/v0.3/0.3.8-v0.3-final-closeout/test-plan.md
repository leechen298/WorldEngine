# Test Plan

## Unit Tests

No unit tests are planned for the documentation stage or final closeout
implementation because this package must not modify runtime, schema, API,
frontend, fixture, migration, or test implementation files.

## Regression Tests

No backend, frontend, API smoke, E2E, Agent smoke, runtime, schema execution,
fixture, migration, or build regression tests are required for the
documentation stage. If final reviewers require fresh behavior evidence before
closeout, those commands must be run in the 0.3.8 implementation session and
recorded in `review.md`.

## Commands

Documentation-stage verification:

```bash
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.md" && test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.zh.md" || exit 1; done
rg -n '0\.3\.8-v0\.3-final-closeout|Status: ready for review|状态：`ready for review`' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md
rg -n 'final closeout|release-candidate|not released|P1|P2|P3|v0\.4|human / ChatGPT|historical evidence' docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
if rg -n '^\| [^|]+ \| [^|]+ \| [^|]+ \| P[12] \| (open|accepted handoff)' docs/iterations/v0.3/findings.md; then exit 1; else exit 0; fi
tmp_patterns="$(mktemp)"; p1="concrete"; p2="demo"; p3="external"; p4="validation"; printf '%s\n' "$p1-$p2-cell" "$p3-$p4-world" "$p1 concrete fixture path" > "$tmp_patterns"; rg -n -i -f "$tmp_patterns" docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md; rc=$?; rm -f "$tmp_patterns"; test "$rc" -eq 1
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
rg -n '[[:blank:]]$' docs/iterations/v0.3/0.3.8-v0.3-final-closeout docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
git status --short --branch
```

Expected implementation-stage verification after review approval:

```bash
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.md" && test -f "docs/iterations/v0.3/0.3.8-v0.3-final-closeout/$f.zh.md" || exit 1; done
rg -n 'final / closeout complete|final closeout complete|final review|no unresolved P1/P2|0\.3\.8|review complete|accepted handoff' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout/README.zh.md docs/iterations/v0.3/findings.md
if rg -n '^\| [^|]+ \| [^|]+ \| [^|]+ \| P[12] \| (open|accepted handoff)' docs/iterations/v0.3/findings.md; then exit 1; else exit 0; fi
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/(releases/v0\.3|iterations/v0\.3/)'
rg -n '[[:blank:]]$' docs/releases/v0.3.md docs/releases/v0.3.zh.md docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/findings.md docs/iterations/v0.3/0.3.8-v0.3-final-closeout
git status --short --branch
```

## Acceptance Criteria

- Package docs and Chinese mirrors exist for README, intent, contract,
  technical design, test plan, plan, and review.
- Documentation-stage status is `ready for review` in this package README and
  the v0.3 milestone index.
- Final release status remains gated until human / ChatGPT review approval.
- No unresolved P1/P2 finding is allowed to pass final closeout.
- Current-session verification distinguishes documentation checks from
  historical package test evidence.
- Changed files remain inside allowed documentation paths.
- No concrete demo world, concrete external validation world, fixture seed
  data, product UI, or application-specific backend details are introduced.

## Not Run

Backend, frontend, API smoke, E2E, Agent smoke, runtime behavior, build,
schema execution, fixture, migration, and test implementation checks are not
planned for the documentation-stage pass because it only creates package
documentation and status docs.
