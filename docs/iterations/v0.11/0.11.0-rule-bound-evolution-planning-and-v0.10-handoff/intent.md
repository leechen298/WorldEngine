# Intent

Chinese mirror: `intent.zh.md`.

v0.11 depends on the v0.10 runnable-session vertical slice. This package makes
that dependency explicit before any rule-bound world evolution implementation
starts.

The intended outcome is narrow:

- v0.10 closeout evidence is recorded as the v0.11 input.
- v0.10 caveats remain caveats, not hidden PASS claims.
- v0.11 route advances only to `0.11.1` documentation package creation.
- no implementation scope opens in this package.

This keeps v0.11 from bypassing the session/runtime/evidence contract while
also preventing v0.10 provider or external-validation gaps from being
misrepresented as solved.
