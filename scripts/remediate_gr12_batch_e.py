"""Remediate Batch E: remaining 17 subskills for Grade 12."""
import os
import re

# 1. telecoms_tariffs.py (subskill 17)
p1 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/telecoms_tariffs.py"
with open(p1, "r", encoding="utf-8") as f:
    c1 = f.read()

c1 = c1.replace(
'''    diff = round(cost_per_minute - cost_per_second, 2)

    prompt = (
        f"A mobile network offers two billing methods for prepaid voice calls:\\n"
        f"• Plan A (Per-Second Billing): R 0,025 per second (no rounding up)\\n"
        f"• Plan B (Per-Minute Billing): R 1,50 per minute (or part thereof, rounded up to the next full minute)\\n\\n"
        f"A subscriber makes a phone call lasting exactly {call_secs} seconds.\\n"
        f"How much more does the call cost on Plan B than on Plan A?"
    )''',
'''    diff = round(cost_per_minute - cost_per_second, 2)

    d_spec_17 = {
        "kind": "bar_graph",
        "title": f"Prepaid Call Cost Comparison ({call_secs} seconds)",
        "categories": ["Plan A (Per-Second)", "Plan B (Per-Minute)"],
        "series": [
            {"name": "Cost", "values": [cost_per_second, cost_per_minute]}
        ],
    }

    prompt = (
        f"Refer to the prepaid call cost comparison for a phone call lasting {call_secs} seconds.\\n"
        f"• Plan A (Per-Second Billing): R 0,025 per second (no rounding up)\\n"
        f"• Plan B (Per-Minute Billing): R 1,50 per minute (or part thereof, rounded up to the next full minute)\\n\\n"
        f"How much more does the call cost on Plan B than on Plan A?"
    )'''
)

c1 = c1.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_17,
    )'''
)

with open(p1, "w", encoding="utf-8") as f:
    f.write(c1)
print("Updated telecoms_tariffs.py")


# 2. small_business_costing_breakeven.py (subskill 45)
p2 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/small_business_costing_breakeven.py"
with open(p2, "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace(
'''    profit = round(total_revenue - total_cost, 2)

    prompt = (
        f"A bespoke leather-goods workshop has fixed monthly costs of R 5 500,00.\\n"
        f"Each leather wallet costs R 25,00 in raw materials and sells for R 65,00.\\n\\n"
        f"During August, the workshop made and sold {units_sold} wallets.\\n"
        f"Calculate the net profit earned by the workshop for the month."
    )''',
'''    profit = round(total_revenue - total_cost, 2)

    d_spec_45 = {
        "kind": "bar_graph",
        "title": f"Workshop Monthly Financials ({units_sold} Units Sold)",
        "categories": ["Total Revenue", "Total Cost", "Net Profit"],
        "series": [
            {"name": "Amount", "values": [total_revenue, total_cost, profit]}
        ],
    }

    prompt = (
        f"Refer to the monthly financial statement of a bespoke leather-goods workshop with fixed monthly costs of R 5 500,00.\\n"
        f"Each leather wallet costs R 25,00 in raw materials and sells for R 65,00.\\n\\n"
        f"During August, the workshop made and sold {units_sold} wallets.\\n"
        f"Calculate the net profit earned by the workshop for the month."
    )'''
)

c2 = c2.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_45,
    )'''
)

with open(p2, "w", encoding="utf-8") as f:
    f.write(c2)
print("Updated small_business_costing_breakeven.py")


# 3. budgets_financial_statements.py (subskill 47)
p3 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_financial_documents_and_tariffs/budgets_financial_statements.py"
with open(p3, "r", encoding="utf-8") as f:
    c3 = f.read()

c3 = c3.replace(
'''    net_surplus = round(total_income - total_expenditure, 2)

    prompt = (
        f"{biz_name}'s monthly Income-and-Expenditure statement lists:\\n\\n"''',
'''    net_surplus = round(total_income - total_expenditure, 2)

    d_spec_47 = {
        "kind": "bar_graph",
        "title": f"{biz_name} Monthly Statement ({_fmt_curr(total_income)})",
        "categories": ["Total Income", "Total Expenditure", "Net Surplus"],
        "series": [
            {"name": "Amount", "values": [total_income, total_expenditure, net_surplus]}
        ],
    }

    prompt = (
        f"Refer to the monthly Income-and-Expenditure statement for {biz_name}:\\n\\n"'''
)

