"""Which exact sequences occur in the corpus, and are they LaTeX or markdown escapes?

'\%' is pymupdf4llm escaping a percent sign, not math. '\( \theta \)' IS LaTeX.
Cleaning them needs the distinction, so count per-pattern and show real samples.
"""
import sys, os, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S  # noqa: E402

PATTERNS = {
    "paren-math \\(...\\)": re.compile(r"\\\((.{1,80}?)\\\)"),
    "bracket-math \\[...\\]": re.compile(r"\\\[(.{1,80}?)\\\]"),
    "\\frac": re.compile(r"\\(?:text|display)style\s*\\frac|\\frac"),
    "greek/op names": re.compile(r"\\(?:alpha|beta|gamma|theta|mu|nu|pi|Delta|Omega|sin|cos|tan|log|ln)"),
    "\\times \\cdot \\pm \\approx": re.compile(r"\\(?:times|cdot|pm|approx|leq|geq|neq)"),
    "escaped %": re.compile(r"\\%"),
    "escaped _": re.compile(r"\\_"),
    "escaped #": re.compile(r"\\#"),
    "escaped *": re.compile(r"\\"),
    "subscript _{..}": re.compile(r"_\{[^}]{1,12}\}"),
    "superscript ^{..}": re.compile(r"\^\{[^}]{1,12}\}"),
    "\\text{ / \\mathrm{": re.compile(r"\\(?:text|mathrm|mathit|mathbf)\{"),
    "left/right": re.compile(r"\\(?:left|right)"),
}

counts = collections.Counter()
samples = collections.defaultdict(list)
files = collections.Counter()
scanned = 0
for dp, _d, fns in os.walk(S._AUTO_DIR):
    if os.path.basename(dp) == "images":
        continue
    for fn in fns:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(dp, fn)
        t = S._read_text(p) or ""
        scanned += 1
        hit = False
        for label, rx in PATTERNS.items():
            for m in rx.finditer(t):
                counts[label] += 1
                hit = True
                if len(samples[label]) < 4:
                    samples[label].append(
                        f"{os.path.relpath(p, S._AUTO_DIR)[:40]}: ...{t[max(0, m.start()-45):m.end()+35]}...")
        if hit:
            files[os.path.relpath(p, S._AUTO_DIR).split(os.sep)[0]] += 1

print(f"scanned {scanned} .md files\n")
print(f"{'pattern':28s} {'count':>8s}")
for label, n in counts.most_common():
    print(f"{label:28s} {n:8d}")
print("\n=== samples ===")
for label, _n in counts.most_common():
    print(f"\n--- {label} ---")
    for s in samples[label]:
        print("   ", s.replace("\n", " ")[:170])
