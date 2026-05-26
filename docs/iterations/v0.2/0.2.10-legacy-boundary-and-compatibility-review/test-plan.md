# Test Plan

## Documentation Checks

- Verify the package has all required English and Chinese mirror documents.
- Verify package README status is `ready for review`.
- Verify the v0.2 milestone index records 0.2.10 as `ready for review`.
- Verify the v0.2 plan records 0.2.10 as `ready for review`.
- Verify Markdown diffs have no whitespace errors.
- Verify the changed-file set contains only approved documentation paths.
- Verify English and Chinese mirrors exist for the planned legacy boundary and
  compatibility review docs after implementation.

## Compatibility Checks After Review

- Confirm active backend and dashboard path claims against repository paths and
  current implementation docs.
- Confirm `backend/worldengine/` is documented as legacy and not presented as
  active runtime behavior.
- Confirm v0.1 runtime scaffold compatibility claims cite current
  implementation docs, backend implementation docs, API docs, package reviews,
  or current-session verification.
- Confirm v0.2 schema and event contract claims remain additive and are not
  described as runtime loading behavior.
- Confirm v0.3 handoff constraints are explicit for loader, runtime bridge,
  API compatibility, event compatibility, frontend compatibility, and legacy
  path handling.
- Check status consistency across English and Chinese v0.2 index and plan
  documents.
- Run a concrete demo anchor sweep over active direction and touched docs
  using a temporary untracked pattern file.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/$f.md" && test -f "docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/$f.zh.md" || exit 1; done
rg -n '0\.2\.10-legacy-boundary-and-compatibility-review|Status: ready for review|状态：`ready for review`' docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/README.md docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/README.zh.md
git diff --name-only
```

Implementation-stage documentation checks:

```bash
git status --short --branch
git diff --check
test -f docs/legacy-boundary.md
test -f docs/legacy-boundary.zh.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/compatibility-review.zh.md
rg -n 'backend/app|frontend|backend/worldengine|legacy|active|v0\.3' docs/legacy-boundary.md
rg -n 'runtime|API|frontend|schema|event|WorldSpec|compatibility|handoff' docs/iterations/v0.2/compatibility-review.md
git diff --name-only | rg -v '^(docs/legacy-boundary|docs/iterations/v0.2/)'
```

Concrete demo anchor sweep:

Use a temporary untracked pattern file under `/tmp` or another untracked path.
Run the sweep against active direction docs, legacy boundary docs,
compatibility review docs, and touched package docs. Record abstract match
categories only; do not write concrete pattern lists into tracked
documentation.

## Acceptance Criteria

- The documentation-stage package is complete and ready for review before
  boundary/review implementation starts.
- Acceptance and verification requirements are concrete and command-backed.
- Assumptions and open risks are recorded.
- The package remains documentation-only.
- Legacy boundary and compatibility review implementation produces English
  and Chinese mirrors.
- Missing evidence or compatibility concerns are captured as findings rather
  than code changes.
- Review evidence records changed files, commands, results, compatibility
  review, scope review, and unresolved findings.

## Not Run

Backend and frontend tests are not required for this documentation-stage pass.
They are also not expected during the boundary/review implementation because
this package forbids runtime, schema, API, frontend, fixture, migration, and
test implementation changes.
