# v0.13 Campaign Plan

Chinese mirror: `CAMPAIGN_PLAN.zh.md`.

Status: documentation preparation / active child 0.13.1

## Objective

Move from architecture discussion to one externally visible, independently
classifiable MVP without allowing current implementation details or a single
client technology to define WorldEngine.

## Authoritative Inputs

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/project-plan.md`
- `docs/roadmap.md`
- `docs/living-world-development-flow.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- the user-approved decisions recorded in the v0.13 package

Existing runtime code is an implementation inventory, not an authoritative
design input.

## Campaign Phases

### Phase 1: WorldEngine runnable anchor

Closed for the `0.13.0` package scope: the headless core, generic protocol,
administration console, and evidence bundle are verified without external
dependencies. This is not a clean full-repository or complete-v0.13 PASS.

### Phase 2: Godot executor and independent checker

Current phase is documentation preparation only. Prepare and review an
external milestone for a minimal Godot 2D executor and a separate checker
process in `WorldEngine-Validation-Client`. The concrete anchor world will live
only there after implementation is separately authorized.

### Phase 3: End-to-end acceptance

Run the same scenario through the administration console and Godot; correlate
WorldEngine evidence, Godot observations, and checker assertions; record a
current classification.

## Campaign Constraints

- One active package at a time.
- Documentation and evaluator gates precede implementation.
- No external repository writes from a WorldEngine-only active package.
- No live-provider requirement for the minimum pass path.
- No client self-certification.
- No concrete validation content in WorldEngine.
- No full MVP PASS before the external run exists.

## Exit Criteria

The campaign exits only when all package exit criteria in `v0.13-plan.md` are
met and `0.13.2` records the final evidence-backed classification.
