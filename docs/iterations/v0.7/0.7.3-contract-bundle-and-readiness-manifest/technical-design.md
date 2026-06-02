# Technical Design

## Current State

WorldEngine has reviewed public contract surfaces from `0.7.1` and a
machine-checkable external validation report schema/checker from `0.7.2`.
There is not yet a single public manifest that indexes those surfaces for
external consumers.

## Implementation Structure

Planned implementation files:

```text
docs/contracts/v0.7-readiness-manifest-schema.json
docs/contracts/v0.7-readiness-manifest.json
tools/testing/validate_readiness_manifest.py
tools/testing/test_validate_readiness_manifest.py
```

Package evidence files:

```text
docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/
```

## Manifest Shape

The manifest should be a JSON object with:

- `manifest_id`
- `manifest_version`
- `engine_reference`
- `generated_from`
- `contract_surfaces`
- `schema_surfaces`
- `template_surfaces`
- `capability_areas`
- `readiness_claim_values`
- `evidence_references`
- `compatibility_notes`
- `redaction_rules`

Surface entries should use repository-relative public paths and abstract ids.
The required manifest must include these public paths:

```text
docs/contracts/external-fixture-runner-contract.md
docs/contracts/external-validation-readiness-contract.md
docs/contracts/projection-consumer-contract.md
docs/testing/external-validation-report-schema.json
docs/validation-report-template.md
tools/testing/validate_external_validation_report.py
docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md
docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md
```

Evidence references in this package may classify evidence as `contract ready`,
`report format ready`, `blocked`, `skipped`, or `out of scope`. The manifest
may list broader reviewed taxonomy values in `readiness_claim_values`, but the
checker must reject `external suite pass`, `external consumer pass`, and
`core-side compatibility ready` as evidence reference statuses for this
package. A historical reference must be marked historical and must not be
treated as current v0.7 PASS evidence.

## Checker Flow

The checker should:

1. Load a JSON manifest file.
2. Validate that the top-level value is an object.
3. Validate required fields and simple field types.
4. Validate public repository-relative paths and reject absolute paths or
   parent traversal.
5. Validate required contract/schema/template references exist in the manifest.
6. Validate readiness claim values are from the reviewed taxonomy.
7. Validate evidence references include an allowed non-PASS status and public
   path or command.
8. Reject forbidden private-detail markers using synthetic sentinel coverage.
9. Print deterministic `FAIL:` lines or one deterministic `PASS:` line.

## Test Strategy

Focused tests should use in-memory manifest dictionaries and temporary JSON
files. They must use only abstract identifiers and synthetic sentinel strings.

Required cases:

- valid manifest passes.
- missing required field fails.
- manifest missing required contract/schema/template surface fails.
- unsupported readiness claim value fails.
- absolute path or parent traversal path fails.
- evidence reference without status fails.
- synthetic private-detail markers fail.
- CLI returns `0` for valid manifests and `1` for invalid manifests.

## Compatibility Strategy

- Keep implementation isolated to new manifest schema/checker/test files.
- Do not modify runtime/API/frontend behavior.
- Do not modify the `0.7.2` report checker except by running its focused
  tests as regression evidence if needed.
- Keep all identifiers generic and public.

## Anti-Drift Rules

- Parent and child status surfaces must agree before closeout.
- Implementation authorization must remain closed until evaluator approval.
- Manifest entries must not imply external suite PASS unless such evidence is
  explicitly present and in scope.
- Manifest paths must not point to private repositories, external fixture
  paths, or generated local artifacts.
