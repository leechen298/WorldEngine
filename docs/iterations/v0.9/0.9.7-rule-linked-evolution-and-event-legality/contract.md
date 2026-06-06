# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`WorldEventCandidate`

- Public candidate for rule-linked world evolution.
- Includes candidate id, world id, optional branch id, event type, source,
  proposed tick/time window, public cause refs, public location refs, public
  rule refs, public parameter patches, direction refs, probability evidence,
  causality evidence, and public summary.
- Extra fields are rejected.
- It is not canonical until accepted by legality evaluation.
- It must not include raw prompts, raw provider responses, provider traces,
  hidden context, private Agent memory, private goals, private evaluator data,
  raw thought, chain-of-thought, authorization headers, API keys, secrets, or
  concrete demo-world oracle data.

`WorldEventLegalityResult`

- Public deterministic result for an event candidate.
- Status values:
  - `accepted`
  - `rejected`
  - `blocked`
- Includes a public legality classification, diagnostics, matched rule ids,
  checked constraint ids, referenced parameter ids, timing evidence,
  probability evidence, causality evidence, redaction status, and a state-diff
  summary when accepted.
- Rejected results must not enqueue or append an accepted world-evolution
  event.

`WorldStateDiff`

- Public summary of parameter changes that would result from an accepted
  candidate.
- Includes changed parameter ids, paths, old public values, new public values,
  operation, rule id, constraint ids, and public explanation.
- Diff values must be redacted if any private marker is detected.
- Diff is bounded to public rule/parameter state; it does not mutate Agent
  private state.
- If implementation applies accepted patches, the diff is the required public
  replay artifact proving exactly what public in-memory parameter state
  changed.

`WorldEvolutionEvidence`

- Public evidence artifact attached to an accepted event or returned by an API
  helper.
- Includes rule linkage, state snapshot references, direction refs, legality
  status, diagnostics count, state-diff summary, and redaction status.
- It is checker-readable in shape, but this package does not implement checker
  fixtures or execute checker validation.

`WorldEvolutionSummary`

- Public summary of accepted and rejected event candidates for a world.
- May be implemented as an in-memory helper or route if implementation needs a
  public inspection surface.

## Required Legality Checks

Legality evaluation must deterministically reject or diagnose:

- candidate rule refs that do not resolve to public rule ids.
- parameter patches that target unknown parameter ids.
- patch operations not allowed by the matched rule.
- parameter values outside public constraints.
- candidate timing outside the current bounded runtime tick/time window.
- direct final facts that bypass rule effects.
- direct Agent private-state, goal, inventory, relationship, life/death, or
  private location mutation.
- candidate evidence or refs containing private markers.
- event candidates without public cause, rule, timing, or state evidence.

Legality evaluation may accept a candidate only when:

- at least one public rule is matched.
- every proposed patch targets a public parameter covered by the matched rule.
- every operation is allowed by the matched rule.
- public constraints remain satisfied after the patch.
- timing evidence is compatible with current runtime state.
- causality and probability evidence is present in public form.
- any linked direction guidance remains bounded and does not directly force a
  final fact.

Accepted candidates may apply public parameter patches to the active
in-memory `WorldState` only after legality evaluation accepts them. The
implementation must record an accepted event and public replay/diff evidence
in the same request flow. This package does not authorize durable storage,
persistent rule installation, background evolution, or hidden state mutation.

## Allowed Changes

After documentation review authorization, this package may modify:

- additive schemas in `backend/app/schemas/` for event candidates, legality
  results, state diffs, and evolution evidence.
- narrow deterministic helpers under `backend/app/core/` for legality
  evaluation and public state-diff construction.
- active-backend in-memory public parameter updates for accepted legal
  candidates only, using public rule-linked patches and recorded diff/replay
  evidence.
- `backend/app/api/routes/world.py`, `backend/app/api/routes/runtime.py`, or a
  narrow active-backend route module only for additive public route behavior
  or manifest/OpenAPI exposure if needed.
- event payload construction only to add public legality/evolution evidence to
  accepted events.
- focused backend tests under `backend/app/tests/`.
- package `review.md` and `review.zh.md`.
- v0.9 parent status/review docs only for route/status handoff after review or
  implementation closeout.

## Forbidden Changes

This package must not:

- modify `backend/worldengine/`.
- modify frontend code.
- modify Validation Client or external repositories.
- execute live provider calls or LLM interpretation.
- create generated worlds, generated rules, or generated-result artifacts.
- execute checkers or modify checker fixtures.
- run external validation or autonomous validation.
- implement durable scheduling, background workers, cron, queue services, or
  deployment infrastructure.
- implement Agent continuity, memory consolidation, narrative projection, or
  diagnostic dialogue.
- mutate Agent private memory, goals, personality, skills, relationships,
  inventory, life/death, or private location state.
- add concrete demo-world names, maps, characters, locations, resources, story
  rules, validation oracle data, or application-specific backend behavior.
- store or export API keys, authorization headers, raw prompts, raw provider
  requests, raw provider responses, provider traces, hidden context, private
  Agent memory, raw thought, chain-of-thought, or private evaluator data.
- claim provider live-call PASS, checker PASS, external validation PASS,
  product readiness, or full v0.9 closeout.

## Compatibility Requirements

- Existing event schemas and `/world/events` behavior must remain
  additive-compatible.
- Existing `/world/event-steps`, `/world/snapshots`, and archive behavior must
  remain additive-compatible.
- Existing runtime bounded-run and `/runtime/step` behavior must remain
  compatible.
- Existing `/world/params` and `/world/params/apply` behavior must remain
  compatible.
- Existing generated rule/parameter validation behavior from `0.9.3` must
  remain compatible.
- Existing `/worlds/{world_id}/direction` and
  `/worlds/{world_id}/director-guidance` behavior must remain compatible.
- Existing public handoff manifest behavior must remain compatible.
- New request schemas must reject extra fields and private markers.
- Accepted event evidence must not require checker support to be useful.
- Rejected candidates must not append canonical accepted events or mutate
  public state.
- Accepted candidates must make public state changes reproducible from the
  recorded diff, rule refs, and event evidence.

## North Star Check

This package keeps WorldEngine generic by linking events to public rules and
state instead of inserting arbitrary story outcomes. It strengthens the event
spine needed for later Agent continuity while preserving the boundary that
Agent pseudo-self work belongs to later packages.

## Out-of-Scope Follow-ups

- `0.9.8`: brain-inspired Agent continuity and consolidation evidence.
- `0.9.9`: narrative projection and diagnostic dialogue boundaries.
- `0.9.10`: LLM-backed checker fixtures, schema, and scorecard support.
- `0.9.12`: live or blocked full lifecycle validation execution.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove legal event acceptance, illegal event rejection,
  direction-biased but rule-compliant acceptance, timing/rule/constraint
  diagnostics, redaction, state-diff consistency, extra-field rejection, and
  compatibility with existing direction/runtime/event/rule surfaces.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.
