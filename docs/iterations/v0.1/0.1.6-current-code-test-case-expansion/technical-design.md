# Technical Design

## Current State

The current v0.1 E2E suite lives in `frontend/e2e/dashboard.spec.ts` and
implements three browser scenarios:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

The current Agent smoke validator supports only
`dashboard-basic-runtime`. It rejects direct API operations in
`operation-log.jsonl` and requires `verdict_source:
deterministic_checker`.

The dashboard already contains current-code surfaces for params agent
auto-tune, timeline pagination, and archive summary display, but the UI lacks
stable selectors for some future E2E and Agent-operated assertions.

## Documentation Architecture

0.1.6 adds four documentation groups:

- `docs/testing/e2e-scenarios/` for deterministic Playwright scenario
  contracts.
- `docs/testing/agent-smoke/scenarios/` for basic Agent smoke contracts.
- `docs/testing/agent-autonomous/` for Codex/test-runner autonomous protocol,
  scorecard, and scenario contracts.
- `docs/testing/test-implementation-prerequisites.md` for selector, validator,
  and checker prerequisites that must be implemented before 0.1.7 can execute
  more scenarios.

## Contract Alignment and Invariants

- Scenario status must be explicit.
- Implemented scenarios must name the current implementation source.
- Non-executable scenarios must name their blocker.
- PASS/FAIL sources must be deterministic.
- Agent smoke and Codex/test-runner autonomous tests must not record direct API
  calls as Agent operations.
- Codex/test-runner autonomous docs must explain that "Agent" means the tester
  agent, not a future WorldEngine in-world Agent.

## Affected Surfaces

Affected:

- documentation under `docs/`.

Not affected:

- backend runtime.
- frontend runtime.
- Playwright implementation.
- Agent smoke validator.
- fixtures.
- skills.
- `backend/worldengine/`.

## Data Model / Schema Changes

None.

## Runtime / Service Design

None. Future implementation packages may add selectors, validator branches,
scorecard schemas, or checker commands, but this package only records the
required contracts.

## Future Implementation Prerequisites

0.1.7 or later must address prerequisites before executing the blocked
scenarios:

- add stable UI selectors for params-agent auto-tune, MemoryPanel summary, and
  timeline expanded details.
- extend the Agent smoke validator for `dashboard-params-flow` and
  `dashboard-invalid-param`.
- define an autonomous scorecard checker before running autonomous scenarios.
- keep Playwright E2E API reads limited to deterministic test-script assertion
  evidence.

## Risks

- A scenario file may be mistaken for executable coverage.
  Mitigation: each scenario has an explicit status and PASS source.
- Agent smoke may be mistaken for full autonomous coverage.
  Mitigation: Agent smoke and autonomous docs state the distinction directly.
- The word Agent may conflict with future in-world Agent work.
  Mitigation: autonomous docs define Agent as Codex/test-runner agent.
- Documentation-only work may accidentally change code.
  Mitigation: the test plan includes a docs-only diff boundary check.
