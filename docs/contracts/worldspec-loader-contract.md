# WorldSpec Loader Contract

Status: review complete

## Purpose

The WorldSpec loader is a data-boundary contract for v0.3. It defines how
generic `WorldSpec` input may be accepted, parsed, validated, and returned as
loaded data before any runtime bridge exists.

The loader is not a runtime world, not a `RuntimeEngine` adapter, not an API
route, and not a persistence layer.

## Public Concepts

- `WorldSpecLoader`: the future component responsible for turning supported
  generic input into either a loaded `WorldSpec` result or structured loader
  errors.
- `WorldSpecInput`: a supported input source containing one candidate
  `WorldSpec` payload.
- `LoadedWorldSpec`: a successful loader result containing a validated
  `WorldSpec` plus neutral source metadata.
- `WorldSpecLoaderError`: a structured failure entry describing why an input
  was not loaded.
- `WorldSpecLoaderResult`: the loader outcome. It is either successful loaded
  data or a failed result with one or more structured errors.

## Accepted Inputs

The future loader may accept these domain-neutral input forms:

- a parsed mapping object, such as a Python dictionary.
- a JSON string or bytes payload.
- a file path to a JSON document, if the implementation package explicitly
  includes file-backed loading.

All accepted inputs must contain a single candidate `WorldSpec` object. The
loader must not accept bundles, directories, generated-world prompts, external
fixture repositories, database records, API requests, or product-specific
payloads in this contract.

## Successful Output

A successful `LoadedWorldSpec` must include:

- `worldspec`: the validated `WorldSpec` model or its reviewed equivalent.
- `source_type`: one of the supported input categories, such as `mapping`,
  `json`, or `file`.
- `source_label`: optional neutral source text for diagnostics. For file input,
  this may be a path supplied by the caller. It must not carry domain meaning.
- `schema_version`: the validated `WorldSpec.schema_version`.

A successful result must not:

- start or mutate `RuntimeEngine`.
- write events.
- write persistence records.
- create archive snapshots.
- apply world params.
- register API routes.
- derive runtime context.

Loaded data remains specification data until a later reviewed runtime bridge
package defines how any subset may reach runtime context.

## Error Model

The loader must report failures using structured errors. Each error must carry:

- `code`: stable machine-readable error code.
- `message`: concise human-readable diagnostic.
- `path`: optional location within the input, using a deterministic path style
  chosen by the implementation package.
- `source_type`: input category when known.
- `source_label`: optional neutral source text when available.

Required error categories:

- `unsupported_input`: the input type or source is outside this contract.
- `parse_error`: the input was meant to be JSON or file-backed JSON but could
  not be parsed.
- `schema_validation_error`: parsed data failed the `WorldSpec`, `WorldCell`,
  or `EntityRef` schema contracts.
- `io_error`: file-backed input could not be read, if file-backed input is
  implemented.

Schema validation errors may be aggregated. The implementation must preserve
enough detail for tests to assert the failing field or path without depending
on framework-private exception formatting.

## Validation Semantics

The loader must validate through the existing `WorldSpec` schema contract in
`backend/app/schemas/world_cell.py` or a reviewed wrapper around it. It must
not reimplement schema rules with ad hoc string or dictionary checks except
for input dispatch, parsing, and error normalization.

The loader must preserve existing schema behavior:

- valid `schema_version = "0.2"` payloads with a valid root remain valid.
- omitted `schema_version` uses the existing `WorldSpec` default.
- unsupported schema versions remain invalid.
- invalid nested `WorldCell` or `EntityRef` data remains invalid.
- metadata is not interpreted by the loader.

## Domain-Neutral Example Policy

Documentation and tests for this contract may use only abstract identifiers,
such as:

- `worldspec-example`
- `cell-root`
- `entity-001`

They must not introduce concrete demo-world names, maps, characters,
locations, resources, story rules, external validation-world data, private
oracle details, product UI selectors, or application-specific backend logic.

## Compatibility Constraints

- Runtime behavior must remain unchanged by this contract.
- API response shapes must remain unchanged by this contract.
- Event contracts must remain unchanged by this contract.
- Archive, params, frontend-facing behavior, and legacy
  `backend/worldengine/` behavior must remain unchanged by this contract.
- Schema compatibility remains additive unless a later reviewed package
  explicitly allows a breaking change.

## Forbidden Inferences

This contract does not authorize:

- loader implementation in this documentation-only package.
- runtime bridge implementation.
- `RuntimeEngine` imports from the loader.
- API route registration.
- persistence or archive writes.
- event emission.
- world generation.
- Agent-in-World loop, memory, self-continuity, or projection behavior.
- external fixture repositories.
- concrete validation-world fixtures.

## Handoff

After this contract is reviewed, `0.3.2-worldspec-loader-implementation` may
implement the minimal loader against this contract and must provide focused
loader tests plus scope and compatibility evidence.
