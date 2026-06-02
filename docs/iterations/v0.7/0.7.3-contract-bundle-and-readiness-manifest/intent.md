# Intent

## Problem / Purpose

v0.7 now has reviewed public readiness contracts and a redacted validation
report checker, but an external validation suite still has to know which
contract files, schemas, report formats, and evidence classifications belong
to the public v0.7 readiness surface.

This package creates a generic readiness manifest so external consumers can
discover public WorldEngine surfaces without reading private chat context,
internal repository structure, or consumer-specific fixture details.

## Why Now

`0.7.2` completed machine-checkable redacted report semantics. The next stable
boundary is a public manifest that references those semantics and the reviewed
contract surfaces for later projection-consumer work.

## Relationship To Roadmap

This package implements the v0.7 roadmap step for contract bundle and
readiness manifest discovery. It remains generic and public. It does not
build projection read models, external validation suites, product apps, or
runtime features.

## Non-Goals

- Do not run an external validation suite.
- Do not implement projection read models or APIs.
- Do not add private suite configuration, private paths, UI selectors, oracle
  internals, transcripts, event payloads, concrete worlds, seed data, or
  consumer-specific examples.
- Do not modify runtime, API, frontend, persistence, migrations, generation,
  Agent loop, memory, or event behavior.
- Do not claim product readiness, projection readiness, external suite PASS,
  or release readiness.

## Expected Handoff

After closeout, `0.7.4-projection-consumer-read-model-contracts` receives a
reviewed public manifest and checker evidence that identify the public
contract surfaces and readiness classifications that projection read-model
contracts may reference.
