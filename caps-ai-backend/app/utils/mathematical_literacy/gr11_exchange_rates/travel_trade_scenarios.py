"""Travel budgets, international e-commerce, and commercial trade scenarios (Subskills 45-52) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Overseas holiday travel budget: Converting total itinerary expenses to ZAR."""
    name = r.choice(SA_NAMES)
    rate_eur = 20.50  # €1 = R 20,50
    hotel_eur = 850.0
    meals_eur = 420.0
    transport_eur = 180.0
    museums_eur = 150.0

    total_eur = hotel_eur + meals_eur + transport_eur + museums_eur
    total_zar = round(total_eur * rate_eur, 2)
    ans_str = _fmt_curr(total_zar)

    prompt = (
        f"{name} is planning a 7-day tour of Rome, Italy and prepares the following budget in Euros (€):\n"
        f"• Hotel accommodation: {_fmt_curr(hotel_eur, '€')}\n"
        f"• Meals and dining: {_fmt_curr(meals_eur, '€')}\n"
        f"• Local trains and buses: {_fmt_curr(transport_eur, '€')}\n"
        f"• Museum and sight-seeing tickets: {_fmt_curr(museums_eur, '€')}\n\n"
        f"If the projected exchange rate is €1,00 = {_fmt_curr(rate_eur)},\n"
        f"calculate the total budget required in South African Rands (ZAR)."
    )
    explanation = (
        f"Step 1: Sum the total budgeted expenses in Euros:\n"
        f"\\text{{Total Euros}} = {hotel_eur:,.0f} + {meals_eur:,.0f} + {transport_eur:,.0f} + {museums_eur:,.0f} = {_fmt_curr(total_eur, '€')}. [1 mark]\n"
        f"Step 2: Multiply total Euros by the exchange rate of 20,50:\n"
        f"\\text{{Total in ZAR}} = {total_eur:,.0f} \\times 20,50 = {total_zar:,.2f} [1 mark]\n"
        f"Step 3: State the final total in Rands:\n"
        f"\\text{{Total budget}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_eur / rate_eur, 2)),
        _fmt_curr(round(total_zar + 3000, 2)),
        _fmt_curr(round(total_zar - 3000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_45",
        prompt,
        ans_str,
        options,
        explanation,
        "Sum all Euro expenses, then multiply the total by 20,50.",
        f"Total Euros = {_fmt_curr(total_eur, '€')}. Total Rands = {total_eur:,.0f} × 20,50.",
        f"Total budget = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Daily travelling allowance calculation in foreign currency from a total Rand budget."""
    name = r.choice(SA_NAMES)
    total_rand_spending = 18000.0
    trip_days = 10
    rate_usd = 18.00  # $1 = R 18,00

    total_usd = total_rand_spending / rate_usd
    daily_usd = round(total_usd / trip_days, 2)
    ans_str = _fmt_curr(daily_usd, "$")

    prompt = (
        f"{name} has allocated a total spending money budget of {_fmt_curr(total_rand_spending)} for a {trip_days}-day trip to New York.\n"
        f"Using an exchange rate of $1,00 = {_fmt_curr(rate_usd)},\n"
        f"calculate {name}'s average daily spending allowance in US Dollars ($).\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Convert the total Rand budget to US Dollars:\n"
        f"\\text{{Total USD}} = 18\\,000 \\div 18,00 = {_fmt_curr(total_usd, '$')}. [1 mark]\n"
        f"Step 2: Divide the total US Dollars by the {trip_days} trip days:\n"
        f"\\text{{Daily Allowance}} = {total_usd:.0f} \\div {trip_days} = {daily_usd:.2f} [1 mark]\n"
        f"Step 3: State the daily allowance in Dollars:\n"
        f"\\text{{Daily allowance}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(daily_usd * 1.5, 2), "$"),
        _fmt_curr(round(daily_usd * 0.5, 2), "$"),
        _fmt_curr(round(total_usd, 2), "$"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_46",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide total Rands by 18 to get Dollars, then divide by 10 days.",
        f"Total USD = 18 000 ÷ 18 = $ 1 000. Daily = $ 1 000 ÷ 10 = {ans_str}.",
        f"Daily allowance = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """International online shopping: Foreign price to ZAR + 15% import VAT + customs tariff."""
    name = r.choice(SA_NAMES)
    rate_usd = 18.00  # $1 = R 18,00
    item_usd = 120.0
    shipping_usd = 30.0
    total_usd = item_usd + shipping_usd

    zar_fob = round(total_usd * rate_usd, 2)
    customs_tariff_pct = 10.0  # 10% duty
    customs_duty = round(zar_fob * (customs_tariff_pct / 100.0), 2)
    import_vat = round((zar_fob + customs_duty) * 0.15, 2)  # 15% VAT on landed value
    total_landed = round(zar_fob + customs_duty + import_vat, 2)
    ans_str = _fmt_curr(total_landed)

    prompt = (
        f"{name} buys an electronic gadget from an international website for {_fmt_curr(item_usd, '$')} "
        f"plus {_fmt_curr(shipping_usd, '$')} international courier shipping.\n"
        f"The exchange rate is $1,00 = {_fmt_curr(rate_usd)}.\n"
        f"Upon arrival in South Africa, customs levies:\n"
        f"• 10% customs import duty on the total converted cost (item + shipping)\n"
        f"• 15% South African import VAT on the total duty-inclusive value\n\n"
        f"Calculate the final total cost in South African Rands (ZAR) that {name} pays."
    )
    explanation = (
        f"Step 1: Convert total US Dollar cost (gadget + shipping) to Rands:\n"
        f"\\text{{USD Total}} = 120 + 30 = \\$ 150\n"
        f"\\text{{ZAR Value}} = 150 \\times 18,00 = {_fmt_curr(zar_fob)}. [1 mark]\n"
        f"Step 2: Calculate 10% customs duty and 15% import VAT:\n"
        f"\\text{{Duty}} = 2\\,700 \\times 0,10 = {_fmt_curr(customs_duty)}\n"
        f"\\text{{Subtotal}} = 2\\,700 + 270 = {_fmt_curr(zar_fob + customs_duty)}\n"
        f"\\text{{VAT}} = 2\\,970 \\times 0,15 = {_fmt_curr(import_vat)}. [1 mark]\n"
        f"Step 3: Sum all components for the landed Rand cost:\n"
        f"\\text{{Total}} = 2\\,970 + 445,50 = {total_landed:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(zar_fob),
        _fmt_curr(round(zar_fob + customs_duty, 2)),
        _fmt_curr(round(total_landed + 250, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_47",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert $ 150 to Rands (R 2 700), add 10% duty (R 270), then add 15% VAT on the sum.",
        f"Subtotal = R 2 970. Landed cost = R 2 970 × 1,15 = {ans_str}.",
        f"Total cost = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Online shopping comparison: Buying locally in ZAR vs importing from USA with duties."""
    name = r.choice(SA_NAMES)
    rate_usd = 18.50
    local_price_zar = 4500.0
    import_price_usd = 180.0
    shipping_and_tax_usd = 40.0
    total_import_usd = import_price_usd + shipping_and_tax_usd
    total_import_zar = round(total_import_usd * rate_usd, 2)
    savings = round(local_price_zar - total_import_zar, 2)
    ans_str = f"Cheaper to import by {_fmt_curr(savings)}"

    prompt = (
        f"{name} wants to purchase an ergonomic office chair:\n"
        f"• Local South African store price: {_fmt_curr(local_price_zar)}\n"
        f"• US e-commerce site price (including international delivery & taxes): {_fmt_curr(total_import_usd, '$')}\n\n"
        f"Using an exchange rate of $1,00 = {_fmt_curr(rate_usd)}, compare the two options "
        f"and determine which option is cheaper and by how much."
    )
    explanation = (
        f"Step 1: Convert the total imported price to South African Rands:\n"
        f"\\text{{Import in ZAR}} = {total_import_usd} \\times 18,50 = {_fmt_curr(total_import_zar)}. [1 mark]\n"
        f"Step 2: Compare with the local price:\n"
        f"\\text{{Local Price}} = {_fmt_curr(local_price_zar)}; \\text{{Import Price}} = {_fmt_curr(total_import_zar)}. [1 mark]\n"
        f"Step 3: Subtract to find the savings:\n"
        f"4\\,500 - {total_import_zar:.2f} = {savings:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Cheaper to buy locally by {_fmt_curr(savings)}",
        f"Cheaper to import by {_fmt_curr(round(savings + 350, 2))}",
        "Both options have identical costs",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_48",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert the US price to Rands (multiply by 18,50) and subtract from the local price.",
        f"Import = 220 × 18,50 = {_fmt_curr(total_import_zar)}. Savings = 4 500 - {_fmt(total_import_zar)}.",
        f"Outcome = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Commercial importer: Foreign invoice payment with exchange rate fluctuation (gain or loss)."""
    name = r.choice(SA_NAMES)
    invoice_usd = 25000.0
    rate_order = 18.00     # $1 = R 18,00 on order date
    rate_payment = 18.75   # $1 = R 18,75 on payment date 30 days later
    cost_order = round(invoice_usd * rate_order, 2)
    cost_payment = round(invoice_usd * rate_payment, 2)
    exchange_loss = round(cost_payment - cost_order, 2)
    ans_str = f"Exchange loss of {_fmt_curr(exchange_loss)}"

    prompt = (
        f"{name}'s manufacturing business imports machine parts from Chicago with an invoice of {_fmt_curr(invoice_usd, '$')}.\n"
        f"When the order was placed, the exchange rate was $1,00 = {_fmt_curr(rate_order)}.\n"
        f"When the invoice was paid 30 days later, the Rand had weakened to $1,00 = {_fmt_curr(rate_payment)}.\n"
        f"Calculate the exchange gain or loss incurred by the business in South African Rands."
    )
    explanation = (
        f"Step 1: Calculate the Rand cost on the order date:\n"
        f"\\text{{Order Cost}} = 25\\,000 \\times 18,00 = {_fmt_curr(cost_order)}. [1 mark]\n"
        f"Step 2: Calculate the Rand cost on the payment date:\n"
        f"\\text{{Payment Cost}} = 25\\,000 \\times 18,75 = {_fmt_curr(cost_payment)}. [1 mark]\n"
        f"Step 3: Subtract to determine the financial impact:\n"
        f"\\text{{Extra Cost}} = {cost_payment:,.2f} - {cost_order:,.2f} = {exchange_loss:,.2f}.\n"
        f"Because the company had to pay more Rands, it is an {ans_str}. [1 mark]"
    )
    distractors = [
        f"Exchange gain of {_fmt_curr(exchange_loss)}",
        f"Exchange loss of {_fmt_curr(round(exchange_loss * 1.5, 2))}",
        f"Exchange loss of {_fmt_curr(round(exchange_loss / 2, 2))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_49",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply $ 25 000 by both rates; the increase represents an exchange loss.",
        f"Order = {_fmt_curr(cost_order)}, Payment = {_fmt_curr(cost_payment)}. Loss = {_fmt_curr(exchange_loss)}.",
        f"Result = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Commercial exporter: Converting container shipment invoice in foreign currency to Rands."""
    name = r.choice(SA_NAMES)
    containers = 4
    eur_per_container = 8200.0  # Rooibos tea export
    rate_eur = 20.40  # €1 = R 20,40
    total_eur = containers * eur_per_container
    total_zar = round(total_eur * rate_eur, 2)
    ans_str = _fmt_curr(total_zar)

    prompt = (
        f"{name}'s agricultural cooperative in the Cederberg exports {containers} shipping containers of organic rooibos tea "
        f"to Hamburg, Germany at a contractual price of {_fmt_curr(eur_per_container, '€')} per container.\n"
        f"If the commercial exchange rate upon receipt of funds is €1,00 = {_fmt_curr(rate_eur)},\n"
        f"calculate the total revenue received in South African Rands (ZAR)."
    )
    explanation = (
        f"Step 1: Calculate total contract revenue in Euros:\n"
        f"\\text{{Total Euros}} = {containers} \\times 8\\,200 = {_fmt_curr(total_eur, '€')}. [1 mark]\n"
        f"Step 2: Multiply total Euros by the exchange rate of 20,40:\n"
        f"\\text{{Revenue in ZAR}} = {total_eur:,.0f} \\times 20,40 = {total_zar:,.2f} [1 mark]\n"
        f"Step 3: State the final total in Rands:\n"
        f"\\text{{Total revenue}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_eur / rate_eur, 2)),
        _fmt_curr(round(total_zar + 25000, 2)),
        _fmt_curr(round(total_zar - 25000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_50",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply containers by Euro price, then multiply by 20,40.",
        f"Total EUR = 4 × 8 200 = {_fmt_curr(total_eur, '€')}. Rands = {total_eur:,.0f} × 20,40.",
        f"Total revenue = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Multi-destination international business itinerary across three different currencies."""
    name = r.choice(SA_NAMES)
    london_gbp = 400.0   # at £1 = R 23,50 -> R 9 400
    paris_eur = 500.0    # at €1 = R 20,00 -> R 10 000
    dubai_aed = 1800.0   # at 1 AED = R 5,00 -> R 9 000

    gbp_rate = 23.50
    eur_rate = 20.00
    aed_rate = 5.00

    london_zar = round(london_gbp * gbp_rate, 2)
    paris_zar = round(paris_eur * eur_rate, 2)
    dubai_zar = round(dubai_aed * aed_rate, 2)
    grand_total_zar = round(london_zar + paris_zar + dubai_zar, 2)
    ans_str = _fmt_curr(grand_total_zar)

    prompt = (
        f"{name} attended a series of trade expos across three countries with the following hotel bills:\n"
        f"• London (UK): {_fmt_curr(london_gbp, '£')} (Exchange rate: £1,00 = {_fmt_curr(gbp_rate)})\n"
        f"• Paris (France): {_fmt_curr(paris_eur, '€')} (Exchange rate: €1,00 = {_fmt_curr(eur_rate)})\n"
        f"• Dubai (UAE): {_fmt_curr(dubai_aed, 'AED ')} (Exchange rate: 1 AED = {_fmt_curr(aed_rate)})\n\n"
        f"Calculate the total combined hotel expenses converted into South African Rands (ZAR)."
    )
    explanation = (
        f"Step 1: Convert each currency into South African Rands:\n"
        f"- London: 400 \\times 23,50 = {_fmt_curr(london_zar)}\n"
        f"- Paris: 500 \\times 20,00 = {_fmt_curr(paris_zar)}\n"
        f"- Dubai: 1\\,800 \\times 5,00 = {_fmt_curr(dubai_zar)}. [1 mark]\n"
        f"Step 2: Sum the three converted Rand amounts:\n"
        f"\\text{{Total ZAR}} = 9\\,400 + 10\\,000 + 9\\,000 [1 mark]\n"
        f"Step 3: State the grand total:\n"
        f"\\text{{Total cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(grand_total_zar - 2500, 2)),
        _fmt_curr(round(grand_total_zar + 3500, 2)),
        _fmt_curr(round(london_gbp + paris_eur + dubai_aed, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_51",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert each hotel bill into Rands and sum the three values.",
        f"London = {_fmt_curr(london_zar)}, Paris = {_fmt_curr(paris_zar)}, Dubai = {_fmt_curr(dubai_zar)}.",
        f"Total = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Credit card foreign transaction surcharge: Overseas POS swipe + 2,75% international fee."""
    name = r.choice(SA_NAMES)
    rate_usd = 18.40  # $1 = R 18,40
    bill_usd = 220.0
    intl_fee_pct = 2.75

    base_zar = round(bill_usd * rate_usd, 2)
    fee_zar = round(base_zar * (intl_fee_pct / 100.0), 2)
    total_billed = round(base_zar + fee_zar, 2)
    ans_str = _fmt_curr(total_billed)

    prompt = (
        f"While dining at a conference in Atlanta, {name} paid a restaurant bill of {_fmt_curr(bill_usd, '$')} "
        f"using a South African credit card.\n"
        f"The bank converted the transaction using an exchange rate of $1,00 = {_fmt_curr(rate_usd)} "
        f"and added an international currency conversion fee of 2,75% on the converted Rand value.\n"
        f"Calculate the total amount in South African Rands billed to {name}'s credit card statement."
    )
    explanation = (
        f"Step 1: Convert the dinner bill to South African Rands:\n"
        f"\\text{{Base ZAR}} = 220 \\times 18,40 = {_fmt_curr(base_zar)}. [1 mark]\n"
        f"Step 2: Calculate the 2,75% bank cross-border fee:\n"
        f"\\text{{Fee}} = {_fmt(base_zar)} \\times 0,0275 = {_fmt_curr(fee_zar)}. [1 mark]\n"
        f"Step 3: Add the fee to the base amount:\n"
        f"\\text{{Total Billed}} = {_fmt(base_zar)} + {_fmt(fee_zar)} = {total_billed:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(base_zar),
        _fmt_curr(round(base_zar - fee_zar, 2)),
        _fmt_curr(round(total_billed + 75.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_52",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply dollars by 18,40 to get Rands, then add the 2,75% cross-border fee.",
        f"Base = 220 × 18,40 = {_fmt_curr(base_zar)}. Fee = 2,75% of {_fmt(base_zar)} = {_fmt_curr(fee_zar)}.",
        f"Total statement charge = {ans_str}.",
        r,
        difficulty="medium",
    )
