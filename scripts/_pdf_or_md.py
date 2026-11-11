"""Are the 5 mis-filed chapters wrong in the SOURCE PDF, or only in the .md?

If the PDF is correct, re-mining the PDF fixes the topic (decision: mine PDFs).
If the PDF is also wrong, no amount of mining helps - it is a source-data gap.
"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend"))
from app.utils import sci_docs_harvester as S
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "curriculum_source_files")
AUTO = os.path.join(ROOT, "curriculum_docs_auto")

CASES = [
    ("Life Sciences", 11, r"LifeSciences_Gr11\Term 4\04. Human impact on the environment.md",
     "Textbook_LifeSciences_Gr11_Human_impact_on_the_environment.pdf"),
    ("Natural Sciences", 7, r"NaturalSciences_Gr7\Term 2\02. Separating mixtures.md",
     "Textbook_NaturalScience_Gr7_Separating_mixtures.pdf"),
    ("Natural Sciences", 8, r"NaturalSciences_Gr8\Term 2\03. Chemical reactions.md",
     "Textbook_NaturalScience_Gr8_Chemical_reactions.pdf"),
    ("Natural Sciences", 9, r"NaturalSciences_Gr9\Term 2\04. Reactions of Acids and bases.md",
     "Textbook_NaturalScience_Gr9_Reactions_of_acids_and_bases.pdf"),
    ("Physical Sciences", 12, r"PhysicalSciences_Gr12\Term 3\04. Electrochemical reactions.md",
     "Textbook_PhysicalSciences_Gr12_Electrochemical_reactions.pdf"),
]


def score(text, subject):
    low = text.lower()
    return S._kw_count(low, S._HOME_WORDS[subject]), S._kw_count(low, S._FOREIGN_WORDS)


def find_pdf(name):
    for dp, _d, fns in os.walk(SRC):
        if name in fns:
            return os.path.join(dp, name)
    for dp, _d, fns in os.walk(SRC):
        for fn in fns:
            if fn.startswith(name.split(".pdf")[0][:34]):
                return os.path.join(dp, fn)
    return None


for subject, grade, mdrel, pdfname in CASES:
    mdp = os.path.join(AUTO, mdrel)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", open(mdp, encoding="utf-8", errors="replace").read()) if os.path.isfile(mdp) else ""
    hp, fp = score(md, subject)
    p = find_pdf(pdfname)
    print("=" * 78)
    print(f"{subject} Gr{grade}  {os.path.basename(mdrel)}")
    print(f"    .md   : home={hp:5d} foreign={fp:5d}  -> {'REJECTED' if S._wrong_subject(md, subject) else 'kept'}")
    if not p:
        print(f"    PDF   : NOT FOUND for {pdfname}")
        continue
    d = pymupdf.open(p)
    txt = "".join(pg.get_text() for pg in d)
    pages = len(d)
    d.close()
    hp2, fp2 = score(txt, subject)
    verdict = "PDF IS CLEAN -> mine the PDF" if not (fp2 >= 10 and fp2 > hp2) else "PDF IS ALSO WRONG -> source gap"
    print(f"    PDF   : {os.path.basename(p)}")
    print(f"            chars={len(txt)} pages={pages} home={hp2:5d} foreign={fp2:5d}")
    print(f"            {verdict}")
    print(f"            first 160: {re.sub(r'[ \t]+',' ',txt[:160]).strip()!r}")
