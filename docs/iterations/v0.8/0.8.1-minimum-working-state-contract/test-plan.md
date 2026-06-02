# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
```

Expected result: changed/untracked files are limited to authorized
`docs/iterations/v0.8/**` documentation surfaces.

```bash
git diff --check
```

Expected result: exit `0` with no output.

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.8/0.8.1-minimum-working-state-contract")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_child_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Expected result: `missing_child_docs=0`.

```bash
python3 -c '<v0.8 parent/child status consistency check>'
```

Expected result: `status_check_failures=0`.

```bash
python3 -c '<v0.8 changed-file scope guard>'
```

Expected result: `out_of_scope_changed_or_untracked=0`.

```bash
python3 -c '<v0.8 markdown shape and authorization/claim guards>'
```

Expected result: no trailing whitespace, no tabs, no unauthorized
implementation/evidence execution, and no unverified positive PASS claims.

## Commands Not Run And Why

Backend, frontend, API, E2E, Agent smoke, autonomous, external validation, and
runtime tests are not run because this package is documentation-only and does
not authorize implementation or evidence execution.

## Blocker Recording Rule

Any failed documentation check, missing mirror, out-of-scope changed file,
positive readiness overclaim, or evaluator P1/P2 must be recorded as a blocker
in `review.md`.

## No Unverified Claims Rule

This package may claim only documentation checks that ran in the current
session. It must not claim minimum working-state, runtime, API, frontend, E2E,
Agent, autonomous, external validation, product, projection, or release pass.
