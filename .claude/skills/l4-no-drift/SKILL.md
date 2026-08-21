---
name: l4-no-drift
description: StableAI L4 constrains fixed or closed-output LLM tasks with schema, repair, canonical attractors, and exact/hash verification to minimize output drift.
---

# StableAI L4 No-Drift

Use this skill to design and test constrained LLM outputs using the StableAI L4 control program:

`p = (S, C, R, A, V)`

- **S — Schema:** allowed output form
- **C — Constraints:** variation that is forbidden
- **R — Repair:** instructions that project mechanical deviations back into the allowed form
- **A — Attractor:** exact canonical target, or a closed canonical output space with deterministic selection rules
- **V — Verification:** external exact-match, schema, and SHA-256 checks

## 1. Diagnose the task

Classify it before applying L4:

- **Exact target already known** → use exact-attractor L4.
- **Output derived from input but values are closed/constrained** → use canonical schema + closed vocabulary + ordered rules + tie-breaks, then verify repeated runs per input.
- **Free-form generation is required** → L4 cannot guarantee byte identity without first defining a canonical target or sufficiently closed output space.
- **Only token reduction is needed** → L2/L3 may be sufficient.

Do not claim deterministic or no-drift behavior merely because a prompt contains L4 instructions. Verification is required.

## 2. Exact-attractor L4

For a fixed known target, use `assets/l4-prompt-template.txt`.

### S — Schema

Return exactly the declared target representation.

### C — Constraints

Use these defaults unless the caller supplies stricter rules:

```text
No markdown. No explanation. No code fences. No extra text.
No paraphrase. No synonyms. No added keys. No removed keys.
No key reorder. No punctuation changes. No case changes. No value changes.
```

### R — Repair

```text
Before final output, compare the candidate with TARGET.
If any key, value, order, case, comma, quote, whitespace, or punctuation differs, repair it.
If any text exists before or after TARGET, remove it.
```

### A — Attractor

TARGET is the only allowed survivor.

### V — Verification

Prefer external measurement. For N repeated calls, report:

- attempted_runs
- completed_runs
- transport_errors
- valid_json_rate
- raw_exact_match_rate
- canonical_exact_match_rate
- unique_outputs
- unique_hashes
- all_hashes_identical
- SHA-256
- average input/output tokens when available
- average latency when available
- model/runtime/system-prompt metadata

For a required N-run battery, success requires all N runs to complete and all N outputs to pass the declared acceptance checks.

## 3. Derived-output L4

When TARGET is not known in advance, do **not** pretend that copying an attractor solves semantic choice.

Instead define:

1. fixed output schema,
2. allowed value vocabularies,
3. ordered decision/extraction rules,
4. explicit default/failure value,
5. deterministic tie-break rules,
6. canonical serialization,
7. external validator.

Operational target:

`same input + same evidence + same runtime conditions -> same canonical output`

This is an empirical repeatability target, not a mathematical guarantee about every stochastic model execution.

## 4. Verification discipline

Never report `L4 SUCCESS` from fewer completed runs than the requested battery size.

Transport failures are not semantic drift, but they must remain visible:

```text
attempted_runs = N
completed_runs = N - transport_errors
```

A strict battery passes only if:

```text
completed_runs == attempted_runs
AND valid_json_rate == 1.0        # when JSON is required
AND raw_exact_match_rate == 1.0   # exact-attractor mode
AND unique_outputs == 1
AND unique_hashes == 1
```

Test under the same model, system prompt, tool configuration, and runtime conditions used in production. Differences in harness behavior can change results.

## 5. Compression

After the full prompt passes, a shorter form may be tested:

```text
Return ONLY valid JSON. Copy TARGET exactly.
No markdown, code fences, explanation, paraphrase, synonym, key, case, order, whitespace, or punctuation change.
Verify exact match; if different, repair.
TARGET is the only allowed output.
```

A compressed prompt is an optimization only if it independently re-passes the battery.

## 6. Claims and terminology

Use precise language:

- Say **"SHA-256 verifies byte identity"**, not "SHA-256 makes the model deterministic."
- Say **"no observed drift across N repeated runs"** unless stronger evidence is available.
- Treat the formal relations in `references/theory.md` as StableAI operational hypotheses/principles unless separately proven under explicit mathematical assumptions.
- Exact-attractor L4 constrains wording because the wording is already defined; derived-output tasks require additional deterministic decision structure.

## Resources

- `references/levels.md` — L0–L4 control ladder.
- `references/theory.md` — formal/operational formulation and boundaries.
- `assets/l4-prompt-template.txt` — full and compressed exact-attractor templates.
- `scripts/verify_nodrift.py` — API battery.
- `scripts/run_battery.sh` — Claude Code CLI battery.
- `scripts/hash_outputs.py` — offline scorer.

## Final rule

Constrain first, verify second, claim only what the measured evidence supports.