c3 = c3.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_47",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tariff_gr12_47",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_47,
    )'''
)

with open(p3, "w", encoding="utf-8") as f:
    f.write(c3)
print("Updated budgets_financial_statements.py")


# 4. payslip_take_home_pay.py (subskill 44)
p4 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_income_tax/payslip_take_home_pay.py"
with open(p4, "r", encoding="utf-8") as f:
    c4 = f.read()

c4 = c4.replace(
'''    increase = 3000.0
    new_gross = old_gross + increase

    # In bracket 2: marginal rate is 25%, pension is 7.5%, UIF is 1%
    marginal_tax_rate = 0.25
    pension_rate = 0.075
    uif_rate = 0.01

    tax_on_increase = increase * marginal_tax_rate
    pension_on_increase = increase * pension_rate
    uif_on_increase = increase * uif_rate

    total_deductions_on_inc = tax_on_increase + pension_on_increase + uif_on_increase
    net_increase = round(increase - total_deductions_on_inc, 2)

    prompt = (
        f"{name} receives a monthly salary increase of {_fmt_curr(increase)} (gross).\\n"
        f"On this additional amount, the following deductions apply:\\n"
        f"• Marginal Income Tax: 25%\\n"
        f"• Pension Fund: 7,5%\\n"
        f"• UIF: 1%\\n\\n"
        f"Calculate the actual NET increase that {name} will see in their monthly take-home pay."
    )''',
'''    increase = r.choice([2500.0, 3000.0, 3500.0, 4000.0])
    new_gross = old_gross + increase

    # In bracket 2: marginal rate is 25%, pension is 7.5%, UIF is 1%
    marginal_tax_rate = 0.25
    pension_rate = 0.075
    uif_rate = 0.01

    tax_on_increase = increase * marginal_tax_rate
    pension_on_increase = increase * pension_rate
    uif_on_increase = increase * uif_rate

    total_deductions_on_inc = tax_on_increase + pension_on_increase + uif_on_increase
    net_increase = round(increase - total_deductions_on_inc, 2)

    d_spec_44 = {
        "kind": "pie_chart",
        "title": f"Gross Increase Deductions ({_fmt_curr(increase)})",
        "slices": [
            {"name": "Net Increase", "value": net_increase},
            {"name": "Income Tax (25%)", "value": tax_on_increase},
            {"name": "Pension (7,5%)", "value": pension_on_increase},
            {"name": "UIF (1%)", "value": uif_on_increase},
        ],
    }

    prompt = (
        f"Refer to the salary increase deduction breakdown for {name} receiving a monthly increase of {_fmt_curr(increase)} (gross).\\n"
        f"On this additional amount, the following deductions apply:\\n"
        f"• Marginal Income Tax: 25%\\n"
        f"• Pension Fund: 7,5%\\n"
        f"• UIF: 1%\\n\\n"
        f"Calculate the actual NET increase that {name} will see in their monthly take-home pay."
    )'''
)

c4 = c4.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tax_gr12_44",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tax_gr12_44",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_44,
    )'''
)

with open(p4, "w", encoding="utf-8") as f:
    f.write(c4)
print("Updated payslip_take_home_pay.py")


# 5. irp5_assessments_refunds.py (subskill 51)
p5 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_income_tax/irp5_assessments_refunds.py"
with open(p5, "r", encoding="utf-8") as f:
    c5 = f.read()

c5 = c5.replace(
'''    bonus_tax = round(net_tax_with_bonus - net_tax_no_bonus, 2)
    net_bonus = round(bonus - bonus_tax, 2)

    prompt = (
        f"{name} (age 30) earns a basic salary of {_fmt_curr(monthly_basic)} per month ({_fmt_curr(annual_basic)} annually).\\n"
        f"In December, {name} receives a 13th cheque bonus of {_fmt_curr(bonus)}.\\n"
        f"SARS rules require tax on the bonus to be calculated as the difference between the annual tax on total earnings (including bonus) "
        f"and annual tax on regular earnings without bonus.\\n\\n"
        f"Calculate the net bonus {name} receives in cash after bonus tax is deducted."
    )''',
'''    bonus_tax = round(net_tax_with_bonus - net_tax_no_bonus, 2)
    net_bonus = round(bonus - bonus_tax, 2)

    d_spec_51 = {
        "kind": "bar_graph",
        "title": f"Annual Bonus Tax Breakdown ({_fmt_curr(bonus)})",
        "categories": ["Gross Bonus", "Bonus Tax (SARS)", "Net Bonus"],
        "series": [
            {"name": "Amount", "values": [bonus, bonus_tax, net_bonus]}
        ],
    }

    prompt = (
        f"Refer to the bonus taxation structure for {name} (age 30) earning {_fmt_curr(monthly_basic)} per month.\\n"
        f"In December, {name} receives a 13th cheque bonus of {_fmt_curr(bonus)}.\\n"
        f"SARS rules require tax on the bonus to be calculated as the difference between the annual tax on total earnings (including bonus) "
        f"and annual tax on regular earnings without bonus.\\n\\n"
        f"Calculate the net bonus {name} receives in cash after bonus tax is deducted."
    )'''
)

