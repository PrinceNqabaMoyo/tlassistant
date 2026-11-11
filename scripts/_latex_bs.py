r"""Do LaTeX / HTML scrape artefacts reach Business Studies learner output?

Same technique as _latex_science.py (which found and now prevents the science
leaks): walk EVERY nested string of every harvested item and pair, not just the
prompt. The BS corpus is LaTeX-heavy too (Accounting_Gr10/Syllabus.md carries
'\frac{Gross\ Profit}{Sales} \times 100'), so the question is whether any of it
survives into a field a learner reads.
"""
import sys, os, re
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import bs_docs_harvester as B  # noqa: E402

LATEX = re.compile(
    r"\$[^$]{3,}\$|\\frac|\\textstyle|\\displaystyle|\\text\{|\\mathrm\{|\\\(|\\\[|"
    r"\\(?:sum|alpha|beta|gamma|theta|Delta|Omega|mu|pi|times|cdot|pm|approx|leq|geq"
    r"|sin|cos|tan|log|ln|rightarrow|left|right|sqrt)\b|_\{[^}]{1,10}\}|\^\{[^}]{1,10}\}|"
    r"</?(?:sup|sub|mark|u)>|\\[^A-Za-z0-9\s]")

BS = ("Business Studies",)

corpus = 0
for dp, _d, fns in os.walk(B._AUTO_DIR):
    if os.path.basename(dp) == "images":
        continue
    top = os.path.relpath(dp, B._AUTO_DIR).split(os.sep)[0]
    if not top.startswith("BusinessStudies"):
        continue
    for fn in fns:
        if fn.endswith(".md"):
            t = open(os.path.join(dp, fn), encoding="utf-8",
                     errors="replace").read()
            corpus += len(LATEX.findall(t))
print(f"Business Studies corpus LaTeX/HTML hits = {corpus}")

fields, bad, tot, offenders = {}, 0, 0, []
kinds = Counter()


def walk(val, where):
    global bad
    if isinstance(val, str):
        hits = LATEX.findall(val)
        n = len(hits)
        for h in hits:
            kinds[h if isinstance(h, str) else h[0]] += 1
        fields[where] = fields.get(where, 0) + n
        if n:
            offenders.append((where, val[:150]))
            return 1
        return 0
    if isinstance(val, dict):
        return sum(walk(v, k) for k, v in val.items())
    if isinstance(val, (list, tuple)):
        return sum(walk(v, where) for v in val)
    return 0


rows = B._registry_names()
keys = set()
for row in rows:
    key = row.get("generator_key")
    if not key or str(row.get("subject")) not in BS or key in keys:
        continue
    keys.add(key)
    try:
        g = int(str(row.get("grade")))
    except (TypeError, ValueError):
        continue
    items = B.harvest_items(g, key, limit=400)
    pairs = B.harvest_pairs(g, key, limit=200)
    for it in items:
        tot += 1
        bad += 1 if walk(it, "item") else 0
    for a, b in pairs:
        tot += 1
        bad += 1 if walk([a, b], "pair") else 0

print(f"keys scanned={len(keys)}  units scanned={tot}  units with LaTeX/HTML={bad}")
print("distinct markup found:", len(kinds))
for k, v in kinds.most_common(15):
    print(f"   {v:4d}  {k!r}")
for k, v in sorted(fields.items(), key=lambda x: -x[1]):
    print(f"  field {k:16s} hits={v}")
for where, s in offenders[:15]:
    print(f"  [{where}] {s!r}")
