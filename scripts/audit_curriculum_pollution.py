import os
from pathlib import Path

base = Path("curriculum_docs_auto")
results = []
for p in base.rglob("*.md"):
    if p.name.startswith("Syllabus"):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")[:300].lower()
    except Exception:
        continue
    parts = p.parts
    subj = parts[1] if len(parts) > 1 else ""
    
    # Check if content obviously contradicts subject
    if "technicalmathematics" in subj.lower():
        if "accounting" in text:
            results.append((str(p), subj, "Accounting content in Tech Maths"))
    elif "mathematics" in subj.lower() and "lit" not in subj.lower() and "technical" not in subj.lower():
        if "accounting" in text or "debit" in text:
            results.append((str(p), subj, "Accounting content in Pure Maths"))
    elif "physicalsciences" in subj.lower():
        if "accounting" in text:
            results.append((str(p), subj, "Accounting content in Physical Sciences"))

print(f"Total cross-pollution files found: {len(results)}")
for r in results:
    print(r)
