# Intent

## Problem / Purpose

E2E and API smoke validation checks execution behavior. This package defines a
separate independent Codex review line that checks whether the v0.3 release
claims are supported by docs, code, tests, and command evidence.

## Why Now

v0.3 loader and bridge claims are subtle. A reviewer must verify the contract
boundaries directly instead of trusting the implementation author's summary.

## Relationship To Roadmap

The review protects v0.4 planning from inheriting unsupported v0.3 claims. It
does not authorize v0.4 implementation.

## Non-Goals

- Run the autonomous review in this package.
- Modify code.
- Modify tests.
- Add fixtures or E2E coverage.
- Change release status.
- Create external repositories.

## Expected Handoff

`04-codex-autonomous-validation-execution` uses this plan and the review
template to conduct the independent review.
