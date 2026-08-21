#!/usr/bin/env python3
"""StableAI L4 repeated-call verification battery for the Anthropic API."""
import argparse
import hashlib
import json
import statistics
import sys
import time


def canonicalize(text: str) -> str:
    try:
        return json.dumps(json.loads(text), sort_keys=True, separators=(",", ":"))
    except Exception:
        return ""


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def mean_or_none(values):
    return round(statistics.mean(values), 3) if values else None


def main() -> int:
    ap = argparse.ArgumentParser(description="StableAI L4 no-drift verification battery")
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--target-file", required=True)
    ap.add_argument("--runs", type=int, default=20)
    ap.add_argument("--model", required=True)
    ap.add_argument("--max-tokens", type=int, default=1024)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--system-prompt-file", default=None)
    ap.add_argument("--out", default="nodrift_report.json")
    args = ap.parse_args()

    if args.runs < 1:
        print("--runs must be >= 1", file=sys.stderr)
        return 2

    try:
        import anthropic
    except ImportError:
        print("Install dependency: pip install anthropic", file=sys.stderr)
        return 2

    prompt = open(args.prompt_file, encoding="utf-8").read()
    target_raw = open(args.target_file, encoding="utf-8").read().strip()
    target_canonical = canonicalize(target_raw)
    if not target_canonical:
        print("TARGET is not valid JSON", file=sys.stderr)
        return 2

    system_prompt = None
    if args.system_prompt_file:
        system_prompt = open(args.system_prompt_file, encoding="utf-8").read()

    client = anthropic.Anthropic()
    outputs, hashes, latencies = [], [], []
    in_toks, out_toks = [], []
    errors = []

    for i in range(args.runs):
        t0 = time.time()
        try:
            kwargs = dict(
                model=args.model,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            if system_prompt is not None:
                kwargs["system"] = system_prompt
            resp = client.messages.create(**kwargs)
            dt = time.time() - t0
            text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
            if not text:
                raise RuntimeError("empty text response")

            outputs.append(text)
            hashes.append(sha256(text))
            latencies.append(dt)
            in_toks.append(resp.usage.input_tokens)
            out_toks.append(resp.usage.output_tokens)
            print(f"run {i+1}/{args.runs}: completed {dt:.2f}s hash={hashes[-1][:12]} raw_match={text == target_raw}")
        except Exception as exc:
            errors.append({"run": i + 1, "type": type(exc).__name__, "message": str(exc)[:500]})
            print(f"run {i+1}/{args.runs}: ERROR {type(exc).__name__}: {exc}", file=sys.stderr)

    attempted = args.runs
    completed = len(outputs)
    valid_json = sum(bool(canonicalize(x)) for x in outputs)
    raw_match = sum(x == target_raw for x in outputs)
    canon_match = sum(canonicalize(x) == target_canonical for x in outputs)
    fenced = sum(x.startswith("```") for x in outputs)

    denom = completed if completed else 1
    unique_outputs = len(set(outputs))
    unique_hashes = len(set(hashes))
    all_hashes_identical = completed > 0 and unique_hashes == 1

    report = {
        "framework": "StableAI L4 No-Drift",
        "model": args.model,
        "attempted_runs": attempted,
        "completed_runs": completed,
        "transport_or_runtime_errors": attempted - completed,
        "completion_rate": completed / attempted,
        "valid_json_rate": valid_json / denom if completed else 0.0,
        "raw_exact_match_rate": raw_match / denom if completed else 0.0,
        "canonical_exact_match_rate": canon_match / denom if completed else 0.0,
        "fenced_output_rate": fenced / denom if completed else 0.0,
        "unique_outputs": unique_outputs,
        "unique_hashes": unique_hashes,
        "all_hashes_identical": all_hashes_identical,
        "avg_input_tokens": mean_or_none(in_toks),
        "avg_output_tokens": mean_or_none(out_toks),
        "avg_latency_seconds": mean_or_none(latencies),
        "system_prompt_mode": "file" if args.system_prompt_file else "none",
        "errors": errors,
    }
    report["l4_success"] = (
        completed == attempted
        and valid_json == attempted
        and raw_match == attempted
        and canon_match == attempted
        and unique_outputs == 1
        and unique_hashes == 1
    )
    report["sha256"] = hashes[0] if report["l4_success"] else None

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))
    print("\nL4 SUCCESS" if report["l4_success"] else "\nL4 FAILED")
    return 0 if report["l4_success"] else 1


if __name__ == "__main__":
    sys.exit(main())
