"""Grade 7 Mathematics - Common Fractions: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/01. Fractions.md
"""
import random
import math
from typing import Dict, Any, List


def _svg_number_line(numerator: int, denominator: int, width: int = 400, height: int = 80) -> str:
    """Renders a clean number line from 0 to 1 with tick marks at fractional divisions."""
    origin_x = 40
    end_x = 360
    y = 40
    span = end_x - origin_x
    step = span / denominator
    
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">',
        f'<line x1="{origin_x - 15}" y1="{y}" x2="{end_x + 15}" y2="{y}" stroke="#1e293b" stroke-width="2.5"/>',
        f'<line x1="{origin_x}" y1="{y - 10}" x2="{origin_x}" y2="{y + 10}" stroke="#1e293b" stroke-width="2"/>',
        f'<text x="{origin_x}" y="{y + 25}" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">0</text>',
        f'<line x1="{end_x}" y1="{y - 10}" x2="{end_x}" y2="{y + 10}" stroke="#1e293b" stroke-width="2"/>',
        f'<text x="{end_x}" y="{y + 25}" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1</text>',
    ]
    
    for i in range(1, denominator):
        tx = origin_x + i * step
        parts.append(f'<line x1="{tx}" y1="{y - 6}" x2="{tx}" y2="{y + 6}" stroke="#64748b" stroke-width="1.5"/>')
        
    dot_x = origin_x + numerator * step
    parts.append(f'<circle cx="{dot_x}" cy="{y}" r="5" fill="#dc2626"/>')
    parts.append(f'<text x="{dot_x}" y="{y - 12}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">P</text>')
    parts.append('</svg>')
    return "".join(parts)


# 26. Multiplying fraction by whole number
def arch_26_multiplying_fraction_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([2, 3])
    d = rng.choice([5, 7, 8])
    whole = rng.choice([2, 3, 4])
    prod_n = n * whole
    prompt = (
        f"Calculate:\n"
        f"$$\\frac{{{n}}}{{{d}}} \\times {whole}$$\n\n"
        f"Write your answer as an improper fraction and as a mixed number if greater than 1."
    )
    mixed_str = f" = {prod_n // d}\\frac{{{prod_n % d}}}{{{d}}}" if prod_n > d else ""
    sol = (
        f"**Step 1:** Multiply the numerator by the whole number, keeping the denominator:\n"
        f"$$\\frac{{{n} \\times {whole}}}{{{d}}} = \\mathbf{{\\frac{{{prod_n}}}{{{d}}}}}{mixed_str}$$"
    )
    ans = f"{prod_n}/{d}" if prod_n <= d else f"{prod_n // d} {prod_n % d}/{d} (or {prod_n}/{d})"
    return {
        "id": f"g7_frac_26_{rng.randint(100000, 999999)}",
        "subskill": "26_multiplying_fraction_by_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_26",
        "hints": {
            "tier_1": f"Multiply the top number by {whole}.",
            "tier_2": f"{n} * {whole} = {prod_n}.",
            "tier_3": ans
        },
        "misconception_tags": ["multiplied_both_numerator_and_denominator_by_whole"]
    }


# 27. Multiplying two common fractions
def arch_27_multiplying_two_common_fractions(rng: random.Random) -> Dict[str, Any]:
    n1, d1 = 2, 3
    n2, d2 = 3, 5
    # 2/3 * 3/5 = 6/15 = 2/5
    prod_n = n1 * n2
    prod_d = d1 * d2
    g = math.gcd(prod_n, prod_d)
    simp_n = prod_n // g
    simp_d = prod_d // g
    prompt = (
        f"Calculate the product and simplify to lowest terms:\n"
        f"$$\\frac{{{n1}}}{{{d1}}} \\times \\frac{{{n2}}}{{{d2}}}$$"
    )
    sol = (
        f"**Step 1:** Multiply the numerators together and the denominators together:\n"
        f"$$\\frac{{{n1} \\times {n2}}}{{{d1} \\times {d2}}} = \\frac{{{prod_n}}}{{{prod_d}}}$$\n\n"
        f"**Step 2:** Simplify by dividing by the common factor {g}:\n"
        f"$$\\frac{{{prod_n} \\div {g}}}{{{prod_d} \\div {g}}} = \\mathbf{{\\frac{{{simp_n}}}{{{simp_d}}}}}$$"
    )
    ans = f"{simp_n}/{simp_d}"
    return {
        "id": f"g7_frac_27_{rng.randint(100000, 999999)}",
        "subskill": "27_multiplying_two_common_fractions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_27",
        "hints": {
            "tier_1": "Multiply straight across: top * top and bottom * bottom.",
            "tier_2": f"6/15 simplifies to 2/5.",
            "tier_3": ans
        },
        "misconception_tags": ["cross_multiplied_instead_of_multiplying_across"]
    }


