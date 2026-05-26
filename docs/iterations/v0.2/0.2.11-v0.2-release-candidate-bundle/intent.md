# Intent

## Problem

v0.2 now has schema, event, boundary, evidence, and compatibility review
artifacts, but they are spread across package reviews, audit docs, release
drafts, and findings. Human / ChatGPT review needs one release-candidate
bundle that maps claims to evidence without promoting planned work into final
release status.

## Goal

Create a release-candidate evidence bundle that is ready for human / ChatGPT
review and clearly states:

- what v0.2 completed.
- what v0.2 intentionally did not implement.
- what evidence supports each release-candidate claim.
- what findings or limitations remain.
- why final closeout is deferred to 0.2.12.

## Non-goals

- Do not declare v0.2 final release.
- Do not close 0.2.12 work.
- Do not implement or modify runtime, schema, API, frontend, fixture,
  migration, or test behavior.
- Do not reroute v0.3 loader, bridge, agent, memory, generation, projection,
  or external validation work into v0.2.
- Do not add concrete external-world fixtures, seed data, roles, locations,
  resources, story rules, private validation internals, or product UI.

## Why Now

0.2.9 created the evidence index and boundary audit. 0.2.10 clarified legacy
and compatibility boundaries. The next milestone step is to assemble a
release-candidate bundle before final closeout, so reviewers can decide
whether v0.2 is ready to finalize or needs more evidence.

## North Star Alignment

This package supports the north star by making the recursive-world foundation
reviewable without narrowing WorldEngine into a concrete application backend.
It preserves the distinction between implemented v0.2 foundations and future
agent, memory, generation, projection, and runtime bridge milestones.
