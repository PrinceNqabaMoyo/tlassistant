"""
Comprehensive Audit of Generator Implementation Gaps in Fundile
Audits:
1. Which topics in the curriculum resolve to valid generators.
2. Which topics resolve to cross-grade proxies (e.g. Gr7 -> Gr8, Gr8 -> Gr9, Gr11 -> Gr12).
3. Which topics fail to resolve completely.
4. Tests generator execution for all registered keys to identify crashes or missing attributes.
"""

import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path('caps-ai-backend').resolve()))
from app.services.generator_registry import (
    ALL_GENERATORS,
    TOPIC_ALIASES,
    resolve_generator_key,
    generate_variant,
)
from curriculum_docs.topic_term_map import CAPS_FALLBACK_MAP

print("=" * 90)
print("AUDIT: GENERATOR REGISTRY COVERAGE & PROXY ROUTING AUDIT")
print("=" * 90)
print(f"Total Registered Generator Functions: {len(ALL_GENERATORS)}")
print(f"Total Topic Aliases: {len(TOPIC_ALIASES)}\n")

unresolved = []
proxy_routed = []
working_direct = []

for subj, grades in CAPS_FALLBACK_MAP.items():
    if subj in ["Geography"]: # Not currently implemented in Fundile
        continue
    for gr, terms in grades.items():
        gr_num = gr.replace("Gr", "")
        for term, topics in terms.items():
            for t in topics:
                if t.strip().lower() == "revision":
                    continue
                resolved_key = resolve_generator_key(t, grade=gr_num, subject=subj)
                if not resolved_key or resolved_key not in ALL_GENERATORS:
                    unresolved.append((subj, gr, term, t, resolved_key))
                else:
                    target_gr = f"grade{gr_num}_"
                    # Check if resolved to a different grade generator
                    other_grades = [f"grade{i}_" for i in range(7, 13) if str(i) != gr_num]
                    is_cross_grade = any(og in resolved_key for og in other_grades)
                    
                    if is_cross_grade:
                        proxy_routed.append((subj, gr, term, t, resolved_key))
                    else:
                        working_direct.append((subj, gr, term, t, resolved_key))

print(f"Direct Grade-Matched Generators : {len(working_direct)}")
print(f"Cross-Grade Proxy Mappings       : {len(proxy_routed)}")
print(f"Unresolved Curriculum Topics     : {len(unresolved)}")

print("\n" + "=" * 90)
print("1. CROSS-GRADE PROXY ROUTED TOPICS (NEEDS DEDICATED GENERATOR OR ALIGNMENT):")
print("=" * 90)
for subj, gr, term, t, key in proxy_routed:
    print(f"  [{subj:18} {gr:4}] {term:6}: '{t}' -> {key}")

print("\n" + "=" * 90)
print("2. UNRESOLVED TOPICS (MISSING FROM REGISTRY):")
print("=" * 90)
for subj, gr, term, t, key in unresolved:
    print(f"  [{subj:18} {gr:4}] {term:6}: '{t}' (key: {key})")

print("\n" + "=" * 90)
print("3. EXECUTABILITY AUDIT: TESTING ALL REGISTERED GENERATORS (1 QUESTION EACH)")
print("=" * 90)

exec_success = 0
exec_failed = []

for gen_key, gen_fn in sorted(ALL_GENERATORS.items()):
    try:
        # Test call
        q_list = None
        # Try generate_variant first if possible, or direct call
        try:
            res = gen_fn(count=1, seed=42, difficulty="medium", mode="compound")
        except TypeError:
            try:
                res = gen_fn(count=1, seed=42)
            except TypeError:
                res = gen_fn()
        
        if isinstance(res, list) and len(res) > 0:
            q = res[0]
        elif isinstance(res, dict):
            if "questions" in res and isinstance(res["questions"], list) and len(res["questions"]) > 0:
                q = res["questions"][0]
            else:
                q = res
        else:
            raise ValueError(f"Unknown return type: {type(res)}")
        
        # Verify essential fields
        prompt = (
            q.get("prompt")
            or q.get("prompt_latex")
            or q.get("question")
            or q.get("question_text")
            or q.get("instruction")
        )
        if not prompt:
            raise ValueError(f"Generated question missing prompt / question text (keys: {list(q.keys())[:5]})")
        
        exec_success += 1
    except Exception as e:
        exec_failed.append((gen_key, str(e)))

print(f"Successfully Executed Generators: {exec_success} / {len(ALL_GENERATORS)}")
if exec_failed:
    print(f"\nGenerators with Execution Failures ({len(exec_failed)}):")
    for k, err in exec_failed:
        print(f"  FAILED [{k}]: {err}")
else:
    print("All registered generators executed cleanly with valid question payloads!")
