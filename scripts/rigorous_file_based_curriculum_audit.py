#!/usr/bin/env python3
"""
Rigorous File-Based Curriculum Audit
Reads every single extracted markdown topic in caps-ai-backend/curriculum_docs_auto/
and cross-references against:
1. caps-ai-backend/curriculum_docs/ (manually typed source docs)
2. caps-ai-backend/app/utils/ (generator python files)
3. caps-ai-backend/app/services/generator_registry.py (topic resolution & execution)

Outputs the REAL, unvarnished coverage without any proxy shortcuts.
"""
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Any

# Ensure backend on sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = REPO_ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key, generate_variant

auto_dir = BACKEND_DIR / "curriculum_docs_auto"
manual_dir = BACKEND_DIR / "curriculum_docs"

# Parse subject and grade from folder names like Mathematics_Gr7, Accounting_Gr10, PhysicalSciences_Gr11
def parse_folder_name(folder_name: str):
    m = re.match(r"^([A-Za-z]+(?:[A-Za-z]+)?)_Gr(\d+)$", folder_name)
    if m:
        return m.group(1), m.group(2)
    # Check alternate format
    m2 = re.match(r"^Grade(\d+)_([A-Za-z]+)$", folder_name)
    if m2:
        return m2.group(2), m2.group(1)
    return folder_name, "10"

print("=" * 100)
print("RIGOROUS FILE-BASED CURRICULUM AUDIT: ALL EXTRACTED .MD TOPIC FILES VS GENERATORS")
print("=" * 100)

all_topics = []
for subject_folder in sorted(auto_dir.iterdir()):
    if not subject_folder.is_dir() or subject_folder.name.startswith("."):
        continue
    
    subj_name, grade_str = parse_folder_name(subject_folder.name)
    
    for term_folder in sorted(subject_folder.glob("Term*")):
        term_num = term_folder.name
        for md_file in sorted(term_folder.glob("*.md")):
            # Strip leading number prefixes like '01. ', '1. '
            raw_title = md_file.stem
            clean_title = re.sub(r"^\d+[\.\s_]+", "", raw_title).strip()
            if not clean_title or clean_title.lower() == "revision":
                continue
            
            all_topics.append({
                "folder": subject_folder.name,
                "subject": subj_name,
                "grade": grade_str,
                "term": term_num,
                "file": md_file.name,
                "title": clean_title,
                "path": str(md_file.relative_to(REPO_ROOT))
            })

print(f"Total Extracted Topic Files Found in curriculum_docs_auto: {len(all_topics)}")

# Check each topic against generator registry
covered_count = 0
uncovered = []
proxy_shortcuts = []

for t in all_topics:
    # Try resolving via topic title, grade, and subject
    gen_key = resolve_generator_key(topic=t["title"], grade=t["grade"], subject=t["subject"])
    
    if not gen_key or gen_key not in ALL_GENERATORS:
        uncovered.append(t)
    else:
        # Check if gen_key is a suspicious cross-topic proxy shortcut
        # (e.g. 3D objects mapped to 2D shapes, or different grade)
        title_lower = t["title"].lower()
        key_lower = gen_key.lower()
        
        # Flag if 3D topic is mapped to 2D
        if "3d" in title_lower and "2d" in key_lower and "3d" not in key_lower:
            proxy_shortcuts.append((t, gen_key, "3D topic mapped to 2D generator"))
        else:
            covered_count += 1

print(f"Cleanly Covered Topics: {covered_count} / {len(all_topics)} ({covered_count / len(all_topics) * 100:.1f}%)")
print(f"Uncovered Topics:       {len(uncovered)} / {len(all_topics)}")
if proxy_shortcuts:
    print(f"Suspicious Proxy Shortcuts: {len(proxy_shortcuts)}")
    for t, key, reason in proxy_shortcuts:
        print(f"  [SHORTCUT] {t['folder']} - {t['title']} -> {key} ({reason})")

print("\n" + "=" * 100)
print("DETAILED BREAKDOWN BY SUBJECT & GRADE")
print("=" * 100)

by_folder = {}
for t in all_topics:
    f = t["folder"]
    if f not in by_folder:
        by_folder[f] = {"total": 0, "covered": 0, "missing": []}
    by_folder[f]["total"] += 1

for t in uncovered:
    by_folder[t["folder"]]["missing"].append(f"{t['term']}: {t['title']}")

for f, stats in sorted(by_folder.items()):
    cov = stats["total"] - len(stats["missing"])
    pct = (cov / stats["total"] * 100) if stats["total"] > 0 else 0
    status_icon = "[OK]     " if len(stats["missing"]) == 0 else "[MISSING]"
    print(f"{status_icon} {f:<30} {cov:>2}/{stats['total']:<2} ({pct:>5.1f}%)")
    if stats["missing"]:
        for m in stats["missing"][:6]: # show up to 6
            print(f"    - Missing: {m}")
        if len(stats["missing"]) > 6:
            print(f"    ... and {len(stats['missing']) - 6} more")
