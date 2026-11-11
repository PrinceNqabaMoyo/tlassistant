import sys
sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import get_topic_archetypes

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

print("=== GRADE 10 ARCHETYPE COUNTS VIA get_topic_archetypes ===")
for title, key in gr10_topics:
    res = get_topic_archetypes(title, grade="10", subject="Mathematical Literacy")
    archs = res.get("archetypes", [])
    print(f"{title:48} -> {len(archs):3} archetypes (key: {res.get('generator_key')})")

print("\n=== GRADE 11 ARCHETYPE COUNTS VIA get_topic_archetypes ===")
for title, key in gr11_topics:
    res = get_topic_archetypes(title, grade="11", subject="Mathematical Literacy")
    archs = res.get("archetypes", [])
    print(f"{title:48} -> {len(archs):3} archetypes (key: {res.get('generator_key')})")
