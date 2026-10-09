"""
Grade 7 Mathematics - Decimal Fractions, Rates & Commercial Calculations Generator
100% CAPS-aligned deterministic question generator.
Calibrated directly against official Grade 7 examination papers (e.g. End of Year Exam & Controlled Tests).
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.

Authentic Exam Archetypes Covered:
1. Column Addition & Subtraction of Decimals with SA Comma Separator (e.g. 124,345 + 42,122 + 3,031) [2 Marks]
2. Division and Multiplication by Whole Numbers & Powers of 10 (e.g. 0,018 ÷ 3 = 0,006; 0,0098 × 10 = 0,098) [2 Marks]
3. Unitary Rate & Practical Pricing with Rounding (e.g. 500g butter @ R15,46 -> cost of 1kg -> round to nearest Rand) [4 Marks]
4. Commercial Discounts & Percentage Markups (e.g. R230 video game @ 20% discount -> new selling price R184) [3 Marks]
5. Decimal Place Value, Fraction Conversion & Rounding (e.g. rounding 45 673,83 to nearest unit/tenth) [2 Marks]
"""

from __future__ import annotations
import random
import math
from typing import Any, Dict, List, Optional

def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)

def _format_sa_decimal(val: float, decimals: int = 2) -> str:
    """Formats a float using the South African comma decimal separator for KaTeX."""
    formatted = f"{val:.{decimals}f}".rstrip('0').rstrip('.') if decimals > 0 else f"{int(round(val))}"
    if '.' in formatted:
        integer_part, frac_part = formatted.split('.')
        return f"{integer_part}{{,}}{frac_part}"
    return formatted

def _format_currency(val: float, decimals: int = 2) -> str:
    """Formats monetary amounts in Rands with comma decimal separator."""
    formatted = f"{val:.{decimals}f}"
    int_part, dec_part = formatted.split('.')
    return f"\\text{{R}}{int_part}{{,}}{dec_part}"


