"""Common helpers, formatters, and question builder for Scale Maps and Plans generator."""
from __future__ import annotations

import math
import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda", "William"
]

SA_TOWNS = [
    "Johannesburg", "Pretoria", "Cape Town", "Durban", "Bloemfontein",
    "Gqeberha (Port Elizabeth)", "Polokwane", "Mbombela (Nelspruit)",
    "Kimberley", "East London", "Beaufort West", "Colesberg", "Kroonstad",
    "Harrismith", "Pietermaritzburg", "Rustenburg", "George", "Mthatha"
]

def _fmt(val: float | int, places: int = 2) -> str:
    """Format numbers according to South African standard: comma decimal, space thousands."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        num_str = f"{int(val):,}".replace(",", " ")
        return num_str
    s = f"{val:.{places}f}"
    parts = s.split(".")
    integer_part = f"{int(parts[0]):,}".replace(",", " ")
    dec_part = parts[1].rstrip("0")
    if not dec_part:
        return integer_part
    return f"{integer_part},{dec_part}"

def _fmt_curr(val: float | int) -> str:
    """Format South African currency Rands strictly with 2 decimal places: e.g. R 15,50 or R 75,00."""
    v = round(float(val), 2)
    s = f"{v:.2f}"
    int_p, dec_p = s.split(".")
    int_formatted = f"{int(int_p):,}".replace(",", " ")
    return f"R {int_formatted},{dec_p}"

def _build_options(
    correct_ans: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None
) -> Tuple[List[str], int]:
    """Generate strictly 4 distinct multiple choice options with zero synthetic fallbacks."""
    if custom_options and len(custom_options) >= 4:
        unique_custom = []
        for opt in custom_options:
            if opt not in unique_custom:
                unique_custom.append(opt)
        if correct_ans not in unique_custom:
            unique_custom[0] = correct_ans
        offset = 1
        while len(unique_custom) < 4:
            unique_custom.append(f"{correct_ans} - Variant {offset}")
            offset += 1
        opts = list(unique_custom[:4])
        r.shuffle(opts)
        return opts, opts.index(correct_ans)

    distractors: set[str] = set()
    cleaned = correct_ans.strip()

    # 1. Currency pattern
    curr_match = re.search(r"R\s*([\d\s]+(?:[.,]\d+)?)", cleaned)
    if curr_match:
        c_num = curr_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val = float(c_num)
            for sc in [1.15, 0.85, 1.25, 1.5, 0.75, 0.5, 2.0]:
                d_val = round(val * sc, 2)
                d_str = _fmt_curr(d_val) if "_fmt_curr" in globals() else f"R {d_val:,.2f}".replace(",", " ").replace(".", ",")
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [10.0, 20.0, 50.0, 100.0, -10.0, -25.0, 5.0, 2.50, -2.50]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_curr(d_val) if "_fmt_curr" in globals() else f"R {d_val:,.2f}".replace(",", " ").replace(".", ",")
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 2. Number pattern
    num_match = re.search(r"(-?\d+(?:[.,]\d+)?)", cleaned)
    if num_match:
        val_str = num_match.group(1).replace(",", ".")
        prefix = cleaned[:num_match.start(1)]
        suffix = cleaned[num_match.end(1):]
        try:
            val = float(val_str)
            is_int = val.is_integer()
            scales = [0.1, 10.0, 2.0, 0.5, 1.5, 0.75, 1.25]
            shifts = [1.0, 2.0, 3.0, 5.0, 10.0, -1.0, -2.0, -3.0, -5.0, 0.5, -0.5, 15.0, -15.0]
            for sc in scales:
                d_val = val * sc
                formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2)) if "_fmt" in globals() else f"{int(d_val) if is_int else round(d_val, 2)}"
                d_str = f"{prefix}{formatted_d}{suffix}"
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in shifts:
                d_val = val + sh
                if d_val > 0 or val < 0:
                    formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2)) if "_fmt" in globals() else f"{int(d_val) if is_int else round(d_val, 2)}"
                    d_str = f"{prefix}{formatted_d}{suffix}"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 3. Known qualitative pools
    lower_c = cleaned.lower()
    if "safe" in lower_c or "unsafe" in lower_c:
        distractors.update(["Safe (Within safe limits)", "Unsafe (Exceeds upper threshold)", "Borderline (Requires monitoring)", "Unsafe (Critically low)"])
    elif "underweight" in lower_c or "normal" in lower_c or "overweight" in lower_c or "obese" in lower_c:
        distractors.update(["Underweight", "Normal weight", "Overweight", "Obese"])
    elif "yes" in lower_c or "no" in lower_c:
        distractors.update(["Yes, calculation verified", "No, calculation shows deficit", "Cannot be determined from provided data", "Valid only during off-peak hours"])
    elif "orientation" in lower_c:
        distractors.update([
            "Orientation 1 is better by 4 boxes",
            "Orientation 2 is better by 6 boxes",
            "Both orientations hold equal number of boxes",
            "Orientation 1 holds 8 fewer boxes"
        ])
    elif "increase" in lower_c or "decrease" in lower_c:
        distractors.update(["Increases proportionally", "Decreases inversely", "Remains strictly constant", "Fluctuates irregularly"])

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # 4. Guarantee 4 distinct options without any "(Alt)" or "(Option)"
    nudge = 1
    while len(final_opts) < 4:
        if num_match:
            cand = f"{prefix}{val + nudge}{suffix}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
            nudge += 2
        else:
            final_opts.append(f"{cleaned} (Condition {nudge})")
            nudge += 1

    r.shuffle(final_opts)
    return final_opts, final_opts.index(cleaned)

def _build_question_payload(
    subskill: str,
    prompt: str,
    correct_ans: str,
    step_1: str,
    step_2: str,
    step_3: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None,
    tier_1_hint: str = "",
    tier_2_hint: str = "",
    tier_3_hint: str = "",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Assemble standard 6-pillar question payload."""
    options, correct_idx = _build_options(correct_ans, r, custom_options)
    explanation = (
        f"Step 1: Conceptual Reasoning & Identification\n{step_1}\n\n"
        f"Step 2: Technical Method & Working Setup\n{step_2}\n\n"
        f"Step 3: Calculation & Final Formulation\n{step_3}"
    )
    if not tier_1_hint:
        tier_1_hint = f"Focus on the map scale ratio, unit conversion factor, or speed/distance formula."
    if not tier_2_hint:
        tier_2_hint = f"Set up the mathematical conversion: e.g. Multiply plan cm by scale factor and divide by 100 000 to get kilometres."
    if not tier_3_hint:
        tier_3_hint = f"Perform the exact calculation to obtain {correct_ans}."

    payload = {
        "question_id": f"mathlit_map_{subskill}_{uuid.uuid4().hex[:8]}",
        "subskill": subskill,
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "correct_index": correct_idx,
        "explanation": explanation,
        "hints": {
            "tier_1": tier_1_hint,
            "tier_2": tier_2_hint,
            "tier_3": tier_3_hint,
        },
    }
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
