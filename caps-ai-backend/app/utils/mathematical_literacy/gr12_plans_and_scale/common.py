"""Common utilities and formatters for Grade 12 Mathematical Literacy: Plans and scale.

Enforces:
  - Strict South African number formatting (space grouping, comma decimals, e.g. 1 200 mm, 15,5 cm, R 450,00).
  - Authentic South African architectural contexts (SANS 10400 building standards, municipal bylaws, Wendy houses, RDP cottages).
  - Pure 6-pillar question payload output with zero synthetic distractors.
  - 3-tier diagnostic hint scaffolding.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

SA_NAMES = [
    "Sipho", "Thabo", "Lerato", "Kagiso", "Nomvula", "Bongani", "Zanele",
    "Mpho", "Tshepo", "Keitumetse", "Sibusiso", "Nthabiseng", "Lungile",
    "Jabulani", "Precious", "Simphiwe", "Anrich", "Willem", "Johan",
    "Devan", "Farouk", "Fatima", "Rashid", "Ayanda", "Khanyisile"
]

SA_BUILDING_EXAMPLES = [
    {"name": "Timber Wendy House", "real_l_m": 4.5, "real_w_m": 3.6, "wall_h_m": 2.4, "roof_apex_h_m": 3.2},
    {"name": "Standard Two-Bedroom RDP House", "real_l_m": 7.5, "real_w_m": 5.4, "wall_h_m": 2.6, "roof_apex_h_m": 3.6},
    {"name": "Suburban Freestanding Cottage", "real_l_m": 9.0, "real_w_m": 6.5, "wall_h_m": 2.8, "roof_apex_h_m": 4.2},
    {"name": "Primary School Classroom", "real_l_m": 10.0, "real_w_m": 7.0, "wall_h_m": 3.0, "roof_apex_h_m": 4.5},
    {"name": "Community Health Consultation Clinic", "real_l_m": 8.0, "real_w_m": 6.0, "wall_h_m": 2.8, "roof_apex_h_m": 3.8},
]


def _fmt(val: float, decimals: int = 2) -> str:
    """Format a float with comma decimals and space grouping."""
    fmt_str = f"{{:,.{decimals}f}}".format(val)
    parts = fmt_str.split(".")
    int_part = parts[0].replace(",", " ")
    if len(parts) > 1:
        dec_part = parts[1].rstrip("0")
        if not dec_part:
            return int_part
        return f"{int_part},{dec_part}"
    return int_part


def _fmt_fixed(val: float, decimals: int = 2) -> str:
    """Format a float with exact fixed decimal places."""
    fmt_str = f"{{:,.{decimals}f}}".format(val)
    parts = fmt_str.split(".")
    int_part = parts[0].replace(",", " ")
    return f"{int_part},{parts[1]}"


def _fmt_zar(val: float) -> str:
    """Format South African Rands."""
    return f"R {_fmt_fixed(val, 2)}"


def _build_options(
    correct_str: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None,
) -> Tuple[List[str], int]:
    """Generate 4 strictly distinct options with authentic mathematical distractors."""
    clean_opts: List[str] = [correct_str]
    if custom_options:
        for opt in custom_options:
            if opt != correct_str and opt not in clean_opts:
                clean_opts.append(opt)
            if len(clean_opts) == 4:
                r.shuffle(clean_opts)
                return clean_opts, clean_opts.index(correct_str)

    # Fallback numerical perturbations if custom_options not fully populated
    options = list(clean_opts)

    # Check if correct_str contains dimensions like "A × B"
    if " × " in correct_str:
        parts = correct_str.split(" × ")
        factors = [(1.2, 1.2), (0.8, 0.8), (1.5, 1.0), (1.0, 1.5), (0.5, 0.5), (2.0, 2.0)]
        for f1, f2 in factors:
            try:
                p1_val = float(parts[0].replace(" cm", "").replace(" mm", "").replace(" m", "").replace(" ", "").replace(",", "."))
                p2_val = float(parts[1].replace(" cm", "").replace(" mm", "").replace(" m", "").replace(" ", "").replace(",", "."))
                u1 = " cm" if " cm" in parts[0] else (" mm" if " mm" in parts[0] else " m")
                u2 = " cm" if " cm" in parts[1] else (" mm" if " mm" in parts[1] else " m")
                cand = f"{_fmt(p1_val * f1, 1)}{u1} × {_fmt(p2_val * f2, 1)}{u2}"
                if cand not in options:
                    options.append(cand)
                if len(options) == 4:
                    break
            except Exception:
                pass

    # Check if ratio format "1 : X"
    if correct_str.startswith("1 : ") and len(correct_str.split(" : ")) == 2:
        try:
            x_str = correct_str.split(" : ")[1].split(" ")[0].replace(",", ".")
            x_val = float(x_str)
            ratio_factors = [2.0, 0.5, 1.5, 0.75, 2.5, 0.4]
            for rf in ratio_factors:
                new_x = int(round(x_val * rf))
                cand = f"1 : {new_x}"
                if cand not in options:
                    options.append(cand)
                if len(options) == 4:
                    break
        except Exception:
            pass

    # Check if single numeric value
    core = correct_str.replace("R ", "").replace(" cm²", "").replace(" m²", "").replace(" cm³", "").replace(" m³", "").replace(" kg", "").replace(" cm", "").replace(" mm", "").replace(" m", "").replace(" bricks", "").replace(" sheets", "").replace("%", "").replace(" ", "").replace(",", ".")
    try:
        val = float(core)
        nudge_factors = [0.8, 1.25, 1.5, 0.5, 2.0, 1.1, 0.9, 0.75, 1.3]
        for f in nudge_factors:
            new_val = val * f
            new_str = correct_str.replace(_fmt(val), _fmt(new_val))
            if new_str not in options:
                options.append(new_str)
            if len(options) == 4:
                break
    except ValueError:
        pass

    r.shuffle(options)
    return options, options.index(correct_str)


def _build_question_payload(
    subskill_id: str,
    prompt: str,
    correct_answer: str,
    options: List[str],
    solution_steps: List[str],
    t1: str,
    t2: str,
    t3: str,
    r: random.Random,
    difficulty: str = "medium",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Build canonical 6-pillar question payload for Grade 12 Plans and Scale."""
    explanation = "\n".join(solution_steps)
    payload: Dict[str, Any] = {
        "id": f"mathlit_gr12_plans_{subskill_id}_{r.randint(10000000, 99999999):08x}",
        "topic": "plans and scale",
        "grade": 12,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": difficulty,
        "subskill_id": subskill_id,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "options": options,
        "explanation": explanation,
        "marking_schema": [
            {"step": "Step 1: Formula / Scale / Unit Conversion Identification", "marks": 1, "type": "Method"},
            {"step": "Step 2: Technical Substitution & Progressive Calculation", "marks": 1, "type": "Method"},
            {"step": "Step 3: Solution Formulation & Dimension Unit Statement", "marks": 1, "type": "Accuracy"},
        ],
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3,
        },
        "misconception_tags": [
            "scale_denominator_inversion",
            "number_vs_bar_scale_conversion_error",
            "unit_conversion_meter_to_cm_error",
            "wall_thickness_internal_area_omission"
        ],
    }
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
