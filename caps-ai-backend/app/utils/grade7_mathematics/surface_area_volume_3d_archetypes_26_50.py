"""Grade 7 Mathematics - Surface Area and Volume of 3D Objects: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/01. Surface area and volume of 3D objects.md
Focus: Capacity conversions (litres, ml, kl), word problems (fish tanks, pools, painting, packaging), dimensional scaling, composite solids, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Capacity conversion cm3 to litres
def arch_26_capacity_conversion_cm3_to_litres(rng: random.Random) -> Dict[str, Any]:
    litres = rng.choice([2, 3, 4, 5, 8])
    cm3 = litres * 1000
    ans = f"{litres} litres"
    prompt = (
        f"A rectangular container has an internal volume of \\({cm3}\\text{{ cm}}^3\\).\n\n"
        f"Convert this volume into **litres**."
    )
    sol = (
        f"**Step 1:** Recall that \\(1\\text{{ litre}} = 1000\\text{{ cm}}^3\\).\n\n"
        f"**Step 2:** Divide by 1 000:\n"
        f"$$\\frac{{{cm3}}}{{1000}} = \\mathbf{{{litres}}}\\text{{ litres}}$$"
    )
    return {
        "id": f"g7_sav_26_{rng.randint(100000, 999999)}",
        "subskill": "26_capacity_conversion_cm3_to_litres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_26",
        "hints": {"tier_1": "1 litre = 1000 cm^3.", "tier_2": f"{cm3} / 1000 = {litres}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_hundred_instead_of_thousand_for_litres"]
    }


# 27. Capacity conversion litres to cm3
def arch_27_capacity_conversion_litres_to_cm3(rng: random.Random) -> Dict[str, Any]:
    ans = "3 500 cm^3"
    prompt = (
        "Convert \\(3{,}5\\text{ litres}\\) of water to cubic centimetres (\\(\\text{cm}^3\\))."
    )
    sol = (
        "**Step 1:** Multiply by 1 000 because \\(1\\text{ l} = 1\\,000\\text{ cm}^3\\):\n"
        "$$3{,}5 \\times 1\\,000 = \\mathbf{3\\,500}\\text{ cm}^3$$"
    )
    return {
        "id": f"g7_sav_27_{rng.randint(100000, 999999)}",
        "subskill": "27_capacity_conversion_litres_to_cm3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_sav_27",
        "hints": {"tier_1": "Multiply by 1000.", "tier_2": "3,5 × 1000 = 3500.", "tier_3": ans},
        "misconception_tags": ["decimal_multiplication_zero_omission"]
    }


# 28. Capacity conversion m3 to litres
def arch_28_capacity_conversion_m3_to_litres(rng: random.Random) -> Dict[str, Any]:
    m3 = rng.choice([2, 3, 5, 8])
    litres = m3 * 1000
    ans = f"{litres} litres"
    prompt = (
        f"A municipal water reservoir holds \\({m3}\\text{{ m}}^3\\) of water.\n\n"
        f"Determine how many litres of water this represents."
    )
    sol = (
        f"**Step 1:** Remember that \\(1\\text{{ m}}^3 = 1\\,000\\text{{ litres}}\\) (or \\(1\\text{{ kl}}\\)).\n\n"
        f"**Step 2:** Multiply by 1 000:\n"
        f"$${m3} \\times 1\\,000 = \\mathbf{{{litres}}}\\text{{ litres}}$$"
    )
    return {
        "id": f"g7_sav_28_{rng.randint(100000, 999999)}",
        "subskill": "28_capacity_conversion_m3_to_litres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_28",
        "hints": {"tier_1": "1 m^3 = 1000 litres.", "tier_2": f"{m3} × 1000 = {litres}.", "tier_3": ans},
        "misconception_tags": ["confusing_m3_to_litre_conversion_factor"]
    }


# 29. Capacity conversion litres to m3
def arch_29_capacity_conversion_litres_to_m3(rng: random.Random) -> Dict[str, Any]:
    ans = "4,5 m^3"
    prompt = (
        "Convert \\(4\\,500\\text{ litres}\\) to cubic metres (\\(\\text{m}^3\\))."
    )
    sol = (
        "**Step 1:** Divide by 1 000:\n"
        "$$\\frac{4\\,500}{1\\,000} = \\mathbf{4{,}5}\\text{ m}^3$$"
    )
    return {
        "id": f"g7_sav_29_{rng.randint(100000, 999999)}",
        "subskill": "29_capacity_conversion_litres_to_m3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_29",
        "hints": {"tier_1": "Divide by 1000.", "tier_2": "4500 / 1000 = 4,5.", "tier_3": ans},
        "misconception_tags": ["dividing_by_ten_thousand"]
    }


# 30. Capacity conversion m3 to kilolitres
def arch_30_capacity_conversion_m3_to_kilolitres(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([4, 6, 8, 12, 15])
    ans = f"{k} kl"
    prompt = (
        f"A storage silo has a capacity of \\({k}\\text{{ m}}^3\\).\n\n"
        f"Convert this capacity into **kilolitres** (\\(\\text{{kl}}\\))."
    )
    sol = (
        f"**Step 1:** \\(1\\text{{ m}}^3 = 1\\,000\\text{{ l}} = 1\\text{{ kl}}\\).\n\n"
        f"**Step 2:** Therefore:\n"
        f"$${k}\\text{{ m}}^3 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_sav_30_{rng.randint(100000, 999999)}",
        "subskill": "30_capacity_conversion_m3_to_kilolitres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_sav_30",
        "hints": {"tier_1": "1 m^3 = 1 kl.", "tier_2": f"{k} m^3 = {k} kl.", "tier_3": ans},
        "misconception_tags": ["multiplying_m3_by_thousand_when_converting_to_kl"]
    }


# 31. Word problem fish tank capacity litres
def arch_31_word_problem_fish_tank_capacity_litres(rng: random.Random) -> Dict[str, Any]:
    l = 60
    b = 40
    h = 30
    vol = l * b * h  # 72000 cm^3
    litres = vol // 1000  # 72 litres
    ans = f"{litres} litres"
    prompt = (
        f"A rectangular glass fish tank measures \\({l}\\text{{ cm}}\\) long, \\({b}\\text{{ cm}}\\) wide, "
        f"and \\({h}\\text{{ cm}}\\) high.\n\n"
        f"1. Calculate the volume of the tank in \\(\\text{{cm}}^3\\).\n"
        f"2. Determine how many litres of water it holds when completely full."
    )
    sol = (
        f"**Step 1:** Calculate volume in \\(\\text{{cm}}^3\\):\n"
        f"$$V = {l} \\times {b} \\times {h} = {l * b} \\times {h} = {vol}\\text{{ cm}}^3$$\n\n"
        f"**Step 2:** Convert to litres by dividing by 1 000:\n"
        f"$$\\text{{Capacity}} = \\frac{{{vol}}}{{1000}} = \\mathbf{{{litres}}}\\text{{ litres}}$$"
    )
    return {
        "id": f"g7_sav_31_{rng.randint(100000, 999999)}",
        "subskill": "31_word_problem_fish_tank_capacity_litres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_31",
        "hints": {"tier_1": f"Volume = {l} × {b} × {h} cm^3.", "tier_2": "Divide cm^3 by 1000 to get litres.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_convert_cm3_to_litres"]
    }


# 32. Word problem swimming pool capacity m3 litres
def arch_32_word_problem_swimming_pool_capacity_m3_litres(rng: random.Random) -> Dict[str, Any]:
    l = 10
    w = 5
    d = 1.5
    vol = round(l * w * d, 1)  # 75.0 m^3
    litres = int(vol * 1000)  # 75000 litres
    ans = f"Volume: 75 m^3; Capacity: 75 000 litres"
    prompt = (
        "A rectangular swimming pool has a uniform depth of \\(1{,}5\\text{ m}\\), length \\(10\\text{ m}\\), "
        "and width \\(5\\text{ m}\\).\n\n"
        "1. Find the volume of the pool in \\(\\text{m}^3\\).\n"
        "2. What is the capacity of the pool in litres?"
    )
    sol = (
        "**Step 1:** Volume in \\(\\text{m}^3\\):\n"
        "$$V = 10 \\times 5 \\times 1{,}5 = 50 \\times 1{,}5 = \\mathbf{75}\\text{ m}^3$$\n\n"
        "**Step 2:** Capacity in litres (\\(1\\text{ m}^3 = 1\\,000\\text{ litres}\\)):\n"
        "$$\\text{Capacity} = 75 \\times 1\\,000 = \\mathbf{75\\,000}\\text{ litres}$$"
    )
    return {
        "id": f"g7_sav_32_{rng.randint(100000, 999999)}",
        "subskill": "32_word_problem_swimming_pool_capacity_m3_litres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_32",
        "hints": {"tier_1": "10 × 5 × 1,5 = 75 m^3.", "tier_2": "75 × 1000 = 75 000 litres.", "tier_3": ans},
        "misconception_tags": ["decimal_depth_multiplication_error"]
    }


# 33. Word problem water tank rate of filling
def arch_33_word_problem_water_tank_rate_of_filling(rng: random.Random) -> Dict[str, Any]:
    cap = 2000
    rate = 25
    time_mins = cap // rate  # 80 mins
    ans = f"{time_mins} minutes"
    prompt = (
        f"A rainwater tank has a capacity of \\({cap}\\text{{ litres}}\\).\n"
        f"A garden hose delivers water into the tank at a steady rate of \\({rate}\\text{{ litres per minute}}\\).\n\n"
        f"How many minutes will it take to fill the empty tank completely?"
    )
    sol = (
        f"**Step 1:** Use formula \\(\\text{{Time}} = \\frac{{\\text{{Capacity}}}}{{\\text{{Rate}}}}\\):\n"
        f"$$\\text{{Time}} = \\frac{{{cap}}}{{{rate}}} = \\mathbf{{{time_mins}}}\\text{{ minutes}}$$"
    )
    return {
        "id": f"g7_sav_33_{rng.randint(100000, 999999)}",
        "subskill": "33_word_problem_water_tank_rate_of_filling",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_33",
        "hints": {"tier_1": f"Divide {cap} by {rate}.", "tier_2": f"{cap} / {rate} = {time_mins}.", "tier_3": ans},
        "misconception_tags": ["multiplying_capacity_by_flow_rate"]
    }


# 34. Word problem painting outer walls surface area
def arch_34_word_problem_painting_outer_walls_surface_area(rng: random.Random) -> Dict[str, Any]:
    l = 6
    w = 4
    h = 3
    # 4 side walls only: 2lh + 2wh = 2(18) + 2(12) = 36 + 24 = 60 m^2
    lateral_sa = 2 * l * h + 2 * w * h
    ans = f"{lateral_sa} m^2"
    prompt = (
        f"The four vertical walls of a classroom measuring \\({l}\\text{{ m}}\\) long, \\({w}\\text{{ m}}\\) wide, "
        f"and \\({h}\\text{{ m}}\\) high need to be painted.\n"
        f"(The ceiling and floor are not painted).\n\n"
        f"Calculate the total area of the four walls to be painted."
    )
    sol = (
        f"**Step 1:** Lateral surface area = \\(2lh + 2wh\\):\n"
        f"- Two walls of \\({l} \\times {h}\\): \\(2({l * h}) = {2 * l * h}\\text{{ m}}^2\\)\n"
        f"- Two walls of \\({w} \\times {h}\\): \\(2({w * h}) = {2 * w * h}\\text{{ m}}^2\\)\n\n"
        f"**Step 2:** Sum: \\({2 * l * h} + {2 * w * h} = \\mathbf{{{lateral_sa}}}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_sav_34_{rng.randint(100000, 999999)}",
        "subskill": "34_word_problem_painting_outer_walls_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_34",
        "hints": {"tier_1": "Only calculate the 4 vertical walls (exclude floor and ceiling).", "tier_2": f"2({l*h}) + 2({w*h}) = {lateral_sa}.", "tier_3": ans},
        "misconception_tags": ["including_floor_and_ceiling_in_wall_painting_area"]
    }


# 35. Word problem packaging small boxes into carton
def arch_35_word_problem_packaging_small_boxes_into_carton(rng: random.Random) -> Dict[str, Any]:
    ans = "80 boxes"
    prompt = (
        "A large carton has dimensions \\(40\\text{ cm} \\times 20\\text{ cm} \\times 10\\text{ cm}\\).\n"
        "How many small matchboxes of dimensions \\(5\\text{ cm} \\times 4\\text{ cm} \\times 2\\text{ cm}\\) "
        "can fit into the carton with no empty space?"
    )
    sol = (
        "**Method 1: Fit along dimensions:**\n"
        "- Length: \\(40 \\div 5 = 8\\) boxes\n"
        "- Width: \\(20 \\div 4 = 5\\) boxes\n"
        "- Height: \\(10 \\div 2 = 5\\) boxes\n"
        "Wait, 8 × 5 × 5 = 200 boxes.\n\n"
        "Let's check volume: \\(V_1 = 40 \\times 20 \\times 10 = 8000\\text{ cm}^3\\).\n"
        "\\(V_2 = 5 \\times 4 \\times 2 = 40\\text{ cm}^3\\).\n"
        "$$\\text{Number of boxes} = \\frac{8000}{40} = \\mathbf{200}\\text{ boxes}$$"
    )
    return {
        "id": f"g7_sav_35_{rng.randint(100000, 999999)}",
        "subskill": "35_word_problem_packaging_small_boxes_into_carton",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": "200 boxes",
        "sample_answer": "200 boxes",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_35",
        "hints": {"tier_1": "Divide large carton volume by small box volume.", "tier_2": "8000 / 40 = 200.", "tier_3": "200 boxes"},
        "misconception_tags": ["dividing_by_sum_of_dimensions"]
    }


# 36. Word problem gift wrapping surface area
def arch_36_word_problem_gift_wrapping_surface_area(rng: random.Random) -> Dict[str, Any]:
    # Box 20 x 15 x 10 -> SA = 2(300 + 200 + 150) = 2(650) = 1300 cm^2. Plus 10% overlap = 1300 + 130 = 1430 cm^2
    ans = "1 430 cm^2"
    prompt = (
        "A gift box measures \\(20\\text{ cm} \\times 15\\text{ cm} \\times 10\\text{ cm}\\).\n"
        "Wrapping paper must cover the entire surface area, plus an extra \\(10\\%\\) for overlap and folds.\n\n"
        "Calculate the total area of wrapping paper required."
    )
    sol = (
        "**Step 1:** Calculate total surface area of the box:\n"
        "$$\\text{SA} = 2(20 \\times 15 + 20 \\times 10 + 15 \\times 10) = 2(300 + 200 + 150) = 2(650) = 1\\,300\\text{ cm}^2$$\n\n"
        "**Step 2:** Add 10% extra:\n"
        "$$\\text{Extra} = 0{,}10 \\times 1\\,300 = 130\\text{ cm}^2$$\n"
        "$$\\text{Total Paper} = 1\\,300 + 130 = \\mathbf{1\\,430}\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_sav_36_{rng.randint(100000, 999999)}",
        "subskill": "36_word_problem_gift_wrapping_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_36",
        "hints": {"tier_1": "Find SA = 1300 cm^2 first.", "tier_2": "Add 10% (130 cm^2).", "tier_3": ans},
        "misconception_tags": ["forgetting_to_add_percentage_overlap"]
    }


# 37. Effect of doubling dimensions on volume
def arch_37_effect_of_doubling_dimensions_on_volume(rng: random.Random) -> Dict[str, Any]:
    ans = "8 times larger (multiplied by 2^3 = 8)"
    prompt = (
        "If all three dimensions (length, width, height) of a rectangular prism are doubled, "
        "by what factor does its volume increase?"
    )
    sol = (
        "**Reasoning:**\n"
        "Original volume: \\(V_1 = l \\times b \\times h\\).\n"
        "New volume with doubled dimensions: \\(V_2 = (2l) \\times (2b) \\times (2h) = (2 \\times 2 \\times 2)(lbh) = 8(lbh) = 8V_1\\).\n\n"
        "The volume increases by **8 times** (or \\(2^3\\))."
    )
    return {
        "id": f"g7_sav_37_{rng.randint(100000, 999999)}",
        "subskill": "37_effect_of_doubling_dimensions_on_volume",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["2 times", "4 times", "6 times", "8 times"],
        "correct_answer": "8 times",
        "sample_answer": "8 times",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_37",
        "hints": {"tier_1": "2 × 2 × 2 = 8.", "tier_2": "Volume increases by 2^3.", "tier_3": "8 times"},
        "misconception_tags": ["thinking_volume_only_doubles_when_dimensions_double"]
    }


# 38. Effect of doubling dimensions on surface area
def arch_38_effect_of_doubling_dimensions_on_surface_area(rng: random.Random) -> Dict[str, Any]:
    ans = "4 times"
    prompt = (
        "If all dimensions of a cube are doubled, by what factor does its surface area increase?"
    )
    sol = (
        "**Reasoning:**\n"
        "Original surface area: \\(\\text{SA}_1 = 6s^2\\).\n"
        "New surface area: \\(\\text{SA}_2 = 6(2s)^2 = 6(4s^2) = 4(6s^2) = 4\\text{SA}_1\\).\n\n"
        "Surface area increases by **4 times** (or \\(2^2\\))."
    )
    return {
        "id": f"g7_sav_38_{rng.randint(100000, 999999)}",
        "subskill": "38_effect_of_doubling_dimensions_on_surface_area",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["2 times", "4 times", "6 times", "8 times"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_38",
        "hints": {"tier_1": "Area depends on the square: 2^2.", "tier_2": "4 times.", "tier_3": ans},
        "misconception_tags": ["confusing_area_scaling_factor_with_volume_scaling_factor"]
    }


# 39. Effect of tripling dimensions on volume
def arch_39_effect_of_tripling_dimensions_on_volume(rng: random.Random) -> Dict[str, Any]:
    ans = "27 times"
    prompt = (
        "If the length, breadth, and height of a rectangular prism are all multiplied by 3, "
        "how many times greater is the new volume?"
    )
    sol = (
        "**Reasoning:**\n"
        "$$\\text{Factor} = 3 \\times 3 \\times 3 = 3^3 = \\mathbf{27}\\text{ times}$$\n\n"
        "The new volume is **27 times** the original volume."
    )
    return {
        "id": f"g7_sav_39_{rng.randint(100000, 999999)}",
        "subskill": "39_effect_of_tripling_dimensions_on_volume",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["3 times", "9 times", "18 times", "27 times"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_39",
        "hints": {"tier_1": "3^3 = 27.", "tier_2": "Volume scales as cube of scale factor.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_nine_instead_of_twenty_seven"]
    }


# 40. Composite solid two prisms volume
def arch_40_composite_solid_two_prisms_volume(rng: random.Random) -> Dict[str, Any]:
    ans = "180 cm^3"
    prompt = (
        "A composite solid consists of two rectangular prisms stacked on top of each other:\n"
        "- Bottom prism: \\(8\\text{ cm} \\times 5\\text{ cm} \\times 3\\text{ cm}\\)\n"
        "- Top prism: \\(5\\text{ cm} \\times 4\\text{ cm} \\times 3\\text{ cm}\\)\n\n"
        "Calculate the total volume of the composite structure."
    )
    sol = (
        "**Step 1:** Calculate volume of bottom prism:\n"
        "$$V_1 = 8 \\times 5 \\times 3 = 120\\text{ cm}^3$$\n\n"
        "**Step 2:** Calculate volume of top prism:\n"
        "$$V_2 = 5 \\times 4 \\times 3 = 60\\text{ cm}^3$$\n\n"
        "**Step 3:** Add volumes:\n"
        "$$V_\\text{total} = 120 + 60 = \\mathbf{180}\\text{ cm}^3$$"
    )
    return {
        "id": f"g7_sav_40_{rng.randint(100000, 999999)}",
        "subskill": "40_composite_solid_two_prisms_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_40",
        "hints": {"tier_1": "Find V1 = 120 and V2 = 60.", "tier_2": "Add them: 120 + 60 = 180.", "tier_3": ans},
        "misconception_tags": ["composite_solid_addition_error"]
    }


# 41. Composite solid hollow prism volume
def arch_41_composite_solid_hollow_prism_volume(rng: random.Random) -> Dict[str, Any]:
    ans = "192 cm^3"
    prompt = (
        "A solid wooden block measures \\(8\\text{ cm} \\times 6\\text{ cm} \\times 5\\text{ cm}\\).\n"
        "A rectangular hole measuring \\(4\\text{ cm} \\times 3\\text{ cm}\\) is carved completely through its "
        "\\(4\\text{ cm}\\) depth (volume removed is \\(4 \\times 3 \\times 4 = 48\\text{ cm}^3\\)).\n"
        "If outer volume is \\(240\\text{ cm}^3\\), find remaining wood volume."
    )
    sol = (
        "**Step 1:** Outer volume = \\(240\\text{ cm}^3\\).\n"
        "**Step 2:** Hole volume = \\(48\\text{ cm}^3\\).\n\n"
        "**Step 3:** Subtract hole volume from outer volume:\n"
        "$$V = 240 - 48 = \\mathbf{192}\\text{ cm}^3$$"
    )
    return {
        "id": f"g7_sav_41_{rng.randint(100000, 999999)}",
        "subskill": "41_composite_solid_hollow_prism_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_41",
        "hints": {"tier_1": "Subtract carved volume from total volume.", "tier_2": "240 - 48 = 192.", "tier_3": ans},
        "misconception_tags": ["adding_hollow_cavity_instead_of_subtracting"]
    }


# 42. Liquid depth in rectangular container
def arch_42_liquid_depth_in_rectangular_container(rng: random.Random) -> Dict[str, Any]:
    ans = "12 cm"
    prompt = (
        "\\(12\\text{ litres}\\) (which equals \\(12\\,000\\text{ cm}^3\\)) of water is poured into a rectangular "
        "container whose base measures \\(40\\text{ cm} \\times 25\\text{ cm}\\).\n\n"
        "Calculate the depth \\(d\\) of the water in the container."
    )
    sol = (
        "**Step 1:** Calculate the base area of the container:\n"
        "$$\\text{Base Area} = 40 \\times 25 = 1\\,000\\text{ cm}^2$$\n\n"
        "**Step 2:** Divide liquid volume by base area to find depth:\n"
        "$$\\text{Depth } d = \\frac{12\\,000\\text{ cm}^3}{1\\,000\\text{ cm}^2} = \\mathbf{12}\\text{ cm}$$"
    )
    return {
        "id": f"g7_sav_42_{rng.randint(100000, 999999)}",
        "subskill": "42_liquid_depth_in_rectangular_container",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_42",
        "hints": {"tier_1": "12 litres = 12 000 cm^3. Base area = 1000 cm^2.", "tier_2": "12 000 / 1000 = 12.", "tier_3": ans},
        "misconception_tags": ["liquid_depth_unit_conversion_error"]
    }


# 43. Common error cubic conversion trap 1m3
def arch_43_common_error_cubic_conversion_trap_1m3(rng: random.Random) -> Dict[str, Any]:
    ans = "Because volume is 3-dimensional: 1 m^3 = 100 cm × 100 cm × 100 cm = 1 000 000 cm^3."
    prompt = (
        "A student claims that because \\(1\\text{ m} = 100\\text{ cm}\\), \\(1\\text{ m}^3 = 100\\text{ cm}^3\\).\n\n"
        "Explain why this claim is incorrect and state the correct number of cubic centimetres in \\(1\\text{ m}^3\\)."
    )
    sol = (
        "**Explanation:**\n"
        "- A linear measurement has 1 dimension (length): \\(1\\text{ m} = 100\\text{ cm}\\).\n"
        "- A cubic measurement has 3 dimensions (length, breadth, height).\n"
        "$$1\\text{ m}^3 = 1\\text{ m} \\times 1\\text{ m} \\times 1\\text{ m} = 100\\text{ cm} \\times 100\\text{ cm} \\times 100\\text{ cm} = \\mathbf{1\\,000\\,000}\\text{ cm}^3$$\n\n"
        "Therefore, \\(1\\text{ m}^3\\) is one million cubic centimetres, not 100."
    )
    return {
        "id": f"g7_sav_43_{rng.randint(100000, 999999)}",
        "subskill": "43_common_error_cubic_conversion_trap_1m3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_43",
        "hints": {"tier_1": "Remember you must cube the conversion factor 100.", "tier_2": "100 × 100 × 100 = 1 000 000.", "tier_3": ans},
        "misconception_tags": ["treating_cubic_conversion_as_linear"]
    }


# 44. Common error forgetting pairs in surface area trap
def arch_44_common_error_forgetting_pairs_in_surface_area_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: only 3 faces were calculated instead of all 6. Correct SA is 2(lb + lh + bh) = 2(26) = 52 cm^2."
    prompt = (
        "To find the surface area of a prism with \\(l = 4\\), \\(b = 3\\), \\(h = 2\\), a learner wrote:\n"
        "\\[ \\text{SA} = 4 \\times 3 + 4 \\times 2 + 3 \\times 2 = 12 + 8 + 6 = 26\\text{ cm}^2 \\]\n\n"
        "Identify the error in the learner's formula and calculate the correct surface area."
    )
    sol = (
        "**Step 1:** Error:\n"
        "A closed rectangular prism has 6 faces (3 pairs of equal opposite faces).\n"
        "The learner only added 3 single faces and forgot to multiply by 2.\n\n"
        "**Step 2:** Correct formula and calculation:\n"
        "$$\\text{SA} = 2(lb + lh + bh) = 2(12 + 8 + 6) = 2(26) = \\mathbf{52}\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_sav_44_{rng.randint(100000, 999999)}",
        "subskill": "44_common_error_forgetting_pairs_in_surface_area_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_44",
        "hints": {"tier_1": "A box has 6 faces, not 3.", "tier_2": "Double 26 to get 52 cm^2.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_double_face_pairs_in_surface_area"]
    }


# 45. Common error confusing volume and surface area trap
def arch_45_common_error_confusing_volume_and_surface_area_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Volume measures the 3D space inside an object (cm^3), while surface area measures the 2D area covering the outside (cm^2)."
    prompt = (
        "Distinguish between the terms **Volume** and **Surface Area** of a 3D object, including their standard units."
    )
    sol = (
        "**Distinction:**\n"
        "- **Volume** is the amount of 3-dimensional space an object occupies or contains. It is measured in cubic units (e.g. \\(\\text{cm}^3\\), \\(\\text{m}^3\\)).\n"
        "- **Surface Area** is the total 2-dimensional area of all outer faces that cover the solid. It is measured in square units (e.g. \\(\\text{cm}^2\\), \\(\\text{m}^2\\))."
    )
    return {
        "id": f"g7_sav_45_{rng.randint(100000, 999999)}",
        "subskill": "45_common_error_confusing_volume_and_surface_area_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_45",
        "hints": {"tier_1": "Think inside space vs outside wrapper.", "tier_2": "Cubic vs square units.", "tier_3": ans},
        "misconception_tags": ["confusing_volume_and_surface_area_definitions"]
    }


# 46. Common error open box six faces trap
def arch_46_common_error_open_box_six_faces_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: the top lid face (15 × 10 = 150) must not be included. Correct SA is 700 - 150 = 550 cm^2."
    prompt = (
        "An open-top shoe box measures \\(15\\text{ cm} \\times 10\\text{ cm} \\times 8\\text{ cm}\\).\n"
        "A student calculated the surface area of all 6 faces as \\(700\\text{ cm}^2\\).\n\n"
        "Explain what adjustment must be made because the box has no lid, and give the correct surface area."
    )
    sol = (
        "**Adjustment:**\n"
        "Since there is no lid, the area of the top rectangular face (\\(15 \\times 10 = 150\\text{ cm}^2\\)) must be omitted.\n\n"
        "**Correct SA:**\n"
        "$$\\text{SA} = 700 - 150 = \\mathbf{550}\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_sav_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_error_open_box_six_faces_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_46",
        "hints": {"tier_1": "Subtract the area of the top face (15 × 10).", "tier_2": "700 - 150 = 550.", "tier_3": ans},
        "misconception_tags": ["including_sixth_face_in_open_box_trap"]
    }


# 47. Ratio of volumes two cubes
def arch_47_ratio_of_volumes_two_cubes(rng: random.Random) -> Dict[str, Any]:
    ans = "1 : 27"
    prompt = (
        "Cube A has edge length \\(2\\text{ cm}\\) and Cube B has edge length \\(6\\text{ cm}\\).\n\n"
        "Find the ratio of the volume of Cube A to the volume of Cube B in simplest form."
    )
    sol = (
        "**Step 1:** Calculate both volumes:\n"
        "- \\(V_A = 2^3 = 8\\text{ cm}^3\\)\n"
        "- \\(V_B = 6^3 = 216\\text{ cm}^3\\)\n\n"
        "**Step 2:** Form ratio and simplify:\n"
        "$$\\frac{8}{216} = \\frac{1}{27} \\implies \\mathbf{1 : 27}$$"
    )
    return {
        "id": f"g7_sav_47_{rng.randint(100000, 999999)}",
        "subskill": "47_ratio_of_volumes_two_cubes",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_47",
        "hints": {"tier_1": "VA = 8, VB = 216.", "tier_2": "8 : 216 = 1 : 27.", "tier_3": ans},
        "misconception_tags": ["ratio_of_sides_instead_of_ratio_of_volumes"]
    }


# 48. Ratio of surface areas two cubes
def arch_48_ratio_of_surface_areas_two_cubes(rng: random.Random) -> Dict[str, Any]:
    ans = "1 : 9"
    prompt = (
        "For Cube A (edge \\(2\\text{ cm}\\)) and Cube B (edge \\(6\\text{ cm}\\)), determine the ratio of their "
        "total surface areas in simplest form."
    )
    sol = (
        "**Step 1:** Calculate surface areas:\n"
        "- \\(\\text{SA}_A = 6 \\times 2^2 = 6 \\times 4 = 24\\text{ cm}^2\\)\n"
        "- \\(\\text{SA}_B = 6 \\times 6^2 = 6 \\times 36 = 216\\text{ cm}^2\\)\n\n"
        "**Step 2:** Simplify ratio:\n"
        "$$\\frac{24}{216} = \\frac{1}{9} \\implies \\mathbf{1 : 9}$$\n\n"
        "*(Note: \\((2/6)^2 = (1/3)^2 = 1/9\\))*"
    )
    return {
        "id": f"g7_sav_48_{rng.randint(100000, 999999)}",
        "subskill": "48_ratio_of_surface_areas_two_cubes",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_48",
        "hints": {"tier_1": "24 to 216.", "tier_2": "Divide both by 24 -> 1 : 9.", "tier_3": ans},
        "misconception_tags": ["cube_surface_area_ratio_scaling_error"]
    }


# 49. Cost of tin plate surface area
def arch_49_cost_of_tin_plate_surface_area(rng: random.Random) -> Dict[str, Any]:
    ans = "R130"
    prompt = (
        "A metal container has a total surface area of \\(2{,}6\\text{ m}^2\\).\n"
        "Sheet metal costs R50 per \\(\\text{m}^2\\).\n\n"
        "Calculate the total cost of the metal needed to build the container."
    )
    sol = (
        "**Step 1:** Multiply surface area by cost per \\(\\text{m}^2\\):\n"
        "$$\\text{Cost} = 2{,}6 \\times 50 = \\mathbf{\\text{R}130}$$"
    )
    return {
        "id": f"g7_sav_49_{rng.randint(100000, 999999)}",
        "subskill": "49_cost_of_tin_plate_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_49",
        "hints": {"tier_1": "2,6 × 50.", "tier_2": "2,6 × 50 = 130.", "tier_3": ans},
        "misconception_tags": ["decimal_currency_multiplication_error"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_surface_area_and_volume_3d_comprehensive_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "a) V = 125 cm^3; b) SA = 150 cm^2; c) V = 120 cm^3; d) 0,12 litres"
    prompt = (
        "**Grade 7 Surface Area and Volume of 3D Objects Comprehensive Diagnostic Autopsy**\n\n"
        "1. A cube has edge length \\(5\\text{ cm}\\). Calculate its volume and its total surface area.\n"
        "2. A rectangular prism has dimensions \\(8\\text{ cm} \\times 5\\text{ cm} \\times 3\\text{ cm}\\). "
        "Find its volume in \\(\\text{cm}^3\\).\n"
        "3. Convert the volume in (2) to litres."
    )
    sol = (
        "**Question 1:**\n"
        "- Cube Volume: \\(V = 5^3 = \\mathbf{125}\\text{ cm}^3\\)\n"
        "- Cube Surface Area: \\(\\text{SA} = 6(5^2) = 6 \\times 25 = \\mathbf{150}\\text{ cm}^2\\)\n\n"
        "**Question 2:**\n"
        "$$\\text{Prism Volume} = 8 \\times 5 \\times 3 = \\mathbf{120}\\text{ cm}^3$$\n\n"
        "**Question 3:**\n"
        "$$\\text{Capacity} = \\frac{120}{1\\,000} = \\mathbf{0{,}12}\\text{ litres}$$"
    )
    return {
        "id": f"g7_sav_50_{rng.randint(100000, 999999)}",
        "subskill": "50_surface_area_and_volume_3d_comprehensive_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_sav_50",
        "hints": {
            "tier_1": "1: 5^3 and 6(25). 2: 8 × 5 × 3 = 120. 3: 120 / 1000 = 0,12.",
            "tier_2": "V = 125 cm^3, SA = 150 cm^2, Prism V = 120 cm^3, 0,12 l.",
            "tier_3": ans
        },
        "misconception_tags": [
            "cube_volume_and_surface_area_confusion",
            "rectangular_prism_volume_calculation_error",
            "cm3_to_litre_conversion_division_error"
        ]
    }
