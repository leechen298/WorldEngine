# 0.8.1 Minimum Working State Contract

Status: review complete
Type: documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## Goal

Define what v0.8 may call a minimum normally working WorldEngine state,
including required core slices, claim taxonomy, evidence classes, and excluded
product or external validation claims.

This package is contract-only. It does not implement schemas, checkers, APIs,
frontend behavior, runtime behavior, tests, external validators, or external
applications.

## Minimum Working-State Contract

A v0.8 minimum working-state claim may be made only when later reviewed
packages provide current-session evidence for all required in-scope slices:

- generation readiness: generated or imported generic world material is
  structured, validated, inspectable, and explicitly marked runtime-ready or
  blocked.
- runtime readiness: a loaded generic world can expose state, advance through
  approved runtime steps, and record events without hidden side effects.
- event evidence: state changes and Agent actions are observable through
  public, redacted event or evidence surfaces.
- Agent loop readiness: an Agent can perceive bounded world context, produce a
  validated intent, and receive a reviewable action result within approved
  runtime boundaries.
- memory-context readiness: bounded read-only memory context can be included
  where already authorized, without exposing raw memory, private transcripts,
  provider traces, or pseudo-self internals beyond current contracts.
- projection/read-model observability: public read-only surfaces can summarize
  current working-state evidence without product-specific behavior.
- evidence and blocker classification: pass, blocked, skipped, and out of
  scope states are distinct and reviewable.

## Claim Taxonomy

- `core contract ready`: documentation contracts are reviewed; no runtime pass
  is implied.
- `core observable surface ready`: public observable surfaces are defined or
  implemented by a reviewed package; no external validation PASS is implied.
- `minimum working-state evidence ready`: current-session core evidence proves
  the required in-scope slices; no product or external-suite PASS is implied.
- `external validation handoff ready`: public redacted handoff evidence exists
  for an external validator to consume; no external validation PASS is implied.
- `external validation pass`: out of scope for current v0.8 core packages
  unless a later reviewed external workflow supplies redacted public evidence.
- `blocked`: required evidence or contract conditions are not satisfied.
- `skipped`: intentionally not run with rationale.
- `out of scope`: excluded by the active package contract.

## Scope

Allowed scope:

- Create this package document set and Chinese mirrors.
- Define minimum working-state concepts, claim taxonomy, evidence classes,
  exclusions, and authorization criteria for later packages.
- Synchronize parent v0.8 route/status surfaces after review.
- Record documentation checks and evaluator findings.

Forbidden scope:

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  or `backend/worldengine/` implementation files.
- Do not implement minimum working-state schemas, observable surfaces,
  services, APIs, UI, persistence, checkers, tests, or evidence artifacts.
- Do not define external validator connection details, private scenarios,
  oracle logic, product app UI, application state, private repository paths,
  concrete world content, UI selectors, hidden reset APIs, provider traces, or
  secrets.
- Do not claim minimum working-state PASS, runtime/API/frontend/E2E PASS,
  Agent smoke PASS, autonomous PASS, external validation PASS, projection
  readiness PASS, product readiness PASS, or release readiness.

## Final Assessment State

Current value: `review complete`.

This package defines the minimum working-state contract and hands off
authorization criteria to `0.8.2-core-observable-surface-boundary`.
