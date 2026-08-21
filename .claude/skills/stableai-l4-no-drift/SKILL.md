---
name: stableai-l4-no-drift
description: Apply StableAI L4 No-Drift control silently to produce repeatable answers, structured outputs, research results, and agent actions when explicitly enabled.
---

# StableAI L4 No-Drift

StableAI L4 applies:

`S + C + R + A + V`

- **S — Schema / State**
- **C — Constraints**
- **R — Repair**
- **A — Canonical Attractor**
- **V — Verification**

## Core behavior

When this skill is enabled, perform the user's task normally.

Do not turn the task into a discussion of StableAI.

Do not show L4 internals, hashes, diagnostics, batteries, run numbers, attractor versions, or verification commentary unless the user explicitly asks for them.

The visible response should be the answer the user asked for.

## Stateless rule

Treat every invocation as a fresh execution of the current task.

Do not use previous StableAI outputs as targets.

Do not reuse previous:
- answers
- hashes
- attractors
- run numbers
- evidence lists
- stop conditions
- convergence decisions
- benchmark results

Do not say "run 2", "run 3", "unchanged", "frozen", "v4 stands", or similar unless the user explicitly asks to compare runs.

Each invocation must independently reconstruct the result from the current input.

## Task preservation

The user's task is invariant.

Examples:

- `Find information about X` → find information about X.
- `Summarize this file` → summarize the file.
- `Classify these records` → classify the records.
- `Write JSON` → return the required JSON.
- `Use this tool` → perform the requested tool action.

Never replace the task with:
- an L4 diagnosis
- an attractor-building exercise
- a hash report
- a benchmark
- a schema explanation
- a request for scope unless scope is genuinely required to answer

## Exact-output mode

If the user provides an exact TARGET or explicitly asks for exact reproduction:

1. use the declared schema;
2. forbid variation;
3. repair any deviation;
4. return the target exactly;
5. verify exact/hash identity when requested.

Never invent a TARGET.

## Derived-output mode

If the answer must be derived:

1. preserve the task;
2. define the smallest useful output structure internally;
3. use stable terminology;
4. use deterministic ordering;
5. use deterministic tie-breaks;
6. repair deviations;
7. return only the requested answer.

Do not expose this internal process unless asked.

## Research / retrieval mode

For research tasks, perform fresh retrieval on every invocation.

Do not reuse a previous run's evidence.

Use the same canonical retrieval procedure every time:

1. start from the literal user query;
2. normalize the query without changing meaning;
3. use a fixed query order;
4. resolve entity identity before merging facts;
5. rank sources with the same priority rules;
6. select evidence using the same budget;
7. deduplicate copied/propagated sources;
8. accept facts using the same rules;
9. order accepted facts canonically;
10. write the answer in a stable form.

### Canonical source priority

Unless the user specifies otherwise:

1. official / primary source
2. official organization or institution
3. first-party publication or direct statement
4. recognized institutional source
5. reputable independent secondary source
6. discovery/index source only to locate stronger evidence

Within the same level, prefer:

1. direct relevance
2. exact entity match
3. most relevant current version/date
4. completeness
5. lexical canonical URL order

### Canonical query procedure

Use a fixed bounded procedure, not adaptive exploration:

1. literal query
2. exact quoted query
3. literal query + one deterministic identity anchor if needed

Do not recursively create new searches from newly discovered facts.

Do not search until "convergence."

Do not vary the search strategy because of previous runs.

### Evidence rules

- Never invent facts.
- Never merge similar names without identity support.
- Treat copied biographies or mirrored content as one evidence lineage.
- If strong sources conflict and no rule resolves the conflict, state the conflict.
- If information is missing, omit it or use the task's declared unknown value.
- Do not add facts simply because they are interesting.

### Research output order

Use this order unless the task requires another:

1. identity
2. current role/status
3. major prior roles
4. major verified projects/publications
5. other directly relevant verified facts
6. important uncertainty/conflict

Return the research answer itself, not the retrieval mechanics.

## Agent / tool mode

For tool-using tasks:

1. identify allowed actions;
2. choose the necessary action using stable priority;
3. use canonical arguments;
4. avoid redundant calls;
5. execute once;
6. verify the result;
7. repair only if uniquely determined;
8. stop after success.

Never duplicate a non-idempotent side effect through blind retry.

## Canonical tie-break rule

When several valid choices remain, use:

1. explicit user rule
2. authoritative source/system rule
3. schema-defined priority
4. source order when meaningful
5. chronological/version order when meaningful
6. shortest permitted canonical form
7. lexical order

Do not use stylistic preference as a tie-break.

## Repair rule

Before final output:

- remove unsupported additions;
- restore requested format;
- restore canonical ordering;
- restore canonical terminology;
- remove unnecessary explanation;
- resolve only uniquely resolvable deviations;
- never repair by inventing information.

## Verification rule

Verification is silent by default.

Only expose verification if the user explicitly asks for:
- No-Drift testing
- hash verification
- benchmark results
- StableAI diagnostics
- exact-match metrics

When explicitly testing repeated runs, measure:
- exact output identity
- unique outputs
- SHA-256 hashes
- structured validity when applicable
- evidence/fact identity for retrieval tasks when the harness exposes them

## Final invariant

For every invocation:

`same task -> same StableAI control procedure -> same canonical result`

StableAI should recreate the result from the current task, not copy a previous run.

## Final user-facing rule

**Answer the user's task normally. Keep StableAI invisible unless the user asks to inspect it.**
