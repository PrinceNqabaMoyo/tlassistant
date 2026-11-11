"""Cluster 1: Number Formats, Conventions & Identification (8 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_num_fmt_sa_decimal_comma_space_grouping(r: random.Random) -> Dict[str, Any]:
    int_val = r.choice([14500, 38500, 125000, 480000, 1250000, 3500000])
    cents = r.choice([25, 50, 75, 80, 99])
    val = round(int_val + (cents / 100.0), 2)
    # American format: $1,450.75
    raw_str = f"${int_val:,}.{cents:02d}"
    # South African standard: R 1 450,75
    sa_answer = _fmt_curr(val)

    prompt = (
        f"In South African mathematical literacy and official business reporting, numbers are formatted using specific national conventions:\n\n"
        f"• A **space** is used to separate blocks of three digits (thousands, millions).\n"
        f"• A **decimal comma** is used to separate whole numbers from fractional parts.\n"
        f"• Currency values are prefixed with **R** (Rand).\n\n"
        f"Convert the following international currency amount into **standard South African format**: **{raw_str}**."
    )
    sol = (
        f"**Step 1: Financial & Mathematical Concept**\n"
        f"• South African convention replaces the dollar symbol (\\$) with the Rand symbol (\\text{{R}}).\n"
        f"• Commas used as thousands separators in international texts are replaced by non-breaking spaces.\n"
        f"• The decimal point (.) is replaced by a decimal comma (,).\n\n"
        f"**Step 2: Method Setup & Conversion**\n"
        f"• Replace \\$ with \\text{{R}}.\n"
        f"• Group digits with spaces: ${int_val:,}$ becomes ${f'{int_val:,}'.replace(',', ' ')}$.\n"
        f"• Decimal point replaced by comma: $.{cents:02d}$ becomes $,{cents:02d}$.\n"
        f"✓ **[1 Mark: Method – applying thousands space grouping and decimal comma convention]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{sa_answer}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct South African notation]**"
    )
    custom_opts = [
        sa_answer,
        sa_answer.replace(" ", ""),
        sa_answer.replace(",", "."),
        f"R {int_val},{cents:02d}".replace(" ", "")
    ]
    return _make_q(
        subskill="num_fmt_sa_decimal_comma_space_grouping",
        prompt=prompt,
        answer=sa_answer,
        sol=sol,
        rubric=["1 Mark: Method – thousands space and decimal comma", f"1 Mark: Accuracy – {sa_answer}"],
        hints={
            "tier_1": "Replace the dollar sign with R, use spaces between groups of three digits, and replace the point with a comma.",
            "tier_2": f"{raw_str} has integer part {int_val} and cents {cents}. Format as R [spaces],[cents].",
            "tier_3": f"Correct format: {sa_answer}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_fmt_counting_vs_order_vs_code(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("The number of learners seated on a school bus (45 learners)", "Counting (Quantity)", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Measurement"]),
        ("A runner finishing in 3rd position in the 100 m sprint", "Ordering (Sequence)", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Calculation value"]),
        ("A learner's South African 13-digit National Identity Number (ID)", "Code / Identification", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Quantitative measurement"]),
        ("The postal code for Soweto (1804)", "Code / Identification", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Counting number"]),
        ("The temperature recorded in Sutherland (-2 °C)", "Measurement", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Measurement"]),
        ("Grade 10 classroom door label (Room 14)", "Code / Identification", ["Counting (Quantity)", "Ordering (Sequence)", "Code / Identification", "Ordering (Sequence)"])
    ]
    item, correct_type, opts = r.choice(scenarios)
    prompt = (
        f"In Mathematical Literacy, numbers serve distinct functional roles in society:\n\n"
        f"1. **Counting (Quantity)**: Represents exact countable amounts of discrete items.\n"
        f"2. **Ordering (Sequence)**: Indicates relative rank or position (e.g. 1st, 2nd).\n"
        f"3. **Code / Identification**: Acts as a label or unique key (cannot be added or multiplied meaningfully).\n"
        f"4. **Measurement**: Continuous quantitative values obtained with an instrument.\n\n"
        f"Classify the role of the number in this context: **{item}**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Determine whether the number represents an actual countable amount, an ordinal ranking, a measurement, or merely an identifying code.\n\n"
        f"**Step 2: Method Setup & Evaluation**\n"
        f"• For '{item}', the number is used for **{correct_type}**.\n"
        f"✓ **[1 Mark: Method – evaluating number usage criteria]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_type}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number classification]**"
    )
    return _make_q(
        subskill="num_fmt_counting_vs_order_vs_code",
        prompt=prompt,
        answer=correct_type,
        sol=sol,
        rubric=["1 Mark: Method – classification criteria", f"1 Mark: Accuracy – {correct_type}"],
        hints={
            "tier_1": "Ask: Does this number count items, show rank, measure a quantity, or label something?",
            "tier_2": f"Analyze: Can you perform arithmetic on {item} meaningfully?",
            "tier_3": f"Classification: {correct_type}."
        },
        options=opts,
        r=r
    )

def _gen_num_fmt_calculable_vs_non_calculable(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Adding the cost of 2 kg of maize meal (R 35,00) and 1 L of milk (R 18,50)", "Calculable (Meaningful calculation)", "Both numbers represent quantitative money values that sum to a total purchase cost", ["Calculable (Meaningful calculation)", "Non-calculable (Label / Identifier)", "Ordering sequence", "Arbitrary index"]),
        ("Adding two cell phone contact numbers together (082 123 4567 + 071 987 6543)", "Non-calculable (Label / Identifier)", "Phone numbers are unique identification codes; adding them produces a meaningless number", ["Calculable (Meaningful calculation)", "Non-calculable (Label / Identifier)", "Measurement value", "Continuous scale"]),
        ("Multiplying a vehicle registration plate number by 2 (CA 123-456 × 2)", "Non-calculable (Label / Identifier)", "License plates are alphanumeric identifiers; multiplication is mathematically invalid in context", ["Calculable (Meaningful calculation)", "Non-calculable (Label / Identifier)", "Direct proportion", "Statistical mean"]),
        ("Calculating the average mass of 5 bags of potatoes (10 kg, 9,8 kg, 10,2 kg...)", "Calculable (Meaningful calculation)", "Mass is a measurable physical quantity where statistical operations are authentic and meaningful", ["Calculable (Meaningful calculation)", "Non-calculable (Label / Identifier)", "Ordinal ranking", "Identification code"]),
        ("Subtracting two postal codes (2001 - 1804)", "Non-calculable (Label / Identifier)", "Postal codes designate geographic delivery areas, not quantitative scalar distances", ["Calculable (Meaningful calculation)", "Non-calculable (Label / Identifier)", "Calculable difference", "Ratio quantity"])
    ]
    item, verdict, explanation, opts = r.choice(scenarios)
    prompt = (
        f"A fundamental rule in Mathematical Literacy states:\n"
        f"> **We can only perform mathematical calculations with numbers that represent an actual quantity or value, never with numbers used for naming, ordering, or identification.**\n\n"
        f"Evaluate the following operation: **{item}**.\n\n"
        f"Is this operation **Calculable (Meaningful)** or **Non-calculable (Label / Identifier)**?"
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Numbers representing values, measurements, or amounts can be calculated.\n"
        f"• Numbers representing telephone numbers, codes, addresses, or identifiers cannot be calculated meaningfully.\n\n"
        f"**Step 2: Method Setup & Justification**\n"
        f"• Operation: {item}.\n"
        f"• Evaluation: {explanation}.\n"
        f"• Verdict: **{verdict}**.\n"
        f"✓ **[1 Mark: Method – applying calculable vs identification rule]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{verdict}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct determination]**"
    )
    return _make_q(
        subskill="num_fmt_calculable_vs_non_calculable",
        prompt=prompt,
        answer=verdict,
        sol=sol,
        rubric=["1 Mark: Method – calculability criteria", f"1 Mark: Accuracy – {verdict}"],
        hints={
            "tier_1": "Ask: Does performing arithmetic on these numbers produce a useful, real-world value?",
            "tier_2": f"{explanation}.",
            "tier_3": f"Classification: {verdict}."
        },
        options=opts,
        r=r
    )

def _gen_num_fmt_negative_numbers_context(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    min_temp = r.choice([-6, -5, -4, -3, -2])
    max_temp = r.choice([14, 16, 18, 20, 22])
    temp_diff = max_temp - min_temp
    ans_str = f"{temp_diff} °C"

    prompt = (
        f"During a cold winter front in Sutherland (Northern Cape), the minimum overnight temperature was **{min_temp} °C**.\n\n"
        f"By mid-afternoon, the maximum temperature reached **{max_temp} °C**.\n\n"
        f"Calculate the **temperature range (difference)** between the minimum and maximum temperatures."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The temperature difference is calculated as the maximum temperature minus the minimum temperature:\n"
        f"  $$\\text{{Difference}} = \\text{{Maximum}} - \\text{{Minimum}}$$\n"
        f"• Subtracting a negative number is equivalent to adding its positive opposite: $a - (-b) = a + b$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Difference}} = {max_temp} - ({min_temp}) = {max_temp} + {abs(min_temp)} = {temp_diff}\\text{{ °C}}$.\n"
        f"✓ **[1 Mark: Method – subtracting negative minimum temperature from maximum]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct temperature difference with units]**"
    )
    return _make_q(
        subskill="num_fmt_negative_numbers_context",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – max - min with negative number", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract the minimum ({min_temp} °C) from the maximum ({max_temp} °C): {max_temp} - ({min_temp}).",
            "tier_2": f"Subtracting a negative is adding: {max_temp} + {abs(min_temp)} = {temp_diff}.",
            "tier_3": f"Temperature range = {ans_str}."
        },
        r=r
    )

def _gen_num_fmt_scientific_large_numbers_words(r: random.Random) -> Dict[str, Any]:
    millions = r.choice([2.5, 3.8, 4.2, 5.6, 12.4, 28.5])
    actual_val = int(millions * 1_000_000)
    ans_str = f"{actual_val:,}".replace(",", " ")

    prompt = (
        f"A South African national census report states that a metropolitan municipality has an estimated population of **{_fmt(millions, 1)} million people**.\n\n"
        f"Write this population figure as a **full standard whole number** using South African digit grouping spaces."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• One million is $1\\ 000\\ 000$ ($10^6$).\n"
        f"• To convert from millions to a whole integer, multiply by $1\\ 000\\ 000$:\n"
        f"  $$\\text{{Total}} = {_fmt(millions, 1)} \\times 1\\ 000\\ 000 = {ans_str}$$\n\n"
        f"**Step 2: Method Setup & Conversion**\n"
        f"• ${millions} \\times 1\\ 000\\ 000 = {actual_val}$.\n"
        f"• Group into blocks of three digits from right to left using spaces: **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000 000 and grouping digits with spaces]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number formatted with spaces]**"
    )
    custom_opts = [
        ans_str,
        str(actual_val),
        f"{actual_val // 10:,}".replace(",", " "),
        f"{actual_val * 10:,}".replace(",", " ")
    ]
    return _make_q(
        subskill="num_fmt_scientific_large_numbers_words",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – multiply by 1 000 000 with spaces", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply {_fmt(millions, 1)} by 1 000 000.",
            "tier_2": f"{millions} × 1 000 000 = {actual_val}. Separate thousands with spaces.",
            "tier_3": f"Formatted number = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_fmt_fraction_decimal_percentage_equivalence(r: random.Random) -> Dict[str, Any]:
    fractions = [
        (1, 4, "0,25", "25%"),
        (3, 4, "0,75", "75%"),
        (1, 2, "0,5", "50%"),
        (1, 5, "0,2", "20%"),
        (2, 5, "0,4", "40%"),
        (3, 5, "0,6", "60%"),
        (4, 5, "0,8", "80%"),
        (3, 8, "0,375", "37,5%"),
        (5, 8, "0,625", "62,5%"),
        (7, 10, "0,7", "70%")
    ]
    num, den, dec_str, pct_str = r.choice(fractions)
    ans_str = pct_str

    prompt = (
        f"In recipe preparation and financial discounts, portions are expressed as fractions, decimals, or percentages.\n\n"
        f"Convert the common fraction **\\frac{{{num}}}{{{den}}}** to its equivalent **percentage**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To convert any fraction $\\frac{{a}}{{b}}$ to a percentage, multiply by $100\\%$:\n"
        f"  $$\\text{{Percentage}} = \\left( \\frac{{a}}{{b}} \\right) \\times 100\\%$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{{num}}}{{{den}}} = {num / den:.4f}$.\n"
        f"• ${num / den:.4f} \\times 100\\% = {ans_str}$.\n"
        f"✓ **[1 Mark: Method – dividing numerator by denominator and multiplying by 100]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct percentage value]**"
    )
    return _make_q(
        subskill="num_fmt_fraction_decimal_percentage_equivalence",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (numerator ÷ denominator) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {num} by {den}, then multiply the decimal result by 100.",
            "tier_2": f"{num} ÷ {den} = {dec_str.replace(',', '.')}. Multiply by 100.",
            "tier_3": f"Equivalent percentage = {ans_str}."
        },
        r=r
    )

def _gen_num_fmt_significant_figures_estimation(r: random.Random) -> Dict[str, Any]:
    raw_num = r.choice([48765210, 72480150, 15894200, 36240800, 94120500])
    # Round to 2 significant figures
    s = str(raw_num)
    first_two = int(s[:2])
    third = int(s[2])
    if third >= 5:
        first_two += 1
    rounded_val = first_two * (10 ** (len(s) - 2))
    ans_str = f"R {rounded_val:,}".replace(",", " ")

    prompt = (
        f"A provincial department of education reports an annual regional infrastructure expenditure of **{_fmt_curr(raw_num)}**.\n\n"
        f"For quick executive review and mental budgeting, round this amount to **2 significant figures**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Significant figures count meaningful digits starting from the first non-zero digit on the left.\n"
        f"• To round to 2 significant figures, look at the 3rd digit:\n"
        f"  - If the 3rd digit is 5 or more, round the second digit up.\n"
        f"  - If less than 5, keep the second digit and replace remaining digits with zeroes.\n\n"
        f"**Step 2: Method Setup & Rounding**\n"
        f"• In {raw_num}, the first two digits are {s[:2]} and the third digit is {third}.\n"
        f"• Since {third} {'is $\\ge 5$, round up' if third >= 5 else 'is $< 5$, round down'}: {first_two} followed by {len(s)-2} zeroes.\n"
        f"• Value = **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – identifying first two significant digits and inspecting the 3rd digit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct figure rounded to 2 significant figures]**"
    )
    custom_opts = [
        ans_str,
        f"R {raw_num:,}".replace(",", " "),
        f"R {first_two * 10 ** (len(s) - 3):,}".replace(",", " "),
        f"R {(first_two + 5) * 10 ** (len(s) - 2):,}".replace(",", " ")
    ]
    return _make_q(
        subskill="num_fmt_significant_figures_estimation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 2 significant figures rounding rule", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Look at the first two digits ({s[:2]}) and the third digit ({third}).",
            "tier_2": f"Since the third digit is {third}, round {'up' if third >= 5 else 'down'}.",
            "tier_3": f"Rounded figure: {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_fmt_calculator_display_translation(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        (14.5, "14.5", "R 14,50", "The calculator omits trailing zeroes after the decimal point"),
        (0.8, "0.8", "R 0,80", "The calculator display 0.8 must be written as 80 cents (R 0,80) with a decimal comma"),
        (1250.6, "1250.6", "R 1 250,60", "Thousands requires space grouping and cents requires two decimal places"),
        (45.05, "45.05", "R 45,05", "A calculator displays 45.05; in South African notation, replace the dot with a comma"),
        (350.0, "350", "R 350,00", "A whole number on a calculator display requires ,00 to represent exact Rands and cents")
    ]
    val, calc_display, sa_formatted, note = r.choice(scenarios)
    prompt = (
        f"When performing financial calculations on a handheld electronic calculator, the screen displays **{calc_display}**.\n\n"
        f"In South African Mathematical Literacy, money answers must always be written in standard Rand and cents notation (strictly two decimal digits with a decimal comma).\n\n"
        f"Write down the **correct final South African currency value** representing this calculator display."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Handheld calculators truncate trailing zeroes (e.g. `14.5` means $14$ Rands and $50$ cents).\n"
        f"• South African currency notation requires:\n"
        f"  1. A capital **R** prefix.\n"
        f"  2. A **decimal comma** separating Rands from cents.\n"
        f"  3. Exactly **two decimal digits** for cents (e.g. `,50` not `,5`).\n"
        f"  4. Space thousands grouping if the value is $\\ge 1\\ 000$.\n\n"
        f"**Step 2: Method Setup & Conversion**\n"
        f"• Raw display `{calc_display}` $\\to$ {note} $\\to$ **{sa_formatted}**.\n"
        f"✓ **[1 Mark: Method – applying currency prefix, decimal comma, and 2 decimal places for cents]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{sa_formatted}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct South African currency notation]**"
    )
    custom_opts = [
        sa_formatted,
        f"R {calc_display}",
        f"{sa_formatted.replace('R ', '')}",
        f"R {calc_display.replace('.', ',')}"
    ]
    return _make_q(
        subskill="num_fmt_calculator_display_translation",
        prompt=prompt,
        answer=sa_formatted,
        sol=sol,
        rubric=["1 Mark: Method – calculator display to currency format", f"1 Mark: Accuracy – {sa_formatted}"],
        hints={
            "tier_1": "Add the 'R' prefix, change the decimal point to a comma, and ensure there are exactly two digits for cents.",
            "tier_2": f"{calc_display} means {val} Rands. Two decimal digits for cents gives {sa_formatted}.",
            "tier_3": f"Correct format: {sa_formatted}."
        },
        options=custom_opts,
        r=r
    )
