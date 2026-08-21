---
name: stableai-l4-no-drift
description: Use when StableAI L4, No-Drift, deterministic/canonical output, drift testing, exact reproduction, or constrained repeatable AI behavior is explicitly requested.
---

# StableAI L4 No-Drift

StableAI L4 is a deterministic control layer for constrained LLM output and agent behavior.

Core program:

`p = (S, C, R, A, V)`

- **S — State/Schema:** admissible states, output form, task contract
- **C — Constraints:** forbidden variation and forbidden actions
- **R — Repair:** deterministic projection of deviations back into the allowed state
- **A — Attractor:** canonical surviving output/action or a closed canonical state space
- **V — Verification:** exact, structural, provenance, or hash checks appropriate to the task

The operating objective is:

`same input + same evidence + same declared conditions -> same canonical result`

## 1. Activation gate

Apply this skill when at least one of these is true:

1. The user explicitly requests **StableAI**, **L4**, **No-Drift**, **deterministic output**, **canonical output**, **exact output**, **same hash**, or **drift testing**.
2. The user supplies a target and asks for exact reproduction or verification.
3. The user asks to transform a workflow, prompt, classifier, extractor, tool-using agent, or other process into a deterministic/canonical form.
4. The task is already running under StableAI L4 because the user enabled or selected this skill.

Do not activate merely because a task *could* be structured.

When this skill is active for an ordinary task, preserve the user's task and apply StableAI control silently unless diagnostics are explicitly requested.

## 2. Task-preservation invariant

**The user's objective is invariant.**

StableAI may constrain execution, retrieval, reasoning structure, serialization, or verification. It must not replace the requested task with a discussion of StableAI.

Examples:

- `Find information about X` remains a research task.
- `Summarize this file` remains a summarization task.
- `Classify these records` remains a classification task.
- `Use this API and update the record` remains the requested tool workflow.

Do not automatically replace such tasks with an attractor-building exercise, hash report, L4 diagnosis, benchmark battery, schema dump, or verification tutorial. Those are diagnostics, not substitutes for the requested output.

## 3. Silent StableAI mode

Default to **silent execution**.

Internally apply the relevant L4 controls, but return the user's requested result in the natural format they asked for.

Do not expose S/C/R/A/V commentary, attractor construction, internal state objects, hashes, battery commands, verifier filenames, retry logs, canonicalization traces, or source-ranking mechanics unless the user asks for StableAI internals, diagnostics, proof, benchmark results, or a machine-readable audit record.

StableAI should improve the task result, not dominate the conversation.

## 4. Never invent an attractor

Never manufacture a TARGET simply to convert a task into exact-attractor mode.

An exact TARGET may come only from the user, a previously accepted/verified canonical result, an explicitly authorized deterministic transformation whose output is uniquely defined, or a deterministic external system of record.

If no exact target exists, use **derived-output L4**. Do not fabricate facts, values, labels, biographies, citations, IDs, or canonical records merely to create a target.

## 5. Choose the correct L4 mode

### Mode A — Exact-attractor

Use when one exact target is already defined. `Y_allowed = {y*}`.

Return TARGET exactly; do not paraphrase or add text; preserve bytes/whitespace when byte identity is required; repair deviations back to TARGET; verify exact match and SHA-256 externally when requested/available.

### Mode B — Closed canonical derivation

Use when the answer must be derived but possible outputs can be closed by explicit rules. Define, in order: task contract, schema, allowed vocabulary, ordered decision/extraction rules, evidence requirements, deterministic tie-breaks, null/conflict/failure states, canonical serialization, validator.

### Mode C — Canonical open-result task

Use for research, summarization, retrieval, explanation, or other tasks where facts/content are not known beforehand and cannot honestly be reduced to a single predeclared target.

`task -> evidence -> facts -> ordering -> canonical expression -> repair -> verification -> answer`

Preserve factual truth and user intent above artificial byte identity. Use deterministic rules wherever the task permits them.

### Mode D — Agent/tool execution

Use for multi-step actions and tools.

`state -> allowed actions -> filter -> rank -> tie-break -> act -> verify -> repair/stop`

The same state, evidence, allowed tools, and constraints should select the same canonical next action.

## 6. Deterministic evidence policy

For evidence tasks, use caller-provided priorities first. Otherwise prefer: authoritative primary source/system of record; official organization/issuer; first-party publication/direct statement; recognized institutional/technical source; reputable secondary source; discovery/index source only to locate stronger evidence.

Within a tier, resolve choice deterministically by directness to the claim, date/version relevance, completeness, then canonical source identifier or lexical URL/order.

Do not silently convert weak evidence into strong facts.

## 7. Entity and identity control

Disambiguate people, organizations, products, records, and other confusable entities before merging facts. Require identity-bearing evidence appropriate to the domain. Do not merge same/similar names by assumption. If identity cannot be resolved, return the canonical unresolved state rather than guessing.

## 8. Conflict rule

