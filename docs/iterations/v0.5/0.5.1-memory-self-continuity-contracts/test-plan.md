# Test Plan

Status: review complete

## Documentation Checks

Run from the repository root:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/',); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
python3 -c "from pathlib import Path; forbidden=('backend/app/','backend/worldengine/','frontend/','migrations/','fixtures/','test-results/'); bad=[p for p in Path('.').glob('**/*agent_memory*') if any(str(p).startswith(prefix) for prefix in forbidden)]; print('forbidden_agent_memory_paths=' + str(len(bad))); [print(str(p)) for p in bad]; raise SystemExit(1 if bad else 0)"
```

Expected results:

- `git diff --check` exits 0.
- package docs and mirrors check prints `missing=0`.
- changed-file scope guard prints `out_of_scope=0`.
- forbidden implementation path sentinel prints
  `forbidden_agent_memory_paths=0`.

## Evaluator Check

A read-only documentation/contract evaluator must review:

- all English package docs.
- Chinese mirror presence and status equivalence.
- concept/scope alignment with v0.5 parent docs.
- authorization criteria for `0.5.2`.
- absence of runtime, schema, API, frontend, test, fixture, migration, and
  `backend/worldengine/` changes.

The evaluator must report no P1 and no blocking P2 before closeout.

## Regression Tests

Backend, frontend, API, E2E, runtime, Agent smoke, autonomous validation,
build, fixture, migration, and external validation commands are not required
for this package because it is documentation-only and must not change
implementation surfaces.

## Acceptance Criteria

- All package docs and mirrors exist.
- Contract defines all six v0.5 public concepts.
- `0.5.2` authorization criteria are explicit.
- Review records exact documentation commands and evaluator findings.
- No implementation files are changed.
- No unresolved P1/P2 remains.

## Blocker Recording Rule

If any check fails, record the exact failure in `review.md`, fix only within
documentation scope, and rerun the failed command before claiming closeout.

If a required evaluator is unavailable, record `BLOCKED` or
`NEEDS_USER_INPUT` and do not close the package.

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

Reason: this package is documentation-only and changes no implementation,
runtime, API, frontend, fixture, migration, or validation-runner surfaces.
