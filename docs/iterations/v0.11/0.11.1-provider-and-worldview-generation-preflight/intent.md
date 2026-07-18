# Intent

Chinese mirror: `intent.zh.md`.

v0.11 needs rule-bound evolution to start from an honest account of how the
world was or would be generated. Before rules and events depend on worldview
data, clients need a public preflight answer:

- Is a provider configured?
- Would live provider execution be blocked because this package does not
  authorize live calls?
- Is a safe mock being used?
- Is deterministic fallback being used?
- Can a worldview request be classified without leaking private input or
  provider details?

This package turns those answers into a public API and manifest surface without
claiming provider-backed quality or running live provider calls.
