"""Subskills 41 to 46: Stokvels, rotational payout schemes, bulk buying cooperatives, and communal savings yields."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_41_stokvel_pool_fund(r: random.Random) -> Dict[str, Any]:
    """Calculate the monthly and annual pooled funds of a South African stokvel."""
    members = r.choice([12, 15, 20])
    monthly_contrib = r.choice([500.00, 1000.00, 1500.00])
    monthly_pool = members * monthly_contrib
    annual_pool = monthly_pool * 12

    correct_ans = f"Monthly Pool: {_fmt_curr(monthly_pool)}; Annual Pool: {_fmt_curr(annual_pool)}"
    custom_options = [
        correct_ans,
        f"Monthly Pool: {_fmt_curr(monthly_pool)}; Annual Pool: {_fmt_curr(monthly_pool * 10)}",
        f"Monthly Pool: {_fmt_curr(monthly_contrib * 12)}; Annual Pool: {_fmt_curr(annual_pool * 1.5)}",
        f"Monthly Pool: {_fmt_curr(monthly_pool / 2)}; Annual Pool: {_fmt_curr(annual_pool / 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A community savings stokvel in Soweto has {members} active members. Each member contributes a fixed "
        f"amount of {_fmt_curr(monthly_contrib)} on the first Sunday of every month.\n\n"
        f"Calculate the total funds collected into the stokvel pool each month, and the total pooled over a full 12-month year."
    )
    explanation = (
        f"Step 1: Monthly pool = {members} members × {_fmt_curr(monthly_contrib)} = {_fmt_curr(monthly_pool)} [M].\n"
        f"Step 2: Annual pool = {_fmt_curr(monthly_pool)} × 12 months = {_fmt_curr(annual_pool)} [M].\n"
        f"Step 3: Monthly: {_fmt_curr(monthly_pool)}; Annual: {_fmt_curr(annual_pool)} [A]."
    )
    return _build_question_payload(
        subskill_id="41_stokvel_pool_fund",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the number of members by the monthly contribution, then multiply by 12 for the annual total.",
        tier_2=f"Monthly = {members} × {_fmt_curr(monthly_contrib)}. Annual = Monthly × 12.",
        tier_3=f"Monthly pool is {_fmt_curr(monthly_pool)}, Annual pool is {_fmt_curr(annual_pool)}.",
        r=r,
    )


def generate_42_rotational_payout_schedule(r: random.Random) -> Dict[str, Any]:
    """Analyze a rotational payout stokvel schedule where one member receives the lump sum each month."""
    members = 12
    monthly_contrib = 1000.00
    payout = members * monthly_contrib

    correct_ans = f"Each member receives a lump sum of {_fmt_curr(payout)} once per 12-month cycle, with zero interest added"

    custom_options = [
        correct_ans,
        f"Each member receives {_fmt_curr(payout * 1.25)} because of stock exchange investment dividends",
        f"Only the stokvel chairperson receives the lump sum each month",
        f"Each member receives {_fmt_curr(monthly_contrib)} per month",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a 12-member rotational payout stokvel, every member deposits {_fmt_curr(monthly_contrib)} monthly, "
        f"and one member takes turns receiving the entire monthly pool.\n\n"
        f"Determine the payout amount each member receives and evaluate the financial interest benefit of this scheme."
    )
    explanation = (
        f"Step 1: Total monthly collection = 12 × {_fmt_curr(monthly_contrib)} = {_fmt_curr(payout)} [M].\n"
        f"Step 2: The recipient receives {_fmt_curr(payout)}, which equals their total annual contributions [M].\n"
        f"Step 3: Rotational stokvels function as forced savings mechanisms rather than interest-bearing investments [A]."
    )
    return _build_question_payload(
        subskill_id="42_rotational_payout_schedule",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the full monthly collection received by the rotating member.",
        tier_2=f"12 × {_fmt_curr(monthly_contrib)} = {_fmt_curr(payout)}.",
        tier_3="Each member receives a R 12 000 lump sum once a year with no interest.",
        r=r,
    )


def generate_43_bulk_grocery_discount_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate collective savings achieved by a shared buying scheme stokvel purchasing bulk groceries."""
    members = 15
    retail_cost_per_family = 3200.00
    wholesale_cost_per_family = 2450.00

    total_retail = members * retail_cost_per_family
    total_wholesale = members * wholesale_cost_per_family
    total_stokvel_saving = total_retail - total_wholesale
    saving_pct = (total_stokvel_saving / total_retail) * 100

    correct_ans = f"Total stokvel saving: {_fmt_curr(total_stokvel_saving)} ({_fmt(saving_pct, 1)}% savings; {_fmt_curr(retail_cost_per_family - wholesale_cost_per_family)} per family)"
    custom_options = [
        correct_ans,
        f"Total stokvel saving: {_fmt_curr(wholesale_cost_per_family)} (50,0% savings)",
        f"Total stokvel saving: R 0,00 (wholesale depots charge equal prices to supermarkets)",
        f"Total stokvel saving: {_fmt_curr(total_stokvel_saving * 2)} (due to government subsidies)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A shared buying scheme stokvel with {members} families pools funds in December to buy festive groceries "
        f"directly from a wholesale distributor.\n"
        f"• If bought individually at retail supermarkets, each family's basket costs {_fmt_curr(retail_cost_per_family)}.\n"
        f"• Buying in bulk pallets at wholesale drops the cost to {_fmt_curr(wholesale_cost_per_family)} per family.\n\n"
        f"Calculate the total monetary saving achieved by the stokvel group and the percentage discount."
    )
    explanation = (
        f"Step 1: Total retail cost = {members} × {_fmt_curr(retail_cost_per_family)} = {_fmt_curr(total_retail)} [M].\n"
        f"Step 2: Total wholesale cost = {members} × {_fmt_curr(wholesale_cost_per_family)} = {_fmt_curr(total_wholesale)} [M].\n"
        f"Step 3: Total saving = {_fmt_curr(total_retail)} - {_fmt_curr(total_wholesale)} = {_fmt_curr(total_stokvel_saving)} ({_fmt(saving_pct, 1)}%) [A]."
    )
    return _build_question_payload(
        subskill_id="43_bulk_grocery_discount_savings",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the total retail cost and total wholesale cost for all 15 families, then find the difference.",
        tier_2=f"Retail total: {_fmt_curr(total_retail)}. Wholesale total: {_fmt_curr(total_wholesale)}.",
        tier_3=f"The group saves {_fmt_curr(total_stokvel_saving)} ({_fmt(saving_pct, 1)}%).",
        r=r,
    )


