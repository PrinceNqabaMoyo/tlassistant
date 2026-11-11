# Script to build the upgraded conversions_time_generator.py
# Grounded in curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/01. Conversions and time.md

code = '''"""Grade 10 Mathematical Literacy - Term 1: Conversions and Time Generator.

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
    if isinstance(val, int) or val.is_integer():
        return str(int(val))
    s = f"{val:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _build_options(answer: str, r: random.Random) -> Tuple[List[str], int]:
    """Generates 4 realistic, distinct options for multiple-choice rendering.
    
    Guarantees:
      1. len(options) == 4
      2. len(set(options)) == 4 (all options strictly unique)
      3. No generic '(Variant)' tokens.
    """
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
        # Check decimal hours first e.g. '52,5 hours'
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
    # e.g., '15,2 cm', '-14 °F', '250 ml', '1,75 m', '45 km/h'
    else:
        m_num = re.match(r"^(-?[0-9]+(?:[.,][0-9]+)?)\s*(.*)$", ans)
        if m_num:
            num_str = m_num.group(1).replace(",", ".")
            unit = m_num.group(2).strip()
            try:
                val = float(num_str)
                is_neg = val < 0
                # Realistic miscalculations:
                # - Inverse operation (multiply instead of divide)
                # - Order of magnitude error (x10 or /10)
                # - Addition shift (+5, -5, +10)
                # - Sign flip if negative
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

    # Fallback for semantic / descriptive answers (e.g. city names, dates, tide directions)
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
            # Generate deterministic distinct variations without 'Variant' tag
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
    # Ensure all 4 are strictly unique
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
'''

with open('scripts/build_upgraded_conversions_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Part 1 written successfully.")
