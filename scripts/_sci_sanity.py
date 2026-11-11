"""Cross-subject contamination audit of curriculum_docs_auto (science trees).

Usage: python scripts/_sci_sanity.py            # all science grades
       python scripts/_sci_sanity.py "Life Sciences" 11

The mypdf pipeline mis-filed at least one Business Studies chapter into
LifeSciences_Gr11/Term 4. BS harvesting already guards this with a keyword gate
(_looks_business); the science harvester had none. This reports, per file, the
home-subject score and the foreign-topic score so wrong-content files are found
before any question is generated from them.
"""
import sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO = os.path.join(ROOT, "curriculum_docs_auto")
# single source of truth: use the very gate the harvester applies
sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
from app.utils import sci_docs_harvester as S
HOME = S._HOME_WORDS


def count(text, words):
    return S._kw_count(text.lower(), words)


def main():
    want_sub = sys.argv[1] if len(sys.argv) > 1 else None
    want_gr = sys.argv[2] if len(sys.argv) > 2 else None
    bad = []
    for stem, subject in (("LifeSciences_Gr", "Life Sciences"),
                          ("NaturalSciences_Gr", "Natural Sciences"),
                          ("PhysicalSciences_Gr", "Physical Sciences")):
        for grade in (7, 8, 9, 10, 11, 12):
            if want_sub and want_sub != subject:
                continue
            if want_gr and str(want_gr) != str(grade):
                continue
            root = os.path.join(AUTO, f"{stem}{grade}")
            if not os.path.isdir(root):
                continue
            for dirpath, _d, fns in os.walk(root):
                if os.path.basename(dirpath) == "images":
                    continue
                for fn in fns:
                    if not fn.endswith(".md") or fn == "Syllabus.md":
                        continue
                    p = os.path.join(dirpath, fn)
                    raw = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ",
                                 open(p, encoding="utf-8", errors="replace").read())
                    home = count(raw, HOME[subject])
                    foreign = count(raw, S._FOREIGN_WORDS)
                    rel = os.path.relpath(p, AUTO).replace("\\", "/")
                    if S._wrong_subject(raw, subject):
                        print(f"WRONG CONTENT  {rel}")
                        print(f"    home={home:5d} foreign={foreign:5d}")
                        bad.append(rel)
                    elif home < 10:
                        print(f"THIN           {rel}  home={home} foreign={foreign}")
                        bad.append(rel + " (thin)")
    print("=" * 70)
    print(f"unusable science chapter files: {len(bad)}")
    for b in bad:
        print("  -", b)


if __name__ == "__main__":
    main()
