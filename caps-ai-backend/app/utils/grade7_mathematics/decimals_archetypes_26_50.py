"""Grade 7 Mathematics - Decimal Fractions: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/01. The decimal notation for fractions.md
Uses South African comma decimal convention: 0,12 etc.
"""
import random
import math
from typing import Dict, Any, List


def _svg_100_grid(shaded: int, width: int = 240, height: int = 240) -> str:
    """Renders a 10x10 hundredths grid."""
    grid_size = 10
    cell_size = 18
    start_x, start_y = 30, 30
    
    rects = []
    for row in range(grid_size):
        for col in range(grid_size):
            idx = row * grid_size + col
            fill = "#2563eb" if idx < shaded else "#ffffff"
            x = start_x + col * cell_size
            y = start_y + row * cell_size
            rects.append(
                f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
                f'fill="{fill}" stroke="#64748b" stroke-width="1"/>'
            )
            
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'<rect x="{start_x}" y="{start_y}" width="{grid_size * cell_size}" height="{grid_size * cell_size}" '
        f'fill="none" stroke="#1e293b" stroke-width="2"/>'
        f'{"".join(rects)}'
        f'</svg>'
    )


# 26. Dividing whole numbers yielding decimal quotient
def arch_26_dividing_whole_numbers_yielding_decimal_quotient(rng: random.Random) -> Dict[str, Any]:
    # e.g. 15 / 4 = 3,75 or 7 / 2 = 3,5 or 9 / 4 = 2,25
    a, b, res_str = rng.choice([(7, 2, "3,5"), (15, 4, "3,75"), (9, 4, "2,25"), (18, 5, "3,6"), (27, 5, "5,4")])
    prompt = (
        f"Divide the two whole numbers to find the exact decimal quotient:\n"
        f"$${a} \\div {b}$$\n\n"
        f"Show working including adding decimal zeros."
    )
    sol = (
        f"**Step 1:** Divide {a} by {b}:\n"
        f"$${a} \\div {b} = {a // b} \\text{{ with remainder }} {a % b}$$\n\n"
        f"**Step 2:** Place a decimal comma and add zeros to divide the remainder:\n"
        f"**Answer:** $\\mathbf{{{res_str}}}$."
    )
    ans = f"{res_str}"
    return {
        "id": f"g7_dec_26_{rng.randint(100000, 999999)}",
        "subskill": "26_dividing_whole_numbers_yielding_decimal_quotient",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_26",
        "hints": {
            "tier_1": f"Write {a} as {a},0 and continue dividing.",
            "tier_2": f"{a} / {b} = {res_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["stopped_at_remainder_instead_of_decimal"]
    }


# 27. Common fraction half quarter to decimal
def arch_27_common_fraction_half_quarter_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n, d, dec = rng.choice([(1, 2, "0,5"), (1, 4, "0,25"), (3, 4, "0,75")])
    prompt = (
        f"Convert the benchmark common fraction $\\frac{{{n}}}{{{d}}}$ into decimal notation.\n\n"
        f"Show the equivalent fraction with denominator 10 or 100."
    )
    mult = 100 // d
    sol = (
        f"**Step 1:** Scale to denominator 100:\n"
        f"$$\\frac{{{n} \\times {mult}}}{{{d} \\times {mult}}} = \\frac{{{n * mult}}}{{100}}$$\n\n"
        f"**Step 2:** Write as a decimal:\n"
        f"$$\\frac{{{n * mult}}}{{100}} = \\mathbf{{{dec}}}$$"
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_27_{rng.randint(100000, 999999)}",
        "subskill": "27_common_fraction_half_quarter_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_27",
        "hints": {
            "tier_1": f"Scale {d} to 100.",
            "tier_2": f"{n}/{d} = {n * mult}/100.",
            "tier_3": ans
        },
        "misconception_tags": ["benchmark_fraction_decimal_memorization_error"]
    }


# 28. Common fraction fifths to decimal
def arch_28_common_fraction_fifths_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([1, 2, 3, 4])
    dec = f"0,{n * 2}"
    prompt = (
        f"Convert the common fraction $\\frac{{{n}}}{{5}}$ into a decimal fraction.\n\n"
        f"Show conversion using denominator 10."
    )
    sol = (
        f"**Step 1:** Multiply numerator and denominator by 2 to get denominator 10:\n"
        f"$$\\frac{{{n} \\times 2}}{{5 \\times 2}} = \\frac{{{n * 2}}}{{10}}$$\n\n"
        f"**Step 2:** Write in decimal notation: $\\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_28_{rng.randint(100000, 999999)}",
        "subskill": "28_common_fraction_fifths_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_28",
        "hints": {
            "tier_1": "Multiply top and bottom by 2.",
            "tier_2": f"{n * 2}/10 = {dec}.",
            "tier_3": ans
        },
        "misconception_tags": ["fifths_decimal_conversion_error"]
    }


# 29. Common fraction eighths to decimal
def arch_29_common_fraction_eighths_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n, dec = rng.choice([(1, "0,125"), (3, "0,375"), (5, "0,625"), (7, "0,875")])
    prompt = (
        f"Convert $\\frac{{{n}}}{{8}}$ into decimal notation using denominator 1 000."
    )
    sol = (
        f"**Step 1:** Multiply numerator and denominator by 125 ($8 \\times 125 = 1\\ 000$):\n"
        f"$$\\frac{{{n} \\times 125}}{{8 \\times 125}} = \\frac{{{n * 125}}}{{1\\ 000}}$$\n\n"
        f"**Step 2:** Write as a decimal: $\\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_29_{rng.randint(100000, 999999)}",
        "subskill": "29_common_fraction_eighths_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_29",
        "hints": {
            "tier_1": "Multiply top and bottom by 125.",
            "tier_2": f"{n * 125}/1000 = {dec}.",
            "tier_3": ans
        },
        "misconception_tags": ["eighths_to_thousandths_scaling_error"]
    }


# 30. Percentage to decimal conversion
def arch_30_percentage_to_decimal_conversion(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([5, 12, 35, 68, 75])
    dec = f"0,{pct:02d}"
    prompt = (
        f"Convert {pct}% into a decimal fraction."
    )
    sol = (
        f"**Step 1:** Divide by 100 (move the comma two places to the left):\n"
        f"$${pct}\\% = \\frac{{{pct}}}{{100}} = \\mathbf{{{dec}}}$$"
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_30_{rng.randint(100000, 999999)}",
        "subskill": "30_percentage_to_decimal_conversion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_30",
        "hints": {
            "tier_1": f"Divide {pct} by 100.",
            "tier_2": "Shift decimal comma 2 places left.",
            "tier_3": ans
        },
        "misconception_tags": ["percentage_to_decimal_shift_error"]
    }


# 31. Decimal to percentage conversion
def arch_31_decimal_to_percentage_conversion(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([8, 15, 45, 60, 85])
    dec = f"0,{pct:02d}"
    prompt = (
        f"Convert the decimal fraction ${dec}$ into a percentage."
    )
    sol = (
        f"**Step 1:** Multiply by 100%:\n"
        f"$${dec} \\times 100\\% = \\mathbf{{{pct}\\%}}$$"
    )
    ans = f"{pct}%"
    return {
        "id": f"g7_dec_31_{rng.randint(100000, 999999)}",
        "subskill": "31_decimal_to_percentage_conversion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_31",
        "hints": {
            "tier_1": f"Multiply {dec} by 100.",
            "tier_2": f"Move comma 2 places right: {pct}%.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_to_percentage_shift_error"]
    }


# 32. Three way equivalence table fraction decimal pct
def arch_32_three_way_equivalence_table_fraction_decimal_pct(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete the 3-way equivalence table:\n\n"
        "| Common Fraction | Decimal Fraction | Percentage |\n"
        "| :--- | :--- | :--- |\n"
        "| $\\frac{1}{4}$ | [a] | 25% |\n"
        "| [b] | 0,5 | 50% |\n"
        "| $\\frac{4}{5}$ | 0,8 | [c] |\n\n"
        "Find the missing values [a], [b], and [c]."
    )
    sol = (
        "**[a]:** $\\frac{1}{4} = \\mathbf{0,25}$\n"
        "**[b]:** $0,5 = \\mathbf{\\frac{1}{2}}$\n"
        "**[c]:** $0,8 = \\mathbf{80\\%}$"
    )
    ans = "[a] = 0,25; [b] = 1/2; [c] = 80%"
    return {
        "id": f"g7_dec_32_{rng.randint(100000, 999999)}",
        "subskill": "32_three_way_equivalence_table_fraction_decimal_pct",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dec_32",
        "hints": {
            "tier_1": "1/4 = 0,25. 0,5 = 1/2. 0,8 = 80%.",
            "tier_2": "Fill in each box.",
            "tier_3": ans
        },
        "misconception_tags": ["three_way_equivalence_confusion"]
    }


# 33. Decimal on a number line reading
def arch_33_decimal_on_a_number_line_reading(rng: random.Random) -> Dict[str, Any]:
    t = rng.choice([3, 4, 6, 7])
    prompt = (
        f"A number line between 0 and 1 is divided into 10 equal intervals (tenths). "
        f"Point M is placed on the {t}th tick mark from 0.\n\n"
        f"What decimal value is represented by point M?"
    )
    dec = f"0,{t}"
    sol = (
        f"**Step 1:** Each interval represents one tenth ($0,1$).\n\n"
        f"**Step 2:** Point M is {t} tenths from 0: $${t} \\times 0,1 = \\mathbf{{{dec}}}$$"
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_33_{rng.randint(100000, 999999)}",
        "subskill": "33_decimal_on_a_number_line_reading",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_33",
        "hints": {
            "tier_1": "Each mark is 0,1.",
            "tier_2": f"Count {t} marks: 0,{t}.",
            "tier_3": ans
        },
        "misconception_tags": ["number_line_decimal_tick_error"]
    }


# 34. Decimal on a number line plotting
def arch_34_decimal_on_a_number_line_plotting(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Between which two consecutive whole numbers does the decimal $6,74$ lie on a number line?\n\n"
        "Which of those two whole numbers is it closer to?"
    )
    sol = (
        "**Step 1:** $6,74$ lies strictly between **6 and 7**.\n\n"
        "**Step 2:** Since the tenths digit is 7 (which is $\\ge 5$), it is closer to **7**."
    )
    ans = "Between 6 and 7; closer to 7"
    return {
        "id": f"g7_dec_34_{rng.randint(100000, 999999)}",
        "subskill": "34_decimal_on_a_number_line_plotting",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_34",
        "hints": {
            "tier_1": "The whole number part is 6.",
            "tier_2": "6,74 is between 6 and 7, closer to 7.",
            "tier_3": ans
        },
        "misconception_tags": ["adjacent_integer_identification_error"]
    }


# 35. Grid 100 square shaded decimal representation
def arch_35_grid_100_square_shaded_decimal_representation(rng: random.Random) -> Dict[str, Any]:
    shaded = rng.choice([25, 34, 48, 62, 75])
    svg = _svg_100_grid(shaded)
    dec = f"0,{shaded:02d}"
    prompt = (
        f"A 10x10 grid contains 100 equal small squares. Exactly {shaded} squares are shaded blue.\n\n"
        f"1. What decimal fraction represents the shaded portion?\n"
        f"2. What decimal fraction represents the unshaded portion?"
    )
    unshaded = 100 - shaded
    unshaded_dec = f"0,{unshaded:02d}"
    sol = (
        f"**Step 1:** Shaded portion: $$\\frac{{{shaded}}}{{100}} = \\mathbf{{{dec}}}$$\n\n"
        f"**Step 2:** Unshaded portion: $$\\frac{{{unshaded}}}{{100}} = \\mathbf{{{unshaded_dec}}}$$"
    )
    ans = f"1. {dec}; 2. {unshaded_dec}"
    return {
        "id": f"g7_dec_35_{rng.randint(100000, 999999)}",
        "subskill": "35_grid_100_square_shaded_decimal_representation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Total Squares", "body": "10 rows * 10 columns = 100 squares (hundredths)."},
                {"title": "Shaded Part", "body": f"{shaded} out of 100 = {dec}."},
                {"title": "Unshaded Part", "body": f"100 - {shaded} = {unshaded} squares = {unshaded_dec}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_35",
        "hints": {
            "tier_1": f"Write {shaded} as a decimal out of 100: {dec}.",
            "tier_2": f"Subtract from 1: 1,00 - {dec} = {unshaded_dec}.",
            "tier_3": ans
        },
        "misconception_tags": ["grid_counting_decimal_error"]
    }


# 36. Money Rand cents addition total cost
def arch_36_money_rand_cents_addition_total_cost(rng: random.Random) -> Dict[str, Any]:
    c1 = 14.50
    c2 = 28.75
    c3 = 9.25
    tot = c1 + c2 + c3 # 52.50
    prompt = (
        "Thabo buys stationery for school:\n"
        "- Notebook: R14,50\n"
        "- Calculator pouch: R28,75\n"
        "- Pen set: R9,25\n\n"
        "Calculate the total cost in Rands and cents."
    )
    sol = (
        "**Step 1:** Align amounts by decimal comma:\n"
        "$$\\text{R}14,50 + \\text{R}28,75 + \\text{R}9,25$$\n\n"
        "**Step 2:** Add cents: $50 + 75 + 25 = 150\\text{ cents} = \\text{R}1,50$\n"
        "**Step 3:** Add Rands: $14 + 28 + 9 + 1 = 52$\n\n"
        "**Total:** $\\mathbf{\\text{R}52,50}$."
    )
    ans = "R52,50"
    return {
        "id": f"g7_dec_36_{rng.randint(100000, 999999)}",
        "subskill": "36_money_rand_cents_addition_total_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_36",
        "hints": {
            "tier_1": "Line up the decimal commas for the three prices.",
            "tier_2": "14,50 + 28,75 + 9,25 = 52,50.",
            "tier_3": ans
        },
        "misconception_tags": ["money_decimal_addition_error"]
    }


# 37. Money Rand cents subtraction calculating change
def arch_37_money_rand_cents_subtraction_calculating_change(rng: random.Random) -> Dict[str, Any]:
    bill = 63.45
    paid = 100.00
    change = paid - bill # 36.55
    prompt = (
        f"A customer's grocery bill comes to R63,45. The customer pays with a R100 banknote.\n\n"
        f"Calculate the change received."
    )
    sol = (
        f"**Step 1:** Subtract the bill from R100,00:\n"
        f"$$\\text{{R}}100,00 - \\text{{R}}63,45 = \\mathbf{{\\text{{R}}36,55}}$$"
    )
    ans = "R36,55"
    return {
        "id": f"g7_dec_37_{rng.randint(100000, 999999)}",
        "subskill": "37_money_rand_cents_subtraction_calculating_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_37",
        "hints": {
            "tier_1": "Write 100 as 100,00.",
            "tier_2": "Subtract 63,45 from 100,00 with borrowing.",
            "tier_3": ans
        },
        "misconception_tags": ["change_subtraction_borrowing_error"]
    }


# 38. Money multiplication unit price
def arch_38_money_multiplication_unit_price(rng: random.Random) -> Dict[str, Any]:
    unit_price = 4.25
    quantity = rng.choice([4, 6, 8])
    total = round(unit_price * quantity, 2)
    tot_str = f"{total:.2f}".replace(".", ",")
    prompt = (
        f"Exercise books cost R4,25 each. A school buys {quantity} exercise books.\n\n"
        f"Calculate the total cost in Rands."
    )
    sol = (
        f"**Step 1:** Multiply price by quantity:\n"
        f"$$\\text{{R}}4,25 \\times {quantity} = \\mathbf{{\\text{{R}}{tot_str}}}$$"
    )
    ans = f"R{tot_str}"
    return {
        "id": f"g7_dec_38_{rng.randint(100000, 999999)}",
        "subskill": "38_money_multiplication_unit_price",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_38",
        "hints": {
            "tier_1": f"Multiply 4,25 by {quantity}.",
            "tier_2": f"4 * {quantity} + 0,25 * {quantity}.",
            "tier_3": ans
        },
        "misconception_tags": ["unit_price_decimal_multiplication_error"]
    }


# 39. Money division equal split
def arch_39_money_division_equal_split(rng: random.Random) -> Dict[str, Any]:
    total = 75.00
    friends = 4
    each = 18.75
    prompt = (
        f"A lunch bill of R{total:.2f}".replace(".", ",") + f" is shared equally among {friends} friends.\n\n"
        f"How much does each friend pay?"
    )
    sol = (
        f"**Step 1:** Divide total cost by {friends}:\n"
        f"$$\\text{{R}}75,00 \\div 4 = \\mathbf{{\\text{{R}}18,75}}$$"
    )
    ans = "R18,75"
    return {
        "id": f"g7_dec_39_{rng.randint(100000, 999999)}",
        "subskill": "39_money_division_equal_split",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_39",
        "hints": {
            "tier_1": "Divide 75 by 4.",
            "tier_2": "75 / 4 = 18,75.",
            "tier_3": ans
        },
        "misconception_tags": ["money_division_remainder_error"]
    }


# 40. Measurement length metres to centimetres decimal
def arch_40_measurement_length_metres_to_centimetres_decimal(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2.4, 3.75, 5.08, 0.65])
    cm = round(m * 100, 1)
    m_str = f"{m}".replace(".", ",")
    cm_str = f"{int(cm) if cm.is_integer() else cm}".replace(".", ",")
    prompt = (
        f"Convert {m_str} metres into centimetres.\n\n"
        f"State the conversion factor."
    )
    sol = (
        f"**Step 1:** $1\\text{{ metre}} = 100\\text{{ centimetres}}$.\n\n"
        f"**Step 2:** Multiply by 100:\n"
        f"$${m_str} \\times 100 = \\mathbf{{{cm_str}\\text{{ cm}}}}$$"
    )
    ans = f"{cm_str} cm"
    return {
        "id": f"g7_dec_40_{rng.randint(100000, 999999)}",
        "subskill": "40_measurement_length_metres_to_centimetres_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_40",
        "hints": {
            "tier_1": "Multiply by 100.",
            "tier_2": f"Move comma 2 places right: {cm_str} cm.",
            "tier_3": ans
        },
        "misconception_tags": ["divided_instead_of_multiplied_for_metric_conversion"]
    }


# 41. Measurement mass kilograms to grams decimal
def arch_41_measurement_mass_kilograms_to_grams_decimal(rng: random.Random) -> Dict[str, Any]:
    kg = rng.choice([1.5, 2.25, 0.45, 3.075])
    g = round(kg * 1000)
    kg_str = f"{kg}".replace(".", ",")
    prompt = (
        f"Convert {kg_str} kilograms into grams."
    )
    sol = (
        f"**Step 1:** $1\\text{{ kg}} = 1\\ 000\\text{{ g}}$.\n\n"
        f"**Step 2:** Multiply by 1 000:\n"
        f"$${kg_str} \\times 1\\ 000 = \\mathbf{{{g}\\text{{ g}}}}$$"
    )
    ans = f"{g} g"
    return {
        "id": f"g7_dec_41_{rng.randint(100000, 999999)}",
        "subskill": "41_measurement_mass_kilograms_to_grams_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_41",
        "hints": {
            "tier_1": "Multiply by 1 000.",
            "tier_2": f"Move comma 3 places right: {g} g.",
            "tier_3": ans
        },
        "misconception_tags": ["metric_mass_conversion_factor_error"]
    }


# 42. Measurement capacity litres to millilitres decimal
def arch_42_measurement_capacity_litres_to_millilitres_decimal(rng: random.Random) -> Dict[str, Any]:
    l_val = rng.choice([0.75, 1.2, 2.5, 0.05])
    ml = round(l_val * 1000)
    l_str = f"{l_val}".replace(".", ",")
    prompt = (
        f"Convert {l_str} litres into millilitres (ml)."
    )
    sol = (
        f"**Step 1:** $1\\text{{ litre}} = 1\\ 000\\text{{ ml}}$.\n\n"
        f"**Step 2:** Multiply by 1 000:\n"
        f"$${l_str} \\times 1\\ 000 = \\mathbf{{{ml}\\text{{ ml}}}}$$"
    )
    ans = f"{ml} ml"
    return {
        "id": f"g7_dec_42_{rng.randint(100000, 999999)}",
        "subskill": "42_measurement_capacity_litres_to_millilitres_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_42",
        "hints": {
            "tier_1": "Multiply by 1 000.",
            "tier_2": f"{l_str} * 1000 = {ml} ml.",
            "tier_3": ans
        },
        "misconception_tags": ["capacity_conversion_factor_error"]
    }


# 43. Spot the error ragged decimal addition alignment
def arch_43_spot_the_error_ragged_decimal_addition_alignment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner attempted to add $3,4$ and $1,25$ by right-aligning the digits without aligning the commas:\n"
        "$$\\begin{array}{r} 3,4 \\\\ + 1,25 \\\\ \\hline 1,59 \\end{array}$$\n\n"
        "1. Explain what fundamental mistake the learner made.\n"
        "2. Provide the correct column setup and sum."
    )
    sol = (
        "**Step 1:** The learner right-aligned the numbers as if adding integers, adding 4 tenths to 5 hundredths.\n\n"
        "**Step 2:** The decimal commas must be aligned vertically (padding $3,4$ as $3,40$):\n"
        "$$3,40 + 1,25 = \\mathbf{4,65}$$"
    )
    ans = "1. Failed to align decimal commas (right-aligned digits instead); 2. 4,65"
    return {
        "id": f"g7_dec_43_{rng.randint(100000, 999999)}",
        "subskill": "43_spot_the_error_ragged_decimal_addition_alignment",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_43",
        "hints": {
            "tier_1": "You must line up commas, not the last digits.",
            "tier_2": "3,40 + 1,25 = 4,65.",
            "tier_3": ans
        },
        "misconception_tags": ["right_aligning_decimal_addition_fallacy"]
    }


# 44. Spot the error longer decimal is larger fallacy
def arch_44_spot_the_error_longer_decimal_is_larger_fallacy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner claims that $0,175$ is greater than $0,4$ because 175 is much larger than 4.\n\n"
        "Explain why this claim is incorrect using place value concepts."
    )
    sol = (
        "**Answer:** When comparing decimals, you must compare place values starting from the tenths column. "
        "In $0,4$, there are 4 tenths ($400$ thousandths), whereas in $0,175$ there is only 1 tenth ($175$ thousandths). "
        "Since $4$ tenths $> 1$ tenth, $0,4 > 0,175$."
    )
    ans = "Incorrect because 4 tenths (0,400) is greater than 1 tenth and 75 thousandths (0,175)."
    return {
        "id": f"g7_dec_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spot_the_error_longer_decimal_is_larger_fallacy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_44",
        "hints": {
            "tier_1": "Look at the tenths digit of each number.",
            "tier_2": "4 tenths is bigger than 1 tenth.",
            "tier_3": ans
        },
        "misconception_tags": ["longer_decimal_treated_as_larger_whole_number"]
    }


