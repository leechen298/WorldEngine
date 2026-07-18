# Contract

Chinese mirror: `contract.zh.md`.

Status: documentation drafted / review pending

## Public Concepts

- **Immediate worldview fidelity**: public scorecard evidence that checks
  whether generated public world model, creation summary, and rule summary
  cover material public premise indicators.
- **Bounded-run worldview fidelity**: public scorecard evidence that checks
  bounded runtime/event/diff evidence for missing premise coverage,
  contradictions, redaction failures, or evidence gaps.
- **v0.11 closeout result**: a bounded claim about rule-bound world evolution,
  not Agent autonomy, provider quality, external validation, or complete MVP
  readiness.

## Allowed Changes

After review approval, this package may change:

- `backend/app/core/worldview_fidelity.py` and
  `backend/app/schemas/world_generation.py` for additive public fidelity
  helpers/schema refinements.
- focused fidelity tests and v0.11 regression tests.
- v0.11 package docs, parent status/review/plan docs, and handoff docs.
- manifest/review text only if needed to classify closeout honestly.

## Forbidden Changes

This package must not:

- use raw prompt, raw provider response, provider trace, hidden context,
  private evaluator data, secret, or private Agent memory in public evidence.
- claim PASS from subjective review without current-session scorecard/test
  evidence.
- implement provider live calls or external Validation Client behavior.
- implement Agent autonomy, pseudo-self, sleep consolidation, or long-term
  memory.
- change frontend, persistence, migrations, concrete demo fixtures, or
  `backend/worldengine/`.
- add new rule/direction/event-generation feature scope unless required as an
  explicitly recorded blocker repair.

## Compatibility Requirements

- Existing world generation, provider preflight, session, rules, directions,
  event/diff, manifest, and public evidence tests must remain compatible.
- Fidelity artifacts must be public and redaction-safe.
- v0.11 closeout must distinguish passed, blocked, failed, not-run, and
  out-of-scope claims.
- External Validation Client and provider live claims remain unauthorized unless
  a later package explicitly authorizes them.

## Out-Of-Scope Follow-Ups

- v0.12 owns Agent continuity, external automated validation, final MVP
  validation, and any Validation Client automation.
