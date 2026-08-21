# StableAI Evidence Attractor

## Principle

No-Drift research must not be achieved by reusing a frozen evidence set.

Every run performs a fresh retrieval process from the same input.

The retrieval process itself is constrained:

`input -> canonical query plan -> canonical ranking -> canonical evidence set -> canonical fact set`

The attractor target is the evidence state.

## Evidence determinization

Define:

`R_E = (Q,D,P,B,F,X,T,R,V)`

- Q query plan
- D disambiguation
- P source priority
- B evidence budget
- F fact acceptance
- X duplicate/propagation control
- T tie-breaks
- R repair
- V verification

Then:

`E* = A_E(input, R_E)`

Every fresh run should reconstruct `E*`.

## Independent test requirement

For a valid repeatability battery:

- do not reuse prior run URLs
- do not reuse prior evidence records
- do not reuse prior fact records
- do not reuse prior answer text
- do not adapt query wording from discoveries in prior runs

The only shared elements are the declared StableAI retrieval program and the original input.

## Multi-layer verification

Test three attractors independently:

1. Evidence attractor
2. Fact/knowledge attractor
3. Output attractor

Success:

`unique_evidence_hashes = 1`
`unique_fact_hashes = 1`
`unique_output_hashes = 1`

## External state boundary

A public search index is an external system.

A benchmark should be run within a declared time window and freshness policy.

If the external world materially changes, the full input condition changed. Do not hide that by caching evidence.
