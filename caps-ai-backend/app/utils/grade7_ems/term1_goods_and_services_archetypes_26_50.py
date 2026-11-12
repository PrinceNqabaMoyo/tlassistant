"""
Grade 7 EMS — Term 1: Goods and Services — Semantic Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/03. Goods and Service.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term1_goods_and_services_archetypes_01_25 import (
    _escape,
    _fmt_rand,
    _mcq,
    _pick_person,
    _pick_place,
    _pick_two_people,
    _q,
    _svg_bars,
    _svg_exchange,
    _svg_wrap,
    _table_q,
)


def _svg_recycling_loop(school: str, kg: int, rand_earned: int) -> Dict[str, Any]:
    steps = [
        ("1. Collect", f"{kg} kg school waste"),
        ("2. Sort", "Paper, glass, cans"),
        ("3. Reprocess", "Pulp, cullet, ingots"),
        ("4. Remake", f"Earn {_fmt_rand(rand_earned)}"),
    ]
    parts: List[str] = []
    for idx, (head, sub) in enumerate(steps):
        x = 24 + idx * 154
        parts.append(f'<rect x="{x}" y="54" width="136" height="78" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>')
        parts.append(f'<text x="{x + 68}" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#166534">{_escape(head)}</text>')
        parts.append(f'<text x="{x + 68}" y="108" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#334155">{_escape(sub)}</text>')
        if idx < 3:
            parts.append(f'<line x1="{x + 136}" y1="93" x2="{x + 154}" y2="93" stroke="#0f766e" stroke-width="2"/>')
    return _svg_wrap(640, 152, f"{school} Four-Step Recycling Loop", "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 26 – 50
# ---------------------------------------------------------------------------

def _b26(rng: random.Random) -> Dict[str, Any]:
    hh = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    wages = rng.choice([4500, 5200, 6400])
    spend = rng.choice([3600, 4100, 5100])
    diag = _svg_exchange(
        f"Household Dual Role — {town}",
        f"{hh}'s Household",
        f"Earns {_fmt_rand(wages)} wages",
        "Local Businesses",
        f"Receives {_fmt_rand(spend)} sales",
        "Supplies labour & skills",
        f"Consumer spending {_fmt_rand(spend)}",
    )
    prompt = (
        f"Refer to the circular flow diagram for {town} showing {hh}'s household earning {_fmt_rand(wages)} wages and "
        f"spending {_fmt_rand(spend)} at local businesses. Explain why households are described as BOTH **producers** and **consumers**."
    )
    sample = (
        f"Households act as **producers** by supplying labour, skills, and factors of production to businesses in return for "
        f"{_fmt_rand(wages)} in wages (plus home production); they act as **consumers** by spending {_fmt_rand(spend)} on goods "
        f"and services to satisfy household needs and wants."
    )
    worked = (
        f"1. **Producer side ({_fmt_rand(wages)}) [1.5]:** Households supply worker hours, talent, and capital to firms to produce output.\n"
        f"2. **Consumer side ({_fmt_rand(spend)}) [1.5]:** Households spend earned income buying final goods and services from businesses."
    )
    return _q(
        rng,
        "26_households_dual_role_circular_flow",
        prompt,
        sample,
        worked,
        "The circular economy relies on households functioning simultaneously as factor suppliers/producers and final buyers/consumers.",
        {
            "tier_1": "Look at both the top arrow and bottom arrow between households and businesses.",
            "tier_2": f"Relate earning {_fmt_rand(wages)} to supplying labour (producer), and spending {_fmt_rand(spend)} to buying goods (consumer).",
            "tier_3": "Explain both dual roles clearly using the diagram values.",
        },
        ["separates_households_into_consumers_only"],
        [
            {"criterion": f"Explains household producer/factor-supplier role ({_fmt_rand(wages)})", "marks": 1},
            {"criterion": f"Explains household consumer/spending role ({_fmt_rand(spend)})", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b27(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    task = rng.choice(["irrigates a school vegetable garden using drip hoses instead of midday sprinklers", "heats exact kettle water for two cups instead of boiling a full kettle"])
    prompt = (
        f"In an EMS resource project, {learner} {task}, achieving the same useful outcome with minimal waste and lower cost. "
        f"Which term specifically describes achieving results with minimal wasted inputs, time, or money?"
    )
    return _mcq(
        rng,
        "27_efficient_vs_effective_use_definitions",
        prompt,
        "Efficient use of resources",
        ["Inefficient overconsumption", "Primary extractive waste", "Unplanned luxury hoarding"],
        "Efficiency means obtaining maximum useful output with minimum wasted resources, whereas effectiveness means successfully achieving the intended goal.",
        {
            "tier_1": "Recall the contrast between achieving the goal (effective) and doing it with minimal waste (efficient).",
            "tier_2": "Focus on cutting water or electricity waste while getting the exact same job done.",
            "tier_3": "Select 'Efficient use of resources'.",
        },
        ["confuses_efficiency_with_wasteful_speed"],
    )


def _b28(rng: random.Random) -> Dict[str, Any]:
    province = rng.choice(["Western Cape", "Eastern Cape", "Northern Cape", "Limpopo", "Free State"])
    rain_mm = rng.choice([450, 464, 490])
    prompt = (
        f"South Africa receives only roughly {rain_mm} mm of average annual rainfall — nearly half the world average — "
        f"making provinces such as {province} drought-prone. Explain TWO reasons why clean water is treated as South Africa's "
        f"most critical scarce natural good."
    )
    sample = (
        f"(1) Low rainfall ({rain_mm} mm/yr) and high evaporation mean natural freshwater supply is strictly limited relative "
        f"to growing population, agriculture, and industry demand; (2) clean water has no substitute for human survival, "
        f"sanitation, farming, and industrial processing."
    )
    worked = (
        f"1. **Low natural supply vs rising demand [1.5]:** With only ~{rain_mm} mm rain/year and frequent droughts in {province}, freshwater dams face severe depletion.\n"
        f"2. **Non-substitutable essential [1.5]:** Survival, hygiene, farming, and power/manufacturing all depend irreplaceably on water."
    )
    return _q(
        rng,
        "28_water_scarcity_sa_demand_supply",
        prompt,
        sample,
        worked,
        "Water scarcity is acute across South Africa because low average rainfall meets rising urban, farming, and industrial water needs.",
        {
            "tier_1": f"Use the {rain_mm} mm rainfall hint alongside why no other resource can replace drinking water.",
            "tier_2": "Combine supply limits (low rain/drought) with rising demand across homes, farms, and factories.",
            "tier_3": "State limited rainfall/drought risk and the irreplaceable demand across survival, farming, and industry.",
        },
        ["thinks_ocean_saltwater_solves_household_scarcity_cheaply"],
        [
            {"criterion": f"Explains low rainfall ({rain_mm} mm) / drought vs growing demand", "marks": 1},
            {"criterion": "Explains essential non-substitutable uses (survival, farming, industry)", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b29(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=True)
    name = _pick_person(rng)
    prompt = (
        f"Water restrictions are declared in {town}. Recommend THREE practical, everyday water-saving habits that {name}'s "
        f"family can apply inside the home or garden."
    )
    sample = (
        "(1) Fix leaking taps, pipes, and running toilets promptly; (2) take short five-minute showers instead of deep baths "
        "and turn off the tap while brushing teeth; and (3) collect rainwater in tanks or reuse bath/laundry greywater for garden watering."
    )
    worked = (
        "1. **Repair leaks [1]:** Fix dripping taps and faulty toilet cistern valves immediately.\n"
        "2. **Daily washing habits [1]:** Short showers instead of full baths and closing taps while brushing teeth/washing dishes.\n"
        "3. **Harvest & reuse [1]:** Catch roof rainwater in tanks and irrigate plants with greywater during cool early/late hours."
    )
    return _q(
        rng,
        "29_five_water_saving_methods",
        prompt,
        sample,
        worked,
        "Practical household conservation measures dramatically extend scarce municipal water reserves.",
        {
            "tier_1": "Think of plumbing repairs, bathroom habits, and outdoor garden/rainwater collection.",
            "tier_2": "Be specific: name actual daily actions rather than writing 'save water'.",
            "tier_3": "List fixing leaks, shorter showers / tap off while brushing, and rainwater/greywater reuse.",
        },
        ["writes_vague_advice_without_concrete_actions"],
        [
            {"criterion": "Concrete action 1 (e.g. fix dripping taps / leaking toilets)", "marks": 1},
            {"criterion": "Concrete action 2 (e.g. shorter showers / close tap brushing)", "marks": 1},
            {"criterion": "Concrete action 3 (e.g. rainwater tank / greywater garden watering)", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b30(rng: random.Random) -> Dict[str, Any]:
    school = _pick_place(rng, rural=True)
    litres_per_day = rng.choice([20, 25, 30, 40])
    taps = rng.choice([4, 5, 6, 8])
    total_month = litres_per_day * taps * 30
    prompt = (
        f"At a school in {school}, {taps} leaking taps each drip away {litres_per_day} litres of clean drinking water per day. "
        f"Calculate how many litres of scarce water are wasted across a 30-day month if the taps remain unrepaired."
    )
    daily_all = litres_per_day * taps
    worked = (
        f"1. **Daily waste ({taps} taps) [1]:** {taps} x {litres_per_day} L = {daily_all} L/day.\n"
        f"2. **30-day monthly waste [1]:** {daily_all} L x 30 = **{total_month} L**."
    )
    return _q(
        rng,
        "30_dripping_tap_water_waste_calculation",
        prompt,
        f"{total_month} L",
        worked,
        "Small daily leaks multiply across taps and days into thousands of wasted litres.",
        {
            "tier_1": "Multiply the number of taps by litres wasted per tap each day.",
            "tier_2": "Multiply the combined daily waste by 30 days.",
            "tier_3": f"Compute {taps} x {litres_per_day} x 30 = {total_month} L.",
        },
        ["forgets_to_multiply_by_number_of_taps_or_days"],
        [
            {"criterion": f"Calculates daily waste across {taps} taps = {daily_all} L", "marks": 1},
            {"criterion": f"Calculates 30-day waste = {total_month} L", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b31(rng: random.Random) -> Dict[str, Any]:
    home = _pick_person(rng)
    old_cost = rng.choice([320, 400, 480])
    new_cost = rng.choice([80, 100, 120])
    monthly_save = old_cost - new_cost
    annual_save = monthly_save * 12
    diag = _svg_bars(
        f"Monthly Lighting Electricity Bill — {home}",
        [
            ("Old Incandescent Bulbs", old_cost, "#dc2626"),
            ("Efficient LED Bulbs", new_cost, "#16a34a"),
        ],
    )
    prompt = (
        f"Refer to the electricity cost diagram showing {home}'s monthly lighting cost dropping from {_fmt_rand(old_cost)} "
        f"(incandescent bulbs) to {_fmt_rand(new_cost)} (LED bulbs). Calculate how many Rands {home} saves over one full year (12 months)."
    )
    worked = (
        f"1. **Monthly Rand saving [1]:** {_fmt_rand(old_cost)} - {_fmt_rand(new_cost)} = {_fmt_rand(monthly_save)}/month.\n"
        f"2. **Annual saving (12 months) [1]:** {_fmt_rand(monthly_save)} x 12 = **{_fmt_rand(annual_save)}**."
    )
    return _q(
        rng,
        "31_electricity_efficient_appliances_saving",
        prompt,
        _fmt_rand(annual_save),
        worked,
        "Energy-efficient LED technology delivers the same brightness while cutting household bills and national grid strain.",
        {
            "tier_1": "Subtract the green LED bar from the red old-bulb bar to find one month's saving.",
            "tier_2": "Multiply the monthly Rand saving by 12 months.",
            "tier_3": f"Compute ({_fmt_rand(old_cost)} - {_fmt_rand(new_cost)}) x 12 = {_fmt_rand(annual_save)}.",
        },
        ["gives_monthly_saving_instead_of_12_month_saving"],
        [
            {"criterion": f"Calculates monthly saving = {_fmt_rand(monthly_save)}", "marks": 1},
            {"criterion": f"Calculates annual saving = {_fmt_rand(annual_save)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b32(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    action = rng.choice(["washes glass jam jars to store dried beans and spices", "carries tough woven cloth shopping bags back to the supermarket every week"])
    prompt = (
        f"Instead of throwing containers away after one trip, {learner} {action}. "
        f"Which sustainable resource practice is {learner} applying?"
    )
    return _mcq(
        rng,
        "32_reuse_definition_and_examples",
        prompt,
        "Reusing",
        ["Industrial factory smelting", "Landfill dumping", "Primary raw mining"],
        "Reusing means using an intact item multiple times for its original purpose or a creative new household use without factory melting or pulping.",
        {
            "tier_1": "Ask whether the jar or bag went to a factory shredder, or was simply cleaned and used again.",
            "tier_2": "Distinguish direct household reuse from industrial recycling.",
            "tier_3": "Select 'Reusing'.",
        },
        ["confuses_household_reuse_with_industrial_recycling"],
    )


def _b33(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    item = rng.choice(["school shoes", "study desk", "commuter bicycle"])
    new_price = rng.choice([750, 900, 1200])
    repair_cost = rng.choice([180, 240, 290])
    saving = new_price - repair_cost
    prompt = (
        f"{owner}'s {item} breaks slightly. Buying a brand-new replacement costs {_fmt_rand(new_price)}, whereas having a local "
        f"artisan repair it costs {_fmt_rand(repair_cost)}. Calculate how many Rands {owner} saves by repairing instead of replacing."
    )
    worked = (
        f"1. **Cost comparison [1]:** Replace = {_fmt_rand(new_price)}, Repair = {_fmt_rand(repair_cost)}.\n"
        f"2. **Net Rand saving [1]:** {_fmt_rand(new_price)} - {_fmt_rand(repair_cost)} = **{_fmt_rand(saving)}** (plus keeping durable materials out of landfill)."
    )
    return _q(
        rng,
        "33_repair_vs_replace_cost_calculation",
        prompt,
        _fmt_rand(saving),
        worked,
        "Repairing broken durable goods saves households scarce money, supports local repair skills, and prevents premature waste.",
        {
            "tier_1": "Subtract the repair cost from the cost of buying brand new.",
            "tier_2": f"Compute {_fmt_rand(new_price)} minus {_fmt_rand(repair_cost)}.",
            "tier_3": f"State the Rand saving: {_fmt_rand(saving)}.",
        },
        ["adds_repair_and_new_costs_together"],
        [
            {"criterion": f"Correct subtraction {_fmt_rand(new_price)} - {_fmt_rand(repair_cost)}", "marks": 1},
            {"criterion": f"Final saving = {_fmt_rand(saving)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b34(rng: random.Random) -> Dict[str, Any]:
    family = _pick_person(rng)
    item = rng.choice(["Grade 7 textbooks and school blazers", "solid wooden furniture and bicycles"])
    prompt = (
        f"Before term begins, {family}'s household buys clean second-hand {item} instead of brand-new factory stock. "
        f"Explain ONE economic benefit for the household and ONE environmental benefit of buying used goods."
    )
    sample = (
        f"Economic benefit: Buying quality second-hand {item} costs far less, freeing scarce Rands for food, electricity, or savings. "
        f"Environmental benefit: Extending product lifespan reduces demand for new raw timber/cotton/energy and keeps usable goods out of landfills."
    )
    worked = (
        f"1. **Household economic benefit [1]:** Lower purchase price preserves household budget for other primary needs.\n"
        f"2. **Environmental benefit [2]:** Slows resource depletion, saves factory manufacturing energy, and cuts municipal landfill waste."
    )
    return _q(
        rng,
        "34_buying_secondhand_used_goods_benefits",
        prompt,
        sample,
        worked,
        "Second-hand markets make durable goods affordable while lowering raw-material extraction and landfill pressure.",
        {
            "tier_1": "Think of one money advantage for the family and one nature advantage for the planet.",
            "tier_2": "Consider budget savings alongside fewer new trees/minerals used and less rubbish.",
            "tier_3": "State lower cost freeing family Rands, and fewer raw materials / less landfill waste.",
        },
        ["sees_secondhand_goods_as_having_only_cost_benefit"],
        [
            {"criterion": "Explains lower household expenditure / freed Rand savings", "marks": 1},
            {"criterion": "Explains environmental saving (less raw extraction / energy / landfill waste)", "marks": 2},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b35(rng: random.Random) -> Dict[str, Any]:
    school = _pick_place(rng, rural=False)
    prompt = (
        f"Classify each eco-club action at a school in {school} as **Reduce**, **Reuse**, **Repair**, or **Recycle**."
    )
    row_specs = [
        {"cells": ["Printing worksheets double-sided to cut paper demand by half", None], "expected": ["Reduce"], "cell_hints": ["Uses fewer total resources from the start."]},
        {"cells": ["Using empty plastic 2L ice-cream tubs to store classroom chalk", None], "expected": ["Reuse"], "cell_hints": ["Uses an intact container again for a new household/school purpose."]},
        {"cells": ["Re-gluing torn textbook spines and fixing broken chair hinges", None], "expected": ["Repair"], "cell_hints": ["Mends damaged goods so they stay functional."]},
        {"cells": ["Sending sorted crushed aluminium cans to a foundry to melt into new cans", None], "expected": ["Recycle"], "cell_hints": ["Reprocesses waste material industrially into new raw stock."]},
    ]
    return _table_q(
        rng,
        "35_reduce_reuse_recycle_table",
        prompt,
        ["Eco-Club Action", "Conservation Method (Reduce / Reuse / Repair / Recycle)"],
        row_specs,
        "Each conservation 'R' plays a distinct role: Reduce cuts initial consumption, Reuse extends intact use, Repair mends breaks, and Recycle reprocesses scrap.",
        {
            "tier_1": "Distinguish buying/using less (Reduce), keeping intact items (Reuse), fixing breaks (Repair), and melting/pulping scrap (Recycle).",
            "tier_2": "Double-sided printing->Reduce, tub storage->Reuse, fixing chairs->Repair, melting cans->Recycle.",
            "tier_3": "Enter Reduce, Reuse, Repair, or Recycle.",
        },
        ["uses_recycle_as_catch_all_for_reuse_and_reduce"],
    )


def _b36(rng: random.Random) -> Dict[str, Any]:
    plant = rng.choice(["glass bottle works", "corrugated cardboard mill", "aluminium beverage foundry"])
    prompt = (
        f"A {plant} buys sorted municipal waste, shreds or melts it cleanly, and turns it into brand-new packaging stock. "
        f"Which process defines turning recovered waste materials back into raw manufacturing inputs?"
    )
    return _mcq(
        rng,
        "36_recycling_definition_and_materials",
        prompt,
        "Recycling",
        ["Open landfill dumping", "Incineration burning", "Primary mineral mining"],
        "Recycling collects, sorts, and industrially reprocesses used materials (paper, glass, metal, plastics) into raw material for new goods.",
        {
            "tier_1": "Notice waste is shredded or melted inside a mill/foundry to form brand-new products.",
            "tier_2": "Contrast reprocessing scrap material against burning or burying rubbish.",
            "tier_3": "Choose 'Recycling'.",
        },
        ["confuses_incineration_with_recycling"],
    )


def _b37(rng: random.Random) -> Dict[str, Any]:
    school = _pick_place(rng, rural=False)
    kg = rng.choice([240, 350, 480])
    earned = kg * 2
    diag = _svg_recycling_loop(school, kg, earned)
    prompt = (
        f"Refer to the four-step recycling loop diagram for {school} collecting {kg} kg of recyclables worth {_fmt_rand(earned)}. "
        f"Briefly explain what happens in each of the four stages from **Collection** to **Remake / Buying Recycled Goods**."
    )
    sample = (
        f"(1) Collect: households and schools separate {kg} kg of clean paper, glass, plastics, and cans; "
        f"(2) Sort: collectors/depots separate items by material type and remove contamination; "
        f"(3) Reprocess: factories pulp paper or melt glass/aluminium into clean feedstock; "
        f"(4) Remake: manufacturers make new products sold to consumers, closing the loop and generating {_fmt_rand(earned)} value."
    )
    worked = (
        f"1. **Step 1 Collect [1]:** Gather {kg} kg of dry recyclables in separate bins.\n"
        f"2. **Step 2 Sort [1]:** Separate paper, glass, cans, and plastics so batches stay pure.\n"
        f"3. **Step 3 Reprocess [1]:** Mills/smelters convert scrap into clean pulp, cullet, or ingots.\n"
        f"4. **Step 4 Remake [1]:** New recycled goods are manufactured and purchased, sustaining demand ({_fmt_rand(earned)} earned)."
    )
    return _q(
        rng,
        "37_recycling_four_step_process",
        prompt,
        sample,
        worked,
        "Recycling only succeeds as a continuous loop when clean collection, careful sorting, industrial reprocessing, and consumer demand for recycled goods connect.",
        {
            "tier_1": "Follow the four numbered green boxes from left to right in the diagram.",
            "tier_2": f"Describe what happens to the {kg} kg material at Step 1, Step 2, Step 3, and Step 4.",
            "tier_3": "Cover Collection, Sorting by material, Industrial Reprocessing, and Manufacturing/Buying recycled products.",
        },
        ["thinks_recycling_stops_at_putting_bottles_in_a_bin"],
        [
            {"criterion": f"Step 1: Collection ({kg} kg separated waste)", "marks": 1},
            {"criterion": "Step 2: Sorting and cleaning by material type", "marks": 1},
            {"criterion": "Step 3: Industrial reprocessing into pulp/cullet/ingots", "marks": 1},
            {"criterion": "Step 4: Remaking and buying recycled products", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=4,
        diagram_spec=diag,
    )


def _b38(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    collector = _pick_person(rng)
    prompt = (
        f"A new buy-back recycling depot opens in {town}, where {collector} and other community members sell sorted cans, "
        f"cardboard, and plastic bottles. Explain THREE **economic benefits** that recycling brings to a town like {town}."
    )
    sample = (
        "(1) Creates jobs and household income for collectors, sorters, drivers, and buy-back operators; "
        "(2) saves municipalities money by extending landfill lifespans and cutting waste-disposal expenses; and "
        "(3) supplies local paper, glass, and metal factories with cheaper domestic raw feedstock."
    )
    worked = (
        f"1. **Income & jobs [1]:** Collectors like {collector}, depot sorters, and truckers earn direct wages.\n"
        f"2. **Lower municipal landfill costs [1]:** Diverting waste delays building expensive new landfill sites in {town}.\n"
        f"3. **Cheaper industrial inputs [1]:** Mills save raw-material and import costs by reprocessing local scrap."
    )
    return _q(
        rng,
        "38_recycling_economic_benefits_jobs",
        prompt,
        sample,
        worked,
        "Beyond protecting nature, recycling generates green employment, municipal tax savings, and competitive manufacturing feedstock.",
        {
            "tier_1": "Focus strictly on money, jobs, costs, and businesses — not just trees and polar bears.",
            "tier_2": "Think of three groups winning economically: collectors, the municipality, and factories.",
            "tier_3": "State income/jobs for collectors, lower municipal landfill expenses, and cheaper raw inputs for manufacturers.",
        },
        ["lists_only_environmental_points_when_asked_for_economic_benefits"],
        [
            {"criterion": "Job creation / income earned by collectors and sorters", "marks": 1},
            {"criterion": "Municipal savings / extended landfill capacity", "marks": 1},
            {"criterion": "Cheaper raw material inputs for local industry", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b39(rng: random.Random) -> Dict[str, Any]:
    club = _pick_person(rng)
    mat = rng.choice(["paper and cardboard", "aluminium cans and glass bottles"])
    prompt = (
        f"{club} prepares a poster on why recycling {mat} protects nature. Explain THREE **environmental benefits** of recycling."
    )
    sample = (
        "(1) Conserves finite natural resources such as timber forests, fresh water, silica sand, and bauxite ore; "
        "(2) uses much less electricity and fossil-fuel energy than processing virgin ores (cutting greenhouse gas emissions); and "
        "(3) reduces air, soil, and water pollution as well as toxic litter entering rivers and landfills."
    )
    worked = (
        "1. **Resource conservation [1]:** Saves trees, minerals, oil, and water from rapid depletion.\n"
        "2. **Energy & emissions savings [1]:** Reprocessing scrap requires less energy, lowering carbon/greenhouse gases.\n"
        "3. **Reduced pollution & landfill pressure [1]:** Keeps plastic, glass, and leachate out of rivers, oceans, and soil."
    )
    return _q(
        rng,
        "39_recycling_environmental_benefits",
        prompt,
        sample,
        worked,
        "Recycling preserves ecosystems, lowers industrial energy use, and prevents land and waterway contamination.",
        {
            "tier_1": "Focus on ecosystems, raw natural resources, energy emissions, and pollution.",
            "tier_2": f"Think about what nature avoids when factories reuse {mat} instead of extracting brand-new raw inputs.",
            "tier_3": "State three clear environmental wins: conserving natural resources, saving energy/lowering greenhouse gases, and cutting pollution.",
        },
        ["gives_only_one_broad_benefit_saves_the_earth"],
        [
            {"criterion": "Conserves natural resources (trees/minerals/water)", "marks": 1},
            {"criterion": "Saves energy and cuts greenhouse gas emissions", "marks": 1},
            {"criterion": "Reduces litter, pollution, and landfill strain", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b40(rng: random.Random) -> Dict[str, Any]:
    school = _pick_place(rng, rural=False)
    paper_kg = rng.choice([250, 300, 400])
    cans_kg = rng.choice([80, 100, 120])
    paper_rate = 2
    cans_rate = 12
    total_rand = paper_kg * paper_rate + cans_kg * cans_rate
    prompt = (
        f"A school recycling drive in {school} gathers {paper_kg} kg of clean cardboard (paid at {_fmt_rand(paper_rate)}/kg) "
        f"and {cans_kg} kg of aluminium cans (paid at {_fmt_rand(cans_rate)}/kg). Calculate the total Rand fundraising income earned."
    )
    worked = (
        f"1. **Cardboard income [1]:** {paper_kg} kg x {_fmt_rand(paper_rate)} = {_fmt_rand(paper_kg * paper_rate)}.\n"
        f"2. **Aluminium income [1]:** {cans_kg} kg x {_fmt_rand(cans_rate)} = {_fmt_rand(cans_kg * cans_rate)}.\n"
        f"3. **Total earned [1]:** {_fmt_rand(paper_kg * paper_rate)} + {_fmt_rand(cans_kg * cans_rate)} = **{_fmt_rand(total_rand)}**."
    )
    return _q(
        rng,
        "40_greenhouse_gas_landfill_saving",
        prompt,
        _fmt_rand(total_rand),
        worked,
        "Higher-value scrap metals like aluminium yield strong recycling income per kilogram alongside high-volume cardboard.",
        {
            "tier_1": "Calculate cardboard earnings and aluminium earnings separately first.",
            "tier_2": f"Multiply {paper_kg} x {paper_rate} and {cans_kg} x {cans_rate}, then add.",
            "tier_3": f"Sum {_fmt_rand(paper_kg * paper_rate)} + {_fmt_rand(cans_kg * cans_rate)} = {_fmt_rand(total_rand)}.",
        },
        ["adds_kilograms_instead_of_multiplying_by_rates"],
        [
            {"criterion": f"Cardboard revenue = {_fmt_rand(paper_kg * paper_rate)}", "marks": 1},
            {"criterion": f"Aluminium revenue = {_fmt_rand(cans_kg * cans_rate)}", "marks": 1},
            {"criterion": f"Combined total = {_fmt_rand(total_rand)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b41(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Match each recyclable waste stream to the primary natural resource or energy input it directly helps preserve."
    )
    row_specs = [
        {"cells": ["Paper and corrugated cardboard", None], "expected": ["Timber trees and water"], "cell_hints": ["Wood pulp comes from plantation forests and uses heavy water."]},
        {"cells": ["Clear and brown glass bottles", None], "expected": ["Silica sand and limestone"], "cell_hints": ["Quarried minerals melted at high furnace heat to make glass."]},
        {"cells": ["Aluminium beverage cans", None], "expected": ["Bauxite ore and electricity"], "cell_hints": ["Smelting fresh aluminium from bauxite ore consumes huge electric power."]},
        {"cells": ["PET plastic water bottles", None], "expected": ["Crude oil (petroleum)"], "cell_hints": ["Fossil-fuel hydrocarbon raw material used to make plastics."]},
    ]
    return _table_q(
        rng,
        "41_paper_vs_glass_vs_metal_recycling_table",
        prompt,
        ["Recyclable Material", "Preserved Natural Input"],
        row_specs,
        "Recycling directly replaces virgin natural resources: trees for paper, silica for glass, bauxite/power for aluminium, and crude oil for plastic.",
        {
            "tier_1": "Trace each material back to the natural earth resource used to make it originally.",
            "tier_2": "Paper->trees/water, Glass->silica sand, Aluminium->bauxite/electricity, PET Plastic->crude oil.",
            "tier_3": "Fill in the matching resource labels accurately.",
        },
        ["thinks_plastic_comes_from_trees_or_sand"],
    )


def _b42(rng: random.Random) -> Dict[str, Any]:
    reclaimer = _pick_person(rng)
    city = _pick_place(rng, rural=False)
    tonnes_day = rng.randint(12, 24)
    prompt = (
        f"Across {city}, informal waste reclaimers such as {reclaimer} pull trolleys recovering huge shares of recyclable "
        f"cardboard and plastic (part of roughly {tonnes_day} tonnes diverted in one district weekly) before bins reach landfills. "
        f"State ONE important economic contribution waste reclaimers make and ONE practical challenge they face."
    )
    sample = (
        f"Contribution: Reclaimers earn self-reliant household income while recovering clean packaging feedstock for local "
        f"recycling factories and saving municipal landfill space. Challenge: They face unstable scrap prices, heavy physical traffic "
        f"risks, or lack of protective gear and safe sorting hubs."
    )
    worked = (
        f"1. **Contribution [1.5]:** Diverts ~{tonnes_day} tonnes from landfills, sustains local mills' raw supply, and generates self-employment income.\n"
        f"2. **Challenge [1.5]:** Volatile buy-back prices, road safety hazards, lack of PPE/protective clothing, or sorting space shortages in {city}."
    )
    return _q(
        rng,
        "42_informal_waste_pickers_value_chain",
        prompt,
        sample,
        worked,
        "South Africa's informal waste reclaimers form the backbone of urban packaging recovery despite tough working conditions.",
        {
            "tier_1": "Think about both the value reclaimers create for cities/factories and the hardships on streets/dumps.",
            "tier_2": f"Consider income, factory feedstock, and {tonnes_day} tonnes saved from landfill vs price swings and safety risks.",
            "tier_3": "State one clear contribution and one concrete working challenge.",
        },
        ["overlooks_informal_reclaimers_in_sa_recycling"],
        [
            {"criterion": f"Valid contribution ({tonnes_day} tonnes recovered / income / factory supply)", "marks": 1},
            {"criterion": "Valid practical challenge (safety, unstable prices, lack of PPE/sorting space)", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b43(rng: random.Random) -> Dict[str, Any]:
    shopper = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Shopping in {town}, {shopper} wants laundry detergent and milk with the lowest long-term packaging waste. "
        f"Which purchasing choice supports sustainable resource use best?"
    )
    return _mcq(
        rng,
        "43_sustainable_packaging_consumer_choice",
        prompt,
        "Refillable concentrated detergent pouches and returnable glass milk bottles",
        [
            "Individually wrapped single-use foam trays inside extra plastic bags",
            "Buying twenty tiny disposable sachets every single week",
            "Non-recyclable multi-layer metallic blister packs for loose apples",
        ],
        "Concentrated refills and returnable glass containers dramatically cut packaging volume per litre while keeping containers circulating cleanly.",
        {
            "tier_1": "Compare how much rubbish lands in the bin after the product finishes.",
            "tier_2": "Single-use sachets and foam trays create maximum waste; returnables and concentrates minimise it.",
            "tier_3": "Choose 'Refillable concentrated detergent pouches and returnable glass milk bottles'.",
        },
        ["picks_individually_wrapped_single_use_sachets"],
    )


def _b44(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    service = rng.choice(["bicycle repairs", "school uniform alterations", "laptop virus cleaning"])
    fee_a = rng.choice([120, 150])
    fee_b = rng.choice([140, 170])
    prompt = (
        f"{p1} needs {service}. Provider A charges {_fmt_rand(fee_a)} with zero warranty and frequent delays, while "
        f"Provider B charges {_fmt_rand(fee_b)} with reliable on-time completion and a 30-day workmanship guarantee. "
        f"Explain TWO criteria consumers use to evaluate **service quality**, and explain why assessing a service before "
        f"buying is harder than inspecting a physical good."
    )
    sample = (
        f"Criteria: (1) reliability/timeliness and (2) workmanship guarantee/after-service trust ({_fmt_rand(fee_b)}). "
        f"Evaluating services beforehand is harder because services are intangible actions — unlike picking up a loaf of bread "
        f"or ruler, you cannot touch or test the completed repair until after it is performed."
    )
    worked = (
        f"1. **Service quality criteria [2]:** Timeliness/reliability, skill quality, transparency, and post-service warranty (making Provider B at {_fmt_rand(fee_b)} stronger value than {_fmt_rand(fee_a)}).\n"
        f"2. **Intangibility problem [1]:** Services cannot be inspected on a shelf prior to delivery."
    )
    return _q(
        rng,
        "44_service_quality_comparison_scenario",
        prompt,
        sample,
        worked,
        "Because services are intangible and variable across providers, reputation, timelines, and guarantees matter hugely alongside price.",
        {
            "tier_1": "Compare more than just the cheapest Rand fee: look at time reliability and warranty.",
            "tier_2": "Ask why you can squeeze bread or inspect a jacket before buying, yet cannot touch a haircut or repair beforehand.",
            "tier_3": "Give two evaluation criteria (timeliness, workmanship guarantee) and link difficulty to service intangibility.",
        },
        ["always_chooses_lowest_price_ignoring_service_reliability"],
        [
            {"criterion": "Criterion 1 & 2: Reliability/timeliness and workmanship guarantee", "marks": 2},
            {"criterion": "Explains intangibility makes pre-purchase testing impossible", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b45(rng: random.Random) -> Dict[str, Any]:
    name1, name2 = _pick_two_people(rng)
    asset = rng.choice(["electric sewing machine", "gas baking oven", "colour laser printer"])
    price = rng.choice([4500, 6200, 8900])
    prompt = (
        f"{name1} buys a {_fmt_rand(price)} {asset} strictly for personal family hobbies at home, while {name2} buys the exact "
        f"same {_fmt_rand(price)} {asset} to manufacture items for paying customers. Explain how the economic classification "
        f"of the same {asset} changes depending on its user."
    )
    sample = (
        f"In {name1}'s home, the {asset} is a **durable consumer good** because it directly satisfies private household wants "
        f"without generating commercial sales. In {name2}'s workshop, the same {_fmt_rand(price)} {asset} is a **capital good** "
        f"because it is used by a business to produce other goods/services for income."
    )
    worked = (
        f"1. **{name1}'s home use [1.5]:** **Durable consumer good** — used privately by the household over several years.\n"
        f"2. **{name2}'s commercial use [1.5]:** **Capital good** — man-made business asset generating goods/services for market sale."
    )
    return _q(
        rng,
        "45_capital_vs_consumer_good_context",
        prompt,
        sample,
        worked,
        "Whether a durable machine counts as a consumer good or a capital good depends on whether it serves final household enjoyment or commercial production.",
        {
            "tier_1": "Focus on WHO buys the item and WHAT they use it for.",
            "tier_2": f"Separate {name1}'s private hobby use from {name2}'s business production for paying clients.",
            "tier_3": f"Classify {name1}'s as a durable consumer good and {name2}'s as a capital good.",
        },
        ["thinks_classification_is_fixed_by_object_only_never_purpose"],
        [
            {"criterion": f"{name1}'s machine = durable consumer good (private household use)", "marks": 1},
            {"criterion": f"{name2}'s machine = capital good (used to produce goods for sale)", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b46(rng: random.Random) -> Dict[str, Any]:
    raw_val = rng.choice([1200, 1500, 1800])
    proc_val = rng.choice([4200, 5000, 5800])
    gain = proc_val - raw_val
    diag = _svg_bars(
        "Export Revenue per Tonne: Raw Timber vs Finished Furniture",
        [
            ("Raw Pine Logs (Primary)", raw_val, "#ca8a04"),
            ("Finished Desks (Secondary)", proc_val, "#16a34a"),
        ],
    )
    prompt = (
        f"Refer to the export value diagram comparing raw primary timber logs ({_fmt_rand(raw_val)}/tonne) against locally "
        f"manufactured finished wooden desks ({_fmt_rand(proc_val)}/tonne). Calculate the extra Rand revenue earned per tonne "
        f"by processing the timber locally instead of exporting it raw."
    )
    worked = (
        f"1. **Export comparison [1]:** Finished desks = {_fmt_rand(proc_val)}, Raw logs = {_fmt_rand(raw_val)}.\n"
        f"2. **Extra local value gain [1]:** {_fmt_rand(proc_val)} - {_fmt_rand(raw_val)} = **{_fmt_rand(gain)}/tonne** "
        f"(creating local manufacturing jobs and higher export income)."
    )
    return _q(
        rng,
        "46_export_raw_vs_processed_goods_value",
        prompt,
        _fmt_rand(gain),
        worked,
        "Beneficiating raw primary commodities into finished secondary goods captures higher export revenue and skilled domestic jobs.",
        {
            "tier_1": "Subtract the raw primary log revenue bar from the finished secondary desk bar.",
            "tier_2": f"Compute {_fmt_rand(proc_val)} minus {_fmt_rand(raw_val)}.",
            "tier_3": f"State the extra Rand gain: {_fmt_rand(gain)}.",
        },
        ["divides_instead_of_subtracting_to_find_extra_rands"],
        [
            {"criterion": f"Reads values {_fmt_rand(proc_val)} and {_fmt_rand(raw_val)}", "marks": 1},
            {"criterion": f"Calculates extra Rand revenue = {_fmt_rand(gain)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b47(rng: random.Random) -> Dict[str, Any]:
    seller = _pick_person(rng)
    pies_qty = rng.randint(15, 25)
    pie_p = rng.choice([20, 22])
    print_qty = rng.randint(12, 20)
    print_p = rng.choice([5, 8])
    goods_rev = pies_qty * pie_p
    serv_rev = print_qty * print_p
    total_rev = goods_rev + serv_rev
    prompt = (
        f"{seller} manages a school enterprise selling both physical **goods** ({pies_qty} beef pies at {_fmt_rand(pie_p)} each) "
        f"and **services** ({print_qty} document laminations at {_fmt_rand(print_p)} each) in one break. "
        f"Calculate {seller}'s combined Rand revenue from goods and services."
    )
    worked = (
        f"1. **Goods revenue (pies) [1]:** {pies_qty} x {_fmt_rand(pie_p)} = {_fmt_rand(goods_rev)}.\n"
        f"2. **Services revenue (laminations) [1]:** {print_qty} x {_fmt_rand(print_p)} = {_fmt_rand(serv_rev)}.\n"
        f"3. **Combined total [1]:** {_fmt_rand(goods_rev)} + {_fmt_rand(serv_rev)} = **{_fmt_rand(total_rev)}**."
    )
    return _q(
        rng,
        "47_tuckshop_goods_and_services_inventory",
        prompt,
        _fmt_rand(total_rev),
        worked,
        "Many everyday South African enterprises earn combined income from tangible goods and complementary services.",
        {
            "tier_1": "Compute pie sales and lamination sales separately first.",
            "tier_2": f"Multiply {pies_qty} x {pie_p} and {print_qty} x {print_p}, then sum both totals.",
            "tier_3": f"Compute {_fmt_rand(goods_rev)} + {_fmt_rand(serv_rev)} = {_fmt_rand(total_rev)}.",
        },
        ["forgets_to_include_service_revenue_in_total"],
        [
            {"criterion": f"Goods revenue = {_fmt_rand(goods_rev)}", "marks": 1},
            {"criterion": f"Services revenue = {_fmt_rand(serv_rev)}", "marks": 1},
            {"criterion": f"Combined revenue = {_fmt_rand(total_rev)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b48(rng: random.Random) -> Dict[str, Any]:
    youth = _pick_person(rng)
    town = _pick_place(rng, rural=True)
    waste_stream = rng.choice(["discarded plastic bottles and scrap timber pallets", "wasted rainwater and torn denim clothes"])
    prompt = (
        f"Seeing high youth unemployment and abundant {waste_stream} around {town}, {youth} wants to start a green "
        f"micro-enterprise. Propose ONE viable recycled/upcycled good or resource-saving service {youth} could sell, "
        f"and explain ONE environmental benefit plus ONE economic benefit of this idea."
    )
    sample = (
        f"Idea: {youth} could upcycle {waste_stream} into durable school book-racks, garden planters, or reusable market totes. "
        f"Environmental benefit: Keeps non-biodegradable scrap out of local rivers and dumps while conserving virgin wood/cotton. "
        f"Economic benefit: Low raw-material input cost lets {youth} earn profit and create local part-time income."
    )
    worked = (
        f"1. **Green product/service idea [1]:** Specific useful item or repair/collection service built from {waste_stream}.\n"
        f"2. **Environmental win [1]:** Reduces local waste/pollution and lowers demand for virgin resources.\n"
        f"3. **Economic win [1]:** Minimal material cost generates entrepreneurial income/jobs in {town}."
    )
    return _q(
        rng,
        "48_green_jobs_entrepreneur_opportunity",
        prompt,
        sample,
        worked,
        "Green entrepreneurship converts waste streams and conservation challenges into viable micro-business opportunities.",
        {
            "tier_1": f"Think of a useful item households in {town} would pay for made from {waste_stream}.",
            "tier_2": "Verify you cover all three parts: the concrete business idea, an environmental gain, and a financial/job gain.",
            "tier_3": "Propose a clear upcycled product/service plus one landfill/resource benefit and one income/cost benefit.",
        },
        ["proposes_unmarketable_craft_with_no_paying_demand"],
        [
            {"criterion": f"Viable product/service idea using {waste_stream}", "marks": 1},
            {"criterion": "Clear environmental conservation/landfill benefit", "marks": 1},
            {"criterion": "Clear economic income/job benefit", "marks": 1},
        ],
        cognitive_level="Problem Solving",
        marks=3,
    )


def _b49(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    prompt = (
        f"Audit each enterprise in {town} by filling in its **Sector** (`Primary`, `Secondary`, or `Tertiary`) in the table."
    )
    row_specs = [
        {"cells": ["Citrus farm picking and packing fresh oranges straight from trees", None], "expected": ["Primary"], "cell_hints": ["Harvests agricultural fruit directly from the land."]},
        {"cells": ["Bottling factory turning oranges into pasteurised juice cartons", None], "expected": ["Secondary"], "cell_hints": ["Processes raw fruit into packaged manufactured beverage."]},
        {"cells": ["Refrigerated courier fleet delivering juice boxes to supermarkets", None], "expected": ["Tertiary"], "cell_hints": ["Commercial freight transport and wholesale distribution service."]},
        {"cells": ["Municipal water testing laboratory advising restaurants", None], "expected": ["Tertiary"], "cell_hints": ["Specialist testing and advisory service."]},
    ]
    return _table_q(
        rng,
        "49_goods_services_sectors_audit_table",
        prompt,
        ["Enterprise Description", "Sector (Primary / Secondary / Tertiary)"],
        row_specs,
        "Auditing economic activity across sectors shows raw harvesting (Primary), industrial transformation (Secondary), and logistics/advisory services (Tertiary).",
        {
            "tier_1": "Identify whether each business harvests raw produce, manufactures inside a plant, or delivers transport/testing services.",
            "tier_2": "Orchard->Primary, bottling factory->Secondary, courier & lab->Tertiary.",
            "tier_3": "Write Primary, Secondary, or Tertiary cleanly.",
        },
        ["classifies_refrigerated_transport_as_secondary"],
    )


def _b50(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    learner = _pick_person(rng)
    prompt = (
        f"Prepare a structured summary for {learner} showing how South Africa's economic system satisfies needs cleanly in {town}: "
        f"explain how **(1) Primary, Secondary, and Tertiary producers**, **(2) Households as dual producers and consumers**, and "
        f"**(3) Water-saving, reuse, and recycling** all work together for long-term sustainability."
    )
    sample = (
        f"1. **Three sectors:** Primary farms/mines supply raw inputs, Secondary factories manufacture durable/utility goods, and "
        f"Tertiary shops/services distribute them to {town} residents.\n"
        f"2. **Households' dual role:** Families supply labour and skills to all three sectors for wages, then spend wages as consumers.\n"
        f"3. **Sustainability:** Saving scarce water, reusing/repairing durables, and recycling waste preserve raw inputs for future production and jobs."
    )
    worked = (
        f"1. **Sector chain [2]:** Raw extraction (Primary) -> processing (Secondary) -> retail/services (Tertiary).\n"
        f"2. **Household dual role [1]:** Supplying labour/entrepreneurship AND buying goods/services.\n"
        f"3. **Sustainable stewardship [1]:** Water conservation, reuse/repair, and recycling stretch finite resources across generations."
    )
    return _q(
        rng,
        "50_goods_services_sustainability_synthesis",
        prompt,
        sample,
        worked,
        "Sustainable economic wellbeing unites productive sector chains, household participation, and disciplined resource conservation.",
        {
            "tier_1": "Use three numbered headings matching the three prompts in the question.",
            "tier_2": "Make sure all three sectors, both household roles, and conservation habits appear explicitly.",
            "tier_3": "Connect Primary/Secondary/Tertiary production with Household labour/spending and Water/Reuse/Recycling stewardship.",
        },
        ["omits_either_household_dual_role_or_sustainability_link"],
        [
            {"criterion": "Explains Primary, Secondary, and Tertiary producer linkage", "marks": 2},
            {"criterion": "Explains households as both producers (labour) and consumers", "marks": 1},
            {"criterion": "Integrates water-saving, reuse, and recycling into long-term sustainability", "marks": 1},
        ],
        cognitive_level="Problem Solving",
        marks=4,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_households_dual_role_circular_flow": _b26,
    "27_efficient_vs_effective_use_definitions": _b27,
    "28_water_scarcity_sa_demand_supply": _b28,
    "29_five_water_saving_methods": _b29,
    "30_dripping_tap_water_waste_calculation": _b30,
    "31_electricity_efficient_appliances_saving": _b31,
    "32_reuse_definition_and_examples": _b32,
    "33_repair_vs_replace_cost_calculation": _b33,
    "34_buying_secondhand_used_goods_benefits": _b34,
    "35_reduce_reuse_recycle_table": _b35,
    "36_recycling_definition_and_materials": _b36,
    "37_recycling_four_step_process": _b37,
    "38_recycling_economic_benefits_jobs": _b38,
    "39_recycling_environmental_benefits": _b39,
    "40_greenhouse_gas_landfill_saving": _b40,
    "41_paper_vs_glass_vs_metal_recycling_table": _b41,
    "42_informal_waste_pickers_value_chain": _b42,
    "43_sustainable_packaging_consumer_choice": _b43,
    "44_service_quality_comparison_scenario": _b44,
    "45_capital_vs_consumer_good_context": _b45,
    "46_export_raw_vs_processed_goods_value": _b46,
    "47_tuckshop_goods_and_services_inventory": _b47,
    "48_green_jobs_entrepreneur_opportunity": _b48,
    "49_goods_services_sectors_audit_table": _b49,
    "50_goods_services_sustainability_synthesis": _b50,
}
