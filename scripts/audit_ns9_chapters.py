import os
import re

base = "curriculum_docs_auto/NaturalSciences_Gr9"
files = []
for root, dirs, fnames in os.walk(base):
    for fn in fnames:
        if fn.endswith(".md") and fn != "Syllabus.md":
            files.append(os.path.join(root, fn))

print(f"Total chapter files found: {len(files)}")
files.sort()

for fp in files:
    rel = os.path.relpath(fp, base)
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Extract headers
    headers = [line.strip("# ").strip() for line in text.splitlines() if line.startswith("# ") or line.startswith("## ") or line.startswith("### ")]
    # Extract images / diagrams
    images = re.findall(r'!\[.*?\]\((.*?)\)', text)
    # Extract math formulas
    maths = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    
    print(f"=== {rel} ({len(text.splitlines())} lines, {len(images)} images, {len(maths)} display math) ===")
    print("  Headers:", headers[:6])
    if images:
        print("  Sample images:", [os.path.basename(img) for img in images[:3]])
    print()
