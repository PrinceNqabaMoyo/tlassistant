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


# ============================================================================
# ARCHETYPE 1: Flow Diagrams (Exam Q4.3)
# ============================================================================

def _generate_flow_diagram_question(rng: random.Random) -> Dict[str, Any]:
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
    is_reverse = rng.choice([True, False])

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

    table_rows = [
        f"\\(x\\) & 1 & 2 & 3 & 4 & {x_missing} \\\\",
        f"\\(y\\) & {y_vals[0]} & {y_vals[1]} & {y_vals[2]} & {y_vals[3]} & ? \\\\"
    ]
    table_latex = (
        "\\begin{array}{|c|c|c|c|c|c|}\n\\hline\n"
        + "\n\\hline\n".join(table_rows)
        + "\n\\hline\n\\end{array}"
    )

    prompt = (
        f"Study the table of values below which follows a consistent linear rule:\n\n"
        f"\\[\n{table_latex}\n\\]\n\n"
        f"Determine the missing output value \\(y\\) when \\(x = {x_missing}\\)."
    )

    diff = y_vals[1] - y_vals[0]
    sol = (
        f"Step 1: Find the common difference in \\(y\\) as \\(x\\) increases by 1:\n"
        f"\\({y_vals[1]} - {y_vals[0]} = {diff}\\). Therefore, the rule involves multiplying by {diff}.\n\n"
        f"Step 2: Check constant term:\n"
        f"For \\(x = 1\\), \\({diff} \\times 1 = {diff}\\). Since \\(y = {y_vals[0]}\\), the rule is \\({rule_str}\\).\n\n"
        f"Step 3: Calculate \\(y\\) when \\(x = {x_missing}\\):\n"
        f"\\(y = {'(' + str(m) + ' \\times ' + str(x_missing) + ') - ' + str(c) if op_is_sub else '(' + str(m) + ' \\times ' + str(x_missing) + ') + ' + str(c)} = {y_missing}\\)."
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

def _generate_line_graph_question(rng: random.Random) -> Dict[str, Any]:
    """
    Interpretation of real-world line graphs.
    Exam Q6.1: Absenteeism graph across months.
    Questions:
    - Linear vs non-linear
    - Dependent vs independent variable
    - Reading values / total calculation
    """
    scenarios = [
        {
            "context": "A line graph records the average daily temperature in Bloemfontein recorded on the first day of each month from January to June: Jan (30°C), Feb (28°C), Mar (24°C), Apr (19°C), May (14°C), Jun (9°C).",
            "sub_type": "dependent_variable",
            "prompt": (
                "A line graph displays the average daily temperature recorded over consecutive months of the year.\n\n"
                "Which axis (horizontal or vertical) and which variable represents the **dependent variable**?"
            ),
            "correct": "Vertical axis (Temperature)",
            "options": [
                "Vertical axis (Temperature)",
                "Horizontal axis (Months of the year)",
                "Neither axis",
                "Both axes simultaneously"
            ],
            "explanation": "In authentic Cartesian graphs, the independent variable (time / months) is placed on the horizontal axis (x-axis), while the dependent variable (the quantity measured, temperature) is placed on the vertical axis (y-axis).",
            "subskill": "graph_dependent_variable",
            "h1": "Ask yourself: which variable depends on the other? Does the month depend on temperature, or does temperature depend on the month?",
            "h2": "The dependent variable is the measured quantity plotted on the vertical y-axis.",
            "h3": "The vertical axis (Temperature) represents the dependent variable."
        },
        {
            "context": "A student monitors a plant's growth. The graph curves upwards with weekly heights: Week 1 (2 cm), Week 2 (5 cm), Week 3 (10 cm), Week 4 (18 cm).",
            "sub_type": "linear_or_nonlinear",
            "prompt": (
                "The line graph representing a growing seedling shows heights: Week 1 (2 cm), Week 2 (5 cm), Week 3 (10 cm), Week 4 (18 cm).\n\n"
                "Is this graph **linear** or **non-linear**, and what is the mathematical reason?"
            ),
            "correct": "Non-linear, because the rate of change is not constant (it does not form a single straight line)",
            "options": [
                "Non-linear, because the rate of change is not constant (it does not form a single straight line)",
                "Linear, because all the height values are positive",
                "Linear, because the points are connected by line segments",
                "Non-linear, because the time cannot be measured"
            ],
            "explanation": "A graph is linear only if it has a constant rate of change and forms a single continuous straight line. Here the differences between consecutive weeks are 3 cm, 5 cm, and 8 cm (changing rate of growth), making it non-linear.",
            "subskill": "linear_vs_nonlinear_graph",
            "h1": "Look at the differences between consecutive values: 5 - 2 = 3, 10 - 5 = 5, 18 - 10 = 8.",
            "h2": "A linear graph must have a constant difference (constant gradient) forming a single straight line.",
            "h3": "The graph is non-linear because the rate of change is not constant."
        },
        {
            "context": "Exam Q6.1 absenteeism scenario",
            "sub_type": "reading_and_summing",
            "prompt": (
                "A line graph tracks learner absenteeism in a Grade 7 class over five terms/cycles:\n"
                "Term 1: 12 days, Term 2: 8 days, Term 3: 15 days, Term 4: 5 days.\n\n"
                "Calculate the total number of absent days recorded across the four terms."
            ),
            "correct": "40",
            "options": ["40", "35", "45", "50"],
            "explanation": "Total days absent = 12 + 8 + 15 + 5 = 40 days.",
            "subskill": "graph_reading_total",
            "h1": "Add the values recorded for all four terms.",
            "h2": "12 + 8 + 15 + 5.",
            "h3": "12 + 8 = 20; 20 + 15 = 35; 35 + 5 = 40."
        }
    ]

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
    - mode="elementary_flow_diagram": Input/output flow diagrams
    - mode="elementary_table": Table of values and rule deduction
    - mode="elementary_graphs": Line graph interpretation (linear/nonlinear, variables)
    - mode="compound": Full authentic exam mix
    """
    rng = _rng(seed)
    questions = []

    for _ in range(count):
        if mode == "elementary_flow_diagram" or subskill == "flow_diagram":
            q = _generate_flow_diagram_question(rng)
        elif mode == "elementary_table" or subskill == "table":
            q = _generate_table_of_values_question(rng)
        elif mode == "elementary_graphs" or subskill == "graphs":
            q = _generate_line_graph_question(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                lambda: _generate_flow_diagram_question(rng),
                lambda: _generate_table_of_values_question(rng),
                lambda: _generate_line_graph_question(rng)
            ])
            q = archetype()
        questions.append(q)

    return questions
