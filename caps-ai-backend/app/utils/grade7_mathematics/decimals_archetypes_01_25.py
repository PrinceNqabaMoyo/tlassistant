"""Grade 7 Mathematics - Decimal Fractions: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/01. The decimal notation for fractions.md
Uses South African comma decimal convention: 0,12 etc.
"""
import random
import math
from typing import Dict, Any, List


# 01. Place value identification tenths, hundredths, thousandths
def arch_01_place_value_identification_tenths_hundredths_thousandths(rng: random.Random) -> Dict[str, Any]:
    u = rng.randint(3, 9)
    t = rng.randint(1, 9)
    h = rng.randint(1, 9)
    th = rng.randint(1, 9)
    num_str = f"{u},{t}{h}{th}"
    prompt = (
        f"Consider the decimal number ${num_str}$.\n\n"
        f"1. Name the place value of the digit {t}.\n"
        f"2. Name the place value of the digit {h}.\n"
        f"3. Name the place value of the digit {th}."
    )
    sol = (
        f"In the decimal number ${num_str}$:\n"
        f"- The digit {t} is in the **tenths** place (first place after the decimal comma).\n"
        f"- The digit {h} is in the **hundredths** place (second place after the decimal comma).\n"
        f"- The digit {th} is in the **thousandths** place (third place after the decimal comma)."
    )
    ans = f"1. Tenths; 2. Hundredths; 3. Thousandths"
    return {
        "id": f"g7_dec_01_{rng.randint(100000, 999999)}",
        "subskill": "01_place_value_identification_tenths_hundredths_thousandths",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dec_01",
        "hints": {
            "tier_1": "1st digit after comma = tenths, 2nd = hundredths, 3rd = thousandths.",
            "tier_2": f"Digits in order: {t} (tenths), {h} (hundredths), {th} (thousandths).",
            "tier_3": ans
        },
        "misconception_tags": ["confused_tenths_with_tens"]
    }


# 02. Digit value in decimal number
def arch_02_digit_value_in_decimal_number(rng: random.Random) -> Dict[str, Any]:
    u = rng.randint(1, 8)
    t = rng.choice([3, 4, 5])
    h = rng.choice([6, 7, 8])
    num_str = f"{u},{t}{h}"
    prompt = (
        f"In the decimal number ${num_str}$:\n\n"
        f"1. What is the value of the digit {t} as a common fraction and as a decimal?\n"
        f"2. What is the value of the digit {h} as a common fraction and as a decimal?"
    )
    sol = (
        f"**Step 1:** The digit {t} is in the tenths place, so its value is:\n"
        f"$$\\frac{{{t}}}{{10}} = 0,{t}$$\n\n"
        f"**Step 2:** The digit {h} is in the hundredths place, so its value is:\n"
        f"$$\\frac{{{h}}}{{100}} = 0,0{h}$$"
    )
    ans = f"1. {t}/10 or 0,{t}; 2. {h}/100 or 0,0{h}"
    return {
        "id": f"g7_dec_02_{rng.randint(100000, 999999)}",
        "subskill": "02_digit_value_in_decimal_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_02",
        "hints": {
            "tier_1": "Tenths place = /10; Hundredths place = /100.",
            "tier_2": f"{t}/10 = 0,{t} and {h}/100 = 0,0{h}.",
            "tier_3": ans
        },
        "misconception_tags": ["place_value_fraction_notation_error"]
    }


# 03. Convert tenth fraction to decimal
def arch_03_convert_tenth_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 7, 9])
    prompt = (
        f"Write the common fraction $\\frac{{{n}}}{{10}}$ in decimal notation."
    )
    sol = (
        f"**Answer:** $\\frac{{{n}}}{{10}} = \\mathbf{{0,{n}}}$."
    )
    ans = f"0,{n}"
    return {
        "id": f"g7_dec_03_{rng.randint(100000, 999999)}",
        "subskill": "03_convert_tenth_fraction_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_03",
        "hints": {
            "tier_1": "Tenths means one digit after the decimal comma.",
            "tier_2": f"Write 0, followed by {n}.",
            "tier_3": ans
        },
        "misconception_tags": ["added_extra_leading_zero_to_tenths"]
    }


