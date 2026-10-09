"""
Comprehensive Audit: Source Syllabus Topics vs. Extracted Markdown Files
Validates that every topic in the syllabus documents has extracted material in curriculum_docs_auto.
"""

import os
import re
import sys
from pathlib import Path
import difflib

# Add curriculum_docs to path to import mappings
sys.path.insert(0, str(Path('caps-ai-backend/curriculum_docs').resolve()))
from topic_term_map import CAPS_FALLBACK_MAP, sanitize_subject_key, normalize_text

auto_root = Path('caps-ai-backend/curriculum_docs_auto').resolve()
source_pdf_dir = Path(r'C:\Users\princ\Desktop\Folders\curriculum_docs')

print("=" * 100)
print("AUDIT REPORT: CAPS SYLLABUS TOPICS VS EXTRACTED MARKDOWN FILES IN curriculum_docs_auto")
print("=" * 100)

results = []
unmatched_details = []

for subj_key, grades_dict in CAPS_FALLBACK_MAP.items():
    for gr_key, terms_dict in grades_dict.items():
        folder_name = f"{subj_key}_{gr_key}"
        target_dir = auto_root / folder_name
        if not target_dir.exists():
            matches = [d for d in auto_root.iterdir() if d.is_dir() and d.name.lower().replace(' ', '') == folder_name.lower().replace(' ', '')]
            target_dir = matches[0] if matches else None
        
        if not target_dir or not target_dir.exists():
            results.append({
                "subject": subj_key,
                "grade": gr_key,
                "status": "DIR_NOT_FOUND",
                "syl_topics": 0,
                "matched_topics": 0,
                "md_count": 0,
                "unmatched": []
            })
            continue

        extracted_mds = list(target_dir.glob("Term*/*.md"))
        extracted_stems = [re.sub(r'^\d+\.\s*', '', f.stem).strip() for f in extracted_mds]
        
        all_syl_topics = []
        for term, topics in terms_dict.items():
            for t in topics:
                if t.strip().lower() != "revision":
                    all_syl_topics.append((term, t.strip()))
        
        matched = 0
        unmatched_list = []
        for term, t in all_syl_topics:
            norm_t = normalize_text(t)
            # Find best match in extracted_stems
            found = False
            best_ratio = 0.0
            best_match_name = ""
            for stem in extracted_stems:
                norm_stem = normalize_text(stem)
                if norm_t in norm_stem or norm_stem in norm_t:
                    found = True
                    break
                ratio = difflib.SequenceMatcher(None, norm_t, norm_stem).ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match_name = stem
                if ratio >= 0.52:
                    found = True
                    break
            
            if found:
                matched += 1
            else:
                unmatched_list.append((term, t, best_match_name, best_ratio))
                unmatched_details.append((subj_key, gr_key, term, t, best_match_name, best_ratio))
        
        results.append({
            "subject": subj_key,
            "grade": gr_key,
            "status": "OK",
            "syl_topics": len(all_syl_topics),
            "matched_topics": matched,
            "md_count": len(extracted_mds),
            "unmatched": unmatched_list
        })

# Print summary table
header = f"{'Subject':22} | {'Grade':6} | {'Syllabus Topics':15} | {'Matched':8} | {'Total MDs':9} | Status"
print(header)
print("-" * 100)

all_ok = True
total_syl = 0
total_matched = 0
total_mds = 0

for r in results:
    s = r["subject"]
    g = r["grade"]
    if r["status"] == "DIR_NOT_FOUND":
        print(f"{s:22} | {g:6} | {'-':15} | {'-':8} | {'-':9} | DIRECTORY NOT FOUND")
        all_ok = False
        continue
    
    st = r["syl_topics"]
    m = r["matched_topics"]
    cnt = r["md_count"]
    total_syl += st
    total_matched += m
    total_mds += cnt
    
    if m == st:
        status_str = f"PASS (100% covered)"
    else:
        diff = st - m
        status_str = f"AUDIT ({diff} near-match checks)"
        all_ok = False
        
    print(f"{s:22} | {g:6} | {st:15d} | {m:8d} | {cnt:9d} | {status_str}")

print("-" * 100)
print(f"{'TOTAL':22} | {'-':6} | {total_syl:15d} | {total_matched:8d} | {total_mds:9d} | Coverage: {total_matched/total_syl*100:.1f}%\n")

if unmatched_details:
    print("=" * 100)
    print("CLOSE INSPECTION OF ITEMS FLAGGED AS POTENTIAL GAPS / NAMING VARIATIONS:")
    print("=" * 100)
    for subj, gr, term, t, best_name, ratio in unmatched_details:
        print(f"  [{subj} {gr}] {term}: '{t}'")
        print(f"     -> Closest extracted MD: '{best_name}' (match score: {ratio:.2f})")
else:
    print("All syllabus topics have 100% corresponding extracted markdown files.")
