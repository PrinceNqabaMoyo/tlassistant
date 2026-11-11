"""Textbook PDF vs scraped .md inventory for the science trees.

Usage: python scripts/_pdf_inventory.py                # all science
       python scripts/_pdf_inventory.py "Life Sciences" 10
For each subject+grade: which chapter .md files exist, which textbook PDFs
exist, which PDF has no .md (content we can still mine), and whether that PDF
yields extractable text (pymupdf) or is a scanned image needing OCR.

PDF naming: Textbook_<Subject>_Gr<N>_<Chapter_Title>.pdf
"""
import sys, os, re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "curriculum_source_files")
AUTO = os.path.join(ROOT, "curriculum_docs_auto")
FOLDER = {"Life Sciences": "LifeSciences", "Natural Sciences": "NaturalSciences",
          "Physical Sciences": "PhysicalSciences"}
# NOTE: the Natural Sciences PDF prefix is singular 'NaturalScience' while the
# auto folder is plural 'NaturalSciences' - they are not interchangeable.
STEM = {"Life Sciences": "LifeSciences", "Natural Sciences": "NaturalScience",
        "Physical Sciences": "PhysicalSciences"}


def md_chapters(subject, grade):
    root = os.path.join(AUTO, f"{FOLDER[subject]}_Gr{grade}")
    out = {}
    for dp, _d, fns in os.walk(root):
        if os.path.basename(dp) == "images":
            continue
        term = None
        m = re.search(r"Term\s*(\d)", os.path.basename(dp), re.I)
        if m:
            term = int(m.group(1))
        for fn in fns:
            if fn.endswith(".md") and fn != "Syllabus.md":
                title = S._norm_name(os.path.splitext(fn)[0])
                out[title] = (term, os.path.relpath(os.path.join(dp, fn), AUTO).replace("\\", "/"))
    return out


def pdf_chapters(subject, grade):
    stem = STEM[subject]
    pat = re.compile(rf"^Textbook_{stem}_Gr{grade}_(.+)\.pdf$", re.I)
    out = {}
    for dp, _d, fns in os.walk(SRC):
        for fn in fns:
            m = pat.match(fn)
            if m:
                out[S._norm_name(m.group(1))] = os.path.join(dp, fn)
    return out


def probe_pdf(path):
    """(chars, pages, kind) using pymupdf; kind = text|thin|scanned."""
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            return None, None, "no-pymupdf"
    try:
        d = pymupdf.open(path)
    except Exception as e:
        return 0, 0, f"error:{type(e).__name__}"
    txt = "".join(p.get_text() for p in d)
    n = len(d)
    d.close()
    if len(txt) > 4000:
        return len(txt), n, "text"
    if len(txt) > 500:
        return len(txt), n, "thin"
    return len(txt), n, "scanned(OCR needed)"


def main():
    subject = sys.argv[1] if len(sys.argv) > 1 else None
    grade = sys.argv[2] if len(sys.argv) > 2 else None
    total = {"md": 0, "pdf": 0, "no_md": 0, "mineable": 0, "ocr": 0}
    for sub in ("Life Sciences", "Natural Sciences", "Physical Sciences"):
        if subject and sub != subject:
            continue
        for gr in (7, 8, 9, 10, 11, 12):
            if grade and str(gr) != str(grade):
                continue
            mds, pdfs = md_chapters(sub, gr), pdf_chapters(sub, gr)
            if not pdfs and not mds:
                continue
            missing = [t for t in pdfs if t not in mds]
            print(f"\n### {sub} Gr{gr}: .md chapters={len(mds)}  textbook PDFs={len(pdfs)}  "
                  f"PDF-without-.md={len(missing)}")
            for t in sorted(missing):
                chars, pages, kind = probe_pdf(pdfs[t])
                name = os.path.basename(pdfs[t])
                print(f"    MINABLE  {name[:70]}\n             chars={chars} pages={pages} -> {kind}")
                if kind == "text":
                    total["mineable"] += 1
                elif kind.startswith("scanned"):
                    total["ocr"] += 1
            total["md"] += len(mds); total["pdf"] += len(pdfs); total["no_md"] += len(missing)
    print("\n" + "=" * 72)
    print(f"chapters with .md={total['md']}  textbook PDFs={total['pdf']}  "
          f"PDFs lacking .md={total['no_md']}  of which text-mineable={total['mineable']}  "
          f"needing OCR={total['ocr']}")


if __name__ == "__main__":
    main()
