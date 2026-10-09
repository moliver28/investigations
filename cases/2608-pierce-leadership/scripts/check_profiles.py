#!/usr/bin/env python3
"""Profile completeness gate. Exit 1 if any profile is below its tier minimums.

Checks per profile: tier parsed from header, sources table rows >= tier minimum,
no 'TODO' left in the tier's required sections, status flipped to researched.
Usage: python3 scripts/check_profiles.py
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import REPO  # noqa: F401  (REPO == investigation root)

PROFILES = os.path.join(REPO, "profiles")
MIN_SOURCES = {"tier1": 10, "tier2": 5, "tier3": 3}

def check(path):
    txt = open(path).read()
    m = re.search(r"\*\*Tier:\*\* (tier\d)", txt)
    tier = m.group(1) if m else None
    src_rows = len(re.findall(r"^\| \d+ \|", txt, re.MULTILINE))
    todos = len(re.findall(r"\[ \]|TODO", txt))
    status = "researched" if re.search(r"\*\*Status:\*\* ✅", txt) else "pending"
    ok = bool(tier) and src_rows >= MIN_SOURCES.get(tier, 999) and todos == 0 and status == "researched"
    # tier1 additionally requires an explicit confidence level (Stress Test finding #7, ICD 203)
    if tier == "tier1" and not re.search(r"\*\*Confidence:?\*?\*?\s* (High|Medium|Low)", txt):
        ok = False
    return tier, src_rows, todos, status, ok

def main():
    bad = []
    for fname in sorted(os.listdir(PROFILES)):
        if not fname.endswith(".md") or fname == "README.md":
            continue
        tier, src, todos, status, ok = check(os.path.join(PROFILES, fname))
        if not ok:
            bad.append(f"{fname}: tier={tier} src={src}/{MIN_SOURCES.get(tier,'?')} todos={todos} status={status}")
    print(f"profiles failing gate: {len(bad)}")
    for b in bad:
        print("  FAIL", b)
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()