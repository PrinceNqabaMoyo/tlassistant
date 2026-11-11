"""
Grade 10 Accounting: Cost Accounting (Introductory Manufacturing Concepts)
Strictly aligned with South African National Curriculum Standards for Grade 10 Accounting (Term 3).
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "cost_classification_table",
    "fixed_vs_variable_costs",
    "direct_material_cost_calculation",
    "direct_labour_cost_calculation",
    "factory_overhead_cost_schedule",
    "total_cost_of_production_and_unit_cost",
]

MANUFACTURERS = [
    ("Ubuntu Uniform Manufacturers", "school blazers"),
    ("Karoo Leather Craft", "leather satchels"),
    ("Ndlovu Furniture Works", "pine study desks"),
    ("Highveld Bakery & Confectionery", "specialty cake boxes"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_cost_classification_table(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    dm = r.randint(45, 95) * 1000
    dl = r.randint(35, 80) * 1000
    foh = r.randint(20, 45) * 1000
    sell = r.randint(12, 28) * 1000
    admin = r.randint(15, 32) * 1000

    headers = ["Cost Item", "Amount (R)", "Cost Category (Direct Material / Direct Labour / Factory Overhead / Administration / Selling & Distribution)"]
    rows = [
        [f"Raw materials used to make {product}", f"R{dm:,}", "{r0_c2}"],
        [f"Wages of factory machine operators assembling {product}", f"R{dl:,}", "{r1_c2}"],
        ["Factory rent, water, electricity, and indirect cleaning materials", f"R{foh:,}", "{r2_c2}"],
        ["Commission paid to sales representatives and delivery vehicle fuel", f"R{sell:,}", "{r3_c2}"],
        ["Salaries of office bookkeeper and office stationery", f"R{admin:,}", "{r4_c2}"],
    ]
    correct_map = {
        "r0_c2": "Direct Material",
        "r1_c2": "Direct Labour",
        "r2_c2": "Factory Overhead",
        "r3_c2": "Selling & Distribution",
        "r4_c2": "Administration",
    }
    worked = (
        f"**{firm} — Cost Classification Schedule**\n\n"
        f"- Raw materials (`R{dm:,}`) $\\rightarrow$ **Direct Material** (traceable directly to each unit produced).\n"
        f"- Machine operators' wages (`R{dl:,}`) $\\rightarrow$ **Direct Labour** (hands-on production workers).\n"
        f"- Factory rent & indirect materials (`R{foh:,}`) $\\rightarrow$ **Factory Overhead** (indirect factory running costs).\n"
        f"- Sales commission & delivery fuel (`R{sell:,}`) $\\rightarrow$ **Selling & Distribution** (marketing and delivery).\n"
        f"- Bookkeeper salary & office stationery (`R{admin:,}`) $\\rightarrow$ **Administration** (general office management)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "cost_classification_table",
        "question_text": (
            f"**{firm}** manufactures **{product}**. Classify each of the following cost items into its correct "
            f"manufacturing or non-manufacturing cost category."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Distinguish between costs incurred inside the factory (Direct Material, Direct Labour, Factory Overhead) and outside the factory (Administration, Selling & Distribution).",
            "Ask: Does this cost physically become part of the product (Direct Material), pay the assembly worker (Direct Labour), or keep the factory running (Factory Overhead)?",
            worked,
        ),
    }


def _gen_fixed_vs_variable_costs(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    fixed_rent = r.randint(15, 30) * 1000
    var_mat_per_unit = r.randint(80, 160)
    units_low = r.randint(400, 600)
    units_high = units_low + 400

    tot_var_low = units_low * var_mat_per_unit
    tot_var_high = units_high * var_mat_per_unit
    fixed_per_unit_low = round(fixed_rent / units_low, 2)
    fixed_per_unit_high = round(fixed_rent / units_high, 2)

    headers = ["Production Level", f"{units_low} units (R)", f"{units_high} units (R)"]
    rows = [
        [f"Total Variable Material Cost (R{var_mat_per_unit} per unit)", "{r0_c1}", "{r0_c2}"],
        [f"Total Fixed Factory Rent (R{fixed_rent:,} per month)", "{r1_c1}", "{r1_c2}"],
        ["Fixed Factory Rent Cost per Unit (rounded to 2 decimal places)", "{r2_c1}", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": tot_var_low,
        "r0_c2": tot_var_high,
        "r1_c1": fixed_rent,
        "r1_c2": fixed_rent,
        "r2_c1": fixed_per_unit_low,
        "r2_c2": fixed_per_unit_high,
    }
    worked = (
        f"**Fixed vs Variable Cost Behaviour ({firm})**\n\n"
        f"- **Total Variable Cost** changes in direct proportion to output:\n"
        f"  - At `{units_low}` units: `{units_low} × R{var_mat_per_unit} = R{tot_var_low:,}`\n"
        f"  - At `{units_high}` units: `{units_high} × R{var_mat_per_unit} = R{tot_var_high:,}`\n"
        f"- **Total Fixed Cost** remains constant at `R{fixed_rent:,}` regardless of production volume.\n"
        f"- **Fixed Cost per Unit** decreases as output increases:\n"
        f"  - At `{units_low}` units: `R{fixed_rent:,} ÷ {units_low} = R{fixed_per_unit_low:.2f}`\n"
        f"  - At `{units_high}` units: `R{fixed_rent:,} ÷ {units_high} = R{fixed_per_unit_high:.2f}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "fixed_vs_variable_costs",
        "question_text": (
            f"**{firm}** produces **{product}**. Monthly fixed factory rent is **R{fixed_rent:,}**, and direct material cost "
            f"is **R{var_mat_per_unit}** per unit. Complete the schedule comparing cost behaviour at **{units_low} units** and **{units_high} units**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Total variable cost varies with the number of units produced, whereas total fixed cost stays constant in total.",
            "Multiply units by the variable cost per unit for Row 1; keep fixed rent identical in Row 2; divide fixed rent by units in Row 3.",
            worked,
        ),
    }


def _gen_direct_material_cost(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    opening = r.randint(20, 45) * 1000
    purchases = r.randint(110, 190) * 1000
    carriage = r.randint(6, 15) * 1000
    returns = r.randint(4, 10) * 1000
    closing = r.randint(25, 50) * 1000
    available = opening + purchases + carriage - returns
    dmc = available - closing

    headers = ["Direct Material Cost Calculation", "Amount (R)"]
    rows = [
        ["Opening stock of raw materials", f"R{opening:,}"],
        ["Net purchases of raw materials (Purchases less returns)", "{r1_c1}"],
        ["Carriage on raw materials purchased", f"R{carriage:,}"],
        ["Raw materials available for production", "{r3_c1}"],
        ["Less: Closing stock of raw materials", f"(R{closing:,})"],
        ["Direct Material Cost issued to factory", "{r5_c1}"],
    ]
    correct_map = {
        "r1_c1": purchases - returns,
        "r3_c1": available,
        "r5_c1": dmc,
    }
    worked = (
        f"**Direct Material Cost Schedule ({firm})**\n\n"
        f"- Opening raw material stock: `R{opening:,}`\n"
        f"- Net purchases: `R{purchases:,} - R{returns:,} = R{purchases - returns:,}`\n"
        f"- Add carriage on purchases: `R{carriage:,}`\n"
        f"- Raw materials available: `R{opening:,} + R{purchases - returns:,} + R{carriage:,} = R{available:,}`\n"
        f"- Less closing raw material stock: `(R{closing:,})`\n"
        f"- **Direct Material Cost**: `R{dmc:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "direct_material_cost_calculation",
        "question_text": (
            f"**{firm}** provided the following raw material figures for the period:\n"
            f"- Opening raw material stock: **R{opening:,}**\n"
            f"- Raw materials purchased: **R{purchases:,}**\n"
            f"- Defective raw materials returned to suppliers: **R{returns:,}**\n"
            f"- Carriage on purchases of raw materials: **R{carriage:,}**\n"
            f"- Closing raw material stock: **R{closing:,}**\n\n"
            f"Complete the Direct Material Cost calculation table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Direct Material Cost follows the same logic as Cost of Sales: Opening Stock + Net Purchases + Carriage - Closing Stock.",
            "First subtract returns from purchases. Add opening stock and carriage to find materials available, then subtract closing stock.",
            worked,
        ),
    }


def _gen_direct_labour_cost(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    workers = r.randint(6, 12)
    normal_hrs = 160
    normal_rate = r.randint(45, 75)
    overtime_hrs = r.randint(10, 25)
    overtime_rate = int(normal_rate * 1.5)
    uif_contrib = round(workers * (normal_hrs * normal_rate) * 0.01)

    total_normal = workers * normal_hrs * normal_rate
    total_overtime = workers * overtime_hrs * overtime_rate
    dlc = total_normal + total_overtime + uif_contrib

    headers = ["Direct Labour Cost Component", "Calculation / Detail", "Amount (R)"]
    rows = [
        ["Normal factory wages", f"{workers} workers × {normal_hrs} hrs × R{normal_rate}/hr", "{r0_c2}"],
        ["Overtime wages", f"{workers} workers × {overtime_hrs} hrs × R{overtime_rate}/hr", "{r1_c2}"],
        ["Employer UIF & skills contribution (1% of normal wages)", "1% employer contribution", f"R{uif_contrib:,}"],
        ["Total Direct Labour Cost", "Sum of direct factory labour remuneration", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c2": total_normal,
        "r1_c2": total_overtime,
        "r3_c2": dlc,
    }
    worked = (
        f"**Direct Labour Cost Calculation ({firm})**\n\n"
        f"- Normal wages: `{workers} × {normal_hrs} × R{normal_rate} = R{total_normal:,}`\n"
        f"- Overtime wages: `{workers} × {overtime_hrs} × R{overtime_rate} = R{total_overtime:,}`\n"
        f"- Employer contributions: `R{uif_contrib:,}`\n"
        f"- **Total Direct Labour Cost**: `R{total_normal:,} + R{total_overtime:,} + R{uif_contrib:,} = R{dlc:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "direct_labour_cost_calculation",
        "question_text": (
            f"**{firm}** employs **{workers} direct production workers** to manufacture **{product}**. "
            f"Each worker worked **{normal_hrs} normal hours** at **R{normal_rate} per hour** and **{overtime_hrs} overtime hours** "
            f"at **R{overtime_rate} per hour**. Employer UIF contribution is **R{uif_contrib:,}**. Complete the Direct Labour Cost schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Direct Labour Cost includes normal wages, overtime wages, and employer contributions for workers directly making the product.",
            "Multiply the number of workers by hours and hourly rate for both normal time and overtime, then add employer contributions.",
            worked,
        ),
    }


def _gen_factory_overhead_schedule(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(MANUFACTURERS)
    indirect_mat = r.randint(8, 18) * 1000
    supervisor = r.randint(24, 42) * 1000
    total_rent = r.randint(40, 60) * 1000
    factory_rent = int(total_rent * 0.75)
    total_elec = r.randint(20, 35) * 1000
    factory_elec = int(total_elec * 0.80)
    depr_plant = r.randint(12, 25) * 1000
    total_foh = indirect_mat + supervisor + factory_rent + factory_elec + depr_plant

    headers = ["Factory Overhead Item", "Allocation Basis", "Factory Portion (R)"]
    rows = [
        ["Indirect materials (cleaning consumables & lubricants)", "100% Factory", f"R{indirect_mat:,}"],
        ["Factory supervisor & cleaner wages (Indirect labour)", "100% Factory", f"R{supervisor:,}"],
        [f"Rent expense (Total R{total_rent:,})", "75% allocated to Factory floor area", "{r2_c2}"],
        [f"Water and electricity (Total R{total_elec:,})", "80% allocated to Factory machinery", "{r3_c2}"],
        ["Depreciation on factory plant and machinery", "100% Factory", f"R{depr_plant:,}"],
        ["Total Factory Overhead Cost", "Total indirect manufacturing costs", "{r5_c2}"],
    ]
    correct_map = {
        "r2_c2": factory_rent,
        "r3_c2": factory_elec,
        "r5_c2": total_foh,
    }
    worked = (
        f"**Factory Overhead Schedule ({firm})**\n\n"
        f"- Indirect materials: `R{indirect_mat:,}`\n"
        f"- Indirect factory wages: `R{supervisor:,}`\n"
        f"- Factory rent (75% of R{total_rent:,}): `R{factory_rent:,}`\n"
        f"- Factory water & electricity (80% of R{total_elec:,}): `R{factory_elec:,}`\n"
        f"- Depreciation on factory machinery: `R{depr_plant:,}`\n"
        f"- **Total Factory Overhead Cost**: `R{total_foh:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "factory_overhead_cost_schedule",
        "question_text": (
            f"Calculate the **Factory Overhead Cost** for **{firm}**. Note that **75%** of rent (`R{total_rent:,}`) "
            f"and **80%** of water and electricity (`R{total_elec:,}`) relate to the factory."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Only the factory portion of shared expenses (rent, electricity) is included in Factory Overheads.",
            "Calculate 75% of total rent and 80% of total water & electricity, then sum all 5 factory overhead items.",
            worked,
        ),
    }


def _gen_total_cost_and_unit_cost(r: random.Random) -> Dict[str, Any]:
    firm, product = r.choice(MANUFACTURERS)
    dmc = r.randint(120, 200) * 1000
    dlc = r.randint(90, 150) * 1000
    prime = dmc + dlc
    foh = r.randint(50, 90) * 1000
    total_cop = prime + foh
    units = 2000
    unit_cost = round(total_cop / units, 2)

    headers = ["Production Cost Summary", "Amount (R)"]
    rows = [
        ["Direct Material Cost", f"R{dmc:,}"],
        ["Direct Labour Cost", f"R{dlc:,}"],
        ["Prime Cost (Direct Cost)", "{r2_c1}"],
        ["Factory Overhead Cost", f"R{foh:,}"],
        ["Total Cost of Production", "{r4_c1}"],
        [f"Unit Cost of Production ({units:,} units produced)", "{r5_c1}"],
    ]
    correct_map = {
        "r2_c1": prime,
        "r4_c1": total_cop,
        "r5_c1": unit_cost,
    }
    worked = (
        f"**Total Cost of Production & Unit Cost ({firm})**\n\n"
        f"- **Prime Cost** = Direct Material (`R{dmc:,}`) + Direct Labour (`R{dlc:,}`) = `R{prime:,}`\n"
        f"- **Total Cost of Production** = Prime Cost (`R{prime:,}`) + Factory Overheads (`R{foh:,}`) = `R{total_cop:,}`\n"
        f"- **Unit Cost** = `R{total_cop:,} ÷ {units:,} units = R{unit_cost:.2f} per unit`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "total_cost_of_production_and_unit_cost",
        "question_text": (
            f"**{firm}** manufactured **{units:,} {product}** during the period. Using the cost figures in the table, "
            f"calculate the **Prime Cost**, **Total Cost of Production**, and **Unit Cost of Production**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Prime Cost is the sum of all direct manufacturing costs (Direct Material + Direct Labour).",
            "Add Factory Overhead Cost to Prime Cost to obtain Total Cost of Production, then divide by the number of units produced.",
            worked,
        ),
    }


_BUILDERS = {
    "cost_classification_table": _gen_cost_classification_table,
    "fixed_vs_variable_costs": _gen_fixed_vs_variable_costs,
    "direct_material_cost_calculation": _gen_direct_material_cost,
    "direct_labour_cost_calculation": _gen_direct_labour_cost,
    "factory_overhead_cost_schedule": _gen_factory_overhead_schedule,
    "total_cost_of_production_and_unit_cost": _gen_total_cost_and_unit_cost,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Cost accounting"
        q["grade"] = "10"
        out.append(q)
    return out
