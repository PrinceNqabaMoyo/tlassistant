import os
from pathlib import Path
import re

pdf_dir = Path(r"C:\Users\princ\Desktop\Folders\curriculum_docs")
md_dir = Path("curriculum_docs_auto")

pdf_files = list(pdf_dir.glob("*.pdf"))
print(f"Total PDF files in source: {len(pdf_files)}")

# Group PDFs by subject and grade
pdf_by_subject = {}
for p in pdf_files:
    name = p.stem
    # e.g. Textbook_TechnicalMathematics_Gr10_Introduction
    m = re.match(r"(?:Textbook|Syllabus)_([A-Za-z]+)_Gr(\d+)(?:_(.*))?", name)
    if m:
        subj, gr, topic = m.group(1), m.group(2), m.group(3) or "Syllabus"
        key = (subj, gr)
        if key not in pdf_by_subject:
            pdf_by_subject[key] = []
        pdf_by_subject[key].append((topic, p))
    else:
        # Check other naming patterns
        key = ("Other", "0")
        if key not in pdf_by_subject:
            pdf_by_subject[key] = []
        pdf_by_subject[key].append((name, p))

print("\nPDF breakdown by Subject and Grade:")
for (subj, gr), items in sorted(pdf_by_subject.items()):
    print(f"  {subj} Gr{gr}: {len(items)} chapters/files")

# Check MD files in curriculum_docs_auto
md_files = list(md_dir.rglob("*.md"))
print(f"\nTotal MD files in curriculum_docs_auto: {len(md_files)}")
