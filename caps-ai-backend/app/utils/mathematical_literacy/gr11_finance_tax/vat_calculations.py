"""Cluster 5: Value Added Tax (VAT) Calculations (Subskills 37 to 44)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)

VAT_RATE = 0.15  # 15% standard rate in South Africa


def _gen_vat_exclusive_to_vat_amount(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_exclusive_to_vat_amount"
    item = r.choice(["laptop computer", "refrigerator", "set of tyres", "office printer", "lawnmower"])
    price_excl = r.randint(2400, 18000)
    vat_amt = round(price_excl * VAT_RATE, 2)
    correct_ans = _fmt_curr(vat_amt)

    prompt = (
        f"A hardware wholesaler quotes the price of a {item} as **{_fmt_curr(price_excl)} excluding VAT**.\n"
        f"In South Africa, the standard Value Added Tax (VAT) rate is **15%**.\n\n"
        f"Calculate the **VAT amount** that must be added to this purchase."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"VAT is calculated directly on the VAT-exclusive price: "
        f"$$\\text{{VAT Amount}} = \\text{{Price Excluding VAT}} \\times 15\\% = \\text{{Price}} \\times 0,15$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{VAT Amount}} = {_fmt_curr(price_excl)} \\times 0,15$$ "
        f"✓ [1 Mark: Method – multiplying VAT-exclusive price by 0,15]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{VAT Amount}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency VAT amount]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the exclusive price by 15% (0,15).",
        tier_2=f"{_fmt_curr(price_excl)} × 0,15 = {correct_ans}.",
        tier_3=f"VAT = {correct_ans}.",
        r=r,
    )


def _gen_vat_exclusive_to_inclusive(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_exclusive_to_inclusive"
    service = r.choice(["plumbing installation", "solar panel maintenance", "building plan drafting", "catering service"])
    price_excl = r.randint(3500, 24000)
    price_incl = round(price_excl * (1.0 + VAT_RATE), 2)
    correct_ans = _fmt_curr(price_incl)

    prompt = (
        f"A contractor submits a quote of **{_fmt_curr(price_excl)} excluding VAT** for a {service}.\n\n"
        f"Calculate the **total price including 15% VAT** that the customer must pay."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To calculate the VAT-inclusive price, multiply the exclusive amount by 1,15 (or add 15% VAT to the base price): "
        f"$$\\text{{Price Including VAT}} = \\text{{Price Excluding VAT}} \\times 1,15$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Price Including VAT}} = {_fmt_curr(price_excl)} \\times 1,15$$ "
        f"✓ [1 Mark: Method – multiplying exclusive price by 1,15]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Price Including VAT}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate VAT-inclusive currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the exclusive price by 1,15.",
        tier_2=f"{_fmt_curr(price_excl)} × 1,15 = {correct_ans}.",
        tier_3=f"Inclusive price = {correct_ans}.",
        r=r,
    )


def _gen_vat_extract_from_inclusive(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_extract_from_inclusive"
    product = r.choice(["television set", "smartphone", "washing machine", "bicycle", "dining table"])
    price_excl = r.randint(2000, 15000)
    price_incl = round(price_excl * 1.15, 2)
    vat_amt = round(price_incl - price_excl, 2)
    correct_ans = _fmt_curr(vat_amt)

    prompt = (
        f"The retail price of a {product} at a department store is **{_fmt_curr(price_incl)} including 15% VAT**.\n\n"
        f"Calculate the **amount of VAT** included in this price.\n"
        f"$$\\text{{VAT}} = \\frac{{\\text{{Price Including VAT}}}}{{1,15}} \\times 0,15$$ (or $\\text{{Price}} \\times \\frac{{15}}{{115}}$)"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A common error is multiplying the inclusive price by 15%. Because the inclusive price is 115% of the base price, "
        f"the VAT portion is $\\frac{{15}}{{115}}$ of the inclusive price.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{VAT Amount}} = \\frac{{{_fmt_curr(price_incl)}}}{{1,15}} \\times 0,15$$ "
        f"✓ [1 Mark: Method – dividing inclusive price by 1,15 and multiplying by 0,15]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{VAT Amount}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate VAT currency]"
    )

    d1 = _fmt_curr(price_incl * 0.15)  # Common misconception (15% of inclusive)
    d2 = _fmt_curr(price_excl)
    d3 = _fmt_curr(vat_amt * 0.5)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Do NOT multiply by 0,15 directly. Divide by 1,15 first, then multiply by 0,15.",
        tier_2=f"({_fmt_curr(price_incl)} ÷ 1,15) × 0,15 = {correct_ans}.",
        tier_3=f"VAT amount = {correct_ans}.",
        r=r,
    )


def _gen_vat_inclusive_to_exclusive(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_inclusive_to_exclusive"
    item = r.choice(["microwave oven", "power drill", "office desk", "car battery"])
    price_excl = r.randint(1800, 9500)
    price_incl = round(price_excl * 1.15, 2)
    correct_ans = _fmt_curr(price_excl)

    prompt = (
        f"An electronic store advertises a {item} for **{_fmt_curr(price_incl)} (VAT inclusive)**.\n\n"
        f"Calculate the **price of the item excluding VAT**.\n"
        f"$$\\text{{Price Excluding VAT}} = \\frac{{\\text{{Price Including VAT}}}}{{1,15}}$$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To remove 15% VAT, divide the inclusive price by 1,15.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Price Excluding VAT}} = \\frac{{{_fmt_curr(price_incl)}}}{{1,15}}$$ "
        f"✓ [1 Mark: Method – dividing inclusive price by 1,15]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Price Excluding VAT}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate exclusive currency]"
    )

    d1 = _fmt_curr(price_incl * 0.85)  # Misconception of subtracting 15%
    d2 = _fmt_curr(price_incl - (price_incl * 0.15))
    d3 = _fmt_curr(price_incl * 1.15)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the inclusive price by 1,15.",
        tier_2=f"{_fmt_curr(price_incl)} ÷ 1,15 = {correct_ans}.",
        tier_3=f"Exclusive price = {correct_ans}.",
        r=r,
    )


def _gen_vat_zero_rated_basic_food_classification(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_zero_rated_basic_food_classification"
    zero_rated_items = [
        "Brown bread", "Maize meal (mielie meal)", "Dried beans", "Samp",
        "Fresh milk", "Eggs", "Fresh unprocessed fruit and vegetables",
        "Lentils", "Pilchards in tins", "Vegetable cooking oil"
    ]
    standard_rated_items = [
        "White bread", "Potato crisps", "Soft drinks / fizzy sodas",
        "Chocolate bars", "Pre-cooked rotisserie chicken", "Ice cream"
    ]

    target_item = r.choice(zero_rated_items)
    correct_ans = f"Zero-rated (0% VAT) — basic staple foodstuff"

    prompt = (
        f"Under South African Value Added Tax (VAT) legislation, certain basic foodstuffs are designated as **zero-rated (0% VAT)** "
        f"to assist low-income households with food affordability.\n\n"
        f"Which VAT classification applies to: **{target_item}**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"SARS designates 19 basic foodstuffs as zero-rated (0% VAT), including brown bread, maize meal, milk, eggs, and dried beans. "
        f"White bread and confectionery items are standard rated (15% VAT).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"{target_item} is an essential unrefined staple on the official SARS zero-rated list. "
        f"✓ [1 Mark: Method – identifying item on statutory zero-rated basic foodstuffs register]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct tax category designation]"
    )

    custom = [
        f"Zero-rated (0% VAT) — basic staple foodstuff",
        f"Standard rated (15% VAT) — processed luxury item",
        f"VAT exempt — financial and banking service",
        f"Special luxury surcharge rate (25% VAT)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Basic staples like brown bread, milk, and eggs carry 0% VAT in South Africa.",
        tier_2=f"{target_item} is an essential nutritious staple.",
        tier_3=f"Classification: {correct_ans}.",
        r=r,
    )


def _gen_vat_till_slip_multi_item_audit(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_till_slip_multi_item_audit"
    # Grocery list: 2 zero-rated, 2 standard-rated (prices are VAT inclusive where standard)
    zero_1 = ("Brown bread loaf", 17.50)
    zero_2 = ("Fresh full-cream milk 2L", 34.00)
    std_1 = ("Toothpaste 100ml", 28.75)  # incl VAT
    std_2 = ("Washing powder 2kg", 74.75)  # incl VAT

    total_zero = zero_1[1] + zero_2[1]
    total_std_incl = std_1[1] + std_2[1]
    # VAT in std items = total_std_incl / 1.15 * 0.15
    vat_amt = round((total_std_incl / 1.15) * 0.15, 2)
    correct_ans = _fmt_curr(vat_amt)

    prompt = (
        f"A supermarket till slip displays the following purchases:\n"
        f"  • {zero_1[0]}: {_fmt_curr(zero_1[1])} [Zero-rated 0%]\n"
        f"  • {zero_2[0]}: {_fmt_curr(zero_2[1])} [Zero-rated 0%]\n"
        f"  • {std_1[0]}: {_fmt_curr(std_1[1])} [Standard rated 15% incl]\n"
        f"  • {std_2[0]}: {_fmt_curr(std_2[1])} [Standard rated 15% incl]\n\n"
        f"Calculate the **total amount of VAT** charged on this till slip."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Zero-rated food items carry 0% VAT. VAT is calculated ONLY on the standard-rated items ({std_1[0]} and {std_2[0]}): "
        f"$$\\text{{Standard Rated Subtotal}} = {_fmt_curr(std_1[1])} + {_fmt_curr(std_2[1])} = {_fmt_curr(total_std_incl)}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{VAT}} = \\frac{{{_fmt_curr(total_std_incl)}}}{{1,15}} \\times 0,15$$ "
        f"✓ [1 Mark: Method – isolating standard rated items and applying 15/115 VAT formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{VAT Charged}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency VAT amount]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add only the standard-rated items, then calculate VAT using ÷ 1,15 × 0,15.",
        tier_2=f"Standard items total {_fmt_curr(total_std_incl)}. ({_fmt_curr(total_std_incl)} ÷ 1,15) × 0,15 = {correct_ans}.",
        tier_3=f"Total VAT = {correct_ans}.",
        r=r,
    )


def _gen_vat_invoice_discount_then_vat(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_invoice_discount_then_vat"
    name = r.choice(SA_NAMES)
    catalogue_price = r.choice([4000, 6000, 8000, 10000])
    discount_pct = r.choice([10, 15, 20])
    discount_amt = catalogue_price * (discount_pct / 100.0)
    discounted_excl = catalogue_price - discount_amt
    total_incl = round(discounted_excl * 1.15, 2)
    correct_ans = _fmt_curr(total_incl)

    prompt = (
        f"{name} buys office furniture with a catalogue list price of **{_fmt_curr(catalogue_price)} excluding VAT**.\n"
        f"The supplier offers a **{discount_pct}% trade discount** on the exclusive price before VAT is added.\n\n"
        f"Calculate the **final total amount including 15% VAT** {name} must pay."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In commercial invoicing, trade discounts are subtracted from the exclusive price FIRST, and 15% VAT is calculated on the discounted net price.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Discount Amount}} = {_fmt_curr(catalogue_price)} \\times {discount_pct}\\% = {_fmt_curr(discount_amt)}$$\n"
        f"$$\\text{{Discounted Exclusive Price}} = {_fmt_curr(catalogue_price)} - {_fmt_curr(discount_amt)} = {_fmt_curr(discounted_excl)}$$\n"
        f"$$\\text{{Final Price Incl VAT}} = {_fmt_curr(discounted_excl)} \\times 1,15$$ "
        f"✓ [1 Mark: Method – subtracting discount first and multiplying net exclusive by 1,15]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Final Total Payable}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Subtract {discount_pct}% discount from {_fmt_curr(catalogue_price)}, then multiply by 1,15.",
        tier_2=f"Net excl = {_fmt_curr(discounted_excl)}. Total incl = {_fmt_curr(discounted_excl)} × 1,15 = {correct_ans}.",
        tier_3=f"Final payable = {correct_ans}.",
        r=r,
    )


def _gen_vat_vendor_input_vs_output(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_fin_vat_vendor_input_vs_output"
    business = r.choice(["Khaya Bakery", "Lindiwe Auto Spares", "Sipho IT Supplies", "Zanele Boutique"])
    sales_excl = r.randint(80000, 150000)
    purchases_excl = r.randint(40000, 75000)

    output_vat = round(sales_excl * 0.15, 2)
    input_vat = round(purchases_excl * 0.15, 2)
    net_vat_payable = round(output_vat - input_vat, 2)
    correct_ans = _fmt_curr(net_vat_payable)

    prompt = (
        f"{business} is a registered South African VAT vendor.\n"
        f"In a two-month VAT tax period, the business records:\n"
        f"  • Total sales (excluding VAT): {_fmt_curr(sales_excl)} [generates **Output VAT**]\n"
        f"  • Total business purchases (excluding VAT): {_fmt_curr(purchases_excl)} [qualifies for **Input VAT**]\n\n"
        f"Formula: $$\\text{{Net VAT Payable to SARS}} = \\text{{Output VAT (on sales)}} - \\text{{Input VAT (on purchases)}}$$\n\n"
        f"Calculate the **net VAT amount** {business} must pay to SARS."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A VAT vendor collects Output VAT from customers on sales and claims back Input VAT paid to suppliers on purchases. "
        f"The difference is paid over to SARS.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Output VAT}} = {_fmt_curr(sales_excl)} \\times 0,15 = {_fmt_curr(output_vat)}$$\n"
        f"$$\\text{{Input VAT}} = {_fmt_curr(purchases_excl)} \\times 0,15 = {_fmt_curr(input_vat)}$$\n"
        f"$$\\text{{Net VAT Payable}} = {_fmt_curr(output_vat)} - {_fmt_curr(input_vat)}$$ "
        f"✓ [1 Mark: Method – calculating output and input VAT and finding the net difference]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net VAT Payable}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate net payable currency]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Output VAT = Sales × 0,15. Input VAT = Purchases × 0,15. Subtract Input from Output.",
        tier_2=f"Output = {_fmt_curr(output_vat)}. Input = {_fmt_curr(input_vat)}. Net = {_fmt_curr(output_vat)} - {_fmt_curr(input_vat)}.",
        tier_3=f"Net VAT payable = {correct_ans}.",
        r=r,
    )
