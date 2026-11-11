"""Municipal Accounts & Invoices Interpretation Subskills (Subskills 1 to 9).

1. fin_doc_muni_account_number_and_easypay_reference
2. fin_doc_muni_property_valuation_and_rates_formula
3. fin_doc_muni_electricity_meter_consumption_kwh
4. fin_doc_muni_water_meter_consumption_kl
5. fin_doc_muni_daily_average_consumption
6. fin_doc_muni_balance_carried_forward_reconciliation
7. fin_doc_muni_overdue_interest_penalty_charge
8. fin_doc_muni_refuse_removal_and_bin_levy
9. fin_doc_muni_sewage_sanitation_percentage_of_water
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_MUNICIPALITIES, SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_doc_muni_account_number_and_easypay_reference(r: random.Random) -> Dict[str, Any]:
    """Identify payment reference identifiers on a municipal tax invoice."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    acc_num = f"{r.randint(100, 999)} {r.randint(100, 999)} {r.randint(100, 999)}"
    easypay_no = f"91404{r.randint(10000000, 99999999)}"
    due_date = f"{r.randint(15, 28)}/02/2024"

    prompt = (
        f"{name} receives a monthly utility tax invoice from {muni} containing the following summary header:\n\n"
        f"• **Account Number**: {acc_num}\n"
        f"• **EasyPay Barcode Number**: {easypay_no}\n"
        f"• **Payment Due Date**: {due_date}\n\n"
        f"Which reference number must {name} provide when paying the bill at an EasyPay pay-point or retail till counter?"
    )
    ans_str = f"EasyPay Barcode Number ({easypay_no})"
    distractors = [
        f"Account Number ({acc_num})",
        f"Municipal Head Office Telephone Number",
        f"Property Stand Size Number"
    ]
    sol = (
        f"Step 1: Understand payment channel identifier requirements:\n"
        f"• The Account Number ({acc_num}) is used for direct bank electronic transfers and branch deposits.\n"
        f"• The EasyPay Barcode Number ({easypay_no}) is the unique automated reference required by EasyPay kiosks, "
        f"retail till points (Pick n Pay, Shoprite, Checkers), and postal outlets.\n\n"
        f"Step 2: Method setup – match payment channel to reference type:\n"
        f"• Channel requested: EasyPay pay-point / retail counter\n"
        f"• Reference required: EasyPay number\n"
        f"✓ [1 Mark: Method – distinguishing between bank account reference and EasyPay pay-point number]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct payment reference identified]"
    )
    rubric = [
        "1 Mark: Method – matching EasyPay payment channel with EasyPay barcode reference",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": "Look for the number specifically labeled for EasyPay payments.",
        "tier_2": "The EasyPay barcode number begins with 91404.",
        "tier_3": f"The correct reference is the {ans_str}."
    }
    return _make_q(
        "fin_doc_muni_account_number_and_easypay_reference",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_fin_doc_muni_property_valuation_and_rates_formula(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly residential property rates using municipal market valuation and rate in the Rand."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    valuation = r.choice([650000, 850000, 1100000, 1250000, 1500000])
    rebate_exempt = 150000.00  # Statutory rates exemption on first R 150 000
    rate_in_rand = 0.00685  # R 0.00685 per Rand of market value per year

    taxable_market_val = valuation - rebate_exempt
    annual_rates = taxable_market_val * rate_in_rand
    monthly_rates = round(annual_rates / 12, 2)
    ans_str = _fmt_curr(monthly_rates)

    prompt = (
        f"{name}'s residential property in {muni} has a municipal market valuation of {_fmt_curr(valuation)}.\n"
        f"The municipal property rates policy states:\n"
        f"• The first **{_fmt_curr(rebate_exempt)}** of market value is completely exempt from property rates.\n"
        f"• Rates are charged at an annual tariff of **R 0,00685 per Rand of market value** above the exempt threshold.\n\n"
        f"Calculate {name}'s **monthly property rates charge**.\n"
        f"Use the formula: $$\\text{{Monthly Rates}} = \\frac{{(\\text{{Market Valuation}} - \\text{{Exemption}}) \\times 0,00685}}{{12}}$$"
    )
    sol = (
        f"Step 1: Calculate the taxable market value above the exemption:\n"
        f"• Taxable Valuation = {_fmt_curr(valuation)} - {_fmt_curr(rebate_exempt)} = {_fmt_curr(taxable_market_val)}\n\n"
        f"Step 2: Method setup – calculate annual rates and divide by 12 months:\n"
        f"• Annual Rates = {_fmt_curr(taxable_market_val)} × 0,00685 = {_fmt_curr(annual_rates)}\n"
        f"• Monthly Rates = {_fmt_curr(annual_rates)} ÷ 12 "
        f"✓ [1 Mark: Method – subtracting exemption, multiplying by rate in the Rand, and dividing by 12]\n\n"
        f"Step 3: Calculate monthly rates:\n"
        f"Monthly Rates = {ans_str} ✓ [1 Mark: Accuracy – correct monthly property rates in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating (({valuation} - {rebate_exempt}) × 0,00685) / 12",
        f"1 Mark: Accuracy – correct monthly charge {ans_str}"
    ]
    hints = {
        "tier_1": f"First subtract the {_fmt_curr(rebate_exempt)} exemption from {_fmt_curr(valuation)}.",
        "tier_2": f"Multiply the taxable value by 0,00685 to get annual rates, then divide by 12.",
        "tier_3": f"(({valuation} - {rebate_exempt}) × 0,00685) ÷ 12 = {monthly_rates:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_property_valuation_and_rates_formula", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_electricity_meter_consumption_kwh(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly electricity consumption in kWh from start and end meter readings."""
    name = r.choice(SA_NAMES)
    start_reading = r.choice([45210, 52340, 68900, 74120, 82081])
    consumption = r.choice([350, 480, 560, 650, 720, 850, 900])
    end_reading = start_reading + consumption
    ans_str = f"{consumption} kWh"

    prompt = (
        f"{name}'s municipal electricity account provides the following post-paid meter readings for the billing month:\n\n"
        f"• **Meter Number**: 379357\n"
        f"• **Previous Meter Reading**: {_fmt(start_reading)} kWh\n"
        f"• **Current Meter Reading**: {_fmt(end_reading)} kWh\n\n"
        f"Calculate {name}'s **total electricity consumption (in kWh)** for this billing period.\n"
        f"Use the formula: $$\\text{{Consumption}} = \\text{{Current Reading}} - \\text{{Previous Reading}}$$"
    )
    sol = (
        f"Step 1: Identify previous and current meter readings:\n"
        f"• Current Reading = {_fmt(end_reading)} kWh\n"
        f"• Previous Reading = {_fmt(start_reading)} kWh\n\n"
        f"Step 2: Method setup – subtract previous reading from current reading:\n"
        f"• Consumption = Current Reading - Previous Reading\n"
        f"• Consumption = {end_reading} - {start_reading} "
        f"✓ [1 Mark: Method – subtracting previous meter reading from current reading]\n\n"
        f"Step 3: Calculate consumption:\n"
        f"Consumption = {ans_str} ✓ [1 Mark: Accuracy – correct units in kWh]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {start_reading} from {end_reading}",
        f"1 Mark: Accuracy – correct consumption {ans_str}"
    ]
    hints = {
        "tier_1": "Subtract the previous reading from the current reading.",
        "tier_2": f"Calculate: {end_reading} - {start_reading}.",
        "tier_3": f"{end_reading} - {start_reading} = {consumption}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_electricity_meter_consumption_kwh", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_water_meter_consumption_kl(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly water consumption in kilolitres (kL) from start and end meter readings."""
    name = r.choice(SA_NAMES)
    start_reading = round(r.choice([145.0, 182.0, 206.0, 245.0, 310.0]), 1)
    consumption = round(r.choice([14.0, 18.0, 22.5, 26.0, 31.0]), 1)
    end_reading = round(start_reading + consumption, 1)
    ans_str = f"{_fmt(consumption)} kL"

    prompt = (
        f"{name}'s municipal water bill displays the following water meter readings for a 30-day period:\n\n"
        f"• **Meter Serial**: WTR-8941\n"
        f"• **Start Reading**: {_fmt(start_reading)} kL\n"
        f"• **End Reading**: {_fmt(end_reading)} kL\n\n"
        f"Calculate the **total volume of water consumed (in kilolitres)** during this billing month."
    )
    sol = (
        f"Step 1: Identify meter reading values:\n"
        f"• End Reading = {_fmt(end_reading)} kL\n"
        f"• Start Reading = {_fmt(start_reading)} kL\n\n"
        f"Step 2: Method setup – subtract start reading from end reading:\n"
        f"• Consumption = End Reading - Start Reading\n"
        f"• Consumption = {end_reading} - {start_reading} "
        f"✓ [1 Mark: Method – subtracting start reading from end reading]\n\n"
        f"Step 3: Calculate consumption:\n"
        f"Consumption = {ans_str} ✓ [1 Mark: Accuracy – correct volume in kL]"
    )
    rubric = [
        f"1 Mark: Method – subtracting {start_reading} from {end_reading}",
        f"1 Mark: Accuracy – correct volume {ans_str}"
    ]
    hints = {
        "tier_1": "Subtract the starting meter reading from the ending meter reading.",
        "tier_2": f"Calculate: {end_reading} - {start_reading}.",
        "tier_3": f"{end_reading} - {start_reading} = {consumption}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_water_meter_consumption_kl", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_daily_average_consumption(r: random.Random) -> Dict[str, Any]:
    """Calculate the daily average consumption across a billing period."""
    name = r.choice(SA_NAMES)
    days = r.choice([28, 29, 30, 31])
    is_elec = r.choice([True, False])

    if is_elec:
        total_usage = r.choice([580, 640, 750, 870, 900, 1020])
        daily_avg = round(total_usage / days, 2)
        ans_str = f"{_fmt(daily_avg)} kWh/day"
        unit_label = "electricity in kilowatt hours (kWh)"
    else:
        total_usage = r.choice([16.0, 18.0, 21.0, 24.5, 28.0])
        daily_avg = round(total_usage / days, 3)
        ans_str = f"{_fmt(daily_avg, 3)} kL/day"
        unit_label = "water in kilolitres (kL)"

    prompt = (
        f"{name}'s household consumed a total of **{_fmt(total_usage)}** of {unit_label} "
        f"over a billing cycle of **{days} days**.\n\n"
        f"Calculate the **daily average consumption** for {name}'s household.\n"
        f"Use the formula: $$\\text{{Daily Average}} = \\frac{{\\text{{Total Consumption}}}}{{\\text{{Number of Days}}ানী}}$$"
    )
    sol = (
        f"Step 1: Identify total consumption and billing days:\n"
        f"• Total Consumption = {_fmt(total_usage)}\n"
        f"• Days in billing cycle = {days} days\n\n"
        f"Step 2: Method setup – divide total consumption by number of days:\n"
        f"• Daily Average = Total Consumption ÷ Days\n"
        f"• Daily Average = {total_usage} ÷ {days} "
        f"✓ [1 Mark: Method – dividing total consumption by {days} days]\n\n"
        f"Step 3: Calculate daily rate:\n"
        f"Daily Average = {ans_str} ✓ [1 Mark: Accuracy – correct daily average with units]"
    )
    rubric = [
        f"1 Mark: Method – dividing {total_usage} by {days}",
        f"1 Mark: Accuracy – correct daily average {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the total usage ({_fmt(total_usage)}) by {days} days.",
        "tier_2": f"Calculate: {total_usage} ÷ {days}.",
        "tier_3": f"{total_usage} ÷ {days} = {daily_avg}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_daily_average_consumption", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_balance_carried_forward_reconciliation(r: random.Random) -> Dict[str, Any]:
    """Reconcile previous balance, payments made, current charges, and total balance due."""
    name = r.choice(SA_NAMES)
    prev_balance = round(r.choice([1250.00, 1450.50, 1890.00, 2100.00]), 2)
    payment_made = round(r.choice([1000.00, 1250.00, 1500.00]), 2)
    current_charges = round(r.choice([1120.40, 1345.80, 1560.20, 1780.50]), 2)

    subtotal = round(prev_balance - payment_made, 2)
    total_due = round(subtotal + current_charges, 2)
    ans_str = _fmt_curr(total_due)

    prompt = (
        f"Below is a financial summary section from {name}'s municipal account:\n\n"
        f"| Description | Amount |\n"
        f"| :--- | :---: |\n"
        f"| Previous Balance Carried Forward | {_fmt_curr(prev_balance)} |\n"
        f"| Less: Payment Received (EFT) | -{_fmt_curr(payment_made)} |\n"
        f"| Current Monthly Utility Charges | {_fmt_curr(current_charges)} |\n\n"
        f"Calculate the **Total Amount Due** that {name} must pay for this statement."
    )
    sol = (
        f"Step 1: Calculate outstanding subtotal from previous cycle:\n"
        f"• Outstanding Subtotal = Previous Balance - Payment Received\n"
        f"• Subtotal = {_fmt_curr(prev_balance)} - {_fmt_curr(payment_made)} = {_fmt_curr(subtotal)}\n\n"
        f"Step 2: Method setup – add current monthly charges:\n"
        f"• Total Due = Subtotal + Current Charges\n"
        f"• Total Due = {_fmt_curr(subtotal)} + {_fmt_curr(current_charges)} "
        f"✓ [1 Mark: Method – subtracting payment from previous balance and adding current charges]\n\n"
        f"Step 3: Calculate total amount due:\n"
        f"Total Amount Due = {ans_str} ✓ [1 Mark: Accuracy – correct total balance in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating ({_fmt_curr(prev_balance)} - {_fmt_curr(payment_made)}) + {_fmt_curr(current_charges)}",
        f"1 Mark: Accuracy – correct total due {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract the payment ({_fmt_curr(payment_made)}) from previous balance ({_fmt_curr(prev_balance)}).",
        "tier_2": f"Add the current charges ({_fmt_curr(current_charges)}) to that remainder.",
        "tier_3": f"{prev_balance:.2f} - {payment_made:.2f} + {current_charges:.2f} = {total_due:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_balance_carried_forward_reconciliation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_overdue_interest_penalty_charge(r: random.Random) -> Dict[str, Any]:
    """Calculate the late payment interest penalty on an overdue municipal balance."""
    name = r.choice(SA_NAMES)
    overdue_amt = r.choice([1200, 1500, 2000, 2500, 3200, 4500])
    annual_rate = r.choice([9.5, 10.5, 11.0, 12.0, 13.5])
    # 1 month late
    monthly_rate = (annual_rate / 100) / 12
    interest_penalty = round(overdue_amt * monthly_rate, 2)
    ans_str = _fmt_curr(interest_penalty)

    prompt = (
        f"{name}'s municipal account has an overdue unpaid balance of {_fmt_curr(overdue_amt)}.\n"
        f"The municipal credit control policy charges late payment penalty interest of "
        f"{_fmt(annual_rate)}% per annum on all arrears balances.\n\n"
        f"Calculate the **penalty interest charged** to {name}'s account for 1 month.\n"
        f"Use the formula: $$\\text{{Monthly Interest}} = \\text{{Arrears Amount}} \\times \\frac{{\\text{{Annual Rate (\\%)}}}}{{12 \\times 100}}$$"
    )
    sol = (
        f"Step 1: Identify arrears amount and monthly rate:\n"
        f"• Arrears Balance = {_fmt_curr(overdue_amt)}\n"
        f"• Annual interest rate = {_fmt(annual_rate)}%\n"
        f"• Monthly interest fraction = ({annual_rate} ÷ 100) ÷ 12\n\n"
        f"Step 2: Method setup – calculate 1 month of interest:\n"
        f"• Interest = {_fmt_curr(overdue_amt)} × ({annual_rate}/100) × (1/12) "
        f"✓ [1 Mark: Method – applying annual interest rate divided by 12 to overdue balance]\n\n"
        f"Step 3: Calculate penalty interest:\n"
        f"Monthly Interest = {ans_str} ✓ [1 Mark: Accuracy – correct penalty fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {_fmt_curr(overdue_amt)} by ({annual_rate}/100) / 12",
        f"1 Mark: Accuracy – correct interest {ans_str}"
    ]
    hints = {
        "tier_1": f"Find {_fmt(annual_rate)}% of {_fmt_curr(overdue_amt)}, then divide by 12 months.",
        "tier_2": f"Calculate: ({overdue_amt} × {annual_rate / 100}) ÷ 12.",
        "tier_3": f"({overdue_amt} × {annual_rate / 100}) ÷ 12 = {interest_penalty:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_overdue_interest_penalty_charge", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_refuse_removal_and_bin_levy(r: random.Random) -> Dict[str, Any]:
    """Calculate annual refuse removal cost for standard 240L wheelie bins."""
    name = r.choice(SA_NAMES)
    num_bins = r.choice([1, 2, 3])
    monthly_per_bin = round(r.choice([148.50, 165.00, 182.20, 195.00]), 2)

    annual_total = round(num_bins * monthly_per_bin * 12, 2)
    ans_str = _fmt_curr(annual_total)

    prompt = (
        f"{name}'s business premises utilizes {num_bins} standard 240L municipal wheelie bin(s) for waste management. "
        f"The municipality bills refuse collection at {_fmt_curr(monthly_per_bin)} per bin per month.\n\n"
        f"Calculate the **total annual refuse removal cost** for {name}'s premises over 12 months."
    )
    sol = (
        f"Step 1: Calculate the total monthly refuse cost:\n"
        f"• Monthly Refuse = {num_bins} bin(s) × {_fmt_curr(monthly_per_bin)} = {_fmt_curr(num_bins * monthly_per_bin)}\n\n"
        f"Step 2: Method setup – multiply by 12 months:\n"
        f"• Annual Cost = Monthly Cost × 12\n"
        f"• Annual Cost = ({num_bins} × {_fmt_curr(monthly_per_bin)}) × 12 "
        f"✓ [1 Mark: Method – multiplying monthly bin fee by number of bins and 12 months]\n\n"
        f"Step 3: Calculate annual total:\n"
        f"Annual Cost = {ans_str} ✓ [1 Mark: Accuracy – correct annual refuse cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {num_bins} × {_fmt_curr(monthly_per_bin)} × 12",
        f"1 Mark: Accuracy – correct annual cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply the fee per bin ({_fmt_curr(monthly_per_bin)}) by {num_bins} bin(s).",
        "tier_2": "Multiply that monthly total by 12 months.",
        "tier_3": f"{num_bins} × {monthly_per_bin:.2f} × 12 = {annual_total:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_refuse_removal_and_bin_levy", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_doc_muni_sewage_sanitation_percentage_of_water(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic sewage/sanitation fee based on a percentage (e.g. 70%) of water consumed."""
    name = r.choice(SA_NAMES)
    water_used_kl = r.choice([15, 20, 25, 30, 35])
    sanitation_rate_per_kl = round(r.choice([8.50, 9.80, 11.20, 12.50]), 2)
    discharge_factor_pct = 70  # Municipalities assume 70% of tap water discharges into sewer system

    sewage_volume_kl = round(water_used_kl * (discharge_factor_pct / 100), 2)
    sanitation_cost = round(sewage_volume_kl * sanitation_rate_per_kl, 2)
    ans_str = _fmt_curr(sanitation_cost)

    prompt = (
        f"{name}'s household consumed **{water_used_kl} kL** of water during the month.\n"
        f"The municipal sanitation tariff rules state:\n"
        f"• Domestic wastewater discharge is estimated at **70% of total metered water consumption**.\n"
        f"• Sewerage sanitation is billed at **{_fmt_curr(sanitation_rate_per_kl)} per kL** of wastewater discharge.\n\n"
        f"Calculate the **sanitation / sewerage charge** for {name}'s household."
    )
    sol = (
        f"Step 1: Calculate the billable sewage discharge volume:\n"
        f"• Sewage Volume = 70% of {water_used_kl} kL = 0,70 × {water_used_kl} = {_fmt(sewage_volume_kl)} kL\n\n"
        f"Step 2: Method setup – multiply discharge volume by sanitation rate:\n"
        f"• Sanitation Charge = Sewage Volume × Tariff per kL\n"
        f"• Sanitation Charge = {_fmt(sewage_volume_kl)} × {_fmt_curr(sanitation_rate_per_kl)} "
        f"✓ [1 Mark: Method – applying 70% discharge factor and multiplying by rate per kL]\n\n"
        f"Step 3: Calculate sanitation charge:\n"
        f"Sanitation Charge = {ans_str} ✓ [1 Mark: Accuracy – correct sanitation charge in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (70% × {water_used_kl}) × {_fmt_curr(sanitation_rate_per_kl)}",
        f"1 Mark: Accuracy – correct charge {ans_str}"
    ]
    hints = {
        "tier_1": f"First find 70% of {water_used_kl} kL to find the wastewater discharge volume.",
        "tier_2": f"Multiply that volume ({_fmt(sewage_volume_kl)} kL) by {_fmt_curr(sanitation_rate_per_kl)}.",
        "tier_3": f"{sewage_volume_kl} × {sanitation_rate_per_kl:.2f} = {sanitation_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_doc_muni_sewage_sanitation_percentage_of_water", prompt, ans_str, sol, rubric, hints, 2, r=r)