# 28. Multiplying mixed numbers
def arch_28_multiplying_mixed_numbers(rng: random.Random) -> Dict[str, Any]:
    # 1 1/2 * 2 1/3 = 3/2 * 7/3 = 21/6 = 7/2 = 3 1/2
    prompt = (
        "Calculate:\n"
        "$$1\\frac{1}{2} \\times 2\\frac{1}{3}$$\n\n"
        "Show conversion to improper fractions and give the final answer as a mixed number."
    )
    sol = (
        "**Step 1:** Convert both mixed numbers to improper fractions:\n"
        "$$1\\frac{1}{2} = \\frac{3}{2}, \\quad 2\\frac{1}{3} = \\frac{7}{3}$$\n\n"
        "**Step 2:** Multiply numerators and denominators:\n"
        "$$\\frac{3}{2} \\times \\frac{7}{3} = \\frac{21}{6}$$\n\n"
        "**Step 3:** Simplify and convert back to a mixed number:\n"
        "$$\\frac{21 \\div 3}{6 \\div 3} = \\frac{7}{2} = \\mathbf{3\\frac{1}{2}}$$"
    )
    ans = "3 1/2 (or 7/2)"
    return {
        "id": f"g7_frac_28_{rng.randint(100000, 999999)}",
        "subskill": "28_multiplying_mixed_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_28",
        "hints": {
            "tier_1": "First convert both mixed numbers into improper fractions.",
            "tier_2": "3/2 * 7/3 = 7/2 = 3 1/2.",
            "tier_3": ans
        },
        "misconception_tags": ["multiplied_wholes_and_fractions_separately"]
    }


# 29. Reciprocal of a fraction concept
def arch_29_reciprocal_of_a_fraction_concept(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 4, 5])
    d = rng.choice([7, 8, 9])
    prompt = (
        f"1. What is the mathematical definition of the **reciprocal** of a fraction?\n"
        f"2. Write down the reciprocal of $\\frac{{{n}}}{{{d}}}$.\n"
        f"3. What is the product of any non-zero fraction and its reciprocal?"
    )
    sol = (
        f"**Step 1:** The reciprocal of a fraction is obtained by swapping its numerator and denominator (inverting the fraction).\n\n"
        f"**Step 2:** The reciprocal of $\\frac{{{n}}}{{{d}}}$ is $\\mathbf{{\\frac{{{d}}}{{{n}}}}}$.\n\n"
        f"**Step 3:** The product of any number and its reciprocal is always **1** "
        f"($\\frac{{{n}}}{{{d}}} \\times \\frac{{{d}}}{{{n}}} = 1$)."
    )
    ans = f"1. Inverted fraction (swapped numerator and denominator); 2. {d}/{n}; 3. 1"
    return {
        "id": f"g7_frac_29_{rng.randint(100000, 999999)}",
        "subskill": "29_reciprocal_of_a_fraction_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_29",
        "hints": {
            "tier_1": "Flip the fraction upside down.",
            "tier_2": f"Numerator becomes {d}, denominator becomes {n}.",
            "tier_3": ans
        },
        "misconception_tags": ["reciprocal_definition_error"]
    }


# 30. Dividing fraction by whole number
def arch_30_dividing_fraction_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([2, 3, 4])
    d = rng.choice([3, 5, 7])
    whole = rng.choice([2, 3, 4])
    res_d = d * whole
    g = math.gcd(n, res_d)
    simp_n = n // g
    simp_d = res_d // g
    prompt = (
        f"Divide the fraction by the whole number:\n"
        f"$$\\frac{{{n}}}{{{d}}} \\div {whole}$$\n\n"
        f"Show conversion to multiplication by the reciprocal."
    )
    sol = (
        f"**Step 1:** Dividing by {whole} is equivalent to multiplying by its reciprocal $\\frac{{1}}{{{whole}}}$:\n"
        f"$$\\frac{{{n}}}{{{d}}} \\div {whole} = \\frac{{{n}}}{{{d}}} \\times \\frac{{1}}{{{whole}}}$$\n\n"
        f"**Step 2:** Multiply across:\n"
        f"$$\\frac{{{n} \\times 1}}{{{d} \\times {whole}}} = \\frac{{{n}}}{{{res_d}}} = \\mathbf{{\\frac{{{simp_n}}}{{{simp_d}}}}}$$"
    )
    ans = f"{simp_n}/{simp_d}"
    return {
        "id": f"g7_frac_30_{rng.randint(100000, 999999)}",
        "subskill": "30_dividing_fraction_by_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_30",
        "hints": {
            "tier_1": f"Multiply by 1/{whole}.",
            "tier_2": f"Bottom becomes {d} * {whole}.",
            "tier_3": ans
        },
        "misconception_tags": ["divided_numerator_by_whole_number_directly"]
    }


