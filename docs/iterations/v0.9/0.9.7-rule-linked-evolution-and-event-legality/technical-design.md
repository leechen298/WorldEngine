# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Active Backend Placement

Implementation must stay in `backend/app/`. The preferred shape is:

```text
backend/app/schemas/world_evolution.py
backend/app/core/rule_linked_evolution.py
backend/app/api/routes/world.py
backend/app/tests/test_rule_linked_evolution_legality.py
```

The implementation may choose a narrow adjacent module name if local patterns
make that clearer. It must not add runtime features under `backend/worldengine/`.

## Data Flow

1. Caller submits or constructs a `WorldEventCandidate`.
2. Deterministic legality helper receives:
   - candidate.
   - `GeneratedRuleParameterSet` or an accepted rule/parameter set summary.
   - current public parameter values.
   - current runtime tick and world time.
   - optional accepted direction queue refs from `0.9.6`.
3. Helper validates rule refs, parameter refs, allowed operations, constraints,
   timing, causality evidence, probability evidence, and redaction.
4. If accepted, helper returns `WorldEventLegalityResult(status="accepted")`
   with `WorldStateDiff` and `WorldEvolutionEvidence`.
5. If accepted through an apply-capable route, public parameter patches are
   applied to active in-memory `WorldState`, and an accepted event records the
   diff/replay evidence.
6. If rejected, helper returns public diagnostics and no accepted event append
   or state mutation.

## Schema Notes

`WorldEventCandidate`

- `candidate_id`: stable public id.
- `world_id`: public world id.
- `event_type`: public event type.
- `source`: public source label, defaulting to `world_rule`.
- `proposed_tick`: optional current-or-future tick.
- `proposed_world_time_seconds`: optional world time.
- `rule_refs`: non-empty public rule ids.
- `parameter_patches`: non-empty public parameter patch requests.
- `direction_refs`: optional public direction ids.
- `cause_refs`: non-empty public event or state refs.
- `location_refs`: optional public refs.
- `probability_evidence`: structured public probability or weight evidence.
- `causality_evidence`: structured public cause/effect evidence.
- `public_summary`: redacted public summary.

`WorldParameterPatch`

- `parameter_ref`
- `op`
- `value`
- `rule_ref`
- `public_explanation`

The operation vocabulary must stay compatible with the `0.9.3` allowed ops:
`add`, `set`, and `remove`.

`WorldEventLegalityDiagnostic`

- `code`
- `message`
- `path`
- `severity`

Diagnostics must not echo unsafe user or provider values.

## Legality Algorithm

The deterministic helper should:

1. Redaction-scan candidate ids, refs, summaries, evidence objects, patches,
   and values.
2. Validate the rule set using existing `0.9.3` validation helpers if the full
   rule set is supplied.
3. Build public lookup maps for rules, parameters, constraints, and current
   values.
4. Require at least one candidate rule ref and one public cause ref.
5. For each patch:
   - require parameter ref resolution.
   - require rule ref resolution.
   - require the parameter to be targeted by the matched rule.
   - require the operation to be in the matched rule's `allowed_ops`.
   - compute the post-patch public value.
   - validate public constraints and value type.
6. Validate candidate timing against current runtime state and bounded
   requested window.
7. Require public causality and probability evidence.
8. Reject direct final fact or Agent private-state categories.
9. Return accepted evidence only when every diagnostic is non-blocking.

## Event Integration

If the implementation exposes an API route, accepted results may append an
event with a generic type such as `world.evolution.accepted` and a public
payload containing:

```text
world_id
candidate_id
legality_status
matched_rule_ids
changed_parameter_ids
state_diff
evidence
redaction_status
direct_state_mutation_applied: false
```

Accepted apply behavior must update only public in-memory world parameters
covered by the accepted diff. It must not install durable rules, mutate hidden
state, or bypass the public diff/evidence record. Evaluate-only helper behavior
may exist for tests or internal callers, but any canonical application must be
paired with an accepted event and replayable state diff.

Rejected candidates may append `world.evolution.rejected` only if the payload
contains no unsafe raw candidate values and does not imply accepted canonical
state.

## API Surface

An implementation may add an additive public endpoint such as:

```text
POST /worlds/{world_id}/evolution/evaluate-event
```

If no route is necessary, the helper and tests are enough for this package.
If a route is added, it must be listed in the public handoff manifest and
covered by focused API tests.

## Compatibility

- Do not change `Event` required fields.
- Do not change existing `/world/events`, `/runtime/step`, `/runtime/run`,
  `/worlds/{world_id}/direction`, or `/world/generation/worldview` response
  shapes except additive manifest exposure if needed.
- Do not install rule sets into durable runtime state.
- Do not convert natural-language direction into direct event outcomes.
- Preserve `/world/params`, `/world/event-steps`, and `/world/snapshots`
  compatibility while adding rule-linked evidence.

## Redaction

The redaction marker vocabulary must include at least:

```text
api_key
authorization
credential
hidden context
private evaluator data
private goal
private memory
private prompt
provider trace
provider_trace
provider_secret
raw prompt
raw provider request
raw provider response
raw request
raw response
self_state
sk-live-
sk-test-
```

When any marker is detected, public ids/lists/summaries derived from the
unsafe candidate must be blanked or replaced with generic diagnostics.

## Stop Conditions

Stop implementation and return to documentation review if:

- legality requires provider-backed interpretation.
- checker support or fixture changes become necessary.
- Agent continuity, memory, relationship, inventory, or life/death semantics
  are required.
- implementation needs durable scheduling, background execution, or persistent
  rule installation.
- event legality cannot be explained through public rule/state evidence.
