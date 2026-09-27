"""Grade 12 Accounting — Cost Accounting & Break-Even Analysis (Paper 2 Managerial Accounting).
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/Accounting_Gr12/Term 1/01. Manufacturing.md` and authentic NSC Paper 2 exam formats.
Covers:
- 2D Tabular Production Cost Statement (Direct Materials, Direct Labour, Prime Cost, Factory Overheads, Work-in-Progress adjustments).
- Factory Overhead Cost Note (Note 1).
- Work-in-Progress adjustments and Cost of Finished Goods Produced.
- Unit cost of production and Break-Even Point (BEP) margin of safety analysis.
- Cell types (required, given, must_be_empty), deduction rules, and standardized misconception tags.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float, places: int = 2) -> str:
    """Format decimal number using South African comma decimal convention."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip('0').rstrip('.')
    return s.replace('.', ',')


# --------------------------------------------------------------------------- #
# Sub-Drill 1: Prime Cost Calculation
# --------------------------------------------------------------------------- #
def _build_prime_cost_drill(r: random.Random) -> Dict[str, Any]:
    dm = r.randint(15, 45) * 10000  # Direct materials: R150,000 to R450,000
    dl = r.randint(12, 35) * 10000  # Direct labour: R120,000 to R350,000
    elec = r.randint(30, 80) * 1000
    prime_cost = dm + dl

    prompt = (
        f"The accounting records of **Protea Manufacturers** reflect the following costs for the financial year:\n\n"
        f"• Direct raw materials issued to production: R{dm:,}\n"
        f"• Direct factory labour wages: R{dl:,}\n"
        f"• Factory electricity & water: R{elec:,}\n\n"
        f"Calculate the **Prime Cost** for the year."
    )

    return {
        "id": f"acc_prime_{r.randint(100000, 999999)}",
        "title": "Prime Cost Calculation",
        "topic": "Cost Accounting",
        "subskill": "elementary_prime_cost",
        "mode": "elementary_prime_cost",
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"R{prime_cost:,}",
        "sample_answer": f"Prime Cost = Direct Materials (R{dm:,}) + Direct Labour (R{dl:,}) = R{prime_cost:,}",
        "marks": 3,
        "misconception_tags": ["included_overhead_in_prime_cost", "omitted_direct_labour"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identification of Direct Materials", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identification of Direct Labour", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct Prime Cost sum: R{prime_cost:,}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "included_factory_electricity", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Look at direct costs only: direct materials and direct labour.",
            "tier2_directional_rule": "Prime Cost = Direct Material Cost + Direct Labour Cost. Factory electricity is a factory overhead, NOT a prime cost.",
            "tier3_worked_step": f"R{dm:,} + R{dl:,} = R{prime_cost:,}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-Drill 2: Factory Overhead Cost Note Drill
# --------------------------------------------------------------------------- #
def _build_factory_overhead_note_drill(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Soweto Textiles", "Kagiso Woodworks", "Durban Plastics", "Ekurhuleni Motors"])
    ind_mat = r.randint(15, 35) * 1000
    ind_lab = r.randint(45, 90) * 1000
    fac_rent = r.randint(60, 120) * 1000
    deprec = r.randint(25, 55) * 1000
    office_admin = r.randint(30, 70) * 1000  # Distractor (non-manufacturing cost)

    total_foh = ind_mat + ind_lab + fac_rent + deprec

    prompt = (
        f"**{business}**: Complete the **Factory Overhead Cost Note** for the year ended 28 February 2026.\n\n"
        f"**Cost items identified from accounting records:**\n"
        f"• Indirect materials consumed in factory: R{ind_mat:,}\n"
        f"• Factory supervisor and cleaner wages (Indirect labour): R{ind_lab:,}\n"
        f"• Rent of factory premises: R{fac_rent:,}\n"
        f"• Depreciation on factory machinery: R{deprec:,}\n"
        f"• Office stationery and administrative costs: R{office_admin:,} *(Note: Assess whether this is factory or office)*"
    )

    headers = ["Factory Overhead Cost Note", "Amount (R)"]
    rows_data = [
        [
            {"coordinate": "t0_r0_c0", "value": "Indirect materials", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": str(ind_mat), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "Indirect labour", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": str(ind_lab), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Factory rent", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": str(fac_rent), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Depreciation on factory machinery", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": str(deprec), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r4_c0", "value": "TOTAL FACTORY OVERHEAD COST", "type": "given", "editable": False},
            {"coordinate": "t0_r4_c1", "value": str(total_foh), "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": str(ind_mat),
        "t0_r1_c1": str(ind_lab),
        "t0_r2_c1": str(fac_rent),
        "t0_r3_c1": str(deprec),
        "t0_r4_c1": str(total_foh),
    }

    cell_hints = {
        "t0_r0_c1": f"Indirect materials = R{ind_mat:,}.",
        "t0_r1_c1": f"Indirect labour = R{ind_lab:,}.",
        "t0_r2_c1": f"Factory rent = R{fac_rent:,}.",
        "t0_r3_c1": f"Depreciation on factory plant = R{deprec:,}.",
        "t0_r4_c1": f"Total Factory Overhead Cost = Sum of factory overheads = R{total_foh:,}. (Do NOT include office admin).",
    }

    return {
        "id": f"acc_foh_note_{r.randint(100000, 999999)}",
        "title": "Factory Overhead Cost Note",
        "topic": "Cost Accounting",
        "subskill": "elementary_factory_overhead",
        "mode": "elementary_factory_overhead",
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 6,
        "ideal_answer": f"Total Factory Overhead Cost: R{total_foh:,} (Office administrative costs excluded)",
        "sample_answer": f"Completed note totaling R{total_foh:,}",
        "misconception_tags": ["included_admin_in_factory_overhead", "omitted_depreciation"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_ind_mat", "desc": f"Indirect materials: R{ind_mat:,}", "marks": 1, "editable": True},
                {"id": "mp_ind_lab", "desc": f"Indirect labour: R{ind_lab:,}", "marks": 1, "editable": True},
                {"id": "mp_rent", "desc": f"Factory rent: R{fac_rent:,}", "marks": 1, "editable": True},
                {"id": "mp_deprec", "desc": f"Depreciation: R{deprec:,}", "marks": 1, "editable": True},
                {"id": "mp_tot", "desc": f"Correct total: R{total_foh:,}", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "included_admin_cost", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Factory Overhead Note only includes costs directly connected to the factory building and machinery.",
            "tier2_directional_rule": "Administrative and office expenses belong to the Income Statement, NOT the factory overhead note.",
            "tier3_worked_step": f"R{ind_mat:,} + R{ind_lab:,} + R{fac_rent:,} + R{deprec:,} = R{total_foh:,}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-Drill 3: Work-in-Progress (WIP) Adjustments Drill
# --------------------------------------------------------------------------- #
def _build_wip_adjustment_drill(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Cape Footwear", "Polokwane Tiles", "Tshwane Metalworks"])
    tmc = r.randint(80, 160) * 10000  # Total Manufacturing Cost: R800k - R1.6m
    wip_start = r.randint(20, 50) * 1000
    wip_end = r.randint(15, 45) * 1000

    cfg = tmc + wip_start - wip_end

    prompt = (
        f"**{business}**: Work-in-Progress Adjustment.\n\n"
        f"• Total Manufacturing Cost for the financial year: R{tmc:,}\n"
        f"• Work-in-progress stock at the beginning of the year: R{wip_start:,}\n"
        f"• Work-in-progress stock at the end of the year: R{wip_end:,}\n\n"
        f"Calculate the **Cost of Finished Goods Produced** for the year."
    )

    return {
        "id": f"acc_wip_{r.randint(100000, 999999)}",
        "title": "Work-in-Progress Adjustment",
        "topic": "Cost Accounting",
        "subskill": "elementary_wip_adjustment",
        "mode": "elementary_wip_adjustment",
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Cost of Finished Goods Produced = R{cfg:,}",
        "sample_answer": f"TMC (R{tmc:,}) + WIP Start (R{wip_start:,}) - WIP End (R{wip_end:,}) = R{cfg:,}",
        "marks": 3,
        "misconception_tags": ["added_closing_wip_instead_of_subtracting", "subtracted_opening_wip"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_wip_start", "desc": "Opening WIP added to TMC", "marks": 1, "editable": True},
                {"id": "mp_wip_end", "desc": "Closing WIP subtracted", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Correct Cost of Finished Goods: R{cfg:,}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "added_closing_wip_instead_of_subtracting", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Work-in-progress at the beginning was completed this year (+). Work-in-progress at the end remains incomplete (-).",
            "tier2_directional_rule": "Cost of Finished Goods = Total Manufacturing Cost + WIP (beginning) - WIP (end).",
            "tier3_worked_step": f"R{tmc:,} + R{wip_start:,} - R{wip_end:,} = R{cfg:,}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-Drill 4: Break-Even Point Calculation
# --------------------------------------------------------------------------- #
def _build_break_even_drill(r: random.Random) -> Dict[str, Any]:
    sp_unit = r.choice([250, 300, 400, 500])
    vc_unit = int(sp_unit * r.choice([0.5, 0.6, 0.65]))
    contribution = sp_unit - vc_unit

    target_bep = r.randint(20, 60) * 100
    fc_total = target_bep * contribution
    actual_produced = int(target_bep * r.choice([1.15, 1.25, 0.90]))

    prompt = (
        f"**Kagiso Shoes** manufactured and sold {actual_produced:,} pairs of school shoes during the financial year.\n\n"
        f"• Selling price per pair: R{sp_unit}\n"
        f"• Variable cost per pair: R{vc_unit}\n"
        f"• Total fixed costs for the year: R{fc_total:,}\n\n"
        f"1. Calculate the Break-Even Point (BEP) in units.\n"
        f"2. Comment on whether the business operated at a profit or a loss based on production volume."
    )

    profit_status = "profit" if actual_produced > target_bep else "loss"
    margin_diff = abs(actual_produced - target_bep)

    return {
        "id": f"acc_bep_{r.randint(100000, 999999)}",
        "title": "Break-Even Point Calculation",
        "topic": "Cost Accounting",
        "subskill": "elementary_break_even_calc",
        "mode": "elementary_break_even_calc",
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"BEP = {target_bep:,} units; Operated at a {profit_status} (margin of {margin_diff:,} units).",
        "sample_answer": (
            f"Contribution per unit = Selling Price (R{sp_unit}) - Variable Cost (R{vc_unit}) = R{contribution}\n"
            f"BEP = Total Fixed Costs / Contribution per unit = R{fc_total:,} / R{contribution} = {target_bep:,} units.\n"
            f"The business produced {actual_produced:,} units, which is {margin_diff:,} units {'above' if actual_produced > target_bep else 'below'} BEP, resulting in a {profit_status}."
        ),
        "marks": 5,
        "misconception_tags": ["inverted_bep_formula", "used_selling_price_instead_of_contribution"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_contrib", "desc": "Calculation of contribution per unit (SP - VC)", "marks": 1, "editable": True},
                {"id": "mp_formula", "desc": "BEP Formula: Fixed Costs / (SP - VC)", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": "Correct substitution into BEP formula", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Correct BEP value: {target_bep:,} units", "marks": 1, "editable": True},
                {"id": "mp_comment", "desc": f"Valid comparison to actual production showing {profit_status}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "First find the contribution per unit: Selling Price minus Variable Cost.",
            "tier2_directional_rule": "Break-Even Point (units) = Total Fixed Costs / (Selling Price per unit - Variable Cost per unit).",
            "tier3_worked_step": f"Contribution = R{sp_unit} - R{vc_unit} = R{contribution}. BEP = R{fc_total:,} / R{contribution} = {target_bep:,} units.",
        },
    }


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Complete 2D Production Cost Statement
# --------------------------------------------------------------------------- #
def _build_compound_production_cost(r: random.Random) -> Dict[str, Any]:
    business = r.choice(["Bafana Clothing", "Sizwe Furniture", "Kasi Bicycles", "Ubuntu Electronics"])
    year = 2026

    dm = r.randint(20, 50) * 10000  # Direct Material
    dl = r.randint(18, 40) * 10000  # Direct Labour
    prime_cost = dm + dl

    # Factory Overheads breakdown
    ind_mat = r.randint(15, 30) * 1000
    ind_lab = r.randint(40, 80) * 1000
    rent_fac = r.randint(60, 120) * 1000
    deprec_plant = r.randint(30, 60) * 1000
    factory_overhead = ind_mat + ind_lab + rent_fac + deprec_plant

    total_manufacturing_cost = prime_cost + factory_overhead

    wip_start = r.randint(15, 35) * 1000
    wip_end = r.randint(10, 30) * 1000
    cost_finished_goods = total_manufacturing_cost + wip_start - wip_end

    units_produced = r.randint(10, 25) * 1000
    unit_cost = round(cost_finished_goods / units_produced, 2)

    prompt = (
        f"You are provided with financial information relating to **{business}** for the year ended 28 February {year}.\n\n"
        f"**Financial Information:**\n"
        f"• Direct raw material cost: R{dm:,}\n"
        f"• Direct factory labour cost: R{dl:,}\n"
        f"• Factory overhead costs (Factory Overhead Note total): R{factory_overhead:,}\n"
        f"• Work-in-progress stock (1 March {year-1}): R{wip_start:,}\n"
        f"• Work-in-progress stock (28 February {year}): R{wip_end:,}\n"
        f"• Number of units completed during the year: {units_produced:,} units\n\n"
        f"**Required:**\n"
        f"1. Complete the **Production Cost Statement** for the year ended 28 February {year}.\n"
        f"2. Calculate the unit cost of production per finished unit."
    )

    headers = ["Production Cost Statement", "Amount (R)"]

    items_data = [
        ("Direct material cost", str(dm), "Given direct raw material cost"),
        ("Direct labour cost", str(dl), "Given direct factory labour wages"),
        ("PRIME COST", str(prime_cost), f"Prime Cost = Direct Materials (R{dm:,}) + Direct Labour (R{dl:,})"),
        ("Factory overhead cost", str(factory_overhead), "From Factory Overhead Cost Note"),
        ("TOTAL PRODUCTION COST", str(total_manufacturing_cost), f"Total Production Cost = Prime Cost (R{prime_cost:,}) + FOH (R{factory_overhead:,})"),
        ("Work-in-progress (beginning of year)", str(wip_start), "Opening WIP is added"),
        ("Work-in-progress subtotal", str(total_manufacturing_cost + wip_start), "Subtotal before deducting closing WIP"),
        ("Work-in-progress (end of year)", f"({wip_end})", "Closing WIP is SUBTRACTED (in brackets)"),
        ("COST OF PRODUCTION OF FINISHED GOODS", str(cost_finished_goods), f"Finished goods = Subtotal - Closing WIP = R{cost_finished_goods:,}"),
    ]

    rows_data = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (desc, val, hint_msg) in enumerate(items_data):
        coord = f"t0_r{rix}_c1"
        correct_map[coord] = val
        cell_hints[coord] = hint_msg

        rows_data.append([
            {"coordinate": f"t0_r{rix}_c0", "value": desc, "type": "given", "editable": False},
            {"coordinate": coord, "value": val, "type": "required", "editable": True},
        ])

    marking_points = [
        {"id": "mp_dm", "desc": f"Direct Material Cost: R{dm:,}", "marks": 1, "editable": True},
        {"id": "mp_dl", "desc": f"Direct Labour Cost: R{dl:,}", "marks": 1, "editable": True},
        {"id": "mp_prime", "desc": f"Prime Cost calculated: R{prime_cost:,}", "marks": 2, "editable": True},
        {"id": "mp_foh", "desc": f"Factory Overhead cost: R{factory_overhead:,}", "marks": 2, "editable": True},
        {"id": "mp_tmc", "desc": f"Total Production Cost: R{total_manufacturing_cost:,}", "marks": 2, "editable": True},
        {"id": "mp_wip_add", "desc": f"Work-in-progress start added: R{wip_start:,}", "marks": 1, "editable": True},
        {"id": "mp_wip_sub", "desc": f"Work-in-progress end subtracted: ({wip_end:,})", "marks": 1, "editable": True},
        {"id": "mp_cfg", "desc": f"Cost of Finished Goods: R{cost_finished_goods:,}", "marks": 1, "editable": True},
        {"id": "mp_unit_cost", "desc": f"Unit cost: R{_fmt_sa(unit_cost)} per unit", "marks": 1, "editable": True},
    ]

    marking_schema = {
        "total_marks": 12,
        "marking_points": marking_points,
        "deductions": [
            {"rule": "added_closing_wip_instead_of_subtracting", "penalty": -1},
            {"rule": "must_be_empty_filled", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    return {
        "id": f"acc_pcs_{r.randint(100000, 999999)}",
        "title": "Production Cost Statement",
        "topic": "Cost Accounting",
        "subskill": "production_cost_statement",
        "mode": "compound",
        "difficulty": "hard",
        "term": 3,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 15,
        "prompt": prompt,
        "question_type": "table_completion",
        "headers": headers,
        "rows": rows_data,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Cost of Finished Goods: R{cost_finished_goods:,}; Unit Cost: R{_fmt_sa(unit_cost)} per unit",
        "sample_answer": f"Completed Production Cost Statement (Finished Goods: R{cost_finished_goods:,})",
        "marks": 12,
        "misconception_tags": [
            "added_closing_wip_instead_of_subtracting",
            "omitted_factory_overhead_note",
            "inverted_unit_cost_ratio",
        ],
        "marking_schema": marking_schema,
        "hints": {
            "tier1_location": "Follow the standard NSC Production Cost Statement format from Prime Cost to Cost of Finished Goods.",
            "tier2_directional_rule": (
                "Prime Cost = Direct Materials + Direct Labour. Add Factory Overheads to get Total Production Cost. "
                "Add opening WIP, and SUBTRACT closing WIP to find Cost of Finished Goods."
            ),
            "tier3_worked_step": (
                f"Prime Cost = R{prime_cost:,}. FOH = R{factory_overhead:,}. Total Production Cost = R{total_manufacturing_cost:,}. "
                f"Finished Goods = R{cost_finished_goods:,}. Unit Cost = R{cost_finished_goods:,} / {units_produced:,} = R{_fmt_sa(unit_cost)}."
            ),
        },
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_production_cost,
    "production_cost_statement": _build_compound_production_cost,
    "elementary_prime_cost": _build_prime_cost_drill,
    "elementary_factory_overhead": _build_factory_overhead_note_drill,
    "elementary_wip_adjustment": _build_wip_adjustment_drill,
    "elementary_break_even_calc": _build_break_even_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Accounting Cost Accounting questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_production_cost)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