c5 = c5.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tax_gr12_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "tax_gr12_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_51,
    )'''
)

with open(p5, "w", encoding="utf-8") as f:
    f.write(c5)
print("Updated irp5_assessments_refunds.py")


# 6. fees_commissions.py (subskill 29)
p6 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_exchange_rates/fees_commissions.py"
with open(p6, "r", encoding="utf-8") as f:
    c6 = f.read()

c6 = c6.replace(
'''    net_zar = round(gross_zar - comm, 2)

    prompt = (
        f"{name} returns from the UK with £{foreign_amt} in leftover notes and sells them to {bank['name']}.\\n\\n"
        f"Bank Exchange Conditions:\\n"
        f"• Bank Buying Rate (BBR): 1 GBP = R {_fmt(bbr, 4)}\\n"
        f"• Commission: {bank['comm_rate'] * 100:.2f}% (minimum fee {_fmt_curr(bank['min_fee'])})\\n\\n"
        f"Calculate the NET amount in Rands that {name} will receive after the bank fee is deducted."
    )''',
'''    net_zar = round(gross_zar - comm, 2)

    d_spec_29 = {
        "kind": "bar_graph",
        "title": f"Forex Conversion: GBP to ZAR ({bank['name']})",
        "categories": ["Gross ZAR Value", "Bank Commission", "Net ZAR Payout"],
        "series": [
            {"name": "Amount", "values": [round(gross_zar, 2), round(comm, 2), net_zar]}
        ],
    }

    prompt = (
        f"Refer to the forex exchange rate slip for {name} selling £{foreign_amt} to {bank['name']}.\\n\\n"
        f"Bank Exchange Conditions:\\n"
        f"• Bank Buying Rate (BBR): 1 GBP = R {_fmt(bbr, 4)}\\n"
        f"• Commission: {bank['comm_rate'] * 100:.2f}% (minimum fee {_fmt_curr(bank['min_fee'])})\\n\\n"
        f"Calculate the NET amount in Rands that {name} will receive after the bank fee is deducted."
    )'''
)

c6 = c6.replace(
'''    return _build_question_payload(
        "exrate_gr12_29",
        prompt,
        correct_ans,
        opts,
        expl,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    return _build_question_payload(
        "exrate_gr12_29",
        prompt,
        correct_ans,
        opts,
        expl,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_29,
    )'''
)

with open(p6, "w", encoding="utf-8") as f:
    f.write(c6)
print("Updated fees_commissions.py")


# 7. surface_areas_painting.py (subskill 21)
p7 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/surface_areas_painting.py"
with open(p7, "r", encoding="utf-8") as f:
    c7 = f.read()

c7 = c7.replace(
'''def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Wall painting area calculation: subtracting window and door opening areas."""
    room_l, room_w, room_h = 5.0, 4.0, 2.8

    # Gross wall area = 2*(l*h) + 2*(w*h) = 2*(l+w)*h
    gross_walls = 2 * (room_l + room_w) * room_h  # 2 * 9.0 * 2.8 = 50.4 m²

    door_area = 1.0 * 2.0  # 2 m²
    window_area = 1.5 * 1.2  # 1.8 m²
    openings_area = door_area + window_area  # 3.8 m²
    net_paint_area = round(gross_walls - openings_area, 2)

    prompt = (
        f"A painter prepares to paint the 4 interior vertical walls of a bedroom measuring "
        f"{_fmt(room_l)} m long, {_fmt(room_w)} m wide, and {_fmt(room_h)} m high.\\n"
        f"The room contains:\\n"
        f"• 1 door measuring 1,0 m wide by 2,0 m high (Area = 2,0 m²)\\n"
        f"• 1 window measuring 1,5 m wide by 1,2 m high (Area = 1,8 m²)\\n\\n"
        f"Calculate the net wall surface area that will actually be painted in square metres (m²)."
    )''',
'''def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Wall painting area calculation: subtracting window and door opening areas."""
    room_l = r.choice([4.5, 5.0, 5.5])
    room_w = r.choice([3.5, 4.0, 4.5])
    room_h = 2.8

    gross_walls = 2 * (room_l + room_w) * room_h
    door_area = 1.0 * 2.0
    window_area = 1.5 * 1.2
    openings_area = door_area + window_area
    net_paint_area = round(gross_walls - openings_area, 2)

    d_spec_21 = {
        "kind": "floor_plan",
        "title": f"Bedroom Floor Plan ({_fmt(room_l)} m x {_fmt(room_w)} m)",
        "rooms": [{"name": "Bedroom", "length_m": room_l, "width_m": room_w, "height_m": room_h}],
    }

    prompt = (
        f"Refer to the bedroom floor plan measuring {_fmt(room_l)} m long, {_fmt(room_w)} m wide, and {_fmt(room_h)} m high.\\n"
        f"The room contains:\\n"
        f"• 1 door measuring 1,0 m wide by 2,0 m high (Area = 2,0 m²)\\n"
        f"• 1 window measuring 1,5 m wide by 1,2 m high (Area = 1,8 m²)\\n\\n"
        f"Calculate the net wall surface area that will actually be painted in square metres (m²)."
    )'''
)

c7 = c7.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "21_wall_painting_minus_doors_and_windows",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "21_wall_painting_minus_doors_and_windows",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_21,
    )'''
)