# 45. Spot the error trailing zero removal confusion
def arch_45_spot_the_error_trailing_zero_removal_confusion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner says: 'Since trailing zeros at the end of a decimal do not change its value (0,50 = 0,5), "
        "we can also remove internal zeros, so 0,05 must be equal to 0,5.'\n\n"
        "Correct the learner's logic."
    )
    sol = (
        "**Answer:** Trailing zeros at the very end of a decimal fraction do not change place values ($50$ hundredths = $5$ tenths). "
        "However, an internal zero in $0,05$ is a critical placeholder showing zero tenths and 5 hundredths ($5$ hundredths is ten times smaller than $5$ tenths: $0,05 \\neq 0,5$)."
    )
    ans = "Internal zeros are placeholders that determine place value; 0,05 is 5 hundredths, which is ten times smaller than 0,5."
    return {
        "id": f"g7_dec_45_{rng.randint(100000, 999999)}",
        "subskill": "45_spot_the_error_trailing_zero_removal_confusion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_45",
        "hints": {
            "tier_1": "Is 5 cents equal to 50 cents?",
            "tier_2": "The placeholder zero keeps 5 in the hundredths column.",
            "tier_3": ans
        },
        "misconception_tags": ["internal_zero_removal_fallacy"]
    }


# 46. Spot the error decimal multiplication point placement
def arch_46_spot_the_error_decimal_multiplication_point_placement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner calculated $0,2 \\times 0,3 = 0,6$.\n\n"
        "1. Identify the learner's error.\n"
        "2. State the correct answer with working."
    )
    sol = (
        "**Step 1:** The learner multiplied $2 \\times 3 = 6$ but only included one decimal place instead of two decimal places.\n\n"
        "**Step 2:** One decimal place in $0,2$ + one decimal place in $0,3$ = 2 decimal places in the product:\n"
        "$$0,2 \\times 0,3 = \\mathbf{0,06}$$"
    )
    ans = "1. Failed to count decimal places across both factors; 2. 0,06"
    return {
        "id": f"g7_dec_46_{rng.randint(100000, 999999)}",
        "subskill": "46_spot_the_error_decimal_multiplication_point_placement",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_46",
        "hints": {
            "tier_1": "Count total digits behind commas: 1 + 1 = 2.",
            "tier_2": "Two decimal places: 0,06.",
            "tier_3": ans
        },
        "misconception_tags": ["single_decimal_place_multiplication_error"]
    }


