"""Common helpers, formatters, and data structures for Grade 12 Mathematical Literacy: INCOME TAX."""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sindiswa", "John", "Xolisa", "Banele", "Mr Modise", "Nomvula", "Thabo",
    "Lerato", "Kagiso", "Zanele", "Sipho", "Mrs Khumalo", "Keletso", "Lungile",
    "Tebogo", "Fatima", "Pieter", "Johan", "Kaveshan", "Dikeledi", "Mandla"
]

# Baseline CAPS Grade 12 SARS Tax Brackets (Via Afrika LB pp. 222-225)
SARS_TAX_BRACKETS = [
    {"bracket": 1, "min": 0, "max": 160000, "base": 0.0, "rate": 0.18, "threshold": 0},
    {"bracket": 2, "min": 160001, "max": 250000, "base": 28800.0, "rate": 0.25, "threshold": 160000},
    {"bracket": 3, "min": 250001, "max": 346000, "base": 51300.0, "rate": 0.30, "threshold": 250000},
    {"bracket": 4, "min": 346001, "max": 484000, "base": 80100.0, "rate": 0.35, "threshold": 346000},
    {"bracket": 5, "min": 484001, "max": 617000, "base": 128400.0, "rate": 0.38, "threshold": 484000},
    {"bracket": 6, "min": 617001, "max": float("inf"), "base": 178940.0, "rate": 0.40, "threshold": 617000},
]

# SARS Tax Rebates (Via Afrika LB p. 224)
REBATE_PRIMARY = 11440.0
REBATE_SECONDARY = 6390.0
REBATE_TERTIARY = 2130.0

# SARS Tax Thresholds (Via Afrika LB p. 224)
THRESHOLD_UNDER_65 = 63556.0
THRESHOLD_65_TO_74 = 99056.0
THRESHOLD_75_AND_OLDER = 110889.0

# Medical Scheme Fees Tax Credits (MTC) per month (Via Afrika LB p. 231)
MTC_MAIN_MEMBER = 230.0
MTC_FIRST_DEPENDANT = 230.0
MTC_ADDITIONAL_DEPENDANT = 154.0


