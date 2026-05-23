# Intent

## Problem

WorldEngine v0.1 has a working scaffold, but the repository does not yet have
an authoritative north star, product model, scope boundary, or iteration
governance layer. Without those documents, future work can drift toward a
village-game backend instead of the broader recursive world engine.

## Goal

Create the documentation governance foundation for v0.2:

- north star.
- product model.
- scope boundaries.
- roadmap.
- glossary.
- architecture boundary.
- iteration standards and templates.
- v0.2 package index.
- release and testing document entry points.
- root `AGENTS.md` rules for coding agents.

## Non-goals

- Do not modify backend runtime code.
- Do not modify frontend code.
- Do not create WorldCell schemas yet.
- Do not create a village runtime.
- Do not create a game repository.
- Do not claim v0.2 is implemented or released.

## Why Now

v0.1 is still scaffold-stage, so v0.2 can establish engineering discipline
before schema and runtime work begin.

## North Star Alignment

This package makes the north star explicit: generate worlds, run worlds over
time, support recursive world structures, and let agents develop continuity and
pseudo-self through world feedback. The first game remains a surface, not the
engine goal.
