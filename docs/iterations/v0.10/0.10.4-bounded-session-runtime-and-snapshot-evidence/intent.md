# Intent

Chinese mirror: `intent.zh.md`.

0.10.4 turns the session into a bounded runtime execution unit. The current
global runtime controls already support bounded runs and archive callbacks, but
external clients need session-scoped controls and evidence references so the
MVP flow can be driven from a session id instead of loose global endpoints.

The intent is to wrap existing runtime behavior additively:

- keep existing `/runtime/*` endpoints compatible.
- require bounded run requests.
- make paused sessions block session runs until resumed.
- expose public event/snapshot deltas after a session run.
- list snapshots relevant to a session-readable timeline.

This package does not prove product PASS, Agent autonomy, provider quality, or
external checker PASS. It only proves the focused session runtime evidence
slice.
