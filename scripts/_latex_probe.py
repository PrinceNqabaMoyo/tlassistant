"""How much LaTeX is leaking, and from where?

pymupdf4llm has a latex_on/latex_off switch: by default it replaces math spans
with LaTeX ('\\( \\sin { \\theta } \\)', '\\textstyle { \\frac { V } { R } }').
That is fine inside a Mathematics generator (KaTeX) and useless in a scraped
Life Sciences sentence. Measure (a) the 6 re-scraped chapters, (b) the existing
auto .md corpus, (c) what students actually see: harvested items.
"""
import sys, os, re, inspect
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S  # noqa: E402

try:
    import pymupdf4llm
    sig = inspect.signature(pymupdf4llm.to_markdown)
    print("to_markdown params:", [p for p in sig.parameters])
except Exception as exc:
    print("inspect failed:", exc)

LEAK = re.compile(
    r"\\\(|\\\[|\\frac|\\textstyle|\\displaystyle|\\left|\\right|\\sin|\\cos|"
    r"\\tan|\\Delta|\\alpha|\\beta|\\gamma|\\theta|\\mu|\\nu|\\pi\b|\\times|"
    r"\\cdot|\\approx|\\pm|\\%|\\circ|\\rightarrow|\\text\{|\\mathrm|\{_|\^\{")


def tally(label, text):
    hits = LEAK.findall(text)
    lines = [ln for ln in text.splitlines() if LEAK.search(ln)]
    print(f"  {label:34s} leaks={len(hits):5d} lines={len(lines):4d} chars={len(text):7d}")
    return lines


print("\n=== (a) the 6 re-scraped chapters ===")
mined = []
for dp, _d, fns in os.walk(S._AUTO_DIR):
    for fn in fns:
        if fn.startswith("PDF - "):
            p = os.path.join(dp, fn)
            mined.append(p)
            tally(os.path.relpath(p, S._AUTO_DIR)[:34], S._read_text(p) or "")

print("\n=== (b) existing auto .md corpus (all chapters, sampled by subject) ===")
by_subj = {}
for dp, _d, fns in os.walk(S._AUTO_DIR):
    if os.path.basename(dp) == "images":
        continue
    for fn in fns:
        if not fn.endswith(".md") or fn.startswith("PDF - ") or fn == "Syllabus.md":
            continue
        parts = dp.replace(S._AUTO_DIR, "").strip("\\/").split(os.sep)[0]
        by_subj.setdefault(parts, []).append(os.path.join(dp, fn))
tot_files = tot_leak = 0
for subj in sorted(by_subj):
    files = by_subj[subj]
    n = leak = 0
    for p in files:
        t = S._read_text(p) or ""
        c = len(LEAK.findall(t))
        n += 1
        leak += 1 if c else 0
    tot_files += n
    tot_leak += leak
    print(f"  {subj:26s} files={n:4d} files_with_latex={leak:4d}")
print(f"  TOTAL {tot_files} files, {tot_leak} contain LaTeX escapes")

print("\n=== (c) what a learner sees: harvested items ===")
bad = 0
tot = 0
for row in S._registry_rows():
    key = row.get("generator_key")
    try:
        g = int(str(row.get("grade")))
    except ValueError:
        continue
    if not key or g not in (7, 8, 9, 10, 11, 12):
        continue
    if str(row.get("subject")) not in ("Life Sciences", "Natural Sciences", "Physical Sciences"):
        continue
    try:
        items = S.harvest_items(g, key, limit=40)
    except Exception:
        continue
    for it in items:
        txt = " ".join(str(it.get(f, "")) for f in ("prompt", "sample_answer", "explanation", "question"))
        tot += 1
        if LEAK.search(txt):
            bad += 1
            if bad <= 6:
                print("   LEAK:", txt[:130])
print(f"  items scanned={tot}  items with LaTeX leak={bad}")