# 31. Dividing whole number by fraction
def arch_31_dividing_whole_number_by_fraction(rng: random.Random) -> Dict[str, Any]:
    whole = rng.choice([6, 8, 10, 12])
    # Divide by 2/3: 6 / (2/3) = 6 * 3/2 = 9
    n, d = 2, 3
    res = (whole * d) // n
    prompt = (
        f"Calculate:\n"
        f"$${whole} \\div \\frac{{{n}}}{{{d}}}$$"
    )
    sol = (
        f"**Step 1:** Multiply the whole number by the reciprocal of the fraction (invert and multiply):\n"
        f"$${whole} \\div \\frac{{{n}}}{{{d}}} = {whole} \\times \\frac{{{d}}}{{{n}}}$$\n\n"
        f"**Step 2:** Simplify:\n"
        f"$$\\frac{{{whole} \\times {d}}}{{{n}}} = \\frac{{{whole * d}}}{{{n}}} = \\mathbf{{{res}}}$$"
    )
    ans = f"{res}"
    return {
        "id": f"g7_frac_31_{rng.randint(100000, 999999)}",
        "subskill": "31_dividing_whole_number_by_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_31",
        "hints": {
            "tier_1": "Multiply by 3/2.",
            "tier_2": f"{whole} * 3 / 2 = {res}.",
            "tier_3": ans
        },
        "misconception_tags": ["forgot_to_invert_divisor"]
    }


# 32. Dividing fraction by fraction
def arch_32_dividing_fraction_by_fraction(rng: random.Random) -> Dict[str, Any]:
    # 3/4 / 1/2 = 3/4 * 2/1 = 6/4 = 3/2 = 1 1/2
    prompt = (
        "Evaluate and simplify:\n"
        "$$\\frac{3}{4} \\div \\frac{1}{2}$$\n\n"
        "Show your working using the 'multiply by the reciprocal' rule."
    )
    sol = (
        "**Step 1:** Invert the second fraction and change division to multiplication:\n"
        "$$\\frac{3}{4} \\div \\frac{1}{2} = \\frac{3}{4} \\times \\frac{2}{1}$$\n\n"
        "**Step 2:** Multiply across:\n"
        "$$\\frac{3 \\times 2}{4 \\times 1} = \\frac{6}{4}$$\n\n"
        "**Step 3:** Simplify to lowest terms:\n"
        "$$\\frac{6 \\div 2}{4 \\div 2} = \\frac{3}{2} = \\mathbf{1\\frac{1}{2}}$$"
    )
    ans = "1 1/2 (or 3/2)"
    return {
        "id": f"g7_frac_32_{rng.randint(100000, 999999)}",
        "subskill": "32_dividing_fraction_by_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_32",
        "hints": {
            "tier_1": "Flip 1/2 to 2/1 and multiply.",
            "tier_2": "3/4 * 2/1 = 6/4 = 3/2.",
            "tier_3": ans
        },
        "misconception_tags": ["inverted_dividend_instead_of_divisor"]
    }


# 33. Convert percentage to common fraction simplified
def arch_33_convert_percentage_to_common_fraction_simplified(rng: random.Random) -> Dict[str, Any]:
    pct, n, d = rng.choice([(25, 1, 4), (50, 1, 2), (75, 3, 4), (20, 1, 5), (40, 2, 5), (60, 3, 5), (80, 4, 5)])
    prompt = (
        f"Convert {pct}% into a common fraction in its **simplest form**."
    )
    sol = (
        f"**Step 1:** Write the percentage as a fraction with denominator 100:\n"
        f"$${pct}\\% = \\frac{{{pct}}}{{100}}$$\n\n"
        f"**Step 2:** Simplify by dividing by the highest common factor:\n"
        f"$$\\frac{{{pct}}}{{100}} = \\mathbf{{\\frac{{{n}}}{{{d}}}}}$$"
    )
    ans = f"{n}/{d}"
    return {
        "id": f"g7_frac_33_{rng.randint(100000, 999999)}",
        "subskill": "33_convert_percentage_to_common_fraction_simplified",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_33",
        "hints": {
            "tier_1": f"Put {pct} over 100.",
            "tier_2": "Simplify top and bottom.",
            "tier_3": ans
        },
        "misconception_tags": ["unsimplified_percentage_fraction"]
    }


# 34. Convert common fraction to percentage
def arch_34_convert_common_fraction_to_percentage(rng: random.Random) -> Dict[str, Any]:
    n, d, pct = rng.choice([(1, 4, 25), (3, 4, 75), (1, 2, 50), (2, 5, 40), (3, 5, 60), (7, 10, 70), (9, 20, 45)])
    prompt = (
        f"Convert the common fraction $\\frac{{{n}}}{{{d}}}$ into a percentage.\n\n"
        f"Show your calculation."
    )
    sol = (
        f"**Step 1:** Multiply the common fraction by 100%:\n"
        f"$$\\frac{{{n}}}{{{d}}} \\times 100\\% = \\frac{{{n * 100}}}{{{d}}}\\% = \\mathbf{{{pct}\\%}}$$"
    )
    ans = f"{pct}%"
    return {
        "id": f"g7_frac_34_{rng.randint(100000, 999999)}",
        "subskill": "34_convert_common_fraction_to_percentage",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_34",
        "hints": {
            "tier_1": f"Multiply {n}/{d} by 100.",
            "tier_2": f"{n * 100} / {d} = {pct}.",
            "tier_3": ans
        },
        "misconception_tags": ["fraction_to_percentage_scaling_error"]
    }


