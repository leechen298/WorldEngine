# Test Plan

## Documentation Checks

- Verify required English and Chinese package files exist.
- Verify `evidence-index.md`, `evidence-index.zh.md`,
  `compatibility-audit.md`, and `compatibility-audit.zh.md` exist.
- Verify 0.3.6 is marked `ready for review` in package README, v0.3 milestone
  index, and v0.3 plan.
- Verify required compatibility surface terms appear in the audit docs.
- Verify no implementation paths are modified.
- Verify concrete demo or external validation-world sentinel terms are absent
  from touched docs.

## Commands

```bash
git diff --check
test -f docs/iterations/v0.3/evidence-index.md
test -f docs/iterations/v0.3/evidence-index.zh.md
test -f docs/iterations/v0.3/compatibility-audit.md
test -f docs/iterations/v0.3/compatibility-audit.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.zh.md
rg -n '0\.3\.6-runtime-bridge-evidence-and-compatibility-audit|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
rg -n 'runtime|API|event|archive|params|frontend|schema|fixture|legacy|WorldSpec loader|runtime context bridge|P1|P2|P3|handoff' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/evidence-index.zh.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/compatibility-audit.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
git status --short --branch
```

## Acceptance Criteria

- All documentation checks exit successfully.
- No implementation files are changed.
- The audit docs list explicit assumptions, risks, and P1/P2/P3 findings.
- Runtime, API, event, archive, params, frontend-facing, schema, fixture, and
  legacy surfaces are classified.
- No runtime, build, E2E, UI smoke, Agent smoke, or backend pytest result is
  claimed as passed unless it is cited from prior package review evidence or
  run in this session.

## Not Run

Backend, frontend, API, E2E, Agent smoke, runtime behavior, build, migration,
fixture, and schema tests are not planned for this package because it modifies
documentation only.
