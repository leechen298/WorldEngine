# Intent

## Problem / Purpose

v0.7 final closeout is historical evidence only. A later code review recorded
3 P1 and 2 P2 checker/schema blockers that prevent clean pass, external suite
PASS, projection readiness PASS, and product readiness PASS.

This package exists to repair those blockers narrowly and then rerun the
validation evidence needed to decide whether v0.7 can honestly move from
partial pass to clean pass.

## Why Now

The user asked to advance v0.7 to clean pass. Carrying unreliable readiness
checkers into v0.8 would weaken the public evidence boundary that v0.7 is meant
to establish.

## Relationship To Roadmap

v0.7 owns external validation readiness and projection consumer readiness
contracts. v0.8 owns the first external projection application. This repair
stays in v0.7 and does not implement v0.8.

## Non-Goals

- Do not build or validate a projection application.
- Do not run a private external suite or import external validation worlds.
- Do not implement runtime/API/frontend features.
- Do not run or claim full autonomous runner/full-suite PASS.
- Do not modify unrelated `docs/iterations/v0.8/**` worktree changes.

## Expected Handoff

If all V07-CR blockers are repaired and the validation matrix passes, this
package hands off a clean-pass v0.7 validation result and repaired checker
evidence to v0.8 planning. If blockers remain, it records partial pass or
failed evidence without overclaiming.
