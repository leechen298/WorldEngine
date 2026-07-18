# Intent

Chinese mirror: `intent.zh.md`.

v0.12 needs visible in-world Agent life evidence. Existing request-driven Agent
loop surfaces prove that perception and action adapters exist, but they do not
by themselves prove session-scoped Agent autonomy because the client can submit
an intent directly.

This package adds the first MVP Agent continuity layer:

- the Agent has public state within a session.
- the Agent step reads public runtime/session/event context.
- WorldEngine chooses a public intent state such as no-intent, wait, rest, or
  a bounded action.
- the result is recorded as public evidence events that later packages can use
  for memory, narrative, diagnostics, and validation handoff.

The package intentionally stays minimal. It does not implement long-term
memory consolidation, sleep, narrative/diagnostic surfaces, external
Validation Client automation, or final MVP closeout.
