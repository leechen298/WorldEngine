# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `v0.11 handoff`: the reviewed rule-bound world evolution slice closed as
  scoped `PASS`.
- `v0.12 input`: public evidence from session, rule, direction, event, diff,
  snapshot, and fidelity surfaces that Agent continuity may build on after
  child authorization.
- `Agent continuity`: future v0.12 behavior where an in-world Agent visibly
  observes, chooses action or no-action, reacts, remembers through public
  summaries, and rests or sleeps across ticks.
- `handoff caveat`: an unproven area that must remain explicit and must not be
  converted into an MVP PASS claim.

## Allowed Changes

- Create and review this package document set.
- Update v0.12 parent docs after review to select `0.12.1` as the next route.
- Record current-session documentation checks and no-code-test rationale.

## Forbidden Changes

- No runtime, API, schema, frontend, checker, fixture, provider, generated
  result, Validation Client, migration, persistence, or `backend/worldengine/`
  implementation changes.
- No live provider execution.
- No external Validation Client execution.
- No Agent runtime loop, memory, rest/sleep, narrative, diagnostic, checker, or
  MVP closeout implementation.
- No claim that v0.11 proved Agent autonomy, external automation, frontend
  E2E, durable persistence, product readiness, or complete MVP PASS.

## Compatibility Requirements

- Preserve v0.11 closeout as PASS only for the reviewed rule-bound world
  evolution scope.
- Preserve provider live-call and external Validation Client automation as
  unproven until a later package has evidence.
- Keep in-world Agents separate from external validation agents.
- Keep narrative and diagnostic inspection read-only until a reviewed package
  authorizes implementation.

## Out-of-Scope Follow-Ups

- Agent public state and runtime loop belongs to `0.12.1`.
- Agent memory and rest consolidation belongs to `0.12.2`.
- Narrative and diagnostic inspection belongs to `0.12.3`.
- Validation Client evidence handoff belongs to `0.12.4`.
- Full lifecycle checker/autonomous validation belongs to `0.12.5`.
- MVP release candidate closeout belongs to `0.12.6`.
