import sys, os
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, "caps-ai-backend")
from app.services.generator_registry import resolve_generator_key

auto_dir = Path("curriculum_docs_auto")
folders = sorted([d for d in auto_dir.iterdir() if d.is_dir()])

subject_map = {
    "Accounting": "Accounting",
    "BusinessStudies": "Business Studies",
    "EMS": "Economic and Management Sciences",
    "LifeSciences": "Life Sciences",
    "MathematicalLiteracy": "Mathematical Literacy",
    "Mathematics": "Mathematics",
    "NaturalSciences": "Natural Sciences",
    "PhysicalSciences": "Physical Sciences",
    "TechnicalMathematics": "Technical Mathematics"
}

tracks = []

for fd in folders:
    parts = fd.name.split("_")
    if len(parts) < 2:
        continue
    subj_code = parts[0]
    subj = subject_map.get(subj_code, subj_code)
    grade = parts[1].replace("Gr", "")
    
    md_files = [f for f in fd.rglob("*.md") if f.name != "Syllabus.md"]
    topic_count = len(md_files)
    
    gen_map = defaultdict(list)
    for md in md_files:
        clean = md.stem
        import re
        clean = re.sub(r"^\d+[\.\s_]*", "", clean).strip()
        gen_key = resolve_generator_key(clean, grade=grade, subject=subj)
        gen_map[gen_key].append(clean)
        
    unique_gens = len(gen_map)
    max_shared = max((len(v) for v in gen_map.values()), default=0)
    
    alien_gens = 0
    for k in gen_map:
        if subj == "Life Sciences" and "natural_sciences" in k:
            alien_gens += len(gen_map[k])
        elif subj == "Technical Mathematics" and "grade" in k and "math_" in k and "technical" not in k:
            alien_gens += len(gen_map[k])
            
    tracks.append({
        "grade": int(grade),
        "subject": subj,
        "code": fd.name,
        "topics": topic_count,
        "unique_gens": unique_gens,
        "max_shared": max_shared,
        "alien_gens": alien_gens,
        "ratio": unique_gens / max(1, topic_count)
    })

tracks.sort(key=lambda x: (x["grade"], x["subject"]))

print("| Grade | Subject | Topics | Distinct Gens | Ratio | Alien / Borrowed | Status |")
print("| :---: | :--- | :---: | :---: | :---: | :---: | :--- |")
for t in tracks:
    ratio_pct = int(t["ratio"] * 100)
    if t["alien_gens"] > 0:
        status = f"BORROWED ({t['alien_gens']} topics)"
    elif t["max_shared"] >= 4 or ratio_pct < 50:
        status = f"BUNDLED (max {t['max_shared']} per gen)"
    elif ratio_pct >= 70:
        status = "DEDICATED"
    else:
        status = "PARTIAL"
    print(f"| Gr{t['grade']:<2} | {t['subject']:32} | {t['topics']:2} | {t['unique_gens']:2} | {ratio_pct:2}% | {t['alien_gens']:2} | {status} |")
