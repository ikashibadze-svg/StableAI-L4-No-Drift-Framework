# StableAI L4 — Formal and Operational Formulation

## 1. Generator model

Let an LLM/runtime be represented as a generator:

`G(p, e) -> y`

where `p` is the control prompt/program, `e` represents runtime/environment conditions, and `y` is the returned output.

StableAI L4 represents the control program as:

`p = (S, C, R, A, V)`

with schema, constraints, repair, attractor, and verification.

## 2. Exact-attractor principle

If A already specifies one exact byte string `y*`, S/C prohibit alternatives, and R instructs correction toward A, then the allowed textual output space is intentionally collapsed toward `y*`.

External verification V measures whether repeated calls actually returned `y*`.

Operational success for N runs:

```text
completed_runs = N
raw_exact_match_rate = 1.0
unique_outputs = 1
unique_hashes = 1
```

This is an empirical statement about the measured model/runtime configuration.

## 3. Distribution-collapse hypothesis

The idealized target can be written as:

`P(y | p, e) -> delta(y*)`

This expression should be read as a **StableAI operational convergence hypothesis/goal** unless a separate formal proof establishes the required assumptions for a specific stochastic generator and runtime.

## 4. Derived-output boundary

If the correct output must be discovered from input, an exact literal attractor is not known in advance. StableAI therefore reduces semantic degrees of freedom using:

- fixed schemas,
- closed vocabularies,
- ordered rules,
- deterministic tie-breaks,
- canonical serialization,
- explicit failure/default states,
- external validators.

Repeatability must then be tested per input or benchmark set.

## 5. Token-reduction principle

Constraining the allowed output generally reduces the amount of generated text needed to satisfy the contract. This can lower output-token usage and latency in tasks where the unconstrained baseline is substantially longer.

It does **not** imply that every constrained prompt has lower total token cost: additional input instructions can offset output savings, and runtime latency depends on more than output length.

## 6. Verification principle

SHA-256 provides a cryptographic fingerprint of bytes. Matching hashes for identical-length practical outputs are evidence of byte identity when paired with direct equality checks; the scripts in this repository perform direct exact matching as the primary test and report SHA-256 as an auditable fingerprint.

## 7. Practical law

```text
Reduce allowed output space.
Define canonical survivors.
Repair mechanically detectable deviations.
Verify externally.
Report the measured boundary honestly.
```
