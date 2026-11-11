import pymupdf
import pymupdf4llm
from pathlib import Path

# Paths setup
pdf_path = "C:\Users\princ\Desktop\Tutor Business\Physical Science\Gr11_PhysicalSciences_Learner_Eng.pdf"
output_dir = Path("C:/Users/princ/fundile-tlassistant-vite/caps-ai-backend/curriculum_docs/Physical-Science-Gr11/Term 1/Output")
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Target pages (Pages 149 to 176 are 0-indexed as 148 to 175)
target_pages = list(range(148, 176))

# 2. Extract Markdown and individual cropped diagrams
print("Extracting Markdown text and cropping diagrams...")
md_text = pymupdf4llm.to_markdown(
    pdf_path,
    pages=target_pages,
    write_images=True,
    image_path=str(output_dir / "images"),
    image_format="png",
    dpi=200
)

# Save the extracted raw markdown text
(output_dir / "raw_extracted.md").write_bytes(md_text.encode())

# 3. Save full-page images as visual backups (No fitz deprecation)
print("Rendering full-page visual backup images...")
doc = pymupdf.open(pdf_path)
full_pages_dir = output_dir / "full_page_images"
full_pages_dir.mkdir(exist_ok=True)

for page_num in target_pages:
    page = doc[page_num]
    pix = page.get_pixmap(dpi=200)
    pix.save(str(full_pages_dir / f"page_{page_num + 1}_full.png"))

doc.close()

print("\n--------------------------------------------------")
print(" Extraction Complete (Zero Deprecation Warnings)")
print(f" Raw Markdown: {output_dir / 'raw_extracted.md'}")
print(f" Diagram Cutouts: {output_dir / 'images'}")
print(f" Full Page Backups: {full_pages_dir}")
print("--------------------------------------------------\n")