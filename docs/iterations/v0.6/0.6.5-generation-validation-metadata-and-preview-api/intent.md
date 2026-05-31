# Intent

Status: review complete

## Problem

`0.6.2` can generate `WorldSpec` data from reviewed templates, `0.6.3` can
compile structured plans, and `0.6.4` can import provider-independent
structured plans with redacted provenance. Consumers still need a stable
backend API surface that can validate a request, return bounded generation
metadata, and preview the generated `WorldSpec` before later packages add
regeneration, runtime-readiness, or dashboard flows.

## Goals

- Expose generation preview through the existing FastAPI application.
- Preserve the current `ApiResponse(code, data, msg)` success envelope and
  `ApiErrorResponse(code, msg, data)` validation-error envelope.
- Reuse existing template, plan, and imported-plan validation instead of
  introducing a parallel validator.
- Return only public `WorldSpec` preview data, deterministic diagnostics, and
  bounded metadata/provenance.
- Make request shape errors distinguishable from generation validation
  failures:
  - invalid HTTP request shape uses the existing 422 handler and API error
    envelope.
  - invalid generation content returns a 200 preview result with
    `validation_status: failed`, diagnostics, and no generated `WorldSpec`.

## Non-Goals

- No dashboard UI or frontend workflow.
- No durable persistence or migrations.
- No regeneration behavior.
- No runtime loading/readiness assertion.
- No live AI provider calls, prompt execution, provider SDKs, background jobs,
  or network access.
- No external validation readiness, projection readiness, product readiness,
  release readiness, autonomous validation, or generation-quality claim.

## Users And Consumers

This package serves backend/API consumers that need to inspect generation
results before running or saving generated worlds. It prepares later v0.6
packages without turning WorldEngine into an application-specific backend.

## North Star Alignment

The package advances the north-star world generation capability by exposing
reviewable generated-world structure through a generic API. It keeps
generation contract-driven, inspectable, deterministic under tests, and
separate from external projection applications.

## Handoff

When complete, `0.6.6-regeneration-and-runtime-readiness-integration` receives
public preview and metadata semantics for bounded regeneration and
runtime-readiness checks.