# 47. Practical context fuel pump litres and cost
def arch_47_practical_context_fuel_pump_litres_and_cost(rng: random.Random) -> Dict[str, Any]:
    litres = 20
    price_per_l = 22.50
    total = litres * price_per_l # 450.00
    prompt = (
        f"A motorist fills up with {litres} litres of petrol at a fuel station. "
        f"The price of petrol is R22,50 per litre.\n\n"
        f"Calculate the total cost in Rands."
    )
    sol = (
        f"**Step 1:** Multiply litres by price per litre:\n"
        f"$${litres} \\times \\text{{R}}22,50 = \\mathbf{{\\text{{R}}450,00}}$$"
    )
    ans = "R450,00"
    return {
        "id": f"g7_dec_47_{rng.randint(100000, 999999)}",
        "subskill": "47_practical_context_fuel_pump_litres_and_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_47",
        "hints": {
            "tier_1": "Multiply 20 by 22,50.",
            "tier_2": "20 * 22,5 = 450.",
            "tier_3": ans
        },
        "misconception_tags": ["petrol_cost_multiplication_error"]
    }


# 48. Practical context athletics race times hundredths second
def arch_48_practical_context_athletics_race_times_hundredths_second(rng: random.Random) -> Dict[str, Any]:
    t1 = 12.35
    t2 = 12.18
    diff = round(t1 - t2, 2)
    s_diff = f"{diff:.2f}".replace(".", ",")
    prompt = (
        f"In a 100 m school sprint final, Runner A finishes in 12,35 seconds and Runner B finishes in 12,18 seconds.\n\n"
        f"1. Which runner won the race?\n"
        f"2. By how many hundredths of a second did the winner beat the other runner?"
    )
    sol = (
        f"**Step 1:** **Runner B** won because 12,18 seconds is faster (less time) than 12,35 seconds.\n\n"
        f"**Step 2:** Time difference: $$12,35\\text{{ s}} - 12,18\\text{{ s}} = \\mathbf{{{s_diff}\\text{{ seconds}}}}$$ (17 hundredths of a second)."
    )
    ans = f"1. Runner B; 2. {s_diff} seconds (or 17 hundredths of a second)"
    return {
        "id": f"g7_dec_48_{rng.randint(100000, 999999)}",
        "subskill": "48_practical_context_athletics_race_times_hundredths_second",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_48",
        "hints": {
            "tier_1": "Faster race time means smaller number.",
            "tier_2": f"Subtract 12,18 from 12,35 = {s_diff}.",
            "tier_3": ans
        },
        "misconception_tags": ["race_time_comparison_inversion"]
    }


