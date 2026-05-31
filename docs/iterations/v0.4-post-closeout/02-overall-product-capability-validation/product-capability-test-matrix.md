# Product Capability Test Matrix

Status: current package matrix

| Capability Area | Current Product Surface | Existing Coverage | This Package Adds | Current Gap / Finding |
| --- | --- | --- | --- | --- |
| Health and service readiness | `/health`, dashboard health display | backend/API, dashboard E2E, Agent smoke | autonomous scorecard fixture | none known |
| Runtime stepping | `/runtime/state`, `/runtime/step`, dashboard Step | backend tests, dashboard E2E, Agent smoke | autonomous scorecard fixture | no restart/persistence test |
| Event timeline | `/world/events`, `/world/event-steps`, TimelinePanel | backend tests, timeline E2E | matrix and autonomous contract alignment | E2E relies on serial in-memory state |
| World params valid flow | `/world/params`, `/world/params/apply`, WorldPanel | backend tests, dashboard E2E, smoke fixture/history | autonomous scorecard fixture | none known |
| World params invalid flow | reserved paths, validation envelope | backend tests, dashboard E2E, smoke fixture/history | autonomous negative rules | none known |
| Archive snapshots/summaries | `/world/snapshots`, `/world/summaries`, MemoryPanel | backend tests, archive-summary E2E | matrix only | not first-batch Agent smoke |
| Params-agent Auto-Tune | `/world/agent/params/propose-and-apply`, dashboard Auto-Tune | backend tests, E2E, latest Agent smoke | docs drift sync, autonomous fixture | stale docs pointed latest smoke at invalid-param |
| v0.4 Agent Loop API | `/world/agent/loop/step` | backend tests, Agent Loop E2E | boundary E2E for noop payload, empty patch, dry-run, event limit, multi/remove | no dashboard UI for loop endpoint |
| Agent smoke | UI/CLI operation logs plus deterministic checker | smoke checker, fixtures, latest Auto-Tune live result | unchanged, revalidated | stale extra screenshot remains P3 |
| Agent autonomous | Codex/test-runner scenario contracts | contract-only docs | minimal scorecard checker, schema, fixtures, timestamped result | not a broad autonomous runner suite |
| Frontend build | `pnpm build` | historical evidence | current command evidence | current TypeScript build failure is P1 |

## Verdict Rules

- E2E PASS comes from Playwright assertions.
- Agent smoke PASS comes from `make validate-agent-smoke-result`.
- Agent autonomous PASS comes from `make validate-agent-autonomous-result`.
- Human or Agent observation can support evidence but never supplies the PASS
  verdict.