# ============================================================================
# ARCHETYPE 1: MULTI-TERM DECIMAL ADDITION & SUBTRACTION
# ============================================================================
def _generate_addition_subtraction(rng: random.Random, mode: str = "compound") -> Dict[str, Any]:
    is_sub = rng.choice([False, True]) if mode == "compound" else (mode == "elementary_subtraction")
    
    if not is_sub:
        # e.g. Exam Q2.1.5: 124,345 + 42,122 + 3,031
        a_int = rng.randint(80, 250)
        a_dec = rng.randint(100, 999)
        b_int = rng.randint(20, 90)
        b_dec = rng.randint(100, 999)
        c_int = rng.randint(2, 15)
        c_dec = rng.randint(10, 99) * 10 + rng.randint(1, 9)
        
        val_a = a_int + a_dec / 1000.0
        val_b = b_int + b_dec / 1000.0
        val_c = c_int + c_dec / 1000.0
        total = val_a + val_b + val_c
        
        sa_a = f"{a_int}{{,}}{a_dec:03d}"
        sa_b = f"{b_int}{{,}}{b_dec:03d}"
        sa_c = f"{c_int}{{,}}{c_dec:03d}"
        sa_tot = f"{int(total)}{{,}}{int(round((total - int(total)) * 1000)):03d}"
        
        prompt = (
            f"Calculate the following sum without using a calculator. Show all vertical column working:\n\n"
            f"$${sa_a} + {sa_b} + {sa_c}$$"
        )
        
        marking_points = [
            f"Correct column alignment of the decimal comma: {sa_a}, {sa_b}, and {sa_c}",
            f"Accurate addition with carries resulting in ${sa_tot}$"
        ]
        
        hints = {
            "tier_1": "Line up the decimal commas in a vertical column before adding each place value column.",
            "tier_2": "Add column by column starting from the thousandths place on the far right, carrying over to the tenths, units, and tens as needed.",
            "tier_3": f"${sa_a} + {sa_b} + {sa_c} = {sa_tot}$"
        }
        
        return {
            "title": "Addition of Decimal Fractions",
            "prompt": prompt,
            "correct_answer": sa_tot,
            "sample_answer": f"${sa_a} + {sa_b} + {sa_c} = {sa_tot}$",
            "ideal_answer": f"${sa_tot}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": marking_points,
            "hints": hints,
            "misconception_tags": ["decimal_alignment_error", "thousandths_carry_over_error"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Alignment of decimal comma and place values", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Final accurate sum: {sa_tot}", "marks": 1, "editable": True}
                ]
            }
        }
    else:
        # Decimal Subtraction
        a_int = rng.randint(80, 199)
        a_dec = rng.randint(400, 950)
        b_int = rng.randint(15, 65)
        b_dec = rng.randint(100, a_dec - 50)
        
        val_a = a_int + a_dec / 1000.0
        val_b = b_int + b_dec / 1000.0
        diff = val_a - val_b
        
        sa_a = f"{a_int}{{,}}{a_dec:03d}"
        sa_b = f"{b_int}{{,}}{b_dec:03d}"
        sa_diff = f"{int(diff)}{{,}}{int(round((diff - int(diff)) * 1000)):03d}"
        
        prompt = (
            f"Calculate the difference without using a calculator. Show all vertical column working:\n\n"
            f"$${sa_a} - {sa_b}$$"
        )
        
        hints = {
            "tier_1": "Align the numbers so the decimal commas are directly on top of each other.",
            "tier_2": "Subtract column by column starting from the right. Borrow from the next column to the left when the top digit is smaller.",
            "tier_3": f"${sa_a} - {sa_b} = {sa_diff}$"
        }
        
        return {
            "title": "Subtraction of Decimal Fractions",
            "prompt": prompt,
            "correct_answer": sa_diff,
            "sample_answer": f"${sa_a} - {sa_b} = {sa_diff}$",
            "ideal_answer": f"${sa_diff}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": [
                f"Correct column alignment of {sa_a} and {sa_b}",
                f"Accurate subtraction resulting in ${sa_diff}$"
            ],
            "hints": hints,
            "misconception_tags": ["subtraction_borrowing_inversion", "decimal_alignment_error"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Correct vertical column setup and borrowing", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Final accurate difference: {sa_diff}", "marks": 1, "editable": True}
                ]
            }
        }


