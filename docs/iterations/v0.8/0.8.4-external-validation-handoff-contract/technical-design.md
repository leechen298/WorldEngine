# Technical Design

Status: documentation-only design

## Design Boundary

This package designs a contract vocabulary, not a runtime or checker
implementation. The design is intentionally expressed in documentation so a
later package can choose whether to implement schemas, templates, or checkers
without smuggling that work into this stage.

## Handoff Record Shape

A future machine-checkable handoff record, if implemented by a later package,
should use this conceptual shape:

```text
ExternalValidationHandoff
  handoff_id
  version
  engine_reference
  surface_id
  contract_surface_path
  evidence_class
  status
  evidence_reference
  redaction_confirmation
  forbidden_detail_review
  unresolved_findings
  rationale
  compatibility_notes
  scope_review
```

This package does not create the schema file. The shape is a design target for
later review.

## Status Design

Allowed handoff statuses:

- `contract_ready`: a contract surface exists and is reviewed.
- `core_evidence_ready`: a later package has current-session evidence for the
  core-side surface.
- `blocked`: the surface cannot support the intended claim until a blocker is
  fixed or accepted by a later reviewed package.
- `skipped`: the check was not run and has an explicit rationale.
- `out_of_scope`: the surface is outside the active package or repository
  boundary.

Forbidden status behavior:

- `blocked`, `skipped`, and `out_of_scope` must not count as PASS.
- `contract_ready` must not count as runtime/API/product/external validation
  PASS.
- `core_evidence_ready` must not count as external validation PASS unless a
  later external workflow provides reviewed public evidence.

## Redaction Design

Every public handoff record must include both:

- a redaction confirmation statement.
- a forbidden-detail review with explicit false/none values for forbidden
  classes.

Future machine checks should reject obvious private paths, UI selector markers,
hidden reset markers, oracle-internal markers, seed-data markers, transcript
markers, secrets, provider trace terms, raw prompt terms, and non-redacted
external event payload markers.

## Compatibility Design

The design composes existing public baselines:

- v0.7 redacted report semantics define report safety.
- v0.7 readiness manifest semantics define public evidence references.
- v0.7 projection read-model semantics define read-only/no-write boundaries.
- v0.8 `0.8.1` defines claim taxonomy.
- v0.8 `0.8.2` defines observable surfaces.
- v0.8 `0.8.3` provides bounded core-readiness evidence.

This package does not change those files or behaviors.

## Review Design

Review must verify that the package:

- names the handoff vocabulary without implementing it.
- keeps implementation authorization closed.
- preserves forbidden detail classes.
- keeps v0.7 repair evidence as handoff context only.
- leaves `0.8.5` responsible for current-session core smoke evidence.
