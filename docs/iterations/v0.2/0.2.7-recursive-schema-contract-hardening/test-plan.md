# Test Plan

## Documentation Checks

- Verify the package has all required English and Chinese mirror documents.
- Verify package README status is `ready for review`.
- Verify the v0.2 milestone index records 0.2.7 as `ready for review`.
- Verify Markdown diffs have no whitespace errors.
- Verify no runtime, API, frontend, fixture, migration, or test implementation
  files were changed during the documentation-stage pass.

## Unit Tests For Implementation Stage

Add or confirm focused tests for:

- EntityRef accepts non-empty generic `id` and `kind`, optional `label`, and
  default empty metadata.
- EntityRef rejects empty `id` and empty `kind`.
- WorldCell accepts default `kind = "world"`, empty entity refs, empty child
  cells, and empty metadata.
- WorldCell validates nested child cells recursively.
- WorldCell rejects non-world `kind`.
- WorldCell rejects invalid child cell payloads.
- WorldCell rejects invalid entity reference payloads.
- WorldSpec accepts `schema_version = "0.2"` and a required root WorldCell.
- WorldSpec rejects unsupported schema versions.
- WorldSpec rejects empty `id`.
- WorldSpec model_dump output can be model_validate'd back to an equivalent
  WorldSpec.
- Generic smoke payloads remain domain-neutral and contain no concrete
  external-world anchors.

Existing tests may satisfy these requirements. Implementation should add tests
only for uncovered cases.

## Regression Tests For Implementation Stage

- Existing backend schema tests must continue to pass.
- Existing backend app tests should pass if schema code changes.
- Event schema compatibility must not regress if schema imports or shared
  model behavior are touched.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
```

Implementation-stage checks, if only docs/contracts and tests are changed:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
make check-backend
```

Implementation-stage checks, if schema code changes:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py app/tests/test_event_schema_compat.py -q
make check-backend
cd backend && .venv/bin/python -m pytest app/tests -q
```

Concrete demo anchor sweep:

Use a temporary untracked pattern file under `/tmp` or another untracked path.
Run the sweep against touched docs and tests. Record only abstract match
categories in review evidence; do not write concrete pattern lists into
tracked documentation.

## Acceptance Criteria

- The documentation-stage package is complete and ready for review before
  implementation starts.
- Contract docs are planned for EntityRef, WorldCell, and WorldSpec.
- Acceptance requirements are testable with concrete commands.
- Assumptions and open risks are recorded.
- The package does not authorize loader, runtime bridge, generation,
  projection, memory, agent loop, frontend, fixture, migration, or external
  repository work.
- Implementation review must record changed files, commands, test results,
  compatibility review, scope review, and unresolved findings.

## Not Run

Backend and frontend tests are not required for this documentation-stage pass.
They must be run during implementation according to the command matrix above
if schema, test, or backend behavior files are changed.
