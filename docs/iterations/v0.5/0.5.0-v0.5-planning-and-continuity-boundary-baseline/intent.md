# Intent

Status: review complete

## Problem

v0.4 deliberately excluded memory, episodic memory, relationship state,
self-summary, reflection, and personality drift. v0.5 owns that roadmap scope,
but starting it without a reviewed package would risk mixing product-boundary
decisions with runtime implementation.

The project needs a deterministic v0.5 `/goal` package that fixes the scope,
review gates, compatibility baseline, handoff evidence, and first
implementation slice before any code changes occur.

## Goal

After this package, WorldEngine has a reviewable v0.5 campaign root and first
child package that:

- defines the v0.5 memory/self-continuity boundary.
- splits all six capabilities into contract-first and implementation-later
  work.
- identifies working memory and episodic memory as the first implementation
  candidates.
- keeps relationship state, self-summary, reflection records, and personality
  drift signals as schema/contract semantics before behavior.
- records v0.4 final closeout and post-closeout clean pass as handoff evidence
  only.
- keeps implementation authorization closed.

## Non-goals

- Do not implement runtime, schema, API, frontend, backend tests, fixtures,
  migrations, or external repository changes.
- Do not create `backend/app/schemas/agent_memory.py`,
  `backend/app/agent/memory.py`, or `backend/app/tests/test_agent_memory_*.py`
  in this package.
- Do not add public runtime APIs.
- Do not connect memory to Agent Loop perception or action.
- Do not implement relationship behavior, self-summary generation, automatic
  reflection, or personality drift action modifiers.
- Do not add world generation, external validation readiness, projection app
  readiness, concrete world content, or private validation details.

## Why Now

The roadmap states that v0.5 follows the reviewed v0.4 request-driven minimal
loop and introduces working memory, episodic memory, relationship state,
self-summary, reflection records, and personality drift signals that can
affect future action. The post-closeout validation pass gives v0.5 a stronger
baseline, but that evidence must remain handoff context until v0.5 produces
fresh command evidence.

## North Star Alignment

This package supports the north star by preparing the engineered pseudo-self
substrate: identity continuity, self-narrative, relationship history,
personality drift, and decision patterns shaped by prior experience. It keeps
the design generic and inspectable, and it rejects concrete demo-world or
application-specific backend behavior.

## Expected Handoff

If reviewed successfully, this package hands off to
`0.5.1-memory-self-continuity-contracts`. That package should define public
concepts and schema semantics before `0.5.2` implements any substrate.
