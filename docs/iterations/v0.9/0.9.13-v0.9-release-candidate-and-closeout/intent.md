# Intent

Chinese mirror: `intent.zh.md`.

## Why This Package Exists

v0.9 implemented and documented several LLM-backed foundation slices, but the
version cannot honestly claim a full LLM-backed lifecycle PASS. 0.9.12
classified the final validation run as BLOCKED before any live provider call.

This package exists to prevent status drift: it records the release-candidate
boundary, keeps unresolved blockers explicit, and hands future work a precise
post-closeout route.

## Intended Outcome

- v0.9 parent docs reflect the final BLOCKED closeout state.
- The 0.9.12 durable result summary is referenced as authoritative evidence.
- No implementation, provider, Validation Client, or external validation claim
  is widened.
- Future work can choose a narrower provider/runner repair package or v1.0
  planning without misreading v0.9 as product-ready.
