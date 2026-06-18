"""
fixed_assets_generator.py — Grade 12 Term 2
=============================================
Fixed/Tangible Assets question generator.

Archetype classes covered:
  1. Depreciation (straight-line)
  2. Depreciation (diminishing balance)
  3. Asset disposal profit/loss
  4. Cost price back-calculation
  5. Trade-in value calculation
  6. Total depreciation for year
  7. Fully depreciated asset handling
  8. Tangible assets note (balance sheet)
  9. CSR / ethics of asset donation
 10. Internal control for fixed assets
 11. GAAP principles for fixed assets
 12. Additional depreciation on sold asset
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed() if seed is None else r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _rm(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


# ---------------------------------------------------------------------------
# Pools
# ---------------------------------------------------------------------------

_COMPANIES = [
    "Kloof Computers (Pty) Ltd", "Ivory Park Ltd", "Thembeka (Pty) Ltd",
    "Starlight Ltd", "Laysano Ltd", "Justime Footwear (Pty) Ltd",
    "Eastgate Motors Ltd", "Hillside Trading (Pty) Ltd",
    "Northgate Engineering Ltd", "Coastal Logistics (Pty) Ltd",
]

_ASSET_TYPES = ["vehicle", "delivery van", "equipment", "computer", "machinery"]

_FIN_YEAR_ENDS = [
    "28 February", "30 June", "31 December", "31 March",
]


# ---------------------------------------------------------------------------
# Factories
# ---------------------------------------------------------------------------

def _make_mcq(*, prompt, options, correct_index, explanation):
    return {
        "id": _make_id("acct12_fa_mcq"), "question_type": "mcq",
        "prompt": prompt, "options": options,
        "correct_index": int(correct_index), "explanation": explanation,
        "expected_answer_type": "mcq", "marks": 2,
        "guidelines": [explanation], "visual_aid_key": "fixed_assets_t2",
    }


def _make_typed(*, prompt, sample_answer, grading_rubric=None):
    gr = grading_rubric or []
    return {
        "id": _make_id("acct12_fa_typed"), "question_type": "typed",
        "prompt": prompt, "sample_answer": sample_answer,
        "expected_answer_type": "text", "grading_rubric": gr,
        "marks": 4 if len(gr) >= 2 else 2,
        "guidelines": [f"Include: {', '.join(gr)}"] if gr else [],
        "visual_aid_key": "fixed_assets_t2",
    }


def _make_calc(*, prompt, correct_answer, unit="R", working_formula=""):
    return {
        "id": _make_id("acct12_fa_calc"), "question_type": "calc",
        "prompt": prompt, "correct_value": correct_answer,
        "correct_answer": correct_answer, "unit": unit,
        "working_formula": working_formula, "expected_answer_type": "number",
        "marks": 3, "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "fixed_assets_t2",
    }


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def _gen_depreciation_straight_line(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["equipment", "vehicle", "computer"])
    cost = _rm(r.choice([100, 150, 200, 250, 300, 400, 500, 600, 800]) * 1000)
    rate = r.choice([10, 15, 20, 25])
    months = r.choice([6, 7, 8, 9, 12])
    dep = _rm(cost * rate / 100 * months / 12)
    return _make_calc(
        prompt=(
            f"{co} purchased {asset} for {_money(cost)}. "
            f"Depreciation is calculated at {rate}% p.a. on cost (straight-line method). "
            f"The asset was used for {months} months during the financial year. "
            f"Calculate the depreciation for the year."
        ),
        correct_answer=dep, unit="R",
        working_formula=f"{rate}% × {_money(cost)} × {months}/12 = {_money(dep)}",
    )


def _gen_depreciation_diminishing(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["vehicle", "delivery van"])
    cost = _rm(r.choice([150, 200, 240, 300, 400]) * 1000)
    rate = r.choice([15, 20, 25])
    yr1_dep = _rm(cost * rate / 100)
    cv_yr2 = _rm(cost - yr1_dep)
    yr2_dep = _rm(cv_yr2 * rate / 100)
    acc_dep = _rm(yr1_dep + yr2_dep)
    cv_yr3 = _rm(cv_yr2 - yr2_dep)
    yr3_dep = _rm(cv_yr3 * rate / 100)
    return _make_calc(
        prompt=(
            f"{co} owns a {asset} purchased for {_money(cost)}. "
            f"Depreciation: {rate}% p.a. on the diminishing-balance method.\n"
            f"Accumulated depreciation after 2 years: {_money(acc_dep)}.\n"
            f"Calculate the depreciation for year 3."
        ),
        correct_answer=yr3_dep, unit="R",
        working_formula=(
            f"Carrying value = {_money(cost)} − {_money(acc_dep)} = {_money(cv_yr3)}. "
            f"Depreciation = {rate}% × {_money(cv_yr3)} = {_money(yr3_dep)}"
        ),
    )


def _gen_disposal_profit_loss(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(_ASSET_TYPES)
    fy = r.choice(_FIN_YEAR_ENDS)
    cost = _rm(r.choice([80, 100, 150, 180, 200, 240, 300]) * 1000)
    rate = r.choice([15, 20, 25])
    method = r.choice(["straight-line", "diminishing-balance"])

    if method == "straight-line":
        yr_dep = _rm(cost * rate / 100)
    else:
        yr_dep = _rm(cost * rate / 100)

    full_years = r.randint(1, 4)
    if method == "straight-line":
        acc = _rm(yr_dep * full_years)
    else:
        acc = 0.0
        cv = cost
        for _ in range(full_years):
            d = _rm(cv * rate / 100)
            acc = _rm(acc + d)
            cv = _rm(cv - d)

    # Additional depreciation for partial year
    add_months = r.choice([3, 6, 9])
    if method == "straight-line":
        add_dep = _rm(cost * rate / 100 * add_months / 12)
    else:
        cv_at_start = _rm(cost - acc)
        add_dep = _rm(cv_at_start * rate / 100 * add_months / 12)

    total_dep = _rm(acc + add_dep)
    carrying = _rm(cost - total_dep)
    sell = _rm(carrying * r.uniform(0.6, 1.5))
    result = _rm(sell - carrying)
    label = "profit" if result >= 0 else "loss"

    return _make_calc(
        prompt=(
            f"A {asset} at {co} was sold after {full_years} full years "
            f"and {add_months} additional months.\n"
            f"• Cost price: {_money(cost)}\n"
            f"• Depreciation: {rate}% p.a. on {method}\n"
            f"• Accumulated depreciation at start of current year: {_money(acc)}\n"
            f"• Selling price: {_money(sell)}\n\n"
            f"Calculate the {label} on disposal."
        ),
        correct_answer=abs(result), unit="R",
        working_formula=(
            f"Additional dep = {rate}% × "
            + (f"{_money(cost)}" if method == "straight-line" else f"{_money(_rm(cost - acc))}")
            + f" × {add_months}/12 = {_money(add_dep)}. "
            f"Total dep = {_money(acc)} + {_money(add_dep)} = {_money(total_dep)}. "
            f"CV = {_money(cost)} − {_money(total_dep)} = {_money(carrying)}. "
            f"{label.title()} = {_money(sell)} − {_money(carrying)} = {_money(abs(result))}"
        ),
    )


def _gen_cost_price_backcalc(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["vehicles", "equipment"])
    closing_bal = _rm(r.randint(800, 2000) * 1000)
    disposed_cost = _rm(r.choice([80, 120, 150, 180, 240]) * 1000)
    new_purchase = _rm(r.choice([200, 260, 300, 320, 400]) * 1000)
    opening = _rm(closing_bal - new_purchase + disposed_cost)

    return _make_calc(
        prompt=(
            f"{co}: {asset.title()} at cost on the current balance sheet = {_money(closing_bal)}. "
            f"During the year, a {asset[:-1]} costing {_money(disposed_cost)} was disposed of "
            f"and a new one costing {_money(new_purchase)} was purchased. "
            f"Calculate the cost price of {asset} at the beginning of the year."
        ),
        correct_answer=opening, unit="R",
        working_formula=(
            f"{_money(closing_bal)} − {_money(new_purchase)} + {_money(disposed_cost)} = {_money(opening)}"
        ),
    )


def _gen_trade_in_value(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["vehicle", "delivery van"])
    cost = _rm(r.choice([150, 180, 200, 240, 300]) * 1000)
    rate = 20
    # 2 full years diminishing balance
    dep1 = _rm(cost * rate / 100)
    cv1 = _rm(cost - dep1)
    dep2 = _rm(cv1 * rate / 100)
    acc_full = _rm(dep1 + dep2)
    cv_start = _rm(cost - acc_full)
    # additional months
    add_months = r.choice([3, 6])
    add_dep = _rm(cv_start * rate / 100 * add_months / 12)
    total_acc = _rm(acc_full + add_dep)
    cv_at_sale = _rm(cost - total_acc)
    profit = _rm(r.randint(2, 15) * 1000)
    trade_in = _rm(cv_at_sale + profit)

    return _make_calc(
        prompt=(
            f"A {asset} at {co} was traded in after 2 years and {add_months} months.\n"
            f"• Cost: {_money(cost)}\n"
            f"• Depreciation: {rate}% p.a. diminishing balance\n"
            f"• Profit on disposal: {_money(profit)}\n"
            f"• Accumulated depreciation at start of disposal year: {_money(acc_full)}\n\n"
            f"Calculate the trade-in value received."
        ),
        correct_answer=trade_in, unit="R",
        working_formula=(
            f"Add. dep = {rate}% × {_money(cv_start)} × {add_months}/12 = {_money(add_dep)}. "
            f"CV = {_money(cost)} − {_money(total_acc)} = {_money(cv_at_sale)}. "
            f"Trade-in = {_money(cv_at_sale)} + {_money(profit)} = {_money(trade_in)}"
        ),
    )


def _gen_total_depreciation(r: random.Random):
    co = r.choice(_COMPANIES)
    veh_dep = _rm(r.randint(100, 200) * 1000)
    sold_veh_dep = _rm(r.randint(10, 30) * 1000)
    equip_rate = r.choice([10, 15, 20])
    equip_cost = _rm(r.randint(500, 900) * 1000)
    equip_dep = _rm(equip_cost * equip_rate / 100)
    new_equip_cost = _rm(r.randint(30, 80) * 1000)
    new_months = r.choice([3, 5, 7])
    new_equip_dep = _rm(new_equip_cost * equip_rate / 100 * new_months / 12)
    total = _rm(veh_dep + sold_veh_dep + equip_dep + new_equip_dep)

    return _make_calc(
        prompt=(
            f"{co}: Calculate total depreciation for the year:\n"
            f"• Depreciation on remaining vehicles: {_money(veh_dep)}\n"
            f"• Depreciation on vehicle sold: {_money(sold_veh_dep)}\n"
            f"• Equipment at cost: {_money(equip_cost)} at {equip_rate}% on cost\n"
            f"• New equipment purchased ({new_months} months ago): {_money(new_equip_cost)}"
        ),
        correct_answer=total, unit="R",
        working_formula=(
            f"Vehicles = {_money(veh_dep)} + {_money(sold_veh_dep)} = {_money(_rm(veh_dep + sold_veh_dep))}. "
            f"Equipment = {equip_rate}% × {_money(equip_cost)} = {_money(equip_dep)}. "
            f"New equip = {equip_rate}% × {_money(new_equip_cost)} × {new_months}/12 = {_money(new_equip_dep)}. "
            f"Total = {_money(total)}"
        ),
    )


def _gen_fully_depreciated(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["computer", "equipment"])
    cost = _rm(r.choice([200, 300, 400, 500]) * 1000)
    rate = r.choice([20, 25, 33])
    acc_dep = _rm(cost * r.uniform(0.8, 0.95))
    remaining = _rm(cost - acc_dep)
    # Cannot depreciate below R1
    correct_dep = _rm(remaining - 1)

    return _make_calc(
        prompt=(
            f"The bookkeeper at {co} calculated depreciation on {asset} as "
            f"{rate}% × {_money(cost)} = {_money(_rm(cost * rate / 100))}. "
            f"However, the accumulated depreciation is already {_money(acc_dep)} "
            f"(cost: {_money(cost)}). "
            f"Calculate the correct depreciation, knowing the minimum carrying value is R1."
        ),
        correct_answer=correct_dep, unit="R",
        working_formula=(
            f"Remaining = {_money(cost)} − {_money(acc_dep)} = {_money(remaining)}. "
            f"Max depreciation = {_money(remaining)} − R1 = {_money(correct_dep)}"
        ),
    )


def _gen_csr_ethics(r: random.Random):
    scenarios = [
        {
            "prompt": (
                "The CEO wants to donate old computers to a local school. "
                "The shareholders feel the computers should be sold at a profit. "
                "Explain TWO points the CEO can use to support the donation."
            ),
            "answer": (
                "1. The donation fulfils CSR obligations (corporate social responsibility / King Code). "
                "2. It promotes the company's image and attracts more customers through goodwill. "
                "3. It is a tax-deductible donation. "
                "4. The assets may be nearly fully depreciated with minimal resale value."
            ),
            "rubric": [
                "CSR/King Code compliance",
                "Good publicity/corporate image",
                "Tax deductibility or low residual value",
            ],
        },
        {
            "prompt": (
                "An employee used a company vehicle for personal errands without permission "
                "and was involved in an accident. The insurance company refused the claim. "
                "Who should bear the cost? Give TWO reasons."
            ),
            "answer": (
                "The employee should bear the cost because: "
                "1. They used the vehicle without authorisation — a breach of company policy. "
                "2. The business should not carry losses from unauthorised personal use. "
                "3. Insurance was voided due to the employee's actions."
            ),
            "rubric": [
                "Employee liability for unauthorised use",
                "Business should not bear loss from personal misuse",
            ],
        },
    ]
    chosen = r.choice(scenarios)
    co = r.choice(_COMPANIES)
    return _make_typed(
        prompt=f"{co}: {chosen['prompt']}",
        sample_answer=chosen["answer"],
        grading_rubric=chosen["rubric"],
    )


def _gen_internal_control(r: random.Random):
    return _make_typed(
        prompt="Suggest TWO internal control measures that a company should implement for fixed assets.",
        sample_answer=(
            "1. Maintain a detailed asset register and reconcile it to physical assets regularly. "
            "2. Keep vehicle keys in a secure location with authorised personnel only. "
            "3. Install tracker systems on vehicles. "
            "4. Use log books to track asset usage."
        ),
        grading_rubric=[
            "Asset register / physical verification",
            "Security measures (keys, trackers, log books)",
        ],
    )


def _gen_gaap_principles_mcq(r: random.Random):
    questions = [
        {
            "prompt": "According to the historical cost principle (GAAP), fixed assets must be recorded at:",
            "options": [
                "The original cost price including acquisition costs",
                "The current market value",
                "The replacement value",
                "The insured value",
            ],
            "correct": 0,
            "explanation": "GAAP's historical cost principle requires assets to be recorded at their original purchase price.",
        },
        {
            "prompt": "The minimum carrying value of a fixed asset in the financial statements is:",
            "options": ["R1", "R0", "10% of cost", "Scrap value"],
            "correct": 0,
            "explanation": "A fixed asset can never be recorded at R0. The minimum carrying value is R1.",
        },
        {
            "prompt": "When a fixed asset is purchased mid-year, depreciation should be:",
            "options": [
                "Calculated for the number of months the asset was owned",
                "Calculated for the full year regardless",
                "Not calculated until the next financial year",
                "Calculated at half the annual rate",
            ],
            "correct": 0,
            "explanation": "Depreciation is calculated proportionally for the months the asset was in the business's possession.",
        },
    ]
    chosen = r.choice(questions)
    return _make_mcq(
        prompt=chosen["prompt"], options=chosen["options"],
        correct_index=chosen["correct"], explanation=chosen["explanation"],
    )


def _gen_additional_dep_on_sale(r: random.Random):
    co = r.choice(_COMPANIES)
    asset = r.choice(["vehicle", "delivery van"])
    carrying_start = _rm(r.choice([80, 100, 120, 150, 170]) * 1000)
    rate = 20
    sale_month = r.choice([3, 6, 9])
    add_dep = _rm(carrying_start * rate / 100 * sale_month / 12)
    cv_at_sale = _rm(carrying_start - add_dep)

    return _make_calc(
        prompt=(
            f"A {asset} at {co} with a carrying value of {_money(carrying_start)} "
            f"at the start of the year was sold {sale_month} months into the financial year. "
            f"Depreciation: {rate}% p.a. on diminishing balance. "
            f"Calculate the additional depreciation up to the date of sale."
        ),
        correct_answer=add_dep, unit="R",
        working_formula=(
            f"{rate}% × {_money(carrying_start)} × {sale_month}/12 = {_money(add_dep)}"
        ),
    )


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

_GENERATORS = [
    _gen_depreciation_straight_line,
    _gen_depreciation_diminishing,
    _gen_disposal_profit_loss,
    _gen_cost_price_backcalc,
    _gen_trade_in_value,
    _gen_total_depreciation,
    _gen_fully_depreciated,
    _gen_csr_ethics,
    _gen_internal_control,
    _gen_gaap_principles_mcq,
    _gen_additional_dep_on_sale,
]


def generate_questions(
    *, subskill="mixed", difficulty="easy", question_type="mixed",
    count=1, seed=None, mode="",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions = []
    for _ in range(count):
        q = r.choice(_GENERATORS)(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)
    return questions
