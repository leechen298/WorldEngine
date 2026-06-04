# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

This package defines planning concepts only:

- `provider_class`: public category such as `kimi_code_subscription`,
  `kimi_platform_api`, `moonshot_api`, `deepseek_api`, `mock`, or
  `unconfigured`.
- `provider_readiness`: public status such as `ready`, `degraded`,
  `unavailable`, `blocked`, or `not_configured`.
- `credential_source_class`: redacted label such as `environment`,
  `secret_manager`, `developer_local`, or `none`.
- `handoff_manifest`: public object that lists core-side validation surfaces,
  evidence references, provider readiness summary, redaction confirmation, and
  blocker classification.
- `external_validation_consumer`: external client or Agent system that consumes
  WorldEngine public contracts.

## Allowed Changes

This documentation package may:

- define provider boundary semantics.
- define handoff manifest field expectations.
- define stop rules and evidence classification.
- reference public provider documentation as planning inputs.
- prepare future package scope for schemas, checkers, or public endpoint docs.

## Forbidden Changes

This package must not:

- modify runtime, schema, API, frontend, tests, fixtures, migrations, or
  generated evidence.
- implement provider calls.
- store provider keys or account details.
- expose provider traces, raw prompts, raw responses, private evaluator oracle
  data, private validation scenarios, external repo paths, product UI
  selectors, concrete world content, or hidden reset APIs.
- claim external validation PASS, product readiness, live provider PASS, Agent
  autonomous PASS, E2E PASS, or human validation PASS.

## Compatibility Constraints

- WorldEngine remains the provider owner.
- External validation clients consume public summaries only.
- Schema/API changes remain future work and require a reviewed implementation
  package.
- Existing v0.7 and v0.8 closeout evidence remains historical and bounded.

## Stop Rules

- Stop if a proposed field requires exposing a secret, private prompt, provider
  raw trace, or private validator detail.
- Stop if the validation client would need to define WorldEngine core
  readiness taxonomy itself.
- Stop if provider integration cannot be described without deciding runtime
  behavior that belongs to a later code package.