def generate_44_stokvel_bank_fees_and_interest(r: random.Random) -> Dict[str, Any]:
    """Calculate net annual yield on a stokvel bank account deducting monthly maintenance fees."""
    annual_interest_earned = r.choice([6800.00, 7450.00, 8200.00, 9100.00])
    monthly_account_fee = r.choice([75.00, 85.00, 95.00])
    annual_fees = monthly_account_fee * 12
    net_interest = annual_interest_earned - annual_fees

    d_spec_44 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Stokvel Account Annual Yield ({_fmt_curr(net_interest)})",
        "categories": ["Gross Interest", "Bank Fees", "Net Yield"],
        "series": [
            {"name": "Amount", "values": [annual_interest_earned, annual_fees, net_interest]}
        ],
    }

    correct_ans = f"Net interest yield = {_fmt_curr(net_interest)} (Gross: {_fmt_curr(annual_interest_earned)} - Fees: {_fmt_curr(annual_fees)})"
    custom_options = [
        correct_ans,
        f"Net interest yield = {_fmt_curr(annual_interest_earned)} (Banks do not charge fees to registered stokvels)",
        f"Net interest yield = {_fmt_curr(annual_interest_earned + annual_fees)}",
        f"Net interest yield = {_fmt_curr(net_interest * 0.85)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the stokvel savings account statement for accumulated savings of R 120 000.\n"
        f"• Gross interest earned over the year: {_fmt_curr(annual_interest_earned)}\n"
        f"• Monthly account maintenance fee: {_fmt_curr(monthly_account_fee)}\n\n"
        f"Calculate the net interest earned by the stokvel after bank account fees are deducted for the year."
    )
    explanation = (
        f"Step 1: Total annual bank fees = 12 × {_fmt_curr(monthly_account_fee)} = {_fmt_curr(annual_fees)} [M].\n"
        f"Step 2: Net Interest = Gross Interest - Annual Fees = {_fmt_curr(annual_interest_earned)} - {_fmt_curr(annual_fees)} [M].\n"
        f"Step 3: Net Interest Yield = {_fmt_curr(net_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="44_stokvel_bank_fees_and_interest",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the monthly bank fee by 12, then subtract from the gross interest earned.",
        tier_2=f"Annual fees = 12 × {_fmt_curr(monthly_account_fee)} = {_fmt_curr(annual_fees)}. Subtract from {_fmt_curr(annual_interest_earned)}.",
        tier_3=f"The net interest is {_fmt_curr(net_interest)}.",
        r=r,
        diagram_spec=d_spec_44,
    )