# 35. Calculate percentage of a quantity
def arch_35_calculate_percentage_of_a_quantity(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([10, 15, 20, 25, 50])
    amount = rng.choice([200, 300, 400, 500])
    res = (pct * amount) // 100
    prompt = (
        f"Calculate {pct}% of R{amount}.\n\n"
        f"Show your working using fractions."
    )
    sol = (
        f"**Step 1:** Convert {pct}% to a fraction: $$\\frac{{{pct}}}{{100}}$$\n\n"
        f"**Step 2:** Multiply by R{amount}:\n"
        f"$$\\frac{{{pct}}}{{100}} \\times \\text{{R}}{amount} = {pct} \\times {amount // 100} = \\mathbf{{\\text{{R}}{res}}}$$"
    )
    ans = f"R{res}"
    return {
        "id": f"g7_frac_35_{rng.randint(100000, 999999)}",
        "subskill": "35_calculate_percentage_of_a_quantity",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_35",
        "hints": {
            "tier_1": f"Divide {amount} by 100, then multiply by {pct}.",
            "tier_2": f"{amount // 100} * {pct} = {res}.",
            "tier_3": ans
        },
        "misconception_tags": ["percentage_calculation_decimal_shift_error"]
    }


# 36. Fraction strip visual strip comparison
def arch_36_fraction_strip_visual_strip_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Refer to fraction strip equivalents:\n"
        "One full strip is divided into 3 equal parts (thirds), and another identical strip is divided into 6 equal parts (sixths).\n\n"
        "1. How many sixths make up exactly one third?\n"
        "2. How many sixths make up two thirds?"
    )
    sol = (
        "**Step 1:** $\\frac{1}{3} = \\frac{1 \\times 2}{3 \\times 2} = \\frac{2}{6}$ $\\rightarrow$ **2 sixths**.\n\n"
        "**Step 2:** $\\frac{2}{3} = \\frac{2 \\times 2}{3 \\times 2} = \\frac{4}{6}$ $\\rightarrow$ **4 sixths**."
    )
    ans = "1. 2 sixths; 2. 4 sixths"
    return {
        "id": f"g7_frac_36_{rng.randint(100000, 999999)}",
        "subskill": "36_fraction_strip_visual_strip_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_36",
        "hints": {
            "tier_1": "Multiply top and bottom by 2.",
            "tier_2": "1/3 = 2/6, so 2/3 = 4/6.",
            "tier_3": ans
        },
        "misconception_tags": ["fraction_strip_partition_error"]
    }


