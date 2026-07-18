# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `v0.10 handoff`: the reviewed runnable-session MVP slice closed as PASS.
- `v0.11 input`: public evidence from manifest, session, runtime, snapshot, and
  dashboard flows that v0.11 may build on after child authorization.
- `handoff caveat`: a known unsupported or unproven area that must stay
  visible and must not be converted into a PASS claim.

## Allowed Changes

- Create and review this package document set.
- Update v0.11 parent docs after review to select `0.11.1` as the next route.
- Record current-session documentation checks and no-code-test rationale.

## Forbidden Changes

- No runtime, API, schema, frontend, checker, fixture, provider, generated
  result, Validation Client, migration, persistence, or `backend/worldengine/`
  implementation changes.
- No live provider execution.
- No external Validation Client execution.
- No claim that v0.10 proved Agent autonomy, durable persistence, or product
  readiness.
- No v0.11 implementation before the relevant child package review records
  authorization.

## Compatibility Requirements

- Preserve v0.10 closeout as PASS only for the reviewed runnable-session MVP
  slice.
- Preserve `manifest_status blocked` as a provider-readiness caveat when
  provider credentials are not configured.
- Keep Validation Client external and evidence-consuming only.
- Keep user/player outside the world.

## Out-of-Scope Follow-Ups

- Provider/worldview preflight implementation belongs to `0.11.1`.
- Structured rules and parameters belong to `0.11.2`.
- Direction queue/boundary belongs to `0.11.3`.
- Rule-compliant events/diffs belong to `0.11.4`.
- Fidelity validation belongs to `0.11.5`.
- Agent continuity and external automation belong to v0.12.
