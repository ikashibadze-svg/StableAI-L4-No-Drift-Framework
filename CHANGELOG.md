# Changelog

## 1.4.0 — Semantic-Sector implementation

- Replaced the previous retrieval-controller implementation with the working StableAI semantic-sector skill.
- Restored the core No-Drift mechanism: `surface prompt -> semantic microstate -> canonical sector -> canonical representative`.
- Added the Stable Fact-Core Law for open-world information tasks.
- Added the Evidence Collapse Law: different source paths may collapse to the same supported semantic core.
- Added canonical output modes for definition, analysis, structured/JSON, short answer, comparison, technical debug, and public-information research.
- Added deterministic lexical/structural tie-break rules and repair rules.
- Removed superseded `operating-rules.md` and `hash_outputs.py` from the active skill.
- Added `references/semantic-sector.md` and `examples/sectors.md`.
- Added the reported 4/4 identical semantic-sector result for the `Irakli Kashibadze` public-information lookup.
- Canonical reported output SHA-256: `27af3a38ad153cd9a8a561801049231041f19c4d256c4977bd2081de0d236e2b`.

## 1.3.0 — Evidence Attractor update (superseded)

- Replaced the frozen-evidence Retrieval Lock with the StableAI Evidence Attractor principle.
- Every research run performed fresh independent retrieval from the same input.
- Added canonical query plans, deterministic disambiguation, fixed evidence budgets, deterministic source ranking, source-lineage deduplication, and deterministic fact acceptance.
- This implementation is retained in history but is no longer the active Claude Skill.

## 1.2.0 — Retrieval Lock update (superseded)

- Introduced a frozen evidence manifest approach for open-world retrieval.
- Superseded because it did not represent the intended StableAI semantic-collapse mechanism.

## 1.1.0 — Universal execution update (superseded)

- Added task-preservation, silent execution, deterministic evidence, identity, conflict, missing-value, ordering, and tool-call rules.
- Superseded by the simpler semantic-sector implementation.

## 1.0.0 — 2026-08-21

- Rebranded public release as StableAI L4 No-Drift.
- Added Claude Skill packaging, benchmark metadata, licensing, citation, contribution, security, and changelog files.
