import sys
import os
import random
import re

sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key, generate_variant

gr10_topics = [
    ("Conversions and time", "grade10_mathlit_conversions_and_time"),
    ("Measuring length weight volume and temperature", "grade10_mathlit_measuring_length_weight_volume_temperature"),
    ("Personal income expenditure and budgets", "grade10_mathlit_personal_income_expenditure_budgets"),
    ("Banking interest and taxation", "grade10_mathlit_banking_interest_and_taxation"),
    ("Financial documents and tariff systems", "grade10_mathlit_financial_documents_and_tariff_systems"),
    ("Numbers and calculations with numbers", "grade10_mathlit_numbers_and_calculations_with_numbers"),
    ("Data handling", "grade10_mathlit_data_handling"),
    ("Scale maps and plans", "grade10_mathlit_scale_maps_and_plans"),
    ("Assembly diagrams floor plans and packaging", "grade10_mathlit_assembly_diagrams_floor_plans_packaging"),
    ("Measurement of perimeter and area", "grade10_mathlit_measurement_of_perimeter_and_area"),
    ("Patterns relationships and representations", "grade10_mathlit_patterns_relationships_and_representations"),
    ("Probability", "grade10_mathlit_probability")
]

gr11_topics = [
    ("FINANCE (TAXATION AND UIF)", "grade11_mathlit_finance_taxation_and_uif"),
    ("CONVERSIONS AND TIME", "grade11_mathlit_conversions_and_time"),
    ("EXCHANGE RATES", "grade11_mathlit_exchange_rates"),
    ("Interest banking and inflation", "grade11_mathlit_interest_banking_and_inflation"),
    ("PATTERNS RELATIONSHIPS AND REPRESENTATIONS", "grade11_mathlit_patterns_relationships_and_representations"),
    ("PLANS AND OTHER REPRESENTATIONS", "grade11_mathlit_plans_and_other_representations"),
    ("DATA HANDLING", "grade11_mathlit_data_handling"),
    ("MAPS", "grade11_mathlit_maps"),
    ("Area and Volume", "grade11_mathlit_area_and_volume")
]

def audit_topic(grade, topic_title, expected_key):
    print(f"\n========================================================")
    print(f"AUDITING Grade {grade}: '{topic_title}' (expected key: {expected_key})")
    print(f"========================================================")
    
    resolved_key = resolve_generator_key(topic_title, grade=str(grade), subject="Mathematical Literacy")
    if resolved_key != expected_key:
        print(f"  [ROUTING ERROR] Resolved key '{resolved_key}' != expected '{expected_key}'")
    else:
        print(f"  [ROUTING OK] Correctly resolves to '{resolved_key}'")
        
    gen_func = ALL_GENERATORS.get(resolved_key)
    if not gen_func:
        print(f"  [REGISTRY ERROR] '{resolved_key}' NOT FOUND in ALL_GENERATORS!")
        return
        
    # Generate 5 questions across different seeds
    corruptions = []
    latex_leaks = []
    missing_diagrams = []
    archetypes_seen = set()
    
    for seed in [101, 102, 103, 104, 105]:
        try:
            res = generate_variant(
                topic=resolved_key,
                grade=str(grade),
                subject="Mathematical Literacy",
                seed=seed,
                count=10
            )
            questions = res if isinstance(res, list) else (res.get("questions") if isinstance(res, dict) else [res])
            for q in questions:
                arch = q.get("subskill") or q.get("archetype") or q.get("subtopic") or "unknown"
                archetypes_seen.add(arch)
                
                prompt = q.get("prompt") or q.get("question") or ""
                ans = str(q.get("correct_answer") or q.get("expected_answer") or "")
                sol = str(q.get("worked_solution") or q.get("explanation") or "")
                
                # Check for { } corruption
                if "{ }" in prompt or "{ }" in ans or "{ }" in sol:
                    corruptions.append(f"Literal '{{ }}' in prompt/answer/solution (Seed {seed})")
                if "7{ }50" in prompt or "7{ }50" in ans:
                    corruptions.append(f"7{{ }}50% defect detected (Seed {seed})")
                    
                # Check for raw un-delimited LaTeX in expected_answer
                if ("\\text{" in ans or "\\quad" in ans or "\\frac{" in ans) and not (ans.startswith("$") or ans.startswith("$$")):
                    latex_leaks.append(f"Raw undelimited LaTeX in answer: '{ans[:60]}...'")
                    
                # Check for diagram references without diagram
                mentions_diagram = any(w in prompt.lower() for w in ["refer to the diagram", "refer to the map", "refer to the floor plan", "refer to the table below", "given below", "diagram below"])
                has_diagram = bool(q.get("diagram") or q.get("diagram_spec") or q.get("diagram_data") or q.get("svg_data") or q.get("diagram_type") or q.get("table") or q.get("table_data"))
                if mentions_diagram and not has_diagram:
                    # check if the diagram or table is embedded directly in prompt text
                    if not ("|" in prompt or "<svg" in prompt or "```" in prompt):
                        missing_diagrams.append(f"Prompt references diagram/table but no diagram object or markup in prompt: '{prompt[:70]}...'")
        except Exception as e:
            print(f"  [EXECUTION ERROR] Seed {seed} failed: {e}")
            
    print(f"  Total archetypes sampled across 5 seeds: {len(archetypes_seen)}")
    if corruptions:
        print(f"  [CORRUPTION DEFECTS] {len(corruptions)} issues found:")
        for c in set(corruptions):
            print(f"    - {c}")
    else:
        print(f"  [CORRUPTIONS] None detected.")
        
    if latex_leaks:
        print(f"  [RAW LATEX LEAKS IN ANSWERS] {len(latex_leaks)} leaks found:")
        for l in set(latex_leaks):
            print(f"    - {l}")
    else:
        print(f"  [RAW LATEX LEAKS] None detected.")
        
    if missing_diagrams:
        print(f"  [MISSING DIAGRAMS] {len(missing_diagrams)} questions reference diagrams with none attached:")
        for m in set(missing_diagrams[:3]):
            print(f"    - {m}")
    else:
        print(f"  [MISSING DIAGRAMS] None detected.")

print(">>> AUDITING GRADE 10 MATHEMATICAL LITERACY <<<")
for title, key in gr10_topics:
    audit_topic(10, title, key)

print("\n>>> AUDITING GRADE 11 MATHEMATICAL LITERACY <<<")
for title, key in gr11_topics:
    audit_topic(11, title, key)
