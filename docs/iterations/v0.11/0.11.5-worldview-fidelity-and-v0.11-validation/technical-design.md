# Technical Design

Chinese mirror: `technical-design.zh.md`.

Status: documentation drafted / review pending

## Implementation Structure

Use deterministic public fidelity helpers if available:

```text
evaluate_immediate_worldview_fidelity(...)
evaluate_bounded_run_worldview_fidelity(...)
build_worldview_fidelity_scorecard(...)
```

The closeout path is evidence-first:

```text
public generation summary + rule summary
  -> immediate fidelity artifact
public runtime/event/diff/snapshot summary
  -> bounded-run fidelity artifact
immediate + bounded-run
  -> v0.11 scorecard
scorecard + child package reviews
  -> v0.11 closeout and v0.12 handoff
```

## Affected Files

Allowed implementation/evidence files:

- `backend/app/core/worldview_fidelity.py`
- `backend/app/schemas/world_generation.py`
- `backend/app/tests/test_worldview_fidelity_evaluation.py`
- focused existing regression tests when required

Allowed documentation/status files:

- this package directory.
- `docs/iterations/v0.11/CURRENT_STATE.md`
- `docs/iterations/v0.11/CURRENT_STATE.zh.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/README.zh.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`
- `docs/iterations/v0.11/review.md`
- `docs/iterations/v0.11/review.zh.md`
- v0.12 route handoff docs if required by closeout.

## Compatibility Strategy

- Keep fidelity helpers deterministic and public.
- Treat deterministic generic fallback as not sufficient for final fidelity
  PASS.
- Treat missing bounded-run evidence as blocked, not pass.
- Treat redaction failures as fail.
- Keep provider live, external Validation Client, and Agent autonomy claims out
  of v0.11 closeout.

## Anti-Drift Rules

- No hidden evaluator oracle.
- No raw provider/prompt evidence.
- No external validation implementation.
- No widening to v0.12 Agent continuity.
