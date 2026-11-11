"""
Grade 7 Mathematics - Functions, Relationships & Graphs Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/END OF YEAR EXAM 2018.md (Q4.3, Q6.1)
and curriculum_docs_auto/Mathematics_Gr7/Term 2/3. Functions and relationships.md and Term 3 Graphs.

Archetypes Covered:
1. Input/Output Flow Diagrams (Forward output calculation and reverse input calculation, Exam Q4.3)
2. Tables of Values & Function Rules (Finding missing values, identifying relation rule)
3. Line Graph Interpretation (Linear vs non-linear, dependent vs independent variables, reading values, Exam Q6.1)
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


SUBSKILLS = [
    'flow_diagram_reverse_input',
    'flow_diagram_forward',
    'table_of_values_completion',
    'linear_vs_nonlinear_graph',
    'graph_dependent_variable',
    'graph_reading_total'
]


# ============================================================================
# ARCHETYPE 1: Flow Diagrams (Exam Q4.3)
# ============================================================================

def _generate_flow_diagram_question(rng: random.Random, force_reverse: Optional[bool] = None) -> Dict[str, Any]:
    """
    Input/output algebraic flow diagram with rule: y = m*x + c or y = m*x - c.
    Exam Q4.3: Rule 3x - 2.
    Given input 1 -> output 1.
    Given input 2 -> output 4.
    Find missing input for output 13 -> x = (13 + 2)/3 = 5.
    Find missing output for input 0 -> y = 3(0) - 2 = -2.
    """
    m = rng.choice([2, 3, 4, 5])
    op_is_sub = rng.choice([True, False])
    c = rng.randint(1, 6)

    # Rule string
    if op_is_sub:
        rule_latex = f"{m}x - {c}"
        calc_forward = lambda x: m * x - c
        calc_reverse = lambda y: (y + c) // m
    else:
        rule_latex = f"{m}x + {c}"
        calc_forward = lambda x: m * x + c
        calc_reverse = lambda y: (y - c) // m

    # Sub-case: reverse calculation (find unknown input x given output y)
    # or forward calculation (find unknown output y given input x)
    is_reverse = force_reverse if force_reverse is not None else rng.choice([True, False])

    if is_reverse:
        target_x = rng.randint(3, 9)
        given_y = calc_forward(target_x)
        prompt = (
            f"An algebraic flow diagram uses the rule:\n\n"
            f"\\[ \\text{{Input }} (x) \\longrightarrow [ \\times {m} \\text{{ then }} "
            f"{'- ' + str(c) if op_is_sub else '+ ' + str(c)} ] \\longrightarrow \\text{{Output }} (y) \\]\n\n"
            f"If the output value is \\(y = {given_y}\\), determine the corresponding input value \\(x\\)."
        )
        if op_is_sub:
            sol = (
                f"Step 1: Set up the equation from the rule:\n"
                f"\\({m}x - {c} = {given_y}\\)\n\n"
                f"Step 2: Apply the inverse operations (add {c}, then divide by {m}):\n"
                f"\\({m}x = {given_y} + {c} = {given_y + c}\\)\n\n"
                f"Step 3: Divide by {m}:\n"
                f"\\(x = \\frac{{{given_y + c}}}{{{m}}} = {target_x}\\)."
            )
            t2 = f"Use inverse operations: add {c} to the output {given_y}, then divide by {m}."
            t3 = f"({given_y} + {c}) ÷ {m} = {given_y + c} ÷ {m} = {target_x}."
        else:
            sol = (
                f"Step 1: Set up the equation from the rule:\n"
                f"\\({m}x + {c} = {given_y}\\)\n\n"
                f"Step 2: Apply the inverse operations (subtract {c}, then divide by {m}):\n"
                f"\\({m}x = {given_y} - {c} = {given_y - c}\\)\n\n"
                f"Step 3: Divide by {m}:\n"
                f"\\(x = \\frac{{{given_y - c}}}{{{m}}} = {target_x}\\)."
            )
            t2 = f"Use inverse operations: subtract {c} from the output {given_y}, then divide by {m}."
            t3 = f"({given_y} - {c}) ÷ {m} = {given_y - c} ÷ {m} = {target_x}."

        correct_ans = str(target_x)
        ans_latex = f"x = {target_x}"
        subskill = "flow_diagram_reverse_input"
    else:
        given_x = rng.choice([0, rng.randint(6, 12)])
        target_y = calc_forward(given_x)
        prompt = (
            f"An algebraic flow diagram uses the rule:\n\n"
            f"\\[ \\text{{Input }} (x) \\longrightarrow [ \\times {m} \\text{{ then }} "
            f"{'- ' + str(c) if op_is_sub else '+ ' + str(c)} ] \\longrightarrow \\text{{Output }} (y) \\]\n\n"
            f"Determine the output value \\(y\\) when the input is \\(x = {given_x}\\)."
        )
        if op_is_sub:
            sol = (
                f"Step 1: Substitute \\(x = {given_x}\\) into the rule \\({m}x - {c}\\):\n"
                f"\\(y = {m}({given_x}) - {c}\\)\n\n"
                f"Step 2: Multiply first:\n"
                f"\\(y = {m * given_x} - {c}\\)\n\n"
                f"Step 3: Subtract:\n"
                f"\\(y = {target_y}\\)."
            )
            t2 = f"Multiply the input {given_x} by {m}, then subtract {c}."
            t3 = f"{m} × {given_x} - {c} = {m * given_x} - {c} = {target_y}."
        else:
            sol = (
                f"Step 1: Substitute \\(x = {given_x}\\) into the rule \\({m}x + {c}\\):\n"
                f"\\(y = {m}({given_x}) + {c}\\)\n\n"
                f"Step 2: Multiply first:\n"
                f"\\(y = {m * given_x} + {c}\\)\n\n"
                f"Step 3: Add:\n"
                f"\\(y = {target_y}\\)."
            )
            t2 = f"Multiply the input {given_x} by {m}, then add {c}."
            t3 = f"{m} × {given_x} + {c} = {m * given_x} + {c} = {target_y}."

        correct_ans = str(target_y)
        ans_latex = f"y = {target_y}"
        subskill = "flow_diagram_forward_output"

    return {
        "id": f"g7_math_flow_diag_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": correct_ans,
        "answer_latex": ans_latex,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "learning_objective_id": "math_g7_functions_flow_diagrams",
        "misconception_tags": [
            "input_output_reversal",
            "operator_precedence_in_rule",
            "arithmetic_calculation_error"
        ],
        "diagnostic_tags": ["functions", "relationships", "flow_diagrams"],
        "minimum_mastery_score": 75,
        "keywords": ["flow diagram", "input", "output", "rule", "inverse operations"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct substitution into formula or inverse formulation", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct final numerical value ({correct_ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Identify whether you are moving forward from input to output, or working backwards using inverse operations.",
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# ARCHETYPE 2: Table of Values & Finding the Rule
# ============================================================================

def _generate_table_of_values_question(rng: random.Random) -> Dict[str, Any]:
    """
    Function table with x and y values.
    Students determine the missing value in the table or the general rule.
    """
    m = rng.choice([2, 3, 4, 6])
    c = rng.choice([1, 2, 3, 5])
    op_is_sub = rng.choice([True, False])

    if op_is_sub:
        fn = lambda x: m * x - c
        rule_str = f"y = {m}x - {c}"
    else:
        fn = lambda x: m * x + c
        rule_str = f"y = {m}x + {c}"

    x_vals = [1, 2, 3, 4, 10]
    y_vals = [fn(x) for x in x_vals]

    # Ask for the value at x = 10
    missing_idx = 4
    x_missing = x_vals[missing_idx]
    y_missing = y_vals[missing_idx]

    prompt = (
        f"Study the table of values below which follows a consistent linear rule:\n\n"
        f"| \\(x\\) | 1 | 2 | 3 | 4 | {x_missing} |\n"
        f"| :---: | :---: | :---: | :---: | :---: | :---: |\n"
        f"| \\(y\\) | {y_vals[0]} | {y_vals[1]} | {y_vals[2]} | {y_vals[3]} | ? |\n\n"
        f"Determine the missing output value \\(y\\) when \\(x = {x_missing}\\)."
    )

    diff = y_vals[1] - y_vals[0]
    calc_expr = f"({m} \\times {x_missing}) - {c}" if op_is_sub else f"({m} \\times {x_missing}) + {c}"
    sol = (
        f"Step 1: Find the common difference in \\(y\\) as \\(x\\) increases by 1:\n"
        f"\\({y_vals[1]} - {y_vals[0]} = {diff}\\). Therefore, the rule involves multiplying by {diff}.\n\n"
        f"Step 2: Check constant term:\n"
        f"For \\(x = 1\\), \\({diff} \\times 1 = {diff}\\). Since \\(y = {y_vals[0]}\\), the rule is \\({rule_str}\\).\n\n"
        f"Step 3: Calculate \\(y\\) when \\(x = {x_missing}\\):\n"
        f"\\(y = {calc_expr} = {y_missing}\\)."
    )

    return {
        "id": f"g7_math_table_values_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(y_missing),
        "answer_latex": f"y = {y_missing}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "table_of_values_completion",
        "learning_objective_id": "math_g7_functions_table_completion",
        "misconception_tags": [
            "pattern_additive_continuation_error",
            "operator_precedence_in_rule"
        ],
        "diagnostic_tags": ["functions", "tables", "linear_rules"],
        "minimum_mastery_score": 75,
        "keywords": ["table of values", "linear rule", "missing term", "input output"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Deducing linear rate of change or functional rule", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct value for y when x = {x_missing} ({y_missing})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Observe how much the y-value increases by each time x goes up by 1.",
            "tier_2": f"The rate of increase is {diff}. Use the general rule {rule_str} to find the value for x = {x_missing}.",
            "tier_3": f"Substitute x = {x_missing}: {rule_str.replace('x', f'({x_missing})')} = {y_missing}."
        }
    }


# ============================================================================
# ARCHETYPE 3: Line Graph Interpretation (Exam Q6.1)
# ============================================================================

def _generate_line_graph_question(rng: random.Random, target_subskill: Optional[str] = None) -> Dict[str, Any]:
    """
    Interpretation of real-world line graphs.
    Dynamic multi-seed scenarios:
    - Linear vs non-linear
    - Dependent vs independent variable
    - Reading values / total calculation
    """
    # Subskill 1: Dependent vs independent variable
    dep_scenarios = [
        ("the average daily temperature recorded over consecutive months of the year in Bloemfontein", "Temperature (°C)", "Months of the year", "vertical", "horizontal"),
        ("the distance travelled by a long-distance bus from Durban to Johannesburg over time", "Distance travelled (km)", "Time elapsed (hours)", "vertical", "horizontal"),
        ("the volume of water remaining in a municipal reservoir in Gqeberha over several weeks of drought", "Water volume (megalitres)", "Time (weeks)", "vertical", "horizontal"),
        ("the total cost charged for electricity usage based on the number of kilowatt-hours consumed", "Total electricity cost (Rands)", "Units consumed (kWh)", "vertical", "horizontal"),
        ("the height of a sunflower recorded each week after germination", "Height of sunflower (cm)", "Time (weeks)", "vertical", "horizontal"),
        ("the heart rate of an athlete monitored during a 30-minute training session", "Heart rate (beats per minute)", "Exercise duration (minutes)", "vertical", "horizontal")
    ]
    ctx_desc, dep_var, indep_var, dep_axis, indep_axis = rng.choice(dep_scenarios)
    dep_prompt = (
        f"A line graph displays {ctx_desc}.\n\n"
        f"Which axis ({dep_axis} or {indep_axis}) and which variable represents the **dependent variable**?"
    )
    dep_correct = f"{dep_axis.capitalize()} axis ({dep_var})"
    dep_options = [
        f"{dep_axis.capitalize()} axis ({dep_var})",
        f"{indep_axis.capitalize()} axis ({indep_var})",
        "Neither axis (both are independent)",
        "Both axes simultaneously"
    ]
    dep_scen = {
        "subskill": "graph_dependent_variable",
        "sub_type": "dependent_variable",
        "prompt": dep_prompt,
        "correct": dep_correct,
        "options": dep_options,
        "explanation": f"In authentic Cartesian graphs, the independent variable ({indep_var}) is placed on the horizontal axis (x-axis), while the dependent variable ({dep_var}) is placed on the vertical axis (y-axis).",
        "h1": f"Ask yourself: which variable depends on the other? Does {dep_var} depend on {indep_var}?",
        "h2": f"The dependent variable is the measured quantity plotted on the vertical y-axis.",
        "h3": f"The {dep_axis} axis ({dep_var}) represents the dependent variable."
    }

    # Subskill 2: Linear vs non-linear
    is_linear = rng.choice([True, False])
    if is_linear:
        d = rng.choice([3, 4, 5, 8, 10, 15])
        s = rng.choice([2, 5, 10, 12])
        w = [s, s + d, s + 2 * d, s + 3 * d]
        obj = rng.choice(["a delivery cyclist riding at constant speed", "water being poured at a steady rate into a cylindrical container", "a savings balance with equal weekly deposits"])
        unit = rng.choice(["km", "cm", "Rands"])
        ln_prompt = (
            f"A line graph tracking {obj} records values across 4 consecutive stages: Stage 1 ({w[0]} {unit}), Stage 2 ({w[1]} {unit}), Stage 3 ({w[2]} {unit}), Stage 4 ({w[3]} {unit}).\n\n"
            f"Is this graph **linear** or **non-linear**, and what is the mathematical reason?"
        )
        ln_correct = f"Linear, because the rate of change is constant ({d} {unit} per stage, forming a single straight line)"
        ln_options = [
            f"Linear, because the rate of change is constant ({d} {unit} per stage, forming a single straight line)",
            f"Non-linear, because the numbers are increasing",
            f"Linear, simply because the points are joined by line segments",
            f"Non-linear, because the starting value is not zero"
        ]
        ln_expl = f"A graph is linear when the rate of change is constant and forms a single continuous straight line. The difference between every consecutive stage is exactly {d} {unit} ({w[1]}-{w[0]} = {w[2]}-{w[1]} = {w[3]}-{w[2]} = {d}), so the relationship is linear."
    else:
        diffs = rng.choice([(2, 5, 9), (3, 7, 12), (1, 4, 10), (4, 10, 18)])
        s = rng.choice([2, 5, 8])
        w = [s, s + diffs[0], s + diffs[0] + diffs[1], s + diffs[0] + diffs[1] + diffs[2]]
        obj = rng.choice(["a growing maize seedling", "a bacteria culture multiplying in a petri dish", "a vehicle accelerating from rest"])
        unit = rng.choice(["cm", "cells", "km/h"])
        ln_prompt = (
            f"A line graph tracking {obj} records values across 4 consecutive stages: Stage 1 ({w[0]} {unit}), Stage 2 ({w[1]} {unit}), Stage 3 ({w[2]} {unit}), Stage 4 ({w[3]} {unit}).\n\n"
            f"Is this graph **linear** or **non-linear**, and what is the mathematical reason?"
        )
        ln_correct = f"Non-linear, because the rate of change is not constant (differences are {diffs[0]}, {diffs[1]}, and {diffs[2]} {unit})"
        ln_options = [
            f"Non-linear, because the rate of change is not constant (differences are {diffs[0]}, {diffs[1]}, and {diffs[2]} {unit})",
            f"Linear, because all the measured values are positive",
            f"Linear, because the graph slopes upwards",
            f"Non-linear, because time cannot be plotted on the x-axis"
        ]
        ln_expl = f"A graph is linear only if it has a constant rate of change and forms a single continuous straight line. Here the differences between consecutive stages are {diffs[0]} {unit}, {diffs[1]} {unit}, and {diffs[2]} {unit} (changing rate of growth), making it non-linear."
    ln_scen = {
        "subskill": "linear_vs_nonlinear_graph",
        "sub_type": "linear_or_nonlinear",
        "prompt": ln_prompt,
        "correct": ln_correct,
        "options": ln_options,
        "explanation": ln_expl,
        "h1": "Look at the differences between consecutive values at each stage.",
        "h2": "A linear graph must have a constant difference (constant gradient) forming a single straight line.",
        "h3": ln_correct
    }

    # Subskill 3: Reading values and summing
    scenarios_total = [
        ("learner absenteeism in a Grade 7 class over four terms", "days", ["Term 1", "Term 2", "Term 3", "Term 4"]),
        ("monthly rainfall recorded at a weather station in Polokwane over four months", "mm", ["January", "February", "March", "April"]),
        ("the number of library books borrowed by Grade 7 learners over four weeks", "books", ["Week 1", "Week 2", "Week 3", "Week 4"]),
        ("the mass of recyclable plastic collected by a school green club over four cycles", "kg", ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"])
    ]
    tot_ctx, tot_unit, labels = rng.choice(scenarios_total)
    vals = [rng.randint(6, 28) for _ in range(4)]
    total_val = sum(vals)
    val_strs = [f"{labels[i]}: {vals[i]} {tot_unit}" for i in range(4)]
    rd_prompt = (
        f"A line graph tracks {tot_ctx}:\n"
        f"{', '.join(val_strs)}.\n\n"
        f"Calculate the total number of {tot_unit} recorded across all four periods."
    )
    rd_correct = str(total_val)
    wrongs = [str(total_val + offset) for offset in [-5, 5, -10, 10, -2, 3] if total_val + offset != total_val]
    rng.shuffle(wrongs)
    rd_options = [rd_correct] + wrongs[:3]
    rd_expl = f"Total {tot_unit} = {' + '.join(str(v) for v in vals)} = {total_val} {tot_unit}."
    rd_scen = {
        "subskill": "graph_reading_total",
        "sub_type": "reading_and_summing",
        "prompt": rd_prompt,
        "correct": rd_correct,
        "options": rd_options,
        "explanation": rd_expl,
        "h1": f"Add the values recorded for all four periods: {' + '.join(str(v) for v in vals)}.",
        "h2": f"Sum all values carefully: {vals[0]} + {vals[1]} = {vals[0]+vals[1]}.",
        "h3": f"Final sum is {total_val}."
    }

    scenarios = [dep_scen, ln_scen, rd_scen]
    if target_subskill:
        matched = [s for s in scenarios if s.get("subskill") == target_subskill or s.get("sub_type") == target_subskill]
        scen = matched[0] if matched else rng.choice(scenarios)
    else:
        scen = rng.choice(scenarios)

    options = list(scen["options"])
    rng.shuffle(options)
    return {
        "id": f"g7_math_graph_interp_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": scen["prompt"],
        "prompt_latex": scen["prompt"],
        "options": options,
        "options_latex": options,
        "answer_mode": "choice",
        "correct_answer": scen["correct"],
        "answer_latex": scen["correct"],
        "explanation": scen["explanation"],
        "canonical_solution": scen["explanation"],
        "marks": 2,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": scen["subskill"],
        "learning_objective_id": "math_g7_graphs_interpretation",
        "misconception_tags": [
            "independent_dependent_inversion",
            "linear_nonlinear_confusion"
        ],
        "diagnostic_tags": ["graphs", "data_interpretation", "variables"],
        "minimum_mastery_score": 75,
        "keywords": ["line graph", "linear", "non-linear", "dependent variable", "independent variable"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate interpretation of graphical components", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct classification or total calculation", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": scen["h1"],
            "tier_2": scen["h2"],
            "tier_3": scen["h3"]
        }
    }


# ============================================================================
# MASTER GENERATE FUNCTION (6-Pillar Contract)
# ============================================================================

def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Functions, Relationships & Graphs Generator.
    Supports atomic micro-drills:
    - flow_diagram_reverse_input
    - flow_diagram_forward
    - table_of_values_completion
    - linear_vs_nonlinear_graph
    - graph_dependent_variable
    - graph_reading_total
    """
    rng = _rng(seed)
    questions = []

    target_sub = str(subskill or "").strip().lower()

    def _build_one(sub_name: str) -> Dict[str, Any]:
        if "reverse" in sub_name:
            return _generate_flow_diagram_question(rng, force_reverse=True)
        if "forward" in sub_name or "flow" in sub_name:
            return _generate_flow_diagram_question(rng, force_reverse=False)
        if "table" in sub_name:
            return _generate_table_of_values_question(rng)
        if "linear" in sub_name or "graph" in sub_name or "dependent" in sub_name or "reading" in sub_name:
            return _generate_line_graph_question(rng, target_subskill=sub_name)
        return _generate_flow_diagram_question(rng)

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        for _ in range(count):
            questions.append(_build_one(target_sub))
        return questions

    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(_build_one(sub))

    return questions
