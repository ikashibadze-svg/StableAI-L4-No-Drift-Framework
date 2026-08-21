#!/usr/bin/env python3
"""Canonicalize and hash a StableAI evidence manifest."""
import argparse, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("manifest")
args = ap.parse_args()

obj = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
canonical = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

print(canonical)
print("evidence_sha256=" + digest)
