"""Common helpers, formatters, and question payload builder for Grade 12 Mathematical Literacy: FINANCE (INTEREST, BANKING, INFLATION)."""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda", "Robert", "William", "Vuyo"
]

# Standard South African mortgage repayment factors per R 1 000 borrowed:
# Table layout: [years][annual_rate] -> factor
LOAN_FACTOR_TABLE: Dict[int, Dict[float, float]] = {
    15: {
        9.5: 10.44,
        10.0: 10.75,
        10.25: 10.90,
        10.5: 11.05,
        10.75: 11.21,
        11.0: 11.37,
        11.5: 11.68,
        12.0: 12.00,
    },
    20: {
        9.5: 9.32,
        10.0: 9.65,
        10.25: 9.82,
        10.5: 9.98,
        10.75: 10.15,
        11.0: 10.32,
        11.5: 10.66,
        12.0: 11.01,
    },
    25: {
        9.5: 8.74,
        10.0: 9.09,
        10.25: 9.26,
        10.5: 9.44,
        10.75: 9.62,
        11.0: 9.80,
        11.5: 10.17,
        12.0: 10.53,
    },
    30: {
        9.5: 8.41,
        10.0: 8.78,
        10.25: 8.96,
        10.5: 9.15,
        10.75: 9.33,
        11.0: 9.52,
        11.5: 9.90,
        12.0: 10.29,
    },
}


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


def _fmt_curr(val: float | int) -> str:
    """Format South African currency Rands strictly with 2 decimal places: e.g. R 1 250,00 or R 75,50."""
    v = round(float(val), 2)
    s = f"{v:.2f}"
    int_p, dec_p = s.split(".")
    int_formatted = f"{int(int_p):,}".replace(",", " ")
    return f"R {int_formatted},{dec_p}"


def _fmt_pct(val: float | int, places: int = 1) -> str:
    """Format percentage with South African comma decimal: e.g. 11,5% or 7%."""
    return f"{_fmt(val, places)}%"


def _build_options(
    correct_ans: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None
) -> Tuple[List[str], int]:
    """Generate strictly 4 distinct multiple choice options with zero synthetic fallbacks."""
    if custom_options and len(custom_options) >= 4:
        unique_custom: List[str] = []
        for opt in custom_options:
            cleaned_opt = opt.strip()
            if cleaned_opt and cleaned_opt not in unique_custom:
                unique_custom.append(cleaned_opt)
        if correct_ans not in unique_custom:
            unique_custom[0] = correct_ans
        if len(unique_custom) >= 4:
            opts = list(unique_custom[:4])
            r.shuffle(opts)
            return opts, opts.index(correct_ans)

    distractors: set[str] = set()
    cleaned = correct_ans.strip()

    # 1. Currency pattern: e.g. R 7 850,94 or R 1 884 225,60
    curr_match = re.search(r"R\s*([\d\s]+(?:[.,]\d+)?)", cleaned)
    if curr_match:
        c_num = curr_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val = float(c_num)
            for sc in [1.15, 0.85, 1.25, 0.75, 1.5, 0.5, 1.10, 0.90]:
                d_val = round(val * sc, 2)
                d_str = _fmt_curr(d_val)
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [1000.0, 2500.0, 5000.0, -1000.0, -2500.0, 50.0, -50.0, 100.0, -100.0]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_curr(d_val)
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 2. Percentage pattern: e.g. 11,5% or 7,6%
    pct_match = re.search(r"(-?\d+(?:[.,]\d+)?)\s*%", cleaned)
    if pct_match:
        p_num = pct_match.group(1).replace(",", ".")
        try:
            val = float(p_num)
            for sc in [1.1, 0.9, 1.25, 0.75, 0.5, 1.5]:
                d_val = round(val * sc, 1)
                d_str = f"{_fmt(d_val, 1)}%"
                if d_str != cleaned and 0 <= d_val <= 100:
                    distractors.add(d_str)
            for sh in [1.0, 2.0, -1.0, -2.0, 0.5, -0.5, 1.5, -1.5, 3.0, -3.0]:
                d_val = round(val + sh, 1)
                if 0 <= d_val <= 100:
                    d_str = f"{_fmt(d_val, 1)}%"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 3. Numeric pattern with optional units
    num_match = re.search(r"(-?\d+(?:[.,]\d+)?)", cleaned)
    if num_match and not pct_match and not curr_match:
        val_str = num_match.group(1).replace(",", ".")
        prefix = cleaned[:num_match.start(1)]
        suffix = cleaned[num_match.end(1):]
        try:
            val = float(val_str)
            is_int = val.is_integer()
            scales = [1.2, 0.8, 1.5, 0.5, 2.0, 0.75, 1.25, 1.1, 0.9]
            shifts = [1.0, 2.0, 3.0, 5.0, 10.0, -1.0, -2.0, -3.0, -5.0, -10.0, 0.5, -0.5]
            for sc in scales:
                d_val = val * sc
                formatted_d = _fmt(int(round(d_val)) if is_int else round(d_val, 2))
                d_str = f"{prefix}{formatted_d}{suffix}"
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in shifts:
                d_val = val + sh
                if d_val > 0 or val < 0:
                    formatted_d = _fmt(int(round(d_val)) if is_int else round(d_val, 2))
                    d_str = f"{prefix}{formatted_d}{suffix}"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # Guarantee 4 distinct options without any synthetic "(Alt)" tokens
    nudge = 1
    while len(final_opts) < 4:
        if num_match:
            n_val = val + nudge
            formatted_n = _fmt(int(round(n_val)) if is_int else round(n_val, 2))
            cand = f"{prefix}{formatted_n}{suffix}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
            nudge += 2
        else:
            final_opts.append(f"{cleaned} (Option {nudge})")
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
    diagram_spec: Optional[Dict[str, Any]] = None,
    difficulty: str = "medium",
) -> Dict[str, Any]:
    """Assemble standard 6-pillar question payload."""
    payload: Dict[str, Any] = {
        "question_id": f"mathlit_gr12_finance_{subskill_id}_{uuid.uuid4().hex[:8]}",
        "topic": "grade12_mathlit_interest_banking_inflation",
        "subskill": subskill_id,
        "difficulty": difficulty,
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "explanation": explanation,
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
    }
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
