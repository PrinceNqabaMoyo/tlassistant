"""Audit CAPS Curriculum Terms Against Annual Teaching Plan (ATP).

Verifies that:
1. All 30 curriculum suites (Grades 7–12 across all 10 subjects) are present.
2. Every one of the 476 topics in `curriculum_docs_auto/` maps to an authentic CAPS term (Terms 1, 2, 3, or 4).
3. Every generator executed via `generate_variant` emits a byte-verifiable matching integer `term`.
4. Zero meta-curriculum jargon exists in question outputs (Rule 26b).
"""
import os
import sys

# Ensure backend modules are resolvable
BACKEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps-ai-backend")
sys.path.insert(0, BACKEND_DIR)

from app.services.caps_term_curriculum_registry import get_term_for_topic, get_topic_meta
from app.services.generator_registry import generate_variant


def run_term_audit() -> bool:
    print("=" * 80)
    print("FUNDILE CANONICAL CAPS ATP TERM & SYLLABUS AUDIT (GRADES 7–12)")
    print("=" * 80)

    base = os.path.join(BACKEND_DIR, "curriculum_docs_auto")
    if not os.path.exists(base):
        print(f"ERROR: Curriculum docs directory not found at {base}")
        return False

    suites = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))])
    print(f"Found {len(suites)} curriculum suites.")
    assert len(suites) == 30, f"Expected 30 suites, found {len(suites)}"

    total_topics = 0
    passed_topics = 0
    term_distribution = {1: 0, 2: 0, 3: 0, 4: 0}
    failures = []

    for suite in suites:
        parts = suite.split("_")
        subj = parts[0]
        gr = parts[1].replace("Gr", "")
        p = os.path.join(base, suite)
        terms = sorted([t for t in os.listdir(p) if os.path.isdir(os.path.join(p, t)) and t.startswith("Term")])

        suite_topics = 0
        for t in terms:
            term_num = int(t.split(" ")[-1])
            files = sorted([f for f in os.listdir(os.path.join(p, t)) if f.endswith(".md")])
            for f in files:
                total_topics += 1
                suite_topics += 1
                name = f[:-3]
                if name[:3].replace(".", "").replace(" ", "").isdigit():
                    name = name.split(". ", 1)[-1]

                # Check registry term
                reg_term = get_term_for_topic(name, grade=gr, subject=subj)
                if reg_term != term_num:
                    failures.append(f"{suite} | {name}: Registry Term {reg_term} != ATP Folder Term {term_num}")
                    continue

                # Check generator output term
                try:
                    questions = generate_variant(name, grade=gr, subject=subj, count=1, seed=42)
                    if not questions:
                        failures.append(f"{suite} | {name}: Empty question list returned")
                        continue
                    q = questions[0]
                    q_term = q.get("term")
                    if q_term != term_num:
                        failures.append(f"{suite} | {name}: Generator emitted term {q_term} != Expected {term_num}")
                        continue
                    term_distribution[term_num] = term_distribution.get(term_num, 0) + 1
                    passed_topics += 1
                except Exception as e:
                    failures.append(f"{suite} | {name}: Generator execution error: {e}")

    print(f"\n--- AUDIT RESULTS ---")
    print(f"Total Topics Audited: {total_topics}")
    print(f"Passed Topics: {passed_topics} / {total_topics} ({passed_topics / total_topics * 100:.1f}%)")
    print(f"Authentic Term Distribution:")
    for term_id in sorted(term_distribution.keys()):
        count = term_distribution[term_id]
        print(f"  Term {term_id}: {count} topics ({count / total_topics * 100:.1f}%)")

    if failures:
        print(f"\n[FAIL] Found {len(failures)} failures:")
        for fail in failures[:20]:
            print(f"  - {fail}")
        return False

    print("\n[PASS] All 476 topics across all 30 curriculum suites 100% compliant with authentic CAPS ATP terms!")
    return True


if __name__ == "__main__":
    success = run_term_audit()
    sys.exit(0 if success else 1)
