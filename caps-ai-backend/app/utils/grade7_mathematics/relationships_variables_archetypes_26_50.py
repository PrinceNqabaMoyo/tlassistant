"""Grade 7 Mathematics - Relationships Between Variables: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/03. Relationships between variables.md
Focus: Contextual formulae (perimeter, utility billing, distance-speed-time), direct/inverse concepts, rate units, correlation vs causation, and variable autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Relationship formula perimeter of rectangles
def arch_26_relationship_formula_perimeter_of_rectangles(rng: random.Random) -> Dict[str, Any]:
    # Fixed breadth b = 6 cm. P = 2l + 2(6) = 2l + 12. For l = 10 -> 2(10) + 12 = 32 cm
    ans = "P = 2l + 12"
    prompt = (
        "A set of rectangles all have a fixed width of 6 cm, but varying lengths \\(l\\).\n\n"
        "1. Write the formula for the perimeter \\(P\\) in terms of length \\(l\\).\n"
        "2. Calculate the perimeter when \\(l = 10\\text{ cm}\\)."
    )
    sol = (
        "**Step 1: Formula:**\n"
        "$$P = 2l + 2b = 2l + 2(6) = \\mathbf{2l + 12}$$\n\n"
        "**Step 2: Calculation for \\(l = 10\\):**\n"
        "$$P = 2(10) + 12 = 20 + 12 = \\mathbf{32\\text{ cm}}$$"
    )
    return {
        "id": f"g7_rel_26_{rng.randint(100000, 999999)}",
        "subskill": "26_relationship_formula_perimeter_of_rectangles",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": "P = 2l + 12 and P = 32 cm",
        "sample_answer": "P = 2l + 12 and P = 32 cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_26",
        "hints": {"tier_1": "Substitute breadth 6 into P = 2l + 2b.", "tier_2": "P = 2l + 12, P(10) = 32.", "tier_3": "P = 2l + 12 and P = 32 cm"},
        "misconception_tags": ["perimeter_formula_substitution_slip"]
    }


# 27. Relationship formula cost of hiring hall fixed plus hourly
def arch_27_relationship_formula_cost_of_hiring_hall_fixed_plus_hourly(rng: random.Random) -> Dict[str, Any]:
    # Hall hire: R500 deposit + R120 per hour. C = 500 + 120h. For 5 hours -> 500 + 600 = R1100
    ans = "R1 100"
    prompt = (
        "A community hall charges a fixed booking fee of R500 plus R120 per hour of use.\n\n"
        "1. State the algebraic formula for total hiring cost \\(C\\) in terms of hours \\(h\\).\n"
        "2. Calculate the cost to hire the hall for 5 hours."
    )
    sol = (
        "**Step 1: Formula:**\n"
        "$$C = 120h + 500$$\n\n"
        "**Step 2: Calculation for \\(h = 5\\):**\n"
        "$$C = 120(5) + 500 = 600 + 500 = \\mathbf{\\text{R1 100}}$$"
    )
    return {
        "id": f"g7_rel_27_{rng.randint(100000, 999999)}",
        "subskill": "27_relationship_formula_cost_of_hiring_hall_fixed_plus_hourly",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_27",
        "hints": {"tier_1": "120 * 5 = 600.", "tier_2": "600 + 500 = 1 100.", "tier_3": ans},
        "misconception_tags": ["fixed_fee_addition_error"]
    }


# 28. Relationship formula water consumption billing
def arch_28_relationship_formula_water_consumption_billing(rng: random.Random) -> Dict[str, Any]:
    # Monthly network fee R80 + R15 per kilolitre (kL). C = 80 + 15k. For 12 kL -> 80 + 180 = R260
    ans = "R260"
    prompt = (
        "A municipality charges a monthly water service charge of R80 plus R15 per kilolitre (kL) consumed.\n\n"
        "Calculate the monthly water bill for a household that used 12 kL of water."
    )
    sol = (
        "**Step 1:** Formula: \\(C = 15k + 80\\)\n\n"
        "**Step 2:** For \\(k = 12\\):\n"
        "$$C = 15(12) + 80 = 180 + 80 = \\mathbf{\\text{R260}}$$"
    )
    return {
        "id": f"g7_rel_28_{rng.randint(100000, 999999)}",
        "subskill": "28_relationship_formula_water_consumption_billing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_28",
        "hints": {"tier_1": "15 * 12 = 180.", "tier_2": "180 + 80 = 260.", "tier_3": ans},
        "misconception_tags": ["utility_billing_arithmetic_slip"]
    }


# 29. Relationship formula electricity units and cost
def arch_29_relationship_formula_electricity_units_and_cost(rng: random.Random) -> Dict[str, Any]:
    # Prepaid electricity: R2,50 per kWh. Cost of 150 kWh = 150 * 2,50 = R375
    ans = "R375"
    prompt = (
        "Prepaid electricity costs R2,50 per kilowatt-hour (kWh).\n\n"
        "Calculate the total cost to purchase 150 kWh of electricity."
    )
    sol = (
        "**Step 1:** Multiply units by rate per unit:\n"
        "$$\\text{Cost} = 150 \\times 2,50 = 150 \\times 2 + 150 \\times 0,50 = 300 + 75 = \\mathbf{\\text{R375}}$$"
    )
    return {
        "id": f"g7_rel_29_{rng.randint(100000, 999999)}",
        "subskill": "29_relationship_formula_electricity_units_and_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_29",
        "hints": {"tier_1": "150 * 2,50.", "tier_2": "300 + 75 = 375.", "tier_3": ans},
        "misconception_tags": ["decimal_rate_multiplication_error"]
    }


# 30. Relationship formula distance from speed and time
def arch_30_relationship_formula_distance_from_speed_and_time(rng: random.Random) -> Dict[str, Any]:
    # Speed s = 65 km/h. Formula d = 65t. Distance in 4 hours = 260 km
    ans = "260 km"
    prompt = (
        "A bus travels at a constant average speed of 65 km/h.\n\n"
        "1. Write the relationship formula for distance \\(d\\) in terms of time \\(t\\).\n"
        "2. Calculate the distance covered in 4 hours."
    )
    sol = (
        "**Step 1: Formula:** \\(d = 65t\\)\n\n"
        "**Step 2: Calculation for \\(t = 4\\):**\n"
        "$$d = 65 \\times 4 = \\mathbf{260\\text{ km}}$$"
    )
    return {
        "id": f"g7_rel_30_{rng.randint(100000, 999999)}",
        "subskill": "30_relationship_formula_distance_from_speed_and_time",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_30",
        "hints": {"tier_1": "65 * 4.", "tier_2": "260 km.", "tier_3": ans},
        "misconception_tags": ["speed_time_distance_formula_mixup"]
    }


# 31. Relationship formula converting temperature celsius fahrenheit concept
def arch_31_relationship_formula_converting_temperature_celsius_fahrenheit_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the relationship between Celsius (\\(C\\)) and Fahrenheit (\\(F\\)) temperatures:\n"
        "When \\(C = 0^\\circ\\text{C}\\), \\(F = 32^\\circ\\text{F}\\).\n\n"
        "Is the relationship between Celsius and Fahrenheit directly proportional? Explain why or why not."
    )
    sol = (
        "**Analysis:**\n"
        "Direct proportion requires that when the input is zero, the output must also be zero (line passes through the origin).\n\n"
        "Since \\(0^\\circ\\text{C} = 32^\\circ\\text{F} \\neq 0\\), the relationship is **not directly proportional**."
    )
    ans = "No, because 0 °C does not correspond to 0 °F"
    return {
        "id": f"g7_rel_31_{rng.randint(100000, 999999)}",
        "subskill": "31_relationship_formula_converting_temperature_celsius_fahrenheit_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_31",
        "hints": {"tier_1": "Does it pass through (0, 0)?", "tier_2": "When C = 0, F = 32.", "tier_3": ans},
        "misconception_tags": ["confusing_linear_temperature_with_proportional"]
    }


# 32. Relationship formula mass and volume density concept
def arch_32_relationship_formula_mass_and_volume_density_concept(rng: random.Random) -> Dict[str, Any]:
    # Pure water: 1 litre has mass 1 kg. 12,5 litres has mass 12,5 kg. Directly proportional!
    ans = "12,5 kg"
    prompt = (
        "Fresh water has a density of 1 kg per litre (\\(M = 1V\\)).\n\n"
        "1. What is the mass of 12,5 litres of pure water?\n"
        "2. Is the relationship between volume and mass of water directly proportional?"
    )
    sol = (
        "**Step 1:** \\(M = 1 \\times 12,5 = \\mathbf{12,5\\text{ kg}}\\)\n\n"
        "**Step 2:** Yes, it is directly proportional because 0 litres has 0 kg mass, and the ratio \\(\\frac{M}{V} = 1\\) is constant."
    )
    return {
        "id": f"g7_rel_32_{rng.randint(100000, 999999)}",
        "subskill": "32_relationship_formula_mass_and_volume_density_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_32",
        "hints": {"tier_1": "1 litre = 1 kg.", "tier_2": "12,5 litres = 12,5 kg.", "tier_3": ans},
        "misconception_tags": ["density_proportionality_slip"]
    }


# 33. Variable relationship direct proportion multiplication factor
def arch_33_variable_relationship_direct_proportion_multiplication_factor(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "If two variables \\(x\\) and \\(y\\) are in **direct proportion**, "
        "what happens to \\(y\\) when \\(x\\) is multiplied by 3?"
    )
    sol = (
        "**Property of Direct Proportion:**\n"
        "In a directly proportional relationship (\\(y = kx\\)), whatever factor the input \\(x\\) is multiplied by, "
        "the output \\(y\\) is multiplied by that exact same factor.\n\n"
        "**Answer:** \\(y\\) is also **multiplied by 3** (tripled)."
    )
    ans = "y is multiplied by 3 (tripled)"
    return {
        "id": f"g7_rel_33_{rng.randint(100000, 999999)}",
        "subskill": "33_variable_relationship_direct_proportion_multiplication_factor",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_33",
        "hints": {"tier_1": "Direct proportion scales by the same factor.", "tier_2": "Tripled (multiplied by 3).", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_multiplying_factor"]
    }


# 34. Variable relationship inverse proportion concept
def arch_34_variable_relationship_inverse_proportion_concept(rng: random.Random) -> Dict[str, Any]:
    # 2 workers take 12 hours. How long will 4 workers take? (2 * 12)/4 = 6 hours
    ans = "6 hours"
    prompt = (
        "Two painters take 12 hours to paint a boundary wall working at the same pace.\n\n"
        "How many hours will it take 4 painters to complete the same wall?"
    )
    sol = (
        "**Step 1:** Total work in painter-hours:\n"
        "$$\\text{Work} = 2 \\times 12 = 24\\text{ painter-hours}$$\n\n"
        "**Step 2:** With 4 painters:\n"
        "$$\\text{Time} = \\frac{24}{4} = \\mathbf{6\\text{ hours}}$$\n\n"
        "*(As the number of workers doubles, the time taken is halved: inverse proportion)*."
    )
    return {
        "id": f"g7_rel_34_{rng.randint(100000, 999999)}",
        "subskill": "34_variable_relationship_inverse_proportion_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_34",
        "hints": {"tier_1": "More workers take less time.", "tier_2": "24 / 4 = 6 hours.", "tier_3": ans},
        "misconception_tags": ["treating_worker_time_as_direct_proportion"]
    }


# 35. Variable relationship identifying non relationships
def arch_35_variable_relationship_identifying_non_relationships(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider two quantities:\n"
        "Quantity 1: A learner's shoe size\n"
        "Quantity 2: Their score on a Grade 7 Mathematics exam\n\n"
        "Is there a mathematical relationship between these two variables? Explain."
    )
    sol = (
        "**Analysis:**\n"
        "Shoe size has no causal or mathematical connection to mathematical ability or test marks.\n\n"
        "**Conclusion:** **No**, there is no mathematical relationship; they are independent, unrelated variables."
    )
    ans = "No relationship exists between shoe size and test marks"
    return {
        "id": f"g7_rel_35_{rng.randint(100000, 999999)}",
        "subskill": "35_variable_relationship_identifying_non_relationships",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_35",
        "hints": {"tier_1": "Does foot size affect math ability?", "tier_2": "No mathematical relationship.", "tier_3": ans},
        "misconception_tags": ["assuming_all_pairs_of_variables_are_related"]
    }


# 36. Variable relationship evaluating at zero starting value
def arch_36_variable_relationship_evaluating_at_zero_starting_value(rng: random.Random) -> Dict[str, Any]:
    # Cost equation: C = 45x + 120. When x = 0, C = 120
    ans = "R120"
    prompt = (
        "The cost formula for an internet contract is \\(C = 45x + 120\\), where \\(x\\) is extra data packages added.\n\n"
        "What is the starting baseline cost when zero extra data packages are added (\\(x = 0\\))?"
    )
    sol = (
        "**Step 1:** Substitute \\(x = 0\\):\n"
        "$$C = 45(0) + 120 = 0 + 120 = \\mathbf{\\text{R120}}$$"
    )
    return {
        "id": f"g7_rel_36_{rng.randint(100000, 999999)}",
        "subskill": "36_variable_relationship_evaluating_at_zero_starting_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_36",
        "hints": {"tier_1": "Set x = 0.", "tier_2": "C = R120.", "tier_3": ans},
        "misconception_tags": ["zero_input_evaluation_slip"]
    }


# 37. Variable relationship determining rate of change
def arch_37_variable_relationship_determining_rate_of_change(rng: random.Random) -> Dict[str, Any]:
    # Fuel consumption: Tank has 60 L. After driving 100 km, has 52 L. Rate of consumption = (60-52)/100 = 0,08 L/km
    ans = "0,08 L/km"
    prompt = (
        "A car starts with 60 litres of petrol. After driving 100 km, 52 litres remain in the tank.\n\n"
        "Calculate the fuel consumption rate in litres per kilometre (L/km)."
    )
    sol = (
        "**Step 1:** Petrol used: $$60 - 52 = 8\\text{ litres}$$\n\n"
        "**Step 2:** Rate per kilometre:\n"
        "$$\\text{Rate} = \\frac{8\\text{ L}}{100\\text{ km}} = \\mathbf{0,08\\text{ L/km}}$$"
    )
    return {
        "id": f"g7_rel_37_{rng.randint(100000, 999999)}",
        "subskill": "37_variable_relationship_determining_rate_of_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_37",
        "hints": {"tier_1": "8 litres used over 100 km.", "tier_2": "8 / 100 = 0,08.", "tier_3": ans},
        "misconception_tags": ["rate_per_unit_division_error"]
    }


# 38. Variable relationship rate of change units interpretation
def arch_38_variable_relationship_rate_of_change_units_interpretation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a formula where cost \\(C\\) is in South African Rand and time \\(t\\) is in hours:\n\n"
        "What are the compound units for the rate of change \\(\\frac{\\Delta C}{\\Delta t}\\)?"
    )
    sol = (
        "**Step 1:** Units of numerator: Rand (R).\n\n"
        "**Step 2:** Units of denominator: Hours (h).\n\n"
        "**Compound Unit:** **Rand per hour (R/h)**."
    )
    ans = "Rand per hour (R/h)"
    return {
        "id": f"g7_rel_38_{rng.randint(100000, 999999)}",
        "subskill": "38_variable_relationship_rate_of_change_units_interpretation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_38",
        "hints": {"tier_1": "Divide currency by time.", "tier_2": "Rand per hour.", "tier_3": ans},
        "misconception_tags": ["rate_units_inversion"]
    }


# 39. Variable relationship positive correlation statement
def arch_39_variable_relationship_positive_correlation_statement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "As the temperature outside increases during summer, ice cream sales at a beach kiosk also increase.\n\n"
        "Does this describe a **positive relationship** or a **negative relationship**? Explain."
    )
    sol = (
        "**Analysis:**\n"
        "When both variables increase together (as \\(x\\) rises, \\(y\\) also rises), "
        "the relationship is **positive**."
    )
    ans = "Positive relationship"
    return {
        "id": f"g7_rel_39_{rng.randint(100000, 999999)}",
        "subskill": "39_variable_relationship_positive_correlation_statement",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_39",
        "hints": {"tier_1": "Both variables move in the same direction.", "tier_2": "Positive relationship.", "tier_3": ans},
        "misconception_tags": ["correlation_direction_confusion"]
    }


# 40. Variable relationship negative correlation statement
def arch_40_variable_relationship_negative_correlation_statement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "As a car travels faster and speed increases, the travel time required to reach a fixed destination decreases.\n\n"
        "Is this a **positive** or a **negative** relationship?"
    )
    sol = (
        "**Analysis:**\n"
        "When an increase in one variable leads to a decrease in the other variable, "
        "the relationship is **negative** (or inverse)."
    )
    ans = "Negative relationship"
    return {
        "id": f"g7_rel_40_{rng.randint(100000, 999999)}",
        "subskill": "40_variable_relationship_negative_correlation_statement",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_40",
        "hints": {"tier_1": "One goes up while the other goes down.", "tier_2": "Negative relationship.", "tier_3": ans},
        "misconception_tags": ["negative_relationship_definition_slip"]
    }


# 41. Variable relationship finding value from graph story
def arch_41_variable_relationship_finding_value_from_graph_story(rng: random.Random) -> Dict[str, Any]:
    # Candle burns down from 20 cm at 2 cm per hour: H = 20 - 2t. Height at t = 6h -> 20 - 12 = 8 cm
    ans = "8 cm"
    prompt = (
        "A burning candle is 20 cm tall initially and burns down at a rate of 2 cm per hour (\\(H = 20 - 2t\\)).\n\n"
        "Calculate the remaining height of the candle after 6 hours."
    )
    sol = (
        "**Step 1:** Burned height: $$6 \\times 2 = 12\\text{ cm}$$\n\n"
        "**Step 2:** Remaining height:\n"
        "$$H = 20 - 12 = \\mathbf{8\\text{ cm}}$$"
    )
    return {
        "id": f"g7_rel_41_{rng.randint(100000, 999999)}",
        "subskill": "41_variable_relationship_finding_value_from_graph_story",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_41",
        "hints": {"tier_1": "20 - 2(6).", "tier_2": "20 - 12 = 8.", "tier_3": ans},
        "misconception_tags": ["candle_burning_subtraction_slip"]
    }


# 42. Variable relationship identifying break even value
def arch_42_variable_relationship_identifying_break_even_value(rng: random.Random) -> Dict[str, Any]:
    # Production cost C = 100 + 5n. Selling revenue R = 15n. Break-even when 15n = 100 + 5n -> 10n = 100 -> n = 10
    ans = "10 items"
    prompt = (
        "A student makes bead necklaces:\n"
        "- Production cost: \\(C = 100 + 5n\\) (where R100 is for tools, R5 per necklace for beads)\n"
        "- Selling revenue: \\(R = 15n\\) (sold at R15 each)\n\n"
        "How many necklaces \\(n\\) must be sold to break even (where revenue equals cost)?"
    )
    sol = (
        "**Step 1:** Set Revenue equal to Cost:\n"
        "$$15n = 100 + 5n$$\n\n"
        "**Step 2:** Subtract \\(5n\\) from both sides:\n"
        "$$10n = 100$$\n\n"
        "**Step 3:** Solve for \\(n\\):\n"
        "$$n = \\frac{100}{10} = \\mathbf{10\\text{ necklaces}}$$"
    )
    return {
        "id": f"g7_rel_42_{rng.randint(100000, 999999)}",
        "subskill": "42_variable_relationship_identifying_break_even_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_rel_42",
        "hints": {"tier_1": "Solve 15n = 100 + 5n.", "tier_2": "10n = 100.", "tier_3": ans},
        "misconception_tags": ["break_even_equation_solving_slip"]
    }


# 43. Variable relationship comparing rates of two linear models
def arch_43_variable_relationship_comparing_rates_of_two_linear_models(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Company A charges \\(C = 12x + 50\\) and Company B charges \\(C = 16x + 20\\).\n\n"
        "1. Which company has the cheaper starting fee?\n"
        "2. Which company has the cheaper rate per unit \\(x\\)?"
    )
    sol = (
        "**Step 1: Starting fees (constants):**\n"
        "Company A: R50; Company B: R20. **Company B** has the cheaper starting fee.\n\n"
        "**Step 2: Rates per unit (coefficients of \\(x\\)):**\n"
        "Company A: R12; Company B: R16. **Company A** has the cheaper rate per unit.\n\n"
        "**Summary:** 1. Company B; 2. Company A"
    )
    ans = "1. Company B; 2. Company A"
    return {
        "id": f"g7_rel_43_{rng.randint(100000, 999999)}",
        "subskill": "43_variable_relationship_comparing_rates_of_two_linear_models",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_43",
        "hints": {"tier_1": "Compare the fixed constants, then compare the rates.", "tier_2": "1. Company B; 2. Company A.", "tier_3": ans},
        "misconception_tags": ["confusing_rate_and_initial_fee"]
    }


# 44. Variable relationship fractional rate per unit
def arch_44_variable_relationship_fractional_rate_per_unit(rng: random.Random) -> Dict[str, Any]:
    # Rule y = 3/4 x. For x = 12 -> y = 9
    ans = "9"
    prompt = (
        "The relationship between two variables is \\(y = \\frac{3}{4}x\\).\n\n"
        "Calculate \\(y\\) when \\(x = 12\\)."
    )
    sol = (
        "**Step 1:** Multiply 12 by \\(\\frac{3}{4}\\):\n"
        "$$y = \\frac{3}{4} \\times 12 = \\frac{36}{4} = \\mathbf{9}$$"
    )
    return {
        "id": f"g7_rel_44_{rng.randint(100000, 999999)}",
        "subskill": "44_variable_relationship_fractional_rate_per_unit",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_44",
        "hints": {"tier_1": "Divide 12 by 4, then multiply by 3.", "tier_2": "3 * 3 = 9.", "tier_3": ans},
        "misconception_tags": ["fraction_multiplication_slip"]
    }


# 45. Variable relationship decimal rate per unit
def arch_45_variable_relationship_decimal_rate_per_unit(rng: random.Random) -> Dict[str, Any]:
    # y = 1,25x. For x = 8 -> 1,25 * 8 = 10
    ans = "10"
    prompt = (
        "A machine produces goods at a rate of \\(y = 1,25x\\).\n\n"
        "Calculate the output \\(y\\) when the input is \\(x = 8\\)."
    )
    sol = (
        "**Step 1:** Multiply 8 by 1,25:\n"
        "$$1,25 \\times 8 = \\frac{5}{4} \\times 8 = 5 \\times 2 = \\mathbf{10}$$"
    )
    return {
        "id": f"g7_rel_45_{rng.randint(100000, 999999)}",
        "subskill": "45_variable_relationship_decimal_rate_per_unit",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_45",
        "hints": {"tier_1": "1,25 * 8.", "tier_2": "10.", "tier_3": ans},
        "misconception_tags": ["decimal_rate_multiplication_slip"]
    }


# 46. Variable relationship identifying input restrictions domain
def arch_46_variable_relationship_identifying_input_restrictions_domain(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A taxi charges \\(C = 15k + 20\\), where \\(k\\) is the distance traveled in kilometres.\n\n"
        "Can the input variable \\(k\\) take on negative values (e.g. \\(k = -5\\))? Explain."
    )
    sol = (
        "**Analysis:**\n"
        "Distance is a physical measurement that cannot be negative (\\(k \\ge 0\\)).\n\n"
        "**Conclusion:** **No**, physical distance cannot be negative, so the domain is restricted to non-negative numbers."
    )
    ans = "No, distance cannot be negative"
    return {
        "id": f"g7_rel_46_{rng.randint(100000, 999999)}",
        "subskill": "46_variable_relationship_identifying_input_restrictions_domain",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_46",
        "hints": {"tier_1": "Can distance be less than zero?", "tier_2": "Distance cannot be negative.", "tier_3": ans},
        "misconception_tags": ["ignoring_real_world_domain_constraints"]
    }


# 47. Variable relationship identifying output restrictions range
def arch_47_variable_relationship_identifying_output_restrictions_range(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the formula \\(y = x^2\\), what kind of numbers can the output \\(y\\) be if \\(x\\) is any integer?\n\n"
        "Can \\(y\\) ever be negative?"
    )
    sol = (
        "**Analysis:**\n"
        "Squaring any real integer (positive, negative, or zero) always yields a non-negative result:\n"
        "- Positive \\(\\times\\) positive = positive\n"
        "- Negative \\(\\times\\) negative = positive\n"
        "- \\(0^2 = 0\\)\n\n"
        "**Conclusion:** **No**, \\(y\\) can never be negative (\\(y \\ge 0\\))."
    )
    ans = "No, y can never be negative"
    return {
        "id": f"g7_rel_47_{rng.randint(100000, 999999)}",
        "subskill": "47_variable_relationship_identifying_output_restrictions_range",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_rel_47",
        "hints": {"tier_1": "What is (-3) * (-3)?", "tier_2": "Squares are always non-negative.", "tier_3": ans},
        "misconception_tags": ["squaring_negative_sign_confusion"]
    }


# 48. Variable relationship detecting misleading assumed causation
def arch_48_variable_relationship_detecting_misleading_assumed_causation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A study observes that towns with more ice cream shops also have higher rates of drowning incidents.\n\n"
        "Does eating ice cream cause people to drown? Explain what underlying variable connects them."
    )
    sol = (
        "**Analysis:**\n"
        "Correlation does not imply causation. Eating ice cream does not cause drowning.\n\n"
        "**Underlying variable:**\n"
        "**Hot summer weather** causes both more ice cream sales and more people swimming in rivers/pools, "
        "which increases exposure to drowning."
    )
    ans = "No, hot weather causes both more swimming and more ice cream eating"
    return {
        "id": f"g7_rel_48_{rng.randint(100000, 999999)}",
        "subskill": "48_variable_relationship_detecting_misleading_assumed_causation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_48",
        "hints": {"tier_1": "What third factor happens in summer?", "tier_2": "Hot summer weather.", "tier_3": ans},
        "misconception_tags": ["confusing_correlation_with_causation"]
    }


# 49. Variable relationship algebraic rearrangement for input
def arch_49_variable_relationship_algebraic_rearrangement_for_input(rng: random.Random) -> Dict[str, Any]:
    # Perimeter of rectangle with fixed width 5: P = 2l + 10. Rearrange for l: 2l = P - 10 -> l = (P - 10)/2
    ans = "l = (P - 10)/2"
    prompt = (
        "The perimeter formula for a rectangle with width 5 is \\(P = 2l + 10\\).\n\n"
        "Rearrange this formula to make length \\(l\\) the subject."
    )
    sol = (
        "**Step 1:** Subtract 10 from both sides:\n"
        "$$P - 10 = 2l$$\n\n"
        "**Step 2:** Divide both sides by 2:\n"
        "$$l = \\mathbf{\\frac{P - 10}{2}}$$"
    )
    return {
        "id": f"g7_rel_49_{rng.randint(100000, 999999)}",
        "subskill": "49_variable_relationship_algebraic_rearrangement_for_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_rel_49",
        "hints": {"tier_1": "Subtract 10, then divide by 2.", "tier_2": "l = (P - 10)/2.", "tier_3": ans},
        "misconception_tags": ["formula_rearrangement_operation_order"]
    }


# 50. Variable relationship comprehensive three phase autopsy
def arch_50_variable_relationship_comprehensive_three_phase_autopsy(rng: random.Random) -> Dict[str, Any]:
    # Scenario: Plant nursery charges R25 per tree plus delivery fee of R150.
    # 1. Formula: C = 25n + 150
    # 2. Cost of 18 trees -> 25(18) + 150 = 450 + 150 = R600
    # 3. If customer has R900: 25n + 150 = 900 -> 25n = 750 -> n = 30 trees
    ans = "1. C = 25n + 150; 2. R600; 3. 30 trees"
    prompt = (
        "A plant nursery charges R25 per fruit tree sapling plus a fixed delivery fee of R150.\n\n"
        "Complete a three-phase diagnostic investigation:\n"
        "1. Write the formula for total cost \\(C\\) in terms of saplings \\(n\\).\n"
        "2. Calculate the total cost to buy and deliver 18 saplings.\n"
        "3. Determine how many saplings a community garden bought if their total invoice was R900."
    )
    sol = (
        "**Phase 1: Formula:**\n"
        "$$C = 25n + 150$$\n\n"
        "**Phase 2: Cost of 18 saplings:**\n"
        "$$C = 25(18) + 150 = 450 + 150 = \\mathbf{\\text{R600}}$$\n\n"
        "**Phase 3: Inverse solve for \\(n\\) given \\(C = 900\\):**\n"
        "$$25n + 150 = 900$$\n"
        "$$25n = 750$$\n"
        "$$n = \\frac{750}{25} = \\mathbf{30\\text{ saplings}}$$\n\n"
        "**Summary:** 1. \\(C = 25n + 150\\); 2. \\(\\text{R600}\\); 3. \\(30\\text{ trees}\\)"
    )
    return {
        "id": f"g7_rel_50_{rng.randint(100000, 999999)}",
        "subskill": "50_variable_relationship_comprehensive_three_phase_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_rel_50",
        "hints": {"tier_1": "1: 25n + 150; 2: 25(18)+150; 3: (900-150)/25.", "tier_2": "C = 25n + 150, R600, 30 trees.", "tier_3": ans},
        "misconception_tags": ["comprehensive_variable_relationship_autopsy_slip"]
    }
