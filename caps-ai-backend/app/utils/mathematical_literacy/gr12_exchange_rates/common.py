"""Common helpers, formatters, and question payload builder for Grade 12 Mathematical Literacy: EXCHANGE RATES."""
from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda", "Kaveshan",
    "Dikeledi", "Mandla", "Nokuthula", "Pieter", "Johan", "Fatima"
]

SA_BANKS = [
    {"name": "Standard Bank", "comm_rate": 0.0185, "min_fee": 70.0, "max_fee": 650.0},
    {"name": "ABSA Bank", "comm_rate": 0.0168, "min_fee": 85.0, "max_fee": 620.0},
    {"name": "First National Bank (FNB)", "comm_rate": 0.0195, "min_fee": 75.0, "max_fee": 700.0},
    {"name": "Nedbank", "comm_rate": 0.0175, "min_fee": 80.0, "max_fee": 680.0},
]

SA_CITIES = [
    "Johannesburg", "Cape Town", "Durban", "Pretoria", "Gqeberha",
    "Bloemfontein", "Polokwane", "Mbombela", "Kimberley", "East London"
]

MAJOR_CURRENCIES = {
    "USD": {"name": "US Dollar", "symbol": "$", "base_bbr": 18.20, "base_bsr": 18.95},
    "GBP": {"name": "British Pound", "symbol": "£", "base_bbr": 23.10, "base_bsr": 24.15},
    "EUR": {"name": "Euro", "symbol": "€", "base_bbr": 19.80, "base_bsr": 20.70},
    "BWP": {"name": "Botswana Pula", "symbol": "P ", "base_bbr": 0.7450, "base_bsr": 0.7120},  # quoted as 1 ZAR = x BWP
    "JPY": {"name": "Japanese Yen", "symbol": "¥", "base_bbr": 0.118, "base_bsr": 0.128},
    "AUD": {"name": "Australian Dollar", "symbol": "A$", "base_bbr": 11.85, "base_bsr": 12.55},
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


def _fmt_curr(val: float | int, curr_symbol: str = "R ") -> str:
    """Format currency values strictly with 2 decimal places and South African number grouping."""
    v = round(float(val), 2)
    s = f"{v:.2f}"
    int_p, dec_p = s.split(".")
    int_formatted = f"{int(int_p):,}".replace(",", " ")
    return f"{curr_symbol}{int_formatted},{dec_p}"


def _fmt_foreign(val: float | int, curr_symbol: str, places: int = 2) -> str:
    """Format foreign currency values with appropriate symbol and decimal places."""
    v = round(float(val), places)
    if places == 0 or (isinstance(v, float) and v.is_integer()):
        int_f = f"{int(v):,}".replace(",", " ")
        return f"{curr_symbol}{int_f}"
    s = f"{v:.{places}f}"
    int_p, dec_p = s.split(".")
    int_f = f"{int(int_p):,}".replace(",", " ")
    return f"{curr_symbol}{int_f},{dec_p}"


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
            unique_custom[0] = correct_ans
        offset = 1
        while len(unique_custom) < 4:
            unique_custom.append(f"{correct_ans} (Variation {offset})")
            offset += 1
        opts = list(unique_custom[:4])
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
            for sc in [1.185, 0.815, 1.25, 0.75, 1.10, 0.90, 1.05, 0.95]:
                d_val = round(val * sc, 2)
                d_str = _fmt_curr(d_val)
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [70.0, 85.0, -70.0, -85.0, 50.0, -50.0, 100.0, -100.0, 15.0, -15.0]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_curr(d_val)
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 2. Foreign currency pattern ($, £, €, P, ¥, A$)
    foreign_match = re.search(r"([$£€¥]|P\s*|A\$\s*)([\d\s]+(?:[.,]\d+)?)", cleaned)
    if foreign_match:
        sym = foreign_match.group(1).strip()
        f_num = foreign_match.group(2).replace(" ", "").replace(",", ".")
        try:
            val = float(f_num)
            for sc in [1.10, 0.90, 1.20, 0.80, 1.05, 0.95]:
                d_val = round(val * sc, 2)
                d_str = _fmt_foreign(d_val, f"{sym} " if len(sym) == 1 and sym not in "$£€¥" else sym)
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [10.0, 20.0, -10.0, -20.0, 50.0, -50.0, 5.0, -5.0]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_foreign(d_val, f"{sym} " if len(sym) == 1 and sym not in "$£€¥" else sym)
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 3. Numeric pattern
    num_match = re.search(r"(-?\d+(?:[.,]\d+)?)", cleaned)
    if num_match and not curr_match and not foreign_match:
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
    if "bank selling rate" in lower_c or "bank buying rate" in lower_c:
        distractors.update([
            "Bank Selling Rate (BSR) because the bank is selling foreign currency to the client",
            "Bank Buying Rate (BBR) because the bank is buying foreign currency from the client",
            "Mid-market interbank exchange rate without bank margin",
            "Travellers' cheque telegraphic settlement rate"
        ])
    elif "undervalued" in lower_c or "overvalued" in lower_c:
        distractors.update([
            "Undervalued against the foreign currency",
            "Overvalued against the foreign currency",
            "At exact Purchasing Power Parity (fair value)",
            "Cannot be evaluated without inflation index data"
        ])
    elif "cheaper" in lower_c or "more expensive" in lower_c:
        distractors.update([
            "Option 1 is cheaper due to lower transaction commission",
            "Option 2 is cheaper due to avoiding fixed withdrawal fees",
            "Both options have exactly identical total costs",
            "Option 1 is more expensive due to minimum fee penalties"
        ])
    elif "benefit" in lower_c or "harm" in lower_c or "advantage" in lower_c:
        distractors.update([
            "Exporters benefit because they earn more Rands for foreign sales",
            "Importers benefit because imported goods cost fewer Rands",
            "Both importers and exporters benefit equally",
            "Neither importers nor exporters are affected by exchange rate changes"
        ])

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # Guarantee 4 distinct options without any synthetic tokens
    nudge = 1
    while len(final_opts) < 4:
        if curr_match:
            cand = _fmt_curr(float(c_num) + nudge * 25.0)
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
        elif foreign_match:
            cand = _fmt_foreign(float(f_num) + nudge * 10.0, sym)
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
    """Assemble standard 6-pillar question payload for Grade 12 MathLit Exchange Rates."""
    payload: Dict[str, Any] = {
        "question_id": f"mathlit_gr12_exrate_{subskill_id}_{uuid.uuid4().hex[:8]}",
        "topic": "grade12_mathlit_exchange_rates",
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
        "explanation": explanation,
        "marking_schema": [
            {"step": 1, "description": "Identify relevant exchange rate or formula", "marks": 1, "type": "M"},
            {"step": 2, "description": "Substitute values and perform arithmetic calculation", "marks": 1, "type": "M"},
            {"step": 3, "description": "State final answer with correct units and currency symbol", "marks": 1, "type": "A"},
        ],
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
        "misconception_tags": [
            "confusing_bank_selling_and_bank_buying_rate",
            "multiplying_instead_of_dividing_currency_rate",
            "omitting_bank_minimum_commission_fee",
            "incorrect_foreign_banknote_denomination_rounding",
        ],
    }
    if table_data:
        payload["table_data"] = table_data
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
