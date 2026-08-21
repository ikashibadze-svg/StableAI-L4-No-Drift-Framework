# Changelog

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
