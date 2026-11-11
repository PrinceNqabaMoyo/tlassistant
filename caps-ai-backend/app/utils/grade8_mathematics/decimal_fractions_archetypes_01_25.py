"""
Grade 8 Mathematics - Fractions in Decimal Notation Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Fractions in decimal notation.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_decimal_number_line_svg


def _fmt_sa(val: float, places: int = 2) -> str:
    s = f"{val:.{places}f}".rstrip("0").rstrip(".") if places > 2 else f"{val:.{places}f}"
    if s == "-0":
        s = "0"
    return s.replace(".", ",")


def arch_01_place_value_identification_tenths_hundredths_thousandths(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(12, 89)
    d1 = rng.randint(1, 9)
    d2 = rng.randint(0, 9)
    d3 = rng.randint(1, 9)
    dec_val = f"{whole},{d1}{d2}{d3}"

    target_pos = rng.choice(["tenths", "hundredths", "thousandths"])
    if target_pos == "tenths":
        digit = str(d1)
        val_name = f"0,{d1} or {d1}/10"
    elif target_pos == "hundredths":
        digit = str(d2)
        val_name = f"0,0{d2} or {d2}/100"
    else:
        digit = str(d3)
        val_name = f"0,00{d3} or {d3}/1000"

    return {
        "title": "Place Value in Decimal Fractions",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "01_place_value_identification_tenths_hundredths_thousandths",
        "difficulty": "easy",
        "question_text": (
            f"Consider the decimal fraction **{dec_val}**.\n\n"
            f"Identify the digit in the **{target_pos}** position."
        ),
        "correct_answer": digit,
        "marking_schema": [
            f"Identify the digit in the {target_pos} column: {digit} (1 mark)",
        ],
        "hints": [
            "In a decimal fraction, the first digit after the decimal comma is tenths, the second is hundredths, and the third is thousandths.",
            f"Locate the column corresponding to {target_pos}.",
            f"The digit in the {target_pos} place is {digit} (having value {val_name}).",
        ],
        "misconception_tags": ["decimal_place_value_column_confusion"],
        "diagram_spec": None,
    }


def arch_02_ordering_positive_decimals_ascending(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(3, 9)
    vals = [
        round(base + 0.4, 3),
        round(base + 0.04, 3),
        round(base + 0.44, 3),
        round(base + 0.004, 3),
        round(base + 0.404, 3),
    ]
    shuffled = list(vals)
    rng.shuffle(shuffled)
    sorted_vals = sorted(vals)

    disp_shuffled = "; ".join(_fmt_sa(x, 3) for x in shuffled)
    disp_sorted = "; ".join(_fmt_sa(x, 3) for x in sorted_vals)

    return {
        "title": "Ordering Positive Decimals (Ascending)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "02_ordering_positive_decimals_ascending",
        "difficulty": "medium",
        "question_text": (
            f"Arrange the following set of decimal numbers in **ascending order** (from smallest to largest):\n\n"
            f"$${disp_shuffled}$$"
        ),
        "correct_answer": disp_sorted,
        "marking_schema": [
            f"Write with equal decimal places: {disp_sorted} (2 marks)",
        ],
        "hints": [
            "Write all numbers with the same number of decimal places (thousandths) by adding trailing zeros.",
            "Compare the numbers column by column from left to right: units, then tenths, hundredths, thousandths.",
            f"The correct ascending order is: {disp_sorted}.",
        ],
        "misconception_tags": ["longer_decimal_is_larger_misconception"],
        "diagram_spec": None,
    }


def arch_03_ordering_positive_decimals_descending(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(10, 25)
    vals = [
        round(base + 0.7, 3),
        round(base + 0.07, 3),
        round(base + 0.77, 3),
        round(base + 0.077, 3),
    ]
    shuffled = list(vals)
    rng.shuffle(shuffled)
    sorted_desc = sorted(vals, reverse=True)

    disp_shuffled = "; ".join(_fmt_sa(x, 3) for x in shuffled)
    disp_sorted = "; ".join(_fmt_sa(x, 3) for x in sorted_desc)

    return {
        "title": "Ordering Decimals (Descending)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "03_ordering_positive_decimals_descending",
        "difficulty": "medium",
        "question_text": (
            f"Arrange the following numbers in **descending order** (from largest to smallest):\n\n"
            f"$${disp_shuffled}$$"
        ),
        "correct_answer": disp_sorted,
        "marking_schema": [
            f"Order descending correctly: {disp_sorted} (2 marks)",
        ],
        "hints": [
            "Descending order means from largest to smallest.",
            "Equate decimal lengths: 0,7 = 0,700; 0,07 = 0,070; 0,77 = 0,770; 0,077.",
            f"Order: {disp_sorted}.",
        ],
        "misconception_tags": ["ascending_descending_order_inversion"],
        "diagram_spec": None,
    }


def arch_04_ordering_signed_decimals_ascending(rng: random.Random) -> Dict[str, Any]:
    v1 = round(rng.uniform(1.2, 4.8), 2)
    v2 = round(rng.uniform(0.1, 0.9), 2)
    v3 = round(-rng.uniform(0.1, 0.9), 2)
    v4 = round(-rng.uniform(1.2, 4.8), 2)
    vals = [v1, v2, v3, v4]
    shuffled = list(vals)
    rng.shuffle(shuffled)
    sorted_vals = sorted(vals)

    disp_shuffled = "; ".join(_fmt_sa(x, 2) for x in shuffled)
    disp_sorted = "; ".join(_fmt_sa(x, 2) for x in sorted_vals)

    return {
        "title": "Ordering Signed Decimals",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "04_ordering_signed_decimals_ascending",
        "difficulty": "medium",
        "question_text": (
            f"Arrange the following signed decimal numbers in **ascending order** (from most negative to largest positive):\n\n"
            f"$${disp_shuffled}$$"
        ),
        "correct_answer": disp_sorted,
        "marking_schema": [
            f"Order signed decimals ascending: {disp_sorted} (2 marks)",
        ],
        "hints": [
            "Negative numbers with larger absolute values are further to the left on a number line, so they are smaller.",
            "Group negatives first in order of value, followed by positive decimals.",
            f"The correct ascending order is: {disp_sorted}.",
        ],
        "misconception_tags": ["negative_decimal_magnitude_inversion"],
        "diagram_spec": None,
    }


def arch_05_comparing_two_decimals_inequality(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(0, 9)
    pair_type = rng.choice(["first_larger", "second_larger", "equal"])
    if pair_type == "first_larger":
        a = round(w + 0.35, 2)
        b = round(w + 0.305, 3)
        ans = ">"
    elif pair_type == "second_larger":
        a = round(w + 0.08, 2)
        b = round(w + 0.8, 1)
        ans = "<"
    else:
        a = round(w + 0.4, 1)
        b = round(w + 0.400, 3)
        ans = "="

    a_str = _fmt_sa(a, 3)
    b_str = _fmt_sa(b, 3)

    return {
        "title": "Comparing Decimals with Inequality Symbols",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "05_comparing_two_decimals_inequality",
        "difficulty": "easy",
        "question_text": (
            f"Insert $<$, $>$, or $=$ between the two decimal numbers to make the statement true:\n\n"
            f"$${a_str} \\quad \\boxed{{\\phantom{{M}}}} \\quad {b_str}$$"
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Insert correct relation symbol: '{ans}' (1 mark)",
        ],
        "hints": [
            "Compare place values column by column.",
            f"Writing both with equal decimal places: {a_str} vs {b_str}.",
            f"Since {a_str} is {ans} {b_str}, the correct symbol is '{ans}'.",
        ],
        "misconception_tags": ["decimal_comparison_shorter_is_smaller_error"],
        "diagram_spec": None,
    }


def arch_06_finding_decimal_between_two_given_decimals(rng: random.Random) -> Dict[str, Any]:
    base = round(rng.uniform(1.0, 8.0), 1)
    d1 = round(base + 0.02, 2)
    d2 = round(base + 0.03, 2)
    mid = round((d1 + d2) / 2, 3)

    d1_str = _fmt_sa(d1, 2)
    d2_str = _fmt_sa(d2, 2)
    mid_str = _fmt_sa(mid, 3)

    return {
        "title": "Finding a Decimal Between Two Numbers",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "06_finding_decimal_between_two_given_decimals",
        "difficulty": "medium",
        "question_text": (
            f"Find the decimal number that lies exactly halfway between **{d1_str}** and **{d2_str}**."
        ),
        "correct_answer": mid_str,
        "marking_schema": [
            f"Add and divide by 2: ({d1_str} + {d2_str}) / 2 = {mid_str} (2 marks)",
        ],
        "hints": [
            f"Add trailing zeros: {d1_str} = {d1_str}0 and {d2_str} = {d2_str}0.",
            f"Now look for the number halfway between {d1_str}0 and {d2_str}0.",
            f"Halfway is {mid_str}.",
        ],
        "misconception_tags": ["discrete_number_fallacy_in_decimals"],
        "diagram_spec": None,
    }


def arch_07_rounding_to_nearest_whole_number(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(14, 99)
    tenth = rng.choice([1, 2, 3, 4, 6, 7, 8, 9])
    hundredth = rng.randint(0, 9)
    val = float(f"{whole}.{tenth}{hundredth}")
    ans = round(val)

    return {
        "title": "Rounding Decimals to Nearest Whole Number",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "07_rounding_to_nearest_whole_number",
        "difficulty": "easy",
        "question_text": (
            f"Round off **{_fmt_sa(val, 2)}** to the nearest whole number."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Round to nearest whole number: {ans} (1 mark)",
        ],
        "hints": [
            "Look at the digit immediately after the comma (the tenths place).",
            f"The tenths digit is {tenth}. If it is 5 or greater, round up; otherwise keep the whole number.",
            f"The rounded whole number is {ans}.",
        ],
        "misconception_tags": ["rounding_digit_direction_error"],
        "diagram_spec": None,
    }


def arch_08_rounding_to_one_decimal_place(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(3, 45)
    d1 = rng.randint(0, 8)
    d2 = rng.choice([2, 3, 5, 7, 8])
    d3 = rng.randint(1, 9)
    val = float(f"{whole}.{d1}{d2}{d3}")
    rounded = round(val, 1)

    return {
        "title": "Rounding to One Decimal Place (Tenths)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "08_rounding_to_one_decimal_place",
        "difficulty": "easy",
        "question_text": (
            f"Round off **{_fmt_sa(val, 3)}** to **one decimal place**."
        ),
        "correct_answer": _fmt_sa(rounded, 1),
        "marking_schema": [
            f"Round to 1 d.p.: {_fmt_sa(rounded, 1)} (1 mark)",
        ],
        "hints": [
            "Identify the tenths digit. Look at the digit to its immediate right (the hundredths digit).",
            f"The hundredths digit is {d2}.",
            f"Rounding {_fmt_sa(val, 3)} gives {_fmt_sa(rounded, 1)}.",
        ],
        "misconception_tags": ["rounding_precision_truncation_slip"],
        "diagram_spec": None,
    }


def arch_09_rounding_to_two_decimal_places(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(5, 60)
    d1 = rng.randint(1, 8)
    d2 = rng.randint(0, 8)
    d3 = rng.choice([1, 4, 5, 6, 9])
    val = float(f"{whole}.{d1}{d2}{d3}")
    rounded = round(val, 2)

    return {
        "title": "Rounding to Two Decimal Places (Hundredths)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "09_rounding_to_two_decimal_places",
        "difficulty": "easy",
        "question_text": (
            f"Round off **{_fmt_sa(val, 3)}** to **two decimal places**."
        ),
        "correct_answer": _fmt_sa(rounded, 2),
        "marking_schema": [
            f"Round to 2 d.p.: {_fmt_sa(rounded, 2)} (1 mark)",
        ],
        "hints": [
            "Look at the third digit after the decimal comma (the thousandths digit).",
            f"The thousandths digit is {d3}.",
            f"Rounding to hundredths gives {_fmt_sa(rounded, 2)}.",
        ],
        "misconception_tags": ["rounding_precision_truncation_slip"],
        "diagram_spec": None,
    }


def arch_10_rounding_to_three_decimal_places(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(1, 15)
    d1 = rng.randint(1, 9)
    d2 = rng.randint(0, 9)
    d3 = rng.randint(0, 8)
    d4 = rng.choice([2, 5, 6, 8])
    val = float(f"{whole}.{d1}{d2}{d3}{d4}")
    rounded = round(val, 3)

    return {
        "title": "Rounding to Three Decimal Places",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "10_rounding_to_three_decimal_places",
        "difficulty": "medium",
        "question_text": (
            f"Round off **{_fmt_sa(val, 4)}** to **three decimal places**."
        ),
        "correct_answer": _fmt_sa(rounded, 3),
        "marking_schema": [
            f"Round to 3 d.p.: {_fmt_sa(rounded, 3)} (1 mark)",
        ],
        "hints": [
            "To round to three decimal places, inspect the fourth digit after the decimal comma.",
            f"The fourth digit is {d4}.",
            f"Rounded value is {_fmt_sa(rounded, 3)}.",
        ],
        "misconception_tags": ["rounding_precision_truncation_slip"],
        "diagram_spec": None,
    }


def arch_11_reading_value_from_calibrated_number_line(rng: random.Random) -> Dict[str, Any]:
    start_int = rng.randint(1, 5)
    target_tenth = rng.choice([0.2, 0.4, 0.6, 0.8])
    target_val = round(start_int + target_tenth, 1)

    seed_val = rng.randint(1, 1000000)
    svg = draw_decimal_number_line_svg(
        min_val=float(start_int),
        max_val=float(start_int + 1),
        step=0.1,
        arrow_pos=target_val,
        arrow_label="P",
        label="Calibrated Number Line",
        seed=seed_val,
    )

    ans_str = _fmt_sa(target_val, 1)

    return {
        "title": "Reading Decimal on a Number Line",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "11_reading_value_from_calibrated_number_line",
        "difficulty": "medium",
        "question_text": (
            "Refer to the calibrated decimal number line below.\n\n"
            "Determine the decimal value indicated by the arrow marked **P**."
        ),
        "correct_answer": ans_str,
        "marking_schema": [
            f"Read value from scale: {ans_str} (1 mark)",
        ],
        "hints": [
            f"Notice that the interval between {start_int} and {start_int + 1} is divided into 10 equal parts.",
            "Each tick represents 0,1 (one tenth).",
            f"Count {int(target_tenth * 10)} tenths past {start_int}: {ans_str}.",
        ],
        "misconception_tags": ["number_line_decimal_tick_counting_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_12_identifying_letter_for_decimal_on_number_line(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(0, 4)
    # 4 distinct points
    pos_map = {
        round(base + 0.2, 1): "A",
        round(base + 0.5, 1): "B",
        round(base + 0.7, 1): "C",
        round(base + 0.9, 1): "D",
    }
    chosen_pos, chosen_letter = rng.choice(list(pos_map.items()))

    seed_val = rng.randint(1, 1000000)
    svg = draw_decimal_number_line_svg(
        min_val=float(base),
        max_val=float(base + 1),
        step=0.1,
        markers=pos_map,
        label="Calibrated Scale",
        seed=seed_val,
    )

    return {
        "title": "Identifying Marked Decimal Position",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "12_identifying_letter_for_decimal_on_number_line",
        "difficulty": "medium",
        "question_text": (
            f"On the number line below, which marked letter represents the decimal fraction **{_fmt_sa(chosen_pos, 1)}**?"
        ),
        "correct_answer": chosen_letter,
        "marking_schema": [
            f"Identify letter corresponding to {_fmt_sa(chosen_pos, 1)}: {chosen_letter} (1 mark)",
        ],
        "hints": [
            f"The scale runs from {base} to {base + 1} with steps of 0,1.",
            f"Count {int((chosen_pos - base) * 10)} tenths from {base}.",
            f"Point {chosen_letter} is located at {_fmt_sa(chosen_pos, 1)}.",
        ],
        "misconception_tags": ["number_line_decimal_tick_counting_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_13_converting_tenth_hundredth_thousandth_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    den = rng.choice([10, 100, 1000])
    if den == 10:
        num = rng.randint(1, 9)
    elif den == 100:
        num = rng.choice([7, 23, 59, 81])
    else:
        num = rng.choice([9, 45, 127, 638])

    val = num / den
    val_str = _fmt_sa(val, 3)

    return {
        "title": "Fraction to Decimal (Tenths, Hundredths, Thousandths)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "13_converting_tenth_hundredth_thousandth_fraction_to_decimal",
        "difficulty": "easy",
        "question_text": (
            f"Write the common fraction $\\frac{{{num}}}{{{den}}}$ as a decimal fraction."
        ),
        "correct_answer": val_str,
        "marking_schema": [
            f"Convert to decimal: {val_str} (1 mark)",
        ],
        "hints": [
            f"A denominator of {den} indicates {len(str(den)) - 1} decimal places.",
            f"Divide {num} by {den}.",
            f"The decimal is {val_str}.",
        ],
        "misconception_tags": ["fraction_denominator_decimal_places_confusion"],
        "diagram_spec": None,
    }


def arch_14_converting_simple_fraction_to_decimal_via_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (1, 2, 5, 10, "0,5"),
        (3, 4, 25, 100, "0,75"),
        (2, 5, 2, 10, "0,4"),
        (4, 5, 2, 10, "0,8"),
        (7, 20, 5, 100, "0,35"),
        (11, 20, 5, 100, "0,55"),
        (9, 25, 4, 100, "0,36"),
        (18, 25, 4, 100, "0,72"),
        (3, 8, 125, 1000, "0,375"),
        (5, 8, 125, 1000, "0,625"),
    ]
    num, den, mult, pow10, ans = rng.choice(pairs)

    return {
        "title": "Converting Common Fraction to Decimal Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "14_converting_simple_fraction_to_decimal_via_powers_of_ten",
        "difficulty": "medium",
        "question_text": (
            f"Convert the common fraction $\\frac{{{num}}}{{{den}}}$ into an equivalent decimal fraction without using a calculator."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Convert denominator to power of 10: ({num}*{mult})/({den}*{mult}) = {num * mult}/{pow10} [1M]",
            f"Write as decimal: {ans} [1A]",
        ],
        "hints": [
            f"Multiply both the numerator and denominator by {mult} to make the denominator {pow10}.",
            f"$\\frac{{{num} \\times {mult}}}{{{den} \\times {mult}}} = \\frac{{{num * mult}}}{{{pow10}}}$.",
            f"Write as decimal: {ans}.",
        ],
        "misconception_tags": ["equivalent_fraction_decimal_conversion_slip"],
        "diagram_spec": None,
    }


def arch_15_converting_improper_fraction_to_decimal(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (7, 2, "3,5"),
        (9, 4, "2,25"),
        (11, 4, "2,75"),
        (14, 5, "2,8"),
        (23, 10, "2,3"),
        (31, 20, "1,55"),
    ]
    num, den, ans = rng.choice(pairs)

    return {
        "title": "Converting Improper Fraction to Decimal",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "15_converting_improper_fraction_to_decimal",
        "difficulty": "medium",
        "question_text": (
            f"Convert the improper fraction $\\frac{{{num}}}{{{den}}}$ into decimal notation."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Convert improper fraction: {ans} (1 mark)",
        ],
        "hints": [
            f"Divide the numerator {num} by the denominator {den}.",
            f"{num} / {den} = {num // den} remainder {num % den}.",
            f"$\\frac{{{num}}}{{{den}}} = {ans}$.",
        ],
        "misconception_tags": ["improper_fraction_decimal_division_error"],
        "diagram_spec": None,
    }


def arch_16_converting_mixed_number_to_decimal(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(2, 9)
    frac_pairs = [
        (1, 2, "5", "5"),
        (1, 4, "25", "25"),
        (3, 4, "75", "75"),
        (3, 5, "6", "6"),
        (7, 20, "35", "35"),
        (1, 8, "125", "125"),
    ]
    num, den, frac_dec, _ = rng.choice(frac_pairs)
    ans = f"{whole},{frac_dec}"

    return {
        "title": "Converting Mixed Number to Decimal",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "16_converting_mixed_number_to_decimal",
        "difficulty": "easy",
        "question_text": (
            f"Convert the mixed number **${whole}\\frac{{{num}}}{{{den}}}$** into a decimal fraction."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Write whole number and decimal part: {ans} (1 mark)",
        ],
        "hints": [
            f"The whole number part is {whole}.",
            f"Convert the fractional part: $\\frac{{{num}}}{{{den}}} = 0,{frac_dec}$.",
            f"Combine: ${whole} + 0,{frac_dec} = {ans}$.",
        ],
        "misconception_tags": ["mixed_number_decimal_combination_error"],
        "diagram_spec": None,
    }


def arch_17_converting_terminating_decimal_to_simplified_fraction(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("0,25", 1, 4),
        ("0,75", 3, 4),
        ("0,4", 2, 5),
        ("0,6", 3, 5),
        ("0,35", 7, 20),
        ("0,65", 13, 20),
        ("0,125", 1, 8),
        ("0,375", 3, 8),
        ("0,625", 5, 8),
        ("0,16", 4, 25),
    ]
    dec_str, num, den = rng.choice(samples)

    return {
        "title": "Converting Terminating Decimal to Common Fraction",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "17_converting_terminating_decimal_to_simplified_fraction",
        "difficulty": "medium",
        "question_text": (
            f"Convert **{dec_str}** into a common fraction in its **simplest form**."
        ),
        "correct_answer": f"{num}/{den}",
        "marking_schema": [
            f"Express with power of 10 denominator [1M]",
            f"Simplify to lowest terms: {num}/{den} [1A]",
        ],
        "hints": [
            f"Write the decimal as a fraction with denominator 10, 100, or 1000.",
            "Divide both numerator and denominator by their highest common factor.",
            f"Simplest form: $\\frac{{{num}}}{{{den}}}$.",
        ],
        "misconception_tags": ["unsimplified_fraction_response_error"],
        "diagram_spec": None,
    }


def arch_18_converting_mixed_decimal_to_simplified_mixed_number(rng: random.Random) -> Dict[str, Any]:
    whole = rng.randint(2, 8)
    samples = [
        ("25", 1, 4),
        ("5", 1, 2),
        ("75", 3, 4),
        ("2", 1, 5),
        ("8", 4, 5),
        ("125", 1, 8),
    ]
    dec_part, num, den = rng.choice(samples)
    dec_str = f"{whole},{dec_part}"
    ans = f"{whole} {num}/{den}"

    return {
        "title": "Converting Mixed Decimal to Mixed Number",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "18_converting_mixed_decimal_to_simplified_mixed_number",
        "difficulty": "medium",
        "question_text": (
            f"Convert the decimal fraction **{dec_str}** into a simplified mixed number."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Keep whole number {whole} and simplify fractional part to {num}/{den}: {ans} (2 marks)",
        ],
        "hints": [
            f"The whole number remains {whole}.",
            f"Convert $0,{dec_part}$ to a simplified common fraction: $\\frac{{{num}}}{{{den}}}$.",
            f"Answer: ${whole}\\frac{{{num}}}{{{den}}}$.",
        ],
        "misconception_tags": ["mixed_number_simplification_slip"],
        "diagram_spec": None,
    }


def arch_19_converting_decimal_to_percentage(rng: random.Random) -> Dict[str, Any]:
    val = rng.choice([0.15, 0.45, 0.72, 0.08, 0.05, 1.25, 0.875])
    val_str = _fmt_sa(val, 3)
    pct = val * 100
    pct_str = _fmt_sa(pct, 1)

    return {
        "title": "Converting Decimal to Percentage",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "19_converting_decimal_to_percentage",
        "difficulty": "easy",
        "question_text": (
            f"Convert the decimal fraction **{val_str}** into a percentage."
        ),
        "correct_answer": f"{pct_str}%",
        "marking_schema": [
            f"Multiply by 100%: {val_str} * 100% = {pct_str}% (1 mark)",
        ],
        "hints": [
            "To convert a decimal to a percentage, multiply by 100% (shift the decimal comma two places to the right).",
            f"${val_str} \\times 100\\% = {pct_str}\\%$.",
            f"Answer: {pct_str}%.",
        ],
        "misconception_tags": ["percentage_decimal_shift_reversal"],
        "diagram_spec": None,
    }


def arch_20_converting_percentage_to_decimal(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([12, 35, 68, 7, 125, 4.5, 37.5])
    pct_str = _fmt_sa(pct, 1)
    dec_val = pct / 100.0
    dec_str = _fmt_sa(dec_val, 3)

    return {
        "title": "Converting Percentage to Decimal",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "20_converting_percentage_to_decimal",
        "difficulty": "easy",
        "question_text": (
            f"Convert **{pct_str}%** into a decimal fraction."
        ),
        "correct_answer": dec_str,
        "marking_schema": [
            f"Divide by 100: {pct_str}% = {dec_str} (1 mark)",
        ],
        "hints": [
            "Percent means 'per hundred'. Divide the percentage by 100.",
            "Shift the decimal comma two places to the left.",
            f"${pct_str}\\% \\div 100 = {dec_str}$.",
        ],
        "misconception_tags": ["percentage_to_decimal_division_error"],
        "diagram_spec": None,
    }


def arch_21_converting_common_fraction_to_percentage_via_decimal(rng: random.Random) -> Dict[str, Any]:
    samples = [
        (3, 5, "0,6", "60%"),
        (1, 8, "0,125", "12,5%"),
        (3, 8, "0,375", "37,5%"),
        (7, 20, "0,35", "35%"),
        (9, 25, "0,36", "36%"),
        (13, 50, "0,26", "26%"),
    ]
    num, den, dec_repr, pct_repr = rng.choice(samples)

    return {
        "title": "Converting Fraction to Percentage",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "21_converting_common_fraction_to_percentage_via_decimal",
        "difficulty": "medium",
        "question_text": (
            f"Convert the common fraction $\\frac{{{num}}}{{{den}}}$ into a percentage."
        ),
        "correct_answer": pct_repr,
        "marking_schema": [
            f"Convert to decimal {dec_repr} or multiply by 100% [1M]",
            f"Percentage: {pct_repr} [1A]",
        ],
        "hints": [
            f"First convert $\\frac{{{num}}}{{{den}}}$ to a decimal fraction: {dec_repr}.",
            f"Then multiply by 100%: ${dec_repr} \\times 100\\% = {pct_repr}$.",
            f"Answer: {pct_repr}.",
        ],
        "misconception_tags": ["fraction_percentage_intermediate_slip"],
        "diagram_spec": None,
    }


def arch_22_identifying_terminating_vs_recurring_decimal(rng: random.Random) -> Dict[str, Any]:
    pool = [
        (1, 6, "recurring", "the denominator has prime factor 3"),
        (3, 8, "terminating", "the denominator only contains prime factor 2"),
        (5, 12, "recurring", "the denominator contains factor 3"),
        (7, 20, "terminating", "the denominator only contains factors 2 and 5"),
        (2, 9, "recurring", "the denominator is a power of 3"),
        (11, 25, "terminating", "the denominator only contains factor 5"),
    ]
    num, den, classification, reason = rng.choice(pool)

    return {
        "title": "Terminating vs Recurring Decimals",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "22_identifying_terminating_vs_recurring_decimal",
        "difficulty": "medium",
        "question_text": (
            f"State whether the common fraction $\\frac{{{num}}}{{{den}}}$ produces a **terminating** decimal or a **recurring** decimal."
        ),
        "correct_answer": classification,
        "marking_schema": [
            f"State {classification} with prime factor justification: 1 mark",
        ],
        "hints": [
            "A simplified common fraction terminates in decimal form if and only if its denominator's prime factors are only 2 and/or 5.",
            f"Analyze the prime factors of denominator {den}.",
            f"$\\frac{{{num}}}{{{den}}}$ is a {classification} decimal.",
        ],
        "misconception_tags": ["terminating_recurring_classification_error"],
        "diagram_spec": None,
    }


def arch_23_recognizing_basic_recurring_decimal_notation(rng: random.Random) -> Dict[str, Any]:
    samples = [
        (1, 3, "0,\\dot{3}", "0.333..."),
        (2, 3, "0,\\dot{6}", "0.666..."),
        (1, 9, "0,\\dot{1}", "0.111..."),
        (5, 9, "0,\\dot{5}", "0.555..."),
        (1, 6, "0,1\\dot{6}", "0.1666..."),
    ]
    num, den, dot_not, approx = rng.choice(samples)

    return {
        "title": "Recurring Decimal Notation",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "23_recognizing_basic_recurring_decimal_notation",
        "difficulty": "medium",
        "question_text": (
            f"Write the common fraction $\\frac{{{num}}}{{{den}}}$ as a recurring decimal using dot or bar notation."
        ),
        "correct_answer": f"${dot_not}$",
        "marking_schema": [
            f"Express using recurring dot/bar notation: ${dot_not}$ (1 mark)",
        ],
        "hints": [
            f"Dividing {num} by {den} gives {approx}.",
            "A recurring dot above the digit shows that the digit repeats indefinitely.",
            f"The notation is ${dot_not}$.",
        ],
        "misconception_tags": ["recurring_notation_syntax_confusion"],
        "diagram_spec": None,
    }


def arch_24_completing_fraction_decimal_percentage_equivalence_table(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("1/4", "0,25", "25%"),
        ("3/5", "0,6", "60%"),
        ("7/10", "0,7", "70%"),
        ("3/8", "0,375", "37,5%"),
        ("4/5", "0,8", "80%"),
    ]
    frac, dec, pct = rng.choice(samples)
    missing = rng.choice(["decimal", "percentage", "fraction"])

    if missing == "decimal":
        q_given = f"Fraction: **{frac}**, Percentage: **{pct}**"
        ans = dec
    elif missing == "percentage":
        q_given = f"Fraction: **{frac}**, Decimal: **{dec}**"
        ans = pct
    else:
        q_given = f"Decimal: **{dec}**, Percentage: **{pct}**"
        ans = frac

    return {
        "title": "Equivalence Table (Fraction, Decimal, Percentage)",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "24_completing_fraction_decimal_percentage_equivalence_table",
        "difficulty": "easy",
        "question_text": (
            f"Complete the missing {missing} representation given the following equivalent values:\n\n"
            f"{q_given}\n\n"
            f"Find the equivalent **{missing}** value."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Determine equivalent {missing}: {ans} (1 mark)",
        ],
        "hints": [
            "Use the relationship between fractions, decimals, and percentages.",
            f"For these values, fraction = {frac}, decimal = {dec}, percentage = {pct}.",
            f"The missing {missing} is {ans}.",
        ],
        "misconception_tags": ["equivalence_conversion_table_slip"],
        "diagram_spec": None,
    }


def arch_25_comparing_fraction_and_decimal_using_inequality(rng: random.Random) -> Dict[str, Any]:
    triplets = [
        (3, 4, 0.72, ">"),
        (1, 2, 0.55, "<"),
        (3, 5, 0.6, "="),
        (5, 8, 0.62, ">"),
        (7, 20, 0.38, "<"),
        (4, 5, 0.80, "="),
    ]
    num, den, dec_comp, ans = rng.choice(triplets)
    dec_comp_str = _fmt_sa(dec_comp, 2)

    return {
        "title": "Comparing Common Fraction and Decimal",
        "topic": "Fractions in decimal notation",
        "grade": 8,
        "term": 1,
        "subskill": "25_comparing_fraction_and_decimal_using_inequality",
        "difficulty": "medium",
        "question_text": (
            f"Insert $<$, $>$, or $=$ between the two quantities to make a true statement:\n\n"
            f"$$\\frac{{{num}}}{{{den}}} \\quad \\boxed{{\\phantom{{M}}}} \\quad {dec_comp_str}$$"
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Convert to common form and compare: '{ans}' (1 mark)",
        ],
        "hints": [
            f"Convert $\\frac{{{num}}}{{{den}}}$ to a decimal fraction.",
            f"$\\frac{{{num}}}{{{den}}} = {_fmt_sa(num / den, 3)}$.",
            f"Comparing {_fmt_sa(num / den, 3)} with {dec_comp_str} gives '{ans}'.",
        ],
        "misconception_tags": ["fraction_decimal_comparison_error"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_place_value_identification_tenths_hundredths_thousandths,
    arch_02_ordering_positive_decimals_ascending,
    arch_03_ordering_positive_decimals_descending,
    arch_04_ordering_signed_decimals_ascending,
    arch_05_comparing_two_decimals_inequality,
    arch_06_finding_decimal_between_two_given_decimals,
    arch_07_rounding_to_nearest_whole_number,
    arch_08_rounding_to_one_decimal_place,
    arch_09_rounding_to_two_decimal_places,
    arch_10_rounding_to_three_decimal_places,
    arch_11_reading_value_from_calibrated_number_line,
    arch_12_identifying_letter_for_decimal_on_number_line,
    arch_13_converting_tenth_hundredth_thousandth_fraction_to_decimal,
    arch_14_converting_simple_fraction_to_decimal_via_powers_of_ten,
    arch_15_converting_improper_fraction_to_decimal,
    arch_16_converting_mixed_number_to_decimal,
    arch_17_converting_terminating_decimal_to_simplified_fraction,
    arch_18_converting_mixed_decimal_to_simplified_mixed_number,
    arch_19_converting_decimal_to_percentage,
    arch_20_converting_percentage_to_decimal,
    arch_21_converting_common_fraction_to_percentage_via_decimal,
    arch_22_identifying_terminating_vs_recurring_decimal,
    arch_23_recognizing_basic_recurring_decimal_notation,
    arch_24_completing_fraction_decimal_percentage_equivalence_table,
    arch_25_comparing_fraction_and_decimal_using_inequality,
]
