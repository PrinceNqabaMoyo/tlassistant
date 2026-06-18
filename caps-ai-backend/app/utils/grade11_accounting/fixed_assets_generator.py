from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ..sole_trader.journal_question import make_journal as _make_journal
from ..sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ..sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, mode: str, archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_fixed_assets_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "expected_answer_type": "mcq",
        "guidelines": [explanation],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold":
        out["explanation"] = explanation
    return out


def _make_calc(*, prompt: str, correct_value: float, unit: str = "", explanation: str = "", working_formula: str = "", mode: str = "", archetype_key: str = "", rubric: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_fixed_assets_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(_round_money(correct_value)),
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "guidelines": [f"Formula: {working_formula}"] if working_formula else [],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold" and str(explanation).strip():
        out["explanation"] = explanation
    if rubric:
        out["rubric"] = rubric
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str, archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_fixed_assets_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
        "guidelines": [f"Sample expected answer: {sample_answer}"],
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold":
        out["sample_answer"] = sample_answer
    return out


def _make_bundle(*, prompt: str, parts: List[Dict[str, Any]], archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct11_fixed_assets_bundle"),
        "question_type": "bundle",
        "prompt": prompt,
        "parts": parts,
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _mk_journal(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
    force_editable_cols: Optional[List[int]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    show_answers = mode_norm == "scaffold"

    if force_editable_cols is not None:
        editable_cols = [int(c) for c in force_editable_cols]
    else:
        editable_cols = _journal_editable_cols_by_difficulty(
            difficulty=diff,
            base_editable_cols=base_editable_cols,
            total_cols=len(headers),
            mode=mode_norm,
        )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}

    for rix, vals in enumerate(values_rows):
        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct row labels and structure.",
            "Show depreciation calculations where required.",
            "If an asset is fully depreciated, the minimum carrying value is R1.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        cell_hints=cell_hints if mode_norm == "scaffold" and cell_hints else None,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_fixed_assets_journal")
    return out


def _pick(r: random.Random, xs: List[Any]) -> Any:
    return xs[int(r.randrange(0, len(xs)))]


def _make_asset_register_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q8.2 style: complete fixed asset register for a vehicle sold.
    business = r.choice(["Goody Shoe Traders", "Good Place Traders", "Majoki Transport"])
    cost = float(r.choice([320_000, 300_000, 120_000]))
    rate = float(r.choice([10.0, 15.0, 20.0, 25.0]))
    months = int(r.choice([6, 9, 10]))

    dep_year1 = _round_money(cost * (rate / 100.0) * 0.5)  # simple starter
    acc1 = dep_year1
    cv1 = _round_money(cost - acc1)

    dep_year2 = _round_money(cv1 * (rate / 100.0))
    acc2 = _round_money(acc1 + dep_year2)
    cv2 = _round_money(cost - acc2)

    dep_pro = _round_money(cv2 * (rate / 100.0) * (months / 12.0))
    acc3 = _round_money(acc2 + dep_pro)
    cv3 = _round_money(cost - acc3)

    headers = ["Date", "Current depreciation", "Accumulated depreciation", "Carrying value", "Calculation"]
    rows: List[List[Optional[str]]] = [
        ["31 Dec 2021", f"{dep_year1:.2f}", f"{acc1:.2f}", f"{cv1:.2f}", ""],
        ["31 Dec 2022", f"{dep_year2:.2f}", f"{acc2:.2f}", f"{cv2:.2f}", f"{cv1:.2f} × {rate:.0f}%"],
        ["1 Jul 2023", f"{dep_pro:.2f}", f"{acc3:.2f}", f"{cv3:.2f}", f"{cv2:.2f} × {rate:.0f}% × {months}/12"],
    ]

    prompt = f"""{business}

#### REQUIRED:
Complete the Fixed Asset Register for the vehicle sold.

#### INFORMATION:
Cost price: R{cost:,.0f}. Depreciation is {rate:.0f}% p.a. on carrying value. The asset was disposed after {months} months in the current year."""

    reg_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        reg_hints["t0_r0_c1"] = f"Year 1 depreciation (pro-rata half year): Cost × {rate:.0f}% × 0.5 = {cost:,.0f} × {rate/100:.2f} × 0.5."
        reg_hints["t0_r0_c2"] = "Accumulated depreciation = sum of all depreciation to date."
        reg_hints["t0_r0_c3"] = "Carrying value = Cost − Accumulated depreciation."
        reg_hints["t0_r1_c1"] = f"Year 2 depreciation on diminishing balance: Previous CV × {rate:.0f}%."
        reg_hints["t0_r1_c2"] = "Accumulated depreciation = previous accumulated + current year depreciation."
        reg_hints["t0_r1_c3"] = "Carrying value = Cost − Accumulated depreciation."
        reg_hints["t0_r1_c4"] = f"Calculation: {cv1:.2f} × {rate:.0f}%."
        reg_hints["t0_r2_c1"] = f"Pro-rata depreciation: CV × {rate:.0f}% × {months}/12."
        reg_hints["t0_r2_c2"] = "Accumulated depreciation up to disposal date."
        reg_hints["t0_r2_c3"] = "Carrying value at disposal date = Cost − Accumulated depreciation."
        reg_hints["t0_r2_c4"] = f"Calculation: {cv2:.2f} × {rate:.0f}% × {months}/12."

    # ── Build rubric_map (per-cell marking metadata) ──
    rubric_map: Dict[str, Dict[str, Any]] = {
        # Row 0: Year 1 depreciation (simple starter: cost × rate × 0.5)
        "t0_r0_c1": {
            "formula_structure": f"Depreciation Year 1 = Cost × {rate:.0f}% × 6/12",
            "foundational_values": [cost, rate / 100, 0.5],
            "operations": ["×", "×"],
            "max_score": 2.0,
        },
        "t0_r0_c2": {
            "formula_structure": "Accumulated depreciation = Current depreciation (first year)",
            "foundational_values": [dep_year1],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r0_c3": {
            "formula_structure": "Carrying value = Cost − Accumulated depreciation",
            "foundational_values": [cost, acc1],
            "operations": ["−"],
            "max_score": 1.5,
        },
        # Row 1: Year 2 depreciation on diminishing balance
        "t0_r1_c1": {
            "formula_structure": f"Depreciation Year 2 = Previous Carrying Value × {rate:.0f}%",
            "foundational_values": [cv1, rate / 100],
            "operations": ["×"],
            "max_score": 1.5,
        },
        "t0_r1_c2": {
            "formula_structure": "Accumulated depreciation = Previous accumulated + Current depreciation",
            "foundational_values": [acc1, dep_year2],
            "operations": ["+"],
            "max_score": 1.5,
        },
        "t0_r1_c3": {
            "formula_structure": "Carrying value = Cost − Accumulated depreciation",
            "foundational_values": [cost, acc2],
            "operations": ["−"],
            "max_score": 1.5,
        },
        # Row 2: Pro-rata depreciation
        "t0_r2_c1": {
            "formula_structure": f"Pro-rata depreciation = Carrying Value × {rate:.0f}% × {months}/12",
            "foundational_values": [cv2, rate / 100, months, 12],
            "operations": ["×", "×", "/"],
            "max_score": 3.0,
        },
        "t0_r2_c2": {
            "formula_structure": "Accumulated depreciation = Previous accumulated + Pro-rata depreciation",
            "foundational_values": [acc2, dep_pro],
            "operations": ["+"],
            "max_score": 1.5,
        },
        "t0_r2_c3": {
            "formula_structure": "Carrying value = Cost − Accumulated depreciation",
            "foundational_values": [cost, acc3],
            "operations": ["−"],
            "max_score": 1.5,
        },
    }

    # ── Build dependency_map (for consequential marking) ──
    dependency_map: Dict[str, List[str]] = {
        "t0_r0_c2": ["t0_r0_c1"],                     # acc1 depends on dep_year1
        "t0_r0_c3": ["t0_r0_c2"],                     # cv1 depends on acc1
        "t0_r1_c1": ["t0_r0_c3"],                     # dep_year2 depends on cv1
        "t0_r1_c2": ["t0_r0_c2", "t0_r1_c1"],         # acc2 depends on acc1 + dep_year2
        "t0_r1_c3": ["t0_r1_c2"],                     # cv2 depends on acc2
        "t0_r2_c1": ["t0_r1_c3"],                     # dep_pro depends on cv2
        "t0_r2_c2": ["t0_r1_c2", "t0_r2_c1"],         # acc3 depends on acc2 + dep_pro
        "t0_r2_c3": ["t0_r2_c2"],                     # cv3 depends on acc3
    }

    q = _mk_journal(
        prompt=prompt,
        journal_type="asset_register",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2, 3, 4],
        cell_hints=reg_hints,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    q["meta"] = {"archetype_key": "g11_fixed_assets_asset_register"}
    return q


def _make_fixed_assets_note_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    business = r.choice(["Good Place Traders", "Sandi Brothers", "Alabama Traders"])
    year_end = r.choice(["28 February 2023", "31 December 2021", "30 June 2022"])

    # VEHICLES: Diminishing balance. One new vehicle bought during the year. No disposals.
    veh_cost_start = float(r.choice([800_000, 1_200_000, 1_500_000]))
    veh_acc_start = _round_money(veh_cost_start * r.choice([0.3, 0.4, 0.5]))
    veh_rate = r.choice([15, 20])

    veh_add_cost = float(r.choice([200_000, 350_000]))
    veh_add_months = r.choice([6, 9])
    veh_add_date = "1 September 2022" if veh_add_months == 6 else "1 June 2022"

    veh_dep_old = _round_money((veh_cost_start - veh_acc_start) * (veh_rate / 100))
    veh_dep_new = _round_money(veh_add_cost * (veh_rate / 100) * (veh_add_months / 12))
    veh_dep_total = _round_money(veh_dep_old + veh_dep_new)

    veh_cv_start = _round_money(veh_cost_start - veh_acc_start)
    veh_cv_end = _round_money(veh_cv_start + veh_add_cost - veh_dep_total)
    veh_cost_end = _round_money(veh_cost_start + veh_add_cost)
    veh_acc_end = _round_money(veh_acc_start + veh_dep_total)

    # EQUIPMENT: Straight line. One old equipment disposed partway through year. No additions.
    eq_cost_start = float(r.choice([500_000, 750_000, 900_000]))
    eq_rate = r.choice([10, 20])
    eq_acc_start = _round_money(eq_cost_start * r.choice([0.2, 0.3, 0.4]))

    eq_disp_cost = float(r.choice([50_000, 100_000]))
    eq_disp_acc_start = _round_money(eq_disp_cost * r.choice([0.2, 0.3, 0.4]))
    eq_disp_date = "31 December 2022"
    eq_disp_months = 10

    eq_dep_old_retained = _round_money((eq_cost_start - eq_disp_cost) * (eq_rate / 100))
    eq_dep_disp = _round_money(eq_disp_cost * (eq_rate / 100) * (eq_disp_months / 12))
    eq_dep_total = _round_money(eq_dep_old_retained + eq_dep_disp)

    eq_disp_acc_total = _round_money(eq_disp_acc_start + eq_dep_disp)
    eq_disp_cv = _round_money(eq_disp_cost - eq_disp_acc_total)

    eq_cv_start = _round_money(eq_cost_start - eq_acc_start)
    eq_cv_end = _round_money(eq_cv_start - eq_disp_cv - eq_dep_total)
    eq_cost_end = _round_money(eq_cost_start - eq_disp_cost)
    eq_acc_end = _round_money(eq_acc_start + eq_dep_total - eq_disp_acc_total)

    headers = ["", "Vehicles", "Equipment"]
    rows: List[List[Optional[str]]] = [
        ["Carrying value at beginning of year", f"{veh_cv_start:.2f}", f"{eq_cv_start:.2f}"],
        ["Cost", f"{veh_cost_start:.2f}", f"{eq_cost_start:.2f}"],
        ["Accumulated depreciation", f"({veh_acc_start:.2f})", f"({eq_acc_start:.2f})"],
        ["Movements", "", ""],
        ["Additions at cost", f"{veh_add_cost:.2f}", "0.00"],
        ["Disposals at carrying value", "0.00", f"({eq_disp_cv:.2f})"],
        ["Depreciation", f"({veh_dep_total:.2f})", f"({eq_dep_total:.2f})"],
        ["Carrying value at end of year", f"{veh_cv_end:.2f}", f"{eq_cv_end:.2f}"],
        ["Cost", f"{veh_cost_end:.2f}", f"{eq_cost_end:.2f}"],
        ["Accumulated depreciation", f"({veh_acc_end:.2f})", f"({eq_acc_end:.2f})"],
    ]

    info_lines = [
        f"Balances at 1 March 2022:",
        f"- Vehicles (Cost): R{veh_cost_start:,.0f}",
        f"- Vehicles (Accumulated depreciation): R{veh_acc_start:,.0f}",
        f"- Equipment (Cost): R{eq_cost_start:,.0f}",
        f"- Equipment (Accumulated depreciation): R{eq_acc_start:,.0f}",
        "",
        "Transactions and depreciation policies:",
        f"- Vehicles are depreciated at {veh_rate}% p.a. on the diminishing balance method.",
        f"- Equipment is depreciated at {eq_rate}% p.a. on cost (straight line).",
        f"- A new vehicle was purchased on {veh_add_date} for R{veh_add_cost:,.0f}.",
        f"- Equipment originally costing R{eq_disp_cost:,.0f} with an accumulated depreciation of R{eq_disp_acc_start:,.0f} on 1 March 2022, was sold on {eq_disp_date}."
    ]

    prompt = f"""{business}

#### REQUIRED:
Complete the Fixed/Tangible Assets Note to the Financial Statements for the year ended {year_end}.
Calculate all depreciation amounts and carrying values based on the transactions provided.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    note_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        note_hints["t0_r0_c1"] = f"CV at beginning = Cost − Acc dep = {veh_cost_start:,.0f} − {veh_acc_start:,.0f}."
        note_hints["t0_r0_c2"] = f"CV at beginning = Cost − Acc dep = {eq_cost_start:,.0f} − {eq_acc_start:,.0f}."
        note_hints["t0_r1_c1"] = "Cost price of vehicles at beginning of year."
        note_hints["t0_r1_c2"] = "Cost price of equipment at beginning of year."
        note_hints["t0_r2_c1"] = "Accumulated depreciation on vehicles (show in brackets)."
        note_hints["t0_r2_c2"] = "Accumulated depreciation on equipment (show in brackets)."
        note_hints["t0_r4_c1"] = f"Additions at cost: new vehicle purchased = {veh_add_cost:,.0f}."
        note_hints["t0_r4_c2"] = "No additions for equipment."
        note_hints["t0_r5_c1"] = "No disposals for vehicles."
        note_hints["t0_r5_c2"] = f"Disposal CV = Cost ({eq_disp_cost:,.0f}) - Acc Dep at start ({eq_disp_acc_start:,.0f}) - Dep for year ({eq_dep_disp:,.0f})"
        note_hints["t0_r6_c1"] = f"Depreciation Vehicles = (Old: {veh_cv_start:,.0f} * {veh_rate}%) + (New: {veh_add_cost:,.0f} * {veh_rate}% * {veh_add_months}/12)"
        note_hints["t0_r6_c2"] = f"Depreciation Equipment = (Retained: {eq_cost_start - eq_disp_cost:,.0f} * {eq_rate}%) + (Disposed: {eq_disp_cost:,.0f} * {eq_rate}% * {eq_disp_months}/12)"
        note_hints["t0_r7_c1"] = "CV at end = CV beginning + Additions − Disposals − Depreciation."
        note_hints["t0_r7_c2"] = "CV at end = CV beginning + Additions − Disposals − Depreciation."
        note_hints["t0_r8_c1"] = f"Cost at end = Opening cost + Additions = {veh_cost_start:,.0f} + {veh_add_cost:,.0f}."
        note_hints["t0_r8_c2"] = f"Cost at end = Opening cost - Disposals = {eq_cost_start:,.0f} - {eq_disp_cost:,.0f}."
        note_hints["t0_r9_c1"] = f"Acc dep at end = Opening acc dep + Depreciation."
        note_hints["t0_r9_c2"] = f"Acc dep at end = Opening acc dep - Acc dep of disposed + Depreciation."

    # Build rubric_map
    rubric_map: Dict[str, Dict[str, Any]] = {
        "t0_r6_c1": {
            "formula_structure": "Total Depreciation = Old + New",
            "foundational_values": [veh_dep_old, veh_dep_new],
            "operations": ["+"],
            "max_score": 3.0,
        },
        "t0_r6_c2": {
            "formula_structure": "Total Depreciation = Retained + Disposed",
            "foundational_values": [eq_dep_old_retained, eq_dep_disp],
            "operations": ["+"],
            "max_score": 3.0,
        },
        "t0_r0_c1": {
            "formula_structure": "CV at beginning = Cost − Accumulated depreciation",
            "foundational_values": [veh_cost_start, veh_acc_start],
            "operations": ["−"],
            "max_score": 1.5,
        },
        "t0_r0_c2": {
            "formula_structure": "CV at beginning = Cost − Accumulated depreciation",
            "foundational_values": [eq_cost_start, eq_acc_start],
            "operations": ["−"],
            "max_score": 1.5,
        },
        "t0_r7_c1": {
            "formula_structure": "CV at end = CV beginning + Additions − Depreciation",
            "foundational_values": [veh_cv_start, veh_add_cost, veh_dep_total],
            "operations": ["+", "−"],
            "max_score": 2.0,
        },
        "t0_r7_c2": {
            "formula_structure": "CV at end = CV beginning − Disposals − Depreciation",
            "foundational_values": [eq_cv_start, eq_disp_cv, eq_dep_total],
            "operations": ["−", "−"],
            "max_score": 2.0,
        },
    }

    dependency_map: Dict[str, List[str]] = {
        "t0_r7_c1": ["t0_r0_c1", "t0_r4_c1", "t0_r6_c1"],
        "t0_r7_c2": ["t0_r0_c2", "t0_r5_c2", "t0_r6_c2"],
        "t0_r9_c1": ["t0_r2_c1", "t0_r6_c1"],
        "t0_r9_c2": ["t0_r2_c2", "t0_r6_c2", "t0_r5_c2"],
    }

    q = _mk_journal(
        prompt=prompt,
        journal_type="fixed_assets_note",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        cell_hints=note_hints,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    q["meta"] = {"archetype_key": "g11_fixed_assets_note"}
    return q


def _make_asset_disposal_account_question(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    # Mirrors Q2/Q11: asset disposal ledger account.
    business = r.choice(["Ratiza Traders", "Makume Stores", "Majoki Transport"])
    cost = float(r.choice([120_000, 132_000, 300_000]))
    acc = float(r.choice([50_880, 31_317, 281_250]))
    proceeds = float(r.choice([25_000, 81_348, 15_000, 31_500]))
    loss = _round_money(max(0.0, (cost - acc) - proceeds))

    headers = ["Date", "Details", "Fol.", "Amount", "Date", "Details", "Fol.", "Amount"]
    rows: List[List[Optional[str]]] = [
        ["", "Asset", "GJ", f"{cost:.2f}", "", "Accumulated depreciation", "GJ", f"{acc:.2f}"],
        ["", "", "", "", "", "Bank/Drawings", "", f"{proceeds:.2f}"],
        ["", "", "", "", "", "Loss on sale of asset", "GJ", f"{loss:.2f}"],
        ["", "Totals", "", f"{cost:.2f}", "", "Totals", "", f"{cost:.2f}"],
    ]

    info_lines = [
        f"- Original cost price of the asset sold: R{cost:,.2f}",
        f"- Accumulated depreciation on the asset to date of sale: R{acc:,.2f}",
        f"- Cash proceeds received from the sale: R{proceeds:,.2f}"
    ]

    prompt = f"""{business}

#### REQUIRED:
Prepare the Asset Disposal account in the General Ledger.

#### INFORMATION:
{chr(10).join(info_lines)}"""

    disp_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        disp_hints["t0_r0_c3"] = f"Debit: Transfer cost price of the asset = {cost:,.0f}."
        disp_hints["t0_r0_c7"] = f"Credit: Transfer accumulated depreciation = {acc:,.0f}."
        disp_hints["t0_r1_c7"] = f"Credit: Proceeds from sale (Bank/Drawings) = {proceeds:,.0f}."
        if loss > 0:
            disp_hints["t0_r2_c7"] = f"Credit: Loss on sale = CV − Proceeds = {cost - acc:,.0f} − {proceeds:,.0f} = {loss:,.0f}."
        else:
            profit_val = _round_money(proceeds - (cost - acc))
            disp_hints["t0_r2_c7"] = f"Credit: Profit on sale = Proceeds − CV = {proceeds:,.0f} − {cost - acc:,.0f} = {profit_val:,.0f}."
        disp_hints["t0_r3_c3"] = "Debit total must equal Credit total (balancing)."
        disp_hints["t0_r3_c7"] = "Credit total must equal Debit total (balancing)."

    cv = _round_money(cost - acc)
    # ── Build rubric_map ──
    rubric_map: Dict[str, Dict[str, Any]] = {
        "t0_r0_c3": {
            "formula_structure": "Debit: Cost price of asset",
            "foundational_values": [cost],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r0_c7": {
            "formula_structure": "Credit: Accumulated depreciation",
            "foundational_values": [acc],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r1_c7": {
            "formula_structure": "Credit: Proceeds from sale",
            "foundational_values": [proceeds],
            "operations": [],
            "max_score": 1.0,
        },
        "t0_r2_c7": {
            "formula_structure": "Loss/Profit = Carrying Value − Proceeds = (Cost − Acc dep) − Proceeds",
            "foundational_values": [cv, proceeds],
            "operations": ["−"],
            "max_score": 1.5,
        },
    }

    dependency_map: Dict[str, List[str]] = {
        "t0_r2_c7": ["t0_r0_c3", "t0_r0_c7", "t0_r1_c7"],
        "t0_r3_c3": ["t0_r0_c3"],
        "t0_r3_c7": ["t0_r0_c7", "t0_r1_c7", "t0_r2_c7"],
    }

    q = _mk_journal(
        prompt=prompt,
        journal_type="asset_disposal",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[3, 7],
        force_editable_cols=[3, 7],
        cell_hints=disp_hints,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    q["meta"] = {"archetype_key": "g11_fixed_assets_asset_disposal_account"}
    return q


def _make_fixed_assets_ethics_internal_control_typed(*, r: random.Random, mode: str) -> Dict[str, Any]:
    # Mirrors Q11.2 / ethics-style response.
    business = r.choice(["Makume Stores", "Malusi's Delivery Services"])
    prompt = f"""{business}

#### REQUIRED:
Explain the consequences of an owner/partner disposing of a fixed asset without proper authorisation (ethical issue).

#### INFORMATION:
A partner took a delivery vehicle for personal use and disposed of it without informing the other partners."""

    sample = (
        "It is unethical to dispose of partnership assets without consent of the other partner(s).\n"
        "The partner may be required to repay the difference between fair value and the amount paid.\n"
        "The loss can be charged against the partner's current account.\n"
        "The partner could face legal action and will be held accountable for losses suffered by the partnership."
    )
    return _make_typed(prompt=prompt, sample_answer=sample, mode=mode, archetype_key="g11_fixed_assets_ethics_typed")


def _straight_line_dep(*, cost: float, rate_pct: float, months: int) -> float:
    return _round_money(cost * (rate_pct / 100.0) * (months / 12.0))


def _diminishing_balance_dep(*, carrying_value: float, rate_pct: float, months: int) -> float:
    return _round_money(carrying_value * (rate_pct / 100.0) * (months / 12.0))


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    concept_pool: List[Dict[str, Any]] = []
    straight_pool: List[Dict[str, Any]] = []
    diminishing_pool: List[Dict[str, Any]] = []
    carrying_value_pool: List[Dict[str, Any]] = []
    disposal_pool: List[Dict[str, Any]] = []
    journal_pool: List[Dict[str, Any]] = []
    bundle_pool: List[Dict[str, Any]] = []
    typed_pool: List[Dict[str, Any]] = []

    concept_pool.append(
        _make_mcq(
            prompt="Which statement best describes depreciation?",
            options=[
                "An increase in the market value of an asset.",
                "The allocation of the cost of an asset over its useful life.",
                "A method of valuing stock.",
                "Money received when an asset is sold.",
            ],
            correct_index=1,
            explanation="Depreciation is the allocation of the value/cost of an asset over its useful life.",
            mode=mode_norm,
            archetype_key="g11_fixed_assets_concepts_depreciation_mcq",
        )
    )

    # Straight line (fixed percentage on cost)
    cost = float(_pick(r, [8000, 12000, 20000, 70000, 120000, 200000]))
    rate = float(_pick(r, [10.0, 15.0, 20.0, 25.0]))
    months = int(_pick(r, [12, 12, 12, 6, 9]))
    dep_sl = _straight_line_dep(cost=cost, rate_pct=rate, months=months)
    straight_pool.append(
        _make_calc(
            prompt=(
                f"A fixed asset was purchased for R{cost:,.0f}. Depreciation is written off at {rate:.0f}% p.a. on cost (straight line). "
                f"Calculate the depreciation for {months} months."
            ),
            correct_value=dep_sl,
            unit="R",
            explanation=f"Depreciation = Cost × Rate% × (months/12) = {cost:,.0f} × {rate:.0f}% × ({months}/12) = R{dep_sl:,.2f}.",
            working_formula="Depreciation = Cost price × Rate% × (months/12)",
            mode=mode_norm,
            archetype_key="g11_fixed_assets_depreciation_straight_calc",
            rubric={
                "formula_structure": f"Depreciation = Cost × {rate:.0f}% × ({months}/12)",
                "foundational_values": [cost, rate / 100, months, 12.0],
                "operations": ["×", "×", "/"],
                "max_score": 3.0,
            },
        )
    )

    # Diminishing balance (percentage on carrying value)
    cost2 = float(_pick(r, [70000, 120000, 200000, 350000]))
    acc_dep = float(_pick(r, [15000, 46000, 60000, 120000]))
    if acc_dep >= cost2:
        acc_dep = _round_money(cost2 * 0.4)
    carrying_start = _round_money(cost2 - acc_dep)
    rate2 = float(_pick(r, [10.0, 15.0, 20.0]))
    months2 = int(_pick(r, [12, 12, 6, 9]))
    dep_db = _diminishing_balance_dep(carrying_value=carrying_start, rate_pct=rate2, months=months2)
    diminishing_pool.append(
        _make_calc(
            prompt=(
                f"A vehicle has cost price R{cost2:,.0f} and accumulated depreciation R{acc_dep:,.0f} at the start of the year. "
                f"It is depreciated at {rate2:.0f}% p.a. on carrying value (diminishing balance). "
                f"Calculate depreciation for {months2} months."
            ),
            correct_value=dep_db,
            unit="R",
            explanation=(
                f"Carrying value = Cost - Acc dep = {cost2:,.0f} - {acc_dep:,.0f} = {carrying_start:,.2f}. "
                f"Depreciation = Carrying value × Rate% × (months/12) = {carrying_start:,.2f} × {rate2:.0f}% × ({months2}/12) = R{dep_db:,.2f}."
            ),
            working_formula="Depreciation = (Cost - Accumulated depreciation) × Rate% × (months/12)",
            mode=mode_norm,
            archetype_key="g11_fixed_assets_depreciation_diminishing_calc",
            rubric={
                "formula_structure": f"Depreciation = (Cost − Acc dep) × {rate2:.0f}% × ({months2}/12)",
                "foundational_values": [cost2, acc_dep, rate2 / 100, months2, 12.0],
                "operations": ["−", "×", "×", "/"],
                "max_score": 3.5,
            },
        )
    )

    # Carrying value
    cost3 = float(_pick(r, [8000, 120000, 200000, 350000]))
    acc3 = float(_pick(r, [2000, 3000, 46000, 150000]))
    if acc3 >= cost3:
        acc3 = _round_money(cost3 * 0.5)
    cv = _round_money(cost3 - acc3)
    carrying_value_pool.append(
        _make_calc(
            prompt=f"Calculate the carrying value if cost price is R{cost3:,.0f} and accumulated depreciation is R{acc3:,.0f}.",
            correct_value=cv,
            unit="R",
            explanation=f"Carrying value = Cost price - Accumulated depreciation = {cost3:,.0f} - {acc3:,.0f} = R{cv:,.2f}.",
            working_formula="Carrying value = Cost price - Accumulated depreciation",
            mode=mode_norm,
            archetype_key="g11_fixed_assets_carrying_value_calc",
            rubric={
                "formula_structure": "Carrying value = Cost price − Accumulated depreciation",
                "foundational_values": [cost3, acc3],
                "operations": ["−"],
                "max_score": 1.5,
            },
        )
    )

    # Disposal profit/loss
    cost4 = float(_pick(r, [8000, 70000, 120000]))
    acc4 = float(_pick(r, [2000, 30000, 46000]))
    if acc4 >= cost4:
        acc4 = _round_money(cost4 * 0.6)
    cv4 = _round_money(cost4 - acc4)
    sold_for = float(_pick(r, [7000, 22000, 50000, 90000]))
    if sold_for <= 0:
        sold_for = _round_money(cv4 * 1.1)

    profit = _round_money(sold_for - cv4)
    label = "profit" if profit >= 0 else "loss"
    disposal_pool.append(
        _make_calc(
            prompt=(
                f"An asset has cost price R{cost4:,.0f} and accumulated depreciation R{acc4:,.0f}. "
                f"It is sold for R{sold_for:,.0f}. Calculate the {label} on disposal."
            ),
            correct_value=abs(profit),
            unit="R",
            explanation=(
                f"Carrying value = {cost4:,.0f} - {acc4:,.0f} = R{cv4:,.2f}. "
                f"{label.title()} = Selling price - Carrying value = {sold_for:,.0f} - {cv4:,.2f} = R{profit:,.2f}."
            ),
            working_formula=f"{label.title()} on sale = Proceeds - Carrying value",
            mode=mode_norm,
            archetype_key="g11_fixed_assets_profit_loss_disposal_calc",
            rubric={
                "formula_structure": f"{label.title()} on sale = Proceeds − (Cost − Accumulated depreciation)",
                "foundational_values": [sold_for, cost4, acc4],
                "operations": ["−", "−"],
                "max_score": 2.0,
            },
        )
    )

    # Doc-faithful table/ledger/typed archetypes
    journal_pool.append(_make_asset_register_question(r=r, difficulty=difficulty, mode=mode_norm))
    journal_pool.append(_make_asset_disposal_account_question(r=r, difficulty=difficulty, mode=mode_norm))
    journal_pool.append(_make_fixed_assets_note_question(r=r, difficulty=difficulty, mode=mode_norm))
    typed_pool.append(_make_fixed_assets_ethics_internal_control_typed(r=r, mode=mode_norm))

    # Bundle: register + disposal + note + ethics
    bundle_pool.append(
        _make_bundle(
            prompt="Fixed/Tangible Assets\n\nComplete all parts.",
            parts=[
                _make_asset_register_question(r=r, difficulty=difficulty, mode=mode_norm),
                _make_asset_disposal_account_question(r=r, difficulty=difficulty, mode=mode_norm),
                _make_fixed_assets_note_question(r=r, difficulty=difficulty, mode=mode_norm),
                _make_fixed_assets_ethics_internal_control_typed(r=r, mode=mode_norm),
            ],
            archetype_key="g11_fixed_assets_full_bundle",
        )
    )

    pools = {
        "concepts": concept_pool,
        "depreciation_straight": straight_pool,
        "straight": straight_pool,
        "depreciation_diminishing": diminishing_pool,
        "diminishing": diminishing_pool,
        "carrying_value": carrying_value_pool,
        "disposal": disposal_pool,
        "asset_register": journal_pool,
        "note": journal_pool,
        "ledger": journal_pool,
        "bundle": bundle_pool,
        "typed": typed_pool,
        "mixed": concept_pool + straight_pool + diminishing_pool + carrying_value_pool + disposal_pool + journal_pool + bundle_pool + typed_pool,
    }

    pool = pools.get(subskill_norm, pools["mixed"])

    if qtype_norm != "mixed":
        pool = [q for q in pool if str(q.get("question_type") or "").strip().lower() == qtype_norm]

    if not pool:
        pool = pools["mixed"]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out
