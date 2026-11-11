import re
import sys
from pathlib import Path

ROOT = Path(".")
sys.path.insert(0, str(ROOT / "caps-ai-backend"))
sys.path.insert(0, str(ROOT / "scripts"))

from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import generate_variant, get_topic_archetypes, resolve_generator_key
from verify_no_hollywood_audit import extract_procedure_text

g12_topics = [t for t in _ALL_TOPIC_RECORDS if str(t.get("grade")) == "12"]
print(f"Loaded {len(g12_topics)} topics for Grade 12.")

crashes = []
entropy_issues = []
raw_latex_issues = []
caps_leak_issues = []
thin_procedure_issues = []
answer_leak_issues = []

for t in g12_topics:
    subject = t.get("subject", "")
    topic_name = t.get("name", "")
    info = get_topic_archetypes(topic=topic_name, grade="12", subject=subject)
    archs = info.get("archetypes") or []
    gen_key = resolve_generator_key(topic_name, grade="12", subject=subject)
    
    for arch in archs:
        try:
            q101 = generate_variant(topic_name, subskill=arch, grade="12", subject=subject, seed=101)[0]
            q202 = generate_variant(topic_name, subskill=arch, grade="12", subject=subject, seed=202)[0]
            q303 = generate_variant(topic_name, subskill=arch, grade="12", subject=subject, seed=303)[0]
        except Exception as e:
            crashes.append(f"{subject} | {topic_name} | {arch} -> {e}")
            continue

        p101 = q101.get("prompt", "")
        p202 = q202.get("prompt", "")
        p303 = q303.get("prompt", "")

        if p101 == p202 == p303:
            entropy_issues.append(f"{subject} | {topic_name} | {arch}")

        # CAPS check
        if re.search(r"\bCAPS\b", p101):
            caps_leak_issues.append(f"{subject} | {topic_name} | {arch}")

        # Answer leak check
        ans = str(q101.get("correct_answer") or "").strip()
        if ans and len(ans) > 4 and ans.lower() in p101.lower():
            answer_leak_issues.append(f"{subject} | {topic_name} | {arch}: answer '{ans}' in prompt")

        # Procedure check
        marks = q101.get("marks") or q101.get("total_marks") or 1
        if marks >= 2:
            steps, sol = extract_procedure_text(q101)
            if len(sol.strip()) < 30 and not q101.get("sub_questions") and not q101.get("parts"):
                thin_procedure_issues.append(f"{subject} | {topic_name} | {arch}: procedure len={len(sol.strip())}")

print(f"\n--- Grade 12 Dry Run Results ---")
print(f"Crashes: {len(crashes)}")
for c in crashes:
    print(f"  CRASH: {c}")

print(f"Entropy issues (static prompts): {len(entropy_issues)}")
for e in entropy_issues:
    print(f"  STATIC: {e}")

print(f"CAPS leaks: {len(caps_leak_issues)}")
for k in caps_leak_issues:
    print(f"  CAPS: {k}")

print(f"Answer leaks: {len(answer_leak_issues)}")
for a in answer_leak_issues:
    print(f"  LEAK: {a}")

print(f"Thin procedures (marks >= 2): {len(thin_procedure_issues)}")
for t in thin_procedure_issues:
    print(f"  THIN: {t}")
