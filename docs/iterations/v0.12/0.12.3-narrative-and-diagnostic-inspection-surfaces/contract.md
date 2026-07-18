# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `inspection surface`: a read-only API/artifact that summarizes public
  evidence without mutating canonical state.
- `session narrative projection`: a readable public summary for a session,
  tick range, optional branch, and optional Agent focus.
- `diagnostic inspection summary`: an out-of-world Q&A-style public summary
  derived from public evidence.
- `inspection provenance`: public refs and filters that identify the events,
  snapshots, Agent state, memory summaries, tick range, branch, or session used
  by a projection.

## Allowed Changes

- Add public inspection request/response schemas in `backend/app/schemas/`.
- Extend existing external projection boundary helpers additively.
- Add read-only session inspection endpoints under existing session or world
  route boundaries.
- Add manifest/public-surface discovery for new endpoints.
- Add focused backend tests.
- Update package and parent review evidence.

## Forbidden Changes

- No canonical state mutation, event append, direction queue write, Agent
  memory write, or in-world dialogue record from narrative/diagnostic
  inspection.
- No raw thought, chain-of-thought, private memory, private goals, hidden
  context, provider traces, raw prompts, raw provider responses, secrets,
  tokens, or private evaluator data in public inspection artifacts.
- No client-owned Agent autonomy or external validation agent represented as
  an in-world Agent.
- No gameplay dialogue, concrete demo content, frontend, persistence/migration,
  provider live calls, external Validation Client implementation, checker
  automation, or full MVP closeout.
- No implementation under `backend/worldengine/`.

## Required Behavior

- Narrative inspection can be scoped by session ID, tick range, branch ID, and
  Agent ID where data exists.
- Diagnostic inspection can answer from public evidence summaries only and
  records that it is out-of-world.
- Accepted inspection artifacts include provenance/filter fields and redaction
  status.
- Rejected inspection requests report public diagnostic codes without echoing
  private payloads.
- Inspection calls do not change event count, canonical state, direction
  queue, or Agent memory.
- Manifest additions are additive and identify the endpoints as read-only
  inspection surfaces.

## Compatibility Requirements

- Existing world-level projection and diagnostic endpoints continue to pass.
- Existing session Agent runtime and memory tests continue to pass.
- Existing public handoff manifest tests continue to pass.
- Schema additions are additive.

## Exit Criteria

- Documentation evaluator records no P1/P2 findings.
- `implementation_authorized: yes` is recorded before code changes.
- Focused tests prove session/tick-range/branch/Agent-focused projection,
  diagnostic public-evidence behavior, read-only behavior, redaction,
  provenance, mutation rejection, and compatibility.
- Implementation-scope evaluator finds no blocking P1/P2 before closeout.
