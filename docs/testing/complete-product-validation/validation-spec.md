# Complete Product Validation Specification

Status: planned validation specification

Chinese mirror: `validation-spec.zh.md`.

## Validation Authority

Complete product validation may claim PASS only from reviewable evidence:

- current-session command output.
- deterministic checker output.
- scorecard checker output.
- saved-result checker output.
- second-Agent read-only review with no blocking P1 or P2 issue.
- durable result files that explicitly record current-session evidence.

The following are not PASS sources:

- plans.
- UI smoke by itself.
- manual impression.
- provider readiness by itself.
- API key presence.
- deterministic mock behavior reported as real behavior.
- an Agent self-report without checker evidence.
- a result directory that has not been checked by the documented checker.

## Roles

| Role | Responsibility | PASS authority |
| --- | --- | --- |
| Main validation agent | Runs commands, operates flows, coordinates evidence, writes result summary. | No self-declared PASS without checker or command evidence. |
| First operating Agent | Operates UI or client flows from a human observer/director perspective. | Supporting evidence only. |
| Second review Agent | Performs read-only evidence review and reports P1/P2/P3 findings. | Can block PASS when P1/P2 exists. |
| Deterministic checker | Validates fixed schemas, fixtures, operation logs, result directories, and redaction rules. | Authoritative for covered fields. |
| Scorecard checker | Validates multi-step autonomous or LLM-backed lifecycle evidence. | Authoritative for declared score items. |
| Human reviewer | Reviews claims and approves next work. | Can accept or reject process, but does not replace missing evidence. |

## Verdict Values

| Verdict | Meaning |
| --- | --- |
| `clean_pass` | Every in-scope required check passed, no blocking P1/P2 remains, and no required evidence is missing. |
| `partial_pass` | Meaningful in-scope checks passed, but at least one required check is missing, skipped, blocked, or failed. |
| `failed` | Core required behavior is contradicted by evidence. |
| `blocked` | Validation cannot proceed because an external dependency, environment, credential, or required artifact is unavailable. |
| `not_run` | The validation layer was planned but not executed. |

Use `out_of_scope` for individual capabilities that are explicitly outside the
current run. Do not use `pass` for future roadmap scope.

## Required Layer Statuses

Every complete validation result must include status for:

- L0 documentation and scope audit.
- L1 schemas and contracts.
- L2 backend unit and API compatibility.
- L3 generation and import.
- L4 runtime lifecycle.
- L5 Agent loop and memory.
- L6 frontend and E2E.
- L7 Agent smoke.
- L8 autonomous saved-result validation.
- L9 LLM-backed lifecycle validation.
- L10 external client evidence review.
- L11 final verdict audit.

If a layer is not executable yet, mark it `blocked`, `not_run`, or
`out_of_scope` with a reason. Do not omit it.

## Non-Negotiable Boundaries

- WorldEngine core must stay generic and must not store concrete validation
  worlds, characters, maps, locations, story rules, or external oracle
  internals.
- External clients may consume public APIs, schemas, CLI contracts, exported
  contracts, and redacted reports only.
- Validation Client must not own LLM generation, provider keys, provider calls,
  or authoritative evaluation.
- User direction may influence external events and world environment, but must
  not directly mutate Agent private state or write final illegal outcomes.
- Agent autonomy evidence must come from WorldEngine public evidence, not
  client scripts.
- Schema changes must be additive unless an active iteration contract allows
  breaking changes.
- Code, checker, fixture, API, frontend, and provider implementation changes
  still require the applicable iteration or milestone gate.

## Redaction Boundaries

Immediate FAIL if evidence contains:

- API keys.
- authorization headers.
- raw prompts.
- raw provider requests.
- raw provider responses.
- raw provider traces.
- private Agent memory.
- private Agent goals.
- raw thought.
- raw chain-of-thought.
- hidden context.
- private evaluator data.
- private validation oracle logic.
- concrete external validation world seed data stored in WorldEngine core.

Allowed evidence must be public and bounded:

- public IDs and public labels.
- public world state summaries.
- public rule summaries.
- public memory summaries.
- public intent summaries.
- public thought or reflection summaries.
- event ids, snapshot ids, diff ids, replay references.
- redacted provider class, model label, success/failure, latency, and
  approximate token bucket.

## Complete Product PASS Rule

Complete product validation can be `clean_pass` only when:

- every CPV row in `coverage-map.md` is present in the result matrix.
- every in-scope CPV row is `pass`.
- every required command or checker has current-session evidence.
- every required artifact exists.
- redaction scan is clean.
- second-Agent review, when required, has no blocking P1/P2.
- skipped or future-scope items are explicitly marked and do not contradict
  the claimed scope.

If LLM-backed lifecycle is in scope but DeepSeek live call is not run,
complete product validation cannot claim LLM-backed lifecycle PASS.