with open(p7, "w", encoding="utf-8") as f:
    f.write(c7)
print("Updated surface_areas_painting.py")


# 8. earthworks_materials.py (subskills 35, 40)
p8 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/earthworks_materials.py"
with open(p8, "r", encoding="utf-8") as f:
    c8 = f.read()

# Subskill 35
c8 = c8.replace(
'''    total_vol = round(vol_one * num_beds, 2)

    prompt = (
        f"A community school garden is constructing {num_beds} identical raised vegetable "
        f"planter boxes. Each box measures {_fmt(length)} m long, {_fmt(width)} m wide, "
        f"and {_fmt(depth)} m deep.\\n\\n"
        f"Using the formula: Volume of one box = Length × Width × Depth,\\n"
        f"calculate the total volume of topsoil needed to fill all {num_beds} boxes (in m³)."
    )''',
'''    total_vol = round(vol_one * num_beds, 2)

    d_spec_35 = {
        "kind": "mensuration_3d",
        "shape": "rectangular_planter",
        "title": f"Planter Box ({_fmt(length)} m x {_fmt(width)} m x {_fmt(depth)} m)",
        "dimensions": {"length": length, "width": width, "depth": depth},
    }

    prompt = (
        f"Refer to the raised planter box diagram ({_fmt(length)} m long, {_fmt(width)} m wide, and {_fmt(depth)} m deep).\\n"
        f"A community school garden is constructing {num_beds} identical raised vegetable planter boxes.\\n\\n"
        f"Using the formula: Volume of one box = Length × Width × Depth,\\n"
        f"calculate the total volume of topsoil needed to fill all {num_beds} boxes (in m³)."
    )'''
)

c8 = c8.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "35_raised_vegetable_planter_topsoil_volume",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "35_raised_vegetable_planter_topsoil_volume",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_35,
    )'''
)

# Subskill 40
c8 = c8.replace(
'''    evap_litres = int(evap_vol_m3 * 1000)

    prompt = (
        f"An open irrigation dam on a citrus farm in Limpopo has a rectangular surface area "
        f"measuring {_fmt(length)} m long by {_fmt(width)} m wide.\\n"
        f"During January, the monthly net evaporation loss is recorded as {evap_mm} mm.\\n\\n"
        f"1. Calculate the surface area of the dam in square metres (m²).\\n"
        f"2. Calculate the volume of water lost to evaporation in cubic metres (m³).\\n"
        f"3. State the volume lost in Litres (L)."
    )''',
'''    evap_litres = int(evap_vol_m3 * 1000)

    d_spec_40 = {
        "kind": "mensuration_2d",
        "shape": "rectangular_dam",
        "title": f"Irrigation Dam ({_fmt(length)} m x {_fmt(width)} m)",
        "dimensions": {"length": length, "width": width},
    }

    prompt = (
        f"Refer to the open irrigation dam diagram on a Limpopo citrus farm ({_fmt(length)} m long by {_fmt(width)} m wide).\\n"
        f"During January, the monthly net evaporation loss is recorded as {evap_mm} mm.\\n\\n"
        f"1. Calculate the surface area of the dam in square metres (m²).\\n"
        f"2. Calculate the volume of water lost to evaporation in cubic metres (m³).\\n"
        f"3. State the volume lost in Litres (L)."
    )'''
)

c8 = c8.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "40_open_farm_dam_evaporation_loss",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "40_open_farm_dam_evaporation_loss",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_40,
    )'''
)

