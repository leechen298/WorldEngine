# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Closeout Inputs

- v0.10 package reviews and final route status.
- v0.11 package reviews and final route status.
- v0.12 package reviews from `0.12.0` through `0.12.5`.
- `0.12.5/full-lifecycle-validation-result.md`.
- `0.12.5/scorecard-summary.md`.
- roadmap and scope boundaries.

## Closeout Outputs

- `mvp-closeout-report.md`.
- parent v0.12 state updated to final closeout.
- roadmap v0.12 status updated to PARTIAL.

## Verification

Closeout verification is documentation-oriented:

- required-file checks.
- status consistency scans.
- authorization scans.
- `git diff --check`.
- optional read-only evaluator review.

No code tests are required unless closeout modifies code, which it must not do.
