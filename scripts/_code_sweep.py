"""What does the 'bare curriculum code' sweep in _clean() actually delete?

/(?<=\s)[A-Z]{2,4}\d[A-Z0-9]{0,3}\b/ was written for CAPS evidence tags, but it
fires on every ALL-CAPS formula too. Tally the real matches over the whole
science corpus so the fix is evidence-based, not a guessed whitelist.
"""
import sys, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO = os.path.join(ROOT, "curriculum_docs_auto")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_out_codes.txt")

CODE_RE = re.compile(r"(?<=\s)[A-Z]{2,4}\d[A-Z0-9]{0,3}\b")
# the ES-family codes the later, deliberately narrow rule already handles
ES_RE = re.compile(r"\bES[GB][BCDFGHJKLMNPQRSTVWXYZ0-9]{1,3}\b")

subj_dirs = [d for d in os.listdir(AUTO) if any(
    d.startswith(p) for p in ("LifeSciences", "NaturalSciences", "PhysicalSciences"))]
tally = Counter()
files = 0
for d in subj_dirs:
    for dp, _dirs, fns in os.walk(os.path.join(AUTO, d)):
        if os.path.basename(dp) == "images":
            continue
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            files += 1
            t = open(os.path.join(dp, fn), encoding="utf-8",
                     errors="replace").read()
            for m in CODE_RE.finditer(t):
                tally[m.group(0)] += 1

only_es = sum(v for k, v in tally.items() if ES_RE.fullmatch(k))
other = sum(v for k, v in tally.items() if not ES_RE.fullmatch(k))
lines = [f"science .md files scanned = {files}",
         f"code-sweep matches        = {sum(tally.values())} distinct {len(tally)}",
         f"  already caught by ES rule = {only_es}",
         f"  ONLY the code sweep       = {other}  <-- these are deleted by mistake",
         "",
         "top 45 tokens deleted by the code sweep:",
         f"{'token':12s} {'count':>7s} {'ES-covered':>11s}"]
for tok, n in tally.most_common(45):
    lines.append(f"{tok:12s} {n:7d} {'yes' if ES_RE.fullmatch(tok) else 'NO':>11s}")
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"report -> {os.path.basename(OUT)}")
