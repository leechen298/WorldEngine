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

Machine field mapping:

| Template field | JSON field |
| --- | --- |
| Report id | `report_id` |
| Engine commit | `engine_reference` |
| Public API / CLI version | `public_contract_surface` |
| External suite id | `external_suite_id` |
| Redacted target id | `redacted_target_id` |
| Capability area | `capability_area` |
| Scenario id | `scenario_id` |
| High-level goal | `high_level_goal` |

## Result

- Status: pass / fail / blocked / skipped / out_of_scope
- Status reason:
- Observed public behavior:
- Redacted evidence summary:
- Compatibility notes:
- Unresolved findings:

Machine field mapping:

| Template field | JSON field |
| --- | --- |
| Status | `status` |
| Status reason | `status_reason` |
| Observed public behavior | `observed_public_behavior` |
| Redacted evidence summary | `redacted_evidence_summary` |
| Compatibility notes | `compatibility_notes` |
| Unresolved findings | `unresolved_findings` |

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

Machine field mapping: each checklist item maps to the same snake_case key in
`forbidden_detail_review`, with `false` required for a redacted report.

## Scope Review

- Public contract exercised:
- Core repository behavior affected:
- External consumer detail redacted: yes / no
- Follow-up required in WorldEngine core: yes / no
- Follow-up summary:

Machine field mapping:

| Template field | JSON field |
| --- | --- |
| Public contract exercised | `scope_review.public_contract_exercised` |
| Core repository behavior affected | `scope_review.core_repository_behavior_affected` |
| External consumer detail redacted | `scope_review.external_consumer_detail_redacted` |
| Follow-up required in WorldEngine core | `scope_review.follow_up_required_in_worldengine_core` |
| Follow-up summary | `scope_review.follow_up_summary` |

If follow-up is required, describe it as a generic engine capability or
contract gap. Do not describe it as a consumer-specific feature request.

`pass` requires redaction confirmation, public behavior evidence, redacted
evidence summary, and no unresolved P1/P2 finding. `blocked`, `skipped`, and
`out_of_scope` are not pass equivalents and must include a status reason.

The JSON Schema checks structure and some expressible constraints. The Python
checker is authoritative for semantic checks such as redaction text scans,
closed P1/P2 finding status, and scope-review consistency.
