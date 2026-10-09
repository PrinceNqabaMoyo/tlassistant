import os
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
BACKEND_DIR = REPO_ROOT / "caps-ai-backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

auto_dir = BACKEND_DIR / "curriculum_docs_auto"

def parse_folder_name(folder_name: str):
    m = re.match(r"^([A-Za-z]+(?:[A-Za-z]+)?)_Gr(\d+)$", folder_name)
    if m:
        return m.group(1), m.group(2)
    return folder_name, "10"

subject_folders = sorted([f for f in auto_dir.iterdir() if f.is_dir() and not f.name.startswith(".")])

results_by_subject = defaultdict(lambda: {
    "total_topics": 0,
    "genuine_covered": 0,
    "proxy_covered": 0,
    "uncovered": 0,
    "uncovered_list": [],
    "proxy_list": []
})

for sfolder in subject_folders:
    subj, grade = parse_folder_name(sfolder.name)
    key = f"{subj} Gr{grade}"
    
    # Collect all topic files
    for term_dir in sorted(sfolder.glob("Term*")):
        for md_file in sorted(term_dir.glob("*.md")):
            raw_title = md_file.stem
            clean_title = re.sub(r"^\d+[\.\s_]+", "", raw_title).strip()
            if not clean_title or clean_title.lower() == "revision":
                continue
            
            results_by_subject[key]["total_topics"] += 1
            gen_key = resolve_generator_key(topic=clean_title, grade=grade, subject=subj)
            
            if not gen_key or gen_key not in ALL_GENERATORS:
                results_by_subject[key]["uncovered"] += 1
                results_by_subject[key]["uncovered_list"].append((clean_title, term_dir.name))
            else:
                # Check for cross-grade or cross-subject proxy
                # Does the gen_key indicate another grade?
                gen_grade_match = re.search(r"grade(\d+)", gen_key.lower())
                gen_subj_match = gen_key.lower()
                
                is_proxy = False
                proxy_reason = ""
                
                if gen_grade_match and gen_grade_match.group(1) != grade:
                    is_proxy = True
                    proxy_reason = f"Grade mismatch: mapped to Grade {gen_grade_match.group(1)} generator ({gen_key})"
                elif "senior_phase" in gen_key.lower() and int(grade) >= 10:
                    is_proxy = True
                    proxy_reason = f"Senior phase generator used in FET Grade {grade} ({gen_key})"
                elif "g_sp_" in str(ALL_GENERATORS.get(gen_key)):
                    # generic senior phase placeholder
                    if "nets" not in gen_key:
                        pass
                
                if is_proxy:
                    results_by_subject[key]["proxy_covered"] += 1
                    results_by_subject[key]["proxy_list"].append((clean_title, gen_key, proxy_reason))
                else:
                    results_by_subject[key]["genuine_covered"] += 1

print("\n" + "=" * 90)
print("COMPREHENSIVE AUDIT OF ALL SUBJECTS IN CURRICULUM_DOCS_AUTO")
print("=" * 90)
print(f"{'Subject & Grade':<30} | {'Total':<6} | {'Genuine':<8} | {'Proxy':<6} | {'Missing':<8} | {'Genuine %':<10}")
print("-" * 90)

grand_total = 0
grand_genuine = 0
grand_proxy = 0
grand_missing = 0

for key in sorted(results_by_subject.keys()):
    d = results_by_subject[key]
    tot = d["total_topics"]
    gen = d["genuine_covered"]
    prx = d["proxy_covered"]
    unc = d["uncovered"]
    pct = (gen / tot * 100) if tot > 0 else 0
    
    grand_total += tot
    grand_genuine += gen
    grand_proxy += prx
    grand_missing += unc
    
    print(f"{key:<30} | {tot:<6} | {gen:<8} | {prx:<6} | {unc:<8} | {pct:>8.1f}%")

print("-" * 90)
grand_pct = (grand_genuine / grand_total * 100) if grand_total > 0 else 0
print(f"{'GRAND TOTAL':<30} | {grand_total:<6} | {grand_genuine:<8} | {grand_proxy:<6} | {grand_missing:<8} | {grand_pct:>8.1f}%")
print("=" * 90)

# Print detail on EMS and any missing/proxy topics
for key in sorted(results_by_subject.keys()):
    d = results_by_subject[key]
    if "EMS" in key or d["uncovered"] > 0 or d["proxy_covered"] > 0:
        print(f"\n[{key}] (Total: {d['total_topics']}, Genuine: {d['genuine_covered']}, Proxy: {d['proxy_covered']}, Missing: {d['uncovered']})")
        if d["uncovered_list"]:
            print("  MISSING TOPICS:")
            for title, term in d["uncovered_list"]:
                print(f"    - {term}: {title}")
        if d["proxy_list"]:
            print("  PROXY SHORTCUTS:")
            for title, gen_key, reason in d["proxy_list"][:10]:
                print(f"    - {title} -> {gen_key} [{reason}]")
            if len(d["proxy_list"]) > 10:
                print(f"    ... and {len(d['proxy_list']) - 10} more")
