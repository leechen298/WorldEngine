# Technical Design

## Primary Artifact

`release-candidate-summary.md` is the release-candidate bundle. It must not be
named or treated as final release notes.

## Sections

- status and claim boundary.
- completed child packages.
- evidence map.
- exclusions.
- unresolved findings.
- recommendation to final closeout.

## Consistency Checks

Use file-existence checks for all child reviews, `0.7.5` evidence matrix, and
`0.7.6` audit report.

Use scope guard to confirm no implementation files outside the reviewed v0.7
surface changed.

Use status searches to verify this package does not mark v0.7 final.

## Compatibility Rule

Release-candidate approval means the final closeout package may review and
mark final if its own checks pass. It is not itself final approval.
