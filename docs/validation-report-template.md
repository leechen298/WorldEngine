# Validation Report Template

Status: template

Use this template to record redacted validation evidence from an external
fixture or projection consumer. Do not include concrete external-world details
or private validation oracle internals.

## Report Metadata

- Report id:
- Engine commit:
- Public API / CLI version:
- External suite id:
- Redacted target id:
- Capability area:
- Scenario id:
- High-level goal:

## Result

- Status: pass / fail / blocked / skipped / out_of_scope
- Status reason:
- Observed public behavior:
- Redacted evidence summary:
- Compatibility notes:
- Unresolved findings:

## Forbidden Leaked Details Checklist

The report must not include:

- concrete external world name.
- character name.
- location name.
- story rule.
- seed data.
- private transcript.
- validation oracle internal implementation.
- UI selector.
- hidden reset API detail.
- private fixture repository path.
- non-redacted event payload from the external consumer.

## Scope Review

- Public contract exercised:
- Core repository behavior affected:
- External consumer detail redacted: yes / no
- Follow-up required in WorldEngine core: yes / no
- Follow-up summary:

If follow-up is required, describe it as a generic engine capability or
contract gap. Do not describe it as a consumer-specific feature request.

`pass` requires redaction confirmation, public behavior evidence, redacted
evidence summary, and no unresolved P1/P2 finding. `blocked`, `skipped`, and
`out_of_scope` are not pass equivalents and must include a status reason.
