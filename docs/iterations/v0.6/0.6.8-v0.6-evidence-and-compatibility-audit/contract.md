# Contract

Status: review complete

implementation_authorized: no

## Audit Contract

This package must audit, not implement. It may update v0.6 documentation and
parent status surfaces only.

The audit must distinguish:

- current-session command evidence from historical handoff evidence.
- implementation checks from documentation checks.
- dashboard E2E smoke from product readiness.
- loader/runtime-context readiness from full runtime migration.
- generated `WorldSpec` validity from generation quality.
- v0.6 generation readiness from v0.7 external validation and v0.8 projection
  readiness.

## Required Evidence Index

The audit must include evidence from:

- `0.6.0` and `0.6.1` documentation gates.
- `0.6.2` deterministic generator core.
- `0.6.3` structured generation plan compiler.
- `0.6.4` AI-assisted boundary and plan import.
- `0.6.5` preview API and generation metadata.
- `0.6.6` regeneration and runtime-readiness integration.
- `0.6.7` dashboard preview and E2E smoke.

## Compatibility Requirements

- Schema/API extensions remain additive inside the reviewed generation surface.
- Existing API response envelopes and validation error behavior remain
  compatible.
- Existing runtime tick/event behavior remains unchanged by generation
  readiness checks.
- Existing dashboard runtime, world, timeline, memory, and agent panels remain
  compatible.
- `backend/worldengine/` remains untouched.

## Exit Criteria

The package may be marked review complete only if:

- documentation checks pass.
- the changed-file scope guard confirms documentation-only work for this
  package.
- a documentation/evidence evaluator reports no P1/P2 findings.
- unresolved findings are classified.
- the release-candidate handoff recommendation is explicit.
