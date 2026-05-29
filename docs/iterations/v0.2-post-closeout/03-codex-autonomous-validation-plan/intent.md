# Intent

Status: planned / ready for review

## Problem / Purpose

Post-closeout validation needs an independent Codex review line. A reviewer
that only restates implementation summaries does not provide enough evidence.

## Why Now

The autonomous validation instructions must exist before a separate Codex run
starts, so the reviewer knows what to read, what to run, what not to modify,
and how to report unsupported claims.

## Relationship To Roadmap

This validation supports later roadmap confidence. It does not implement
WorldEngine Agent-in-World behavior.

## Non-Goals

- Do not run autonomous validation in this package.
- Do not modify code.
- Do not accept unverified claims.
- Do not use private external validation details.

## Expected Handoff

`04-codex-autonomous-validation-execution/` uses this plan to run and verify
an independent Codex review.
