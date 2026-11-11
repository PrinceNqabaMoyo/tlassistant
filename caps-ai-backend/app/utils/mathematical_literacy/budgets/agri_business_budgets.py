"""Cluster 6: Small Business, Agricultural & Poultry Enterprise Budgets (7 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_agri_tomato_farming_enterprise(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    seedlings = round(r.choice([650.00, 750.00, 850.00]), 2)  # seedling trays
    fertilizer = round(r.choice([1200.00, 1400.00, 1600.00]), 2)  # 2:3:4 bags
    irrigation_fittings = round(r.choice([450.00, 550.00]), 2)
    pest_control = round(r.choice([380.00, 450.00]), 2)
    crates_produced = r.choice([80, 100, 120, 140])
    price_per_crate = round(r.choice([65.00, 75.00, 80.00, 90.00]), 2)

    total_costs = round(seedlings + fertilizer + irrigation_fittings + pest_control, 2)
    total_revenue = round(crates_produced * price_per_crate, 2)
    net_profit = round(total_revenue - total_costs, 2)
    ans_str = _fmt_curr(net_profit)

    prompt = (
        f"{name} operates an intensive 0,25-hectare open-field tomato enterprise in Limpopo:\n\n"
        f"**Input Costs:**\n"
        f"• Certified tomato seedling trays: **{_fmt_curr(seedlings)}**\n"
        f"• Basal and top-dressing fertilizer (2:3:4 & LAN): **{_fmt_curr(fertilizer)}**\n"
        f"• Drip irrigation fittings and emitters: **{_fmt_curr(irrigation_fittings)}**\n"
        f"• Biological pest management sprays: **{_fmt_curr(pest_control)}**\n\n"
        f"**Harvest & Sales:**\n"
        f"{name} harvests and sells **{crates_produced} wooden crates of fresh tomatoes** at the local farm gate market for **{_fmt_curr(price_per_crate)} per crate**.\n\n"
        f"Calculate {name}'s **Net Enterprise Profit (Surplus)** from the tomato crop."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In agricultural enterprise budgeting, Net Profit is calculated as:\n"
        f"  $$\\text{{Total Input Costs}} = \\text{{Seedlings}} + \\text{{Fertilizer}} + \\text{{Irrigation}} + \\text{{Pest Spray}}$$\n"
        f"  $$\\text{{Gross Sales Revenue}} = \\text{{Crates Harvested}} \\times \\text{{Price per Crate}}$$\n"
        f"  $$\\text{{Net Profit}} = \\text{{Gross Sales Revenue}} - \\text{{Total Input Costs}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Costs}} = \\text{{{_fmt_curr(seedlings)}}} + \\text{{{_fmt_curr(fertilizer)}}} + \\text{{{_fmt_curr(irrigation_fittings)}}} + \\text{{{_fmt_curr(pest_control)}}} = \\text{{{_fmt_curr(total_costs)}}}$.\n"
        f"• $\\text{{Gross Revenue}} = {crates_produced} \\times \\text{{{_fmt_curr(price_per_crate)}}} = \\text{{{_fmt_curr(total_revenue)}}}$.\n"
        f"• $\\text{{Net Profit}} = \\text{{{_fmt_curr(total_revenue)}}} - \\text{{{_fmt_curr(total_costs)}}} = \\text{{{_fmt_curr(net_profit)}}}$.\n"
        f"✓ **[1 Mark: Method – summing all 4 input costs, finding sales revenue, and subtracting total costs]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct net profit in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_tomato_farming_enterprise",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total revenue - total input costs", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Sum costs: {_fmt_curr(seedlings)} + {_fmt_curr(fertilizer)} + {_fmt_curr(irrigation_fittings)} + {_fmt_curr(pest_control)} = {_fmt_curr(total_costs)}.",
            "tier_2": f"Revenue = {crates_produced} crates × {_fmt_curr(price_per_crate)} = {_fmt_curr(total_revenue)}. Subtract costs from revenue.",
            "tier_3": f"Net profit = {_fmt_curr(net_profit)}."
        },
        r=r
    )

def _gen_budg_agri_poultry_broiler_batch_budget(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    batch_size = r.choice([100, 150, 200])
    chick_cost_each = round(r.choice([12.50, 13.00, 13.50, 14.00]), 2)
    chick_total = round(batch_size * chick_cost_each, 2)
    feed_total = round(batch_size * r.choice([42.00, 45.00, 48.00]), 2)  # starter/grower/finisher combined
    vaccines = round(r.choice([250.00, 300.00]), 2)
    bedding_shavings = round(r.choice([180.00, 220.00]), 2)
    heating_gas = round(r.choice([280.00, 320.00]), 2)

    total_batch_cost = round(chick_total + feed_total + vaccines + bedding_shavings + heating_gas, 2)
    cost_per_bird = round(total_batch_cost / batch_size, 2)
    ans_str = _fmt_curr(cost_per_bird)

    prompt = (
        f"{name} prepares a 6-week production budget for raising a batch of **{batch_size} day-old broiler chicks**:\n\n"
        f"• Day-old chicks: **{_fmt_curr(chick_cost_each)} per chick**\n"
        f"• Poultry feed (broiler starter, grower, and finisher pellets): **{_fmt_curr(feed_total)}** total\n"
        f"• Newcastle and Gumboro vaccines: **{_fmt_curr(vaccines)}**\n"
        f"• Pine wood shavings bedding: **{_fmt_curr(bedding_shavings)}**\n"
        f"• Brooding heat lamps & LPG gas: **{_fmt_curr(heating_gas)}**\n\n"
        f"1. Calculate the total cost to produce the entire batch.\n"
        f"2. Calculate the **production cost per bird**, rounded to 2 decimal places."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Production cost per bird is calculated by dividing total batch costs by the number of birds raised:\n"
        f"  $$\\text{{Total Batch Cost}} = (\\text{{Chicks}} \\times \\text{{Price per chick}}) + \\text{{Feed}} + \\text{{Vaccines}} + \\text{{Bedding}} + \\text{{Heating}}$$\n"
        f"  $$\\text{{Unit Cost per Bird}} = \\frac{{\\text{{Total Batch Cost}}}}{{\\text{{Batch Size}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Chicks Cost}} = {batch_size} \\times \\text{{{_fmt_curr(chick_cost_each)}}} = \\text{{{_fmt_curr(chick_total)}}}$.\n"
        f"• $\\text{{Total Batch Cost}} = \\text{{{_fmt_curr(chick_total)}}} + \\text{{{_fmt_curr(feed_total)}}} + \\text{{{_fmt_curr(vaccines)}}} + \\text{{{_fmt_curr(bedding_shavings)}}} + \\text{{{_fmt_curr(heating_gas)}}} = \\text{{{_fmt_curr(total_batch_cost)}}}$.\n"
        f"• $\\text{{Cost per Bird}} = \\frac{{\\text{{{_fmt_curr(total_batch_cost)}}}}}{{{batch_size}}} = \\text{{{_fmt_curr(cost_per_bird)}}}$.\n"
        f"✓ **[1 Mark: Method – summing all batch input expenses and dividing by batch size {batch_size}]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct production cost per bird in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_poultry_broiler_batch_budget",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total batch expenses ÷ batch size", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Chicks cost = {batch_size} × {_fmt_curr(chick_cost_each)} = {_fmt_curr(chick_total)}.",
            "tier_2": f"Sum all costs ({_fmt_curr(total_batch_cost)}) and divide by {batch_size} chicks.",
            "tier_3": f"Cost per bird = {_fmt_curr(cost_per_bird)}."
        },
        r=r
    )

def _gen_budg_agri_layer_chicken_egg_cash_flow(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    hens = r.choice([50, 60, 80, 100])
    # Average lay rate ~80% => hens * 0.8 * 30 days = total eggs
    lay_rate = 0.80
    monthly_eggs = int(hens * lay_rate * 30)
    trays_30_eggs = monthly_eggs // 30
    price_per_tray = round(r.choice([60.00, 65.00, 70.00, 75.00]), 2)
    egg_revenue = round(trays_30_eggs * price_per_tray, 2)

    layer_feed = round(hens * 32.00, 2)  # Feed per hen per month
    cartons_cost = round(trays_30_eggs * 3.50, 2)
    total_layer_exp = round(layer_feed + cartons_cost, 2)
    monthly_cash_flow = round(egg_revenue - total_layer_exp, 2)
    ans_str = _fmt_curr(monthly_cash_flow)

    prompt = (
        f"{name} keeps a flock of **{hens} point-of-lay hens** producing fresh eggs for sale in the community:\n\n"
        f"• The flock produces an average of **{trays_30_eggs} trays of eggs per month** (30 eggs per tray).\n"
        f"• {name} sells each 30-egg tray at **{_fmt_curr(price_per_tray)}**.\n"
        f"• Monthly layer mash feed cost: **{_fmt_curr(layer_feed)}**\n"
        f"• Egg packaging cartons & labels cost: **{_fmt_curr(cartons_cost)}**\n\n"
        f"Calculate {name}'s **Monthly Net Cash Flow (Surplus)** from the layer egg enterprise."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Monthly surplus is sales revenue minus operational feed and packaging costs:\n"
        f"  $$\\text{{Egg Sales Revenue}} = \\text{{Trays Sold}} \\times \\text{{Price per Tray}}$$\n"
        f"  $$\\text{{Total Operational Costs}} = \\text{{Layer Feed}} + \\text{{Cartons}}$$\n"
        f"  $$\\text{{Monthly Net Cash Flow}} = \\text{{Egg Sales Revenue}} - \\text{{Total Operational Costs}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Egg Revenue}} = {trays_30_eggs} \\times \\text{{{_fmt_curr(price_per_tray)}}} = \\text{{{_fmt_curr(egg_revenue)}}}$.\n"
        f"• $\\text{{Total Costs}} = \\text{{{_fmt_curr(layer_feed)}}} + \\text{{{_fmt_curr(cartons_cost)}}} = \\text{{{_fmt_curr(total_layer_exp)}}}$.\n"
        f"• $\\text{{Net Cash Flow}} = \\text{{{_fmt_curr(egg_revenue)}}} - \\text{{{_fmt_curr(total_layer_exp)}}} = \\text{{{_fmt_curr(monthly_cash_flow)}}}$.\n"
        f"✓ **[1 Mark: Method – calculating revenue, summing costs, and finding net cash flow]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct monthly cash flow in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_layer_chicken_egg_cash_flow",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (trays × price) - (feed + packaging)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Revenue = {trays_30_eggs} trays × {_fmt_curr(price_per_tray)} = {_fmt_curr(egg_revenue)}.",
            "tier_2": f"Expenses = {_fmt_curr(layer_feed)} + {_fmt_curr(cartons_cost)} = {_fmt_curr(total_layer_exp)}. Subtract expenses from revenue.",
            "tier_3": f"Monthly cash flow = {_fmt_curr(monthly_cash_flow)}."
        },
        r=r
    )

def _gen_budg_agri_feed_cost_per_bird_margin(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    feed_consumed_kg = round(r.choice([3.6, 3.8, 4.0, 4.2]), 1)
    feed_cost_per_50kg_bag = round(r.choice([380.00, 400.00, 420.00, 450.00]), 2)
    cost_per_kg = feed_cost_per_50kg_bag / 50.0
    feed_cost_per_bird = round(feed_consumed_kg * cost_per_kg, 2)
    selling_price_live_bird = round(r.choice([85.00, 90.00, 95.00, 100.00]), 2)
    margin_over_feed = round(selling_price_live_bird - feed_cost_per_bird, 2)
    ans_str = _fmt_curr(margin_over_feed)

    prompt = (
        f"{name} produces free-range broiler chickens. Over the 6-week rearing cycle:\n\n"
        f"• Each bird consumes an average of **{_fmt(feed_consumed_kg, 1)} kg of feed**.\n"
        f"• A 50 kg bag of complete broiler feed costs **{_fmt_curr(feed_cost_per_50kg_bag)}**.\n"
        f"• The finished live chicken is sold directly to consumers for **{_fmt_curr(selling_price_live_bird)}**.\n\n"
        f"1. Calculate the cost of feed consumed per bird.\n"
        f"2. Calculate the **Margin Over Feed Cost (MOFC)** per bird (Selling price minus feed cost per bird)."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Feed cost per kg = $\\frac{{\\text{{Cost per 50 kg bag}}}}{{50}}$.\n"
        f"• Total feed cost per bird = $\\text{{Feed consumed (kg)}} \\times \\text{{Cost per kg}}$.\n"
        f"• Margin Over Feed Cost = $\\text{{Selling Price}} - \\text{{Feed Cost per Bird}}$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Cost per kg}} = \\frac{{\\text{{{_fmt_curr(feed_cost_per_50kg_bag)}}}}}{{50}} = \\text{{{_fmt_curr(cost_per_kg)}}}\\text{{/kg}}$.\n"
        f"• $\\text{{Feed Cost per Bird}} = {_fmt(feed_consumed_kg, 1)} \\times \\text{{{_fmt_curr(cost_per_kg)}}} = \\text{{{_fmt_curr(feed_cost_per_bird)}}}$.\n"
        f"• $\\text{{Margin Over Feed}} = \\text{{{_fmt_curr(selling_price_live_bird)}}} - \\text{{{_fmt_curr(feed_cost_per_bird)}}} = \\text{{{_fmt_curr(margin_over_feed)}}}$.\n"
        f"✓ **[1 Mark: Method – finding feed cost per kg, calculating feed cost per bird, and subtracting from selling price]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct margin over feed cost in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_feed_cost_per_bird_margin",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – selling price - (feed_kg × bag_price ÷ 50)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Feed cost per kg = {_fmt_curr(feed_cost_per_50kg_bag)} ÷ 50 = {_fmt_curr(cost_per_kg)}/kg.",
            "tier_2": f"Feed per bird = {feed_consumed_kg} kg × {_fmt_curr(cost_per_kg)} = {_fmt_curr(feed_cost_per_bird)}. Subtract from {_fmt_curr(selling_price_live_bird)}.",
            "tier_3": f"Margin over feed = {_fmt_curr(margin_over_feed)}."
        },
        r=r
    )

def _gen_budg_agri_spaza_produce_stall_break_even(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    wholesale_stock_daily = round(r.choice([450.00, 520.00, 600.00]), 2)  # potatoes, onions, tomatoes
    stall_permit_daily = round(r.choice([25.00, 30.00, 35.00]), 2)
    bakkie_transport_daily = round(r.choice([75.00, 90.00, 100.00]), 2)
    plastic_carry_bags = round(r.choice([20.00, 25.00]), 2)

    total_daily_cost = round(wholesale_stock_daily + stall_permit_daily + bakkie_transport_daily + plastic_carry_bags, 2)
    ans_str = _fmt_curr(total_daily_cost)

    prompt = (
        f"{name} operates a fresh produce stall at a busy commuter taxi rank:\n\n"
        f"**Daily Operational Expenses:**\n"
        f"• Wholesale fresh vegetable purchases at the market: **{_fmt_curr(wholesale_stock_daily)}**\n"
        f"• Municipal informal trading permit fee: **{_fmt_curr(stall_permit_daily)}**\n"
        f"• Bakkie delivery transport from fresh produce market: **{_fmt_curr(bakkie_transport_daily)}**\n"
        f"• Plastic packaging & grocery carrier bags: **{_fmt_curr(plastic_carry_bags)}**\n\n"
        f"Calculate the **minimum daily sales revenue** {name} must generate to **break even** (cover all daily operational expenses)."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In micro-enterprise financial budgeting, the daily break-even sales revenue equals the sum of all daily input and operational costs:\n"
        f"  $$\\text{{Break-even Daily Revenue}} = \\sum \\text{{All Daily Expenses}}$$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"• $\\text{{Total Daily Cost}} = \\text{{{_fmt_curr(wholesale_stock_daily)}}} + \\text{{{_fmt_curr(stall_permit_daily)}}} + \\text{{{_fmt_curr(bakkie_transport_daily)}}} + \\text{{{_fmt_curr(plastic_carry_bags)}}} = \\text{{{_fmt_curr(total_daily_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – correctly summing all 4 daily operating expenses]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct daily break-even revenue in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_spaza_produce_stall_break_even",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sum of all 4 daily stall expenses", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "To break even, total revenue must equal total expenses.",
            "tier_2": f"Add {_fmt_curr(wholesale_stock_daily)} + {_fmt_curr(stall_permit_daily)} + {_fmt_curr(bakkie_transport_daily)} + {_fmt_curr(plastic_carry_bags)}.",
            "tier_3": f"Break-even daily revenue = {_fmt_curr(total_daily_cost)}."
        },
        r=r
    )

def _gen_budg_agri_livestock_goat_herd_budget(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    goats_count = r.choice([20, 25, 30])
    annual_dip_vaccines_per_goat = round(r.choice([45.00, 55.00]), 2)
    annual_vet_total = round(goats_count * annual_dip_vaccines_per_goat, 2)
    winter_feed_blocks = round(r.choice([1500.00, 1800.00, 2200.00]), 2)
    kraal_maintenance = round(r.choice([800.00, 1000.00]), 2)
    total_costs = round(annual_vet_total + winter_feed_blocks + kraal_maintenance, 2)

    goats_sold = r.choice([6, 8, 10])
    price_per_goat = round(r.choice([1400.00, 1600.00, 1800.00]), 2)
    total_sales = round(goats_sold * price_per_goat, 2)
    annual_profit = round(total_sales - total_costs, 2)
    ans_str = _fmt_curr(annual_profit)

    prompt = (
        f"{name} manages a smallholder herd of **{goats_count} indigenous Boer goats** in the Eastern Cape:\n\n"
        f"**Annual Operational Expenses:**\n"
        f"• Herd veterinary deworming and tick dip: **{_fmt_curr(annual_dip_vaccines_per_goat)} per goat per year**\n"
        f"• Winter supplementary lucerne and mineral feed lick blocks: **{_fmt_curr(winter_feed_blocks)}**\n"
        f"• Night kraal fence security maintenance: **{_fmt_curr(kraal_maintenance)}**\n\n"
        f"**Annual Sales Inflows:**\n"
        f"During the December festive season, {name} sells **{goats_sold} live adult goats** at **{_fmt_curr(price_per_goat)} each**.\n\n"
        f"Calculate {name}'s **Annual Net Enterprise Return (Profit)** from the goat herd."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Net Enterprise Return is calculated as:\n"
        f"  $$\\text{{Total Revenue}} = \\text{{Goats Sold}} \\times \\text{{Selling Price per Goat}}$$\n"
        f"  $$\\text{{Total Costs}} = (\\text{{Herd Size}} \\times \\text{{Dip per goat}}) + \\text{{Winter Feed}} + \\text{{Kraal Maintenance}}$$\n"
        f"  $$\\text{{Net Return}} = \\text{{Total Revenue}} - \\text{{Total Costs}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Vet Costs}} = {goats_count} \\times \\text{{{_fmt_curr(annual_dip_vaccines_per_goat)}}} = \\text{{{_fmt_curr(annual_vet_total)}}}$.\n"
        f"• $\\text{{Total Costs}} = \\text{{{_fmt_curr(annual_vet_total)}}} + \\text{{{_fmt_curr(winter_feed_blocks)}}} + \\text{{{_fmt_curr(kraal_maintenance)}}} = \\text{{{_fmt_curr(total_costs)}}}$.\n"
        f"• $\\text{{Total Revenue}} = {goats_sold} \\times \\text{{{_fmt_curr(price_per_goat)}}} = \\text{{{_fmt_curr(total_sales)}}}$.\n"
        f"• $\\text{{Net Profit}} = \\text{{{_fmt_curr(total_sales)}}} - \\text{{{_fmt_curr(total_costs)}}} = \\text{{{_fmt_curr(annual_profit)}}}$.\n"
        f"✓ **[1 Mark: Method – finding total revenue from animal sales and subtracting all herd expenses]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct annual net profit in Rands]**"
    )
    return _make_q(
        subskill="budg_agri_livestock_goat_herd_budget",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total goat sales - total herd costs", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Vet costs = {goats_count} × {_fmt_curr(annual_dip_vaccines_per_goat)} = {_fmt_curr(annual_vet_total)}. Total costs = {_fmt_curr(total_costs)}.",
            "tier_2": f"Sales revenue = {goats_sold} × {_fmt_curr(price_per_goat)} = {_fmt_curr(total_sales)}. Subtract total costs.",
            "tier_3": f"Net return = {_fmt_curr(annual_profit)}."
        },
        r=r
    )

def _gen_budg_agri_crop_irrigation_cost_comparison(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    # Option 1: Buying water from private water tanker: R 650 per delivery load * 12 deliveries a year
    tanker_cost_per_load = round(r.choice([550.00, 600.00, 650.00, 700.00]), 2)
    loads_per_year = 12
    tanker_annual_total = round(tanker_cost_per_load * loads_per_year, 2)

    # Option 2: Purchasing 5000L JoJo tank + guttering + gravity drip irrigation kit (once-off)
    tank_cost = round(r.choice([4200.00, 4500.00, 4800.00]), 2)
    guttering_fittings = round(r.choice([950.00, 1100.00]), 2)
    gravity_drip_kit = round(r.choice([650.00, 750.00]), 2)
    jojo_system_total = round(tank_cost + guttering_fittings + gravity_drip_kit, 2)

    diff = round(abs(tanker_annual_total - jojo_system_total), 2)
    cheaper_option = "JoJo rainwater system" if jojo_system_total < tanker_annual_total else "Water tanker deliveries"
    ans_str = f"{cheaper_option} by {_fmt_curr(diff)}"

    prompt = (
        f"{name} needs an irrigation water supply for a vegetable garden over a **12-month period** and compares two options:\n\n"
        f"• **Option A (Water Tanker Deliveries)**: Purchasing water from a private tanker company at **{_fmt_curr(tanker_cost_per_load)} per delivery**, requiring **{loads_per_year} deliveries per year**.\n"
        f"• **Option B (Rainwater Harvesting System)**: Installing a 5 000-litre JoJo tank (**{_fmt_curr(tank_cost)}**), roof guttering and leaf trap fittings (**{_fmt_curr(guttering_fittings)}**), and a gravity drip irrigation kit (**{_fmt_curr(gravity_drip_kit)}**).\n\n"
        f"1. Calculate the total cost of each option for the first year.\n"
        f"2. Determine which option is **cheaper over the first year** and by **how much**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Calculate the 12-month expenditure for both alternatives:\n"
        f"  $$\\text{{Option A Total}} = \\text{{Cost per Tanker Load}} \\times \\text{{Number of Deliveries}}$$\n"
        f"  $$\\text{{Option B Total}} = \\text{{JoJo Tank}} + \\text{{Guttering}} + \\text{{Drip Kit}}$$\n"
        f"• Find the difference: $|\\text{{Option A}} - \\text{{Option B}}|$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Option A}} = \\text{{{_fmt_curr(tanker_cost_per_load)}}} \\times {loads_per_year} = \\text{{{_fmt_curr(tanker_annual_total)}}}$.\n"
        f"• $\\text{{Option B}} = \\text{{{_fmt_curr(tank_cost)}}} + \\text{{{_fmt_curr(guttering_fittings)}}} + \\text{{{_fmt_curr(gravity_drip_kit)}}} = \\text{{{_fmt_curr(jojo_system_total)}}}$.\n"
        f"• $\\text{{Difference}} = |\\text{{{_fmt_curr(tanker_annual_total)}}} - \\text{{{_fmt_curr(jojo_system_total)}}}| = \\text{{{_fmt_curr(diff)}}}$.\n"
        f"• Therefore, **{cheaper_option}** is cheaper by **{_fmt_curr(diff)}**.\n"
        f"✓ **[1 Mark: Method – calculating annual tanker cost, summing rainwater system costs, and finding difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct option selection and cost savings in Rands]**"
    )
    custom_opts = [
        f"JoJo rainwater system by {_fmt_curr(diff)}",
        f"Water tanker deliveries by {_fmt_curr(diff)}",
        f"JoJo rainwater system by {_fmt_curr(round(diff * 1.1, 2))}",
        f"Water tanker deliveries by {_fmt_curr(round(diff * 1.1, 2))}"
    ]
    return _make_q(
        subskill="budg_agri_crop_irrigation_cost_comparison",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – |tanker annual - jojo system total|", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Option A = {_fmt_curr(tanker_cost_per_load)} × {loads_per_year} = {_fmt_curr(tanker_annual_total)}. Option B = {_fmt_curr(tank_cost)} + {_fmt_curr(guttering_fittings)} + {_fmt_curr(gravity_drip_kit)} = {_fmt_curr(jojo_system_total)}.",
            "tier_2": f"Subtract the smaller total from the larger total.",
            "tier_3": f"Result: {ans_str}."
        },
        options=custom_opts,
        r=r
    )