When credible evidence conflicts, do not choose whichever wording appears first or seems preferable. Use the caller's conflict rule if supplied; otherwise preserve materially conflicting claims and mark the fact `CONFLICT`, `UNRESOLVED`, or the schema's equivalent. A deterministic system must be deterministic about uncertainty too.

## 9. Missing-information rule

Do not fill missing information with plausible values. Use one declared convention per task, such as `null`, `UNKNOWN`, `NOT_FOUND`, or `UNRESOLVED`.

## 10. Canonical ordering and tie-breaks

Where multiple valid representations remain, resolve using: explicit user rule; authoritative source/system rule; schema-defined priority; source order when meaningful; chronological/version order when meaningful; shortest permitted canonical representation; lexical order of canonical identifiers.

Do not use subjective preference as a tie-break.

## 11. Canonical expression

Separate knowledge selection from surface wording. First determine supported facts/decisions, then serialize through a stable expression policy.

For structured output: fixed key set/order/types/vocabulary, canonical null/failure tokens, no extra prose.

For user-facing prose: preserve requested tone/format, keep fact order deterministic, use stable terminology, avoid unnecessary synonyms when consistency matters, and keep StableAI machinery silent unless requested.

## 12. Repair operator

Repair is not free rewriting. Repair only toward a uniquely determined permitted state.

Repair categories include structural, lexical, provenance, identity, conflict, execution, and finalization violations. If the correct repair is not uniquely determined, move to the canonical unresolved/failure state instead of guessing.

## 13. Tool-call and agent lock

Before a tool call verify: `allowed AND available AND necessary AND arguments_complete AND not_redundant`.

Prefer existing evidence over new calls when it already satisfies the task.

For side effects: verify user intent, exact target and payload; execute once; verify observable result; never duplicate a non-idempotent side effect through blind retry.

Default action priority: terminate if success verified; verify existing result; use existing evidence; acquire only missing evidence; execute required tool; repair uniquely repairable failure; ask only for genuinely missing required input; fail canonically if completion is impossible.

## 14. Retry discipline

Retries are bounded. Default maximum same-action retries: 1. Default maximum total repair retries: 2. Classify failure before retrying. Do not confuse transport/tool failure with output drift.

## 15. Verification layers

Use verification appropriate to the task.

Exact target: byte equality, SHA-256 identity, exact match rate, unique outputs/hashes.

Structured derived output: parse/schema validity, key set/order, vocabulary, canonical serialization, evidence/provenance, repeated-run identity when benchmarked.

Research/evidence: claim-source support, entity identity, conflict handling, missing-value discipline, canonical fact ordering.

Agent/tool: allowed action, canonical arguments, observable success, no duplicate side effect, bounded retry, terminal-state correctness.

## 16. No-Drift certification

When the user explicitly asks to test/certify No-Drift, run/report the declared battery rather than merely asserting it.

For exact-target N-run strict success:

```text
attempted_runs = N
completed_runs = N
transport_errors = 0
raw_exact_match_rate = 1.0
unique_outputs = 1
unique_hashes = 1
all_hashes_identical = true
```

Add schema validity requirements when applicable. SHA-256 verifies byte identity; StableAI L4 supplies the control architecture.

## 17. Diagnostics mode

Expose StableAI diagnostics only when explicitly requested. Diagnostics may include selected mode, S/C/R/A/V contract, evidence policy, canonicalization rules, conflicts, hashes, battery metrics, and runtime metadata. Keep diagnostics separate from the primary task result unless the user asks for a combined report.

## 18. Low-token rule

Reduce unnecessary generation freedom and execution overhead without trading away correctness. Prefer compact schemas, closed vocabularies, reuse of evidence, fewer redundant tool calls, no repeated explanations, and immediate stop after verified success.

## 19. Invariants

```text
I1  user objective is preserved
I2  no invented target
I3  no invented fact
I4  ambiguity is explicit
I5  conflicts are handled deterministically
I6  evidence selection follows declared rules
I7  remaining choices use deterministic tie-breaks
I8  repair never guesses
I9  tool calls are necessary and non-redundant
I10 side effects are not duplicated
I11 verification matches the task type
I12 diagnostics stay silent unless requested
I13 verified success terminates execution
I14 final output follows the user's requested format
```

If an invariant is violated, repair before final output.

## 20. Final behavior

StableAI is a control layer, not the user's task.

Default execution:

`preserve intent -> constrain -> derive/act -> canonicalize -> repair -> verify -> answer`

Default user experience: **Return the requested answer. Keep StableAI machinery silent.**

When the user explicitly requests a No-Drift proof or benchmark: `answer/result -> verify -> report exact evidence and hashes`.

## Resources

- `references/levels.md` — L0–L4 control ladder.
- `references/theory.md` — physics-based and operational formulation.
- `references/execution.md` — derived-output, evidence, and agent control rules.
- `assets/l4-prompt-template.txt` — exact-attractor templates.
- `scripts/verify_nodrift.py` — Anthropic API battery.
- `scripts/run_battery.sh` — Claude Code CLI battery.
- `scripts/hash_outputs.py` — offline exact/hash scorer.
