#!/usr/bin/env python3
"""Readability gate for entity profiles (Flesch-Kincaid grade level, 8–10 target).

Scans every researched profile's reader-facing prose (body after the '---' frontmatter,
machine blocks stripped) and reports the Flesch-Kincaid grade level. Exit 1 if any
researched profile reads above grade 10 (the user's 8–10th-grade writing standard).

Usage: python3 scripts/check_readability.py [--max-grade 10]
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import REPO

PROFILES = os.path.join(REPO, "profiles")
MAX_GRADE = 10
if "--max-grade" in sys.argv:
    MAX_GRADE = int(sys.argv[sys.argv.index("--max-grade") + 1])

def syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    n = len(groups)
    if word.endswith("e") and n > 1 and not word.endswith(("le","ce","ge","be","de","ke","me","ne","pe","se","te","ve","ze")):
        n -= 1
    if word.endswith("es") and n > 1:
        n -= 1
    if word.endswith("ed") and n > 1:
        n -= 1
    return max(n, 1)

def fk_grade(text):
    # strip markdown artifacts, tables, URLs, machine syntax
    text = re.sub(r"\|.*\|", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[#*`>\[\]()]", " ", text)
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"edge:\s*source=", " ", text)
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if len(s.strip().split()) > 3]
    words = [w for s in sentences for w in s.split()]
    if not sentences or not words:
        return None
    asl = len(words) / len(sentences)
    asw = sum(syllables(w) for w in words) / len(words)
    return 0.39 * asl + 11.8 * asw - 15.59

def main():
    # optional: python3 check_readability.py <file.md> [<file.md> ...] scores only those
    only = [a for a in sys.argv[1:] if a.endswith(".md") and a not in ("--max-grade",)]
    bad = []
    grades = []
    files = only or sorted(f for f in os.listdir(PROFILES) if f.endswith(".md") and f != "README.md")
    for fname in files:
        path = fname if (os.path.isabs(fname) or os.path.exists(fname)) else os.path.join(PROFILES, fname)
        if not os.path.exists(path):
            print(f"missing: {fname}"); continue
        txt = open(path, encoding="utf-8").read()
        if "✅ researched" not in txt:
            continue
        body = txt.split("\n---\n", 1)[1] if "\n---\n" in txt else txt
        body = re.split(r"\n#{1,2}\s*[^\n]*(?:New relationships|relationships to record)", body)[0]
        g = fk_grade(body)
        if g is None:
            continue
        grades.append(g)
        tag = "PASS" if g <= MAX_GRADE else "FAIL"
        print(f"  {tag} {fname}: grade {g:.1f} (target ≤{MAX_GRADE})")
        if g > MAX_GRADE:
            bad.append(f"{fname}: grade {g:.1f}")

    if grades:
        avg = sum(grades) / len(grades)
        print(f"profiles scored: {len(grades)} | mean FK grade: {avg:.1f} | target: ≤{MAX_GRADE}")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
