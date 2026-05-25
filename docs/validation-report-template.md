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

- Status: pass / fail / blocked
- Observed public behavior:
- Redacted evidence summary:
- Compatibility notes:
- Unresolved issues:

## Forbidden Leaked Details Checklist

The report must not include:

- concrete external world name.
- character name.
- location name.
- story rule.
- seed data.
- validation oracle internal implementation.
- UI selector.
- hidden reset API.
- private fixture repository path.
- non-redacted transcript or event payload from the external consumer.

## Scope Review

- Public contract exercised:
- Core repository behavior affected:
- External consumer detail redacted: yes / no
- Follow-up required in WorldEngine core: yes / no

If follow-up is required, describe it as a generic engine capability or
contract gap. Do not describe it as a consumer-specific feature request.