# 04. Convert hundredth fraction to decimal
def arch_04_convert_hundredth_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 7, 19, 43, 85])
    dec = f"0,{n:02d}"
    prompt = (
        f"Write the common fraction $\\frac{{{n}}}{{100}}$ in decimal notation."
    )
    sol = (
        f"**Answer:** $\\frac{{{n}}}{{100}} = \\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_04_{rng.randint(100000, 999999)}",
        "subskill": "04_convert_hundredth_fraction_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_04",
        "hints": {
            "tier_1": "Hundredths means two digits after the decimal comma.",
            "tier_2": f"For single-digit numbers like 4/100, write 0,04.",
            "tier_3": ans
        },
        "misconception_tags": ["omitted_placeholder_zero_in_hundredths"]
    }


# 05. Convert thousandth fraction to decimal
def arch_05_convert_thousandth_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 27, 147, 999])
    dec = f"0,{n:03d}"
    prompt = (
        f"Write the fraction $\\frac{{{n}}}{{1\\ 000}}$ in decimal notation."
    )
    sol = (
        f"**Answer:** $\\frac{{{n}}}{{1\\ 000}} = \\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_05_{rng.randint(100000, 999999)}",
        "subskill": "05_convert_thousandth_fraction_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_05",
        "hints": {
            "tier_1": "Thousandths means three digits after the decimal comma.",
            "tier_2": f"Pad with zeros if fewer than 3 digits.",
            "tier_3": ans
        },
        "misconception_tags": ["omitted_placeholder_zeros_thousandths"]
    }


# 06. Convert mixed fraction to decimal
def arch_06_convert_mixed_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(3, 12)
    n = rng.choice([7, 19, 45])
    dec = f"{w},{n:02d}"
    prompt = (
        f"Write the mixed number ${w}\\frac{{{n}}}{{100}}$ in decimal notation."
    )
    sol = (
        f"**Answer:** ${w}\\frac{{{n}}}{{100}} = \\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_06_{rng.randint(100000, 999999)}",
        "subskill": "06_convert_mixed_fraction_to_decimal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dec_06",
        "hints": {
            "tier_1": f"The whole number {w} goes before the comma.",
            "tier_2": f"The fraction {n}/100 goes after the comma.",
            "tier_3": ans
        },
        "misconception_tags": ["whole_number_lost_in_decimal_conversion"]
    }


# 07. Convert decimal to common fraction simplified
def arch_07_convert_decimal_to_common_fraction_simplified(rng: random.Random) -> Dict[str, Any]:
    # e.g. 0,6 -> 6/10 = 3/5 or 0,25 -> 25/100 = 1/4 or 0,75 -> 3/4
    pair = rng.choice([(6, 10, 3, 5), (8, 10, 4, 5), (25, 100, 1, 4), (75, 100, 3, 4), (15, 100, 3, 20)])
    num, denom, s_num, s_denom = pair
    dec_str = f"0,{num}" if denom == 10 else f"0,{num:02d}"
    prompt = (
        f"Convert the decimal fraction ${dec_str}$ into a common fraction in its **simplest form**."
    )
    sol = (
        f"**Step 1:** Write the decimal as a fraction over {denom}:\n"
        f"$${dec_str} = \\frac{{{num}}}{{{denom}}}$$\n\n"
        f"**Step 2:** Simplify by dividing by the common factor:\n"
        f"$$\\frac{{{num}}}{{{denom}}} = \\mathbf{{\\frac{{{s_num}}}{{{s_denom}}}}}$$"
    )
    ans = f"{s_num}/{s_denom}"
    return {
        "id": f"g7_dec_07_{rng.randint(100000, 999999)}",
        "subskill": "07_convert_decimal_to_common_fraction_simplified",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_07",
        "hints": {
            "tier_1": f"Write {num} over {denom}.",
            "tier_2": "Simplify top and bottom.",
            "tier_3": ans
        },
        "misconception_tags": ["unsimplified_common_fraction_from_decimal"]
    }


