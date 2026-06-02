# Full Autonomous Scenario: agent-loop-api

Status: contract-only / checker-extension-required
Scenario ID: AUTO-FULL-V07-003

## User Goal

As a public API user, verify that `POST /world/agent/loop/step` handles noop,
accepted patch, multi-patch/remove, rejected actions, and schema errors with
correct mutation and event evidence.

## Autonomous Operation Boundary

Allowed operations:

- Public API calls to `/world/agent/loop/step`, `/world/params`,
  `/world/events`, and `/runtime/state`.
- CLI operations to start services and run documented checker commands.
- Artifact creation for request/response logs and scorecard output.

Forbidden operations:

- private reset, private fixture hooks, database state, or hidden test oracles.
- external validation world internals.
- code, test, checker, scenario, or fixture edits during the run.
- converting a 200 rejected result into PASS without no-mutation evidence.

## Preconditions

- API server is reachable.
- The agent can record params and `params.applied` event ids before each
  negative case.
- The result schema/checker accepts public API operations in `api-log.jsonl` or
  an equivalent API evidence artifact.

## Steps The Agent May Choose

1. Record current params and recent `params.applied` event ids.
2. POST `/world/agent/loop/step` with default/noop intent and bounded
   `event_limit`.
3. POST a valid `params.patch` that changes `counter.increment`.
4. POST a multi-patch sequence that sets `counter.increment`, sets
   `scene.weather`, then removes `scene.weather`.
5. POST a reserved-path patch.
6. POST a `noop` intent with unexpected patches.
7. POST an empty `params.patch`.
8. POST a duplicate-path dry-run rejection case.
9. POST an unsupported action such as `world.spawn`.
10. POST schema-invalid requests such as invalid `event_limit`.
11. After each case, read params and events and record whether mutation and
    event evidence match the expected classification.

## Expected Assertions

- Noop returns bounded perception and no params mutation.
- Accepted single patch mutates params and emits `params.applied` with
  `source=agent.loop`.
- Multi-patch/remove mutates `counter.increment`, removes `scene.weather`, and
  emits one event whose payload contains the full patch sequence.
- Reserved path, noop-with-patch, empty patch, dry-run duplicate, and
  unsupported action return rejected results without mutation or new applied
  event.
- Schema-invalid requests return HTTP 422 with API envelope `code=30` and no
  mutation.

## Failure Or Blocked Conditions

- Rejected action mutates state.
- Accepted patch lacks event evidence.
- Multi-patch/remove event payload omits or misorders the patch sequence.
- Schema error is silently accepted.
- The agent relies on non-public state.

## Required Artifacts

- `result.json`
- `operation-log.jsonl` recording the autonomous agent's public API/CLI choices
- `api-log.jsonl` with request and response summaries
- `api-summary.json` with before/after params and event ids
- `transcript.md`
- `console.log` or explicit empty-console note
- `scorecard-summary.json`

Screenshots are optional for this API-only scenario unless the future runner
also opens dashboard evidence.
`operation-log.jsonl` records the agent's chosen steps; `api-log.jsonl` records
request/response summaries. A future checker must accept this public API
evidence shape before the scenario can be reported as PASS.

## PASS Source

Future full-autonomous scorecard/checker over the saved result directory.
Current v0.7 may document this scenario but must not report it as PASS until
the protocol and checker support public API operations and the result has been
validated.
