"""Percentages and Percentage Applications Subskills (Subskills 44 to 52).

44. num_pct_calculate_percentage_of_amount
45. num_pct_express_one_amount_as_percentage_of_another
46. num_pct_percentage_increase_calculation
47. num_pct_percentage_decrease_discount
48. num_pct_percentage_change_increase_or_decrease
49. num_pct_reverse_percentage_pre_vat_cost
50. num_pct_reverse_percentage_pre_discount_price
51. num_pct_pass_rate_test_score_percentage
52. num_pct_deposit_and_hire_purchase_percentage
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Calculate a percentage of an amount (e.g. discount or fee)."""
    name = r.choice(SA_NAMES)
    pct = r.choice([5, 8, 10, 12, 15, 20, 25, 30])
    base = r.choice([240, 350, 480, 600, 750, 840, 960, 1200, 1500, 2400])
    ans_val = round(base * pct / 100, 2)
    ans_str = _fmt_curr(ans_val)

    prompt = (
        f"{name} receives a monthly municipal service account of {_fmt_curr(base)}. "
        f"The municipality applies an early settlement discount of {pct}%. "
        f"Calculate the discount amount {name} will receive if paid on time."
    )
    sol = (
        f"Step 1: Calculate {pct}% of {_fmt_curr(base)}.\n"
        f"Discount = {pct}/100 × {_fmt_curr(base)}\n"
        f"Step 2: Method setup:\n"
        f"Discount = {pct / 100} × {base} ✓ [1 Mark: Method – percentage of amount]\n"
        f"Step 3: Calculate value:\n"
        f"Discount = {ans_str} ✓ [1 Mark: Accuracy – final discount amount]"
    )
    rubric = [
        f"1 Mark: Method – multiplying amount by {pct}/100",
        f"1 Mark: Accuracy – correct discount {ans_str}"
    ]
    hints = {
        "hint_1": f"Write {pct}% as a fraction or decimal: {pct}/100 or {pct/100}.",
        "hint_2": f"Multiply the base amount {_fmt_curr(base)} by {pct}/100.",
        "hint_3": f"Calculate: {base} × {pct/100} = {ans_val:.2f}, giving {ans_str}."
    }
    return _make_q("num_pct_calculate_percentage_of_amount", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Express one quantity as a percentage of another."""
    name = r.choice(SA_NAMES)
    total = r.choice([40, 50, 60, 80, 120, 150, 200])
    pct_options = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80, 85]
    pct = r.choice(pct_options)
    part = int(round(total * pct / 100))
    # Recalculate true percentage rounded to 1 decimal place
    true_pct = round((part / total) * 100, 1)
    ans_str = f"{_fmt(true_pct)}%"

    prompt = (
        f"{name} completed a Mathematical Literacy test scored out of a total of {total} marks. "
        f"{name} achieved {part} marks. "
        f"Express {name}'s score as a percentage of the total marks."
    )
    sol = (
        f"Step 1: Write the score as a fraction of the total:\n"
        f"Fraction = {part}/{total}\n"
        f"Step 2: Method setup to convert to percentage:\n"
        f"Percentage = ({part} ÷ {total}) × 100% ✓ [1 Mark: Method – fraction multiplied by 100%]\n"
        f"Step 3: Calculate final percentage:\n"
        f"Percentage = {ans_str} ✓ [1 Mark: Accuracy – percentage value]"
    )
    rubric = [
        f"1 Mark: Method – setting up fraction ({part}/{total}) and multiplying by 100%",
        f"1 Mark: Accuracy – correct percentage {ans_str}"
    ]
    hints = {
        "hint_1": "Divide the marks obtained by the total possible marks.",
        "hint_2": f"Multiply ({part} / {total}) by 100.",
        "hint_3": f"({part} / {total}) × 100 = {true_pct}%, so the answer is {ans_str}."
    }
    return _make_q("num_pct_express_one_amount_as_percentage_of_another", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Calculate a percentage increase."""
    name = r.choice(SA_NAMES)
    orig = r.choice([3200, 4500, 5000, 6200, 7500, 8000, 9500])
    pct = r.choice([5, 6, 7, 8, 9, 10, 12])
    incr = orig * pct / 100
    new_val = round(orig + incr, 2)
    ans_str = _fmt_curr(new_val)

    prompt = (
        f"{name}'s monthly apartment rent is currently {_fmt_curr(orig)}. "
        f"The landlord announces an annual rent increase of {pct}%. "
        f"Calculate {name}'s new monthly rent after the increase."
    )
    sol = (
        f"Step 1: Calculate the increase amount:\n"
        f"Increase = {pct}% of {_fmt_curr(orig)} = ({pct}/100) × {orig} = {_fmt_curr(incr)}\n"
        f"Step 2: Method setup to add increase to original rent:\n"
        f"New Rent = {_fmt_curr(orig)} + {_fmt_curr(incr)} ✓ [1 Mark: Method – adding percentage increase]\n"
        f"Step 3: Calculate total new rent:\n"
        f"New Rent = {ans_str} ✓ [1 Mark: Accuracy – final increased amount]"
    )
    rubric = [
        f"1 Mark: Method – calculating {pct}% increase and adding to base",
        f"1 Mark: Accuracy – correct new rent {ans_str}"
    ]
    hints = {
        "hint_1": f"First find {pct}% of {_fmt_curr(orig)}.",
        "hint_2": f"Alternatively, multiply {_fmt_curr(orig)} by (1 + {pct}/100) = {1 + pct/100:.2f}.",
        "hint_3": f"{orig} × {1 + pct/100} = {new_val:.2f}, which is {ans_str}."
    }
    return _make_q("num_pct_percentage_increase_calculation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Calculate a percentage decrease or discount price."""
    name = r.choice(SA_NAMES)
    orig = r.choice([350, 450, 600, 750, 890, 1200, 1500])
    pct = r.choice([10, 15, 20, 25, 30, 40])
    discount = orig * pct / 100
    new_price = round(orig - discount, 2)
    ans_str = _fmt_curr(new_price)

    prompt = (
        f"A department store offers a seasonal sale. {name} selects a winter jacket with an original "
        f"price tag of {_fmt_curr(orig)}. The store is offering a {pct}% discount. "
        f"Calculate the final sale price of the jacket."
    )
    sol = (
        f"Step 1: Calculate the discount amount:\n"
        f"Discount = {pct}% of {_fmt_curr(orig)} = ({pct}/100) × {orig} = {_fmt_curr(discount)}\n"
        f"Step 2: Method setup to subtract discount from original price:\n"
        f"Sale Price = {_fmt_curr(orig)} - {_fmt_curr(discount)} ✓ [1 Mark: Method – subtracting discount]\n"
        f"Step 3: Final sale price:\n"
        f"Sale Price = {ans_str} ✓ [1 Mark: Accuracy – correct discounted price]"
    )
    rubric = [
        f"1 Mark: Method – calculating {pct}% discount and subtracting from original",
        f"1 Mark: Accuracy – correct discounted price {ans_str}"
    ]
    hints = {
        "hint_1": f"Calculate {pct}% of {_fmt_curr(orig)} to find the discount amount.",
        "hint_2": f"Subtract that discount from {_fmt_curr(orig)}, or multiply by (100 - {pct})% = {100 - pct}%.",
        "hint_3": f"{orig} × {(100 - pct)/100} = {new_price:.2f}, giving {ans_str}."
    }
    return _make_q("num_pct_percentage_decrease_discount", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Calculate percentage change (increase or decrease) between two values."""
    name = r.choice(SA_NAMES)
    is_increase = r.choice([True, False])
    old_val = r.choice([120, 150, 200, 250, 300, 400, 500])
    pct_raw = r.choice([10, 15, 20, 25, 30, 40, 50])
    if is_increase:
        new_val = int(round(old_val * (1 + pct_raw / 100)))
        diff = new_val - old_val
        direction = "increase"
    else:
        new_val = int(round(old_val * (1 - pct_raw / 100)))
        diff = old_val - new_val
        direction = "decrease"

    true_pct = round((diff / old_val) * 100, 1)
    ans_str = f"{_fmt(true_pct)}%"

    prompt = (
        f"{name} monitors the price of a grocery basket. Last year, the basket cost {_fmt_curr(old_val)}. "
        f"This year, the basket costs {_fmt_curr(new_val)}. "
        f"Calculate the percentage {direction} in the price of the grocery basket."
    )
    sol = (
        f"Step 1: Calculate the absolute difference:\n"
        f"Difference = |{new_val} - {old_val}| = {_fmt_curr(diff)}\n"
        f"Step 2: Method setup using the percentage change formula:\n"
        f"Percentage {direction.capitalize()} = (Difference ÷ Original Value) × 100%\n"
        f"= ({diff} ÷ {old_val}) × 100% ✓ [1 Mark: Method – difference divided by original]\n"
        f"Step 3: Calculate percentage:\n"
        f"Percentage {direction.capitalize()} = {ans_str} ✓ [1 Mark: Accuracy – final percentage]"
    )
    rubric = [
        f"1 Mark: Method – setting up difference ({diff}) divided by original value ({old_val}) × 100%",
        f"1 Mark: Accuracy – correct percentage {direction} {ans_str}"
    ]
    hints = {
        "hint_1": f"Find the difference between the new price {_fmt_curr(new_val)} and old price {_fmt_curr(old_val)}.",
        "hint_2": f"Divide the difference by the ORIGINAL price ({_fmt_curr(old_val)}), not the new price.",
        "hint_3": f"({diff} / {old_val}) × 100 = {true_pct}%, so the answer is {ans_str}."
    }
    return _make_q("num_pct_percentage_change_increase_or_decrease", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Reverse percentage: Calculate VAT-exclusive price from VAT-inclusive price (15% VAT)."""
    name = r.choice(SA_NAMES)
    pre_vat = r.choice([200, 300, 450, 500, 600, 800, 1200, 1500, 2400])
    vat_inclusive = round(pre_vat * 1.15, 2)
    ans_str = _fmt_curr(pre_vat)

    prompt = (
        f"{name} buys an office desk with a price tag of {_fmt_curr(vat_inclusive)} including 15% VAT. "
        f"Calculate the price of the desk EXCLUDING VAT."
    )
    sol = (
        f"Step 1: Identify that the VAT-inclusive amount represents 115% of the original cost:\n"
        f"VAT-inclusive price = 100% + 15% = 115% = 1,15 × Exclusive price\n"
        f"Step 2: Method setup to reverse the percentage:\n"
        f"VAT-exclusive price = {_fmt_curr(vat_inclusive)} ÷ 1,15 ✓ [1 Mark: Method – dividing by 1,15]\n"
        f"Step 3: Calculate original price:\n"
        f"VAT-exclusive price = {ans_str} ✓ [1 Mark: Accuracy – pre-VAT price]"
    )
    rubric = [
        "1 Mark: Method – dividing VAT-inclusive price by 1,15 (or 115%)",
        f"1 Mark: Accuracy – correct exclusive price {ans_str}"
    ]
    hints = {
        "hint_1": "The inclusive price is 115% of the exclusive price (100% original + 15% VAT).",
        "hint_2": "To find the original price before VAT, divide the inclusive price by 1,15.",
        "hint_3": f"{vat_inclusive:.2f} ÷ 1,15 = {pre_vat:.2f}, which is {ans_str}."
    }
    return _make_q("num_pct_reverse_percentage_pre_vat_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Reverse percentage: Calculate original price before a discount was applied."""
    name = r.choice(SA_NAMES)
    orig_price = r.choice([250, 300, 400, 500, 600, 750, 800, 1000])
    pct_discount = r.choice([10, 20, 25, 50])
    discounted_price = round(orig_price * (1 - pct_discount / 100), 2)
    rem_pct = 100 - pct_discount
    ans_str = _fmt_curr(orig_price)

    prompt = (
        f"{name} purchased a pair of sports shoes on clearance for {_fmt_curr(discounted_price)}. "
        f"The clearance tag indicates that this price reflects a {pct_discount}% discount on the original marked price. "
        f"Calculate the original marked price of the shoes before the discount was applied."
    )
    sol = (
        f"Step 1: Determine the percentage that the discounted price represents:\n"
        f"Percentage remaining = 100% - {pct_discount}% = {rem_pct}% = {rem_pct/100:.2f}\n"
        f"Step 2: Method setup to find original price:\n"
        f"Original Price = {_fmt_curr(discounted_price)} ÷ {rem_pct/100:.2f} ✓ [1 Mark: Method – dividing by {rem_pct}%]\n"
        f"Step 3: Calculate original marked price:\n"
        f"Original Price = {ans_str} ✓ [1 Mark: Accuracy – pre-discount price]"
    )
    rubric = [
        f"1 Mark: Method – dividing discounted price by ({rem_pct}/100)",
        f"1 Mark: Accuracy – correct original marked price {ans_str}"
    ]
    hints = {
        "hint_1": f"If the discount was {pct_discount}%, the customer paid {100 - pct_discount}% of the original price.",
        "hint_2": f"Divide {_fmt_curr(discounted_price)} by {rem_pct / 100}.",
        "hint_3": f"{discounted_price:.2f} ÷ {rem_pct/100} = {orig_price:.2f}, which is {ans_str}."
    }
    return _make_q("num_pct_reverse_percentage_pre_discount_price", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Pass rate / test performance percentage in a classroom or school cohort."""
    total_learners = r.choice([30, 40, 50, 60, 80, 100, 120])
    pct_pass = r.choice([65, 70, 75, 80, 85, 90, 95])
    passed = int(round(total_learners * pct_pass / 100))
    true_pct = round((passed / total_learners) * 100, 1)
    ans_str = f"{_fmt(true_pct)}%"

    prompt = (
        f"In a Grade 10 Mathematical Literacy class with {total_learners} registered learners, "
        f"{passed} learners achieved a passing grade in the Term 1 examination. "
        f"Calculate the examination pass rate percentage for this class."
    )
    sol = (
        f"Step 1: Identify learners who passed vs total enrolled:\n"
        f"Passed = {passed}, Total = {total_learners}\n"
        f"Step 2: Method setup to calculate pass percentage:\n"
        f"Pass Rate = ({passed} ÷ {total_learners}) × 100% ✓ [1 Mark: Method – passed over total × 100%]\n"
        f"Step 3: Calculate final pass rate:\n"
        f"Pass Rate = {ans_str} ✓ [1 Mark: Accuracy – pass rate percentage]"
    )
    rubric = [
        f"1 Mark: Method – setting up ({passed}/{total_learners}) × 100%",
        f"1 Mark: Accuracy – correct pass rate {ans_str}"
    ]
    hints = {
        "hint_1": "Divide the number of learners who passed by the total number of learners in the class.",
        "hint_2": f"Multiply ({passed} / {total_learners}) by 100.",
        "hint_3": f"({passed} / {total_learners}) × 100 = {true_pct}%, which is {ans_str}."
    }
    return _make_q("num_pct_pass_rate_test_score_percentage", prompt, ans_str, sol, rubric, hints, 2, r=r)


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Deposit percentage and hire purchase down payment calculation."""
    name = r.choice(SA_NAMES)
    item = r.choice(["refrigerator", "washing machine", "smart television", "laptop computer", "lounge suite"])
    cash_price = r.choice([4500, 5500, 6800, 7500, 8400, 9600, 12000])
    deposit_pct = r.choice([10, 15, 20])
    deposit_amt = round(cash_price * deposit_pct / 100, 2)
    ans_str = _fmt_curr(deposit_amt)

    prompt = (
        f"{name} wants to purchase a {item} on a hire purchase agreement. "
        f"The cash price of the {item} is {_fmt_curr(cash_price)}. "
        f"The store requires an upfront cash deposit of {deposit_pct}% before delivery. "
        f"Calculate the deposit amount {name} must pay."
    )
    sol = (
        f"Step 1: Identify the deposit percentage and cash price:\n"
        f"Cash Price = {_fmt_curr(cash_price)}, Deposit required = {deposit_pct}%\n"
        f"Step 2: Method setup to calculate deposit:\n"
        f"Deposit = ({deposit_pct}/100) × {_fmt_curr(cash_price)} ✓ [1 Mark: Method – percentage × cash price]\n"
        f"Step 3: Calculate deposit amount:\n"
        f"Deposit = {ans_str} ✓ [1 Mark: Accuracy – deposit amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(cash_price)} by {deposit_pct}/100",
        f"1 Mark: Accuracy – correct deposit amount {ans_str}"
    ]
    hints = {
        "hint_1": f"Write {deposit_pct}% as a decimal ({deposit_pct/100}).",
        "hint_2": f"Multiply the cash price {_fmt_curr(cash_price)} by {deposit_pct/100}.",
        "hint_3": f"{cash_price} × {deposit_pct/100} = {deposit_amt:.2f}, giving {ans_str}."
    }
    return _make_q("num_pct_deposit_and_hire_purchase_percentage", prompt, ans_str, sol, rubric, hints, 2, r=r)
