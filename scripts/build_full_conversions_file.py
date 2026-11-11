# Builder script that writes the comprehensive conversions_time_generator.py

content = '''"""Grade 10 Mathematical Literacy - Term 1: Conversions and Time Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/01. Conversions and time.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering length, mass, volume, cooking,
    imperial conversions, temperature, time conversions, timetables, and speed.
  - Full step-by-step pedagogical worked solutions showing the thought process:
      Step 1: Unit relationship & thought process (multiply vs divide)
      Step 2: Method setup with explicit mark allocation [1 Mark: Method]
      Step 3: Final answer with units and explicit mark allocation [1 Mark: Accuracy]
  - No formulas provided in prompts for standard curriculum units (temperature, metric, cooking, speed).
  - Clean LaTeX and unicode (°C, °F) that never triggers KaTeX parse errors or red font.
  - Calibrated, strictly unique 4-distractor multiple-choice options with zero identical options.
  - 3-tier diagnostic pre-baked hints for scaffolded remediation.
"""

from __future__ import annotations

import random
import re
import uuid
from typing import Any, Dict, List, Optional, Tuple

SUBSKILLS = [
    # Cluster 1: Metric Length Conversions (8 Archetypes)
    "conv_len_mm_to_cm",
    "conv_len_cm_to_mm",
    "conv_len_cm_to_m",
    "conv_len_m_to_cm",
    "conv_len_mm_to_m",
    "conv_len_m_to_mm",
    "conv_len_m_to_km",
    "conv_len_km_to_m",

    # Cluster 2: Metric Mass Conversions (7 Archetypes)
    "conv_mass_g_to_kg",
    "conv_mass_kg_to_g",
    "conv_mass_kg_to_tonne",
    "conv_mass_tonne_to_kg",
    "conv_mass_mg_to_g",
    "conv_mass_g_to_mg",
    "conv_mass_multi_step_tonne_to_g",

    # Cluster 3: Metric Volume & Liquid Capacity (7 Archetypes)
    "conv_vol_ml_to_l",
    "conv_vol_l_to_ml",
    "conv_vol_l_to_kl",
    "conv_vol_kl_to_l",
    "conv_vol_cm3_to_ml",
    "conv_vol_cm3_to_l",
    "conv_vol_m3_to_l",

    # Cluster 4: Kitchen Cooking & Recipe Conversions (6 Archetypes)
    "cook_tsp_to_ml",
    "cook_tbsp_to_ml",
    "cook_tbsp_to_tsp",
    "cook_cups_to_ml",
    "cook_recipe_scaling",
    "cook_dry_cups_to_grams",

    # Cluster 5: Imperial to Metric Contexts (2 Archetypes)
    "conv_imperial_inches_feet_to_cm_m",
    "conv_imperial_pounds_gallons_to_metric",

    # Cluster 6: Temperature Conversions (5 Archetypes)
    "temp_celsius_to_fahrenheit",
    "temp_fahrenheit_to_celsius",
    "temp_baking_oven_setting",
    "temp_weather_comparison",
    "temp_negative_freezing_c_to_f",

    # Cluster 7: Time Calculations, Timetables & Speed (17 Archetypes)
    "time_unit_seconds_minutes",
    "time_unit_minutes_hours",
    "time_unit_hours_days",
    "time_unit_days_weeks_months",
    "time_format_12h_to_24h",
    "time_format_24h_to_12h",
    "time_decimal_to_hours_minutes",
    "time_elapsed_same_day",
    "time_elapsed_crossing_midnight",
    "time_elapsed_multi_day",
    "time_schedule_bus_timetable",
    "time_schedule_train_flight",
    "time_tide_table_reading",
    "speed_distance_time_travel_duration",
    "speed_unit_conversion_kmh_to_ms",
    "time_international_time_zones",
    "time_pace_speed_running",
]

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina"
]


def _fmt(val: float | int) -> str:
    """Format numbers using South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _build_options(answer: str, r: random.Random) -> Tuple[List[str], int]:
    """Generates 4 realistic, distinct options for multiple-choice rendering."""
    ans = answer.strip()
    distractors: List[str] = []

    # 1. 12-hour or 24-hour clock time (e.g., '14:35' or '02:35 p.m.')
    m_clock = re.match(r"^([0-9]{1,2}):([0-9]{2})(?:\s*(a\.m\.|p\.m\.|am|pm))?$", ans, re.I)
    if m_clock:
        hh = int(m_clock.group(1))
        mm = int(m_clock.group(2))
        merid = m_clock.group(3) or ""
        clk_cands = [
            f"{(hh + 1) % 24:02d}:{mm:02d}{' ' + merid if merid else ''}",
            f"{(hh - 1) % 24:02d}:{mm:02d}{' ' + merid if merid else ''}",
            f"{hh:02d}:{(mm + 15) % 60:02d}{' ' + merid if merid else ''}",
            f"{hh:02d}:{abs(mm - 15):02d}{' ' + merid if merid else ''}",
            f"{(hh + 2) % 24:02d}:{mm:02d}{' ' + merid if merid else ''}",
            f"{(hh + 12) % 24:02d}:{mm:02d}",
        ]
        for c in clk_cands:
            if c != ans and c not in distractors:
                distractors.append(c)

    # 2. Elapsed time with hours and minutes (e.g., '4 hours and 25 minutes' or '52,5 hours')
    elif "hour" in ans.lower():
        m_dec_hours = re.match(r"^(-?[0-9]+(?:[.,][0-9]+)?)\s*(hours?|hrs?)$", ans, re.I)
        if m_dec_hours:
            val_h = float(m_dec_hours.group(1).replace(",", "."))
            unit_h = m_dec_hours.group(2)
            cands_h = [val_h + 1, val_h - 1, val_h + 2, max(0.5, val_h - 2), val_h + 0.5, val_h - 0.5]
            for ch in cands_h:
                lbl = f"{_fmt(round(ch, 2))} {unit_h}"
                if lbl != ans and lbl not in distractors:
                    distractors.append(lbl)
        else:
            m_time = re.match(r"^([0-9]+)\s*hours?(?:\s*(?:and)?\s*([0-9]+)\s*minutes?)?", ans, re.I)
            if m_time:
                h = int(m_time.group(1))
                m = int(m_time.group(2)) if m_time.group(2) else 0
                t_cands = [
                    f"{h + 1} hours and {m} minutes" if m else f"{h + 1} hours",
                    f"{max(0, h - 1)} hours and {m} minutes" if m else f"{max(1, h - 1)} hours",
                    f"{h} hours and {(m + 15) % 60} minutes",
                    f"{h} hours and {abs(m - 15)} minutes",
                    f"{h + 2} hours and {m} minutes" if m else f"{h + 2} hours",
                ]
                for c in t_cands:
                    if c != ans and c not in distractors:
                        distractors.append(c)

    # 3. Numeric value with units (including negative numbers and decimal commas)
    else:
        m_num = re.match(r"^(-?[0-9]+(?:[.,][0-9]+)?)\s*(.*)$", ans)
        if m_num:
            num_str = m_num.group(1).replace(",", ".")
            unit = m_num.group(2).strip()
            try:
                val = float(num_str)
                is_neg = val < 0
                cands: List[float] = []
                if is_neg:
                    cands = [val - 5, val + 5, -val, val - 10, val + 10, val * 1.5]
                elif val < 5:
                    cands = [val * 10, val / 10, val + 1, max(0.1, val - 1), val * 2, val + 0.5]
                elif val < 50:
                    cands = [val / 10, val * 10, val + 5, max(1.0, val - 5), val * 2, val / 2]
                else:
                    cands = [val / 10, val / 100, val * 10, val + 10, val - 10, val / 2]

                for c in cands:
                    c_str = _fmt(round(c, 2))
                    cand_label = f"{c_str} {unit}".strip()
                    if cand_label != ans and cand_label not in distractors:
                        distractors.append(cand_label)
            except ValueError:
                pass

    # Fallback for city comparison or descriptive answers
    if len(distractors) < 3:
        if "durban" in ans.lower() or "phoenix" in ans.lower():
            diff_match = re.search(r"([0-9]+(?:,[0-9]+)?)", ans)
            diff_val = diff_match.group(1) if diff_match else "9,6"
            distractors = [
                f"Phoenix (USA) (by {diff_val} °F)",
                f"Durban (by {diff_val} °F)",
                "Both cities had the same temperature",
                f"Durban (by 15 °F)"
            ]
            distractors = [d for d in distractors if d != ans]
        else:
            offsets = [10, -10, 5, -5, 20, -20]
            for off in offsets:
                m_num_fallback = re.search(r"(-?[0-9]+(?:[.,][0-9]+)?)", ans)
                if m_num_fallback:
                    raw_n = float(m_num_fallback.group(1).replace(",", "."))
                    repl_n = _fmt(round(raw_n + off, 2))
                    cand_f = ans.replace(m_num_fallback.group(1), repl_n, 1)
                    if cand_f != ans and cand_f not in distractors:
                        distractors.append(cand_f)
                if len(distractors) >= 3:
                    break

    # Final guarantee: ensure exactly 3 distinct distractors
    idx_counter = 1
    while len(distractors) < 3:
        cand_pad = f"{ans} (Option {chr(65 + idx_counter)})"
        if cand_pad not in distractors and cand_pad != ans:
            distractors.append(cand_pad)
        idx_counter += 1

    final_opts = [ans] + distractors[:3]
    unique_opts: List[str] = []
    for opt in final_opts:
        if opt not in unique_opts:
            unique_opts.append(opt)
    while len(unique_opts) < 4:
        unique_opts.append(f"{ans} [Alt {len(unique_opts)}]")

    r.shuffle(unique_opts)
    return unique_opts, unique_opts.index(ans)


def _make_q(
    *,
    subskill: str,
    prompt: str,
    answer: str,
    sol: str,
    rubric: List[str],
    hints: Dict[str, str],
    marks: int = 2,
    difficulty: str = "medium",
    q_type: str = "math_short",
    options: Optional[List[str]] = None,
    correct_idx: Optional[int] = None,
) -> Dict[str, Any]:
    qid = f"mathlit10_time_{subskill}_{uuid.uuid4().hex[:8]}"
    if options is None:
        options, correct_idx = _build_options(answer, random.Random(hash(prompt) & 0xffffffff))

    return {
        "id": qid,
        "question_id": qid,
        "subskill": subskill,
        "question_family_id": f"mathlit10_time_{subskill}",
        "prompt": prompt,
        "question": prompt,
        "sample_answer": answer,
        "expected_answer": answer,
        "correct_answer": answer,
        "worked_solution": sol,
        "explanation": sol,
        "marking_schema": rubric,
        "grading_rubric": rubric,
        "hints": hints,
        "marks": marks,
        "total_marks": marks,
        "difficulty": difficulty,
        "modality": "math",
        "solution_type": "symbolic_steps" if q_type == "math_short" else "multiple_choice",
        "question_type": q_type,
        "options": options,
        "correct_index": correct_idx if correct_idx is not None else 0,
        "correct_idx": correct_idx if correct_idx is not None else 0,
        "caps_weight_percent": 15,
        "term": 1,
    }


# ===========================================================================
# CLUSTER 1: METRIC LENGTH CONVERSIONS (8 Archetypes)
# ===========================================================================

def _gen_conv_len_mm_to_cm(r: random.Random) -> Dict[str, Any]:
    val_mm = r.randint(15, 950)
    ans_cm = val_mm / 10.0
    name = r.choice(SA_NAMES)
    items = ["wire segment", "ribbon", "pencil", "tile spacer", "pipe fitting"]
    item = r.choice(items)
    prompt = f"{name} measured the length of a {item} to be **{val_mm} mm**.\n\nConvert this measurement to centimetres (**cm**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ cm}} = 10\\\\text{{ mm}}$\\n"
        f"• Converting from a smaller unit (\\\\text{{mm}}) to a larger unit (\\\\text{{cm}}) requires **division** by $10$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Length in cm}} = \\\\frac{{{val_mm}\\\\text{{ mm}}}}{{10}} = \\\\mathbf{{{_fmt(ans_cm)}\\\\text{{ cm}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing measurement by 10]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_cm)}\\\\text{{ cm}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_mm_to_cm",
        prompt=prompt,
        answer=f"{_fmt(ans_cm)} cm",
        sol=sol,
        rubric=[f"Method: {val_mm} ÷ 10 [1 Mark]", f"Accuracy: {_fmt(ans_cm)} cm [1 Mark]"],
        hints={
            "tier_1": "There are 10 millimetres in 1 centimetre (1 cm = 10 mm).",
            "tier_2": f"To convert from mm to cm, divide by 10: {val_mm} ÷ 10.",
            "tier_3": f"{val_mm} ÷ 10 = {_fmt(ans_cm)} cm."
        }
    )

def _gen_conv_len_cm_to_mm(r: random.Random) -> Dict[str, Any]:
    val_cm = round(r.uniform(2.5, 85.0), 1)
    ans_mm = round(val_cm * 10, 1)
    name = r.choice(SA_NAMES)
    prompt = f"{name} uses a ruler to measure a wooden dowel of length **{_fmt(val_cm)} cm**.\n\nConvert this length to millimetres (**mm**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ cm}} = 10\\\\text{{ mm}}$\\n"
        f"• Converting from a larger unit (\\\\text{{cm}}) to a smaller unit (\\\\text{{mm}}) requires **multiplication** by $10$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Length in mm}} = {_fmt(val_cm)}\\\\text{{ cm}} \\\\times 10 = \\\\mathbf{{{_fmt(ans_mm)}\\\\text{{ mm}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying measurement by 10]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_mm)}\\\\text{{ mm}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_cm_to_mm",
        prompt=prompt,
        answer=f"{_fmt(ans_mm)} mm",
        sol=sol,
        rubric=[f"Method: {_fmt(val_cm)} × 10 [1 Mark]", f"Accuracy: {_fmt(ans_mm)} mm [1 Mark]"],
        hints={
            "tier_1": "There are 10 millimetres in 1 centimetre (1 cm = 10 mm).",
            "tier_2": f"To convert from cm to mm, multiply by 10: {_fmt(val_cm)} × 10.",
            "tier_3": f"{_fmt(val_cm)} × 10 = {_fmt(ans_mm)} mm."
        }
    )

def _gen_conv_len_cm_to_m(r: random.Random) -> Dict[str, Any]:
    val_cm = r.randint(25, 850)
    ans_m = val_cm / 100.0
    name = r.choice(SA_NAMES)
    prompt = f"{name} measured the width of a study table as **{val_mm if 'val_mm' in locals() else val_cm} cm**.\n\nConvert this width to metres (**m**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ m}} = 100\\\\text{{ cm}}$\\n"
        f"• Converting from a smaller unit (\\\\text{{cm}}) to a larger unit (\\\\text{{m}}) requires **division** by $100$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Width in m}} = \\\\frac{{{val_cm}\\\\text{{ cm}}}}{{100}} = \\\\mathbf{{{_fmt(ans_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing measurement by 100]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_m)}\\\\text{{ m}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_cm_to_m",
        prompt=prompt,
        answer=f"{_fmt(ans_m)} m",
        sol=sol,
        rubric=[f"Method: {val_cm} ÷ 100 [1 Mark]", f"Accuracy: {_fmt(ans_m)} m [1 Mark]"],
        hints={
            "tier_1": "There are 100 centimetres in 1 metre (1 m = 100 cm).",
            "tier_2": f"Divide {val_cm} by 100.",
            "tier_3": f"{val_cm} ÷ 100 = {_fmt(ans_m)} m."
        }
    )

def _gen_conv_len_m_to_cm(r: random.Random) -> Dict[str, Any]:
    val_m = round(r.uniform(1.2, 18.5), 2)
    ans_cm = round(val_m * 100, 1)
    prompt = f"A roll of fabric has a length of **{_fmt(val_m)} m**.\n\nConvert this length to centimetres (**cm**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ m}} = 100\\\\text{{ cm}}$\\n"
        f"• Converting from metres to centimetres requires **multiplication** by $100$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Length in cm}} = {_fmt(val_m)}\\\\text{{ m}} \\\\times 100 = \\\\mathbf{{{_fmt(ans_cm)}\\\\text{{ cm}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 100]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_cm)}\\\\text{{ cm}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_m_to_cm",
        prompt=prompt,
        answer=f"{_fmt(ans_cm)} cm",
        sol=sol,
        rubric=[f"Method: {_fmt(val_m)} × 100 [1 Mark]", f"Accuracy: {_fmt(ans_cm)} cm [1 Mark]"],
        hints={
            "tier_1": "1 metre = 100 centimetres.",
            "tier_2": f"Multiply {_fmt(val_m)} by 100.",
            "tier_3": f"{_fmt(val_m)} × 100 = {_fmt(ans_cm)} cm."
        }
    )

def _gen_conv_len_mm_to_m(r: random.Random) -> Dict[str, Any]:
    val_mm = r.randint(350, 4800)
    ans_m = val_mm / 1000.0
    prompt = f"An architectural building plan indicates an interior doorway clearance of **{val_mm} mm**.\n\nConvert this dimension to metres (**m**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ m}} = 1\\\\,000\\\\text{{ mm}}$\\n"
        f"• Converting from millimetres to metres requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Dimension in m}} = \\\\frac{{{val_mm}\\\\text{{ mm}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_m)}\\\\text{{ m}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_mm_to_m",
        prompt=prompt,
        answer=f"{_fmt(ans_m)} m",
        sol=sol,
        rubric=[f"Method: {val_mm} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_m)} m [1 Mark]"],
        hints={
            "tier_1": "There are 1 000 millimetres in 1 metre (1 m = 1 000 mm).",
            "tier_2": f"Divide {val_mm} by 1 000.",
            "tier_3": f"{val_mm} ÷ 1 000 = {_fmt(ans_m)} m."
        }
    )

def _gen_conv_len_m_to_mm(r: random.Random) -> Dict[str, Any]:
    val_m = round(r.uniform(0.35, 4.5), 2)
    ans_mm = round(val_m * 1000, 1)
    prompt = f"A carpenter measures a plank of timber as **{_fmt(val_m)} m**.\n\nConvert this length to millimetres (**mm**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ m}} = 1\\\\,000\\\\text{{ mm}}$\\n"
        f"• Converting from metres to millimetres requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Length in mm}} = {_fmt(val_m)}\\\\text{{ m}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_mm)}\\\\text{{ mm}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_mm)}\\\\text{{ mm}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_m_to_mm",
        prompt=prompt,
        answer=f"{_fmt(ans_mm)} mm",
        sol=sol,
        rubric=[f"Method: {_fmt(val_m)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_mm)} mm [1 Mark]"],
        hints={
            "tier_1": "1 metre = 1 000 millimetres.",
            "tier_2": f"Multiply {_fmt(val_m)} by 1 000.",
            "tier_3": f"{_fmt(val_m)} × 1 000 = {_fmt(ans_mm)} mm."
        }
    )

def _gen_conv_len_m_to_km(r: random.Random) -> Dict[str, Any]:
    val_m = r.randint(450, 18500)
    ans_km = val_m / 1000.0
    prompt = f"An athlete completes a morning cross-country run of **{val_m} m**.\n\nConvert this distance to kilometres (**km**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ km}} = 1\\\\,000\\\\text{{ m}}$\\n"
        f"• Converting from metres to kilometres requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Distance in km}} = \\\\frac{{{val_m}\\\\text{{ m}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_km)}\\\\text{{ km}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_km)}\\\\text{{ km}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_m_to_km",
        prompt=prompt,
        answer=f"{_fmt(ans_km)} km",
        sol=sol,
        rubric=[f"Method: {val_m} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_km)} km [1 Mark]"],
        hints={
            "tier_1": "There are 1 000 metres in 1 kilometre (1 km = 1 000 m).",
            "tier_2": f"Divide {val_m} by 1 000.",
            "tier_3": f"{val_m} ÷ 1 000 = {_fmt(ans_km)} km."
        }
    )

def _gen_conv_len_km_to_m(r: random.Random) -> Dict[str, Any]:
    val_km = round(r.uniform(1.2, 45.0), 2)
    ans_m = round(val_km * 1000, 1)
    prompt = f"The road distance from a township school to the regional library is **{_fmt(val_km)} km**.\n\nConvert this distance to metres (**m**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ km}} = 1\\\\,000\\\\text{{ m}}$\\n"
        f"• Converting from kilometres to metres requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Distance in m}} = {_fmt(val_km)}\\\\text{{ km}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_m)}\\\\text{{ m}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_len_km_to_m",
        prompt=prompt,
        answer=f"{_fmt(ans_m)} m",
        sol=sol,
        rubric=[f"Method: {_fmt(val_km)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_m)} m [1 Mark]"],
        hints={
            "tier_1": "1 kilometre = 1 000 metres.",
            "tier_2": f"Multiply {_fmt(val_km)} by 1 000.",
            "tier_3": f"{_fmt(val_km)} × 1 000 = {_fmt(ans_m)} m."
        }
    )
'''

with open('scripts/build_full_conversions_file.py', 'a', encoding='utf-8') as f:
    f.write(content)

print("Cluster 1 appended.")