with open(p8, "w", encoding="utf-8") as f:
    f.write(c8)
print("Updated earthworks_materials.py")


# 9. packaging_stacking.py (subskill 46)
p9 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/packaging_stacking.py"
with open(p9, "r", encoding="utf-8") as f:
    c9 = f.read()

c9 = c9.replace(
'''    total_pallets = standard_floor_fit * fit_height  # 16 pallets

    prompt = (
        f"A logistics company exports fruit on standard wooden pallets measuring "
        f"1 200 mm long by 1 000 mm wide, stacked with cartons to a total height of 1 100 mm.\\n"
        f"A standard 6-metre (20-foot) shipping container has internal dimensions of:\\n"
        f"• Length = 5 898 mm\\n"
        f"• Width = 2 352 mm\\n"
        f"• Height = 2 390 mm\\n\\n"
        f"1. Pallets are loaded with the 1 200 mm length along the length of the container and "
        f"the 1 000 mm width side-by-side across the width.\\n"
        f"   Calculate how many pallets fit on the container floor.\\n"
        f"2. Pallets can be stacked 2 tiers high (height limit allows 2 tiers: 2 × 1 100 mm = 2 200 mm < 2 390 mm).\\n"
        f"   Calculate the MAXIMUM total number of pallets that can be loaded into the container."
    )''',
'''    total_pallets = standard_floor_fit * fit_height  # 16 pallets

    d_spec_46 = {
        "kind": "packaging_packing",
        "title": "Shipping Container Pallet Arrangement (6 m Container)",
        "container": {"length": cont_l_mm, "width": cont_w_mm, "height": cont_h_mm},
        "item": {"length": pallet_l_mm, "width": pallet_w_mm, "height": pallet_h_mm},
    }

    prompt = (
        f"Refer to the shipping container packing diagram for loading standard pallets ({pallet_l_mm} mm × {pallet_w_mm} mm) into a 6-metre container ({cont_l_mm} mm × {cont_w_mm} mm × {cont_h_mm} mm).\\n"
        f"Pallets are loaded lengthwise in two rows.\\n\\n"
        f"Calculate the total number of pallets that can be loaded in the container when stacked two tiers high."
    )'''
)

c9 = c9.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "46_standard_pallets_in_shipping_container",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "46_standard_pallets_in_shipping_container",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_46,
    )'''
)

with open(p9, "w", encoding="utf-8") as f:
    f.write(c9)
print("Updated packaging_stacking.py")


# 10. costing_projects.py (subskill 49)
p10 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measurement_lengths_perimeter_area_volume/costing_projects.py"
with open(p10, "r", encoding="utf-8") as f:
    c10 = f.read()

c10 = c10.replace(
'''    # Skirting boards perimeter = 2(length + width) - 0.8 m door opening
    skirting_m = round(2 * (length + width) - 0.8, 1)

    prompt = (
        f"A living room has dimensions: Length = {_fmt(length)} m, Width = {_fmt(width)} m, Height = {_fmt(height)} m.\\n"
        f"The room has one door (2,0 m × 0,8 m) and one window (1,5 m × 1,2 m).\\n\\n"
        f"1. Ceiling area = Length × Width.\\n"
        f"2. Net wall painting area = Gross wall area − Door and window area.\\n"
        f"3. Skirting boards perimeter = Room perimeter − Door opening (0,8 m).\\n\\n"
        f"Calculate the net wall painting area (in m²) and the skirting board length required (in m)."
    )''',
'''    # Skirting boards perimeter = 2(length + width) - 0.8 m door opening
    skirting_m = round(2 * (length + width) - 0.8, 1)

    d_spec_49 = {
        "kind": "floor_plan",
        "title": f"Living Room Floor Plan ({_fmt(length)} m x {_fmt(width)} m)",
        "rooms": [{"name": "Living Room", "length_m": length, "width_m": width, "height_m": height}],
    }

    prompt = (
        f"Refer to the living room floor plan measuring Length = {_fmt(length)} m, Width = {_fmt(width)} m, Height = {_fmt(height)} m.\\n"
        f"The room has one door (2,0 m × 0,8 m) and one window (1,5 m × 1,2 m).\\n\\n"
        f"1. Ceiling area = Length × Width.\\n"
        f"2. Net wall painting area = Gross wall area − Door and window area.\\n"
        f"3. Skirting boards perimeter = Room perimeter − Door opening (0,8 m).\\n\\n"
        f"Calculate the net wall painting area (in m²) and the skirting board length required (in m)."
    )'''
)

c10 = c10.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "49_room_decorating_ceiling_walls_and_skirting",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "49_room_decorating_ceiling_walls_and_skirting",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_49,
    )'''
)

