"""Syllabus coverage audit: CAPS syllabus (authority) vs the generator registry.

Usage: python scripts/_sci_coverage.py "Life Sciences" 11
Answers the question the per-topic harvest review CANNOT answer: is every
syllabus topic actually implemented? A topic missing from the registry is
invisible to any registry-driven review, so the syllabus must drive the checklist.

Sources, in order:
  caps-ai-backend/caps-wiki/<subject>/grade-<n>/syllabus.md   (official CAPS ATP)
  curriculum_source_files/Syllabus_<Subject>_Gr<n>.pdf        (the SAME document
      in its original form - used when the .md is missing, and ALWAYS compared
      against, because a corrupt/truncated .md would silently shrink this
      checklist, which is the exact blind spot the checklist exists to close)
  caps-ai-backend/app/services/caps_term_registry_data.json   (what we implement)
"""
import sys, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "caps-ai-backend", "caps-wiki")
SRC_PDF = os.path.join(ROOT, "curriculum_source_files")
REG = os.path.join(ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")

# the syllabus PDFs use the SAME (singular) stem as the textbooks: NaturalScience
# here, NaturalSciences in the auto folder. Not interchangeable.
PDF_STEM = {"Life Sciences": "LifeSciences", "Natural Sciences": "NaturalScience",
            "Physical Sciences": "PhysicalSciences", "Business Studies": "BusinessStudies",
            "Accounting": "Accounting", "EMS": "EMS", "Mathematics": "Mathematics",
            "Mathematical Literacy": "MathematicalLiteracy",
            "Technical Mathematics": "TechnicalMathematics"}

SUBJECT_DIR = {
    "Life Sciences": "life-sciences",
    "Natural Sciences": "natural-sciences",
    "Physical Sciences": "physical-sciences",
    "Business Studies": "business-studies",
    "Accounting": "accounting",
    "EMS": "ems",
    "Mathematics": "mathematics",
}

# section headers that are scaffolding, never a content topic
_BOILER = re.compile(
    r"annual teaching plan|atp|assessment matrix|exam weighting|cognitive level|"
    r"mathematical application|pacing guideline|strand|overview|reference|"
    r"resource|policy|administrative|note\b|^grade\b|coverage|practical\b.*work"
    # cognitive-level bands and assessment scaffolding are NOT content topics
    r"|\bknowledge\b|routine procedure|complex procedure|problem solving"
    r"|examination|\bexam\b|project|assignment|portfolio|practical exam"
    r"|assessment|\bterm ?\d\b|total term|duration|weighting|marks?$"
    r"|^a?the?\s+(following|table)|infographic|checklist|rubric|memo"
    r"|^do you know|^key words|^new words|^summary|^revision"
    # ATP table noise that passed as a 'topic' in the LS Gr10 run:
    # cognitive-level BANDS ('Level 1'..'Level 4'), pacing cells, and the
    # optional-enrichment rows. None of them is assessable content.
    r"|^level ?\d|\bcognitive band\b|^optional\b|^enrichment|^remediation"
    r"|^sample|^activity \d|^week\b|^do now|^warm|^topic \d$|^content$",
    re.I,
)
# a duration / weighting cell, not a topic name
_NOT_TOPIC = re.compile(
    r"^\s*[\d,.]+\s*(week|hour|day|lesson|term|marks?|%|cap|weeks)"
    r"|^\s*[^\w]\s*(week|weeks)\b"          # '?? week' from a mangled pacing cell
    r"|^\s*(see|formal|informal|continuous|ongoing|\d+\s*-\s*\d+)",
    re.I,
)
_TERM_RE = re.compile(r"term[\s:_\-]*(\d)", re.I)


def norm(s: str) -> str:
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    stop = {"the", "a", "an", "of", "and", "or", "for", "to", "in", "on", "with",
            "grade", "term", "chapter", "unit", "topic", "content", "caps",
            "curriculum", "specification", "specifications", "life", "sciences"}
    return " ".join(w for w in s.split() if w not in stop)


def syllabus_topics(path):
    """[(term, topic_name)] harvested from a syllabus .md file."""
    return syllabus_topics_from_text(
        open(path, encoding="utf-8", errors="replace").read().splitlines())


def syllabus_topics_from_text(lines):
    """[(term, topic_name)] from ATP tables + content headings of any form.

    Shared by the .md and the scraped PDF because pymupdf4llm writes the ATP
    tables as '| **topic** |' rows - the same shape the .md uses.
    """
    out, cur_term = [], None
    for line in lines:
        h = re.match(r"^(#{2,6})\s+(.*)$", line)
        if h:
            txt = h.group(2)
            m = _TERM_RE.search(txt)
            if m:
                cur_term = int(m.group(1))
            # a numbered content heading, e.g. '#### 4. TRANSPORT IN MAMMALS'
            body = re.sub(r"^[\d.,]+\s*", "", txt)
            if (cur_term and len(body) > 6 and not _BOILER.search(body)
                    and not _NOT_TOPIC.match(body) and "&" not in body
                    and body.upper() == body and len(body) > 12):
                out.append((cur_term, body.title()))
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        for c in cells:
            b = re.findall(r"\*\*(.+?)\*\*", c)
            for name in b:
                name = re.sub(r"\*\*", "", name).strip()
                if cur_term is None or len(name) < 6 or len(name) > 70:
                    continue
                if _NOT_TOPIC.match(name) or _BOILER.search(name):
                    continue
                if ":" in name or " | " in name:
                    continue
                out.append((cur_term, name))
    # dedupe, keep first term seen
    seen, res = set(), []
    for t, n in out:
        k = (t, norm(n))
        if k in seen or not norm(n):
            continue
        seen.add(k)
        res.append((t, n))
    return res


def syllabus_pdf_topics(subject, grade):
    """([(term, name)], path) read from the ORIGINAL Syllabus_<Subject>_Gr<n>.pdf.

    The PDF is the same CAPS document the .md was scraped from, so it is the
    reference the .md itself can be checked against. Scrape failures show up as
    far fewer topics in the .md than in the PDF.
    """
    stem = PDF_STEM.get(subject, subject.replace(" ", "") if subject else "")
    path = os.path.join(SRC_PDF, f"Syllabus_{stem}_Gr{grade}.pdf")
    if not os.path.isfile(path):
        return [], path
    sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
    try:
        from app.utils import sci_docs_harvester as S
    except ImportError:
        return [], path
    text = S._pdf_to_md(path)
    return syllabus_topics_from_text(text.splitlines()), path


def registry_topics(subject, grade):
    data = json.load(open(REG, encoding="utf-8"))
    rows, seen = [], set()
    for e in data:
        if str(e.get("subject")) == subject and str(e.get("grade")) == str(grade):
            key = (str(e.get("term")), norm(str(e.get("name"))))
            if key in seen:
                continue
            seen.add(key)
            rows.append((e.get("term"), e.get("name"), e.get("generator_key")))
    return rows


def related(syl_name, reg_name):
    a, b = norm(syl_name), norm(reg_name)
    if not a or not b:
        return False
    if a == b:
        return True
    ta, tb = set(a.split()), set(b.split())
    inter = len(ta & tb)
    if inter >= 2 and inter / max(1, min(len(ta), len(tb))) >= 0.5:
        return True
    return a in b or b in a


def main():
    subject = sys.argv[1] if len(sys.argv) > 1 else "Life Sciences"
    grade = sys.argv[2] if len(sys.argv) > 2 else "11"
    wdir = SUBJECT_DIR.get(subject)
    if not wdir:
        print("no wiki dir for", subject); return 1
    path = os.path.join(WIKI, wdir, f"grade-{grade}", "syllabus.md")
    syl = syllabus_topics(path) if os.path.isfile(path) else []
    src = os.path.relpath(path, ROOT) if syl else "MISSING " + os.path.relpath(path, ROOT)

    # Cross-check against the original PDF. It is NOT merged by default:
    # measured on Syllabus_LifeSciences_Gr11.pdf, pymupdf4llm interleaves the
    # ATP table's columns mid-word ('|Life exists in a wide variety of fo and
    # animals. These are organise i|microorganisms that are a major|'), so its
    # 'topics' are fragments. Merging them would inject fake topics - the very
    # failure this checklist exists to catch. So the PDF is used only when the
    # .md yields nothing at all, and otherwise reported as a sanity number.
    pdf_syl, pdf_path = syllabus_pdf_topics(subject, grade)
    if not syl:
        syl = pdf_syl
        src = f"PDF {os.path.relpath(pdf_path, ROOT)}"
        print(f"NOTE  no usable syllabus .md; checklist built from the PDF "
              f"({len(syl)} topics - verify by eye, its tables extract garbled)")
    else:
        print(f"CHECK syllabus .md={len(syl)} topics, original PDF={len(pdf_syl)} "
              f"({os.path.relpath(pdf_path, ROOT)})")

    reg = registry_topics(subject, grade)
    print(f"SYLLABUS  {src}")
    print(f"  {len(syl)} distinct syllabus topics | {len(reg)} distinct registry topics\n")
    print("REGISTRY (what the app currently implements):")
    for t, name, key in sorted(reg, key=lambda x: (str(x[0]), x[1])):
        print(f"  T{t}  {name[:56]:56s} {key}")
    print("\nSYLLABUS COVERAGE:")
    missing = []
    for t, name in sorted(syl, key=lambda x: (x[0] or 9, x[1])):
        hit = next((r for r in reg if related(name, r[1])), None)
        flag = f"OK   -> {hit[2]}" if hit else "MISSING (no registry topic / no generator)"
        if not hit:
            missing.append((t, name))
        print(f"  T{t}  {name[:58]:58s} {flag}")
    print(f"\nTERMS - syllabus vs registry topic counts:")
    for term in (1, 2, 3, 4):
        s = len([x for x in syl if x[0] == term])
        r = len([x for x in reg if str(x[0]) == str(term)])
        print(f"  Term {term}: syllabus={s:2d}  registry={r:2d}")
    print(f"\n{subject} Gr{grade}: {len(missing)} syllabus topics NOT implemented.")
    for t, n in missing:
        print(f"   - T{t} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
