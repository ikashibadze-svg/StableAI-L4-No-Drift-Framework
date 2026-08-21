# Changelog

## 1.3.0 — Evidence Attractor update

- Replaced the frozen-evidence Retrieval Lock with the StableAI Evidence Attractor principle.
- Every research run now performs fresh independent retrieval from the same input.
- Added canonical query plans, deterministic disambiguation, fixed evidence budgets, deterministic source ranking, source-lineage deduplication, and deterministic fact acceptance.
- Added canonical evidence-set and fact-set hashing.
- Added multi-layer No-Drift metrics for query-plan, evidence, fact, and output identity.
- Explicitly forbids reusing prior-run URLs, evidence, facts, or answers to manufacture repeatability.
- Added `references/evidence-attractor.md` and `scripts/canonical_evidence.py`.
- Removed obsolete `references/retrieval-lock.md` and `scripts/freeze_manifest.py`.

## 1.2.0 — Retrieval Lock update (superseded by 1.3.0)

- Introduced a frozen evidence manifest approach for open-world retrieval.
- This approach is retained in history only and was superseded because StableAI No-Drift requires independent fresh runs to collapse to the same evidence attractor rather than reuse cached evidence.

## 1.1.0 — Universal execution update

- Renamed skill to `stableai-l4-no-drift`.
- Added task-preservation and silent-execution invariants.
- Prohibited invented targets and invented facts.
- Added exact, closed-derived, open-result, and agent/tool L4 modes.
- Added deterministic evidence, identity, conflict, missing-value, ordering, and tie-break rules.
- Added tool-call, side-effect, retry, and agent execution locks.
- Separated user-facing execution from explicit StableAI diagnostics.
- Added `references/execution.md`.

## 1.0.0 — 2026-08-21

- Rebranded public release as StableAI L4 No-Drift.
- Shortened Claude Skill frontmatter description for compatibility.
- Distinguished exact-attractor mode from derived-output canonicalization.
- Fixed benchmark logic so requested runs cannot silently shrink after transport failures.
- Added benchmark provenance guidance and reported-results metadata.
- Added commercial-use-protective community license, citation metadata, contribution, security, and changelog files.
- Added separate Claude Customize skill ZIP packaging guidance.
