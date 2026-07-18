# AGENTS.md

WorldEngine generates a world, advances its authoritative history, runs Agents,
accepts bounded interventions, and publishes public projections to independent
clients.

## Active Goal

The active source of truth is `docs/current/MVP.zh.md`.

Files under `docs/iterations/` are historical design and evidence records. They
may explain earlier decisions, but they do not route current work, require a
version package, or block implementation.

## Working Mode

- Inspect current code and runtime evidence before relying on documentation.
- Implement the smallest complete vertical slice that advances the active goal.
- Update the current MVP document when scope, decisions, or evidence changes.
- Detailed iteration packages, bilingual mirrors, per-task commits, and routine
  evaluator gates are optional, not prerequisites.
- Use subagents when parallel work materially helps; the main agent owns
  integration and verification.

## Hard Boundaries

1. `backend/app/` is the active backend. `backend/worldengine/` is legacy.
2. WorldEngine owns authoritative history, rules, Agent continuity, and public
   evidence. Rendering and fine physics belong to external clients or engines.
3. External clients use public HTTP/OpenAPI contracts only. Do not import
   WorldEngine internals or add client-specific worlds, maps, art, or UI to the
   engine core.
4. Accepted state changes must produce events and replayable evidence.
5. Public responses must not expose secrets, provider traces, raw prompts,
   private memory, or chain-of-thought.
6. An executor may record evidence but may not certify its own PASS. Final MVP
   verdicts belong to an independent checker.
7. Preserve unrelated user changes and avoid destructive git operations.

## Verification

Run focused tests while developing, then the full backend suite, frontend tests
and build, a real HTTP smoke, and the external client/checker flow before
claiming MVP completion. Report failures and unverified areas explicitly.
