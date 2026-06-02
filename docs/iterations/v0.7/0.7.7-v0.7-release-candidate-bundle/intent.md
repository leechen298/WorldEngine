# Intent

## Problem

v0.7 has completed implementation, evidence, and audit packages. The final
closeout package should not start from scattered evidence. It needs a
reviewable release-candidate bundle that summarizes what is complete, what is
excluded, and what final closeout may claim.

## Desired Outcome

- Produce a release-candidate summary from reviewed evidence.
- Preserve exact exclusions for unrun runtime/API/frontend/live/external
  surfaces.
- Confirm no unresolved P1/P2 blocks final closeout.
- Hand off a bounded candidate to `0.7.8`.

## Non-Goals

- Do not mark v0.7 final.
- Do not run new validation suites.
- Do not change implementation files.
- Do not hide exclusions or unresolved findings.
