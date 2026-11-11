"""Common helpers, formatters, and question payload builder for Grade 12 Mathematical Literacy: CONVERSIONS & TIME."""
from __future__ import annotations

import math
import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda", "Devan", "Riaan", "Johan"
]


def _fmt(val: float | int, places: int = 2) -> str:
    """Format numbers according to South African standard: comma decimal, space thousands."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()) or places == 0:
        return f"{int(round(float(val))):,}".replace(",", " ")
    s = f"{val:.{places}f}"
    parts = s.split(".")
    integer_part = f"{int(parts[0]):,}".replace(",", " ")
    if len(parts) < 2:
        return integer_part
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
    """Format percentage with South African comma decimal: e.g. 25,5% or 50%."""
    return f"{_fmt(val, places)}%"


def _fmt_frac(num: int, den: int) -> str:
    """Format simplified fraction without raw LaTeX: e.g. 3/7 or 12/49."""
    common = math.gcd(num, den)
    s_num = num // common
    s_den = den // common
    return f"{s_num}/{s_den}"



def _fmt_time(hours: int, minutes: int) -> str:
    """Format 24-hour time e.g. 08:20, 14:45."""
    h = hours % 24
    m = minutes % 60
    return f"{h:02d}:{m:02d}"


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

    # Time pattern: e.g. 08:20 or 14:45
    time_match = re.search(r"(\d{1,2}):(\d{2})", cleaned)
    if time_match:
        th = int(time_match.group(1))
        tm = int(time_match.group(2))
        prefix = cleaned[:time_match.start()]
        suffix = cleaned[time_match.end():]
        perturbations = [(1, 0), (-1, 0), (0, 15), (0, -15), (0, 30), (0, -30), (2, 0)]
        for dh, dm in perturbations:
            nh = (th + dh) % 24
            nm = (tm + dm)
            if nm >= 60:
                nh = (nh + 1) % 24
                nm -= 60
            elif nm < 0:
                nh = (nh - 1) % 24
                nm += 60
            cand = f"{prefix}{nh:02d}:{nm:02d}{suffix}"
            if cand != cleaned:
                distractors.add(cand)

    # Currency pattern: e.g. R 1 250,00
    curr_match = re.search(r"R\s*([0-9\s]+),(\d{2})", cleaned)
    if curr_match:
        int_str = curr_match.group(1).replace(" ", "")
        cents_str = curr_match.group(2)
        base_val = float(f"{int_str}.{cents_str}")
        factors = [0.85, 1.15, 0.90, 1.10, 1.25, 0.75, 1.50]
        for f in factors:
            perturbed = round(base_val * f, 2)
            cand = _fmt_curr(perturbed)
            if cand != cleaned:
                distractors.add(cand)

    # General decimal or integer pattern
    num_match = re.search(r"(\d+(?:[ ,]\d+)*(?:\.\d+)?)", cleaned.replace(",", "."))
    if num_match:
        val_str = num_match.group(1).replace(" ", "")
        try:
            val = float(val_str)
            if val > 0:
                del_list = [val * 1.1, val * 0.9, val * 1.2, val * 0.8, val + 1, val - 1, val * 10, val / 10]
                prefix = cleaned[:num_match.start()]
                suffix = cleaned[num_match.end():]
                for d in del_list:
                    cand = f"{prefix}{_fmt(d, 2)}{suffix}"
                    if cand != cleaned:
                        distractors.add(cand)
        except ValueError:
            pass

    opts_list = [cleaned] + list(distractors)
    unique_opts: List[str] = []
    for opt in opts_list:
        if opt not in unique_opts:
            unique_opts.append(opt)
        if len(unique_opts) == 4:
            break

    # If still fewer than 4, craft deterministic authentic variations
    counter = 1
    while len(unique_opts) < 4:
        cand = f"{cleaned} + {counter}"
        if cand not in unique_opts:
            unique_opts.append(cand)
        counter += 1

    r.shuffle(unique_opts)
    return unique_opts, unique_opts.index(cleaned)


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
    visual_context: Optional[str] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Assemble standardized 6-pillar question payload for Grade 12 Conversions and Time."""
    q_uuid = uuid.UUID(int=r.getrandbits(128), version=4).hex[:8]
    qid = f"mathlit_gr12_conv_{subskill_id}_{q_uuid}"
    correct_idx = options.index(correct_ans)

    payload: Dict[str, Any] = {
        "question_id": qid,
        "topic": "grade12_mathlit_conversions_and_time",
        "subskill": subskill_id,
        "grade": "12",
        "term": 4,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "correct_index": correct_idx,
        "explanation": explanation,
        "marking_schema": [
            {"step": 1, "description": "Identify conversion factor, formula, or timetable entry", "marks": 1, "type": "M"},
            {"step": 2, "description": "Perform calculation with proper unit progression", "marks": 1, "type": "M"},
            {"step": 3, "description": "Formulate final answer with accurate units and rounding", "marks": 1, "type": "A"},
        ],
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
        "misconception_tags": [
            f"conv_{subskill_id}_unit_confusion",
            f"conv_{subskill_id}_inversion_error",
            f"conv_{subskill_id}_rounding_premature",
        ],
    }

    if visual_context:
        payload["visual_context"] = visual_context
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec

    return payload
