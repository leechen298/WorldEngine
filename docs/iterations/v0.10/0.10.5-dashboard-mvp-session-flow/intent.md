# Intent

Chinese mirror: `intent.zh.md`.

0.10.5 makes the MVP session visible. The backend can now create a session
from worldview input and run bounded session ticks with public evidence, but
the dashboard still presents separate backend/runtime/generation/world panels.

The intended dashboard flow is:

```text
enter worldview -> create session -> run bounded ticks -> inspect status,
timeline, and snapshots
```

The UI should stay operational and dense rather than marketing-like. It should
make the session id, generation mode, runtime evidence, and snapshot evidence
visible without exposing private prompts, provider traces, or secrets.

The dashboard remains a client. Backend session/runtime APIs remain the system
authority.