# 08. Expanded notation to decimal standard form
def arch_08_expanded_notation_to_decimal_standard_form(rng: random.Random) -> Dict[str, Any]:
    u = rng.randint(2, 9)
    t = rng.randint(1, 9)
    h = rng.randint(1, 9)
    th = rng.randint(1, 9)
    prompt = (
        f"Write the following expanded expression as a single decimal number in standard notation:\n"
        f"$${u} + \\frac{{{t}}}{{10}} + \\frac{{{h}}}{{100}} + \\frac{{{th}}}{{1\\ 000}}$$"
    )
    dec = f"{u},{t}{h}{th}"
    sol = (
        f"**Step 1:** Combine the place values:\n"
        f"- Units: {u}\n"
        f"- Tenths: {t}\n"
        f"- Hundredths: {h}\n"
        f"- Thousandths: {th}\n\n"
        f"**Answer:** $\\mathbf{{{dec}}}$."
    )
    ans = f"{dec}"
    return {
        "id": f"g7_dec_08_{rng.randint(100000, 999999)}",
        "subskill": "08_expanded_notation_to_decimal_standard_form",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_08",
        "hints": {
            "tier_1": "Place each digit in its correct column after the decimal comma.",
            "tier_2": f"Tenths={t}, Hundredths={h}, Thousandths={th}.",
            "tier_3": ans
        },
        "misconception_tags": ["expanded_decimal_place_order_confusion"]
    }


# 09. Decimal to expanded fraction form
def arch_09_decimal_to_expanded_fraction_form(rng: random.Random) -> Dict[str, Any]:
    u = rng.randint(1, 7)
    t = rng.randint(2, 8)
    h = rng.randint(2, 8)
    dec = f"{u},{t}{h}"
    prompt = (
        f"Write the decimal number ${dec}$ in expanded fractional notation (as a sum of units, tenths, and hundredths)."
    )
    sol = (
        f"**Answer:** $${dec} = \\mathbf{{{u} + \\frac{{{t}}}{{10}} + \\frac{{{h}}}{{100}}}}$$"
    )
    ans = f"{u} + {t}/10 + {h}/100"
    return {
        "id": f"g7_dec_09_{rng.randint(100000, 999999)}",
        "subskill": "09_decimal_to_expanded_fraction_form",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_09",
        "hints": {
            "tier_1": f"Split into {u} (whole), {t}/10, and {h}/100.",
            "tier_2": f"Write as {u} + {t}/10 + {h}/100.",
            "tier_3": ans
        },
        "misconception_tags": ["expanded_fraction_breakdown_error"]
    }


# 10. Comparing two decimal numbers
def arch_10_comparing_two_decimal_numbers(rng: random.Random) -> Dict[str, Any]:
    # e.g. 0,35 vs 0,4 (common misconception: 35 > 4 so 0,35 > 0,4)
    prompt = (
        "Insert the correct symbol ($<$, $>$, or $=$) between the two decimals:\n"
        "$$0,35 \\quad \\square \\quad 0,4$$\n\n"
        "Explain your reasoning using tenths and hundredths."
    )
    sol = (
        "**Step 1:** Compare place by place starting from the tenths:\n"
        "- In $0,35$, there are 3 tenths and 5 hundredths ($35$ hundredths).\n"
        "- In $0,4$, there are 4 tenths and 0 hundredths ($40$ hundredths).\n\n"
        "**Step 2:** Since 3 tenths < 4 tenths (or $35$ hundredths < $40$ hundredths):\n"
        "$$0,35 < 0,4$$"
    )
    ans = "< (because 0,35 < 0,40)"
    return {
        "id": f"g7_dec_10_{rng.randint(100000, 999999)}",
        "subskill": "10_comparing_two_decimal_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_10",
        "hints": {
            "tier_1": "Pad 0,4 with a trailing zero: 0,40.",
            "tier_2": "Now compare 0,35 and 0,40.",
            "tier_3": ans
        },
        "misconception_tags": ["longer_decimal_is_larger_fallacy"]
    }


