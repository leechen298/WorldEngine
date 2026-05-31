# Intent

Status: review complete

## Why This Exists

`0.6.3` made structured plans compilable. `0.6.4` creates the safe boundary for
plans that may have been produced by AI-assisted tools: they enter as
structured data with redacted provenance, not as prompts, provider sessions, or
trusted executable behavior.

## Intended Outcome

After implementation and review:

- imported plans use provider-independent schemas.
- provenance is inspectable but redacted and contains no secrets, private
  prompts, or external application data.
- invalid imported plans are rejected before compilation.
- tests use static/mock data and do not require network or provider access.

## Non-Goals

- No live LLM/provider integration.
- No API route, dashboard UI, preview API, regeneration, persistence, or
  background execution.
- No prompt library, prompt execution, hidden retry loop, or provider-specific
  orchestration.
- No concrete world content or private validation oracle details.

## Handoff

`0.6.5-generation-validation-metadata-and-preview-api` receives reviewed
generation result/provenance semantics for later API exposure.
