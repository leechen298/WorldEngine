# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Artifact Directory Shape

Future Validation Client exports should write a single result directory:

```text
worldengine-mvp-result/
  manifest.json
  operation-log.jsonl
  api-log.jsonl
  session-summary.json
  agent-evidence.json
  inspection-evidence.json
  scorecard-input.json
  redaction-report.json
  reviewer-notes.md
```

`reviewer-notes.md` is optional. If present, it must contain public review
notes only.

## Status Taxonomy

- `PASS`: all required public evidence is present and checker/scorecard/review
  agree no blocking P1/P2 remains.
- `PARTIAL`: WorldEngine produced some MVP evidence, but a required capability
  or artifact is incomplete.
- `BLOCKED`: provider credentials, external client capability, checker assets,
  permissions, or environment prevent required validation.
- `FAIL`: evidence exists and checker/scorecard/review find a blocking product
  or contract failure.

## Operation Log Rows

Each `operation-log.jsonl` row must include:

- `operation_id`
- `timestamp`
- `actor_class: "external_validation_agent"`
- `worldengine_surface`
- `public_action_summary`
- `result_status`
- `public_artifact_refs`
- `redaction_status`

Rows must not include raw prompts, hidden reasoning, secrets, raw provider
payloads, or private evaluator notes.

## API Log Rows

Each `api-log.jsonl` row must include:

- `request_id`
- `timestamp`
- `method`
- `path`
- `status_code`
- `operation_id`
- `public_request_summary`
- `public_response_summary`
- `artifact_refs`
- `redaction_status`

Raw request/response bodies are forbidden unless they are already public and
redaction-scanned.

## Scorecard Input

`scorecard-input.json` must normalize:

- manifest readiness.
- session creation and bounded runtime.
- rule-linked event/diff evidence.
- Agent observe/intent/action-or-wait/rest evidence.
- Agent memory/consolidation evidence.
- narrative/diagnostic read-only inspection evidence.
- redaction report status.
- terminology checks for in-world Agent versus external validation agent.

## Redaction Scan

The redaction report must scan all public artifacts for:

```text
api_key
authorization
bearer
chain-of-thought
hidden context
private memory
private prompt
provider trace
raw prompt
raw provider response
raw response
raw thought
secret
sk-live-
token
```

The scan may include more markers, but it must include these.

## Integration Boundary

WorldEngine defines these artifact semantics and public API expectations.
WorldEngine-Validation-Client implements export and client automation in its
own repository. The client can report evidence completeness, but PASS remains a
checker/scorecard/review classification.
