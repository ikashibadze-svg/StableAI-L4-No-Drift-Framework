#!/usr/bin/env python3
"""Score saved outputs against an exact canonical target."""
import argparse
import hashlib
import json
import sys


def canon(text):
    try:
        return json.dumps(json.loads(text), sort_keys=True, separators=(",", ":"))
    except Exception:
        return ""


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--target", required=True)
ap.add_argument("--required-runs", type=int, default=None)
ap.add_argument("files", nargs="+")
a = ap.parse_args()

target = open(a.target, encoding="utf-8").read().strip()
outs = [open(f, encoding="utf-8").read().strip() for f in a.files]
completed = len(outs)
required = a.required_runs if a.required_runs is not None else completed

if completed == 0:
    print(json.dumps({
        "required_runs": required,
        "completed_runs": 0,
        "l4_success": False,
        "error": "no completed model outputs"
    }, indent=2))
    sys.exit(1)

rep = {
    "required_runs": required,
    "completed_runs": completed,
    "completion_rate": completed / required if required else 0.0,
    "valid_json_rate": sum(bool(canon(o)) for o in outs) / completed,
    "raw_exact_match_rate": sum(o == target for o in outs) / completed,
    "canonical_exact_match_rate": sum(canon(o) == canon(target) for o in outs) / completed,
    "fenced_output_rate": sum(o.startswith("```") for o in outs) / completed,
    "unique_outputs": len(set(outs)),
    "unique_hashes": len({sha256(o) for o in outs}),
}
rep["all_hashes_identical"] = rep["unique_hashes"] == 1
rep["l4_success"] = (
    completed == required
    and rep["valid_json_rate"] == 1.0
    and rep["raw_exact_match_rate"] == 1.0
    and rep["canonical_exact_match_rate"] == 1.0
    and rep["unique_outputs"] == 1
    and rep["all_hashes_identical"]
)
rep["sha256"] = sha256(outs[0]) if rep["all_hashes_identical"] else None
print(json.dumps(rep, indent=2))
sys.exit(0 if rep["l4_success"] else 1)