# ============================================================================
# ARCHETYPE 2: MULTIPLICATION & DIVISION (POWERS OF 10 AND WHOLE NUMBERS)
# ============================================================================
def _generate_powers_of_ten_division(rng: random.Random) -> Dict[str, Any]:
    is_mult = rng.choice([True, False])
    
    if is_mult:
        # e.g. Exam: 0,0098 × 10 = 0,098 or 3,456 × 100 = 345,6
        power = rng.choice([10, 100, 1000])
        shift = int(math.log10(power))
        digits = rng.randint(12, 98)
        # e.g. digits = 45 -> 0,0045 or 0,045
        zeros_prefix = rng.choice([2, 3])
        val = digits / (10 ** (zeros_prefix + len(str(digits))))
        ans = val * power
        
        sa_val = _format_sa_decimal(val, decimals=zeros_prefix + len(str(digits)))
        sa_ans = _format_sa_decimal(ans, decimals=zeros_prefix + len(str(digits)) - shift)
        
        prompt = (
            f"Calculate the following product without using a calculator:\n\n"
            f"$${sa_val} \\times {power}$$"
        )
        
        hints = {
            "tier_1": f"Multiplying by {power} shifts the decimal comma to the right.",
            "tier_2": f"Count the zeros in {power} ({shift} zeros). Shift the decimal comma {shift} places to the right.",
            "tier_3": f"${sa_val} \\times {power} = {sa_ans}$"
        }
        
        return {
            "title": f"Multiplication of Decimals by {power}",
            "prompt": prompt,
            "correct_answer": sa_ans,
            "sample_answer": f"${sa_val} \\times {power} = {sa_ans}$",
            "ideal_answer": f"${sa_ans}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": [
                f"Understanding that multiplying by {power} moves the comma {shift} places right",
                f"Accurate final value: ${sa_ans}$"
            ],
            "hints": hints,
            "misconception_tags": ["power_of_ten_shift_direction_error", "miscounted_zero_shifts"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct shift by {shift} places right", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Correct final answer: {sa_ans}", "marks": 1, "editable": True}
                ]
            }
        }
    else:
        # e.g. Exam Q2.1.6: 0,018 ÷ 3 = 0,006 or 0,042 ÷ 6 = 0,007
        divisor = rng.choice([2, 3, 4, 5, 6, 7, 8, 9])
        quotient_digit = rng.randint(2, 9)
        dividend_num = divisor * quotient_digit
        
        # Format as e.g. 0,018 or 0,045
        zeros = rng.choice([2, 3])
        dividend = dividend_num / (10 ** zeros)
        quotient = dividend / divisor
        
        sa_div = _format_sa_decimal(dividend, decimals=zeros)
        sa_ans = _format_sa_decimal(quotient, decimals=zeros)
        
        prompt = (
            f"Calculate the following division without using a calculator:\n\n"
            f"$${sa_div} \\div {divisor}$$"
        )
        
        hints = {
            "tier_1": "Divide the non-zero digits first, then place the leading zeros and decimal comma.",
            "tier_2": f"Notice that ${dividend_num} \\div {divisor} = {quotient_digit}$. Since {sa_div} is in the thousandths place, the answer must also be in the thousandths place.",
            "tier_3": f"${sa_div} \\div {divisor} = {sa_ans}$"
        }
        
        return {
            "title": "Division of a Decimal Fraction by a Whole Number",
            "prompt": prompt,
            "correct_answer": sa_ans,
            "sample_answer": f"${sa_div} \\div {divisor} = {sa_ans}$",
            "ideal_answer": f"${sa_ans}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": [
                f"Correct place-value division of {sa_div} by {divisor}",
                f"Accurate final quotient: ${sa_ans}$"
            ],
            "hints": hints,
            "misconception_tags": ["omitted_leading_zeros", "decimal_division_place_value_error"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Method: place-value division with correct zero placeholders", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Accuracy: final quotient {sa_ans}", "marks": 1, "editable": True}
                ]
            }
        }


