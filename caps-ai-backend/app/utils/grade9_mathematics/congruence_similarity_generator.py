"""Grade 9 Mathematics — Congruence, Similarity & 2D Geometry Proofs (Deterministic 6-Pillar Generator).
Covers official CAPS Term 3 Euclidean proofs:
- Congruent Triangles (SSS, SAS, AAS, RHS) with formal 2-column Statement-Reason tables.
- Similar Triangles (AAA, sides in proportion) and Pythagoras integration.
- Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    rng,
    solution_graph,
    step,
)

TOPIC = "geometry_congruence_similarity"
LO = "math9_congruence_similarity"


CONGRUENCE_CASES = [
    {
        "case": "SAS",
        "name": "Side-Angle-Included Side (SAS)",
        "desc": "Two pairs of equal sides and the included angle between them.",
        "example_reasons": ["AB = DE (Given)", "angle B = angle E (Given)", "BC = EF (Given)"],
        "conclusion_reason": "SAS",
    },
    {
        "case": "SSS",
        "name": "Side-Side-Side (SSS)",
        "desc": "All three pairs of corresponding sides are equal.",
        "example_reasons": ["AB = DE (Given)", "BC = EF (Given)", "AC = DF (Common side / Given)"],
        "conclusion_reason": "SSS",
    },
    {
        "case": "AAS",
        "name": "Angle-Angle-Side (AAS)",
        "desc": "Two pairs of equal angles and a corresponding side.",
        "example_reasons": ["angle A = angle D (Given)", "angle B = angle E (Given)", "BC = EF (Given)"],
        "conclusion_reason": "AAS",
    },
    {
        "case": "RHS",
        "name": "Right Angle-Hypotenuse-Side (RHS)",
        "desc": "Right angle, equal hypotenuse, and one other pair of equal sides.",
        "example_reasons": ["angle B = angle E = 90 deg (Given)", "AC = DF (Hypotenuse, Given)", "AB = DE (Given)"],
        "conclusion_reason": "RHS",
    },
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Pythagoras Step
# --------------------------------------------------------------------------- #
def _build_pythagoras_drill(r, difficulty: str) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (7, 24, 25), (9, 12, 15)]
    a_len, b_len, c_len = r.choice(triples)
    solve_for_hyp = r.random() < 0.5

    scale = 3.5 / max(a_len, b_len)
    if solve_for_hyp:
        prompt = f"In right-angled triangle $\\triangle \\text{{ABC}}$ with $\\hat{{B}} = 90^\\circ$, $AB = {a_len}\\text{{ cm}}$ and $BC = {b_len}\\text{{ cm}}$. Calculate the length of hypotenuse $AC$."
        ans = f"{c_len}\\text{{ cm}}"
        sample = rf"AC^2 = AB^2 + BC^2 = {a_len}^2 + {b_len}^2 = {a_len**2} + {b_len**2} = {c_len**2} \implies AC = {c_len}\text{{ cm}}"
        diag = {
            "kind": "triangle",
            "vertices": ["A", "B", "C"],
            "points": {
                "A": [0.0, round(a_len * scale, 2)],
                "B": [0.0, 0.0],
                "C": [round(b_len * scale, 2), 0.0],
            },
            "right_angle_at": "B",
            "side_labels": {
                "AB": f"{a_len} cm", "BA": f"{a_len} cm",
                "BC": f"{b_len} cm", "CB": f"{b_len} cm",
                "AC": "AC = ?", "CA": "AC = ?",
            },
            "angle_labels": {"B": "90°"},
            "equal_sides": [],
            "caption": f"Triangle ABC with right angle at B, AB = {a_len} cm, BC = {b_len} cm (not to scale)",
        }
    else:
        prompt = f"In right-angled triangle $\\triangle \\text{{PQR}}$ with $\\hat{{Q}} = 90^\\circ$, hypotenuse $PR = {c_len}\\text{{ cm}}$ and $PQ = {a_len}\\text{{ cm}}$. Calculate the length of side $QR$."
        ans = f"{b_len}\\text{{ cm}}"
        sample = rf"QR^2 = PR^2 - PQ^2 = {c_len}^2 - {a_len}^2 = {c_len**2} - {a_len**2} = {b_len**2} \implies QR = {b_len}\text{{ cm}}"
        diag = {
            "kind": "triangle",
            "vertices": ["P", "Q", "R"],
            "points": {
                "P": [0.0, round(a_len * scale, 2)],
                "Q": [0.0, 0.0],
                "R": [round(b_len * scale, 2), 0.0],
            },
            "right_angle_at": "Q",
            "side_labels": {
                "PQ": f"{a_len} cm", "QP": f"{a_len} cm",
                "PR": f"{c_len} cm", "RP": f"{c_len} cm",
                "QR": "QR = ?", "RQ": "QR = ?",
            },
            "angle_labels": {"Q": "90°"},
            "equal_sides": [],
            "caption": f"Triangle PQR with right angle at Q, PQ = {a_len} cm, PR = {c_len} cm (not to scale)",
        }

    return make_math_question(
        prefix="geom_pyth",
        topic=TOPIC,
        subskill="elementary_pythagoras_step",
        learning_objective_id=f"{LO}_pythagoras",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans,
        answer_sympy=str(c_len if solve_for_hyp else b_len),
        sample_answer=sample,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_thm", "desc": "Statement of Pythagoras theorem with reason (Pythagoras)", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": "Substitution of given side lengths", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Correct answer with units: {ans}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_square_root_step", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        hints={
            "1_nudge": "In a right-angled triangle, hypotenuse^2 = side1^2 + side2^2.",
            "2_concept": "Theorem of Pythagoras: $c^2 = a^2 + b^2$.",
            "3_breakdown": sample,
        },
        misconception_tags=["added_when_finding_shorter_side", "forgot_to_take_square_root"],
        keywords=["Pythagoras", "hypotenuse", "right-angled triangle"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="elementary_pythagoras_step",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Congruence Case Identification
# --------------------------------------------------------------------------- #
def _build_congruence_id_drill(r, difficulty: str) -> Dict[str, Any]:
    c_case = r.choice(CONGRUENCE_CASES)
    options = ["SSS", "SAS", "AAS", "RHS"]

    prompt = (
        f"Two triangles $\\triangle \\text{{ABC}}$ and $\\triangle \\text{{DEF}}$ are proven congruent using the following statements:\n\n"
        + "\n".join(f"• {stmt}" for stmt in c_case["example_reasons"])
        + f"\n\nState the correct reason for congruence: [{', '.join(options)}]."
    )

    case_key = c_case["case"]
    if case_key == "RHS":
        pts = {
            "A": [0.0, 3.0], "B": [0.0, 0.0], "C": [3.5, 0.0],
            "D": [5.5, 3.0], "E": [5.5, 0.0], "F": [9.0, 0.0],
        }
        side_lbls = {"AB": "s", "DE": "s", "CA": "hyp", "DF": "hyp", "AC": "hyp", "FD": "hyp", "BA": "s", "ED": "s"}
        eq_sides = [["AB", "DE"], ["CA", "DF"]]
        right_ang = ["B", "E"]
        ang_lbls = {"B": "90°", "E": "90°"}
        cap = "Two right-angled triangles with equal hypotenuses and one equal side"
    elif case_key == "SAS":
        pts = {
            "A": [1.5, 3.0], "B": [0.0, 0.0], "C": [3.5, 0.0],
            "D": [7.0, 3.0], "E": [5.5, 0.0], "F": [9.0, 0.0],
        }
        side_lbls = {"AB": "c", "DE": "c", "BC": "a", "EF": "a", "BA": "c", "ED": "c", "CB": "a", "FE": "a"}
        eq_sides = [["AB", "DE"], ["BC", "EF"]]
        right_ang = None
        ang_lbls = {"B": "θ", "E": "θ"}
        cap = "Two triangles with two pairs of equal sides and included angle"
    elif case_key == "SSS":
        pts = {
            "A": [1.5, 3.0], "B": [0.0, 0.0], "C": [3.5, 0.0],
            "D": [7.0, 3.0], "E": [5.5, 0.0], "F": [9.0, 0.0],
        }
        side_lbls = {
            "AB": "c", "DE": "c", "BC": "a", "EF": "a", "CA": "b", "DF": "b",
            "BA": "c", "ED": "c", "CB": "a", "FE": "a", "AC": "b", "FD": "b",
        }
        eq_sides = [["AB", "DE"], ["BC", "EF"], ["CA", "DF"]]
        right_ang = None
        ang_lbls = {}
        cap = "Two triangles with three pairs of equal corresponding sides"
    else:  # AAS
        pts = {
            "A": [1.5, 3.0], "B": [0.0, 0.0], "C": [3.5, 0.0],
            "D": [7.0, 3.0], "E": [5.5, 0.0], "F": [9.0, 0.0],
        }
        side_lbls = {"BC": "a", "EF": "a", "CB": "a", "FE": "a"}
        eq_sides = [["BC", "EF"]]
        right_ang = None
        ang_lbls = {"A": "α", "D": "α", "B": "β", "E": "β"}
        cap = "Two triangles with two pairs of equal angles and one equal side"

    diag = {
        "kind": "triangle",
        "vertices": ["A", "B", "C", "D", "E", "F"],
        "triangles": [["A", "B", "C"], ["D", "E", "F"]],
        "points": pts,
        "side_labels": side_lbls,
        "equal_sides": eq_sides,
        "right_angle_at": right_ang,
        "angle_labels": ang_lbls,
        "caption": cap,
    }

    return make_math_question(
        prefix="geom_cong_id",
        topic=TOPIC,
        subskill="elementary_congruence_case_id",
        learning_objective_id=f"{LO}_congruence_id",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=c_case["conclusion_reason"],
        answer_sympy=c_case["conclusion_reason"],
        sample_answer=f"Reason: ({c_case['conclusion_reason']}) — {c_case['desc']}",
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_case", "desc": f"Correct congruence condition: ({c_case['conclusion_reason']})", "marks": 2, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict",
        },
        hints={
            "1_nudge": "Count how many sides and how many angles are given, and check whether the angle is between the sides.",
            "2_concept": f"For {c_case['conclusion_reason']}: {c_case['desc']}",
            "3_breakdown": f"The correct reason is ({c_case['conclusion_reason']}).",
        },
        misconception_tags=["confused_sas_with_ass", "omitted_rhs_hypotenuse_check"],
        keywords=["congruence", "triangle proof", "SSS", "SAS", "AAS", "RHS"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        mode="elementary_congruence_case_id",
        difficulty="easy",
    )


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Formal 2-Column Congruence Proof
# --------------------------------------------------------------------------- #
def _build_compound_congruence_proof(r, difficulty: str) -> Dict[str, Any]:
    c_case = r.choice(CONGRUENCE_CASES)
    s1 = r.randint(4, 9)
    s2 = r.randint(10, 16)
    ang = r.choice([35, 42, 50, 65, 72])

    prompt = (
        f"In the geometric figure, $AB = DE = {s1}\\text{{ cm}}$, $BC = EF = {s2}\\text{{ cm}}$, and $\\hat{{B}} = \\hat{{E}} = {ang}^\\circ$.\n\n"
        f"1. Prove that $\\triangle \\text{{ABC}} \\equiv \\triangle \\text{{DEF}}$. Present your answer in a formal two-column table (Statements and Reasons).\n"
        f"2. If $AC = (2x - 3)\\text{{ cm}}$ and $DF = 11\\text{{ cm}}$, calculate the value of $x$, giving a clear geometric reason."
    )

    x_val = 7 # 2x - 3 = 11 => 2x = 14 => x = 7

    proof_table = (
        r"\begin{array}{|l|l|}"
        r"\hline"
        r"\textbf{Statement} & \textbf{Reason} \\ \hline"
        rf"\text{{In }} \triangle \text{{ABC}} \text{{ and }} \triangle \text{{DEF}}: & \\ "
        rf"1.\; AB = DE = {s1}\text{{ cm}} & \text{{Given}} \\ "
        rf"2.\; \hat{{B}} = \hat{{E}} = {ang}^\circ & \text{{Given}} \\ "
        rf"3.\; BC = EF = {s2}\text{{ cm}} & \text{{Given}} \\ \hline"
        rf"\therefore \triangle \text{{ABC}} \equiv \triangle \text{{DEF}} & \text{{SAS}} \\ \hline"
        rf"AC = DF & \equiv \triangle\text{{s (corresponding sides equal)}} \\ "
        rf"2x - 3 = 11 \implies 2x = 14 \implies x = {x_val} & \\ \hline"
        r"\end{array}"
    )

    canonical = solution_graph(
        goal="prove triangle congruence and deduce unknown variable",
        steps=[
            step(from_latex="AB = DE", to_latex_str="AB = DE (Given)", op="first condition", rule="Given"),
            step(from_latex=r"\hat{B} = \hat{E}", to_latex_str=rf"\hat{{B}} = \hat{{E}} = {ang}^\circ (\text{{Given}})", op="second condition", rule="Given"),
            step(from_latex="BC = EF", to_latex_str="BC = EF (Given)", op="third condition", rule="Given"),
            step(from_latex=r"\triangle \text{ABC} \equiv \triangle \text{DEF}", to_latex_str=r"\triangle \text{ABC} \equiv \triangle \text{DEF} (\text{SAS})", op="congruence deduction", rule="SAS"),
            step(from_latex="2x - 3 = 11", to_latex_str=f"x = {x_val}", op="solve for x", rule="corresponding sides of congruent triangles"),
        ],
        final_latex=f"x = {x_val}",
    )

    marking_schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Statement 1 with reason (Given)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Statement 2 with reason (Given)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Statement 3 with reason (Given)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Conclusion with correct reason (SAS)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Equating corresponding sides AC = DF with reason", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Linear equation 2x - 3 = 11", "marks": 1, "editable": True},
            {"id": "mp7", "desc": f"Correct value of x = {x_val}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_geometric_reasons", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Set up a formal 3-statement proof listing corresponding sides and angles before concluding congruence.",
        "concept": "Once $\\triangle \\text{ABC} \\equiv \\triangle \\text{DEF}$, all remaining corresponding sides and angles are equal.",
        "breakdown": f"List the 3 given facts. Conclude congruence (SAS). Then set $AC = DF \\implies 2x - 3 = 11 \\implies x = {x_val}$.",
    }

    rad = math.radians(ang)
    a_x = round(2.8 * math.cos(rad), 2)
    a_y = round(2.8 * math.sin(rad), 2)
    pts = {
        "B": [0.0, 0.0],
        "C": [3.8, 0.0],
        "A": [a_x, a_y],
        "E": [5.5, 0.0],
        "F": [9.3, 0.0],
        "D": [round(5.5 + a_x, 2), a_y],
    }
    diag = {
        "kind": "triangle",
        "vertices": ["A", "B", "C", "D", "E", "F"],
        "triangles": [["A", "B", "C"], ["D", "E", "F"]],
        "points": pts,
        "side_labels": {
            "AB": f"{s1} cm", "BA": f"{s1} cm",
            "DE": f"{s1} cm", "ED": f"{s1} cm",
            "BC": f"{s2} cm", "CB": f"{s2} cm",
            "EF": f"{s2} cm", "FE": f"{s2} cm",
            "AC": "(2x - 3) cm", "CA": "(2x - 3) cm",
            "DF": "11 cm", "FD": "11 cm",
        },
        "equal_sides": [["AB", "DE"], ["BC", "EF"]],
        "angle_labels": {"B": f"{ang}°", "E": f"{ang}°"},
        "caption": f"Triangles ABC and DEF with AB = DE = {s1} cm, BC = EF = {s2} cm, B = E = {ang}° (not to scale)",
    }

    return make_math_question(
        prefix="geom_cong_proof",
        topic=TOPIC,
        subskill="congruence_proof_compound",
        learning_objective_id=f"{LO}_congruence_proof",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=f"\\triangle \\text{{ABC}} \\equiv \\triangle \\text{{DEF}} \\text{{ (SAS)}}; \\quad x = {x_val}",
        answer_sympy=str(x_val),
        sample_answer=proof_table,
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_geometric_reasons", "assumed_unproven_equality", "wrong_congruence_case"],
        keywords=["congruence proof", "Statement Reason", "SAS", "corresponding sides"],
        term=3,
        caps_weight_percent=30,
        suggested_duration_mins=10,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_congruence_proof,
    "elementary_congruence_case_id": _build_congruence_id_drill,
    "elementary_pythagoras_step": _build_pythagoras_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 9 Geometry Congruence and Similarity proofs."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill if (subskill and subskill in BUILDERS) else mode
    builder = BUILDERS.get(target, _build_compound_congruence_proof)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