# 49. Practical context supermarket till slip rounding
def arch_49_practical_context_supermarket_till_slip_rounding(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([84.23, 115.68, 49.92])
    tot_str = f"{total:.2f}".replace(".", ",")
    # South African cash rounding to nearest 10c / 5c: nearest 10 cents
    rounded_10c = round(round(total * 10) / 10, 2)
    r_str = f"{rounded_10c:.2f}".replace(".", ",")
    prompt = (
        f"In South African retail stores when paying cash, bills are rounded to the nearest 10 cents.\n\n"
        f"Round the bill of R{tot_str} to the nearest 10 cents."
    )
    sol = (
        f"**Step 1:** Look at the hundredths digit of R{tot_str}.\n\n"
        f"**Step 2:** Round to the nearest tenth of a Rand (10 cents):\n"
        f"$$\\text{{R}}{tot_str} \\approx \\mathbf{{\\text{{R}}{r_str}}}$$"
    )
    ans = f"R{r_str}"
    return {
        "id": f"g7_dec_49_{rng.randint(100000, 999999)}",
        "subskill": "49_practical_context_supermarket_till_slip_rounding",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_49",
        "hints": {
            "tier_1": "Look at the last digit (cents).",
            "tier_2": f"Round to one decimal place: R{r_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["cash_rounding_nearest_ten_cents_error"]
    }


# 50. Comprehensive multi step decimal word problem
def arch_50_comprehensive_multi_step_decimal_word_problem(rng: random.Random) -> Dict[str, Any]:
    # Mom buys 3 kg apples at R14,50/kg and 2 bread loaves at R16,75 each. She pays R100.
    cost_apples = 3 * 14.50 # 43.50
    cost_bread = 2 * 16.75 # 33.50
    tot_cost = cost_apples + cost_bread # 77.00
    change = 100.00 - tot_cost # 23.00
    prompt = (
        "Mrs Mthembu goes shopping:\n"
        "- She buys 3 kg of apples at R14,50 per kg.\n"
        "- She buys 2 loaves of bread at R16,75 each.\n"
        "- She pays with a R100 banknote.\n\n"
        "1. Calculate the cost of the apples.\n"
        "2. Calculate the cost of the bread.\n"
        "3. Calculate the total bill.\n"
        "4. Calculate how much change Mrs Mthembu receives."
    )
    sol = (
        f"**Step 1:** Cost of apples: $$3 \\times \\text{{R}}14,50 = \\mathbf{{\\text{{R}}43,50}}$$\n\n"
        f"**Step 2:** Cost of bread: $$2 \\times \\text{{R}}16,75 = \\mathbf{{\\text{{R}}33,50}}$$\n\n"
        f"**Step 3:** Total bill: $$\\text{{R}}43,50 + \\text{{R}}33,50 = \\mathbf{{\\text{{R}}77,00}}$$\n\n"
        f"**Step 4:** Change: $$\\text{{R}}100,00 - \\text{{R}}77,00 = \\mathbf{{\\text{{R}}23,00}}$$"
    )
    ans = "1. R43,50; 2. R33,50; 3. R77,00; 4. R23,00"
    return {
        "id": f"g7_dec_50_{rng.randint(100000, 999999)}",
        "subskill": "50_comprehensive_multi_step_decimal_word_problem",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_dec_50",
        "hints": {
            "tier_1": "Calculate each item's total first.",
            "tier_2": "Add them up to get R77,00, then subtract from R100.",
            "tier_3": ans
        },
        "misconception_tags": ["multi_item_decimal_budget_error"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
