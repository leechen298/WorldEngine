# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `public working memory`: a short-term redaction-safe summary derived from
  public observation/action/rest evidence.
- `public episodic memory`: a redaction-safe summary of public Agent experience
  anchored to event/runtime refs.
- `rest consolidation`: a WorldEngine-owned step that records public rest and
  consolidation evidence without claiming private cognition.
- `memory evidence ref`: a public reference to events, runtime ticks, session
  Agent steps, or consolidation records.

## Allowed Changes

- Add public memory response schemas in `backend/app/schemas/`.
- Extend the in-memory Agent memory store only additively if helper methods are
  needed.
- Add session Agent memory read/consolidation APIs in the existing session
  route boundary.
- Extend the `0.12.1` session Agent rest path to write public memory and
  consolidation evidence.
- Update manifest/public handoff discovery.
- Add focused backend tests.
- Update package and parent review evidence.

## Forbidden Changes

- No raw private memory, raw thought, chain-of-thought, private goals, hidden
  context, secrets, raw prompts, raw provider responses, or provider traces in
  memory records, events, API responses, tests, or review evidence.
- No automatic per-tick personality, skill, relationship, injury, death,
  inventory, or long-term memory mutation.
- No diagnostic conversation insertion into memory.
- No external Validation Client implementation or execution.
- No provider live call.
- No frontend, persistence/migration, checker automation, narrative/diagnostic,
  or complete MVP closeout work.
- No implementation under `backend/worldengine/`.

## Required Behavior

- Session Agent memory read returns public working and episodic summaries.
- A non-rest Agent step may record bounded public working memory.
- A rest Agent step records public rest/consolidation evidence and an episodic
  public summary.
- Memory records include evidence refs to public events/runtime/session Agent
  steps.
- Repeated normal ticks do not automatically mutate personality, skills, or
  long-term memory.
- Private markers in memory-facing requests are rejected or absent from public
  evidence.

## Compatibility Requirements

- Existing memory substrate tests continue to pass.
- Existing session Agent runtime loop tests continue to pass.
- Manifest additions are additive.
- Existing request-driven Agent loop memory context remains compatible.

## Exit Criteria

- Documentation evaluator records no P1/P2 findings.
- `implementation_authorized: yes` is recorded before code changes.
- Focused tests prove memory summary creation, rest consolidation, redaction,
  no per-tick personality/skill mutation, evidence refs, and compatibility.
- Implementation-scope evaluator finds no blocking P1/P2 before closeout.
