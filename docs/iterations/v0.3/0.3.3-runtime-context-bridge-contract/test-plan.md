# Test Plan

## Documentation Checks

- Verify required package files and Chinese mirrors exist.
- Verify `docs/contracts/runtime-context-bridge-contract.md` contains required
  bridge concepts, accepted input, context fields, error categories,
  compatibility surfaces, and forbidden inferences.
- Verify English and Chinese milestone indexes mark 0.3.3 as `ready for
  review` / `待评审`.
- Verify touched documentation does not introduce concrete demo-world anchors.
- Verify changed files stay inside allowed documentation paths.

## Future Implementation Tests

`0.3.4-runtime-context-bridge-implementation` should add focused tests for:

- deriving context from a successful loaded `WorldSpec`.
- rejecting unsupported bridge input with `unsupported_input`.
- rejecting incomplete loader output with `invalid_loaded_worldspec`.
- returning `context_derivation_error` for derivation failures not covered by
  schema validation.
- default `RuntimeEngine` construction and `step()` behavior when no context is
  supplied.
- optional context storage without changing `RuntimeEngine.step()` output.
- no raw `WorldSpec` event payloads.
- unchanged `/runtime/state`, `/runtime/step`, `/world/events`, and
  `/world/event-steps` response shapes if implementation touches those
  surfaces.
- unchanged params and archive behavior if implementation touches runtime
  construction.
- no frontend, fixture, migration, persistence, or legacy path changes unless
  a reviewed package explicitly allows them.

These tests are not implemented or run in this documentation-only package.

## Commands

```bash
git status --short --branch
git diff --check
test -f docs/contracts/runtime-context-bridge-contract.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.zh.md
rg -n 'RuntimeContextBridge|RuntimeContextInput|RuntimeContext|RuntimeContextSummary|RuntimeContextBridgeError|unsupported_input|invalid_loaded_worldspec|context_derivation_error|Accepted Input|Runtime Context Shape|Compatibility Evidence Required Before Implementation' docs/contracts/runtime-context-bridge-contract.md
rg -n 'tick|world_time_seconds|/runtime/state|/runtime/step|/world/events|/world/event-steps|params|archive|frontend|backend/worldengine|raw `WorldSpec`|WorldCell.*runtime module' docs/contracts/runtime-context-bridge-contract.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.3-runtime-context-bridge-contract' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/contracts/runtime-context-bridge-contract.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

The concrete-anchor grep is a no-match check. If a future documentation review
requires one of those words only in a forbidden-change sentence, record the
match and rationale in `review.md`.

## Acceptance Criteria

- Required docs and Chinese mirrors exist.
- Bridge contract headings and required terms are present.
- Package status is `ready for review` in the package README and milestone
  index.
- Chinese mirrors have equivalent status and scope.
- Scope guard shows no implementation files modified by this package.
- `git diff --check` passes.
- Documentation records assumptions, open risks, compatibility evidence
  requirements, and docs-only no-test rationale.

## Not Run

Backend, frontend, API, E2E, Agent smoke, and runtime tests are not planned for
this package because it is documentation-only and does not modify runtime,
schema, API, frontend, fixture, migration, or test implementation files.
