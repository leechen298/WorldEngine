# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Shape

The handoff is a documentation contract for a future evidence bundle. It does
not add a new API, checker, fixture, or runtime path in this package.

The intended bundle shape is:

```text
evidence-bundle/
  manifest.json
  result.json
  operation-log.jsonl
  provider-live-summary.json
  world-creation-summary.json
  world-rule-summary.json
  rule-parameter-summary.json
  event-legality-summary.json
  agent-autonomy-summary.json
  diff-replay-summary.json
  world-lifecycle-summary.json
  narrative-projection-summary.json
  diagnostic-conversation-summary.json
  redaction-scan.json
  scorecard-summary.json
  second-agent-review.md
  screenshots/
  transcript.md
```

Only scenario-required artifacts need to exist. The manifest must say whether
each artifact is required, displayable, exportable, and checker-consumable.

## Artifact Producer Roles

- `worldengine`: produces canonical public evidence summaries.
- `validation_client`: displays or bundles public artifacts without changing
  evaluator meaning.
- `worldengine_checker`: validates result status from structured artifacts.
- `second_agent_review`: records read-only review findings when required.

## Manifest Validation Rules

A future compatibility probe should check:

1. manifest exists and is valid JSON.
2. `client_role` is `display_export_only`.
3. `provider_owner` is `worldengine`.
4. `evaluator_role` is not a client-owned evaluator.
5. all artifact paths are relative and stay inside the bundle.
6. required artifact names match the 0.9.10 checker contract.
7. every displayable/exportable artifact has a clean redaction status.
8. unsupported items are explicit and never converted to PASS.

## Display Guidance

The client may display:

- scenario and status.
- provider class/model label and redacted call status.
- world creation summary and public model metadata.
- rule and event legality summaries.
- public Agent autonomy and continuity summaries.
- narrative projection and diagnostic conversation summaries as external
  inspection surfaces.
- scorecard status and second-Agent review summary.

The client must not display raw prompts, raw provider payloads, private memory,
hidden context, private evaluator data, seed/oracle data, or provider secrets.

## Export Guidance

The client may export the bundle as relative files compatible with the
autonomous saved-result checker. It must preserve artifact names and status
values. If an artifact is missing, malformed, blocked, or not run, the export
must preserve that fact.

## Risk Controls

- Avoid client-side evaluator drift by forbidding client-owned PASS decisions.
- Avoid redaction drift by requiring the bundle redaction status and preserving
  `redaction-scan.json`.
- Avoid path leakage by requiring bundle-relative paths.
- Avoid application-specific narrowing by keeping the contract generic and
  artifact-based.