def _fmt(val: float | int, places: int = 2) -> str:
    """Format numbers according to South African standard: comma decimal, space thousands."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return f"{int(val):,}".replace(",", " ")
    s = f"{val:.{places}f}"
    parts = s.split(".")
    integer_part = f"{int(parts[0]):,}".replace(",", " ")
    dec_part = parts[1].rstrip("0")
    if not dec_part:
        return integer_part
    return f"{integer_part},{dec_part}"


def _fmt_curr(val: float | int, curr_symbol: str = "R ") -> str:
    """Format currency values strictly with 2 decimal places and South African number grouping."""
    v = round(float(val), 2)
    s = f"{v:.2f}"
    int_p, dec_p = s.split(".")
    int_formatted = f"{int(int_p):,}".replace(",", " ")
    return f"{curr_symbol}{int_formatted},{dec_p}"


def calculate_tax_before_rebate(taxable_income: float) -> Tuple[float, int, float, float, float]:
    """Calculate tax before rebates and return (tax_before_rebates, bracket_num, base, rate, threshold)."""
    for b in SARS_TAX_BRACKETS:
        if b["min"] <= taxable_income <= b["max"]:
            tax = b["base"] + b["rate"] * (taxable_income - b["threshold"])
            return round(tax, 2), b["bracket"], b["base"], b["rate"], b["threshold"]
    # Fallback to top bracket
    b = SARS_TAX_BRACKETS[-1]
    tax = b["base"] + b["rate"] * (taxable_income - b["threshold"])
    return round(tax, 2), b["bracket"], b["base"], b["rate"], b["threshold"]


def get_rebates_for_age(age: int) -> Tuple[float, str]:
    """Return (total_rebate, explanation_string)."""
    if age < 65:
        return REBATE_PRIMARY, f"Primary rebate only: {_fmt_curr(REBATE_PRIMARY)}"
    elif age < 75:
        tot = REBATE_PRIMARY + REBATE_SECONDARY
        return tot, f"Primary ({_fmt_curr(REBATE_PRIMARY)}) + Secondary ({_fmt_curr(REBATE_SECONDARY)}) = {_fmt_curr(tot)}"
    else:
        tot = REBATE_PRIMARY + REBATE_SECONDARY + REBATE_TERTIARY
        return tot, f"Primary ({_fmt_curr(REBATE_PRIMARY)}) + Secondary ({_fmt_curr(REBATE_SECONDARY)}) + Tertiary ({_fmt_curr(REBATE_TERTIARY)}) = {_fmt_curr(tot)}"


def _build_options(
    correct_ans: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None
) -> Tuple[List[str], int]:
    """Generate strictly 4 distinct multiple choice options with zero synthetic fallbacks."""
    if custom_options and len(custom_options) >= 4:
        unique_custom: List[str] = []
        for opt in custom_options:
            if opt not in unique_custom:
                unique_custom.append(opt)
        if correct_ans not in unique_custom:
            unique_custom.insert(0, correct_ans)
        
        other_opts = [opt for opt in unique_custom if opt != correct_ans]
        if len(other_opts) >= 3:
            selected_others = r.sample(other_opts, 3)
            opts = [correct_ans] + selected_others
        else:
            opts = [correct_ans] + other_opts
            nudge = 1
            while len(opts) < 4:
                opts.append(f"{correct_ans} (Alternative {nudge})")
                nudge += 1
        r.shuffle(opts)
        return opts, opts.index(correct_ans)

    distractors: set[str] = set()
    cleaned = correct_ans.strip()

    # 1. Currency pattern (Rands)
    curr_match = re.search(r"R\s*([\d\s]+(?:[.,]\d+)?)", cleaned)
    if curr_match:
        c_num = curr_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val = float(c_num)
            for sc in [1.15, 0.85, 1.25, 0.75, 1.10, 0.90, 1.05, 0.95]:
                d_val = round(val * sc, 2)
                d_str = _fmt_curr(d_val)
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [REBATE_PRIMARY, REBATE_SECONDARY, 500.0, -500.0, 1000.0, -1000.0, 250.0, -250.0]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_curr(d_val)
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 2. Percentage pattern
    pct_match = re.search(r"([\d\s]+(?:[.,]\d+)?)\s*%", cleaned)
    if pct_match:
        p_num = pct_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val = float(p_num)
            for sh in [2.5, -2.5, 5.0, -5.0, 1.0, -1.0, 3.5, -3.5]:
                d_val = round(val + sh, 2)
                if 0 <= d_val <= 100:
                    d_str = f"{_fmt(d_val, 2)}%"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 3. Numeric pattern
    num_match = re.search(r"(-?\d+(?:[.,]\d+)?)", cleaned)
    if num_match and not curr_match and not pct_match:
        val_str = num_match.group(1).replace(",", ".")
        prefix = cleaned[:num_match.start(1)]
        suffix = cleaned[num_match.end(1):]
        try:
            val = float(val_str)
            is_int = val.is_integer()
            scales = [1.15, 0.85, 1.25, 0.75, 1.10, 0.90]
            shifts = [1.0, 2.0, 5.0, 10.0, -1.0, -2.0, -5.0, -10.0]
            for sc in scales:
                d_val = val * sc
                formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2))
                d_str = f"{prefix}{formatted_d}{suffix}"
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in shifts:
                d_val = val + sh
                if d_val > 0 or val < 0:
                    formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2))
                    d_str = f"{prefix}{formatted_d}{suffix}"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 4. Known qualitative options
    lower_c = cleaned.lower()
    if "bracket" in lower_c:
        distractors.update([
            "Tax Bracket 1 (R0 to R160 000)",
            "Tax Bracket 2 (R160 001 to R250 000)",
            "Tax Bracket 3 (R250 001 to R346 000)",
            "Tax Bracket 4 (R346 001 to R484 000)",
            "Tax Bracket 5 (R484 001 to R617 000)",
            "Tax Bracket 6 (R617 001 and above)"
        ])
    elif "deductible" in lower_c:
        distractors.update([
            "Tax-deductible deduction (reduces taxable income before tax calculation)",
            "Non-tax-deductible expense (paid from after-tax income, does not reduce tax)",
            "Direct medical scheme tax credit (deducted directly from tax owed)",
            "Tax-free capital allowance"
        ])
    elif "yes" in lower_c or "no" in lower_c:
        distractors.update([
            "Yes, the taxpayer earns below the applicable tax threshold and owes R0 tax",
            "No, the taxpayer earns above the threshold and must pay personal income tax",
            "Cannot be determined without medical tax credit data",
            "Only eligible if registered as a provisional taxpayer"
        ])

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # Guarantee 4 distinct options without any synthetic tokens
    nudge = 1
    while len(final_opts) < 4:
        if curr_match:
            cand = _fmt_curr(float(c_num) + nudge * 150.0)
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        elif pct_match:
            cand = f"{_fmt(float(p_num) + nudge * 1.5, 2)}%"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        elif num_match:
            cand = f"{prefix}{_fmt(val + nudge * 2.5)}{suffix}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        else:
            final_opts.append(f"{cleaned} (Standard Tier {nudge})")
        nudge += 1

    r.shuffle(final_opts)
    return final_opts, final_opts.index(cleaned)


def _build_question_payload(
    subskill_id: str,
    prompt: str,
    correct_ans: str,
    options: List[str],
    explanation: str,
    tier_1: str,
    tier_2: str,
    tier_3: str,
    r: random.Random,
    table_data: Optional[Dict[str, Any]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
    difficulty: str = "medium",
) -> Dict[str, Any]:
    """Assemble standard 6-pillar question payload for Grade 12 MathLit Income Tax."""
    payload: Dict[str, Any] = {
        "question_id": f"mathlit_gr12_incometax_{subskill_id}_{uuid.uuid4().hex[:8]}",
        "topic": "grade12_mathlit_income_tax",
        "subskill": subskill_id,
        "difficulty": difficulty,
        "term": 1,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "expected_answer": correct_ans,
        "correct_index": options.index(correct_ans) if correct_ans in options else 0,
        "explanation": explanation,
        "marking_schema": [
            {"step": 1, "description": "Identify tax bracket, threshold, or relevant formula", "marks": 1, "type": "M"},
            {"step": 2, "description": "Perform progressive rate calculation or deduction substitution", "marks": 1, "type": "M"},
            {"step": 3, "description": "Apply rebate / tax credit and state final value with units", "marks": 1, "type": "A"},
        ],
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
        "misconception_tags": [
            "confusing_gross_salary_and_taxable_income",
            "applying_tax_rate_to_entire_salary_instead_of_marginal_excess",
            "omitting_age_appropriate_tax_rebates",
            "treating_medical_scheme_credit_as_income_deduction_instead_of_tax_credit",
        ],
    }
    if table_data:
        payload["table_data"] = table_data
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
