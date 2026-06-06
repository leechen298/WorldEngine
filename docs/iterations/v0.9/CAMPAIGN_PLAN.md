# Campaign Plan

Chinese mirror: `CAMPAIGN_PLAN.zh.md`.

Status: final / blocked closeout complete

## Objective

Run v0.9 as a review-gated `/goal` campaign that establishes WorldEngine's
first LLM-backed world lifecycle foundation.

The campaign objective is not to produce a polished game or external product
client. It is to make WorldEngine capable of:

- calling a live provider through WorldEngine-owned configuration.
- generating a public runnable world model from a user's basic worldview.
- validating whether generated worldview output is faithful immediately and
  after bounded runtime execution.
- controlling world execution by tick count, world-time duration, pause,
  resume, and provider/cost bounds.
- accepting user natural-language direction as bounded world-level guidance.
- evolving parameters and events through explicit rules and legality checks.
- exposing brain-inspired public Agent continuity evidence without leaking
  private internals.
- separating Agent consolidation cadence from per-tick runtime progression so
  memory, personality, and skill updates can settle during sleep, rest, or
  low-activity phases.
- defining external narrative projection and out-of-world diagnostic
  player-to-Agent conversation as inspection surfaces, not canonical world
  mutation.
- proving the above through checker-backed LLM-backed lifecycle validation.

## Authoritative Inputs Read For Parent Drafting

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`

## Campaign Rules

- The parent v0.9 package remains the authoritative campaign entrypoint.
- Planned `0.9.x` entries in `v0.9-plan.md` are roadmap-level planned package
  specs. They do not authorize implementation and are not immutable execution
  scripts.
- Implementation authorization starts as no for every child.
- Provider live-call authorization starts as no for every child.
- Mixed/code packages must complete documentation review before
  implementation.
- Historical v0.8 evidence is handoff context only.
- Planned LLM-backed testing docs are validation specs, not current PASS
  evidence.
- Current-session command evidence is required before v0.9 provider live
  smoke, LLM-backed world creation, rule evolution, event legality, Agent
  autonomy, checker support, Validation Client evidence export, full lifecycle
  validation, or release claims.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility requirements, findings, and final assessment semantics.
- Readiness claims must distinguish `planned`, `blocked`, `implemented`,
  `checker-supported`, `evidence-ready`, `validation-pass`, and `out of scope`.

## Planned Child Sequence

1. `0.9.0-v0.9-planning-and-v0.8-handoff-baseline`
2. `0.9.1-provider-live-smoke-and-redaction-boundary`
3. `0.9.2-llm-worldview-ingestion-and-generation-contract`
4. `0.9.3-world-model-rule-parameter-schema`
5. `0.9.4-worldview-generation-fidelity-evaluation`
6. `0.9.5-bounded-runtime-control-and-run-budget`
7. `0.9.6-natural-language-world-direction-boundary`
8. `0.9.7-rule-linked-evolution-and-event-legality`
9. `0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
10. `0.9.9-external-narrative-and-diagnostic-dialogue-boundary`
11. `0.9.10-llm-backed-autonomous-checker-and-fixtures`
12. `0.9.11-validation-client-evidence-handoff-contract`
13. `0.9.12-llm-backed-full-lifecycle-validation-execution`
14. `0.9.13-v0.9-release-candidate-and-closeout`

This sequence is a route proposal. It may be revised by reviewed child package
documents. It must not be followed mechanically if implementation or evidence
uncovers a design problem.

## Cross-Child Handoff Rules

- `0.9.0` hands off reviewed v0.9 campaign structure and v0.8 blocker
  baseline.
- `0.9.1` hands off provider live smoke and redacted provider evidence.
- `0.9.2` hands off LLM-backed world creation output shape and generation
  metadata.
- `0.9.3` hands off world parameters, rule schema, constraints, and boundary
  semantics.
- `0.9.4` hands off worldview fidelity evaluation before and after bounded run.
- `0.9.5` hands off bounded runtime and provider/cost run controls.
- `0.9.6` hands off natural-language world direction semantics and queueing.
- `0.9.7` hands off rule-linked parameter evolution and event legality.
- `0.9.8` hands off brain-inspired public Agent continuity and consolidation
  evidence.
- `0.9.9` hands off external narrative projection and diagnostic dialogue
  boundaries.
- `0.9.10` hands off LLM-backed checker, fixtures, schema, and scorecard.
  Current state: implementation complete / verification passed.
- `0.9.11` hands off public evidence artifacts expected by the Validation
  Client without implementing the client in this repository.
  Current state: documentation reviewed / no implementation authorized.
- `0.9.12` hands off checker-valid BLOCKED full lifecycle validation evidence
  from provider live-smoke preflight.
- `0.9.13` closes v0.9 as BLOCKED after evidence consistency and review gates
  passed.

## Campaign Exit Criteria

v0.9 may be marked `final / closeout complete` only when:

- all active child packages are review complete or explicitly deferred by
  contract.
- implementation-bearing children record current-session command evidence.
- provider live-call evidence is redacted and checker-validated, or remaining
  provider blockers are explicitly classified.
- generated world output is public, system-digestible, premise-specific, and
  not a deterministic generic fallback.
- worldview fidelity checks validate both generated output and bounded runtime
  behavior, or blockers are classified.
- runtime controls prevent unbounded tick, duration, provider-call, and cost
  execution.
- user direction is world-level guidance and cannot directly mutate Agent
  private state or final facts.
- event generation is tied to rules, state, probability, causality, location,
  time, and legality evidence.
- Agent continuity evidence is public and does not expose raw thought, chain of
  thought, private memory, hidden context, or private goals.
- Agent memory, personality, and skill consolidation is not modeled as
  automatic per-tick mutation; sleep/rest/low-activity consolidation evidence
  is explicit or blockers are classified.
- narrative projection and diagnostic player-to-Agent conversation remain
  outside canonical world state unless a reviewed future bridge explicitly
  changes that boundary.
- LLM-backed checker/schema/fixtures can judge the required artifacts.
- Validation Client handoff is defined through public evidence contracts.
- unresolved findings are classified and no P1/P2 remains without explicit
  accepted rationale.

## Stop Conditions

Stop before implementation or closeout if:

- active child package docs are missing required files or mirrors.
- a planned package has not been converted into current child package docs.
- provider call work starts without explicit active child authorization.
- a required evaluator checkpoint is unavailable or reports blocking P1/P2.
- implementation touches files outside the active package contract.
- implementation discovers a design gap and the active child docs have not
  been updated and re-reviewed.
- tests, checkers, or provider calls fail and the package cannot honestly
  record pass evidence.
- user direction bypasses rules and directly writes final facts.
- Validation Client starts owning LLM behavior.
- concrete application content or product-specific backend behavior appears in
  the core repository.
- status surfaces drift between README, current state, plan, review, and
  closeout docs.