# 11. Ordering decimals ascending descending
def arch_11_ordering_decimals_ascending_descending(rng: random.Random) -> Dict[str, Any]:
    # 0,08; 0,8; 0,75; 0,105
    prompt = (
        "Arrange the following decimals in **ascending order** (from smallest to largest):\n"
        "$$0,75; \\quad 0,08; \\quad 0,8; \\quad 0,105$$\n\n"
        "Show working by writing each number with 3 decimal places."
    )
    sol = (
        "**Step 1:** Pad each number to three decimal places:\n"
        "- $0,75 = 0,750$\n"
        "- $0,08 = 0,080$\n"
        "- $0,8 = 0,800$\n"
        "- $0,105 = 0,105$\n\n"
        "**Step 2:** Compare: $80 < 105 < 750 < 800$.\n\n"
        "**Conclusion (Ascending Order):** $$\\mathbf{0,08; \\quad 0,105; \\quad 0,75; \\quad 0,8}$$"
    )
    ans = "0,08; 0,105; 0,75; 0,8"
    return {
        "id": f"g7_dec_11_{rng.randint(100000, 999999)}",
        "subskill": "11_ordering_decimals_ascending_descending",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dec_11",
        "hints": {
            "tier_1": "Pad all numbers so they each have 3 decimal digits: 0,750; 0,080; 0,800; 0,105.",
            "tier_2": "Order the whole numbers 80, 105, 750, 800.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_ordering_without_padding_error"]
    }