# ============================================================================
# ARCHETYPE 3: UNITARY RATES & ROUNDING (EXAM Q3.1 AUTHENTIC PARALLEL)
# ============================================================================
def _generate_unitary_rates_pricing(rng: random.Random) -> Dict[str, Any]:
    # e.g. Exam Q3.1: 500g butter costs R15,46. Calculate cost of 1kg and round to nearest whole Rand.
    goods = [
        {"item": "salted farm butter", "unit_small": "500g", "unit_large": "1kg", "factor": 2, "base_min": 14.20, "base_max": 28.50},
        {"item": "grade A long-grain white rice", "unit_small": "500g", "unit_large": "1kg", "factor": 2, "base_min": 11.50, "base_max": 19.80},
        {"item": "pure blossom honey", "unit_small": "250g", "unit_large": "1kg", "factor": 4, "base_min": 22.40, "base_max": 34.60},
        {"item": "ground Arabica filter coffee", "unit_small": "250g", "unit_large": "1kg", "factor": 4, "base_min": 28.50, "base_max": 42.00},
        {"item": "sweet navel oranges", "unit_small": "500g", "unit_large": "2kg", "factor": 4, "base_min": 8.50, "base_max": 14.50}
    ]
    g = rng.choice(goods)
    
    cents = rng.randint(10, 95)
    rands = rng.randint(int(g["base_min"]), int(g["base_max"]))
    price_small = rands + cents / 100.0
    factor = g["factor"]
    
    price_large = price_small * factor
    rounded_large = int(round(price_large))
    
    sa_small = _format_currency(price_small)
    sa_large = _format_currency(price_large)
    sa_round = f"\\text{{R}}{rounded_large}"
    
    prompt = (
        f"At a local grocery store, a {g['unit_small']} pack of {g['item']} costs ${sa_small}$.\n\n"
        f"3.1.1 Calculate the cost of {g['unit_large']} of {g['item']}. (2 marks)\n"
        f"3.1.2 Round off your answer to the nearest whole Rand. (2 marks)"
    )
    
    marking_points = [
        f"Multiply unit price by {factor}: ${sa_small} \\times {factor} = {sa_large}$ [2 marks]",
        f"Round off to nearest Rand: ${sa_round}$ [2 marks]"
    ]
    
    hints = {
        "tier_1": f"Determine how many {g['unit_small']} portions make up {g['unit_large']}.",
        "tier_2": f"There are {factor} portions of {g['unit_small']} in {g['unit_large']}. Multiply ${sa_small} \\times {factor}$, then check the cents digit to round up or down.",
        "tier_3": f"Cost of {g['unit_large']} = ${sa_small} \\times {factor} = {sa_large}$. Rounded to nearest Rand = ${sa_round}$."
    }
    
    return {
        "title": "Unitary Rates and Rounding",
        "prompt": prompt,
        "correct_answer": f"{sa_large}; {sa_round}",
        "sample_answer": (
            f"3.1.1 Cost of {g['unit_large']} = ${sa_small} \\times {factor} = {sa_large}$\n"
            f"3.1.2 Rounded to nearest whole Rand = ${sa_round}$"
        ),
        "ideal_answer": f"3.1.1 ${sa_large}$, 3.1.2 ${sa_round}$",
        "marks": 4,
        "question_type": "math",
        "marking_points": marking_points,
        "hints": hints,
        "misconception_tags": ["unitary_rate_multiplier_inversion", "rounding_up_down_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Method: multiply unit price by {factor}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Accuracy: calculated cost {sa_large}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Rounding inspection: look at cents (>= 50 round up, < 50 round down)", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Accuracy: rounded amount {sa_round}", "marks": 1, "editable": True}
            ]
        }
    }


# ============================================================================
# ARCHETYPE 4: COMMERCIAL DISCOUNTS & PERCENTAGE PROFIT/LOSS (EXAM Q3.2 PARALLEL)
# ============================================================================
def _generate_commercial_discounts(rng: random.Random) -> Dict[str, Any]:
    # e.g. Exam Q3.2: A video game normally costs R230 and is sold at a 20% discount. Find the new selling price.
    items = [
        {"name": "school backpack", "price_base": 180, "step": 10},
        {"name": "high school scientific calculator", "price_base": 240, "step": 20},
        {"name": "running shoes", "price_base": 450, "step": 50},
        {"name": "video game", "price_base": 230, "step": 10},
        {"name": "cotton school blazer", "price_base": 360, "step": 20}
    ]
    it = rng.choice(items)
    orig_price = it["price_base"] + rng.choice([0, 1, 2, 3]) * it["step"]
    discount_pct = rng.choice([10, 15, 20, 25, 30])
    
    discount_amount = orig_price * (discount_pct / 100.0)
    final_price = orig_price - discount_amount
    
    sa_orig = _format_currency(orig_price)
    sa_disc = _format_currency(discount_amount)
    sa_final = _format_currency(final_price)
    
    prompt = (
        f"A {it['name']} that normally costs ${sa_orig}$ is on special sale at a ${discount_pct}\\%$ discount.\n\n"
        f"Calculate the new selling price of the {it['name']}. Show all your calculations. (3 marks)"
    )
    
    marking_points = [
        f"Calculate the discount amount: ${sa_orig} \\times \\frac{{{discount_pct}}}{{100}} = {sa_disc}$ [2 marks]",
        f"Subtract discount from original price: ${sa_orig} - {sa_disc} = {sa_final}$ [1 mark]"
    ]
    
    hints = {
        "tier_1": f"First calculate the Rand value of the {discount_pct}% discount.",
        "tier_2": f"Find {discount_pct}% of ${sa_orig}$ by multiplying ${orig_price} \\times \\frac{{{discount_pct}}}{{100}}$. Then subtract this discount from the original price.",
        "tier_3": f"Discount = ${sa_disc}$. New selling price = ${sa_orig} - {sa_disc} = {sa_final}$."
    }
    
    return {
        "title": "Commercial Discounts and Selling Price",
        "prompt": prompt,
        "correct_answer": sa_final,
        "sample_answer": (
            f"\\text{{Discount}} = {sa_orig} \\times \\frac{{{discount_pct}}}{{100}} = {sa_disc}\n"
            f"\\text{{New Price}} = {sa_orig} - {sa_disc} = {sa_final}"
        ),
        "ideal_answer": f"${sa_final}$",
        "marks": 3,
        "question_type": "math",
        "marking_points": marking_points,
        "hints": hints,
        "misconception_tags": ["discount_subtraction_omission", "percentage_calculation_error"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Method: calculate {discount_pct}% of original price", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Accuracy: discount value {sa_disc}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Final answer: subtract discount to get {sa_final}", "marks": 1, "editable": True}
            ]
        }
    }


