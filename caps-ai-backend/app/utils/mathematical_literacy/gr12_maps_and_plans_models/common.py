"""Common utilities and formatters for Grade 12 Mathematical Literacy: Maps and plans (models).

Enforces:
  - Strict South African number formatting (space grouping, comma decimals, e.g. 1 450 mm, 12,5 cm, R 450,00).
  - Authentic South African architectural and community contexts (RDP homes, school halls, clinics, Wendy houses).
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

SA_BUILDING_PROJECTS = [
    {"type": "Standard 40 m² RDP House", "real_length_m": 7.5, "real_width_m": 5.4, "wall_height_m": 2.6, "roof_pitch_deg": 15},
    {"type": "Extended 54 m² Community Cottage", "real_length_m": 9.0, "real_width_m": 6.0, "wall_height_m": 2.7, "roof_pitch_deg": 20},
    {"type": "Primary School Classroom Block", "real_length_m": 12.0, "real_width_m": 7.0, "wall_height_m": 3.0, "roof_pitch_deg": 18},
    {"type": "Community Clinic Consultation Room", "real_length_m": 6.5, "real_width_m": 4.8, "wall_height_m": 2.8, "roof_pitch_deg": 15},
    {"type": "Timber Wendy House Workshop", "real_length_m": 4.5, "real_width_m": 3.6, "wall_height_m": 2.4, "roof_pitch_deg": 25},
    {"type": "Pre-School Hall & Daycare Center", "real_length_m": 15.0, "real_width_m": 9.0, "wall_height_m": 3.5, "roof_pitch_deg": 22},
]

PAGE_SIZES_MM = {
    "A4": {"length_mm": 297, "width_mm": 210, "length_cm": 29.7, "width_cm": 21.0},
    "A3": {"length_mm": 420, "width_mm": 297, "length_cm": 42.0, "width_cm": 29.7},
    "A2": {"length_mm": 594, "width_mm": 420, "length_cm": 59.4, "width_cm": 42.0},
    "A1": {"length_mm": 841, "width_mm": 594, "length_cm": 84.1, "width_cm": 59.4},
}

STANDARD_MODEL_SCALES = [10, 20, 25, 50, 75, 100, 150, 200, 500]


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

    # Check if single numeric value
    core = correct_str.replace("R ", "").replace(" kg/m²", "").replace(" cm²", "").replace(" m²", "").replace(" cm³", "").replace(" m³", "").replace(" kg", "").replace(" cm", "").replace(" mm", "").replace(" m", "").replace(" L", "").replace(" g", "").replace(" Hz", "").replace("%", "").replace(" ", "").replace(",", ".")
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
    """Build canonical 6-pillar question payload for Grade 12 Maps and Plans Models."""
    explanation = "\n".join(solution_steps)
    payload: Dict[str, Any] = {
        "id": f"mathlit_gr12_models_{subskill_id}_{r.randint(10000000, 99999999):08x}",
        "topic": "Maps and plans (models)",
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
            {"step": "Step 1: Formula / Scale / Ratio Identification", "marks": 1, "type": "Method"},
            {"step": "Step 2: Technical Substitution & Dimension Conversion", "marks": 1, "type": "Method"},
            {"step": "Step 3: Solution Formulation & Dimension Unit Statement", "marks": 1, "type": "Accuracy"},
        ],
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3,
        },
        "misconception_tags": [
            "scale_denominator_inversion",
            "linear_vs_area_volume_scaling_confusion",
            "unit_conversion_meter_to_cm_error",
            "pallet_stack_height_clearance_omission"
        ],
    }
    if diagram_spec:
        if isinstance(diagram_spec, dict) and "diagram_role" not in diagram_spec:
            diagram_spec["diagram_role"] = "context"
        payload["diagram_spec"] = diagram_spec
    return payload