# 12. Rounding to nearest whole number
def arch_12_rounding_to_nearest_whole_number(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(4, 18)
    t = rng.choice([2, 3, 6, 7, 8])
    h = rng.randint(1, 9)
    dec = f"{w},{t}{h}"
    rounded = w if t < 5 else w + 1
    prompt = (
        f"Round off the decimal number ${dec}$ to the **nearest whole number**.\n\n"
        f"State the critical digit that determines whether to round up or down."
    )
    sol = (
        f"**Step 1:** Look at the first digit after the comma (the tenths digit, which is {t}).\n\n"
        f"**Step 2:** Since {t} is {'less than 5' if t < 5 else '5 or greater'}, we round {'down' if t < 5 else 'up'}.\n\n"
        f"**Conclusion:** ${dec} \\approx \\mathbf{{{rounded}}}$."
    )
    ans = f"{rounded} (critical digit is {t})"
    return {
        "id": f"g7_dec_12_{rng.randint(100000, 999999)}",
        "subskill": "12_rounding_to_nearest_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_12",
        "hints": {
            "tier_1": f"Look at tenths digit {t}.",
            "tier_2": "If 5 or more, round up; if less than 5, keep whole number unchanged.",
            "tier_3": ans
        },
        "misconception_tags": ["looked_at_hundredths_digit_for_whole_rounding"]
    }


# 13. Rounding to one decimal place tenths
def arch_13_rounding_to_one_decimal_place_tenths(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 9)
    t = rng.randint(1, 8)
    h = rng.choice([2, 4, 5, 7, 9])
    th = rng.randint(1, 9)
    dec = f"{w},{t}{h}{th}"
    new_t = t if h < 5 else t + 1
    rounded_str = f"{w},{new_t}"
    prompt = (
        f"Round off ${dec}$ to **one decimal place** (the nearest tenth)."
    )
    sol = (
        f"**Step 1:** Look at the hundredths digit ({h}).\n\n"
        f"**Step 2:** Since {h} is {'less than 5' if h < 5 else '5 or greater'}, "
        f"we {'leave the tenths digit as ' + str(t) if h < 5 else 'round the tenths digit up to ' + str(new_t)}.\n\n"
        f"**Conclusion:** ${dec} \\approx \\mathbf{{{rounded_str}}}$."
    )
    ans = f"{rounded_str}"
    return {
        "id": f"g7_dec_13_{rng.randint(100000, 999999)}",
        "subskill": "13_rounding_to_one_decimal_place_tenths",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_13",
        "hints": {
            "tier_1": f"Look at the second digit after comma ({h}).",
            "tier_2": f"Round tenths digit {t} accordingly.",
            "tier_3": ans
        },
        "misconception_tags": ["rounded_wrong_decimal_column"]
    }


# 14. Rounding to two decimal places hundredths
def arch_14_rounding_to_two_decimal_places_hundredths(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(1, 8)
    t = rng.randint(1, 8)
    h = rng.randint(1, 8)
    th = rng.choice([3, 4, 6, 7, 8])
    dec = f"{w},{t}{h}{th}"
    new_h = h if th < 5 else h + 1
    rounded_str = f"{w},{t}{new_h}"
    prompt = (
        f"Round off ${dec}$ to **two decimal places** (the nearest hundredth)."
    )
    sol = (
        f"**Step 1:** The hundredths place is {h}. Look at the thousandths digit ({th}).\n\n"
        f"**Step 2:** Since {th} is {'less than 5' if th < 5 else '5 or more'}, "
        f"the hundredths digit becomes {new_h}.\n\n"
        f"**Conclusion:** ${dec} \\approx \\mathbf{{{rounded_str}}}$."
    )
    ans = f"{rounded_str}"
    return {
        "id": f"g7_dec_14_{rng.randint(100000, 999999)}",
        "subskill": "14_rounding_to_two_decimal_places_hundredths",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_14",
        "hints": {
            "tier_1": f"Look at the third digit ({th}).",
            "tier_2": f"Keep 2 digits after comma: {rounded_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["thousandths_rounding_error"]
    }


# 15. Adding decimals same decimal places
def arch_15_adding_decimals_same_decimal_places(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(3.1, 8.9), 2)
    b = round(rng.uniform(2.1, 6.9), 2)
    tot = round(a + b, 2)
    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.2f}".replace(".", ",")
    tot_str = f"{tot:.2f}".replace(".", ",")
    prompt = (
        f"Calculate the sum using column addition (aligning the commas):\n"
        f"$${a_str} + {b_str}$$"
    )
    sol = (
        f"**Step 1:** Align decimal commas vertically:\n"
        f"$$\\begin{{array}}{{rl}} {a:.2f} \\\\ + {b:.2f} \\\\ \\hline {tot:.2f} \\end{{array}}$$\n\n"
        f"**Answer:** $\\mathbf{{{tot_str}}}$."
    )
    ans = f"{tot_str}"
    return {
        "id": f"g7_dec_15_{rng.randint(100000, 999999)}",
        "subskill": "15_adding_decimals_same_decimal_places",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_15",
        "hints": {
            "tier_1": "Line up the decimal commas.",
            "tier_2": f"Add {a_str} and {b_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_addition_carry_over_error"]
    }


# 16. Adding decimals different decimal places padding
def arch_16_adding_decimals_different_decimal_places_padding(rng: random.Random) -> Dict[str, Any]:
    # e.g. 4,7 + 3,25 -> 4,70 + 3,25 = 7,95
    a = 4.7
    b = 3.25
    tot = 7.95
    prompt = (
        "Calculate:\n"
        "$$4,7 + 3,25$$\n\n"
        "Show how you pad trailing zeros to align decimal places."
    )
    sol = (
        "**Step 1:** Pad $4,7$ with a zero so both numbers have two decimal places: $4,70$.\n\n"
        "**Step 2:** Add vertically:\n"
        "$$4,70 + 3,25 = \\mathbf{7,95}$$"
    )
    ans = "7,95"
    return {
        "id": f"g7_dec_16_{rng.randint(100000, 999999)}",
        "subskill": "16_adding_decimals_different_decimal_places_padding",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_16",
        "hints": {
            "tier_1": "Write 4,7 as 4,70.",
            "tier_2": "Add: 4,70 + 3,25 = 7,95.",
            "tier_3": ans
        },
        "misconception_tags": ["misaligned_ragged_decimal_addition"]
    }


# 17. Adding three decimal numbers
def arch_17_adding_three_decimal_numbers(rng: random.Random) -> Dict[str, Any]:
    # 12,4 + 5,08 + 0,35 = 17,83
    prompt = (
        "Calculate the sum of three decimal numbers:\n"
        "$$12,4 + 5,08 + 0,35$$\n\n"
        "Show column alignment."
    )
    sol = (
        "**Step 1:** Pad with zeros to 2 decimal places:\n"
        "$$12,40 + 5,08 + 0,35$$\n\n"
        "**Step 2:** Add column by column:\n"
        "- Hundredths: $0 + 8 + 5 = 13$ (write 3, carry 1)\n"
        "- Tenths: $1 + 4 + 0 + 3 = 8$\n"
        "- Units: $2 + 5 + 0 = 7$\n"
        "- Tens: $1$\n\n"
        "**Answer:** $\\mathbf{17,83}$."
    )
    ans = "17,83"
    return {
        "id": f"g7_dec_17_{rng.randint(100000, 999999)}",
        "subskill": "17_adding_three_decimal_numbers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_17",
        "hints": {
            "tier_1": "Line up commas and pad: 12,40 + 5,08 + 0,35.",
            "tier_2": "Add carefully with carry-over.",
            "tier_3": ans
        },
        "misconception_tags": ["three_decimal_carry_over_error"]
    }


# 18. Subtracting decimals same decimal places
def arch_18_subtracting_decimals_same_decimal_places(rng: random.Random) -> Dict[str, Any]:
    a = 8.74
    b = 3.21
    diff = 5.53
    prompt = (
        "Calculate:\n"
        "$$8,74 - 3,21$$"
    )
    sol = (
        "**Step 1:** Subtract column by column:\n"
        "- Hundredths: $4 - 1 = 3$\n"
        "- Tenths: $7 - 2 = 5$\n"
        "- Units: $8 - 3 = 5$\n\n"
        "**Answer:** $\\mathbf{5,53}$."
    )
    ans = "5,53"
    return {
        "id": f"g7_dec_18_{rng.randint(100000, 999999)}",
        "subskill": "18_subtracting_decimals_same_decimal_places",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_18",
        "hints": {
            "tier_1": "Subtract straight down.",
            "tier_2": "8,74 - 3,21 = 5,53.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_subtraction_arithmetic_error"]
    }


# 19. Subtracting decimals with borrowing
def arch_19_subtracting_decimals_with_borrowing(rng: random.Random) -> Dict[str, Any]:
    # 7,24 - 3,58 -> 3,66
    prompt = (
        "Calculate the difference showing all borrowing / regrouping:\n"
        "$$7,24 - 3,58$$"
    )
    sol = (
        "**Step 1:** Subtract hundredths: $4 - 8$ requires borrowing from tenths ($2$ tenths becomes $1$, and $4$ becomes $14$):\n"
        "$$14 - 8 = 6$$\n\n"
        "**Step 2:** Subtract tenths: $1 - 5$ requires borrowing from units ($7$ becomes $6$, and $1$ becomes $11$):\n"
        "$$11 - 5 = 6$$\n\n"
        "**Step 3:** Subtract units: $6 - 3 = 3$.\n\n"
        "**Answer:** $\\mathbf{3,66}$."
    )
    ans = "3,66"
    return {
        "id": f"g7_dec_19_{rng.randint(100000, 999999)}",
        "subskill": "19_subtracting_decimals_with_borrowing",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dec_19",
        "hints": {
            "tier_1": "You cannot subtract 8 from 4. Regroup 1 tenth into 10 hundredths.",
            "tier_2": "Regroup again across the comma.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracted_top_from_bottom_digit"]
    }


# 20. Subtracting decimal from whole number
def arch_20_subtracting_decimal_from_whole_number(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(5, 15)
    dec_part = rng.choice([0.35, 0.45, 0.65, 0.75])
    diff = round(whole - dec_part, 2)
    dec_str = f"{dec_part:.2f}".replace(".", ",")
    diff_str = f"{diff:.2f}".replace(".", ",")
    prompt = (
        f"Evaluate:\n"
        f"$${whole} - {dec_str}$$\n\n"
        f"Show how you write {whole} as a decimal before subtracting."
    )
    sol = (
        f"**Step 1:** Write {whole} as a decimal with two zeros: $${whole},00$$\n\n"
        f"**Step 2:** Subtract vertically with borrowing:\n"
        f"$${whole},00 - {dec_str} = \\mathbf{{{diff_str}}}$$"
    )
    ans = f"{diff_str}"
    return {
        "id": f"g7_dec_20_{rng.randint(100000, 999999)}",
        "subskill": "20_subtracting_decimal_from_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_20",
        "hints": {
            "tier_1": f"Write {whole} as {whole},00.",
            "tier_2": f"Borrow from {whole} to get 00 - {dec_str[2:]}.",
            "tier_3": ans
        },
        "misconception_tags": ["subtracted_from_zero_without_borrowing_whole"]
    }


# 21. Multiplying decimal by 10, 100, 1000
def arch_21_multiplying_decimal_by_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    val = 3.475
    mult = rng.choice([10, 100, 1000])
    res = round(val * mult, 3)
    val_str = f"{val:.3f}".replace(".", ",")
    res_str = f"{res}".replace(".", ",")
    shift = 1 if mult == 10 else (2 if mult == 100 else 3)
    prompt = (
        f"Calculate without using a calculator:\n"
        f"$${val_str} \\times {mult}$$\n\n"
        f"State how many places and in which direction the decimal comma shifts."
    )
    sol = (
        f"**Step 1:** Multiplying by {mult} shifts the decimal comma **{shift} place{'s' if shift > 1 else ''} to the right**.\n\n"
        f"**Answer:** $${val_str} \\times {mult} = \\mathbf{{{res_str}}}$$"
    )
    ans = f"{res_str} (shifts {shift} place{'s' if shift > 1 else ''} right)"
    return {
        "id": f"g7_dec_21_{rng.randint(100000, 999999)}",
        "subskill": "21_multiplying_decimal_by_10_100_1000",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_21",
        "hints": {
            "tier_1": f"Multiplying by {mult} moves comma {shift} places to the right.",
            "tier_2": f"{val_str} becomes {res_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["shifted_decimal_comma_left_instead_of_right"]
    }


# 22. Dividing decimal by 10, 100, 1000
def arch_22_dividing_decimal_by_10_100_1000(rng: random.Random) -> Dict[str, Any]:
    val = 45.8
    div = rng.choice([10, 100])
    res = round(val / div, 3)
    val_str = f"{val}".replace(".", ",")
    res_str = f"{res}".replace(".", ",")
    shift = 1 if div == 10 else 2
    prompt = (
        f"Calculate:\n"
        f"$${val_str} \\div {div}$$\n\n"
        f"State how the decimal comma moves."
    )
    sol = (
        f"**Step 1:** Dividing by {div} moves the decimal comma **{shift} place{'s' if shift > 1 else ''} to the left**.\n\n"
        f"**Answer:** $${val_str} \\div {div} = \\mathbf{{{res_str}}}$$"
    )
    ans = f"{res_str} (shifts {shift} place{'s' if shift > 1 else ''} left)"
    return {
        "id": f"g7_dec_22_{rng.randint(100000, 999999)}",
        "subskill": "22_dividing_decimal_by_10_100_1000",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_22",
        "hints": {
            "tier_1": f"Dividing by {div} moves comma {shift} places left.",
            "tier_2": f"Move comma left to get {res_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["shifted_comma_wrong_direction_division"]
    }


# 23. Multiplying decimal by single digit whole number
def arch_23_multiplying_decimal_by_single_digit_whole_number(rng: random.Random) -> Dict[str, Any]:
    # 2,4 * 3 = 7,2 or 3,15 * 4 = 12,60
    dec_val = rng.choice([2.4, 3.2, 4.3, 1.25])
    mult = rng.choice([3, 4, 5])
    res = round(dec_val * mult, 2)
    dec_str = f"{dec_val}".replace(".", ",")
    res_str = f"{res}".replace(".", ",")
    prompt = (
        f"Calculate:\n"
        f"$${dec_str} \\times {mult}$$"
    )
    sol = (
        f"**Step 1:** Multiply ignoring the decimal comma:\n"
        f"$${int(dec_val * 100 if dec_val == 1.25 else dec_val * 10)} \\times {mult} = {int(res * 100 if dec_val == 1.25 else res * 10)}$$\n\n"
        f"**Step 2:** Restore the decimal comma:\n"
        f"**Answer:** $\\mathbf{{{res_str}}}$."
    )
    ans = f"{res_str}"
    return {
        "id": f"g7_dec_23_{rng.randint(100000, 999999)}",
        "subskill": "23_multiplying_decimal_by_single_digit_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_23",
        "hints": {
            "tier_1": f"Multiply as whole numbers first, then insert comma.",
            "tier_2": f"{dec_str} * {mult} = {res_str}.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_comma_lost_in_multiplication"]
    }


# 24. Multiplying two decimal fractions
def arch_24_multiplying_two_decimal_fractions(rng: random.Random) -> Dict[str, Any]:
    # e.g. 0,3 * 0,4 = 0,12 or 0,2 * 0,3 = 0,06
    d1 = rng.choice([0.2, 0.3, 0.4])
    d2 = rng.choice([0.3, 0.4, 0.5])
    prod = round(d1 * d2, 2)
    s1 = f"{d1}".replace(".", ",")
    s2 = f"{d2}".replace(".", ",")
    sprod = f"{prod:.2f}".replace(".", ",")
    prompt = (
        f"Evaluate:\n"
        f"$${s1} \\times {s2}$$\n\n"
        f"Explain how you determine the number of decimal places in the product."
    )
    sol = (
        f"**Step 1:** Multiply as whole numbers: $${int(d1*10)} \\times {int(d2*10)} = {int(prod*100)}$$\n\n"
        f"**Step 2:** Count total decimal places in factors: 1 place in ${s1}$ + 1 place in ${s2}$ = 2 decimal places.\n\n"
        f"**Conclusion:** $${s1} \\times {s2} = \\mathbf{{{sprod}}}$$"
    )
    ans = f"{sprod} (1 place + 1 place = 2 decimal places)"
    return {
        "id": f"g7_dec_24_{rng.randint(100000, 999999)}",
        "subskill": "24_multiplying_two_decimal_fractions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_24",
        "hints": {
            "tier_1": "Multiply 3 * 4 = 12. Two decimal places -> 0,12.",
            "tier_2": "Count total digits behind commas in both factors.",
            "tier_3": ans
        },
        "misconception_tags": ["product_decimal_places_count_error"]
    }


# 25. Dividing decimal by whole number
def arch_25_dividing_decimal_by_whole_number(rng: random.Random) -> Dict[str, Any]:
    div = rng.choice([2, 3, 4, 5])
    quot = round(rng.uniform(1.2, 4.8), 1)
    num = round(quot * div, 1)
    num_str = f"{num}".replace(".", ",")
    quot_str = f"{quot}".replace(".", ",")
    prompt = (
        f"Calculate:\n"
        f"$${num_str} \\div {div}$$"
    )
    sol = (
        f"**Step 1:** Divide as with whole numbers, keeping the decimal comma directly in line in the quotient:\n"
        f"$${num_str} \\div {div} = \\mathbf{{{quot_str}}}$$"
    )
    ans = f"{quot_str}"
    return {
        "id": f"g7_dec_25_{rng.randint(100000, 999999)}",
        "subskill": "25_dividing_decimal_by_whole_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dec_25",
        "hints": {
            "tier_1": f"Divide {num_str} by {div}.",
            "tier_2": "Keep the comma aligned.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_comma_dropped_in_long_division"]
    }
