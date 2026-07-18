# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `WorldEngine MVP evidence bundle`: a directory of public artifacts exported
  from WorldEngine and client operation logs.
- `operation-log.jsonl`: external client action log that records public client
  operations without private prompts, secrets, raw provider payloads, or hidden
  evaluator data.
- `api-log.jsonl`: request/response summary log for WorldEngine public APIs,
  redacted to public fields.
- `scorecard-input.json`: public normalized input for checker/scorecard
  classification.
- `in-world Agent`: an Agent represented by WorldEngine public runtime state.
- `external validation agent`: Codex/OpenClaw-style actor operating outside
  the world; never an in-world Agent or player.

## Required Artifact Contract

The MVP evidence bundle must include at minimum:

- `manifest.json`: exported WorldEngine `/manifest` response.
- `operation-log.jsonl`: external client public operation log.
- `api-log.jsonl`: public API summary log.
- `session-summary.json`: public session, runtime, snapshot, rule, Agent, memory,
  and inspection refs.
- `agent-evidence.json`: public Agent observe/intent/action-or-wait/rest/memory
  evidence.
- `inspection-evidence.json`: narrative/diagnostic read-only inspection
  evidence.
- `scorecard-input.json`: normalized public evidence for checker/scorecard.
- `redaction-report.json`: public redaction scan result.

Optional artifacts may include screenshots, OpenAPI metadata, or reviewer
notes if they contain public evidence only.

## Allowed Changes

- Add or update package documentation and handoff prompt docs.
- Add public schema/checker support only after this package records
  implementation authorization for that support.
- Add redaction marker lists, artifact field definitions, and status taxonomy.
- Update parent review/route evidence after closeout.

## Forbidden Changes

- No Validation Client implementation in this repository.
- No provider live calls or external validation execution.
- No external validation agent represented as an in-world Agent or player.
- No Validation Client authority over WorldEngine provider calls, generation,
  world mutation, Agent autonomy, or PASS decisions.
- No raw/private evidence, private prompts, secrets, raw provider responses,
  raw thought, private Agent memory, hidden context, or private evaluator data.
- No frontend, autonomous validation, complete MVP closeout, or
  `backend/worldengine/` implementation.

## Required Behavior

- Handoff artifacts must be public-only and redaction-scannable.
- PASS/PARTIAL/BLOCKED/FAIL must be checker/scorecard/review classifications,
  not Validation Client claims by itself.
- Missing provider credentials, missing external client capability, or missing
  checker capability must be classified as BLOCKED/PARTIAL in later validation,
  not papered over here.
- Artifact additions must remain additive to earlier manifest/result concepts.

## Exit Criteria

- Documentation evaluator records no P1/P2 findings.
- Handoff artifact contract and prompt are complete enough for a separate
  Validation Client iteration.
- No provider live-call or external validation execution is claimed.
- Parent route advances to `0.12.5-full-lifecycle-checker-and-autonomous-validation`.
