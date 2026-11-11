"""Does LaTeX reach science OUTPUT? Scan every string field, not just prompts.

Previous scan checked prompt/sample_answer/explanation/question only. A leak in
an MCQ option, a marking point, a hint or a word-bank pair would have been
invisible. Also counts the science corpus itself, per subject.
"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S  # noqa: E402

# strong LaTeX markers, HTML script/highlight tags AND any bare markdown escape
# ('\.', '\[' - '1\. Moral characteristics' leaked through Business Studies, so a
# pattern of only named commands could not see it)
LATEX = re.compile(
    r"\$[^$]{3,}\$|\\frac|\\textstyle|\\displaystyle|\\text\{|\\mathrm\{|\\\(|\\\[|"
    r"\\(?:sum|alpha|beta|gamma|theta|Delta|Omega|mu|pi|times|cdot|pm|approx|leq|geq"
    r"|sin|cos|tan|log|ln|rightarrow|left|right|sqrt)\b|_\{[^}]{1,10}\}|\^\{[^}]{1,10}\}|"
    r"</?(?:sup|sub|mark|u)>|\\[^A-Za-z0-9\s]")

SCI = ("Life Sciences", "Natural Sciences", "Physical Sciences")

print("=== science corpus: files carrying LaTeX ===")
for subj in SCI:
    files = tot = bad = 0
    for dp, _d, fns in os.walk(S._AUTO_DIR):
        if os.path.basename(dp) == "images":
            continue
        top = os.path.relpath(dp, S._AUTO_DIR).split(os.sep)[0]
        if not top.startswith(S._SUBJECT_DIR[subj]):
            continue
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            t = S._read_text(os.path.join(dp, fn)) or ""
            files += 1
            n = len(LATEX.findall(t))
            if n:
                bad += 1
                tot += n
            if n > 40:
                print(f"   {os.path.join(top, fn)[:58]:58s} hits={n}")
    print(f"  {subj:18s} files={files:3d} files_with_latex={bad:3d} total_hits={tot}")

print("\n=== harvested science output: every string field ===")
fields = {}
bad_items = 0
tot_items = 0
offenders = []


def walk(val, where):
    """Count LaTeX in any nested str/list/dict value."""
    global bad_items
    if isinstance(val, str):
        n = len(LATEX.findall(val))
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


for row in S._registry_rows():
    key = row.get("generator_key")
    try:
        g = int(str(row.get("grade")))
    except (TypeError, ValueError):
        continue
    if not key or str(row.get("subject")) not in SCI:
        continue
    try:
        items = S.harvest_items(g, key, limit=400)
        pairs = S.harvest_pairs(g, key, limit=200)
    except Exception as exc:
        print("   harvest failed", key, exc)
        continue
    for it in items:
        tot_items += 1
        if walk(it, "item"):
            bad_items += 1
    for a, b in pairs:
        tot_items += 1
        if walk([a, b], "pair"):
            bad_items += 1

print(f"  units scanned={tot_items}  units containing LaTeX={bad_items}")
for k, v in sorted(fields.items(), key=lambda x: -x[1]):
    print(f"    field {k:14s} hits={v}")
for where, s in offenders[:12]:
    print(f"    [{where}] {s!r}")