# 37. Fraction on a number line plotting
def arch_37_fraction_on_a_number_line_plotting(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([4, 5, 6, 8])
    num = rng.randint(1, denom - 1)
    prompt = (
        f"A number line starts at 0 and ends at 1. The space between 0 and 1 is partitioned into {denom} equal intervals.\n\n"
        f"1. What fraction does each interval tick mark represent?\n"
        f"2. How many tick marks from 0 must you count to plot the fraction $\\frac{{{num}}}{{{denom}}}$?"
    )
    sol = (
        f"**Step 1:** Each tick mark represents $\\mathbf{{\\frac{{1}}{{{denom}}}}}$.\n\n"
        f"**Step 2:** You must count **{num} tick marks** to the right of 0 to plot $\\frac{{{num}}}{{{denom}}}$."
    )
    ans = f"1. 1/{denom}; 2. {num} tick marks"
    return {
        "id": f"g7_frac_37_{rng.randint(100000, 999999)}",
        "subskill": "37_fraction_on_a_number_line_plotting",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_37",
        "hints": {
            "tier_1": f"Each division is 1/{denom}.",
            "tier_2": f"Count {num} spaces from 0.",
            "tier_3": ans
        },
        "misconception_tags": ["counted_tick_marks_instead_of_intervals"]
    }


# 38. Fraction on a number line reading value
def arch_38_fraction_on_a_number_line_reading_value(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([5, 6, 8])
    num = rng.randint(2, denom - 1)
    svg = _svg_number_line(num, denom)
    prompt = (
        f"On the number line below from 0 to 1, point P is marked with a red dot.\n\n"
        f"Identify the common fraction represented by point P."
    )
    sol = (
        f"**Step 1:** Count the total number of equal intervals between 0 and 1: there are {denom} intervals (denominator).\n\n"
        f"**Step 2:** Count the intervals from 0 to point P: point P is at the {num}th mark.\n\n"
        f"**Conclusion:** Point P represents $\\mathbf{{\\frac{{{num}}}{{{denom}}}}}$.\n"
    )
    ans = f"{num}/{denom}"
    return {
        "id": f"g7_frac_38_{rng.randint(100000, 999999)}",
        "subskill": "38_fraction_on_a_number_line_reading_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Total Segments", "body": f"There are {denom} equal spaces between 0 and 1."},
                {"title": "Locate P", "body": f"Point P is {num} spaces from 0."},
                {"title": "Fraction", "body": f"Value is {num}/{denom}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_38",
        "hints": {
            "tier_1": "Count how many segments make up the whole.",
            "tier_2": f"Count to dot P: it is at {num} out of {denom}.",
            "tier_3": ans
        },
        "misconception_tags": ["number_line_segment_miscounting"]
    }


# 39. Fraction word problem remaining fraction
def arch_39_fraction_word_problem_remaining_fraction(rng: random.Random) -> Dict[str, Any]:
    f1_num, f1_denom = 1, 3
    f2_num, f2_denom = 1, 4
    # 1/3 on food, 1/4 on transport -> sum = 7/12 -> remaining = 5/12
    prompt = (
        "Sipho spends $\\frac{1}{3}$ of his pocket money on food and $\\frac{1}{4}$ of his pocket money on transport.\n\n"
        "1. What fraction of his pocket money does he spend altogether?\n"
        "2. What fraction of his pocket money remains for saving?"
    )
    sol = (
        "**Step 1:** Find total spent:\n"
        "$$\\frac{1}{3} + \\frac{1}{4} = \\frac{4}{12} + \\frac{3}{12} = \\mathbf{\\frac{7}{12}}$$\n\n"
        "**Step 2:** Find remaining fraction:\n"
        "$$1 - \\frac{7}{12} = \\frac{12}{12} - \\frac{7}{12} = \\mathbf{\\frac{5}{12}}$$"
    )
    ans = "1. 7/12; 2. 5/12"
    return {
        "id": f"g7_frac_39_{rng.randint(100000, 999999)}",
        "subskill": "39_fraction_word_problem_remaining_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_39",
        "hints": {
            "tier_1": "Add 1/3 and 1/4 with LCD 12.",
            "tier_2": "Subtract 7/12 from 1 whole (12/12).",
            "tier_3": ans
        },
        "misconception_tags": ["pocket_money_fraction_subtraction_error"]
    }


# 40. Fraction word problem baking recipe scaling
def arch_40_fraction_word_problem_baking_recipe_scaling(rng: random.Random) -> Dict[str, Any]:
    # Recipe requires 3/4 cup sugar. We make 2 1/2 batches.
    # 3/4 * 5/2 = 15/8 = 1 7/8 cups
    prompt = (
        "A recipe for traditional South African rusks calls for $\\frac{3}{4}$ cup of brown sugar. "
        "Aunt Mary wants to bake $2\\frac{1}{2}$ batches of rusks.\n\n"
        "How many cups of brown sugar does she need in total? Give your answer as a mixed number."
    )
    sol = (
        "**Step 1:** Convert $2\\frac{1}{2}$ to an improper fraction:\n"
        "$$2\\frac{1}{2} = \\frac{5}{2}$$\n\n"
        "**Step 2:** Multiply by $\\frac{3}{4}$:\n"
        "$$\\frac{3}{4} \\times \\frac{5}{2} = \\frac{15}{8}$$\n\n"
        "**Step 3:** Convert to a mixed number:\n"
        "$$\\frac{15}{8} = \\mathbf{1\\frac{7}{8}\\text{ cups}}$$"
    )
    ans = "1 7/8 cups"
    return {
        "id": f"g7_frac_40_{rng.randint(100000, 999999)}",
        "subskill": "40_fraction_word_problem_baking_recipe_scaling",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_40",
        "hints": {
            "tier_1": "Multiply 3/4 by 5/2.",
            "tier_2": "15/8 = 1 7/8.",
            "tier_3": ans
        },
        "misconception_tags": ["recipe_scaling_mixed_multiplication_error"]
    }


# 41. Fraction word problem sharing food equally
def arch_41_fraction_word_problem_sharing_food_equally(rng: random.Random) -> Dict[str, Any]:
    pizzas = 3
    friends = 4
    prompt = (
        f"Three large homemade pizzas are shared equally among 4 friends.\n\n"
        f"What fraction of a pizza does each friend receive?"
    )
    sol = (
        f"**Step 1:** Divide the total number of pizzas by the number of friends:\n"
        f"$$3 \\div 4 = \\mathbf{{\\frac{{3}}{{4}}}}$$\n\n"
        f"Each friend receives $\\frac{{3}}{{4}}$ of a pizza."
    )
    ans = "3/4 of a pizza"
    return {
        "id": f"g7_frac_41_{rng.randint(100000, 999999)}",
        "subskill": "41_fraction_word_problem_sharing_food_equally",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_41",
        "hints": {
            "tier_1": "Division creates a fraction: total items / number of shares.",
            "tier_2": "3 / 4 = 3/4.",
            "tier_3": ans
        },
        "misconception_tags": ["inversion_of_sharing_division"]
    }


# 42. Fraction word problem travel stages
def arch_42_fraction_word_problem_travel_stages(rng: random.Random) -> Dict[str, Any]:
    total_km = 300
    # Day 1: 2/5 -> 120 km
    # Day 2: 1/2 of remainder
    prompt = (
        f"A family drives {total_km} km to Durban for holidays.\n"
        f"- On Day 1, they drive $\\frac{2}{5}$ of the total distance.\n"
        f"- On Day 2, they drive half of the remaining distance.\n\n"
        f"1. How many kilometres did they drive on Day 1?\n"
        f"2. How many kilometres did they drive on Day 2?"
    )
    d1 = (2 * total_km) // 5 # 120
    rem = total_km - d1 # 180
    d2 = rem // 2 # 90
    sol = (
        f"**Step 1:** Day 1 distance: $$\\frac{{2}}{{5}} \\times {total_km} = 2 \\times 60 = \\mathbf{{{d1}\\text{{ km}}}}$$\n\n"
        f"**Step 2:** Remaining distance: $${total_km} - {d1} = {rem}\\text{{ km}}$$\n\n"
        f"**Step 3:** Day 2 distance: $$\\frac{{1}}{{2}} \\times {rem} = \\mathbf{{{d2}\\text{{ km}}}}$$"
    )
    ans = f"1. {d1} km; 2. {d2} km"
    return {
        "id": f"g7_frac_42_{rng.randint(100000, 999999)}",
        "subskill": "42_fraction_word_problem_travel_stages",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_42",
        "hints": {
            "tier_1": f"Find 2/5 of {total_km}.",
            "tier_2": f"Subtract to find remainder ({rem}), then take half.",
            "tier_3": ans
        },
        "misconception_tags": ["took_fraction_of_total_instead_of_remainder"]
    }


# 43. Spot the error adding denominators fallacy
def arch_43_spot_the_error_adding_denominators_fallacy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner solved the following addition problem:\n"
        "$$\\frac{1}{3} + \\frac{1}{2} = \\frac{1 + 1}{3 + 2} = \\frac{2}{5}$$\n\n"
        "1. Identify the conceptual error in the learner's method.\n"
        "2. Provide the correct solution and working."
    )
    sol = (
        "**Step 1:** The learner added the denominators together. "
        "Fractions cannot be added by adding denominators because denominators define the size of each part, not the count.\n\n"
        "**Step 2:** Correct solution using LCD (6):\n"
        "$$\\frac{1}{3} + \\frac{1}{2} = \\frac{2}{6} + \\frac{3}{6} = \\mathbf{\\frac{5}{6}}$$"
    )
    ans = "1. Added denominators directly instead of finding a common denominator; 2. 5/6"
    return {
        "id": f"g7_frac_43_{rng.randint(100000, 999999)}",
        "subskill": "43_spot_the_error_adding_denominators_fallacy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_43",
        "hints": {
            "tier_1": "You can never add denominators together when adding fractions.",
            "tier_2": "Convert to LCD = 6: 2/6 + 3/6 = 5/6.",
            "tier_3": ans
        },
        "misconception_tags": ["adding_denominators_universal_fallacy"]
    }


# 44. Spot the error simplifying by canceling terms
def arch_44_spot_the_error_simplifying_by_canceling_terms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner tried to simplify $\\frac{4 + 3}{4}$ by crossing out the 4 in the numerator and denominator, "
        "obtaining an answer of 3.\n\n"
        "Explain why this cancellation is mathematically illegal."
    )
    sol = (
        "**Answer:** You can only cancel common factors that multiply the entire numerator and denominator. "
        "You cannot cancel terms that are separated by addition or subtraction (+ or -). "
        "The correct evaluation is $\\frac{4 + 3}{4} = \\frac{7}{4} = 1\\frac{3}{4}$."
    )
    ans = "You can only cancel factors in multiplication, never terms in addition."
    return {
        "id": f"g7_frac_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spot_the_error_simplifying_by_canceling_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_44",
        "hints": {
            "tier_1": "Does 4 + 3 = 7?",
            "tier_2": "7 / 4 is not 3.",
            "tier_3": ans
        },
        "misconception_tags": ["additive_cancellation_error"]
    }


