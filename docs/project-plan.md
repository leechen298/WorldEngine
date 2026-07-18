# Project Plan

Chinese mirror: `project-plan.zh.md`.

Status: authoritative project planning overview

## Purpose

This document is the human and agent entrypoint for WorldEngine's overall
project goal and delivery plan.

It does not replace the deeper project documents:

- `project-north-star.md` defines the long-term direction.
- `product-model.md` defines what the product is and is not.
- `scope-boundaries.md` defines hard repository boundaries.
- `roadmap.md` defines version-level delivery.
- `docs/iterations/` defines review-gated implementation packages.

Use this file first when the question is: "What are we building, why, and what
is the current practical path?"

## Overall Goal

WorldEngine is a generic world generation and runtime engine. Its long-term
goal is to create worlds, run those worlds over time, and let Agents live
inside them with memory, continuity, feedback-shaped behavior, and an
inspectable engineered pseudo-self.

The project is not trying to build only a demo, only a story generator, only an
NPC chat system, or only a game client. Those can be consumers of
WorldEngine, but the core repository must remain a reusable engine.

## Product Direction

WorldEngine should eventually support these major capabilities:

1. **World creation**: turn user direction, templates, structured inputs, and
   WorldEngine-owned LLM calls into public, validated, runnable world models.
2. **World runtime**: advance time, evaluate rules, apply consequences, record
   events, create snapshots, and support replay/recovery.
3. **Rule-bound evolution**: let world parameters, environment, events, and
   state changes evolve through explicit rules and legality evidence.
4. **Agent life**: let Agents observe, form intent or no intent, act, react,
   remember, rest, sleep, and consolidate experience over time.
5. **Projection and inspection**: expose the running world to dashboards,
   games, validation clients, novel-style narrative projections, diagnostic
   conversations, and replay tools without letting those surfaces become the
   canonical world.
6. **Validation and evidence**: produce public, redacted evidence that an
   external client and checker can use to classify results as `pass`, `fail`,
   `blocked`, or `not_run`.

## Current Practical Strategy

Earlier planning tried to describe a large product-quality world simulation in
one broad step. The current plan is intentionally smaller:

> Build a complete MVP through multiple gated iterations.

The MVP is not "finished intelligence." It is a full visible loop:

```text
client discovery
-> create world from worldview input
-> run bounded ticks
-> produce rule-linked events and diffs
-> show Agent public behavior and memory evidence
-> export evidence through WorldEngine-Validation-Client
-> classify the result with checker / scorecard / read-only review
```

This makes the engine usable for debugging and automation before world quality,
Agent depth, and product presentation are polished.

## MVP Delivery Plan

### v0.10 - MVP Debug Contract And Runnable World Session

Goal: make WorldEngine discoverable and runnable as a session.

This version should align public manifest/debug handoff contracts for
WorldEngine-Validation-Client, then implement the first user-visible flow:
enter worldview input, create a world session, run bounded ticks, inspect
events/snapshots/state, and view the flow in the dashboard or external client.

Success means the world can be created and run in a debuggable way. It does
not claim Agent autonomy, LLM quality, or full MVP validation.

### v0.11 - MVP Rule-Bound World Evolution

Goal: make the running world change for inspectable reasons.

This version should add honest provider/worldview preflight, structured world
rules and parameters, natural-language direction as bounded world-level
guidance, legal event generation/application, public diffs, replay evidence,
and worldview fidelity checks.

Success means validators can understand why the world changed. It does not
claim complete Agent continuity or full external automation.

### v0.12 - MVP Agent Continuity And Validation Automation

Goal: complete the MVP loop.

This version should add minimal public Agent state and runtime behavior,
short-term memory and rest/sleep consolidation evidence, read-only narrative
and diagnostic inspection surfaces, a stable evidence handoff to
WorldEngine-Validation-Client, and full lifecycle checker/scorecard review.

Success means the MVP can be operated and automatically classified through
exported public evidence. If provider, client, or checker capability is
missing, the closeout should honestly report `PARTIAL`, `BLOCKED`, or `FAIL`.

### v0.13 - Minimum Runnable MVP Anchor

