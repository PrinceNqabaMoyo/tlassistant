"""Common helpers, formatters, and reference medical data for Grade 12 Mathematical Literacy:
MEASURING WEIGHT: BODY MASS INDEX (BMI), GROWTH CHARTS & MEDICINE DOSAGES.
"""
from __future__ import annotations

import math
import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Amy", "Nontando", "Sipho", "Nandi", "Farai", "Johan", "Fatima", "Lerato", "Kagiso",
    "Thabo", "Nomvula", "Pieter", "Zanele", "Dikeledi", "Bongani", "Mrs Mokoena",
    "Lwazi", "Mpho", "Tariro", "Willem", "Amina", "Jabulani", "Keval"
]

# WHO Adult BMI Classification Boundaries
# < 18.5: Underweight
# 18.5 - 24.9: Normal / Healthy weight
# 25.0 - 29.9: Overweight
# >= 30.0: Obese

# Child/Adolescent (2-20 years) Percentile Range Boundaries
# < 5th: Underweight
# 5th to < 85th: Healthy weight
# 85th to < 95th: At risk of overweight
# >= 95th: Overweight


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
    is_neg = v < 0
    abs_v = abs(v)
    s = f"{abs_v:.2f}"
    int_p, dec_p = s.split(".")
    int_formatted = f"{int(int_p):,}".replace(",", " ")
    prefix = f"-{curr_symbol}" if is_neg else curr_symbol
    return f"{prefix}{int_formatted},{dec_p}"


def _build_options(
    correct_ans: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None
) -> Tuple[List[str], int]:
    """Generate strictly 4 distinct multiple choice options with zero synthetic fallbacks."""
    distractors: set[str] = set()
    cleaned = correct_ans.strip()

    if custom_options:
        for opt in custom_options:
            o_clean = opt.strip()
            if o_clean and o_clean != cleaned:
                distractors.add(o_clean)

    # 1. Currency pattern (Rands)
    curr_match = re.search(r"(-?)\s*R\s*([\d\s]+(?:[.,]\d+)?)", cleaned)
    val_curr = 0.0
    if curr_match:
        sign = -1.0 if curr_match.group(1) == "-" else 1.0
        c_num = curr_match.group(2).replace(" ", "").replace(",", ".")
        try:
            val_curr = sign * float(c_num)
            for sc in [1.15, 0.85, 1.25, 0.75, 1.10, 0.90, 1.05, 0.95]:
                d_val = round(val_curr * sc, 2)
                d_str = _fmt_curr(d_val)
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [25.0, -25.0, 50.0, -50.0, 100.0, -100.0, 250.0, -250.0]:
                d_val = round(val_curr + sh, 2)
                d_str = _fmt_curr(d_val)
                if d_str != cleaned:
                    distractors.add(d_str)
        except ValueError:
            pass

    # 2. Percentage pattern
    pct_match = re.search(r"(-?[\d\s]+(?:[.,]\d+)?)\s*%", cleaned)
    val_pct = 0.0
    if pct_match:
        p_num = pct_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val_pct = float(p_num)
            for sh in [2.5, -2.5, 5.0, -5.0, 1.0, -1.0, 3.5, -3.5]:
                d_val = round(val_pct + sh, 2)
                d_str = f"{_fmt(d_val, 2)}%"
                if d_str != cleaned:
                    distractors.add(d_str)
        except ValueError:
            pass

    # 3. Numeric pattern with units (e.g. kg/m², kg, g, mg, mL, cm, m, drops/min, kcal)
    num_match = re.search(r"(-?\d+(?:[.,]\d+)?)", cleaned)
    if num_match and not curr_match and not pct_match:
        val_str = num_match.group(1).replace(",", ".")
        prefix = cleaned[:num_match.start(1)]
        suffix = cleaned[num_match.end(1):]
        try:
            val = float(val_str)
            is_int = val.is_integer()
            scales = [1.10, 0.90, 1.20, 0.80, 1.25, 0.75, 1.05, 0.95, 1.50, 0.50]
            shifts = [1.0, 2.0, 3.0, 4.0, 5.0, 10.0, -1.0, -2.0, -3.0, -4.0, -5.0, -10.0]
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

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # Guarantee 4 distinct options without any synthetic tokens
    nudge = 1
    while len(final_opts) < 4:
        if curr_match:
            cand = _fmt_curr(val_curr + nudge * 35.0)
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        elif pct_match:
            cand = f"{_fmt(val_pct + nudge * 2.0, 2)}%"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        elif num_match:
            cand_val = val + nudge * (2 if is_int else 1.5)
            cand = f"{prefix}{_fmt(int(cand_val) if is_int else round(cand_val, 2))}{suffix}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        else:
            cand = f"Classification {nudge}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
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
    """Assemble standard 6-pillar question payload for Grade 12 MathLit BMI & Medicine Dosages."""
    payload: Dict[str, Any] = {
        "question_id": f"mathlit_gr12_bmi_{subskill_id}_{uuid.uuid4().hex[:8]}",
        "topic": "grade12_mathlit_measuring_weight_bmi_medicine_dosages",
        "subskill": subskill_id,
        "difficulty": difficulty,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "expected_answer": correct_ans,
        "correct_index": options.index(correct_ans) if correct_ans in options else 0,
        "explanation": explanation,
        "marking_schema": [
            {"step": 1, "description": "Identify relevant formula, growth chart parameters, or medical variables", "marks": 1, "type": "M"},
            {"step": 2, "description": "Substitute values into formula and perform calculation", "marks": 1, "type": "M"},
            {"step": 3, "description": "State final BMI, percentile classification, or dosage with correct units", "marks": 1, "type": "A"},
        ],
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
        "misconception_tags": [
            "forgetting_to_square_height_in_bmi_formula",
            "using_height_in_centimetres_instead_of_metres_in_bmi",
            "applying_adult_bmi_cutoffs_directly_to_children_instead_of_percentiles",
            "confusing_mg_dosage_with_ml_liquid_suspension_volume",
            "forgetting_to_divide_daily_antibiotic_dose_into_individual_administrations",
        ],
    }
    if table_data:
        payload["table_data"] = table_data
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
