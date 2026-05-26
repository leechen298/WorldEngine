# Technical Design

## Design Summary

0.2.11 is a documentation assembly package. It creates a release-candidate
bundle by reading existing v0.2 evidence, classifying each claim, and
publishing a review handoff. It does not add implementation behavior.

## Source Inputs

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- completed v0.2 package reviews from 0.2.1 through 0.2.10.
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/findings.md`
- `docs/releases/v0.2.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/legacy-boundary.md`

Chinese mirrors must be used for synchronized `.zh.md` outputs where they
exist.

## Output Structure

### Release-Candidate Bundle

`docs/iterations/v0.2/v0.2-release-candidate-bundle.md` must include:

- release-candidate status and explicit not-final warning.
- v0.2 scope summary.
- completed package table.
- claim-to-evidence matrix.
- test and verification evidence summary.
- compatibility and boundary summary.
- known limitations and non-goals.
- unresolved findings and blocker classification.
- final-closeout prerequisites.
- request for human / ChatGPT review.

The `.zh.md` mirror must preserve the same headings and decisions.

### Final Review Bundle

`final-review-bundle.md` must follow
`docs/iterations/v0.2/final-review-bundle-template.md` and fill each section
with 0.2.11-specific evidence. It must include branch, status, changed files,
contract mapping, forbidden-change confirmation, commands run, test results,
grep classification, unresolved findings, compatibility review, scope review,
and requested reviewer decision.

The `.zh.md` mirror must preserve the same review information.

### Release Draft Update

`docs/releases/v0.2.md` must remain a release draft but add the
release-candidate evidence summary. It must state that final release remains
blocked until 0.2.12 approval.

The `.zh.md` mirror must stay synchronized.

## Claim Classification

Each claim must use one or more of these statuses:

- `implemented`
- `documented`
- `tested`
- `reviewed`
- `planned`
- `not implemented`
- `historical artifact`
- `finding`

If a claim cannot be mapped to evidence, record it as a finding instead of
rewriting the claim to appear complete.

## Findings Handling

Use `docs/iterations/v0.2/findings.md` for unresolved or newly discovered
risks:

- P1: blocks release-candidate acceptance and final closeout.
- P2: blocks final closeout unless explicitly accepted by review.
- P3: may be a v0.3 handoff if documented and non-blocking for v0.2.

## Status Rules

- During documentation-stage preparation, this package is `ready for review`.
- After approved implementation of the release-candidate bundle, this package
  may be marked `review complete`.
- v0.2 must not be marked final in this package.
- 0.2.12 must remain planned until release-candidate review approval exists.

## Bilingual Mirror Rules

Every created or modified release-candidate document must have an English and
Chinese mirror with the same status, scope boundaries, acceptance criteria,
and findings classification.

## Security and Boundary Notes

The bundle must not expose private validation internals, concrete external
world details, private runner state, or application-specific backend logic. It
may summarize anchor sweeps only through abstract classifications.
