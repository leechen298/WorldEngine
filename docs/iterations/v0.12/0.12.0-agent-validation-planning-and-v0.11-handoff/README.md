# 0.12.0 Agent Validation Planning And v0.11 Handoff

Chinese mirror: `README.zh.md`.

Status: review complete
Type: documentation-only handoff package
implementation_authorized: no
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Open v0.12 from the completed v0.11 rule-bound world evolution handoff and
prepare the first Agent implementation package.

This package does not implement Agent runtime, memory, narrative inspection,
checker automation, or Validation Client behavior. It records the handoff
facts, checks that v0.12 scope starts from public rule-linked world evidence,
and prepares `0.12.1` as the next documentation-package-needed route after
review.

## Scope

Allowed:

- Create this `0.12.0` package document set and Chinese mirrors.
- Record v0.11 closeout evidence used as v0.12 input.
- Synchronize v0.12 parent status and route after review.
- Prepare `0.12.1` as the next documentation-package-needed route.

Forbidden:

- No runtime, API, schema, frontend, checker, fixture, provider, generated
  result, Validation Client, migration, persistence, or `backend/worldengine/`
  implementation changes.
- No provider live call.
- No external Validation Client execution or PASS claim.
- No Agent runtime, autonomy, memory, rest, sleep, narrative, diagnostic, or
  checker implementation.
- No complete MVP PASS claim.

## Handoff Facts From v0.11

v0.11 closed as scoped `PASS` for rule-bound world evolution.

Evidence available to v0.12:

- public session/manifest/debug handoff surfaces from v0.10 remain available.
- provider/worldview preflight labels configured, safe mock, fallback, and
  blocked provider states without live-provider PASS claims.
- session-scoped structured rules and parameters can be attached and read.
- natural-language direction is accepted only as world-level pressure or
  rejected when it attempts direct final facts or Agent private-state changes.
- rule-compliant session evolution step can build/evaluate/apply public event
  candidates and public diffs with replay evidence.
- worldview fidelity checks now cover immediate and bounded-run public
  premise coverage; missing bounded-run premise indicators fail.
- v0.11 focused closeout regression suite passed with `53 passed`.
- closeout evaluator re-review passed after bounded-run coverage repair.

Known caveats not converted into v0.12 PASS:

- provider live call is not proven.
- external Validation Client automation is not proven.
- Agent autonomy, memory, rest/sleep, narrative, diagnostics, and full MVP
  lifecycle are not proven.
- frontend E2E, durable persistence, and product readiness are not proven.

## Status Checklist

- [x] Package documents drafted.
- [x] Documentation evaluator complete.
- [x] Parent v0.12 route synchronized.

## Next Route

After documentation review passes, v0.12 should route to:

```text
0.12.1-agent-public-state-and-runtime-loop-documentation-package-needed
```
