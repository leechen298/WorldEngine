# Test Plan

## Documentation Checks

Run:

```bash
git diff --check
```

Verify required files exist:

```bash
test -f docs/contracts/external-fixture-runner-contract.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.zh.md
```

Verify contract headings and required terms:

```bash
rg -n 'ExternalFixtureRunner|ExternalSuiteId|RedactedTargetId|PublicContractSurface|RedactedValidationReport|Allowed Consumption Surfaces|Redacted Validation Report Shape|Required Redaction Rules|Forbidden Inferences|Acceptance Requirements' docs/contracts/external-fixture-runner-contract.md
```

Verify redaction and report fields:

```bash
rg -ni 'report id|engine commit|public API / CLI version|external suite id|redacted target id|capability area|scenario id|status: `pass`, `fail`, or `blocked`|observed public behavior|redacted evidence summary|compatibility notes|unresolved issues' docs/contracts/external-fixture-runner-contract.md docs/validation-report-template.md
```

Verify status synchronization:

```bash
rg -n '0\.3\.5-external-fixture-contract-readiness|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness
```

Verify no concrete fixture sentinel anchors were added:

```bash
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/contracts/external-fixture-runner-contract.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
```

Verify no implementation files are modified:

```bash
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
```

## Tests Not Planned

Backend, frontend, API, E2E, Agent smoke, runtime, build, migration, fixture,
and schema tests are not planned because this package modifies documentation
only.
