"""Syllabus-first coverage check (the sign-off instrument).

The per-topic harvest review can only talk about topics the REGISTRY already
has, so a syllabus topic that was never registered is invisible to it - that is
how LS Gr11 Term 4 went missing from my "complete" topic list. This script
makes the CAPS syllabus the authority and asks four stages per topic:

  1. syllabus  : topic named in caps-wiki/<subject>/grade-<n>/syllabus.md
  2. source    : a CLEAN chapter or chapter SECTION exists (.md, else textbook PDF)
  3. registry  : a generator_key is registered for it
  4. items     : harvest_items() actually returns questions, with a memo

Usage: python scripts/_syllabus_check.py "Life Sciences" 11
Writes UTF-8 detail to scripts/_out_syllabus_check.txt (console is cp1252).
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))

from _sci_coverage import syllabus_topics, registry_topics, related, SUBJECT_DIR  # noqa: E402
from app.utils import sci_docs_harvester as S  # noqa: E402

OUT = os.path.join(HERE, "_out_syllabus_check.txt")
WIKI = os.path.join(ROOT, "caps-ai-backend", "caps-wiki")
_AUTO_STEM = S._SUBJECT_DIR


def _md_files(subject, grade):
    """[(norm_title, rel, cleaned)] for every usable chapter .md of a grade."""
    root = os.path.join(S._AUTO_DIR, f"{_AUTO_STEM[subject]}{grade}")
    out = []
    if not os.path.isdir(root):
        return out
    for dp, _d, fns in os.walk(root):
        if os.path.basename(dp) == "images":
            continue
        for fn in fns:
            if not fn.endswith(".md") or fn == "Syllabus.md":
                continue
            p = os.path.join(dp, fn)
            raw = S._read_text(p)
            if not raw:
                continue
            cleaned = S._strip_images(raw)
            rel = os.path.relpath(p, S._AUTO_DIR).replace("\\", "/")
            out.append((S._norm_name(os.path.splitext(fn)[0]), rel, cleaned))
    return out


def _pdf_titles(subject, grade):
    return S._pdf_index().get((subject, grade), {}) or {}


def source_stage(name, subject, grade, md, pdfs):
    """('md chapter'|'md section'|'pdf chapter'|'pdf not mined'|'NONE', detail)."""
    t = S._norm_name(name)
    tset = frozenset(t.split())
    tg = [(t, tset)]
    for norm, rel, cleaned in md:
        if norm == t or (len(tset) >= 2 and (tset <= frozenset(norm.split())
                                             or frozenset(norm.split()) <= tset)):
            if len(cleaned) < 1200:
                continue
            if S._wrong_subject(cleaned, subject):
                return "CORRUPT .md", rel
            return "md chapter", rel
        if S._scope_to_headings(cleaned, tg) and not S._wrong_subject(cleaned, subject):
            return "md section", rel
    for norm, path in pdfs.items():
        if norm == t or (len(tset) >= 2 and (tset <= frozenset(norm.split())
                                             or frozenset(norm.split()) <= tset)):
            return "pdf chapter", os.path.basename(path)
    return "NONE", "-"


def main():
    subject = sys.argv[1] if len(sys.argv) > 1 else "Life Sciences"
    grade = sys.argv[2] if len(sys.argv) > 2 else "11"
    path = os.path.join(WIKI, SUBJECT_DIR[subject], f"grade-{grade}", "syllabus.md")
    syl = syllabus_topics(path)
    reg = registry_topics(subject, grade)
    md, pdfs = _md_files(subject, int(grade)), _pdf_titles(subject, int(grade))

    rows, buf = [], [f"{subject} Gr{grade}  syllabus={len(syl)} topics  "
                     f"registry={len(reg)} topics", ""]
    for term, name in sorted(syl, key=lambda x: (x[0] or 9, x[1])):
        hit = next((r for r in reg if related(name, r[1])), None)
        key = hit[2] if hit else None
        src, detail = source_stage(name, subject, int(grade), md, pdfs)
        n_items = n_memo = -1
        err = ""
        if key:
            try:
                items = S.harvest_items(int(grade), key, limit=220)
                n_items = len(items)
                n_memo = len([i for i in items if i.get("sample_answer") or i.get("marking_points")])
            except Exception as e:
                err = f"ERR {type(e).__name__}: {e}"
        rows.append((term, name, key, src, n_items, n_memo))
        buf.append(f"T{term}  {name}")
        buf.append(f"     registry : {key or 'MISSING - no generator'}")
        buf.append(f"     source   : {src}  ({detail})")
        buf.append(f"     items    : {n_items if n_items >= 0 else 'n/a'} "
                   f"with-memo {n_memo if n_memo >= 0 else ''} {err}")
        buf.append("")

    hdr = f"{'T':2s} {'SYLLABUS TOPIC':42s} {'SOURCE':14s} {'REGISTRY':34s} ITEMS"
    print(hdr)
    print("-" * len(hdr))
    bad = 0
    for term, name, key, src, n_items, n_memo in rows:
        ok = bool(key) and src.startswith(("md",)) and isinstance(n_items, int) and n_items > 0
        if not ok:
            bad += 1
        k = (key or "MISSING")[:34]
        it = n_items if isinstance(n_items, int) else 0
        print(f"T{term:<1d} {name[:42]:42s} {src:14s} {k:34s} {it:4d} {'' if ok else '<-- GAP'}")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(buf))
    print(f"\n{subject} Gr{grade}: {len(rows)} syllabus topics, {bad} NOT fully implemented")
    print(f"detail -> {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
