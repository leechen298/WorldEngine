# Intent

## Problem

v0.7 readiness work can easily overclaim product readiness or leak private
external validation details. Before report schemas, checkers, readiness
manifests, projection payloads, or APIs are implemented, WorldEngine needs
reviewed public semantics for what external validation and projection consumer
readiness mean.

## Goal

Create a documentation-only contract package that defines readiness claim
taxonomy, redacted evidence requirements, projection consumer boundaries,
compatibility requirements, and authorization criteria for `0.7.2`.

## Why Now

`0.7.0` established campaign routing and external-consumer boundaries. The
next step is to make those boundaries concrete enough that later code-bearing
packages can implement schemas and checkers without inventing product-specific
or private validation semantics.

## Relationship To Roadmap

This package is the contract stage for v0.7. It prepares report schema and
redaction checker work in `0.7.2`, readiness manifest work in `0.7.3`, and
projection read-model work in `0.7.4` while keeping v0.8 projection
application work out of scope.

## Non-goals

- Do not implement report schemas or redaction checkers.
- Do not implement contract bundle or readiness manifest tooling.
- Do not implement projection read-model schemas or APIs.
- Do not run external validation suites.
- Do not claim runtime/API/frontend/E2E/Agent/autonomous/product/release
  readiness.
- Do not add concrete external-world or product-specific examples.

## Expected Handoff

`0.7.2-validation-report-schema-and-redaction-checker` receives the reviewed
redacted report semantics, readiness status values, forbidden leaked-detail
rules, and checker authorization criteria.

## North Star Alignment

This package protects the generic engine boundary by making external
validation suites and projection applications public consumers of WorldEngine
contracts. It does not turn WorldEngine into a validation app, projection app,
or product-specific backend.
