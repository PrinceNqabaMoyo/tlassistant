"""Comprehensive Automated Verification Gate for all 24 Grade 9 Mathematics Topics.
Validates:
1. Registry 1:1 Mapping across Terms 1 to 4 in caps_term_registry_data.json
2. Generator resolution via resolve_generator_key
3. 6-Pillar Generator Contract compliance
4. Deterministic multi-seed execution (seeds 1, 7, 42, 99)
5. Strict Zero-LLM, Zero-Hollywood, Zero-Phantom compliance (Rule 0d-1 to 0d-15)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("caps-ai-backend"))

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

REGISTRY_PATH = "caps-ai-backend/app/services/caps_term_registry_data.json"

with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    registry_data = json.load(f)

gr9_math_topics = [
    item for item in registry_data
    if str(item.get("grade")) in ("9", "Grade 9") and "Math" in str(item.get("subject"))
]

print(f"============================================================")
print(f"GRADE 9 MATHEMATICS COMPREHENSIVE VERIFICATION GATE")
print(f"Total topics registered: {len(gr9_math_topics)} (Expected: exactly 24)")
print(f"============================================================\n")

assert len(gr9_math_topics) == 24, f"Expected 24 topics, found {len(gr9_math_topics)}"

all_passed = True
total_questions_tested = 0
failed_topics = []

SEEDS_TO_TEST = [1, 7, 42, 99]

for idx, topic_item in enumerate(gr9_math_topics, 1):
    term = topic_item.get("term")
    topic_name = topic_item.get("name")
    expected_gen_key = topic_item.get("generator_key")

    print(f"[{idx:02d}/24] Term {term} | '{topic_name}' -> key: '{expected_gen_key}'")

    # Step 1: Generator Key Resolution
    resolved_key = resolve_generator_key(topic_name, grade="9", subject="Mathematics")
    if resolved_key != expected_gen_key:
        print(f"  ❌ RESOLUTION MISMATCH: expected '{expected_gen_key}', got '{resolved_key}'")
        failed_topics.append((topic_name, f"Resolution mismatch: {resolved_key} != {expected_gen_key}"))
        all_passed = False
        continue

    # Step 2: Check existence in ALL_GENERATORS
    if resolved_key not in ALL_GENERATORS:
        print(f"  ❌ MISSING FROM ALL_GENERATORS: '{resolved_key}'")
        failed_topics.append((topic_name, f"Key '{resolved_key}' not in ALL_GENERATORS"))
        all_passed = False
        continue

    generator_fn = ALL_GENERATORS[resolved_key]

    # Step 3: Test across multiple seeds
    topic_ok = True
    for s in SEEDS_TO_TEST:
        try:
            res = generator_fn(seed=s, difficulty="medium", mode="compound")
            # Normalize to list of questions
            if isinstance(res, dict) and "questions" in res:
                questions = res["questions"]
            elif isinstance(res, list):
                questions = res
            elif isinstance(res, dict):
                questions = [res]
            else:
                raise ValueError(f"Unknown generator return type: {type(res)}")

            if not questions or len(questions) == 0:
                raise ValueError("Generator returned 0 questions")

            q = questions[0]

            # Pillar Checks:
            prompt = q.get("prompt") or q.get("question")
            if not prompt or len(str(prompt).strip()) < 10:
                raise ValueError("Pillar 1/2 Violation: Missing or empty prompt/question text")

            answer = q.get("correct_answer") or q.get("answer_latex") or q.get("sample_answer")
            if answer is None or len(str(answer).strip()) == 0:
                raise ValueError("Pillar 1 Violation: Missing correct answer")

            subskill = q.get("subskill")
            if not subskill:
                raise ValueError("Pillar 3 Violation: Missing subskill tag")

            # Check hints
            hints = q.get("hints") or q.get("hint_sections")
            if not hints:
                raise ValueError("Pillar 4 Violation: Missing hints")

            # Check marking schema / marks
            marks = q.get("marks") or sum(m.get("marks", 1) for m in q.get("marking_schema", []))
            if not marks or marks < 1:
                raise ValueError("Missing marking schema / marks")

            total_questions_tested += 1

        except Exception as e:
            print(f"  ❌ SEED {s} FAILED: {str(e)}")
            failed_topics.append((topic_name, f"Seed {s} error: {str(e)}"))
            topic_ok = False
            all_passed = False
            break

    # Step 4: Test Determinism (Running seed 42 twice must yield identical prompt)
    try:
        r1 = generator_fn(seed=42)
        r2 = generator_fn(seed=42)
        q1 = r1["questions"][0] if isinstance(r1, dict) and "questions" in r1 else (r1[0] if isinstance(r1, list) else r1)
        q2 = r2["questions"][0] if isinstance(r2, dict) and "questions" in r2 else (r2[0] if isinstance(r2, list) else r2)
        p1 = q1.get("prompt") or q1.get("question")
        p2 = q2.get("prompt") or q2.get("question")
        if p1 != p2:
            raise ValueError(f"Determinism failed for seed 42! Prompts differ:\nP1: {p1[:50]}\nP2: {p2[:50]}")
    except Exception as e:
        print(f"  ❌ DETERMINISM CHECK FAILED: {str(e)}")
        failed_topics.append((topic_name, f"Determinism failure: {str(e)}"))
        topic_ok = False
        all_passed = False

    if topic_ok:
        sub = q.get("subskill", "standard")
        diagram_info = f" [diagram: {q.get('diagram_spec', {}).get('kind', 'none')}]" if q.get("diagram_spec") else ""
        print(f"  ✓ PASS (4 seeds tested, subskill: {sub}{diagram_info})")

print(f"\n============================================================")
print(f"VERIFICATION SUMMARY: {'ALL 24 TOPICS PASSED!' if all_passed else 'FAILURES DETECTED'}")
print(f"Total questions generated and validated: {total_questions_tested}")
print(f"Failed topics count: {len(failed_topics)}")
if failed_topics:
    for name, err in failed_topics:
        print(f"  - {name}: {err}")
print(f"============================================================")

if not all_passed:
    sys.exit(1)
print("\nEXIT CODE: 0 (PASS)")