Goal: stop expanding the architecture in the abstract and build one small,
current, independently verifiable vertical slice.

The required path is deterministic and provider-independent so development is
not blocked by live model access. It uses a fixed-seed runnable package, one
session, exact lockstep steps, one Agent causal loop, one accepted and one
rejected intervention in the same explicit window, public event/diff/snapshot
evidence, a generic client protocol, and the WorldEngine administration
console.

After the WorldEngine-side contract passes, the existing external
`WorldEngine-Validation-Client` repository adds a Godot executor and an
isolated checker. The old Web executor remains legacy and cannot self-certify
the new run.

Success means the same session, tick, revision, state hash, Agent evidence, and
intervention results agree across WorldEngine, the administration console, and
Godot, and an independent checker classifies current sealed evidence. The
v0.13 package is defined under `docs/iterations/v0.13/`.

## Role of WorldEngine-Validation-Client

WorldEngine-Validation-Client is an external consumer and validation surface.
It should help humans and Agents operate, inspect, log, replay, and export
evidence from WorldEngine.

It may:

- connect to WorldEngine public APIs.
- discover public surfaces from manifests.
- operate the world like a client.
- record operation logs and API logs.
- export evidence bundles.
- support Agent-operated autonomous validation.

It must not:

- own provider keys or provider calls.
- generate canonical world content.
- mutate the world outside public APIs.
- become the authoritative evaluator.
- store raw prompts, raw provider responses, private Agent memory, raw thought,
  hidden context, secrets, or private evaluator data.

## Player, Direction, Agent, And Branch Boundaries

The MVP track treats the player or user as an external operator by default,
not as an in-world entity. The user may guide the world's direction through
external world-level guidance, but must not directly drop items into the
world, directly trigger detailed events, or assign final facts.

For example, a request such as "this Agent dies now" is not valid world
guidance. A request such as "this Agent may face a lightning-strike risk" can
be accepted as external pressure only if WorldEngine still decides the actual
outcome through weather, location, probability, life state, and public world
rules.

Worldline branches are like code branches: replayable, comparable timelines.
They should not be described as parent/child worlds, source worlds, or a
hierarchy of origins unless a later reviewed package explicitly introduces a
separate recursive-world relationship.

Project documents must distinguish two meanings of "Agent":

- **In-world Agent**: a simulated entity living inside WorldEngine.
- **External validation agent**: Codex, OpenClaw, or another tool operating a
  client and reviewing evidence from outside the world.

Novel-style narrative projections and diagnostic conversations are external
inspection surfaces by default. They can help humans judge whether the world
is running sensibly, but they must not mutate the canonical world timeline or
Agent memory unless a later reviewed bridge explicitly allows that behavior.
Users may request them as read-only session/tick-range/branch/Agent-focused
views. Any request intended to change the future world must leave the
diagnostic surface and enter the v0.11-style direction queue.

## Development Workflow

All code or mixed work must remain iteration-gated:

1. Create or confirm the active package documents.
2. Review `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md`.
3. Authorize implementation only in the active package.
4. Implement the scoped package.
5. Run focused verification and broader regression when required.
6. Record evidence in `review.md`.
7. Close with an honest `PASS`, `PARTIAL`, `BLOCKED`, or `FAIL`.

Documentation-only planning may update project plans, roadmap, scope, and
iteration package documents, but it must not silently modify runtime, API,
schema, frontend, tests, fixtures, migrations, generated results, or external
repositories.

## Non-Goals For The MVP Track

The MVP track must not be expanded into:

- a polished game release.
- concrete demo-world content inside the core repository.
- Steam/native distribution.
- real-consciousness claims.
- unbounded provider-cost execution.
- raw prompt/response logging.
- private Agent memory or raw thought exposure.
- external client ownership of WorldEngine behavior.
- player-as-world-entity gameplay, item drops, or direct detailed event
  triggering.
- full recursive worlds or subjective inner-world cells unless a later
  reviewed package explicitly reopens that scope.

## Decision Rule

When choosing between a large polished feature and a small complete slice,
prefer the complete slice that strengthens this loop:

```text
create -> run -> evolve -> Agent reacts -> evidence -> external validation
```

That loop is the practical definition of the current MVP.
