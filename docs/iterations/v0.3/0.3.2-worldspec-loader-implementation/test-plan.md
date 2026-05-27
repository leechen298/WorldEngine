# Test Plan

## Unit Tests

Add `backend/app/tests/test_worldspec_loader.py` with focused tests for:

- valid minimal mapping input.
- valid JSON string input.
- valid JSON bytes input.
- optional valid file-backed JSON input, if file loading is implemented.
- unsupported input type returning `unsupported_input`.
- malformed JSON returning `parse_error`.
- unsupported `schema_version` returning `schema_validation_error`.
- invalid root cell data returning `schema_validation_error`.
- error `path` normalization using JSON Pointer-style paths, including
  `/schema_version` for unsupported schema versions and a `/root/...` path for
  invalid root cell data.
- non-locatable loader errors, such as unsupported input or unlocatable parse
  failures, returning `path = None`.
- successful result metadata: `source_type`, optional `source_label`, and
  validated `schema_version`.
- no `RuntimeEngine`, API, event, archive, params, persistence, frontend,
  fixture, migration, or legacy side effects.

## Regression Tests

Run existing schema smoke tests that cover `WorldSpec` validation. Run broader
backend tests only if implementation touches shared helpers beyond the loader
module or test file.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.zh.md
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.2-worldspec-loader-implementation' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation
rg -n 'unsupported_input|parse_error|schema_validation_error|io_error|RuntimeEngine|WorldSpec|source_type|source_label|JSON Pointer|/schema_version|/root' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

Implementation-stage checks:

```bash
git status --short --branch
git diff --check
pytest backend/app/tests/test_worldspec_loader.py
pytest backend/app/tests/test_worldspec_schema_smoke.py
! rg -n 'RuntimeEngine|runtime_engine|FastAPI|APIRouter|archive|params|event' backend/app/core/worldspec_loader.py
! rg -n 'concrete demo|character|location|story rule|external validation-world data|private oracle' backend/app/core/worldspec_loader.py backend/app/tests/test_worldspec_loader.py
```

The runtime/API coupling and concrete-anchor sweeps are no-match checks. If an
implementation needs a term only in a negative test or explanatory comment,
run the matching `rg -n ...` command without `!`, review each match, and record
the rationale in `review.md` before implementation closes.

## Acceptance Criteria

- Required package docs and Chinese mirrors exist.
- Package README and milestone index mark 0.3.2 as `ready for review` /
  `待评审`.
- Documentation states assumptions, open risks, allowed changes, forbidden
  changes, deterministic loader error path style, and testable acceptance
  requirements.
- Implementation adds only the approved loader module and focused tests unless
  review approves a narrower local helper.
- Focused loader tests pass in the current implementation session.
- Existing `WorldSpec` schema smoke tests pass in the current implementation
  session.
- Scope checks show no runtime, schema, API, frontend, fixture, migration,
  persistence, archive, params, event, or legacy implementation changes unless
  explicitly approved by this package contract.
- Concrete anchor sweep shows no introduced concrete demo-world or external
  validation-world content.

## Not Run

During documentation stage, backend, frontend, API, E2E, Agent smoke, and
runtime behavior tests are not planned because implementation files are not
modified.

During implementation stage, any skipped verification must be recorded in
`review.md` with the reason and residual risk.
