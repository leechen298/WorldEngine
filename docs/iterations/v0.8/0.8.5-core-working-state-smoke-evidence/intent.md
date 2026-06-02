# Intent

## Problem

v0.8 cannot reach a minimum working-state claim from documentation alone.
`0.8.3` proved one bounded core-readiness slice, and `0.8.4` defined how
handoff evidence should be classified, but the campaign still needs a broader
current-session smoke matrix over the public core surfaces that matter for
WorldEngine's normal operation.

Without this package, later audit or release-candidate work would risk
overclaiming from:

- historical v0.7/v0.6 evidence.
- a single focused readiness probe.
- documentation-only handoff contracts.
- tests that do not cover the claimed surface.

## Objective

Define and review the command matrix, evidence classes, artifact boundaries,
and non-claims for v0.8 core-side working-state smoke evidence.

After review, the package may run only the authorized commands and record only
the evidence those commands actually prove.

## Non-Goals

- Do not implement or run an external validator.
- Do not import, clone, or run an external app repository.
- Do not add product-specific scenarios, concrete validation worlds, private
  transcripts, screenshots, UI selectors, private paths, oracle details,
  provider traces, prompts, secrets, or external event payloads.
- Do not change product/runtime behavior just to make validation pass.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, projection application readiness, full autonomous PASS, or final
  v0.8 readiness.

## Success Criteria

Documentation review succeeds when the package:

- names exact command groups and their proof boundaries.
- separates in-scope, skipped, blocked, and out-of-scope checks.
- defines redacted evidence and artifact rules.
- records compatibility expectations for v0.3 through v0.7 surfaces.
- keeps implementation and evidence execution authorization closed until
  review.