def generate_45_burial_society_premium_claims(r: random.Random) -> Dict[str, Any]:
    """Calculate the reserve balance of a communal burial society after claims and admin expenses."""
    members = r.choice([50, 60, 70, 80])
    premium = r.choice([120.00, 150.00, 200.00])
    annual_premiums = members * premium * 12
    claims_paid = 2 * 25000.00  # two bereavement claims of R25 000
    admin_costs = 6000.00
    net_reserve = annual_premiums - claims_paid - admin_costs

    d_spec_45 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Burial Society Financial Overview ({_fmt_curr(annual_premiums)})",
        "categories": ["Premiums Collected", "Claims Paid", "Admin Costs", "Net Reserve"],
        "series": [
            {"name": "Amount", "values": [annual_premiums, claims_paid, admin_costs, net_reserve]}
        ],
    }

    correct_ans = f"Annual Premiums: {_fmt_curr(annual_premiums)}; Year-end Net Reserve: {_fmt_curr(net_reserve)}"
    custom_options = [
        correct_ans,
        f"Annual Premiums: {_fmt_curr(annual_premiums)}; Year-end Net Reserve: {_fmt_curr(annual_premiums - claims_paid)}",
        f"Annual Premiums: {_fmt_curr(annual_premiums / 2)}; Year-end Net Reserve: {_fmt_curr(net_reserve / 2)}",
        f"Annual Premiums: {_fmt_curr(annual_premiums)}; Year-end Net Reserve: R 0,00",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the annual financial summary of a registered burial society stokvel with {members} active members paying a monthly premium of {_fmt_curr(premium)}.\n"
        f"During the year:\n"
        f"• The society paid out 2 funeral bereavement claims of R 25 000,00 each.\n"
        f"• Administrative catering and transport expenses totaled {_fmt_curr(admin_costs)}.\n\n"
        f"Calculate the total annual premium revenue collected and the remaining net reserve funds added to the society's account."
    )
    explanation = (
        f"Step 1: Total premium revenue = {members} × {_fmt_curr(premium)} × 12 = {_fmt_curr(annual_premiums)} [M].\n"
        f"Step 2: Total outlays = {_fmt_curr(claims_paid)} (claims) + {_fmt_curr(admin_costs)} (admin) = {_fmt_curr(claims_paid + admin_costs)} [M].\n"
        f"Step 3: Net Reserve = {_fmt_curr(annual_premiums)} - {_fmt_curr(claims_paid + admin_costs)} = {_fmt_curr(net_reserve)} [A]."
    )
    return _build_question_payload(
        subskill_id="45_burial_society_premium_claims",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total premiums (60 × R 150 × 12), then subtract funeral claims and admin expenses.",
        tier_2=f"Revenue = {_fmt_curr(annual_premiums)}. Deduct R 50 000 claims and {_fmt_curr(admin_costs)} admin.",
        tier_3=f"The net reserve fund addition is {_fmt_curr(net_reserve)}.",
        r=r,
        diagram_spec=d_spec_45,
    )


def generate_46_stokvel_yield_vs_individual_retail(r: random.Random) -> Dict[str, Any]:
    """Compare higher institutional interest rates obtained by a pooled stokvel versus a small retail saver."""
    principal = 100000.00
    stokvel_rate = 8.5
    retail_rate = 5.0
    stokvel_interest = principal * (stokvel_rate / 100.0)
    retail_interest = principal * (retail_rate / 100.0)
    extra_interest = stokvel_interest - retail_interest

    correct_ans = f"Stokvel pool earns {_fmt_curr(extra_interest)} more per year ({_fmt_pct(stokvel_rate)} vs {_fmt_pct(retail_rate)})"
    custom_options = [
        correct_ans,
        f"Retail savings account earns {_fmt_curr(extra_interest)} more due to individual tax exemptions",
        f"Both earn identical interest because banking regulations enforce equal interest rates",
        f"Stokvel pool earns {_fmt_curr(extra_interest * 2)} more due to municipal bonus coupons",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A community group pools R 100 000,00 into a 32-day notice Stokvel Club Account earning {_fmt_pct(stokvel_rate)} p.a.\n"
        f"An individual saver with only R 10 000,00 can only access a basic retail savings account earning {_fmt_pct(retail_rate)} p.a.\n\n"
        f"Calculate the annual interest advantage earned on R 100 000 under the wholesale stokvel rate compared to the retail rate."
    )
    explanation = (
        f"Step 1: Stokvel interest = {_fmt_curr(principal)} × {_fmt_pct(stokvel_rate)} = {_fmt_curr(stokvel_interest)} [M].\n"
        f"Step 2: Retail interest = {_fmt_curr(principal)} × {_fmt_pct(retail_rate)} = {_fmt_curr(retail_interest)} [M].\n"
        f"Step 3: Difference = {_fmt_curr(stokvel_interest)} - {_fmt_curr(retail_interest)} = {_fmt_curr(extra_interest)} [A]."
    )
    return _build_question_payload(
        subskill_id="46_stokvel_yield_vs_individual_retail",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the difference in interest earned on R 100 000 at 8,5% versus 5,0%.",
        tier_2=f"Stokvel: {_fmt_curr(stokvel_interest)}; Retail: {_fmt_curr(retail_interest)}.",
        tier_3=f"The pooled advantage is {_fmt_curr(extra_interest)} per year.",
        r=r,
    )