# 45. Spot the error borrowing mixed number subtraction
def arch_45_spot_the_error_borrowing_mixed_number_subtraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In calculating $4\\frac{1}{5} - 1\\frac{3}{5}$, a learner wrote:\n"
        "$$4\\frac{1}{5} = 3\\frac{11}{5} \\quad \\text{because } 1 + 10 = 11$$\n\n"
        "1. What base system error did the learner commit when borrowing?\n"
        "2. What is the correct value of $4\\frac{1}{5}$ after regrouping 1 whole as fifths?"
    )
    sol = (
        "**Step 1:** The learner borrowed as if working in base 10 (adding 10 to the numerator) instead of base 5 (adding the denominator 5).\n\n"
        "**Step 2:** $1\\text{ whole} = \\frac{5}{5}$, so:\n"
        "$$4\\frac{1}{5} = 3 + \\frac{5}{5} + \\frac{1}{5} = \\mathbf{3\\frac{6}{5}}$$"
    )
    ans = "1. Borrowed 10 instead of the denominator 5; 2. 3 6/5"
    return {
        "id": f"g7_frac_45_{rng.randint(100000, 999999)}",
        "subskill": "45_spot_the_error_borrowing_mixed_number_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_45",
        "hints": {
            "tier_1": "In fifths, 1 whole is 5/5, not 10/5.",
            "tier_2": "Add 5 to 1: 1 + 5 = 6.",
            "tier_3": ans
        },
        "misconception_tags": ["borrowing_base_10_in_fractions_fallacy"]
    }


