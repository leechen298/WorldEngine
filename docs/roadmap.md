# Roadmap

Status: planning guide

This roadmap defines delivery direction. Each version still requires scoped
iteration packages before implementation.

## v0.1 - Runtime Scaffold

Status: current baseline

Goal: establish the monorepo, FastAPI backend, Vue dashboard, runtime tick,
event log, params, archive, and basic API envelope.

## v0.2 - Recursive World Foundation

Status: final / closeout complete

Goal: establish the documentation governance, north star, recursive world
schema/spec language, additive event contract, generic schema smoke
validation, external fixture boundary, legacy boundary, iterative development
workflow, and reviewable release-candidate evidence.

Non-goal: do not migrate RuntimeEngine to WorldCell or build demo-specific
runtime.

Concrete external worlds must not appear inside the core repository as
fixtures, loader inputs, projection targets, or acceptance targets. They may
consume WorldEngine only through public APIs, CLI contracts, schemas, exported
contracts, and redacted validation reports.

### v0.2.5 - Core Boundary Cleanup and Roadmap Reset

Goal: remove concrete external-world anchors from active core docs, fixtures,
and tests, and reset the later roadmap around generic engine consumers.

### v0.2.6 - Iteration Workflow and Plan Reset

Goal: reset the remaining v0.2 package sequence, add the automation workflow
for ChatGPT / Codex A / Codex B iteration, and abstract residual concrete demo
anchors from v0.2 iteration documentation.

### v0.2.7 - Recursive Schema Contract Hardening

Goal: harden EntityRef, WorldCell, and WorldSpec schema contracts and generic
schema tests without implementing runtime loading.

### v0.2.8 - Event Reference Contract Hardening

Goal: harden EventRef and Event.refs as additive event reference contracts
without implementing a resolver or causality engine.

### v0.2.9 - Generic Schema Evidence and Boundary Audit

Goal: audit v0.2 schema, event, external boundary, and legacy boundary
evidence before compatibility review.

### v0.2.10 - Legacy Boundary and Compatibility Review

Goal: clarify v0.1 runtime scaffold compatibility and legacy boundaries before
v0.3 bridge work.

### v0.2.11 - v0.2 Release Candidate Bundle

Goal: prepare release-candidate evidence for human / ChatGPT review without
declaring final release.

### v0.2.12 - v0.2 Final Closeout

Goal: perform final closeout only after the release-candidate bundle passes
human / ChatGPT review.

## v0.3 - WorldSpec Loader and Runtime Bridge

Status: final / closeout complete

Goal: load validated generic WorldSpec data into runtime context without
losing v0.1 runtime compatibility.

Handoff: v0.4 may start only through its own reviewed iteration package.

## v0.3.5 - External Fixture Contract Readiness

Goal: define how external fixture runners invoke the core repository through
public contracts without creating those repositories inside WorldEngine.

## v0.4 - Agent-in-World Minimal Loop

Status: final / closeout complete

Goal: let agents perceive world events, produce action intents, receive action
results, and affect world state through a minimal validated loop.

Handoff: v0.5 may start from the reviewed request-driven minimal loop, but
memory and self-continuity remain explicitly future scope.

## v0.5 - Memory and Self-Continuity Substrate

Status: final / closeout complete

Goal: introduce working memory, episodic memory, relationship state,
self-summary, reflection records, and personality drift signals that can affect
future action.

Closed scope: v0.5 implemented additive generic working-memory and
episodic-memory backend schemas, a process-local in-memory substrate, and
bounded read-only memory context in Agent Loop perception. Relationship state,
self-summary, reflection records, and personality drift signals are refined as
deferred contracts only.

Final evidence: focused backend memory/loop/action compatibility `33 passed`;
full backend regression `145 passed`; required docs/mirrors `missing=0`;
changed-file scope guard `out_of_scope=0`; closeout consistency evaluator
PASS. No frontend, E2E, Agent smoke, autonomous, external validation,
projection readiness, or product readiness pass claim is made.

Handoff: v0.6 world generation v1 may start only from its own reviewed
iteration package.

## v0.6 - World Generation v1

Status: final / closeout complete

Goal: generate runnable WorldSpec data from templates and structured
AI-assisted generation with validation, metadata, preview, and regeneration
support.

Closed scope: v0.6 implemented generic world-generation contracts, template
semantics, deterministic template catalog generation, structured generation
plan compilation, AI-assisted plan import boundaries without live provider
integration, validation metadata, preview/regeneration/runtime-readiness APIs,
and dashboard generation preview with focused E2E smoke.

Final evidence: full backend regression `220 passed`; frontend unit
`36 passed`; frontend build passed with a Vite large-chunk warning only; E2E
`16 passed`; required docs/mirrors `missing=0`; changed-file scope guard
`out_of_scope=0`; closeout consistency evaluator PASS. No external validation
readiness, projection readiness, product readiness, Agent smoke, autonomous
runner, live provider, or generation-quality pass claim is made.

Handoff: v0.7 external validation readiness may start only from its own
reviewed iteration package.

## v0.7 - External Validation Readiness / Projection Consumer Readiness