# ============================================================================
# ARCHETYPE 5: PLACE VALUE, ROUNDING & FRACTION-DECIMAL CONVERSION
# ============================================================================
def _generate_place_value_rounding(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["rounding", "fraction_conversion"])
    
    if choice == "rounding":
        # e.g. Rounding 45 673,83 to nearest unit / tenth / ten
        num_int = rng.randint(12000, 89000)
        tenth = rng.randint(1, 9)
        hundredth = rng.randint(1, 9)
        val = num_int + tenth / 10.0 + hundredth / 100.0
        
        target = rng.choice(["tenth", "whole number"])
        
        if target == "tenth":
            rounded_val = round(val, 1)
            sa_val = f"{num_int:,}".replace(",", " ") + f"{{,}}{tenth}{hundredth}"
            sa_round = f"{int(rounded_val):,}".replace(",", " ") + f"{{,}}{int(round((rounded_val - int(rounded_val))*10))}"
            rule_explanation = f"Look at the hundredths digit ({hundredth}). Since it is {'5 or greater, round up' if hundredth >= 5 else 'less than 5, leave the tenths digit unchanged'}."
        else:
            rounded_val = round(val)
            sa_val = f"{num_int:,}".replace(",", " ") + f"{{,}}{tenth}{hundredth}"
            sa_round = f"{int(rounded_val):,}".replace(",", " ")
            rule_explanation = f"Look at the tenths digit ({tenth}). Since it is {'5 or greater, round up' if tenth >= 5 else 'less than 5, round down'}."
            
        prompt = (
            f"Round off the following decimal number to the nearest **{target}**:\n\n"
            f"$${sa_val}$$"
        )
        
        hints = {
            "tier_1": f"Identify the digit in the {target}s place and inspect the digit immediately to its right.",
            "tier_2": rule_explanation,
            "tier_3": f"${sa_val}$ rounded to the nearest {target} is ${sa_round}$."
        }
        
        return {
            "title": f"Rounding Decimals to the Nearest {target.capitalize()}",
            "prompt": prompt,
            "correct_answer": sa_round,
            "sample_answer": f"${sa_val} \\approx {sa_round}$ (to nearest {target})",
            "ideal_answer": f"${sa_round}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": [
                f"Inspection of deciding digit: {rule_explanation}",
                f"Accurate rounded value: ${sa_round}$"
            ],
            "hints": hints,
            "misconception_tags": ["rounding_up_down_inversion", "incorrect_place_value_inspection"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Method: correct identification of deciding place value", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Accuracy: correct rounded value {sa_round}", "marks": 1, "editable": True}
                ]
            }
        }
    else:
        # Converting common fractions to decimal fractions (e.g. 3/4 = 0,75, 7/20 = 0,35)
        pairs = [
            (3, 4, "0{,}75"),
            (1, 4, "0{,}25"),
            (1, 2, "0{,}5"),
            (3, 5, "0{,}6"),
            (4, 5, "0{,}8"),
            (7, 20, "0{,}35"),
            (9, 25, "0{,}36"),
            (3, 8, "0{,}375"),
            (5, 8, "0{,}625"),
            (7, 10, "0{,}7")
        ]
        num, den, sa_dec = rng.choice(pairs)
        
        prompt = (
            f"Convert the common fraction to a decimal fraction without using a calculator:\n\n"
            f"$$\\frac{{{num}}}{{{den}}}$$"
        )
        
        # Scaling factor to make denominator 10, 100, or 1000
        factor = 100 // den if 100 % den == 0 else 1000 // den
        equiv_num = num * factor
        equiv_den = den * factor
        
        hints = {
            "tier_1": "Convert the denominator to a power of 10 (10, 100, or 1 000) using equivalent fractions.",
            "tier_2": f"Multiply both numerator and denominator by {factor}: $\\frac{{{num} \\times {factor}}}{{{den} \\times {factor}}} = \\frac{{{equiv_num}}}{{{equiv_den}}}$.",
            "tier_3": f"$\\frac{{{equiv_num}}}{{{equiv_den}}} = {sa_dec}$."
        }
        
        return {
            "title": "Converting Common Fractions to Decimal Fractions",
            "prompt": prompt,
            "correct_answer": sa_dec,
            "sample_answer": f"\\frac{{{num}}}{{{den}}} = \\frac{{{equiv_num}}}{{{equiv_den}}} = {sa_dec}",
            "ideal_answer": f"${sa_dec}$",
            "marks": 2,
            "question_type": "math",
            "marking_points": [
                f"Conversion to equivalent fraction with base 10/100/1000: $\\frac{{{equiv_num}}}{{{equiv_den}}}$",
                f"Accurate decimal representation: ${sa_dec}$"
            ],
            "hints": hints,
            "misconception_tags": ["fraction_to_decimal_conversion_error"],
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Method: equivalent fraction with denominator {equiv_den}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Accuracy: correct decimal value {sa_dec}", "marks": 1, "editable": True}
                ]
            }
        }