with open(p10, "w", encoding="utf-8") as f:
    f.write(c10)
print("Updated costing_projects.py")


# 11. child_growth_bmi_percentiles.py (subskills 09, 10, 13)
p11 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/child_growth_bmi_percentiles.py"
with open(p11, "r", encoding="utf-8") as f:
    c11 = f.read()

# Subskill 09
c11 = c11.replace(
'''    w, h, b, perc = cases[age]

    table_data = {''',
'''    w, h, b, perc = cases[age]

    d_spec_09 = {
        "kind": "line_graph",
        "title": f"Girls BMI-for-Age Growth Curves ({name}, Age {age})",
        "x_label": "Age (years)",
        "y_label": "BMI (kg/m²)",
        "series": [
            {"name": "50th Percentile", "points": [[9, 16.0], [10, 16.6], [12, 18.0], [14, 19.5]]},
            {"name": f"{name}'s BMI", "points": [[age, b]]},
        ],
    }

    table_data = {'''
)

c11 = c11.replace(
'''    return _build_question_payload(
        "09_girls_bmi_for_age_percentile_reading",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
    )''',
'''    return _build_question_payload(
        "09_girls_bmi_for_age_percentile_reading",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
        diagram_spec=d_spec_09,
    )'''
)

# Subskill 10
c11 = c11.replace(
'''def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Calculating child BMI and reading BMI-for-age percentile for boys."""
    name = r.choice(["Sipho", "Kagiso", "Lethabo", "Bandile"])
    age = r.choice([10, 12, 15, 17])''',
'''def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Calculating child BMI and reading BMI-for-age percentile for boys."""
    name = r.choice(["Sipho", "Kagiso", "Lethabo", "Bandile"])
    age = r.choice([10, 12, 15, 17])'''
)

c11 = c11.replace(
'''    w, h, b, perc = cases[age]

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "50th Percentile (Median)", "85th Percentile", "95th Percentile"],''',
'''    w, h, b, perc = cases[age]

    d_spec_10 = {
        "kind": "line_graph",
        "title": f"Boys BMI-for-Age Growth Curves ({name}, Age {age})",
        "x_label": "Age (years)",
        "y_label": "BMI (kg/m²)",
        "series": [
            {"name": "50th Percentile", "points": [[10, 16.4], [12, 17.8], [15, 20.2], [17, 21.8]]},
            {"name": f"{name}'s BMI", "points": [[age, b]]},
        ],
    }

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "50th Percentile (Median)", "85th Percentile", "95th Percentile"],'''
)

c11 = c11.replace(
'''    return _build_question_payload(
        "10_boys_bmi_for_age_percentile_reading",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
    )''',
'''    return _build_question_payload(
        "10_boys_bmi_for_age_percentile_reading",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
        diagram_spec=d_spec_10,
    )'''
)

# Subskill 13
c11 = c11.replace(
'''def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Identifying 'at risk of overweight' category (85th to < 95th percentile)."""
    age_years = r.choice([8, 11, 13])
    bmi_calc = 19.4''',
'''def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Identifying 'at risk of overweight' category (85th to < 95th percentile)."""
    age_years = r.choice([8, 11, 13])
    bmi_calc = r.choice([19.2, 19.4, 19.8])
    d_spec_13 = {
        "kind": "line_graph",
        "title": f"Child BMI-for-Age Risk Curves (Age {age_years})",
        "x_label": "Age (years)",
        "y_label": "BMI (kg/m²)",
        "series": [
            {"name": "85th Percentile (Overweight Threshold)", "points": [[age_years, 18.0]]},
            {"name": "Child BMI", "points": [[age_years, bmi_calc]]},
            {"name": "95th Percentile (Obese Threshold)", "points": [[age_years, 21.5]]},
        ],
    }'''
)

