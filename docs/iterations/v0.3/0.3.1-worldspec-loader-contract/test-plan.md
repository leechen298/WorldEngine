# Test Plan

## Documentation Checks

- Verify required package files exist.
- Verify `docs/contracts/worldspec-loader-contract.md` contains required
  loader concepts, accepted input forms, output fields, and error categories.
- Verify English and Chinese milestone indexes mark 0.3.1 as `ready for
  review` / `待评审`.
- Verify touched documentation does not include concrete demo-world anchors.
- Verify changed files stay inside allowed documentation paths.

## Future Implementation Tests

`0.3.2-worldspec-loader-implementation` should add focused tests for:

- valid minimal mapping input.
- valid JSON string or bytes input.
- optional file-backed JSON input if implemented.
- unsupported input type.
- malformed JSON parse error.
- schema validation failure for unsupported `schema_version`.
- schema validation failure for invalid root cell.
- neutral source metadata in successful output.
- no `RuntimeEngine`, event, archive, params, API, persistence, or frontend
  side effects.

These tests are not implemented or run in this documentation-only package.

## Commands

```bash
git status --short --branch
git diff --check
test -f docs/contracts/worldspec-loader-contract.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.md
rg -n 'WorldSpecLoader|WorldSpecInput|LoadedWorldSpec|WorldSpecLoaderError|unsupported_input|parse_error|schema_validation_error|io_error|Accepted Inputs|Successful Output|Validation Semantics' docs/contracts/worldspec-loader-contract.md
rg -n 'Status: ready for review|Status: `ready for review`|状态：`待评审`|状态：待评审|0\.3\.1-worldspec-loader-contract' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md
rg -n 'concrete demo|character|location|story rule|external validation-world data|private oracle' docs/contracts/worldspec-loader-contract.md docs/iterations/v0.3/0.3.1-worldspec-loader-contract docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
git status --porcelain=v1 -uall | rg -v '^( M docs/iterations/v0\.3/0\.3\.0-v0\.3-planning-and-compatibility-baseline/README\.md| M docs/iterations/v0\.3/README\.md| M docs/iterations/v0\.3/README\.zh\.md| M docs/iterations/v0\.3/v0\.3-plan\.md| M docs/iterations/v0\.3/v0\.3-plan\.zh\.md|\?\? docs/contracts/worldspec-loader-contract\.md|\?\? docs/iterations/v0\.3/0\.3\.1-worldspec-loader-contract/)'
```

The concrete-anchor grep is expected to show only boundary text that forbids
those anchors, not introduced fixture content.

## Acceptance Criteria

- All required docs exist.
- Loader contract headings and required error categories are present.
- Package status is `ready for review` in the package README and milestone
  index.
- Chinese mirrors have equivalent status and scope.
- Scope guard shows no implementation files modified by this package.
- The pre-existing modified `0.3.0` package README is not part of this package
  and remains untouched by the 0.3.1 scope.
- `git diff --check` passes.

## Not Run

Backend, frontend, API, E2E, Agent smoke, and runtime tests are not planned for
this package because it is documentation-only and does not modify runtime,
schema, API, frontend, fixture, migration, or test implementation files.