# ============================================================================
# MASTER GENERATOR INTERFACE
# ============================================================================
def generate(
    subskill: str = "compound",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any
) -> Any:
    rng = _rng(seed)
    subskill_str = str(subskill or "compound").strip().lower()
    
    generators_map = {
        "elementary_addition": lambda: _generate_addition_subtraction(rng, mode="elementary_addition"),
        "elementary_subtraction": lambda: _generate_addition_subtraction(rng, mode="elementary_subtraction"),
        "elementary_powers_of_ten": lambda: _generate_powers_of_ten_division(rng),
        "elementary_rates_discounts": lambda: rng.choice([
            _generate_unitary_rates_pricing(rng),
            _generate_commercial_discounts(rng)
        ]),
        "elementary_place_value_rounding": lambda: _generate_place_value_rounding(rng),
    }
    
    all_gen_funcs = [
        lambda: _generate_addition_subtraction(rng, mode="compound"),
        lambda: _generate_powers_of_ten_division(rng),
        lambda: _generate_unitary_rates_pricing(rng),
        lambda: _generate_commercial_discounts(rng),
        lambda: _generate_place_value_rounding(rng)
    ]
    
    results = []
    for _ in range(count):
        if subskill_str in generators_map:
            q = generators_map[subskill_str]()
        else:
            q = rng.choice(all_gen_funcs)()
            
        # Enrich with common 6-pillar properties
        q.update({
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 15,
            "topic_id": "grade7_mathematics",
            "subtopic_id": "decimal_fractions",
            "curriculum_reference": "Grade 7 Term 2 > Numbers, Operations and Relationships: Decimal Fractions"
        })
        results.append(q)
        
    if count == 1 and len(results) == 1:
        return results[0]
    return results
