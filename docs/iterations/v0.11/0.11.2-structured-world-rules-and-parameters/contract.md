# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `session_rule_parameter_set`: structured public rule/parameter evidence
  attached to a session.
- `rule_parameter_validation`: public accepted/rejected result from existing
  validators.
- `public_rule_summary`: redaction-safe summary with parameter paths, rule
  ids, boundary ids, diagnostics count, and redaction status.

## Allowed Changes

- Add session storage fields for rule parameter validation and summary.
- Add `POST /sessions/{session_id}/rules` and `GET /sessions/{session_id}/rules`
  or equivalent additive endpoints.
- Reuse existing rule-parameter schemas/validators.
- Add manifest discovery entries and focused backend tests.
- Update docs and route status.

## Forbidden Changes

- No runtime event generation.
- No direction queue or user guidance interpretation.
- No direct mutation of Agent private memory, goals, injury, death, inventory,
  or hidden state.
- No live provider calls.
- No Validation Client implementation.
- No durable persistence/migrations.
- No concrete demo-world fixtures or `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/world/params` behavior remains unchanged.
- Existing session create/run/snapshot behavior remains unchanged except for
  additive rule summary fields/endpoints.
- Rejected/private marker rule sets must not echo private values in public
  diagnostics or summaries.
- Accepted rule sets must reference only public structured parameter/rule ids.

## Out-of-Scope Follow-Ups

- Natural-language direction queue belongs to `0.11.3`.
- Rule-compliant event generation/diffs belong to `0.11.4`.
- Fidelity validation belongs to `0.11.5`.
