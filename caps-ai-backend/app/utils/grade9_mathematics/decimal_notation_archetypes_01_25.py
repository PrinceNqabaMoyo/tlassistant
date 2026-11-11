"""Grade 9 Mathematics - Decimal Notation Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/01. The decimal notation for fractions.md:
Place value, expanded notation, hundredths grids, fraction/decimal/percentage equivalence,
recurring decimals, zoomed number lines, ordering, sequences, and rounding.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .decimal_notation_svg import (
    draw_decimal_number_line_svg,
    draw_hundredths_grid_svg,
)


# ----------------------------------------------------------------------
# 01. Place Value Identification: Tenths, Hundredths, Thousandths
# ----------------------------------------------------------------------
def arch_01_place_value_identification_tenths_hundredths_thousandths(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(12, 85)
    t = rng.randint(1, 9)
    h = rng.randint(1, 9)
    th = rng.randint(1, 9)
    target = rng.choice(["tenths", "hundredths", "thousandths"])

    if target == "tenths":
        d = t
        ans_frac = f"\\frac{{{d}}}{{10}}"
        ans_dec = f"0{{,}}{d}"
    elif target == "hundredths":
        d = h
        ans_frac = f"\\frac{{{d}}}{{100}}"
        ans_dec = f"0{{,}}0{d}"
    else:
        d = th
        ans_frac = f"\\frac{{{d}}}{{1000}}"
        ans_dec = f"0{{,}}00{d}"

    num_str = f"{whole}{{,}}{t}{h}{th}"
    prompt = (
        f"In the decimal number \\({num_str}\\), state the place value and fractional value "
        f"of the digit \\({d}\\) located in the {target} position."
    )
    sol = (
        f"**Place Value Analysis:**\n"
        f"The digit \\({d}\\) is in the **{target}** position.\n"
        f"Fractional value: \\({ans_frac}\\) (or \\({ans_dec}\\))."
    )
    return {
        "id": f"g9_dec_pv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_frac,
        "expected_answer": ans_frac,
        "sample_answer": ans_frac,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify place value as {target}", "marks": 1},
            {"desc": f"State fractional value {ans_frac}", "marks": 1},
        ],
        "hints": [
            "Tenths is the 1st position after comma, hundredths 2nd, thousandths 3rd.",
            f"Write the digit {d} over the appropriate power of 10.",
            f"The value is {ans_frac}.",
        ],
    }


# ----------------------------------------------------------------------
# 02. Expanded Notation: Powers of Ten and Negative Exponents
# ----------------------------------------------------------------------
def arch_02_expanded_notation_powers_of_ten_negative_exponents(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 9)
    t = rng.randint(1, 9)
    h = rng.randint(1, 9)
    th = rng.randint(1, 9)

    num_str = f"{w}{{,}}{t}{h}{th}"
    ans = f"{w} \\times 10^0 + {t} \\times 10^{{-1}} + {h} \\times 10^{{-2}} + {th} \\times 10^{{-3}}"

    prompt = (
        f"Write the decimal \\({num_str}\\) in fully expanded exponential form using "
        f"powers of 10 with negative exponents."
    )
    sol = (
        f"**Expanded Exponential Form:**\n"
        f"\\({num_str} = {w} + \\frac{{{t}}}{{10}} + \\frac{{{h}}}{{100}} + \\frac{{{th}}}{{1000}}\\)\n"
        f"Using powers of 10:\n"
        f"\\[ = {ans} \\]"
    )
    return {
        "id": f"g9_dec_exp_not_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Decompose into tenths, hundredths, thousandths", "marks": 1},
            {"desc": "Apply negative exponents correctly", "marks": 1},
        ],
        "hints": [
            "10^(-1) = 1/10, 10^(-2) = 1/100, 10^(-3) = 1/1000.",
            f"Units digit is {w} * 10^0.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 03. Compose Decimal from Expanded Fractional Form
# ----------------------------------------------------------------------
def arch_03_compose_decimal_from_expanded_fractional_form(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(10, 99)
    t = rng.choice([0, rng.randint(1, 9)])
    h = rng.choice([0, rng.randint(1, 9)])
    th = rng.randint(1, 9)
    if t == 0 and h == 0:
        t = rng.randint(1, 9)

    ans = f"{w}{{,}}{t}{h}{th}"
    parts = [f"{w}"]
    if t > 0:
        parts.append(f"\\frac{{{t}}}{{10}}")
    if h > 0:
        parts.append(f"\\frac{{{h}}}{{100}}")
    if th > 0:
        parts.append(f"\\frac{{{th}}}{{1000}}")

    expr = " + ".join(parts)
    prompt = (
        f"Express the following sum as a single decimal number:\n\n"
        f"\\[ {expr} \\]"
    )
    sol = (
        f"**Assembling Place Values:**\n"
        f"Whole number = \\({w}\\)\n"
        f"Tenths = \\({t}\\), Hundredths = \\({h}\\), Thousandths = \\({th}\\)\n"
        f"Decimal result = \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_compose_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Align fractions to decimal positions", "marks": 1},
            {"desc": f"Correct combined decimal {ans}", "marks": 1},
        ],
        "hints": [
            "Notice which place values have 0.",
            "Combine whole number and fractional parts.",
            f"The decimal is {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 04. Hundredths Grid Shaded Area to Decimal and Percentage
# ----------------------------------------------------------------------
def arch_04_hundredths_grid_shaded_area_to_decimal_and_percentage(rng: random.Random) -> Dict[str, Any]:
    shaded = rng.choice([15, 24, 37, 48, 56, 63, 72, 85])
    svg = draw_hundredths_grid_svg(shaded_count=shaded, seed=rng.randint(1, 9999))
    dec_val = f"0{{,}}{shaded:02d}"
    pct_val = f"{shaded}\\%"
    frac_val = f"\\frac{{{shaded}}}{{100}}"

    prompt = (
        f"Consider the provided 10 × 10 grid representing one whole unit.\n\n"
        f"Determine:\n"
        f"1. The common fraction of the grid shaded in blue.\n"
        f"2. The decimal fraction represented by the shaded region.\n"
        f"3. The percentage of the grid that is shaded."
    )
    sol = (
        f"**Grid Analysis:**\n"
        f"Total squares = 100.\n"
        f"Shaded squares = {shaded}.\n"
        f"1. Common fraction: \\({frac_val}\\).\n"
        f"2. Decimal: \\({dec_val}\\).\n"
        f"3. Percentage: \\({pct_val}\\)."
    )
    return {
        "id": f"g9_dec_grid_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{frac_val}; {dec_val}; {pct_val}",
        "expected_answer": f"{frac_val}; {dec_val}; {pct_val}",
        "sample_answer": f"{frac_val}; {dec_val}; {pct_val}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 3,
        "marking_schema": [
            {"desc": f"Common fraction {frac_val}", "marks": 1},
            {"desc": f"Decimal fraction {dec_val}", "marks": 1},
            {"desc": f"Percentage {pct_val}", "marks": 1},
        ],
        "hints": [
            "Count the shaded squares out of 100.",
            "Each small square is 1/100 or 0,01 or 1%.",
            f"Result: {shaded}/100 = {dec_val} = {pct_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 05. Convert Common Fraction to Terminating Decimal
# ----------------------------------------------------------------------
def arch_05_convert_common_fraction_terminating_decimal(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (3, 8, "0{,}375", "Multiply numerator and denominator by 125: \\frac{375}{1000}"),
        (7, 20, "0{,}35", "Multiply numerator and denominator by 5: \\frac{35}{100}"),
        (13, 25, "0{,}52", "Multiply numerator and denominator by 4: \\frac{52}{100}"),
        (9, 40, "0{,}225", "Multiply numerator and denominator by 25: \\frac{225}{1000}"),
        (11, 16, "0{,}6875", "Perform long division 11 / 16"),
        (4, 5, "0{,}8", "Multiply numerator and denominator by 2: \\frac{8}{10}"),
    ]
    num, den, ans, method = rng.choice(cases)

    prompt = (
        f"Convert the common fraction \\(\\frac{{{num}}}{{{den}}}\\) into its exact decimal fraction."
    )
    sol = (
        f"**Conversion Method:**\n"
        f"{method}.\n"
        f"Result: \\(\\frac{{{num}}}{{{den}}} = {ans}\\)."
    )
    return {
        "id": f"g9_dec_frac_to_dec_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Scale to power of 10 or perform division", "marks": 1},
            {"desc": f"Correct decimal {ans}", "marks": 1},
        ],
        "hints": [
            f"Scale denominator {den} to 10, 100, or 1000.",
            "Alternatively divide numerator by denominator.",
            f"The answer is {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 06. Convert Mixed Number to Decimal Notation
# ----------------------------------------------------------------------
def arch_06_convert_mixed_number_to_decimal_notation(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 8)
    cases = [
        (3, 4, "75"),
        (1, 8, "125"),
        (3, 8, "375"),
        (7, 25, "28"),
        (9, 20, "45"),
        (17, 50, "34"),
    ]
    num, den, dec_part = rng.choice(cases)
    ans = f"{w}{{,}}{dec_part}"

    prompt = (
        f"Convert the mixed number \\({w}\\frac{{{num}}}{{{den}}}\\) into decimal notation."
    )
    sol = (
        f"**Mixed Number Conversion:**\n"
        f"Whole part = \\({w}\\).\n"
        f"Fractional part: \\(\\frac{{{num}}}{{{den}}} = 0{{,}}{dec_part}\\).\n"
        f"Combined: \\({w} + 0{{,}}{dec_part} = {ans}\\)."
    )
    return {
        "id": f"g9_dec_mixed_to_dec_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Convert fraction to 0,{dec_part}", "marks": 1},
            {"desc": f"Combine to get {ans}", "marks": 1},
        ],
        "hints": [
            "Keep the whole number part in front of the comma.",
            f"Convert {num}/{den} to decimals.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 07. Convert Terminating Decimal to Simplified Common Fraction
# ----------------------------------------------------------------------
def arch_07_convert_terminating_decimal_to_simplified_common_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("0{,}375", 375, 1000, "\\frac{3}{8}"),
        ("0{,}64", 64, 100, "\\frac{16}{25}"),
        ("0{,}08", 8, 100, "\\frac{2}{25}"),
        ("0{,}125", 125, 1000, "\\frac{1}{8}"),
        ("0{,}85", 85, 100, "\\frac{17}{20}"),
        ("0{,}48", 48, 100, "\\frac{12}{25}"),
    ]
    dec_str, num_unsimp, den_unsimp, ans = rng.choice(cases)

    prompt = (
        f"Convert the decimal fraction \\({dec_str}\\) into a common fraction in its simplest form."
    )
    sol = (
        f"**Fraction Simplification:**\n"
        f"1. Write over power of 10: \\(\\frac{{{num_unsimp}}}{{{den_unsimp}}}\\).\n"
        f"2. Simplify by dividing by the greatest common divisor:\n"
        f"\\[ = {ans} \\]"
    )
    return {
        "id": f"g9_dec_to_simp_frac_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Express as {num_unsimp}/{den_unsimp}", "marks": 1},
            {"desc": f"Simplify fully to {ans}", "marks": 1},
        ],
        "hints": [
            f"Write {dec_str} over 100 or 1000.",
            "Divide numerator and denominator by their HCF.",
            f"Simplified answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 08. Convert Percentage to Decimal and Fraction
# ----------------------------------------------------------------------
def arch_08_convert_percentage_to_decimal_and_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (35, "0{,}35", "\\frac{7}{20}"),
        (68, "0{,}68", "\\frac{17}{25}"),
        (12, "0{,}12", "\\frac{3}{25}"),
        (45, "0{,}45", "\\frac{9}{20}"),
        (84, "0{,}84", "\\frac{21}{25}"),
    ]
    pct, dec_str, frac_str = rng.choice(cases)

    prompt = (
        f"Express \\({pct}\\%\\) as:\n"
        f"1. A decimal fraction.\n"
        f"2. A common fraction in its simplest form."
    )
    sol = (
        f"**Percentage Conversions:**\n"
        f"1. Divide by 100: \\({pct}\\% = \\frac{{{pct}}}{{100}} = {dec_str}\\).\n"
        f"2. Simplify common fraction: \\(\\frac{{{pct}}}{{100}} = {frac_str}\\)."
    )
    return {
        "id": f"g9_dec_pct_conv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{dec_str}; {frac_str}",
        "expected_answer": f"{dec_str}; {frac_str}",
        "sample_answer": f"{dec_str}; {frac_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct decimal {dec_str}", "marks": 1},
            {"desc": f"Correct simplified fraction {frac_str}", "marks": 1},
        ],
        "hints": [
            "Per cent means per hundred.",
            f"Decimal: divide {pct} by 100.",
            f"Answers: {dec_str} and {frac_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 09. Convert Decimal to Percentage
# ----------------------------------------------------------------------
def arch_09_convert_decimal_to_percentage(rng: random.Random) -> Dict[str, Any]:
    dec_val = rng.choice(["0{,}085", "0{,}34", "0{,}625", "1{,}45", "0{,}04", "0{,}782"])
    num_float = float(dec_val.replace("{,}", "."))
    pct_val = f"{num_float * 100:.1f}".rstrip("0").rstrip(".").replace(".", ",") + "\\%"

    prompt = (
        f"Convert the decimal number \\({dec_val}\\) to a percentage."
    )
    sol = (
        f"**Multiply by 100%:**\n"
        f"\\[ {dec_val} \\times 100\\% = {pct_val} \\]"
    )
    return {
        "id": f"g9_dec_to_pct_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": pct_val,
        "expected_answer": pct_val,
        "sample_answer": pct_val,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Multiply by 100 to yield {pct_val}", "marks": 1},
        ],
        "hints": [
            "Multiply the decimal by 100 and add the % sign.",
            f"Shift the comma two places to the right: {pct_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 10. Recurring Decimal Notation: Single Period
# ----------------------------------------------------------------------
def arch_10_recurring_decimal_notation_single_period(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (1, 3, "0{,}\\dot{3}", "3"),
        (2, 3, "0{,}\\dot{6}", "6"),
        (1, 9, "0{,}\\dot{1}", "1"),
        (4, 9, "0{,}\\dot{4}", "4"),
        (7, 9, "0{,}\\dot{7}", "7"),
    ]
    num, den, ans, dot_digit = rng.choice(cases)

    prompt = (
        f"Convert the common fraction \\(\\frac{{{num}}}{{{den}}}\\) into decimal notation, "
        f"using recurring dot notation to indicate the repeating digit."
    )
    sol = (
        f"**Long Division & Recurring Notation:**\n"
        f"\\({num} \\div {den} = 0{dot_digit}{dot_digit}{dot_digit}\\dots\\)\n"
        f"In South African recurring notation, place a dot above the repeating digit:\n"
        f"\\[ \\frac{{{num}}}{{{den}}} = {ans} \\]"
    )
    return {
        "id": f"g9_dec_recurring_single_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify division results in repeating pattern", "marks": 1},
            {"desc": f"Correct recurring dot notation {ans}", "marks": 1},
        ],
        "hints": [
            f"Divide {num} by {den}.",
            f"Notice that {dot_digit} repeats infinitely.",
            f"Write as {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 11. Recurring Decimal Notation: Multi-Digit Period
# ----------------------------------------------------------------------
def arch_11_recurring_decimal_notation_multi_digit_period(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (5, 11, "0{,}\\dot{4}\\dot{5}", "45"),
        (7, 11, "0{,}\\dot{6}\\dot{3}", "63"),
        (1, 6, "0{,}1\\dot{6}", "6"),
        (5, 6, "0{,}8\\dot{3}", "3"),
    ]
    num, den, ans, period = rng.choice(cases)

    prompt = (
        f"Convert the fraction \\(\\frac{{{num}}}{{{den}}}\\) into a recurring decimal "
        f"using standard dot notation."
    )
    sol = (
        f"**Division:**\n"
        f"\\({num} \\div {den}\\) gives a recurring block of \\({period}\\).\n"
        f"Standard recurring notation: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_recurring_multi_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Perform division identifying repeating block", "marks": 1},
            {"desc": f"Correct recurring dot notation {ans}", "marks": 1},
        ],
        "hints": [
            f"Divide {num} by {den}.",
            "Place dots above the repeating digits.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 12. Read Point on Zoomed Decimal Number Line
# ----------------------------------------------------------------------
def arch_12_read_point_on_zoomed_decimal_number_line(rng: random.Random) -> Dict[str, Any]:
    start = rng.choice([2.0, 3.5, 4.2, 5.0])
    step = 0.1
    end = start + 0.5
    point_val = start + rng.choice([0.15, 0.25, 0.35, 0.45])
    label = "P"
    svg = draw_decimal_number_line_svg(start=start, end=end, step=step, marked_points=[(point_val, label)], seed=rng.randint(1, 9999))

    ans = f"{point_val:.2f}".replace(".", ",")
    prompt = (
        f"Consider the provided zoomed decimal coordinate axis with markings at tenths.\n\n"
        f"Read and state the exact decimal value represented by point **{label}**."
    )
    sol = (
        f"**Reading Decimal Point:**\n"
        f"The tick marks are separated by intervals of \\(0{{,}}1\\).\n"
        f"Point \\({label}\\) lies halfway between two tenths.\n"
        f"The exact value is \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_line_read_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify interval scale (0,1 per major mark)", "marks": 1},
            {"desc": f"State exact coordinate {ans}", "marks": 1},
        ],
        "hints": [
            "Observe the distance between consecutive marked ticks.",
            f"Notice that P is halfway between ticks.",
            f"Coordinate is {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 13. Plot and Locate Decimal Between Two Tenths
# ----------------------------------------------------------------------
def arch_13_plot_and_locate_decimal_between_two_tenths(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([0.3, 0.4, 0.6, 0.7, 1.2, 2.5])
    offset = rng.choice([0.02, 0.04, 0.07, 0.08])
    val = t1 + offset
    t2 = round(t1 + 0.1, 2)
    val_str = f"{val:.2f}".replace(".", ",")
    t1_str = f"{t1:.1f}".replace(".", ",")
    t2_str = f"{t2:.1f}".replace(".", ",")

    prompt = (
        f"Between which two consecutive tenths on a decimal scale does the number "
        f"\\({val_str}\\) lie?"
    )
    ans = f"Between {t1_str} and {t2_str}"
    sol = (
        f"**Tenths Placement:**\n"
        f"\\({t1_str} < {val_str} < {t2_str}\\).\n"
        f"Therefore, \\({val_str}\\) lies between \\({t1_str}\\) and \\({t2_str}\\)."
    )
    return {
        "id": f"g9_dec_between_tenths_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify lower tenth {t1_str}", "marks": 1},
            {"desc": f"Identify upper tenth {t2_str}", "marks": 1},
        ],
        "hints": [
            "Look at the first digit after the comma.",
            f"The tenths digit is {int(round(t1*10)) % 10}.",
            f"It lies between {t1_str} and {t2_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 14. Compare Two Decimals Using Inequality Symbols
# ----------------------------------------------------------------------
def arch_14_compare_two_decimals_using_inequality_symbols(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("0{,}307", "0{,}37", "<", "307 thousandths is less than 370 thousandths"),
        ("0{,}5", "0{,}05", ">", "5 tenths is greater than 5 hundredths"),
        ("1{,}24", "1{,}239", ">", "240 thousandths is greater than 239 thousandths"),
        ("0{,}089", "0{,}1", "<", "89 thousandths is less than 100 thousandths"),
        ("2{,}405", "2{,}45", "<", "405 thousandths is less than 450 thousandths"),
    ]
    d1, d2, sym, reason = rng.choice(pairs)

    prompt = (
        f"Insert the correct relational symbol (\\(<\\), \\(>\\), or \\(=\\)) to make the statement true:\n\n"
        f"\\[ {d1} \\quad \\square \\quad {d2} \\]"
    )
    sol = (
        f"**Comparison:**\n"
        f"Equalize decimal places to compare: {reason}.\n"
        f"Result: \\({d1} {sym} {d2}\\)."
    )
    return {
        "id": f"g9_dec_compare_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": sym,
        "expected_answer": sym,
        "sample_answer": sym,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct inequality symbol {sym}", "marks": 1},
        ],
        "hints": [
            "Add trailing zeros so both numbers have the same number of decimal places.",
            "Compare digits column by column from left to right.",
            f"Symbol: {sym}.",
        ],
    }


# ----------------------------------------------------------------------
# 15. Order Set of Four Decimals: Ascending / Descending
# ----------------------------------------------------------------------
def arch_15_order_set_of_four_decimals_ascending_descending(rng: random.Random) -> Dict[str, Any]:
    sets = [
        ([0.4, 0.04, 0.404, 0.44], "ascending"),
        ([1.25, 1.025, 1.205, 1.5], "ascending"),
        ([3.7, 3.07, 3.707, 3.77], "descending"),
        ([0.89, 0.9, 0.098, 0.809], "ascending"),
    ]
    nums, order = rng.choice(sets)
    if order == "ascending":
        sorted_nums = sorted(nums)
    else:
        sorted_nums = sorted(nums, reverse=True)

    orig_str = "; ".join(f"{x:.3f}".rstrip("0").rstrip(".").replace(".", ",") for x in nums)
    ans_str = "; ".join(f"{x:.3f}".rstrip("0").rstrip(".").replace(".", ",") for x in sorted_nums)

    prompt = (
        f"Arrange the following set of decimal numbers in **{order}** order:\n\n"
        f"\\[ {orig_str} \\]"
    )
    sol = (
        f"**Ordering Decimals ({order.capitalize()}):**\n"
        f"Pad with zeros to compare thousandths.\n"
        f"Ordered result: \\({ans_str}\\)."
    )
    return {
        "id": f"g9_dec_order_set_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Pad numbers with equal decimal places", "marks": 1},
            {"desc": f"Correct {order} sequence {ans_str}", "marks": 1},
        ],
        "hints": [
            "Write each number with 3 decimal digits.",
            f"Sort them from {'smallest to largest' if order=='ascending' else 'largest to smallest'}.",
            f"Correct order: {ans_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 16. Find Decimal Midpoint Between Two Numbers
# ----------------------------------------------------------------------
def arch_16_find_decimal_midpoint_between_two_numbers(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(1, 5)
    t = rng.randint(1, 8)
    a = w + t / 10 + 0.04
    b = w + t / 10 + 0.05
    mid = (a + b) / 2

    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.2f}".replace(".", ",")
    mid_str = f"{mid:.3f}".replace(".", ",")

    prompt = (
        f"Find the exact decimal number that lies exactly halfway (the midpoint) "
        f"between \\({a_str}\\) and \\({b_str}\\)."
    )
    sol = (
        f"**Midpoint Calculation:**\n"
        f"\\[ \\text{{Midpoint}} = \\frac{{{a_str} + {b_str}}}{{2}} = \\frac{{{a + b:.3f}}}{{2}} = {mid_str} \\]"
    )
    return {
        "id": f"g9_dec_midpoint_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": mid_str,
        "expected_answer": mid_str,
        "sample_answer": mid_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Add both decimals", "marks": 1},
            {"desc": f"Divide by 2 to yield {mid_str}", "marks": 1},
        ],
        "hints": [
            f"Write {a_str} as {a:.3f}0 and {b_str} as {b:.3f}0.",
            "Find the average of the two numbers.",
            f"Midpoint: {mid_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Decimal Jump Sequences: Arithmetic Step
# ----------------------------------------------------------------------
def arch_17_decimal_jump_sequences_arithmetic_step(rng: random.Random) -> Dict[str, Any]:
    start = rng.choice([0.15, 0.45, 1.25, 2.30])
    step = rng.choice([0.15, 0.25, 0.05, 0.08])
    seq = [start + i * step for i in range(5)]

    seq_str = "; ".join(f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",") for x in seq[:3])
    next_two = [f"{seq[3]:.2f}".rstrip("0").rstrip(".").replace(".", ","), f"{seq[4]:.2f}".rstrip("0").rstrip(".").replace(".", ",")]
    ans = f"{next_two[0]}; {next_two[1]}"

    prompt = (
        f"Identify the constant step of the decimal sequence and write down the next two numbers:\n\n"
        f"\\[ {seq_str}; \\dots; \\dots \\]"
    )
    sol = (
        f"**Sequence Pattern:**\n"
        f"Common difference = \\({seq[1]:.2f} - {seq[0]:.2f} = {step:.2f}\\).\n"
        f"Next term 1: \\({seq[2]:.2f} + {step:.2f} = {next_two[0]}\\).\n"
        f"Next term 2: \\({seq[3]:.2f} + {step:.2f} = {next_two[1]}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_jump_seq_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Determine step size {step}", "marks": 1},
            {"desc": f"State next two terms {ans}", "marks": 1},
        ],
        "hints": [
            "Subtract the first term from the second term to find the jump size.",
            f"Add {step} to find each subsequent term.",
            f"Next terms: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 18. Round Off to Nearest Whole Number
# ----------------------------------------------------------------------
def arch_18_round_off_to_nearest_whole_number(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(12, 85)
    t = rng.randint(1, 9)
    h = rng.randint(0, 9)
    num_str = f"{w}{{,}}{t}{h}"
    ans = w + 1 if t >= 5 else w

    prompt = (
        f"Round off \\({num_str}\\) to the nearest whole number."
    )
    sol = (
        f"**Rounding to Nearest Whole Number:**\n"
        f"Inspect tenths digit: \\({t}\\).\n"
        f"Since \\({t} {'\\ge 5' if t>=5 else '< 5'}\\), we round {'up' if t>=5 else 'down'}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_round_whole_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct rounded integer {ans}", "marks": 1},
        ],
        "hints": [
            f"Check the tenths digit ({t}).",
            "5 or more rounds up; 4 or less stays the same.",
            f"Answer is {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 19. Round Off to One Decimal Place
# ----------------------------------------------------------------------
def arch_19_round_off_to_one_decimal_place(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(4, 50)
    t = rng.randint(0, 8)
    h = rng.randint(1, 9)
    th = rng.randint(0, 9)
    num_str = f"{w}{{,}}{t}{h}{th}"

    t_rounded = t + 1 if h >= 5 else t
    ans = f"{w}{{,}}{t_rounded}"

    prompt = (
        f"Round off \\({num_str}\\) to one decimal place (the nearest tenth)."
    )
    sol = (
        f"**Rounding to 1 d.p.:**\n"
        f"Tenths digit: \\({t}\\); Hundredths digit to check: \\({h}\\).\n"
        f"Since \\({h} {'\\ge 5' if h>=5 else '< 5'}\\), round {'up' if h>=5 else 'down'}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_round_1dp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct rounded decimal {ans}", "marks": 1},
        ],
        "hints": [
            f"Look at the second digit after the comma: {h}.",
            f"{'Rounds up because >= 5' if h>=5 else 'Stays same because < 5'}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 20. Round Off to Two Decimal Places
# ----------------------------------------------------------------------
def arch_20_round_off_to_two_decimal_places(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 35)
    t = rng.randint(1, 8)
    h = rng.randint(0, 8)
    th = rng.randint(1, 9)
    fth = rng.randint(1, 9)
    num_str = f"{w}{{,}}{t}{h}{th}{fth}"

    h_rounded = h + 1 if th >= 5 else h
    ans = f"{w}{{,}}{t}{h_rounded}"

    prompt = (
        f"Round off \\({num_str}\\) to two decimal places (the nearest hundredth)."
    )
    sol = (
        f"**Rounding to 2 d.p.:**\n"
        f"Hundredths digit: \\({h}\\); Thousandths digit to check: \\({th}\\).\n"
        f"Since \\({th} {'\\ge 5' if th>=5 else '< 5'}\\), round {'up' if th>=5 else 'down'}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_round_2dp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct rounded decimal {ans}", "marks": 1},
        ],
        "hints": [
            f"Check the thousandths digit: {th}.",
            f"Round to 2 decimal places: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 21. Round Off to Three Decimal Places
# ----------------------------------------------------------------------
def arch_21_round_off_to_three_decimal_places(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(1, 20)
    t = rng.randint(1, 9)
    h = rng.randint(1, 9)
    th = rng.randint(0, 8)
    ten_th = rng.randint(1, 9)
    num_str = f"{w}{{,}}{t}{h}{th}{ten_th}"

    th_rounded = th + 1 if ten_th >= 5 else th
    ans = f"{w}{{,}}{t}{h}{th_rounded}"

    prompt = (
        f"Round off \\({num_str}\\) to three decimal places."
    )
    sol = (
        f"**Rounding to 3 d.p.:**\n"
        f"Ten-thousandths digit: \\({ten_th}\\).\n"
        f"Since \\({ten_th} {'\\ge 5' if ten_th>=5 else '< 5'}\\), round {'up' if ten_th>=5 else 'down'}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_round_3dp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct rounded decimal {ans}", "marks": 1},
        ],
        "hints": [
            f"Look at the fourth decimal place: {ten_th}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Rounding in Financial Context: Nearest 5 Cents
# ----------------------------------------------------------------------
def arch_22_rounding_in_financial_context_nearest_five_cents(rng: random.Random) -> Dict[str, Any]:
    rands = rng.randint(15, 80)
    cents = rng.choice([21, 22, 23, 24, 26, 27, 28, 29, 71, 72, 73, 74, 76, 77, 78, 79])
    raw_str = f"\\text{{R}}{rands}{{,}}{cents:02d}"

    # SA cash rounding rules:
    rem = cents % 5
    if rem in (1, 2):
        rounded_cents = cents - rem
    elif rem in (3, 4):
        rounded_cents = cents + (5 - rem)
    else:
        rounded_cents = cents

    ans = f"\\text{{R}}{rands}{{,}}{rounded_cents:02d}"
    prompt = (
        f"A till slip totals \\({raw_str}\\). Under South African cash payment rules, "
        f"cash totals are rounded to the nearest 5 cents (since 1c and 2c coins are decommissioned). "
        f"What is the final payable cash amount?"
    )
    sol = (
        f"**Cash Rounding to Nearest 5c:**\n"
        f"Cents: \\({cents}\\text{{c}}\\).\n"
        f"Distance to multiples of 5: nearest multiple of 5 is \\({rounded_cents}\\text{{c}}\\).\n"
        f"Payable cash total: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_fin_round_5c_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify closest multiple of 5c ({rounded_cents}c)", "marks": 1},
            {"desc": f"State final cash amount {ans}", "marks": 1},
        ],
        "hints": [
            "Multiples of 5 cents end in 0 or 5.",
            f"{cents}c is closest to {rounded_cents}c.",
            f"Cash total: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Rounding in Financial Context: Nearest Cent
# ----------------------------------------------------------------------
def arch_23_rounding_in_financial_context_nearest_cent(rng: random.Random) -> Dict[str, Any]:
    rands = rng.randint(120, 650)
    c1 = rng.randint(1, 9)
    c2 = rng.randint(0, 9)
    c3 = rng.randint(1, 9)
    c4 = rng.randint(1, 9)

    raw_str = f"\\text{{R}}{rands}{{,}}{c1}{c2}{c3}{c4}"
    cents_rounded = (c1 * 10 + c2) + (1 if c3 >= 5 else 0)
    ans = f"\\text{{R}}{rands}{{,}}{cents_rounded:02d}"

    prompt = (
        f"A banking interest calculation produces an unrounded balance of \\({raw_str}\\). "
        f"Round off this amount to the nearest cent (two decimal places)."
    )
    sol = (
        f"**Rounding to Nearest Cent (2 d.p.):**\n"
        f"3rd decimal digit is \\({c3}\\).\n"
        f"Since \\({c3} {'\\ge 5' if c3>=5 else '< 5'}\\), we round {'up' if c3>=5 else 'down'}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_dec_fin_round_cent_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct rounded currency amount {ans}", "marks": 1},
        ],
        "hints": [
            "Cents are represented by the first two decimal places.",
            f"The third decimal digit is {c3}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Addition of Two Decimals with Carrying
# ----------------------------------------------------------------------
def arch_24_addition_of_two_decimals_with_carrying(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(14.5, 48.8), 2)
    b = round(rng.uniform(8.7, 35.6), 2)
    tot = round(a + b, 2)

    a_str = f"{a:.2f}".replace(".", ",")
    b_str = f"{b:.2f}".replace(".", ",")
    tot_str = f"{tot:.2f}".replace(".", ",")

    prompt = (
        f"Calculate the sum by aligning the decimal commas vertically:\n\n"
        f"\\[ {a_str} + {b_str} \\]"
    )
    sol = (
        f"**Vertical Decimal Addition:**\n"
        f"Align place value columns:\n"
        f"\\({a_str} + {b_str} = {tot_str}\\)."
    )
    return {
        "id": f"g9_dec_add_carry_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": tot_str,
        "expected_answer": tot_str,
        "sample_answer": tot_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Align commas and carry correctly", "marks": 1},
            {"desc": f"Correct sum {tot_str}", "marks": 1},
        ],
        "hints": [
            "Align the decimal commas one directly under the other.",
            "Add column by column from right to left, carrying as needed.",
            f"Sum is {tot_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 25. Addition of Three Decimals with Different Lengths
# ----------------------------------------------------------------------
def arch_25_addition_of_three_decimals_different_lengths(rng: random.Random) -> Dict[str, Any]:
    w1 = rng.randint(5, 25)
    t1 = rng.randint(1, 9)
    n1 = w1 + t1 / 10

    w2 = rng.randint(1, 9)
    n2 = round(w2 + rng.randint(11, 99) / 100, 2)

    n3 = round(rng.randint(111, 899) / 1000, 3)

    tot = round(n1 + n2 + n3, 3)

    s1 = f"{n1:.1f}".replace(".", ",")
    s2 = f"{n2:.2f}".replace(".", ",")
    s3 = f"{n3:.3f}".replace(".", ",")
    tot_str = f"{tot:.3f}".replace(".", ",")

    prompt = (
        f"Evaluate the sum of three decimal fractions of varying lengths:\n\n"
        f"\\[ {s1} + {s2} + {s3} \\]"
    )
    sol = (
        f"**Addition with Place-Value Padding:**\n"
        f"Pad with trailing zeros:\n"
        f"\\({s1}00 + {s2}0 + {s3} = {tot_str}\\)."
    )
    return {
        "id": f"g9_dec_add_three_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": tot_str,
        "expected_answer": tot_str,
        "sample_answer": tot_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Align decimal commas with trailing zero padding", "marks": 1},
            {"desc": f"Accurate sum {tot_str}", "marks": 1},
        ],
        "hints": [
            "Pad the numbers with zeros so all have 3 decimal places.",
            "Add thousandths, hundredths, tenths, then whole units.",
            f"Result: {tot_str}.",
        ],
    }
