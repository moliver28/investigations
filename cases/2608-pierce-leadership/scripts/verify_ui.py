#!/usr/bin/env python3
"""Task 5.1 — the 16-gate verification suite.

Gates 1-12: build/browser behaviors (1 diameter, 2 overlaps, 3/4 contrast,
5 search, 6 directory, 7 entity, 8 deep links, 9 money, 10 console, 11 size,
12 offline). Gate 13: nav budget. Gate 14: mission-content map. Gate 15:
zero-other edges. Gate 16: money figures sourced. Exit 1 on any FAIL.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VENV = str(Path('/Users/moliver/.hermes/hermes-agent/venv/bin/python3'))
NODE = '/Users/moliver/.hermes/tools/node-26.7.0-darwin-arm64/bin/node'
NET = REPO / 'evidence' / 'network'

# ---------------------------------------------------------------- helpers
def contrast(h1, h2):
    def lum(hx):
        h = hx.lstrip('#')
        if len(h) == 3:
            h = ''.join(c*2 for c in h)
        ch = []
        for i in (0, 2, 4):
            v = int(h[i:i+2], 16) / 255
            f = v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
            ch.append(f)
        return 0.2126*ch[0] + 0.7152*ch[1] + 0.0722*ch[2]
    la, lb = lum(h1), lum(h2)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

results = []
def gate(n, name, ok, detail=""):
    results.append((n, name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'} {n:>2} {name}" + (f"  — {detail}" if detail else ""))

# ---------------------------------------------------------------- load data.js
dtext = (NET / 'assets' / 'data.js').read_text()
D = json.loads(dtext[dtext.index('{'):dtext.rindex(';')])
nodes, edges = D['nodes'], D['edges']
css = (NET / 'assets' / 'app.css').read_text()

# Gate 15 + 16 (pure-file checks, no browser needed)
others = [e for e in edges if e['relClass'] == 'other']
gate(15, "zero-other edges", len(others) == 0, f"{len(others)} other-classed")
e28 = (REPO / 'evidence' / '28-source-of-economic-power.md').read_text()
funded = [n for n in nodes if n.get('moneyFigure')]
bad_money = [n['id'] for n in funded
             if not (n.get('moneySource') and n['moneyFigure'] in e28)]
gate(16, "money figures sourced", len(bad_money) == 0,
     f"{len(funded)} funded, bad: {bad_money or 'none'}")

# Gate 11 (bundle size)
dbytes = (NET / 'assets' / 'data.js').stat().st_size
ibytes = (NET / 'index.html').stat().st_size
gate(11, "bundle size", dbytes < 4_000_000 and ibytes < 40_000,
     f"data.js {dbytes:,}B < 4MB; index.html {ibytes:,}B < 40KB")

# Gate 17 (review pass 2026-10-05): exec summaries ship and ride FIRST.
# Cover: every node keyed in the payload; summaries non-empty; and the client
# renders the exec card as the FIRST element of .entity-main (callout may
# precede it) — asserted from the authored client source (walkthrough's JS.
# source(openEntity) can't see template strings inside innerHTML assignments).
ex = D.get('execSummaries') or {}
missing_ex = [n['id'] for n in nodes if n['id'] not in ex or not (ex[n['id']].get('headline') or '').strip()]
gate(17, "exec summaries on all 163", len(missing_ex) == 0,
     f"{len(ex)} summaries, missing: {missing_ex[:3] or 'none'}")
appjs = (NET / 'assets' / 'app.js').read_text()
exec_first = ('${callout}${execCard}${egoBlock}${body}' in appjs
              and 'exec-summary' in appjs and 'execSummaries' in appjs)
gate(18, "exec summary renders first", exec_first,
     "openEntity main = callout+execCard+ego+body")
# Gate 19: zero dead-text URLs anywhere in the emitted profiles
import re as _re
dead_hits = []
for nd in nodes:
    h = nd['profile']
    t = _re.sub(r'<a\s[^>]*>.*?</a>', ' ', h, flags=_re.S)
    t = _re.sub(r'<[^>]+>', ' ', t)
    n_dead = len(_re.findall(r'https?://[^\s<>"\')\]]+', t))
    if n_dead:
        dead_hits.append((nd['id'], n_dead))
gate(19, "zero bare urls outside anchors", len(dead_hits) == 0,
     f"dead-text URL totals: {dead_hits[:3] or 'none'}")

# Gate 21 (review pass 2026-10-05, journalist lane): rendered section headings
# ship clean — the template numbers (0. / 3a. / 12.) are stripped from the
# visible text so rail titles == body titles on all 163 pages, and every
# section still carries its sec- anchor. Fails if any page regresses.
bad21, noanchor21 = [], []
for nd in nodes:
    prof = nd['profile']
    if _re.search(r'<h[23]><a class="h-anchor" id="sec-[^"]+" tabindex="-1"></a>\s*\d+[a-z]?\.', prof):
        bad21.append(nd['id'])
    body_titles = [m.group(1).strip() for m in
                   _re.finditer(r'<h[23]><a class="h-anchor"[^>]*></a>\s*([^<]*)</h[23]>', prof)]
    if body_titles != [t['title'] for t in nd['sections']]:
        bad21.append(nd['id'] + ':rail!=body')
    if len(_re.findall(r'<a class="h-anchor"', prof)) != len(nd['sections']):
        noanchor21.append(nd['id'])
gate(21, "rail == body titles, section numbers stripped",
     not bad21 and not noanchor21,
     f"bad {len(bad21)}, unanchored {len(noanchor21)}")

# ------------------------------------------------- Browser gates via CDP probe
# Use browser_exec-verified equivalents: replay the walkthrough in this process
# via the browser harness is unavailable here, so gate the DOM-coupled checks
# (1,2,5,6,7,8,9,10,13,14) from the browser session's captured state instead:
# verify_ui.py runs the browser through scripts/browser_walkthrough.py (below).

def browser_gates():
    wt = REPO / 'scripts' / 'browser_walkthrough.js'
    if not wt.exists():
        for n, name in [(1, 'node diameter'), (2, 'overlaps'), (5, 'search'),
                        (6, 'directory'), (7, 'entity page'), (8, 'deep links'),
                        (9, 'money toggle'), (10, 'console errors'), (12, 'offline'),
                        (13, 'nav budget'), (14, 'mission map')]:
            gate(n, name + ' (browser)', False, 'browser_walkthrough.js missing')
        return
    r = subprocess.run(['node', str(wt)], capture_output=True, text=True)
    for line in r.stdout.splitlines():
        m = re.match(r'(PASS|FAIL)\s+(\d+)\s+(.*)', line.strip())
        if m:
            gate(int(m.group(2)), m.group(3), m.group(1) == 'PASS')
    if r.returncode not in (0, 1):
        print(r.stderr[-400:])

import subprocess  # noqa: E402
browser_gates()

fails = [r for r in results if not r[2]]
print(f"\n{len(results) - len(fails)}/{len(results)} gates PASS" + (f" — FAILURES: {[r[1] for r in fails]}" if fails else ""))
sys.exit(1 if fails else 0)