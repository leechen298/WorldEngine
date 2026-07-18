# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `session Agent`: an in-world Agent represented inside a WorldEngine session.
- `public Agent state`: redaction-safe Agent fields such as status, last
  observation summary, public intent label, visible action, runtime refs, and
  evidence refs.
- `Agent step`: a WorldEngine-owned transition that observes public state,
  chooses a public intent/action-or-wait/rest outcome, records events, and
  updates public Agent state.
- `client-scripted action`: a client-provided concrete action or patch that
  bypasses WorldEngine intent selection. It must not be reported as Agent
  autonomy.

## Allowed Changes

- Add public session Agent schemas in `backend/app/schemas/`.
- Add session Agent state storage in `backend/app/core/world_session.py` or a
  small adjacent core module.
- Add session Agent APIs in `backend/app/api/routes/session.py` under the
  existing session route boundary.
- Update manifest/public handoff discovery in `backend/app/api/routes/world.py`.
- Add focused backend tests under `backend/app/tests/`.
- Update package and parent review evidence.

## Forbidden Changes

- No raw thought, raw chain-of-thought, private memory, private goals, hidden
  context, raw prompts, raw provider responses, provider traces, or secrets in
  schemas, events, API responses, tests, or review evidence.
- No accepting client-provided action patches/intents on the session Agent
  step endpoint.
- No direct mutation of Agent private state, long-term memory, personality,
  skills, injury, death, or inventory.
- No rule/event legality bypass for public world mutations.
- No frontend, persistence/migration, provider live, external Validation
  Client, checker automation, narrative/diagnostic, or complete MVP closeout
  work.
- No new runtime feature under `backend/worldengine/`.

## Required Behavior

- A new or existing session can expose at least one public Agent record.
- Reading/listing public Agent state is redaction-safe.
- Running a session Agent step without client action intent produces public
  observe/intent/action-or-wait/rest evidence.
- Runtime refs in Agent evidence match the current runtime tick/time.
- Agent step evidence is appended to the event log and referenced by the
  response.
- If a client tries to submit a scripted action intent, the API rejects it or
  ignores it with explicit public diagnostic evidence.
- Existing request-driven `/world/agent/loop/step` remains compatible but is
  not used as proof of session Agent autonomy.

## Compatibility Requirements

- Existing session create/list/read/status/run/snapshot/rules/directions/
  evolution APIs remain additive-compatible.
- Existing agent loop service tests continue to pass.
- Manifest additions are additive.
- Event payloads remain public and redaction-safe.

## Exit Criteria

- Documentation evaluator records no P1/P2 findings.
- `implementation_authorized: yes` is recorded before code changes.
- Focused tests prove public Agent state, WorldEngine-owned step selection,
  event evidence, client-scripted-action rejection, redaction boundary, and
  compatibility.
- Implementation-scope evaluator finds no blocking P1/P2 before closeout.
