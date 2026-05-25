# Intent

## Problem

v0.2 has completed several foundational packages, including boundary cleanup,
but active planning still points toward an immediate final closeout. That is
too early. The remaining work needs to be decomposed into small, reviewable
packages with clear boundaries before final release-candidate and closeout
work can happen.

Historical v0.2 iteration documents also contain concrete demo details from
superseded fixture direction. Those details are now risky for automation
because future agents may read all v0.2 iteration documents, not only active
direction docs.

## Goal

Create a documentation-only package that resets the remaining v0.2 sequence,
adds an automatic iteration workflow, provides a final-review-bundle template,
and abstracts historical concrete demo details while preserving historical
facts.

## Non-goals

- Do not implement runtime, schema, API, frontend, test, fixture, or external
  repository changes.
- Do not create package directories for 0.2.7 through 0.2.12.
- Do not declare v0.2 final release.
- Do not hide historical facts or pretend superseded fixture work did not
  happen.
- Do not restore concrete fixture direction as an active roadmap target.

## Why Now

0.2.5 removed active concrete external-world anchors and replaced fixture
tests with generic schema smoke coverage. The next step is to make the
remaining v0.2 work executable by automation without letting a future package
expand into loader, runtime bridge, agent loop, memory, generation, or product
UI work.

## North Star Alignment

This package supports the north star by keeping WorldEngine focused on a
generic recursive world engine. It strengthens the process that lets future
packages build schema, event, evidence, and compatibility foundations without
narrowing the repository into a demo-specific backend.
