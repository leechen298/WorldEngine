# Complete Product Validation Gap Routing

Status: planned routing guide

Chinese mirror: `gap-routing.zh.md`.

## Purpose

This guide prevents validation failures from turning into ad hoc fixes. Every
gap found during complete product validation should be classified before any
implementation work begins.

## Failure Taxonomy

| Taxonomy | Meaning |
| --- | --- |
| `provider` | Provider configuration, live call, quota, network, model, or provider response failed. |
| `world_creation` | World creation is generic, deterministic fallback, non-digestible, not provider-backed, or missing required structures. |
| `world_evolution` | Ticks, parameters, rules, snapshots, diffs, or replay do not show coherent rule-driven evolution. |
| `event_legality` | Random/user-directed events bypass rules, directly force illegal outcomes, or lack legality evidence. |
| `agent_autonomy` | Agent action is missing, single-round only, client-scripted, or not tied to WorldEngine public evidence. |
| `redaction` | Evidence leaks secrets, private provider data, private Agent state, raw thought, hidden context, oracle internals, or concrete external world data. |
| `client_evidence` | Validation Client logs, API summaries, screenshots, evidence bundle, replay, diff, or export fields are missing or malformed. |
| `checker_gap` | Scenario is documented but checker/schema/fixture/result validation cannot yet judge it. |
| `runtime` | Core runtime, event, params, snapshot, replay, or API behavior fails outside LLM-specific concerns. |
| `frontend` | Dashboard or E2E behavior fails. |
| `docs` | Documentation is inconsistent, overclaims, or omits required scope/evidence. |
| `environment` | Local services, dependencies, credentials, ports, budget, or external availability block validation. |

## Routing Rules

Route to testing assets when the product behavior exists but validation cannot
judge it:

- missing scenario docs.
- missing saved-result schema.
- missing checker fixtures.
- missing result template.
- missing redaction scan rule.
- missing command profile.

Preferred location:

- `docs/testing`.
- `tools/testing`.

Route to a WorldEngine implementation iteration when core engine capability is
missing:

- provider live smoke endpoint or command.
- provider call abstraction.
- LLM redacted evidence schema.
- LLM-backed world creation.
- world parameter and rule schema.
- world rule evolution engine.
- event legality engine.
- Agent persistent memory evidence.
- Agent persistent action evidence.
- runtime, event, snapshot, replay, projection, or backend API behavior.

Route to a Validation Client milestone when external client evidence or UI is
missing:

- operation log export.
- API summary export.
- evidence bundle field.
- replay/diff/snapshot display.
- LLM-backed lifecycle evidence display.
- Agent autonomous operation capture.
- second-Agent evidence handoff package.

Route to provider/environment when the interface is correct but external
execution fails:

- DeepSeek key missing or invalid.
- provider quota exhausted.
- provider rate limit.
- network failure.
- model unavailable.
- local service startup failure.
- insufficient budget.

Route to redaction repair immediately when secrets or private data leak. Do
not continue validation until the boundary is repaired and rechecked.

## Iteration Decision Rule

Do not open a WorldEngine product iteration just because a validation document
or checker is missing. Use a product iteration only when the missing capability
belongs to WorldEngine core behavior.

Do not open a Validation Client milestone just because WorldEngine cannot
create, evolve, or validate the world. The client observes and exports
evidence; it does not own engine behavior.

Do not repair product code inside a validation run unless an approved package
explicitly authorizes repair.

## Output Format

Every gap should be recorded as:

```text
ID:
Severity:
Taxonomy:
Evidence:
Blocked PASS item:
Recommended route:
Required next document or package:
Stop rule triggered: yes/no
```
