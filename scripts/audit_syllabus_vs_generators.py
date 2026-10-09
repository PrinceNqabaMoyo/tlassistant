import os
import re
import sys
import json
from pathlib import Path

REPO_ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
AUTO_ROOT = REPO_ROOT / "caps-ai-backend" / "curriculum_docs_auto"
sys.path.insert(0, str(REPO_ROOT / "caps-ai-backend"))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

def clean_topic_title(raw: str) -> str:
    # Strip markdown bold/italics
    t = re.sub(r"[*_`]", "", raw)
    # Strip leading numbers like '1. ', '10. ', '1 '
    t = re.sub(r"^\d+[\.\s_]+", "", t)
    # Strip prefixes like 'The economy:', 'Financial literacy:', etc.
    t = re.sub(r"^(The economy:|Financial literacy:|Entrepreneurship:|Content:)\s*", "", t, flags=re.I)
    # Clean whitespace
    return t.strip()

def parse_atp_from_syllabus(syllabus_path: Path):
    text = syllabus_path.read_text(encoding="utf-8")
    atp_items = []
    current_term = "Term 1"
    
    for line in text.splitlines():
        term_match = re.search(r"Term\s*([1-4])", line, re.I)
        if term_match and ("#" in line or "Annual Teaching Plan" in line or "ATP" in line):
            current_term = f"Term {term_match.group(1)}"
            
        if line.strip().startswith("|") and not line.strip().startswith("| ---") and not line.strip().startswith("| Week"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2:
                week_col = parts[0]
                # Filter out header rows or summary rows
                if any(k in week_col.lower() for k in ["weighting", "curriculum", "cognitive", "mark"]):
                    continue
                topic_col = parts[1] if len(parts) > 1 else ""
                content_col = parts[2] if len(parts) > 2 else ""
                
                clean_topic = clean_topic_title(topic_col)
                if clean_topic and clean_topic.lower() not in ["revision", "topic", "content", "examination"]:
                    atp_items.append({
                        "term": current_term,
                        "weeks": week_col,
                        "topic": clean_topic,
                        "content": content_col
                    })
    return atp_items

syllabus_files = sorted(list(AUTO_ROOT.glob("*/Syllabus.md")))
summary_results = {}

for sfile in syllabus_files:
    folder_name = sfile.parent.name
    atp = parse_atp_from_syllabus(sfile)
    if not atp:
        continue
        
    m = re.match(r"^([A-Za-z]+(?:[A-Za-z]+)?)_Gr(\d+)$", folder_name)
    subj = m.group(1) if m else folder_name
    grade = m.group(2) if m else "10"
    
    summary_results[folder_name] = {
        "subject": subj,
        "grade": grade,
        "total_atp_items": len(atp),
        "items": []
    }
    
    for item in atp:
        gen_key = resolve_generator_key(topic=item["topic"], grade=grade, subject=subj)
        func = ALL_GENERATORS.get(gen_key) if gen_key else None
        
        status = "covered"
        issue = None
        if not gen_key or not func:
            status = "missing"
            issue = f"Topic '{item['topic']}' did not resolve to a generator"
        else:
            m_gr = re.search(r"grade(\d+)", gen_key.lower())
            if m_gr and m_gr.group(1) != grade:
                status = "proxy"
                issue = f"Borrowed from Grade {m_gr.group(1)} ({gen_key})"
            elif "senior_phase" in gen_key.lower() and int(grade) >= 10:
                status = "proxy"
                issue = f"Generic Senior Phase generator used in FET ({gen_key})"
                
        summary_results[folder_name]["items"].append({
            "term": item["term"],
            "weeks": item["weeks"],
            "topic": item["topic"],
            "status": status,
            "gen_key": gen_key,
            "issue": issue
        })

print("\n" + "=" * 95)
print("REFINED AUDIT: SYLLABUS.MD ATP SPECIFICATIONS VS ACTIVE GENERATORS")
print("=" * 95)
print(f"{'Subject / Grade':<30} | {'ATP Topics':<12} | {'Genuine':<10} | {'Proxy':<8} | {'Missing':<8} | {'Coverage %':<10}")
print("-" * 95)

total_atp = 0
total_gen = 0
total_prx = 0
total_mis = 0

for folder, d in summary_results.items():
    tot = d["total_atp_items"]
    gen = sum(1 for it in d["items"] if it["status"] == "covered")
    prx = sum(1 for it in d["items"] if it["status"] == "proxy")
    mis = sum(1 for it in d["items"] if it["status"] == "missing")
    pct = (gen / tot * 100) if tot > 0 else 0
    
    total_atp += tot
    total_gen += gen
    total_prx += prx
    total_mis += mis
    
    print(f"{folder:<30} | {tot:<12} | {gen:<10} | {prx:<8} | {mis:<8} | {pct:>8.1f}%")

print("-" * 95)
tot_pct = (total_gen / total_atp * 100) if total_atp > 0 else 0
print(f"{'TOTAL':<30} | {total_atp:<12} | {total_gen:<10} | {total_prx:<8} | {total_mis:<8} | {tot_pct:>8.1f}%")
print("=" * 95)

# Save JSON
out_path = REPO_ROOT / "scripts" / "syllabus_audit_refined.json"
out_path.write_text(json.dumps(summary_results, indent=2), encoding="utf-8")
print(f"Detailed output saved to: {out_path}")
