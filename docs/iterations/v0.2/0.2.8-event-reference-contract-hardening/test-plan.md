# Test Plan

## Documentation Checks

- Verify the package has all required English and Chinese mirror documents.
- Verify package README status is `ready for review`.
- Verify the v0.2 milestone index records 0.2.8 as `ready for review`.
- Verify Markdown diffs have no whitespace errors.
- Verify no runtime, schema, API, frontend, fixture, migration, or test
  implementation files were changed during the documentation-stage pass.

## Unit Tests For Implementation Stage

Add or confirm focused tests for:

- Event construction without `refs` still validates and produces `refs == []`.
- Event accepts refs with non-empty generic `id` and `kind`.
- EventRef accepts optional `role`.
- EventRef accepts omitted `metadata` and defaults it to `{}`.
- EventRef accepts free-form metadata without v0.2 runtime interpretation.
- EventRef rejects empty `id`.
- EventRef rejects empty `kind`.
- Event model_dump output can be model_validate'd back to an equivalent Event
  while preserving refs.
- EventPage validates events with and without refs.
- EventStep and EventStepPage validate nested events with refs.
- Generic test payloads remain domain-neutral and contain no concrete
  external-world anchors.

Existing tests may satisfy these requirements. Implementation should add
tests only for uncovered cases.

## Regression Tests For Implementation Stage

- Existing event schema compatibility tests must continue to pass.
- Existing backend app tests should pass if event schema code changes.
- Recursive schema tests should not be affected if shared schema behavior or
  contract imports are touched.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
```

Implementation-stage checks, if only docs/contracts and focused tests are
changed:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
make check-backend
```

Implementation-stage checks, if event schema code changes:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
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
- Contract documentation is planned for EventRef and Event.refs.
- Acceptance requirements are testable with concrete commands.
- Assumptions and open risks are recorded.
- The package does not authorize resolver, causality, runtime bridge,
  generation, projection, memory, agent loop, frontend, fixture, migration,
  external repository, or API route work.
- Implementation review must record changed files, commands, test results,
  compatibility review, scope review, and unresolved findings.

## Not Run

Backend and frontend tests are not required for this documentation-stage pass.
They must be run during implementation according to the command matrix above
if schema, test, or backend behavior files are changed.