# 46. Practical context school test score fraction to pct
def arch_46_practical_context_school_test_score_fraction_to_pct(rng: random.Random) -> Dict[str, Any]:
    score = rng.choice([16, 17, 18, 19])
    total = 20
    pct = score * 5
    prompt = (
        f"A learner scores {score} out of {total} in a Mathematics class test.\n\n"
        f"1. Express the mark as a common fraction.\n"
        f"2. Convert the score to a percentage."
    )
    sol = (
        f"**Step 1:** As a common fraction: $$\\mathbf{{\\frac{{{score}}}{{{total}}}}}$$\n\n"
        f"**Step 2:** Convert to percentage:\n"
        f"$$\\frac{{{score}}}{{{total}}} \\times 100\\% = {score} \\times 5 = \\mathbf{{{pct}\\%}}$$"
    )
    ans = f"1. {score}/20; 2. {pct}%"
    return {
        "id": f"g7_frac_46_{rng.randint(100000, 999999)}",
        "subskill": "46_practical_context_school_test_score_fraction_to_pct",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_46",
        "hints": {
            "tier_1": f"Put {score} over {total}.",
            "tier_2": f"Multiply by 100% ({score} * 5).",
            "tier_3": ans
        },
        "misconception_tags": ["test_score_percentage_conversion_error"]
    }


# 47. Practical context budget allowance fraction breakdown
def arch_47_practical_context_budget_allowance_fraction_breakdown(rng: random.Random) -> Dict[str, Any]:
    allowance = 300
    # 1/3 books = 100, 1/2 clothes = 150, rest = 50
    prompt = (
        f"Kagiso receives a monthly allowance of R{allowance}.\n"
        f"- He spends $\\frac{1}{3}$ on school stationery and books.\n"
        f"- He spends $\\frac{1}{2}$ on clothes.\n"
        f"- He saves the rest.\n\n"
        f"How much money in Rands does Kagiso save?"
    )
    spent = allowance // 3 + allowance // 2 # 100 + 150 = 250
    saved = allowance - spent # 50
    sol = (
        f"**Step 1:** Calculate stationery: $$\\frac{{1}}{{3}} \\times \\text{{R}}{allowance} = \\text{{R}}{allowance // 3}$$\n\n"
        f"**Step 2:** Calculate clothes: $$\\frac{{1}}{{2}} \\times \\text{{R}}{allowance} = \\text{{R}}{allowance // 2}$$\n\n"
        f"**Step 3:** Calculate savings: $$\\text{{R}}{allowance} - (\\text{{R}}{allowance // 3} + \\text{{R}}{allowance // 2}) = \\text{{R}}{allowance} - \\text{{R}}{spent} = \\mathbf{{\\text{{R}}{saved}}}$$"
    )
    ans = f"R{saved}"
    return {
        "id": f"g7_frac_47_{rng.randint(100000, 999999)}",
        "subskill": "47_practical_context_budget_allowance_fraction_breakdown",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_47",
        "hints": {
            "tier_1": f"1/3 of {allowance} is 100. 1/2 of {allowance} is 150.",
            "tier_2": f"Subtract 250 from {allowance}.",
            "tier_3": ans
        },
        "misconception_tags": ["allowance_allocation_arithmetic_error"]
    }


