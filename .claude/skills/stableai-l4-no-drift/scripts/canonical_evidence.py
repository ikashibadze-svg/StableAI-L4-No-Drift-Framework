#!/usr/bin/env python3
"""Canonicalize StableAI evidence or fact JSON and compute SHA-256."""
import argparse, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("file")
ap.add_argument("--kind", choices=["evidence","facts","generic"], default="generic")
args = ap.parse_args()

obj = json.loads(Path(args.file).read_text(encoding="utf-8"))

def normalize_url(u):
    return u.strip()

if args.kind == "evidence" and isinstance(obj, dict):
    for s in obj.get("sources", []):
        if "canonical_url" in s:
            s["canonical_url"] = normalize_url(s["canonical_url"])

canonical = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

print(canonical)
print(f"{args.kind}_sha256={digest}")
