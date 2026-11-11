"""Scrape textbook PDFs into the auto docs tree.

Why this is a build step and not a request-time path: the auto-scrape mis-filed
5 science chapters with another subject's text (so those topics harvest nothing)
and 1 chapter has no .md at all, while the SOURCE PDFs for those same chapters
are clean. pymupdf4llm takes seconds per chapter, so each needed chapter is
converted ONCE into a markdown file the harvester then reads like any other
chapter.

The engine is pymupdf4llm - the same one curriculum_docs/extract_pdf.py used -
because it emits '##'/'###' headings AND '| **term** | definition |' tables,
which is exactly what _blocks() and _TROW_RE parse. write_images is off: the
committed tree's images/*.md noise came from the original scrape turning every
figure into a file.

Usage: python scripts/mine_pdf_chapters.py               # everything, dry-run
       python scripts/mine_pdf_chapters.py --write       # actually write
       python scripts/mine_pdf_chapters.py "Life Sciences" 11 --write
"""
import sys, os, re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S  # noqa: E402

DRY = "--write" not in sys.argv
_args = [a for a in sys.argv[1:] if not a.startswith("-")]
ONLY_SUBJECT = _args[0] if _args else None
ONLY_GRADE = int(_args[1]) if len(_args) > 1 else None


def md_chapters(subject, grade):
    """{norm_title: (rel_path, is_usable)} for every scraped chapter .md.

    'usable' means long enough AND it passes the wrong-subject gate, so a
    chapter mis-scraped with another subject's text counts as needing a re-mine.
    """
    root = os.path.join(S._AUTO_DIR, f"{S._SUBJECT_DIR[subject]}{grade}")
    out = {}
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
            usable = len(cleaned) > 1200 and not S._wrong_subject(cleaned, subject)
            norm = S._norm_name(os.path.splitext(fn)[0])
            out.setdefault(norm, (os.path.relpath(p, S._AUTO_DIR).replace("\\", "/"), usable))
    return out


def scraped_term(subject, grade, norm_title):
    """Term folder the scrape used for this chapter, even if its text is corrupt."""
    root = os.path.join(S._AUTO_DIR, f"{S._SUBJECT_DIR[subject]}{grade}")
    for dp, _d, fns in os.walk(root):
        if os.path.basename(dp) == "images":
            continue
        for fn in fns:
            if fn.endswith(".md") and S._norm_name(os.path.splitext(fn)[0]) == norm_title:
                return S._dir_term(os.path.basename(dp))
    return None


def registry_term(subject, grade, norm_title):
    for e in S._registry_rows():
        if (str(e.get("subject")) == subject and str(e.get("grade")) == str(grade)
                and S._norm_name(str(e.get("name"))) == norm_title):
            try:
                return int(str(e.get("term")))
            except (TypeError, ValueError):
                pass
    return None


def main():
    written = skipped = 0
    for subject in ("Life Sciences", "Natural Sciences", "Physical Sciences"):
        if ONLY_SUBJECT and subject != ONLY_SUBJECT:
            continue
        for grade in (7, 8, 9, 10, 11, 12):
            if ONLY_GRADE and grade != ONLY_GRADE:
                continue
            mds = md_chapters(subject, grade)
            good = {k for k, (_rel, ok) in mds.items() if ok}
            pdfs = S._pdf_index().get((subject, grade), {}) or {}
            todo = []
            for norm, path in sorted(pdfs.items()):
                if norm in good:
                    continue
                # a scrape with the same title exists elsewhere but was rejected,
                # or there is no scrape at all: either way the PDF is the source
                todo.append((norm, path))
            if not todo:
                continue
            print(f"\n### {subject} Gr{grade}: {len(pdfs)} PDFs, "
                  f"{len(good)} usable .md chapters, {len(todo)} to mine")
            for norm, path in todo:
                title = os.path.splitext(os.path.basename(path))[0]
                title = title.split(f"_Gr{grade}_", 1)[1]
                title = title.replace("-", " ").replace("_", " ").strip()
                term = (scraped_term(subject, grade, norm)
                        or registry_term(subject, grade, norm) or 1)
                text = S._pdf_to_md(path)
                if not text:
                    print(f"    SKIP  {title[:52]:52s} no text (scanned PDF, needs OCR)")
                    skipped += 1
                    continue
                if S._wrong_subject(text, subject):
                    print(f"    SKIP  {title[:48]:48s} WRONG SUBJECT in the PDF itself")
                    skipped += 1
                    continue
                heads = len(re.findall(r"^#{2,6}\s", text, re.M))
                rows = len(re.findall(r"^\s*\|.*\|\s*$", text, re.M))
                dest = os.path.join(S._AUTO_DIR, f"{S._SUBJECT_DIR[subject]}{grade}",
                                    f"Term {term}", f"PDF - {title}.md")
                tag = "ok"
                if heads == 0 or len(text) < 1500:
                    tag = f"THIN heads={heads} chars={len(text)}"
                reason = (f"corrupt .md: {mds[norm][0]}" if norm in mds
                          else "no .md at all")
                print(f"    DO    {title[:48]:48s} T{term} chars={len(text):6d} "
                      f"heads={heads:3d} tables={rows:4d} [{reason}] {tag}")
                print(f"          -> {os.path.relpath(dest, S._AUTO_DIR).replace(chr(92), '/')}")
                if not DRY:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    with open(dest, "w", encoding="utf-8") as fh:
                        fh.write(text)
                written += 1
    print(f"\n{'DRY RUN - ' if DRY else ''}{written} chapter(s) "
          f"{'to write' if DRY else 'written'}, {skipped} skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