c11 = c11.replace(
'''    return _build_question_payload(
        "13_child_at_risk_overweight_85th_to_95th",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    return _build_question_payload(
        "13_child_at_risk_overweight_85th_to_95th",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_13,
    )'''
)

with open(p11, "w", encoding="utf-8") as f:
    f.write(c11)
print("Updated child_growth_bmi_percentiles.py")


# 12. height_weight_percentiles.py (subskill 17)
p12 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_measuring_weight_bmi_medicine_dosages/height_weight_percentiles.py"
with open(p12, "r", encoding="utf-8") as f:
    c12 = f.read()

c12 = c12.replace(
'''    height_cm, perc = cases[age]

    table_data = {''',
'''    height_cm, perc = cases[age]

    d_spec_17 = {
        "kind": "line_graph",
        "title": f"Boys Stature-for-Age Growth Curves (Age {age})",
        "x_label": "Age (years)",
        "y_label": "Height (cm)",
        "series": [
            {"name": "50th Percentile", "points": [[12, 149.0], [14, 164.0], [16, 173.0]]},
            {"name": "Recorded Height", "points": [[age, height_cm]]},
        ],
    }

    table_data = {'''
)

c12 = c12.replace(
'''    return _build_question_payload(
        "17_boys_stature_for_age_percentile",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
    )''',
'''    return _build_question_payload(
        "17_boys_stature_for_age_percentile",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
        diagram_spec=d_spec_17,
    )'''
)

with open(p12, "w", encoding="utf-8") as f:
    f.write(c12)
print("Updated height_weight_percentiles.py")


# 13. spread_rates_chemicals.py (generate_10)
p13 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_conversions_and_time/spread_rates_chemicals.py"
with open(p13, "r", encoding="utf-8") as f:
    c13 = f.read()

c13 = c13.replace(
'''    tins_5l = math.ceil(litres_exact / 5.0)

    correct_ans = f"Total Area = {total_area_to_cover} m²; Litres = {_fmt(litres_exact, 2)} ℓ; Purchase {tins_5l} × 5 ℓ tins"''',
'''    tins_5l = math.ceil(litres_exact / 5.0)

    d_spec_10 = {
        "kind": "mensuration_2d",
        "shape": "garage_floor",
        "title": f"Concrete Garage Floor ({floor_area} m²)",
        "area_m2": floor_area,
    }

    correct_ans = f"Total Area = {total_area_to_cover} m²; Litres = {_fmt(litres_exact, 2)} ℓ; Purchase {tins_5l} × 5 ℓ tins"'''
)

c13 = c13.replace(
'''    prompt = (
        f"A concrete garage floor with an area of {floor_area} m² is to be painted with 2 coats of heavy-duty epoxy floor paint.\\n"
        f"• Spread rate of floor paint: 1 ℓ covers 11 m²\\n"
        f"• Floor paint is sold only in 5-litre tins\\n\\n"
        f"1. Calculate the total area to be covered for {coats} coats.\\n"
        f"2. Calculate the exact number of litres required.\\n"
        f"3. Determine the minimum number of 5-litre tins to purchase."
    )''',
'''    prompt = (
        f"Refer to the garage floor diagram with an area of {floor_area} m² to be painted with 2 coats of heavy-duty epoxy floor paint.\\n"
        f"• Spread rate of floor paint: 1 ℓ covers 11 m²\\n"
        f"• Floor paint is sold only in 5-litre tins\\n\\n"
        f"1. Calculate the total area to be covered for {coats} coats.\\n"
        f"2. Calculate the exact number of litres required.\\n"
        f"3. Determine the minimum number of 5-litre tins to purchase."
    )'''
)

c13 = c13.replace(
'''        subskill_id="10_multi_coat_paint_tin_packaging",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total area = floor area × 2 coats. Litres = total area ÷ 11. Round up to full 5-litre tins.",
        tier_2=f"Total area = {total_area_to_cover} m². Litres = {_fmt(litres_exact, 2)} ℓ. Tins = {litres_exact:.2f} ÷ 5 = {litres_exact/5:.2f} -> round up.",
        tier_3=f"Purchase {tins_5l} × 5-litre tins.",
        r=r,
    )''',
'''        subskill_id="10_multi_coat_paint_tin_packaging",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total area = floor area × 2 coats. Litres = total area ÷ 11. Round up to full 5-litre tins.",
        tier_2=f"Total area = {total_area_to_cover} m². Litres = {_fmt(litres_exact, 2)} ℓ. Tins = {litres_exact:.2f} ÷ 5 = {litres_exact/5:.2f} -> round up.",
        tier_3=f"Purchase {tins_5l} × 5-litre tins.",
        r=r,
        diagram_spec=d_spec_10,
    )'''
)

