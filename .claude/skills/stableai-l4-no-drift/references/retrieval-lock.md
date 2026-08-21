# StableAI Retrieval Lock

## Problem

A live search engine, web index, API, database, or external tool may return different evidence at different times.

If evidence changes, the model is not receiving the same complete input state.

StableAI therefore represents research as:

`R = (task, E, C)`

where `E` is the frozen canonical evidence manifest.

## No-Drift research condition

Two runs are comparable for output drift only if:

`task_1 = task_2`
`E_1 = E_2`
`C_1 = C_2`

Operationally:

`evidence_hash_1 = evidence_hash_2`

If evidence hashes differ, classify the difference as `EVIDENCE_CHANGE`, not output drift.

## Discovery

Discovery is allowed only when no manifest exists, the user asks for fresh/latest/current information, the declared freshness boundary has expired, or the user explicitly requests refresh.

Discovery is bounded and non-adaptive.

## Freeze

After discovery:

1. normalize source identifiers/URLs;
2. deduplicate evidence lineages;
3. record selected sources;
4. record content hashes when available;
5. record supported claims;
6. canonicalize the manifest;
7. compute the evidence hash;
8. freeze it.

## Repeat

A repeat run reuses the frozen manifest. It does not change query phrasing, search deeper, add/drop sources, search until convergence, or broaden scope.

## Refresh

A refresh is versioned:

`E1 -> E2`

The resulting answer is also versioned. This is knowledge/evidence evolution, not stochastic answer drift.

## Connection to Atomic Knowledge

For stronger persistence, convert the frozen evidence into canonical atomic knowledge records with provenance and use those records as `E`.

That moves StableAI retrieval from a live-search boundary to a deterministic knowledge-state boundary.