Goal: make WorldEngine ready for external validation suites and projection
consumers through public contracts, redacted reports, and compatibility
evidence.

## v0.8 - Minimum Proved Working WorldEngine / External Validation Readiness

Goal: prepare WorldEngine's core runtime, generation, Agent loop, memory
context, and projection/read-model surfaces so an external validation function
can verify that the engine reaches a minimum normally working state without
moving validation logic, external application code, app-specific behavior, or
concrete world content into the core repository.

v0.8 is not the external validation implementation and is not the first
external product application. It defines the core-side readiness boundary,
observable public surfaces, evidence expectations, and stop rules needed for a
separate external validator or projection application to judge whether
WorldEngine works.

## v0.9 - LLM-backed World Lifecycle Foundation

Status: reviewed / planning-ready

Goal: move WorldEngine from a proved basic lifecycle to the first LLM-backed
lifecycle foundation where the engine owns live provider calls, turns a user's
basic worldview into a runnable public world model, evaluates generated
worldview fidelity, controls bounded world execution, accepts natural-language
world direction as rule-bound environmental guidance, evolves parameters and
events through explicit legality evidence, exposes brain-inspired public Agent
continuity and consolidation evidence, keeps narrative projection and
out-of-world diagnostic conversation outside canonical world mutation, and
validates the full flow through checker-backed artifacts.

v0.9 is not a product client, game release, concrete demo world, or external
validator implementation. It must not move provider ownership, evaluation
authority, concrete world content, or application-specific backend behavior out
of the generic WorldEngine core boundary.

## v0.10 - MVP Debug Contract And Runnable World Session

Status: PARTIAL / WorldEngine-side MVP slice complete; external Validation Client export blocked

Goal: start the MVP delivery track by aligning the public manifest/debug
handoff contract for WorldEngine-Validation-Client, then create the first
runnable world session slice: worldview input, session identity, bounded
runtime, events, snapshots, dashboard inspection, public client discovery,
and replay/worldline branch terminology that avoids parent/source semantics.

v0.10 is not a full LLM-quality, Agent-autonomy, or product-readiness claim.
It should produce a debuggable session baseline that can honestly report
`pass`, `fail`, `blocked`, or `not_run` evidence.

Handoff: v0.11 may start only after the runnable session and debug handoff are
evidenced or explicitly blocked.

## v0.11 - MVP Rule-Bound World Evolution

Status: PARTIAL / closeout complete; external Validation Client export blocked

Goal: make the runnable MVP world evolve through public rules, parameters,
user direction boundaries, legal event candidates, applied public diffs, and
worldview fidelity evidence.

User direction remains external world-level pressure: it may introduce a risk
such as a lightning-strike possibility, but WorldEngine must decide the actual
outcome through rules, state, probability, and legality evidence instead of
copying user instructions into final facts.

v0.11 is not the Agent pseudo-self or full validation automation version. It
should make world changes explainable before Agent continuity is layered on.

Handoff: v0.12 may start only after rule-linked event/diff evidence exists or
the missing handoff is explicitly recorded as a blocker.

## v0.12 - MVP Agent Continuity And Validation Automation

Status: PARTIAL / closeout complete; external Validation Client export blocked

Goal: complete the MVP by adding a minimal public Agent continuity loop,
memory/rest consolidation evidence, read-only novel-style narrative and
diagnostic inspection surfaces, explicit in-world-Agent versus external
validation-agent terminology, and checker-backed full lifecycle validation
through WorldEngine-Validation-Client evidence.

v0.12 is the first version that may claim complete MVP PASS, but only through
checker, scorecard, and read-only review evidence. If provider, client, or
checker capability is missing, closeout should honestly classify the result as
PARTIAL, BLOCKED, or FAIL.

Closeout result: PARTIAL. WorldEngine-side Agent continuity, memory,
inspection, handoff, and deterministic checker evidence are present. Complete
MVP PASS remains blocked by the missing current v0.12 external Validation
Client export/result directory.

## v0.13 - Minimum Runnable MVP Anchor

Status: planning / documentation package ready for user review

Goal: reset implementation around one deterministic, single-session,
single-Agent, lockstep vertical slice that proves world generation, canonical
runtime, Agent action and experience, accepted/rejected operator intervention,
generic projection, administration-console operation, Godot consumption, and
independent external classification as one causal run.

v0.13 treats v0.10-v0.12 code and evidence as historical background rather
than the target design or current proof. Existing work may be reused only when
it passes the new contract. The version must not delete historical work, put a
concrete validation world in WorldEngine, or make Godot a core dependency.

Delivery sequence:

1. `0.13.0-worldengine-runnable-anchor`: WorldEngine-side generic protocol,
   deterministic package/session/runtime/Agent/intervention loop, evidence,
   and administration console.
2. `0.13.1-godot-validation-client-anchor`: external Godot executor and
   isolated checker in `WorldEngine-Validation-Client`.
3. `0.13.2-anchor-run-validation-and-closeout`: clean cross-client run and
   evidence-backed `PASS`, `PARTIAL`, `BLOCKED`, or `FAIL`.

Complete v0.13 PASS requires the external Godot/checker run. Passing
`0.13.0` alone proves only the WorldEngine-side anchor.
