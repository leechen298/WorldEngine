# Technical Design

Status: documentation-stage design

## Artifact Shape

This package creates a documentation-only release-candidate bundle with these
files:

- package governance docs: `README.md`, `intent.md`, `contract.md`,
  `technical-design.md`, `test-plan.md`, `plan.md`, and `review.md`.
- Chinese mirrors for each governance doc.
- release-candidate artifact: `release-candidate-summary.md` and
  `release-candidate-summary.zh.md`.

## Bundle Model

The release-candidate summary is organized as a set of bounded tables:

1. Package matrix: reviewed package, evidence source, disposition, and
   boundary.
2. Evidence references: path, existence expectation, supported claim, and
   claim limit.
3. Compatibility summary: v0.3 through v0.7 surfaces and their reviewed
   evidence relationship.
4. Exclusions: surfaces not claimed by v0.8 release-candidate packaging.
5. Findings: P1/P2/P3 status and handoff disposition.
6. Handoff decision: whether final closeout review may start.

## Status Transitions

Allowed transition in this package:

```text
0.8.7-documentation-package-needed
  -> documentation-review-needed
  -> review complete
  -> 0.8.8-documentation-package-needed
```

Only the first transition is part of initial package creation. Later
transitions require review evidence in `review.md`.

## Evidence Boundaries

The summary must treat evidence as follows:

- `0.8.3` backend/app changes and focused tests are current-session
  implementation evidence for the bounded core-readiness surface only.
- `0.8.5` smoke evidence is current-session bounded core/backend evidence
  only.
- v0.7 code-review and `0.7.9` repair evidence are handoff evidence only.
- `0.8.6` audit is release-candidate packaging authorization evidence only.
- Historical v0.1 through v0.7 testing docs are context unless a reviewed
  v0.8 package explicitly cites them with a boundary.

## Redaction Design

The package stores only public repository paths and redacted evidence
classifications. It must not introduce private external validator commands,
private repository paths, hidden scenario data, UI selectors, oracle internals,
raw prompts, provider traces, secrets, or concrete validation-world details.

## Implementation Impact

No runtime, schema, API, frontend, backend test, checker, fixture, migration,
external repository, generated result, deployment, or `backend/worldengine/`
implementation impact is permitted.
