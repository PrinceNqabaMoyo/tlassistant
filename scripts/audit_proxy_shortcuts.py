#!/usr/bin/env python3
"""
Inspect all 94 cross-grade borrowed proxies across curriculum_docs_auto.
"""
from pathlib import Path
import re
from collections import defaultdict
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = REPO_ROOT / "caps-ai-backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

auto_dir = BACKEND_DIR / "curriculum_docs_auto"

def parse_folder_name(folder_name: str):
    m = re.match(r"^([A-Za-z]+(?:[A-Za-z]+)?)_Gr(\d+)$", folder_name)
    if m:
        return m.group(1), m.group(2)
    m2 = re.match(r"^Grade(\d+)_([A-Za-z]+)$", folder_name)
    if m2:
        return m2.group(2), m2.group(1)
    return folder_name, "10"

proxies_by_folder = defaultdict(list)
total_topics = 0
genuine_count = 0

for subject_folder in sorted(auto_dir.iterdir()):
    if not subject_folder.is_dir() or subject_folder.name.startswith("."):
        continue
    subj_name, grade_str = parse_folder_name(subject_folder.name)
    for term_folder in sorted(subject_folder.glob("Term*")):
        for md_file in sorted(term_folder.glob("*.md")):
            clean_title = re.sub(r"^\d+[\.\s_]+", "", md_file.stem).strip()
            if not clean_title or clean_title.lower() == "revision":
                continue
            total_topics += 1
            key = resolve_generator_key(topic=clean_title, grade=grade_str, subject=subj_name)
            
            # Check grade match
            key_grade_match = f"grade{grade_str}" in key or f"gr{grade_str}" in key or (grade_str in ["7","8","9"] and "senior_phase" in key)
            if not key_grade_match:
                proxies_by_folder[subject_folder.name].append((term_folder.name, clean_title, key))
            else:
                genuine_count += 1

print("=" * 100)
print(f"AUDIT SUMMARY: {total_topics} Total Topics | {genuine_count} Genuine | {total_topics - genuine_count} Borrowed Proxies")
print("=" * 100)

for folder, items in sorted(proxies_by_folder.items()):
    print(f"\n[{folder}] ({len(items)} cross-grade borrowed proxies):")
    for term, topic, key in items:
        print(f"   [{term}] \"{topic}\" -> routed to \"{key}\"")
