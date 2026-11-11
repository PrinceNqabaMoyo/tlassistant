"""Grade 7 Mathematics - Common Fractions: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/01. Fractions.md
"""
import random
import math
from typing import Dict, Any, List


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def _svg_fraction_bar(shaded: int, total: int, width: int = 400, height: int = 80) -> str:
    """Renders a clean segmented fraction bar on white background."""
    w_bar = 320
    h_bar = 40
    start_x, start_y = 40, 20
    part_w = w_bar / total
    
    rects = []
    for i in range(total):
        fill = "#2563eb" if i < shaded else "#ffffff"
        rects.append(
            f'<rect x="{start_x + i * part_w:.1f}" y="{start_y}" width="{part_w:.1f}" height="{h_bar}" '
            f'fill="{fill}" stroke="#1e293b" stroke-width="2"/>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{"".join(rects)}'
        f'</svg>'
    )


# 01. Fraction part of a whole greystick
def arch_01_fraction_part_of_a_whole_greystick(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([5, 6, 8, 10, 12])
    num = rng.randint(2, denom - 1)
    while math.gcd(num, denom) > 1:
        num = rng.randint(2, denom - 1)
    svg = _svg_fraction_bar(num, denom)
    prompt = (
        f"A measuring stick is divided into {denom} equal parts, and {num} of these parts are shaded.\n\n"
        f"1. Write the shaded portion as a common fraction.\n"
        f"2. Identify the numerator and the denominator, explaining what each represents."
    )
    sol = (
        f"**Step 1:** The shaded portion is $\\mathbf{{\\frac{{{num}}}{{{denom}}}}}$.\n\n"
        f"**Step 2:**\n"
        f"- **Numerator ({num}):** Represents the number of equal parts taken / shaded.\n"
        f"- **Denominator ({denom}):** Represents the total number of equal parts the whole is divided into."
    )
    ans = f"1. {num}/{denom}; 2. Numerator: {num} (shaded parts), Denominator: {denom} (total parts in the whole)"
    return {
        "id": f"g7_frac_01_{rng.randint(100000, 999999)}",
        "subskill": "01_fraction_part_of_a_whole_greystick",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Count Total Parts", "body": f"The bar is partitioned into {denom} equal parts (denominator)."},
                {"title": "Count Shaded Parts", "body": f"{num} parts are blue (numerator)."},
                {"title": "Form Fraction", "body": f"Fraction is {num}/{denom}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_01",
        "hints": {
            "tier_1": "Top number = shaded count; bottom number = total count.",
            "tier_2": f"Denominator is {denom}, numerator is {num}.",
            "tier_3": ans
        },
        "misconception_tags": ["swapped_numerator_and_denominator"]
    }


# 02. Proper vs improper vs mixed classification
def arch_02_proper_vs_improper_vs_mixed_classification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Classify each of the following fractions as a **proper fraction**, an **improper fraction**, or a **mixed number**:\n\n"
        "(a) $\\frac{4}{7}$\n"
        "(b) $\\frac{9}{5}$\n"
        "(c) $2\\frac{1}{3}$"
    )
    sol = (
        "(a) $\\frac{4}{7}$ $\\rightarrow$ **Proper fraction** (numerator < denominator; value < 1).\n"
        "(b) $\\frac{9}{5}$ $\\rightarrow$ **Improper fraction** (numerator > denominator; value > 1).\n"
        "(c) $2\\frac{1}{3}$ $\\rightarrow$ **Mixed number** (contains a whole number and a proper fraction)."
    )
    ans = "(a) Proper fraction, (b) Improper fraction, (c) Mixed number"
    return {
        "id": f"g7_frac_02_{rng.randint(100000, 999999)}",
        "subskill": "02_proper_vs_improper_vs_mixed_classification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_02",
        "hints": {
            "tier_1": "Proper: top < bottom; Improper: top >= bottom; Mixed: whole + fraction.",
            "tier_2": "Look at each fraction's structure.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_improper_and_mixed_definitions"]
    }


# 03. Convert mixed number to improper fraction
def arch_03_convert_mixed_number_to_improper_fraction(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(2, 6)
    denom = rng.choice([3, 4, 5, 7, 8])
    num = rng.randint(1, denom - 1)
    improper_num = whole * denom + num
    prompt = (
        f"Convert the mixed number ${whole}\\frac{{{num}}}{{{denom}}}$ into an improper fraction.\n\n"
        f"Show all working steps."
    )
    sol = (
        f"**Step 1:** Multiply the whole number by the denominator:\n"
        f"$${whole} \\times {denom} = {whole * denom}$$\n\n"
        f"**Step 2:** Add the numerator:\n"
        f"$${whole * denom} + {num} = {improper_num}$$\n\n"
        f"**Conclusion:** $${whole}\\frac{{{num}}}{{{denom}}} = \\mathbf{{\\frac{{{improper_num}}}{{{denom}}}}}$$"
    )
    ans = f"{improper_num}/{denom}"
    return {
        "id": f"g7_frac_03_{rng.randint(100000, 999999)}",
        "subskill": "03_convert_mixed_number_to_improper_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_03",
        "hints": {
            "tier_1": f"Multiply {whole} by {denom}, then add {num}.",
            "tier_2": f"Keep the same denominator ({denom}).",
            "tier_3": ans
        },
        "misconception_tags": ["added_whole_to_numerator_directly"]
    }


# 04. Convert improper fraction to mixed number
def arch_04_convert_improper_fraction_to_mixed_number(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(2, 7)
    denom = rng.choice([3, 4, 5, 6, 7])
    rem = rng.randint(1, denom - 1)
    improper_num = whole * denom + rem
    prompt = (
        f"Convert the improper fraction $\\frac{{{improper_num}}}{{{denom}}}$ into a mixed number in its simplest form."
    )
    sol = (
        f"**Step 1:** Divide the numerator by the denominator:\n"
        f"$${improper_num} \\div {denom} = {whole} \\text{{ remainder }} {rem}$$\n\n"
        f"**Step 2:** Write as a mixed number (quotient as whole number, remainder over original denominator):\n"
        f"$$\\frac{{{improper_num}}}{{{denom}}} = \\mathbf{{{whole}\\frac{{{rem}}}{{{denom}}}}}$$"
    )
    ans = f"{whole} {rem}/{denom}"
    return {
        "id": f"g7_frac_04_{rng.randint(100000, 999999)}",
        "subskill": "04_convert_improper_fraction_to_mixed_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_04",
        "hints": {
            "tier_1": f"How many times does {denom} go into {improper_num}?",
            "tier_2": f"Quotient is {whole}, remainder is {rem}.",
            "tier_3": ans
        },
        "misconception_tags": ["remainder_placed_in_wrong_position"]
    }


# 05. Equivalent fractions scaling up
def arch_05_equivalent_fractions_scaling_up(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([2, 3, 4])
    d = rng.choice([5, 7, 9])
    scale = rng.choice([3, 4, 5, 6])
    n_scaled = n * scale
    d_scaled = d * scale
    prompt = (
        f"Find the missing numerator to make the two fractions equivalent:\n"
        f"$$\\frac{{{n}}}{{{d}}} = \\frac{{\\square}}{{{d_scaled}}}$$"
    )
    sol = (
        f"**Step 1:** Determine the scaling factor for the denominators:\n"
        f"$${d_scaled} \\div {d} = {scale}$$\n\n"
        f"**Step 2:** Multiply the numerator by the same scaling factor:\n"
        f"$$\\square = {n} \\times {scale} = \\mathbf{{{n_scaled}}}$$\n\n"
        f"**Conclusion:** $\\frac{{{n}}}{{{d}}} = \\frac{{{n_scaled}}}{{{d_scaled}}}$."
    )
    ans = f"{n_scaled}"
    return {
        "id": f"g7_frac_05_{rng.randint(100000, 999999)}",
        "subskill": "05_equivalent_fractions_scaling_up",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_05",
        "hints": {
            "tier_1": f"What number was {d} multiplied by to get {d_scaled}?",
            "tier_2": f"Multiply {n} by {scale}.",
            "tier_3": ans
        },
        "misconception_tags": ["added_difference_instead_of_multiplying"]
    }


# 06. Simplify fraction to lowest terms
def arch_06_simplify_fraction_to_lowest_terms(rng: random.Random) -> Dict[str, Any]:
    n_simp = rng.choice([2, 3, 4, 5])
    d_simp = rng.choice([7, 9, 11, 13])
    factor = rng.choice([2, 3, 4, 6])
    n = n_simp * factor
    d = d_simp * factor
    prompt = (
        f"Simplify the fraction $\\frac{{{n}}}{{{d}}}$ to its lowest (simplest) terms.\n\n"
        f"Show the common factor used."
    )
    sol = (
        f"**Step 1:** Find the highest common factor (HCF) of {n} and {d}, which is {factor}.\n\n"
        f"**Step 2:** Divide both the numerator and denominator by {factor}:\n"
        f"$$\\frac{{{n} \\div {factor}}}{{{d} \\div {factor}}} = \\mathbf{{\\frac{{{n_simp}}}{{{d_simp}}}}}$$"
    )
    ans = f"{n_simp}/{d_simp}"
    return {
        "id": f"g7_frac_06_{rng.randint(100000, 999999)}",
        "subskill": "06_simplify_fraction_to_lowest_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_06",
        "hints": {
            "tier_1": f"Both {n} and {d} are divisible by {factor}.",
            "tier_2": f"Divide top and bottom by {factor}.",
            "tier_3": ans
        },
        "misconception_tags": ["divided_only_one_term_by_factor"]
    }


# 07. Comparing fractions with same denominator
def arch_07_comparing_fractions_with_same_denominator(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([7, 9, 11, 13])
    n1 = rng.randint(2, denom - 2)
    n2 = n1 + rng.choice([1, 2])
    sign = "<" if n1 < n2 else ">"
    prompt = (
        f"Insert the correct relational symbol ($<$, $>$, or $=$) between the two fractions:\n"
        f"$$\\frac{{{n1}}}{{{denom}}} \\quad \\square \\quad \\frac{{{n2}}}{{{denom}}}$$\n\n"
        f"Explain your reasoning."
    )
    sol = (
        f"**Step 1:** When fractions have the **same denominator** ({denom}), "
        f"the fraction with the larger numerator is the larger fraction.\n\n"
        f"**Step 2:** Since ${n1} < {n2}$, we write:\n"
        f"$$\\frac{{{n1}}}{{{denom}}} < \\frac{{{n2}}}{{{denom}}}$$"
    )
    ans = f"< (because {n1} < {n2})"
    return {
        "id": f"g7_frac_07_{rng.randint(100000, 999999)}",
        "subskill": "07_comparing_fractions_with_same_denominator",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_07",
        "hints": {
            "tier_1": "With equal denominators, just compare the top numbers.",
            "tier_2": f"{n1} is less than {n2}.",
            "tier_3": ans
        },
        "misconception_tags": ["symbol_inversion_error"]
    }


# 08. Comparing fractions with different denominators LCD
def arch_08_comparing_fractions_with_different_denominators_lcd(rng: random.Random) -> Dict[str, Any]:
    # e.g. 2/3 vs 3/5 -> LCD 15 -> 10/15 vs 9/15 -> 2/3 > 3/5
    d1, d2 = 3, 5
    n1, n2 = 2, 3
    lcd = 15
    eq1 = n1 * 5 # 10
    eq2 = n2 * 3 # 9
    prompt = (
        f"Compare the two fractions by converting them to equivalent fractions with a lowest common denominator (LCD):\n"
        f"$$\\frac{{{n1}}}{{{d1}}} \\quad \\text{{and}} \\quad \\frac{{{n2}}}{{{d2}}}$$\n\n"
        f"1. What is the LCD of {d1} and {d2}?\n"
        f"2. Write down the equivalent fractions and insert $>$ or $<$."
    )
    sol = (
        f"**Step 1:** The LCD of {d1} and {d2} is **{lcd}**.\n\n"
        f"**Step 2:** Convert both fractions:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} = \\frac{{{eq1}}}{{{lcd}}}, \\quad \\frac{{{n2}}}{{{d2}}} = \\frac{{{eq2}}}{{{lcd}}}$$\n\n"
        f"**Step 3:** Since ${eq1} > {eq2}$, we conclude:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} > \\frac{{{n2}}}{{{d2}}}$$"
    )
    ans = f"1. LCD = {lcd}; 2. {eq1}/{lcd} > {eq2}/{lcd}, so {n1}/{d1} > {n2}/{d2}"
    return {
        "id": f"g7_frac_08_{rng.randint(100000, 999999)}",
        "subskill": "08_comparing_fractions_with_different_denominators_lcd",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_08",
        "hints": {
            "tier_1": f"Find LCM of {d1} and {d2} (which is {lcd}).",
            "tier_2": f"Convert to /15: {eq1}/15 and {eq2}/15.",
            "tier_3": ans
        },
        "misconception_tags": ["compared_numerators_without_lcd"]
    }


# 09. Ordering fractions ascending descending
def arch_09_ordering_fractions_ascending_descending(rng: random.Random) -> Dict[str, Any]:
    # 1/2, 2/3, 3/4 -> LCD = 12 -> 6/12, 8/12, 9/12
    prompt = (
        "Arrange the following fractions in **ascending order** (from smallest to largest):\n"
        "$$\\frac{3}{4}, \\quad \\frac{1}{2}, \\quad \\frac{2}{3}$$\n\n"
        "Show working using equivalent fractions with a common denominator of 12."
    )
    sol = (
        "**Step 1:** Convert each fraction to twelfths ($/12$):\n"
        "- $\\frac{1}{2} = \\frac{6}{12}$\n"
        "- $\\frac{2}{3} = \\frac{8}{12}$\n"
        "- $\\frac{3}{4} = \\frac{9}{12}$\n\n"
        "**Step 2:** Compare the numerators: $6 < 8 < 9$.\n\n"
        "**Conclusion (Ascending Order):** $$\\mathbf{\\frac{1}{2}, \\quad \\frac{2}{3}, \\quad \\frac{3}{4}}$$"
    )
    ans = "1/2, 2/3, 3/4"
    return {
        "id": f"g7_frac_09_{rng.randint(100000, 999999)}",
        "subskill": "09_ordering_fractions_ascending_descending",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_09",
        "hints": {
            "tier_1": "Change all three fractions to have denominator 12.",
            "tier_2": "6/12, 8/12, 9/12.",
            "tier_3": ans
        },
        "misconception_tags": ["descending_instead_of_ascending_order"]
    }


# 10. Adding fractions like denominators
def arch_10_adding_fractions_like_denominators(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([7, 9, 11, 13])
    n1 = rng.randint(1, denom - 3)
    n2 = rng.randint(1, denom - 1 - n1)
    sum_n = n1 + n2
    prompt = (
        f"Calculate the sum and simplify if possible:\n"
        f"$$\\frac{{{n1}}}{{{denom}}} + \\frac{{{n2}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Since denominators are the same, add the numerators and keep the common denominator:\n"
        f"$$\\frac{{{n1} + {n2}}}{{{denom}}} = \\mathbf{{\\frac{{{sum_n}}}{{{denom}}}}}$$"
    )
    ans = f"{sum_n}/{denom}"
    return {
        "id": f"g7_frac_10_{rng.randint(100000, 999999)}",
        "subskill": "10_adding_fractions_like_denominators",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_10",
        "hints": {
            "tier_1": "Do not add the denominators! Keep the bottom number unchanged.",
            "tier_2": f"Add {n1} + {n2}.",
            "tier_3": ans
        },
        "misconception_tags": ["added_denominators_together"]
    }


# 11. Subtracting fractions like denominators
def arch_11_subtracting_fractions_like_denominators(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([8, 10, 12, 14])
    n2 = rng.randint(1, denom // 2)
    n1 = n2 + rng.randint(1, denom - n2 - 1)
    diff = n1 - n2
    g = math.gcd(diff, denom)
    simp_str = f" = \\frac{{{diff//g}}}{{{denom//g}}}" if g > 1 else ""
    prompt = (
        f"Calculate the difference and write the answer in simplest form:\n"
        f"$$\\frac{{{n1}}}{{{denom}}} - \\frac{{{n2}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Subtract the numerators and keep the common denominator:\n"
        f"$$\\frac{{{n1} - {n2}}}{{{denom}}} = \\frac{{{diff}}}{{{denom}}}{simp_str}$$"
    )
    ans = f"{diff//g}/{denom//g}" if g > 1 else f"{diff}/{denom}"
    return {
        "id": f"g7_frac_11_{rng.randint(100000, 999999)}",
        "subskill": "11_subtracting_fractions_like_denominators",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_11",
        "hints": {
            "tier_1": f"Subtract the top numbers: {n1} - {n2}.",
            "tier_2": "Simplify the resulting fraction if possible.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracted_denominators_to_get_zero"]
    }


# 12. Adding fractions one denominator multiple of other
def arch_12_adding_fractions_one_denominator_multiple_of_other(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([2, 3, 4, 5])
    mult = rng.choice([2, 3])
    d2 = d1 * mult
    n1 = rng.randint(1, d1 - 1)
    n2 = rng.randint(1, mult)
    n1_scaled = n1 * mult
    total_n = n1_scaled + n2
    g = math.gcd(total_n, d2)
    prompt = (
        f"Calculate:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}}$$\n\n"
        f"Show conversion to the common denominator."
    )
    sol = (
        f"**Step 1:** Notice {d2} is a multiple of {d1}. The LCD is **{d2}**.\n\n"
        f"**Step 2:** Convert $\\frac{{{n1}}}{{{d1}}}$ to denominator {d2}:\n"
        f"$$\\frac{{{n1} \\times {mult}}}{{{d1} \\times {mult}}} = \\frac{{{n1_scaled}}}{{{d2}}}$$\n\n"
        f"**Step 3:** Add the fractions:\n"
        f"$$\\frac{{{n1_scaled}}}{{{d2}}} + \\frac{{{n2}}}{{{d2}}} = \\mathbf{{\\frac{{{total_n}}}{{{d2}}}}}$$"
    )
    ans = f"{total_n//g}/{d2//g}" if g > 1 else f"{total_n}/{d2}"
    return {
        "id": f"g7_frac_12_{rng.randint(100000, 999999)}",
        "subskill": "12_adding_fractions_one_denominator_multiple_of_other",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_12",
        "hints": {
            "tier_1": f"The LCD is {d2}.",
            "tier_2": f"Change {n1}/{d1} into {n1_scaled}/{d2}.",
            "tier_3": ans
        },
        "misconception_tags": ["added_unlike_denominators_directly"]
    }


# 13. Subtracting fractions one denominator multiple of other
def arch_13_subtracting_fractions_one_denominator_multiple_of_other(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([3, 4, 5])
    mult = 2
    d2 = d1 * mult
    n1 = rng.randint(2, d1 - 1)
    n2 = 1
    n1_scaled = n1 * mult
    diff = n1_scaled - n2
    g = math.gcd(diff, d2)
    prompt = (
        f"Calculate:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} - \\frac{{{n2}}}{{{d2}}}$$"
    )
    sol = (
        f"**Step 1:** The LCD is {d2}.\n\n"
        f"**Step 2:** Convert $\\frac{{{n1}}}{{{d1}}} = \\frac{{{n1_scaled}}}{{{d2}}}$.\n\n"
        f"**Step 3:** Subtract:\n"
        f"$$\\frac{{{n1_scaled}}}{{{d2}}} - \\frac{{{n2}}}{{{d2}}} = \\mathbf{{\\frac{{{diff}}}{{{d2}}}}}$$"
    )
    ans = f"{diff//g}/{d2//g}" if g > 1 else f"{diff}/{d2}"
    return {
        "id": f"g7_frac_13_{rng.randint(100000, 999999)}",
        "subskill": "13_subtracting_fractions_one_denominator_multiple_of_other",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_13",
        "hints": {
            "tier_1": f"Convert to LCD = {d2}.",
            "tier_2": f"Subtract {n2} from {n1_scaled}.",
            "tier_3": ans
        },
        "misconception_tags": ["forgot_to_scale_numerator"]
    }


# 14. Adding fractions coprime denominators LCD
def arch_14_adding_fractions_coprime_denominators_lcd(rng: random.Random) -> Dict[str, Any]:
    d1, d2 = rng.choice([(2, 3), (3, 4), (3, 5), (4, 5)])
    n1 = rng.randint(1, d1 - 1)
    n2 = rng.randint(1, d2 - 1)
    lcd = d1 * d2
    new_n1 = n1 * d2
    new_n2 = n2 * d1
    total_n = new_n1 + new_n2
    prompt = (
        f"Add the fractions with unlike denominators:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} + \\frac{{{n2}}}{{{d2}}}$$\n\n"
        f"Show all steps including finding the LCD."
    )
    sol = (
        f"**Step 1:** Find LCD: $\\text{{LCD}}({d1}, {d2}) = {lcd}$.\n\n"
        f"**Step 2:** Convert both fractions to have denominator {lcd}:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} = \\frac{{{new_n1}}}{{{lcd}}}, \\quad \\frac{{{n2}}}{{{d2}}} = \\frac{{{new_n2}}}{{{lcd}}}$$\n\n"
        f"**Step 3:** Add:\n"
        f"$$\\frac{{{new_n1}}}{{{lcd}}} + \\frac{{{new_n2}}}{{{lcd}}} = \\mathbf{{\\frac{{{total_n}}}{{{lcd}}}}}$$"
    )
    ans = f"{total_n}/{lcd}"
    return {
        "id": f"g7_frac_14_{rng.randint(100000, 999999)}",
        "subskill": "14_adding_fractions_coprime_denominators_lcd",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_14",
        "hints": {
            "tier_1": f"Multiply denominators to find LCD: {d1} * {d2} = {lcd}.",
            "tier_2": f"Rewrite as {new_n1}/{lcd} + {new_n2}/{lcd}.",
            "tier_3": ans
        },
        "misconception_tags": ["uncommon_denominator_addition_error"]
    }


# 15. Subtracting fractions coprime denominators LCD
def arch_15_subtracting_fractions_coprime_denominators_lcd(rng: random.Random) -> Dict[str, Any]:
    d1, d2 = rng.choice([(2, 3), (3, 4), (3, 5), (4, 5)])
    n1, n2 = d1 - 1, 1
    lcd = d1 * d2
    new_n1 = n1 * d2
    new_n2 = n2 * d1
    diff = new_n1 - new_n2
    prompt = (
        f"Calculate the difference:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} - \\frac{{{n2}}}{{{d2}}}$$"
    )
    sol = (
        f"**Step 1:** $\\text{{LCD}}({d1}, {d2}) = {lcd}$.\n\n"
        f"**Step 2:** Convert both:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} = \\frac{{{new_n1}}}{{{lcd}}}, \\quad \\frac{{{n2}}}{{{d2}}} = \\frac{{{new_n2}}}{{{lcd}}}$$\n\n"
        f"**Step 3:** Subtract:\n"
        f"$$\\frac{{{new_n1}}}{{{lcd}}} - \\frac{{{new_n2}}}{{{lcd}}} = \\mathbf{{\\frac{{{diff}}}{{{lcd}}}}}$$"
    )
    ans = f"{diff}/{lcd}"
    return {
        "id": f"g7_frac_15_{rng.randint(100000, 999999)}",
        "subskill": "15_subtracting_fractions_coprime_denominators_lcd",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_15",
        "hints": {
            "tier_1": f"Convert both fractions to have denominator {lcd}.",
            "tier_2": f"{new_n1}/{lcd} - {new_n2}/{lcd}.",
            "tier_3": ans
        },
        "misconception_tags": ["subtraction_cross_multiplication_confusion"]
    }


# 16. Adding three fractions different denominators
def arch_16_adding_three_fractions_different_denominators(rng: random.Random) -> Dict[str, Any]:
    # 1/2 + 1/3 + 1/4 -> LCD = 12 -> 6/12 + 4/12 + 3/12 = 13/12 = 1 1/12
    prompt = (
        "Evaluate the sum of three fractions:\n"
        "$$\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{4}$$\n\n"
        "State the LCD and give the final answer as a mixed number."
    )
    sol = (
        "**Step 1:** Find the LCD of 2, 3, and 4:\n"
        "$$\\text{LCD}(2, 3, 4) = 12$$\n\n"
        "**Step 2:** Convert to equivalent fractions with denominator 12:\n"
        "$$\\frac{1}{2} = \\frac{6}{12}, \\quad \\frac{1}{3} = \\frac{4}{12}, \\quad \\frac{1}{4} = \\frac{3}{12}$$\n\n"
        "**Step 3:** Add the numerators:\n"
        "$$\\frac{6 + 4 + 3}{12} = \\frac{13}{12} = \\mathbf{1\\frac{1}{12}}$$"
    )
    ans = "1 1/12"
    return {
        "id": f"g7_frac_16_{rng.randint(100000, 999999)}",
        "subskill": "16_adding_three_fractions_different_denominators",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_16",
        "hints": {
            "tier_1": "The LCD of 2, 3, and 4 is 12.",
            "tier_2": "Convert: 6/12 + 4/12 + 3/12.",
            "tier_3": ans
        },
        "misconception_tags": ["three_fraction_lcd_error"]
    }


# 17. Adding mixed numbers without regrouping
def arch_17_adding_mixed_numbers_without_regrouping(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.randint(1, 4)
    w2 = rng.randint(1, 4)
    denom = rng.choice([5, 7, 8])
    n1 = 1
    n2 = 2
    w_sum = w1 + w2
    n_sum = n1 + n2
    prompt = (
        f"Calculate the sum of the mixed numbers:\n"
        f"$${w1}\\frac{{{n1}}}{{{denom}}} + {w2}\\frac{{{n2}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Add the whole numbers:\n"
        f"$${w1} + {w2} = {w_sum}$$\n\n"
        f"**Step 2:** Add the fractional parts:\n"
        f"$$\\frac{{{n1}}}{{{denom}}} + \\frac{{{n2}}}{{{denom}}} = \\frac{{{n_sum}}}{{{denom}}}$$\n\n"
        f"**Conclusion:** $$\\mathbf{{{w_sum}\\frac{{{n_sum}}}{{{denom}}}}}$$"
    )
    ans = f"{w_sum} {n_sum}/{denom}"
    return {
        "id": f"g7_frac_17_{rng.randint(100000, 999999)}",
        "subskill": "17_adding_mixed_numbers_without_regrouping",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_17",
        "hints": {
            "tier_1": f"Add wholes: {w1} + {w2} = {w_sum}.",
            "tier_2": f"Add fractions: {n1}/{denom} + {n2}/{denom} = {n_sum}/{denom}.",
            "tier_3": ans
        },
        "misconception_tags": ["mixed_number_addition_separation_error"]
    }


# 18. Adding mixed numbers with improper fraction sum
def arch_18_adding_mixed_numbers_with_improper_fraction_sum(rng: random.Random) -> Dict[str, Any]:
    w1, w2 = 2, 3
    denom = 5
    n1, n2 = 3, 4
    # 2 3/5 + 3 4/5 = 5 7/5 = 6 2/5
    w_init = w1 + w2
    n_sum = n1 + n2
    w_final = w_init + (n_sum // denom)
    rem = n_sum % denom
    prompt = (
        f"Calculate and simplify:\n"
        f"$${w1}\\frac{{{n1}}}{{{denom}}} + {w2}\\frac{{{n2}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Add wholes and fractions:\n"
        f"$$({w1} + {w2}) + \\left(\\frac{{{n1} + {n2}}}{{{denom}}}\\right) = {w_init} + \\frac{{{n_sum}}}{{{denom}}}$$\n\n"
        f"**Step 2:** Convert $\\frac{{{n_sum}}}{{{denom}}}$ to a mixed number:\n"
        f"$$\\frac{{{n_sum}}}{{{denom}}} = 1\\frac{{{rem}}}{{{denom}}}$$\n\n"
        f"**Step 3:** Add the carry-over whole number:\n"
        f"$${w_init} + 1\\frac{{{rem}}}{{{denom}}} = \\mathbf{{{w_final}\\frac{{{rem}}}{{{denom}}}}}$$"
    )
    ans = f"{w_final} {rem}/{denom}"
    return {
        "id": f"g7_frac_18_{rng.randint(100000, 999999)}",
        "subskill": "18_adding_mixed_numbers_with_improper_fraction_sum",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_18",
        "hints": {
            "tier_1": f"7/5 is an improper fraction equal to 1 2/5.",
            "tier_2": f"Add the 1 whole to {w_init}.",
            "tier_3": ans
        },
        "misconception_tags": ["left_improper_fraction_in_mixed_number"]
    }


# 19. Subtracting mixed numbers without borrowing
def arch_19_subtracting_mixed_numbers_without_borrowing(rng: random.Random) -> Dict[str, Any]:
    w1, w2 = 5, 2
    denom = 7
    n1, n2 = 5, 2
    w_diff = w1 - w2
    n_diff = n1 - n2
    prompt = (
        f"Calculate:\n"
        f"$${w1}\\frac{{{n1}}}{{{denom}}} - {w2}\\frac{{{n2}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Subtract whole numbers: $${w1} - {w2} = {w_diff}$$\n\n"
        f"**Step 2:** Subtract fractions: $$\\frac{{{n1}}}{{{denom}}} - \\frac{{{n2}}}{{{denom}}} = \\frac{{{n_diff}}}{{{denom}}}$$\n\n"
        f"**Conclusion:** $$\\mathbf{{{w_diff}\\frac{{{n_diff}}}{{{denom}}}}}$$"
    )
    ans = f"{w_diff} {n_diff}/{denom}"
    return {
        "id": f"g7_frac_19_{rng.randint(100000, 999999)}",
        "subskill": "19_subtracting_mixed_numbers_without_borrowing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_19",
        "hints": {
            "tier_1": f"Subtract wholes: {w1} - {w2} = {w_diff}.",
            "tier_2": f"Subtract fractions: {n1} - {n2} = {n_diff}.",
            "tier_3": ans
        },
        "misconception_tags": ["mixed_number_subtraction_order_error"]
    }


# 20. Subtracting mixed numbers with borrowing
def arch_20_subtracting_mixed_numbers_with_borrowing(rng: random.Random) -> Dict[str, Any]:
    # 5 1/4 - 2 3/4 -> borrow 1 from 5: 4 5/4 - 2 3/4 = 2 2/4 = 2 1/2
    w1, w2 = 5, 2
    denom = 4
    n1, n2 = 1, 3
    # Borrow 1: 5 1/4 = 4 (1+4)/4 = 4 5/4
    new_w1 = w1 - 1
    new_n1 = n1 + denom
    w_diff = new_w1 - w2 # 2
    n_diff = new_n1 - n2 # 2
    g = math.gcd(n_diff, denom)
    prompt = (
        f"Calculate the difference:\n"
        f"$${w1}\\frac{{{n1}}}{{{denom}}} - {w2}\\frac{{{n2}}}{{{denom}}}$$\n\n"
        f"Show how you regroup (borrow) from the whole number."
    )
    sol = (
        f"**Step 1:** Notice that $\\frac{{{n1}}}{{{denom}}} < \\frac{{{n2}}}{{{denom}}}$, so we must borrow $1$ from ${w1}$:\n"
        f"$${w1}\\frac{{{n1}}}{{{denom}}} = {new_w1} + 1 + \\frac{{{n1}}}{{{denom}}} = {new_w1} + \\frac{{{denom}}}{{{denom}}} + \\frac{{{n1}}}{{{denom}}} = {new_w1}\\frac{{{new_n1}}}{{{denom}}}$$\n\n"
        f"**Step 2:** Now subtract:\n"
        f"$${new_w1}\\frac{{{new_n1}}}{{{denom}}} - {w2}\\frac{{{n2}}}{{{denom}}} = {w_diff}\\frac{{{n_diff}}}{{{denom}}} = \\mathbf{{{w_diff}\\frac{{{n_diff//g}}}{{{denom//g}}}}}$$"
    )
    ans = f"{w_diff} {n_diff//g}/{denom//g}"
    return {
        "id": f"g7_frac_20_{rng.randint(100000, 999999)}",
        "subskill": "20_subtracting_mixed_numbers_with_borrowing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_20",
        "hints": {
            "tier_1": "You cannot subtract 3/4 from 1/4. Borrow 1 whole (4/4) from 5.",
            "tier_2": "5 1/4 becomes 4 5/4.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracted_smaller_numerator_from_larger"]
    }


# 21. Subtracting fraction from a whole number
def arch_21_subtracting_fraction_from_a_whole_number(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(3, 8)
    denom = rng.choice([5, 6, 7, 8])
    num = rng.randint(1, denom - 1)
    new_whole = whole - 1
    new_num = denom - num
    prompt = (
        f"Evaluate:\n"
        f"$${whole} - \\frac{{{num}}}{{{denom}}}$$"
    )
    sol = (
        f"**Step 1:** Rewrite $1$ of the whole units as a fraction with denominator {denom}:\n"
        f"$${whole} = {new_whole} + \\frac{{{denom}}}{{{denom}}} = {new_whole}\\frac{{{denom}}}{{{denom}}}$$\n\n"
        f"**Step 2:** Subtract the fraction:\n"
        f"$${new_whole}\\frac{{{denom}}}{{{denom}}} - \\frac{{{num}}}{{{denom}}} = \\mathbf{{{new_whole}\\frac{{{new_num}}}{{{denom}}}}}$$"
    )
    ans = f"{new_whole} {new_num}/{denom}"
    return {
        "id": f"g7_frac_21_{rng.randint(100000, 999999)}",
        "subskill": "21_subtracting_fraction_from_a_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_21",
        "hints": {
            "tier_1": f"Borrow 1 from {whole}: {whole} = {new_whole} + {denom}/{denom}.",
            "tier_2": f"Subtract: {denom}/{denom} - {num}/{denom} = {new_num}/{denom}.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracted_from_whole_without_borrowing"]
    }


# 22. Fraction of a whole number money Rand
def arch_22_fraction_of_a_whole_number_money_rand(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([4, 5, 6, 8, 10])
    num = rng.choice([2, 3, 5]) if denom > 5 else 3
    unit_val = rng.choice([15, 20, 25, 30])
    total_rand = unit_val * denom
    res = num * unit_val
    prompt = (
        f"Calculate $\\frac{{{num}}}{{{denom}}}$ of R{total_rand}.\n\n"
        f"Show both division and multiplication steps."
    )
    sol = (
        f"**Step 1:** Divide the total amount by the denominator to find the value of one fractional part:\n"
        f"$$\\text{{R}}{total_rand} \\div {denom} = \\text{{R}}{unit_val}$$\n\n"
        f"**Step 2:** Multiply by the numerator:\n"
        f"$$\\text{{R}}{unit_val} \\times {num} = \\mathbf{{\\text{{R}}{res}}}$$"
    )
    ans = f"R{res}"
    return {
        "id": f"g7_frac_22_{rng.randint(100000, 999999)}",
        "subskill": "22_fraction_of_a_whole_number_money_rand",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_22",
        "hints": {
            "tier_1": f"Divide {total_rand} by {denom}.",
            "tier_2": f"Multiply the answer by {num}.",
            "tier_3": ans
        },
        "misconception_tags": ["multiplied_by_denominator_instead_of_dividing"]
    }


# 23. Fraction of a whole number distance km
def arch_23_fraction_of_a_whole_number_distance_km(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([3, 4, 5])
    num = rng.choice([2, 3, 4]) if denom > 3 else 2
    step_km = rng.choice([30, 40, 50])
    total_km = step_km * denom
    res_km = num * step_km
    prompt = (
        f"A bus journey between two towns in the Free State is {total_km} km.\n"
        f"The bus has completed $\\frac{{{num}}}{{{denom}}}$ of the journey.\n\n"
        f"How many kilometres has the bus traveled?"
    )
    sol = (
        f"**Step 1:** One fractional part is: $${total_km}\\text{{ km}} \\div {denom} = {step_km}\\text{{ km}}$$\n\n"
        f"**Step 2:** Multiply by {num}: $${step_km}\\text{{ km}} \\times {num} = \\mathbf{{{res_km}\\text{{ km}}}}$$"
    )
    ans = f"{res_km} km"
    return {
        "id": f"g7_frac_23_{rng.randint(100000, 999999)}",
        "subskill": "23_fraction_of_a_whole_number_distance_km",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_23",
        "hints": {
            "tier_1": f"Find 1/{denom} of {total_km}.",
            "tier_2": f"Multiply {step_km} by {num}.",
            "tier_3": ans
        },
        "misconception_tags": ["fraction_of_distance_calculation_error"]
    }


# 24. Fraction of a whole number mass kg
def arch_24_fraction_of_a_whole_number_mass_kg(rng: random.Random) -> Dict[str, Any]:
    denom = 4
    num = 3
    mass = rng.choice([60, 80, 120, 200])
    part = mass // denom
    ans_mass = num * part
    prompt = (
        f"A sack of maize flour weighs {mass} kg. A baker uses $\\frac{3}{4}$ of the sack for porridge.\n\n"
        f"What mass of flour in kilograms was used?"
    )
    sol = (
        f"**Step 1:** $\\frac{{1}}{{4}} \\text{{ of }} {mass}\\text{{ kg}} = {mass} \\div 4 = {part}\\text{{ kg}}$\n\n"
        f"**Step 2:** $\\frac{{3}}{{4}} \\text{{ of }} {mass}\\text{{ kg}} = 3 \\times {part} = \\mathbf{{{ans_mass}\\text{{ kg}}}}$"
    )
    ans = f"{ans_mass} kg"
    return {
        "id": f"g7_frac_24_{rng.randint(100000, 999999)}",
        "subskill": "24_fraction_of_a_whole_number_mass_kg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_24",
        "hints": {
            "tier_1": f"Divide {mass} by 4.",
            "tier_2": f"Multiply {part} by 3.",
            "tier_3": ans
        },
        "misconception_tags": ["mass_fraction_arithmetic_error"]
    }


# 25. Fraction of a collection or learners
def arch_25_fraction_of_a_collection_or_learners(rng: random.Random) -> Dict[str, Any]:
    total_learners = 40
    # 3/5 play soccer
    num, denom = 3, 5
    part = total_learners // denom # 8
    ans_learners = num * part # 24
    prompt = (
        f"In a Grade 7 class of {total_learners} learners, $\\frac{{{num}}}{{{denom}}}$ play soccer.\n\n"
        f"1. How many learners play soccer?\n"
        f"2. What fraction of the class does NOT play soccer?"
    )
    rem_frac = f"{denom - num}/{denom}"
    sol = (
        f"**Step 1:** Calculate soccer players:\n"
        f"$$\\frac{{{num}}}{{{denom}}} \\times {total_learners} = {num} \\times ({total_learners} \\div {denom}) = {num} \\times {part} = \\mathbf{{{ans_learners}\\text{{ learners}}}}$$\n\n"
        f"**Step 2:** Fraction not playing soccer:\n"
        f"$$1 - \\frac{{{num}}}{{{denom}}} = \\mathbf{{\\frac{{{denom - num}}}{{{denom}}}}}$$"
    )
    ans = f"1. {ans_learners} learners; 2. {rem_frac}"
    return {
        "id": f"g7_frac_25_{rng.randint(100000, 999999)}",
        "subskill": "25_fraction_of_a_collection_or_learners",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_25",
        "hints": {
            "tier_1": f"Divide {total_learners} by 5 and multiply by 3.",
            "tier_2": f"Subtract 3/5 from 1 whole.",
            "tier_3": ans
        },
        "misconception_tags": ["complementary_fraction_subtraction_error"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
