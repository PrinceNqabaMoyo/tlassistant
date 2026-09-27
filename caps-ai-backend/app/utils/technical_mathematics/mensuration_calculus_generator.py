"""Grade 11–12 Technical Mathematics — Mensuration & Trapezoidal Rule (Deterministic 6-Pillar Generator).
Covers numerical integration for irregular areas using the Trapezoidal Rule and Mid-ordinate Rule (Paper 2, Term 3).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# --------------------------------------------------------------------------- #
# Sub-Drill: Common Interval Width (h)
# --------------------------------------------------------------------------- #
def _build_interval_drill(r: random.Random) -> Dict[str, Any]:
    total_span = r.choice([20, 24, 30, 36, 40, 50, 60])
    num_intervals = r.choice([4, 5, 6, 8, 10])
    h = round(total_span / num_intervals, 2)
    num_ordinates = num_intervals + 1

    prompt = (
        f"An irregular cross-section has a total baseline width of ${total_span}\\text{{ m}}$. "
        f"Measurements of ordinates are taken across the span dividing it into **{num_intervals} equal intervals**.\n\n"
        f"1. How many ordinates ($y_1, y_2, \\dots$) were measured in total?\n"
        f"2. Calculate the common interval width ($h$)."
    )

    ans_latex = rf"\text{{Total ordinates: }} {num_ordinates}, \quad h = \frac{{{total_span}\\text{{ m}}}}{{{num_intervals}}} = {_fmt_sa(h)}\\text{{ m}}"

    marking_schema = {
        "total_marks": 2,
        "marking_points": [
            {"id": "mp1", "desc": f"Identify number of ordinates = intervals + 1 = {num_ordinates}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate common interval width h = {_fmt_sa(h)} m", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: For $n$ equal intervals, there are $n + 1$ boundary ordinates.",
        "tier_2": "The interval width is $h = \\frac{\\text{total width}}{\\text{number of intervals}}$.",
        "tier_3": f"Ordinates: {num_ordinates}. Interval width: $h = {total_span} / {num_intervals} = {_fmt_sa(h)}\\text{{ m}}$.",
    }

    return {
        "id": f"tech_mens_h_{r.randint(100000, 999999)}",
        "question_id": f"tech_mens_h_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "mensuration_interval_elementary",
        "learning_objective_id": "techmath_mensuration_interval",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["counted_intervals_instead_of_ordinates", "divided_by_ordinates_count"],
        "keywords": ["trapezoidal rule", "ordinates", "interval width", "mensuration"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_ordinate_interval",
        "difficulty": "easy",
        "marks": 2,
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Trapezoidal Formula Direct Application
# --------------------------------------------------------------------------- #
def _build_trapezoidal_formula_drill(r: random.Random) -> Dict[str, Any]:
    h = r.choice([2, 3, 4, 5])
    # 5 ordinates (4 intervals)
    y1 = r.choice([0, 1.2, 2.0, 3.5])
    y2 = r.choice([4.2, 5.0, 5.8, 6.4])
    y3 = r.choice([6.0, 7.2, 8.5, 9.0])
    y4 = r.choice([4.5, 5.5, 6.2, 7.0])
    y5 = r.choice([0, 1.0, 2.5, 3.0])

    ordinates = [y1, y2, y3, y4, y5]
    ends_sum = (y1 + y5) / 2
    middle_sum = y2 + y3 + y4
    area = round(h * (ends_sum + middle_sum), 2)

    prompt = (
        f"The following five ordinates were measured at equal intervals of $h = {h}\\text{{ m}}$:\n"
        f"$$y_1 = {_fmt_sa(y1)}\\text{{ m}}, \\quad y_2 = {_fmt_sa(y2)}\\text{{ m}}, \\quad "
        f"y_3 = {_fmt_sa(y3)}\\text{{ m}}, \\quad y_4 = {_fmt_sa(y4)}\\text{{ m}}, \\quad "
        f"y_5 = {_fmt_sa(y5)}\\text{{ m}}$$\n\n"
        f"Use the **Trapezoidal Rule** to approximate the area under this irregular curve."
    )

    ans_latex = (
        rf"\text{{Area}} = h \left[ \frac{{y_1 + y_5}}{{2}} + y_2 + y_3 + y_4 \right] = "
        rf"{h} \left[ \frac{{{_fmt_sa(y1)} + {_fmt_sa(y5)}}}{{2}} + {_fmt_sa(y2)} + {_fmt_sa(y3)} + {_fmt_sa(y4)} \right] "
        rf"= {_fmt_sa(area)}\text{{ m}}^2"
    )

    sample_answer = (
        f"Trapezoidal Rule Formula:\n"
        f"$$\\text{{Area}} \\approx h \\left[ \\frac{{y_1 + y_n}}{{2}} + y_2 + y_3 + \\dots + y_{{n-1}} \\right]$$\n\n"
        f"Substitution:\n"
        f"Ends average: $\\frac{{{_fmt_sa(y1)} + {_fmt_sa(y5)}}}{{2}} = {_fmt_sa(ends_sum)}$\n"
        f"Sum of intermediate ordinates: ${middle_sum:.2f}$\n"
        f"$$\\text{{Area}} = {h} \\times ({_fmt_sa(ends_sum)} + {middle_sum:.2f}) = {_fmt_sa(area)}\\text{{ m}}^2$$"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Trapezoidal Rule formula stated", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct calculation of (first + last) / 2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Sum of middle ordinates correctly added", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final area: {_fmt_sa(area)} m^2", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_square_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The first and last ordinates are averaged by dividing their sum by 2; intermediate ordinates are added fully.",
        "tier_2": "Formula: $\\text{Area} = h \\left[ \\frac{y_1 + y_n}{2} + \\sum y_{\\text{middle}} \\right]$.",
        "tier_3": f"Area = ${h} \\times ({_fmt_sa(ends_sum)} + {_fmt_sa(middle_sum)}) = {_fmt_sa(area)}\\text{{ m}}^2$.",
    }

    return {
        "id": f"tech_mens_trap_{r.randint(100000, 999999)}",
        "question_id": f"tech_mens_trap_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "trapezoidal_rule_elementary",
        "learning_objective_id": "techmath_trapezoidal_formula",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_half_first_last_ordinates", "added_all_ordinates_equally"],
        "keywords": ["trapezoidal rule", "mensuration", "irregular area", "integration"],
        "term": 3,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_trapezoidal_formula",
        "difficulty": "medium",
        "marks": 4,
    }


# --------------------------------------------------------------------------- #
# Compound: Authentic CAPS Exam Standard Mensuration & Volume (8 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_mensuration(r: random.Random) -> Dict[str, Any]:
    context = r.choice([
        ("railway embankment cutting", "gravel", 1.8),
        ("canal cross-section", "water", 1.0),
        ("highway culvert foundation", "concrete", 2.4),
        ("farm dam drainage ditch", "soil", 1.6),
    ])
    ctx_name, material, density = context

    # 6 ordinates (5 intervals)
    h = r.choice([3, 4, 5, 6])
    span = h * 5
    length = r.choice([25, 40, 50, 60, 80])

    y1 = r.choice([0, 1.5, 2.0])
    y2 = r.choice([4.2, 5.5, 6.0])
    y3 = r.choice([7.0, 8.4, 9.2])
    y4 = r.choice([6.5, 7.8, 8.0])
    y5 = r.choice([3.8, 4.5, 5.0])
    y6 = r.choice([0, 1.2, 2.0])

    ends_avg = round((y1 + y6) / 2, 2)
    middle_sum = round(y2 + y3 + y4 + y5, 2)
    area = round(h * (ends_avg + middle_sum), 2)
    volume = round(area * length, 2)
    mass_tons = round((volume * density), 1)

    prompt = (
        f"A civil engineering survey investigates the irregular cross-sectional area of a **{ctx_name}**.\n"
        f"The baseline span has a total width of ${span}\\text{{ m}}$ and is divided into **$5$ equal intervals**.\n\n"
        f"The measured boundary ordinates are:\n"
        f"$$y_1 = {_fmt_sa(y1)}\\text{{ m}}, \\quad y_2 = {_fmt_sa(y2)}\\text{{ m}}, \\quad "
        f"y_3 = {_fmt_sa(y3)}\\text{{ m}}, \\quad y_4 = {_fmt_sa(y4)}\\text{{ m}}, \\quad "
        f"y_5 = {_fmt_sa(y5)}\\text{{ m}}, \\quad y_6 = {_fmt_sa(y6)}\\text{{ m}}$$\n\n"
        f"1. Calculate the common interval width ($h$).\n"
        f"2. Use the **Trapezoidal Rule** to approximate the cross-sectional area ($A$) of the cutting.\n"
        f"3. If the cutting extends along a straight length of $L = {length}\\text{{ m}}$, calculate the total volume ($V$) of {material} excavated in $\\text{{m}}^3$.\n"
        f"4. Given that the density of the {material} is $\\rho = {_fmt_sa(density)}\\text{{ tonnes/m}}^3$, calculate the total mass in tonnes."
    )

    ans_latex = (
        rf"h = {h}\text{{ m}}, \quad A = {_fmt_sa(area)}\text{{ m}}^2, \quad "
        rf"V = {_fmt_sa(volume)}\text{{ m}}^3, \quad \text{{Mass}} = {_fmt_sa(mass_tons)}\text{{ tonnes}}"
    )

    sample_answer = (
        f"1. Interval Width:\n"
        f"   $$h = \\frac{{{span}\\text{{ m}}}}{{5}} = {h}\\text{{ m}}$$\n\n"
        f"2. Cross-sectional Area via Trapezoidal Rule:\n"
        f"   $$\\text{{Area}} = h \\left[ \\frac{{y_1 + y_6}}{{2}} + y_2 + y_3 + y_4 + y_5 \\right]$$\n"
        f"   Ends Average: $\\frac{{{_fmt_sa(y1)} + {_fmt_sa(y6)}}}{{2}} = {_fmt_sa(ends_avg)}$\n"
        f"   Sum of Middle Ordinates: ${y2} + {y3} + {y4} + {y5} = {_fmt_sa(middle_sum)}$\n"
        f"   $$\\text{{Area}} = {h} \\times ({_fmt_sa(ends_avg)} + {_fmt_sa(middle_sum)}) = {_fmt_sa(area)}\\text{{ m}}^2$$\n\n"
        f"3. Volume of Excavation:\n"
        f"   $$V = \\text{{Area}} \\times L = {_fmt_sa(area)}\\text{{ m}}^2 \\times {length}\\text{{ m}} = {_fmt_sa(volume)}\\text{{ m}}^3$$\n\n"
        f"4. Total Mass:\n"
        f"   $$\\text{{Mass}} = V \\times \\rho = {_fmt_sa(volume)} \\times {_fmt_sa(density)} = {_fmt_sa(mass_tons)}\\text{{ tonnes}}$$"
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate interval width h = {h} m", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "State Trapezoidal Rule formula", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Accurate calculation of (y1 + y6)/2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Sum of intermediate ordinates", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Cross-sectional area A = {_fmt_sa(area)} m^2", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Volume calculation: V = A x L = {_fmt_sa(volume)} m^3", "marks": 2, "editable": True},
            {"id": "mp7", "desc": f"Mass calculation: M = V x rho = {_fmt_sa(mass_tons)} tonnes", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Calculate $h = \\text{span} / 5$, then evaluate the Trapezoidal formula step by step.",
        "tier_2": "Area $A = h [ (y_1 + y_6)/2 + y_2 + y_3 + y_4 + y_5 ]$. Volume $V = A \\times L$. Mass = $V \\times \\rho$.",
        "tier_3": f"Area = {_fmt_sa(area)} m^2, Volume = {_fmt_sa(volume)} m^3, Mass = {_fmt_sa(mass_tons)} tonnes.",
    }

    return {
        "id": f"tech_mens_comp_{r.randint(100000, 999999)}",
        "question_id": f"tech_mens_comp_{r.randint(100000, 999999)}",
        "topic": "technical_mathematics_mensuration",
        "subskill": "irregular_mensuration_compound",
        "learning_objective_id": "techmath_mensuration_compound",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": [
            "omitted_half_first_last_ordinates",
            "divided_span_by_number_of_ordinates",
            "confused_area_and_volume_units",
        ],
        "keywords": ["mensuration", "trapezoidal rule", "irregular area", "volume", "density", "civil engineering"],
        "term": 3,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 12,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_mensuration,
    "elementary_ordinate_interval": _build_interval_drill,
    "elementary_trapezoidal_formula": _build_trapezoidal_formula_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11-12 Technical Mathematics Mensuration questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_mensuration)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
