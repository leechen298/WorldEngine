# Test Plan

## Documentation Checks

- Verify the package has all required English and Chinese mirror documents.
- Verify package README status is `ready for review`.
- Verify the v0.2 milestone index records 0.2.9 as `ready for review`.
- Verify the v0.2 plan records 0.2.9 as `ready for review`.
- Verify Markdown diffs have no whitespace errors.
- Verify the changed-file set contains only approved documentation paths.
- Verify English and Chinese mirrors exist for the planned evidence index and
  boundary audit after implementation.

## Audit Checks After Review

- Map active v0.2 claims from the milestone index, plan, roadmap, and scope
  boundary docs to evidence rows.
- Confirm schema claims cite EntityRef, WorldCell, WorldSpec contracts and
  package review evidence.
- Confirm event claims cite EventRef contract and package review evidence.
- Confirm external boundary claims cite boundary docs and cleanup package
  evidence.
- Confirm legacy boundary claims cite current implementation docs and remain
  as handoff input for 0.2.10 where needed.
- Check status consistency across English and Chinese v0.2 index and plan
  documents.
- Check the deferred 0.2.7 status finding and either close it with evidence or
  leave it open with updated rationale.
- Run concrete demo anchor sweep over active direction and audit docs using a
  temporary untracked pattern file.

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/$f.md" && test -f "docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/$f.zh.md" || exit 1; done
rg -n '0\.2\.9-generic-schema-evidence-and-boundary-audit|Status: ready for review|状态：`ready for review`' docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.md docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.zh.md
git diff --name-only
```

Implementation-stage documentation checks:

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/evidence-index.zh.md
test -f docs/iterations/v0.2/boundary-audit.md
test -f docs/iterations/v0.2/boundary-audit.zh.md
rg -n 'implemented|documented|tested|reviewed|planned|not implemented|historical artifact|finding' docs/iterations/v0.2/evidence-index.md
rg -n 'external|fixture|legacy|runtime|schema|event|status' docs/iterations/v0.2/boundary-audit.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

Concrete demo anchor sweep:

Use a temporary untracked pattern file under `/tmp` or another untracked path.
Run the sweep against active direction docs, evidence index, boundary audit,
and touched package docs. Record abstract match categories only; do not write
concrete pattern lists into tracked documentation.

## Acceptance Criteria

- The documentation-stage package is complete and ready for review before
  audit implementation starts.
- Acceptance and verification requirements are concrete and command-backed.
- Assumptions and open risks are recorded.
- The package remains documentation-only.
- Audit implementation produces evidence index and boundary audit mirrors.
- Missing evidence is captured as findings rather than code changes.
- Review evidence records changed files, commands, results, compatibility
  review, scope review, and unresolved findings.

## Not Run

Backend and frontend tests are not required for this documentation-stage pass.
They are also not expected during the audit implementation because this package
forbids runtime, schema, API, frontend, fixture, migration, and test
implementation changes.
