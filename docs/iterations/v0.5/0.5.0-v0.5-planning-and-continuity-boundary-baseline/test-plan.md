# Test Plan

Status: planned / ready for review

## Documentation Checks

Run from the repository root:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); child=parent/'0.5.0-v0.5-planning-and-continuity-boundary-baseline'; parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()]; missing += [str(child/(name+suffix)) for name in child_docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed='docs/iterations/v0.5/'; out=subprocess.check_output(['git','status','--short'], text=True); bad=[]; [bad.append(line) for line in out.splitlines() if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

Expected results:

- `git status --short --branch` shows only v0.5 documentation files as changed
  for this package.
- `git diff --check` exits 0.
- required docs and mirrors check prints `missing=0`.
- scope guard prints `out_of_scope=0`.

## Regression Tests

No backend, frontend, API, E2E, runtime, Agent smoke, autonomous validation,
build, fixture, migration, or external validation regression command is
required for `0.5.0`, because this package is documentation-only and must not
change implementation surfaces.

## Acceptance Criteria

- All required v0.5 parent and child docs exist with Chinese mirrors.
- `review.md` records changed files, commands, not-run implementation checks,
  compatibility review, scope review, subagent/evaluator findings, and
  unresolved findings.
- Implementation authorization remains `no`.
- No changed file appears outside `docs/iterations/v0.5/**`.
- No P1/P2 finding remains unresolved.

## Blocker Recording Rule

If any documentation check fails, record the exact failure in `review.md`,
fix within docs-only scope, and rerun the failed check before claiming the
package is ready for review.

If any implementation file appears in the scope guard, stop and do not
continue until the file set is reconciled with the package contract.

## Not Run

The following checks are intentionally not run:

- backend tests
- frontend tests
- E2E tests
- runtime/API smoke tests
- Agent smoke checks
- autonomous validation checks
- builds
- fixture validation
- migrations
- external validation runners

Reason: `0.5.0` is documentation-only and does not modify implementation,
runtime, API, frontend, fixture, migration, or validation-runner surfaces.

