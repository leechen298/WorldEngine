# Intent

Chinese mirror: `intent.zh.md`.

## Problem

v0.12 now has public Agent continuity surfaces and a Validation Client evidence
handoff contract. The MVP still needs an evidence-backed lifecycle
classification. The repository contains deterministic autonomous checker
fixtures, but a current fresh external Validation Client export may not exist.

## User Value

The user receives an honest classification: what checker evidence passed, what
fresh validation did or did not run, and whether the remaining MVP path is
PASS, PARTIAL, BLOCKED, or FAIL.

## Engineering Value

This package prevents historical saved results or UI smoke from being
misrepresented as a current v0.12 full lifecycle PASS. It also defines the
input to the final `0.12.6` closeout.

## Non-Goals

- No external Validation Client implementation.
- No product code changes.
- No provider live calls unless later explicitly authorized.
- No final MVP closeout.