with open(p13, "w", encoding="utf-8") as f:
    f.write(c13)
print("Updated spread_rates_chemicals.py")


# 14. travel_timetables_transit.py (generate_36)
p14 = "caps-ai-backend/app/utils/mathematical_literacy/gr12_conversions_and_time/travel_timetables_transit.py"
with open(p14, "r", encoding="utf-8") as f:
    c14 = f.read()

c14 = c14.replace(
'''def generate_36_feasibility_of_day_trip_excursion(r: random.Random) -> Dict[str, Any]:
    """Assess whether a day trip excursion allows the minimum required leisure time before the return departure."""
    dep_time = "14:45"
    duration_mins = 55
    arr_time = "15:40"
    latest_return = "19:15"
    required_hours = 4''',
'''def generate_36_feasibility_of_day_trip_excursion(r: random.Random) -> Dict[str, Any]:
    """Assess whether a day trip excursion allows the minimum required leisure time before the return departure."""
    dep_time = "14:45"
    duration_mins = r.choice([45, 50, 55, 60])
    arr_h = 14 + (45 + duration_mins) // 60
    arr_m = (45 + duration_mins) % 60
    arr_time = f"{arr_h:02d}:{arr_m:02d}"
    latest_return = "19:15"
    required_hours = 4

    d_spec_36 = {
        "kind": "strip_map",
        "title": f"Day Trip Transit Timetable (Departure: {dep_time})",
        "towns": [
            {"name": f"Departure ({dep_time})", "km": 0},
            {"name": f"Arrival ({arr_time})", "km": 40},
            {"name": f"Return ({latest_return})", "km": 80},
        ],
    }'''
)

c14 = c14.replace(
'''    # Time available: 19:15 - 15:40 = 3 hours 35 minutes (215 minutes)
    mins_available = (19 * 60 + 15) - (15 * 60 + 40)''',
'''    mins_available = (19 * 60 + 15) - (arr_h * 60 + arr_m)'''
)

c14 = c14.replace(
'''    prompt = (
        f"A tour group departs on a regional flight at {dep_time}. The flight duration is {duration_mins} minutes.\\n"
        f"The itinerary states that they arrive at their destination at {arr_time}.\\n"
        f"The last return transport leaves at {latest_return}.\\n"
        f"The tour group requires a minimum of {required_hours} hours of leisure sightseeing time at the destination.\\n\\n"
        f"Determine the time available between arrival and the return departure, and state whether the excursion is feasible."
    )''',
'''    prompt = (
        f"Refer to the transit timetable scheme for a day-trip excursion departing at {dep_time}.\\n"
        f"The flight duration is {duration_mins} minutes, arriving at {arr_time}.\\n"
        f"The last return transport leaves at {latest_return}.\\n"
        f"The tour group requires a minimum of {required_hours} hours of leisure sightseeing time at the destination.\\n\\n"
        f"Determine the time available between arrival and the return departure, and state whether the excursion is feasible."
    )'''
)

c14 = c14.replace(
'''        subskill_id="36_feasibility_of_day_trip_excursion",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Calculate arrival: 14:45 + 55 min = 15:40. Find time between 15:40 and 19:15.",
        tier_2="Available time: 19:15 - 15:40 = 3 hours 35 minutes.",
        tier_3=f"Since 3 h 35 min is less than 4 hours, the trip is NOT feasible.",
        r=r,
    )''',
'''        subskill_id="36_feasibility_of_day_trip_excursion",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Calculate arrival: {dep_time} + {duration_mins} min = {arr_time}. Find time between {arr_time} and {latest_return}.",
        tier_2=f"Available time: {avail_h} hours {avail_m} minutes.",
        tier_3=f"Comparison: {correct_ans}.",
        r=r,
        diagram_spec=d_spec_36,
    )'''
)

with open(p14, "w", encoding="utf-8") as f:
    f.write(c14)
print("Updated travel_timetables_transit.py")