# 48. Practical context crop field allocation fractions
def arch_48_practical_context_crop_field_allocation_fractions(rng: random.Random) -> Dict[str, Any]:
    # 2/5 maize, 3/10 wheat, rest sunflowers
    # 4/10 + 3/10 = 7/10 -> rest is 3/10
    prompt = (
        "A farmer allocates his farmland as follows:\n"
        "- $\\frac{2}{5}$ for maize\n"
        "- $\\frac{3}{10}$ for wheat\n"
        "- The remainder for sunflowers\n\n"
        "What fraction of the farm is used for sunflowers?"
    )
    sol = (
        "**Step 1:** Convert $\\frac{2}{5}$ to tenths: $$\\frac{2 \\times 2}{5 \\times 2} = \\frac{4}{10}$$\n\n"
        "**Step 2:** Sum maize and wheat: $$\\frac{4}{10} + \\frac{3}{10} = \\frac{7}{10}$$\n\n"
        "**Step 3:** Remainder for sunflowers: $$1 - \\frac{7}{10} = \\mathbf{\\frac{3}{10}}$$"
    )
    ans = "3/10"
    return {
        "id": f"g7_frac_48_{rng.randint(100000, 999999)}",
        "subskill": "48_practical_context_crop_field_allocation_fractions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_frac_48",
        "hints": {
            "tier_1": "Change 2/5 into 4/10.",
            "tier_2": "Add: 4/10 + 3/10 = 7/10. Subtract from 10/10.",
            "tier_3": ans
        },
        "misconception_tags": ["crop_field_fraction_conversion_error"]
    }


# 49. Practical context water tank fractional fill
def arch_49_practical_context_water_tank_fractional_fill(rng: random.Random) -> Dict[str, Any]:
    capacity = 1200
    # Currently 3/4 full -> 900 L. 1/3 of the water in tank is used.
    # Used = 1/3 * 900 = 300 L.
    # Remaining = 600 L.
    prompt = (
        f"A rainwater tank has a capacity of {capacity} litres. It is currently $\\frac{3}{4}$ full.\n"
        f"During a dry week, $\\frac{1}{3}$ of the water in the tank is used to irrigate a community vegetable garden.\n\n"
        f"1. How many litres of water were in the tank initially?\n"
        f"2. How many litres of water were used for irrigation?"
    )
    init_vol = (3 * capacity) // 4 # 900
    used_vol = init_vol // 3 # 300
    sol = (
        f"**Step 1:** Initial water: $$\\frac{{3}}{{4}} \\times {capacity} = 3 \\times 300 = \\mathbf{{{init_vol}\\text{{ litres}}}}$$\n\n"
        f"**Step 2:** Water used: $$\\frac{{1}}{{3}} \\times {init_vol} = \\mathbf{{{used_vol}\\text{{ litres}}}}$$"
    )
    ans = f"1. {init_vol} litres; 2. {used_vol} litres"
    return {
        "id": f"g7_frac_49_{rng.randint(100000, 999999)}",
        "subskill": "49_practical_context_water_tank_fractional_fill",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_49",
        "hints": {
            "tier_1": f"3/4 of {capacity} is {init_vol}.",
            "tier_2": f"1/3 of {init_vol} is {used_vol}.",
            "tier_3": ans
        },
        "misconception_tags": ["fraction_of_capacity_instead_of_content"]
    }


# 50. Comprehensive fraction order of operations BODMAS
def arch_50_comprehensive_fraction_order_of_operations_bodmas(rng: random.Random) -> Dict[str, Any]:
    # (1/2 + 1/4) * 2/3 = 3/4 * 2/3 = 6/12 = 1/2
    prompt = (
        "Evaluate using the correct order of operations (BODMAS):\n"
        "$$\\left(\\frac{1}{2} + \\frac{1}{4}\\right) \\times \\frac{2}{3}$$\n\n"
        "Show all steps and write the final answer in simplest form."
    )
    sol = (
        "**Step 1:** Brackets first (add inside brackets with LCD 4):\n"
        "$$\\frac{1}{2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\frac{3}{4}$$\n\n"
        "**Step 2:** Multiply by $\\frac{2}{3}$:\n"
        "$$\\frac{3}{4} \\times \\frac{2}{3} = \\frac{3 \\times 2}{4 \\times 3} = \\frac{6}{12}$$\n\n"
        "**Step 3:** Simplify to lowest terms:\n"
        "$$\\frac{6 \\div 6}{12 \\div 6} = \\mathbf{\\frac{1}{2}}$$"
    )
    ans = "1/2"
    return {
        "id": f"g7_frac_50_{rng.randint(100000, 999999)}",
        "subskill": "50_comprehensive_fraction_order_of_operations_bodmas",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_frac_50",
        "hints": {
            "tier_1": "Calculate the brackets first: 1/2 + 1/4 = 3/4.",
            "tier_2": "Then multiply: 3/4 * 2/3 = 1/2.",
            "tier_3": ans
        },
        "misconception_tags": ["bodmas_order_of_operations_violation"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
