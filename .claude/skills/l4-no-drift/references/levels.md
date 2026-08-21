# StableAI No-Drift Control Levels (L0–L4)

## L0 — Free generation

No fixed output contract. High structural and lexical freedom.

## L1 — Structure lock

Adds headings or a schema. Formatting becomes more stable, but wording can still vary.

## L2 — Constraint lock

Adds constraints such as fixed labels, no extra prose, and shorter responses. Reduces output freedom but may leave synonyms or equivalent values open.

## L3 — Canonical style lock

Adds a canonical style/template and tighter lexical conventions. Often compresses output substantially, but byte identity must still be measured rather than assumed.

## L4 — Exact/canonical attractor lock

Adds a single exact target **or** a closed canonical output space with deterministic selection rules, plus repair and external verification.

For a known fixed target:

`L4 = schema + constraints + repair + exact attractor + verification`

For a derived output:

`L4 = schema + closed values + ordered rules + tie-breaks + repair + verification`

## Choosing a level

- Fixed known content, byte identity required → L4 exact-attractor.
- Derived content with a closed decision space → L4 canonical/derived mode.
- Stable structure but open wording → L2/L3.
- Free writing → L0/L1 unless a canonicalization layer is intentionally added.

## Verification language

Use "cryptographic verification of byte identity" for SHA-256 comparisons. Do not describe SHA-256 itself as a mechanism that guarantees model determinism.
