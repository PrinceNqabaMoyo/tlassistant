import os
from pathlib import Path
import re

pdf_dir = Path(r"C:\Users\princ\Desktop\Folders\curriculum_docs")
md_dir = Path("curriculum_docs_auto")

# Collect all markdown files and their first line/heading
md_map = {}
for p in md_dir.rglob("*.md"):
    if p.name.startswith("Syllabus"):
        continue
    try:
        lines = [line.strip() for line in p.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip()]
        first_h = lines[0] if lines else ""
    except Exception:
        first_h = ""
    # key: (subject, grade, topic_slug)
    parts = p.parts
    # parts: ('curriculum_docs_auto', 'TechnicalMathematics_Gr10', 'Term 1', '01. Introduction.md')
    subj_gr = parts[1] if len(parts) > 1 else ""
    md_map[p.name.lower()] = (str(p), subj_gr, first_h)

print(f"Total markdown files indexed: {len(md_map)}")

# Now scan PDFs
textbook_pdfs = list(pdf_dir.glob("Textbook_*.pdf"))
print(f"Total Textbook PDFs: {len(textbook_pdfs)}")

missing = []
for pdf in textbook_pdfs:
    # e.g. Textbook_TechnicalMathematics_Gr10_Introduction.pdf
    stem = pdf.stem
    # strip Textbook_
    clean = stem[9:] # e.g. TechnicalMathematics_Gr10_Introduction
    # Find matching md file
    found = False
    for md_name, (md_path, md_subj, first_h) in md_map.items():
        # check if matching
        topic_part = clean.split("_")[-1].lower().replace("-", " ")
        if topic_part in md_name.lower().replace("-", " "):
            found = True
            break
    if not found:
        missing.append(stem)

print(f"\nPDFs with no obvious markdown match in curriculum_docs_auto: {len(missing)}")
for m in missing[:30]:
    print(" ", m)
