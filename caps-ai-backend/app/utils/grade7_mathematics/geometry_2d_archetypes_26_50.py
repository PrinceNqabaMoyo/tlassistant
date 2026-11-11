"""
Grade 7 Mathematics - Geometry of 2D Shapes Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of 2D shapes.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Quadrilateral Interior Angles Calculation (26 - 34)
# ==============================================================================

def arch_26_quadrilateral_interior_angle_sum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain why the sum of the interior angles of any convex quadrilateral is always **360°**."
    )
    sol = (
        f"**Step 1:** Drawing a diagonal from one vertex divides any convex quadrilateral into **two non-overlapping triangles** [1 Mark: Method].\n\n"
        f"**Step 2:** Each triangle has an interior angle sum of $180^\\circ$. Therefore: "
        f"$$2 \\times 180^\\circ = \\mathbf{{360^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "A diagonal divides the quadrilateral into two triangles; 2 x 180° = 360°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_quadrilateral_interior_angle_sum",
        "hints": {
            "tier_1": "How many triangles are formed by drawing one diagonal across a quadrilateral?",
            "tier_2": "2 triangles. 2 * 180° = 360°.",
            "tier_3": "Can be divided into 2 triangles, each having 180°, so 2 * 180° = 360°."
        }
    }


def arch_27_missing_fourth_angle_quadrilateral(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([75, 85, 95, 105])
    a2 = rng.choice([70, 80, 90, 110])
    a3 = rng.choice([60, 65, 75, 85])
    a4 = 360 - (a1 + a2 + a3)

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,120 180,120 200,40 60,40" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="65" y="60" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>'
            f'<text x="175" y="60" font-size="12" font-weight="bold" fill="#2563eb">{a2}°</text>'
            f'<text x="160" y="112" font-size="12" font-weight="bold" fill="#2563eb">{a3}°</text>'
            f'<text x="55" y="112" font-size="13" font-weight="bold" fill="#ef4444">x</text>'
            f'</svg>'
        ),
        "caption": f"Quadrilateral with known angles {a1}°, {a2}°, {a3}° and unknown x",
        "diagram_role": "context"
    }

    prompt = (
        f"In quadrilateral $ABCD$, three interior angles measure **{a1}°**, **{a2}°**, and **{a3}°**.\n\n"
        f"Calculate the size of the fourth interior angle $x$, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** The sum of interior angles in any quadrilateral is $360^\\circ$ [1 Mark: Reason (sum of $\\angle$s in quad)].\n\n"
        f"**Step 2:** $$x = 360^\\circ - ({a1}^\\circ + {a2}^\\circ + {a3}^\\circ) = 360^\\circ - {a1+a2+a3}^\\circ = \\mathbf{{{a4}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a4}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "27_missing_fourth_angle_quadrilateral",
        "hints": {
            "tier_1": f"Add {a1} + {a2} + {a3} and subtract from 360°.",
            "tier_2": f"360 - ({a1+a2+a3}) = {a4}.",
            "tier_3": f"{a4}°."
        }
    }


def arch_28_opposite_angles_in_parallelogram(rng: random.Random) -> Dict[str, Any]:
    angle_a = rng.choice([65, 70, 75, 110, 115, 120])

    prompt = (
        f"In parallelogram $ABCD$, angle $\\hat{{A}} = {angle_a}^\\circ$.\n\n"
        f"Calculate the size of the opposite angle $\\hat{{C}}$, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** In any parallelogram, opposite angles are equal: $\\hat{{C}} = \\hat{{A}}$ [1 Mark: Reason (opp $\\angle$s of $\\parallel$m)].\n\n"
        f"**Step 2:** $$\\hat{{C}} = \\mathbf{{{angle_a}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{angle_a}° (opposite angles of parallelogram are equal)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "28_opposite_angles_in_parallelogram",
        "hints": {
            "tier_1": "Opposite angles in a parallelogram are equal.",
            "tier_2": f"Angle C = Angle A = {angle_a}°.",
            "tier_3": f"{angle_a}°."
        }
    }


def arch_29_consecutive_angles_in_parallelogram(rng: random.Random) -> Dict[str, Any]:
    angle_a = rng.choice([60, 70, 75, 80, 110, 120])
    angle_b = 180 - angle_a

    prompt = (
        f"In parallelogram $ABCD$, angle $\\hat{{A}} = {angle_a}^\\circ$.\n\n"
        f"Calculate the size of the consecutive adjacent angle $\\hat{{B}}$, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** Consecutive interior angles between parallel lines are supplementary (co-interior angles add to $180^\\circ$) [1 Mark: Reason].\n\n"
        f"**Step 2:** $$\\hat{{B}} = 180^\\circ - {angle_a}^\\circ = \\mathbf{{{angle_b}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{angle_b}° (co-interior angles between parallel lines sum to 180°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_consecutive_angles_in_parallelogram",
        "hints": {
            "tier_1": f"Subtract {angle_a}° from 180°.",
            "tier_2": f"180 - {angle_a} = {angle_b}.",
            "tier_3": f"{angle_b}°."
        }
    }


def arch_30_angles_in_a_rhombus(rng: random.Random) -> Dict[str, Any]:
    acute_ang = rng.choice([50, 60, 70])
    obtuse_ang = 180 - acute_ang

    prompt = (
        f"A rhombus has an acute interior angle of **{acute_ang}°**.\n\n"
        f"Calculate the size of its obtuse interior angle, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** A rhombus is a parallelogram, so adjacent co-interior angles add up to $180^\\circ$ [1 Mark: Reason].\n\n"
        f"**Step 2:** $$\\text{{Obtuse angle}} = 180^\\circ - {acute_ang}^\\circ = \\mathbf{{{obtuse_ang}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{obtuse_ang}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_angles_in_a_rhombus",
        "hints": {
            "tier_1": f"Subtract {acute_ang}° from 180°.",
            "tier_2": f"180 - {acute_ang} = {obtuse_ang}.",
            "tier_3": f"{obtuse_ang}°."
        }
    }


def arch_31_angles_in_a_kite(rng: random.Random) -> Dict[str, Any]:
    top_ang = rng.choice([70, 80, 90])
    bot_ang = rng.choice([40, 50, 60])
    # The other two side angles are equal
    side_ang = (360 - (top_ang + bot_ang)) // 2

    prompt = (
        f"In kite $ABCD$, side $AB = AD$ and side $BC = CD$.\n"
        f"The angle at the top is $\\hat{{A}} = {top_ang}^\\circ$ and the angle at the bottom is $\\hat{{C}} = {bot_ang}^\\circ$.\n\n"
        f"Calculate the size of angle $\\hat{{B}}$ (between the unequal sides)."
    )
    sol = (
        f"**Step 1:** In a kite, the two angles between the unequal sides are equal: $\\hat{{B}} = \\hat{{D}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Sum of angles in quad is $360^\\circ$:\n"
        f"$$2\\hat{{B}} = 360^\\circ - ({top_ang}^\\circ + {bot_ang}^\\circ) = 360^\\circ - {top_ang + bot_ang}^\\circ = {360 - top_ang - bot_ang}^\\circ$$\n"
        f"$$\\hat{{B}} = \\frac{{{360 - top_ang - bot_ang}^\\circ}}{{2}} = \\mathbf{{{side_ang}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{side_ang}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_angles_in_a_kite",
        "hints": {
            "tier_1": f"Subtract ({top_ang} + {bot_ang}) from 360°, then divide by 2.",
            "tier_2": f"({360 - top_ang - bot_ang}) / 2 = {side_ang}.",
            "tier_3": f"{side_ang}°."
        }
    }


def arch_32_isosceles_trapezium_angles(rng: random.Random) -> Dict[str, Any]:
    base_ang = rng.choice([65, 70, 75])
    top_ang = 180 - base_ang

    prompt = (
        f"In an isosceles trapezium, the non-parallel sides are equal in length.\n\n"
        f"If one base angle measures **{base_ang}°**:\n"
        f"1. What is the size of the other base angle?\n"
        f"2. What is the size of each top interior angle?"
    )
    sol = (
        f"**Step 1:** In an isosceles trapezium, base angles are equal: other base angle is **${base_ang}^\\circ$** [1 Mark].\n\n"
        f"**Step 2:** Co-interior angles along the non-parallel sides add to $180^\\circ$: "
        f"$$180^\\circ - {base_ang}^\\circ = \\mathbf{{{top_ang}^\\circ}} \\text{{ each [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1. {base_ang}°; 2. {top_ang}° each",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "32_isosceles_trapezium_angles",
        "hints": {
            "tier_1": f"Base angles are equal ({base_ang}°). Top angles are 180° - {base_ang}°.",
            "tier_2": f"Top angles are {top_ang}°.",
            "tier_3": f"1. {base_ang}°; 2. {top_ang}° each."
        }
    }


def arch_33_trapezium_cointerior_angles(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([72, 80, 85])
    a2 = 180 - a1

    prompt = (
        f"In trapezium $ABCD$, side $AB \\parallel CD$.\n"
        f"If $\\hat{{A}} = {a1}^\\circ$, calculate $\\hat{{D}}$."
    )
    sol = (
        f"**Step 1:** $\\hat{{A}}$ and $\\hat{{D}}$ are co-interior angles between parallel lines $AB \\parallel CD$ (they add up to $180^\\circ$) [1 Mark: Reason].\n\n"
        f"**Step 2:** $$\\hat{{D}} = 180^\\circ - {a1}^\\circ = \\mathbf{{{a2}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a2}° (co-interior angles AB || CD)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_trapezium_cointerior_angles",
        "hints": {
            "tier_1": f"Subtract {a1}° from 180°.",
            "tier_2": f"180 - {a1} = {a2}.",
            "tier_3": f"{a2}°."
        }
    }


def arch_34_algebraic_angles_quadrilateral(rng: random.Random) -> Dict[str, Any]:
    # x, 2x, 3x, 4x => 10x = 360 => x = 36
    prompt = (
        f"The four angles of a quadrilateral are $x$, $2x$, $3x$, and $4x$.\n\n"
        f"1. Solve for $x$.\n"
        f"2. Calculate the size of the smallest and largest angles."
    )
    sol = (
        f"**Step 1:** Sum of angles in a quadrilateral is $360^\\circ$:\n"
        f"$$x + 2x + 3x + 4x = 360^\\circ \\implies 10x = 360^\\circ \\implies x = \\mathbf{{36^\\circ}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Smallest is $x = \\mathbf{{36^\\circ}}$; Largest is $4x = 4 \\times 36^\\circ = \\mathbf{{144^\\circ}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. x = 36°; 2. Smallest = 36°, Largest = 144°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_algebraic_angles_quadrilateral",
        "hints": {
            "tier_1": "10x = 360°. Divide 360 by 10.",
            "tier_2": "x = 36°. Largest is 4 * 36 = 144°.",
            "tier_3": "x = 36°; Smallest = 36°, Largest = 144°."
        }
    }


# ==============================================================================
# CLUSTER 5: Congruence & Similarity (35 - 42)
# ==============================================================================

def arch_35_congruent_shapes_definition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Define what it means for two 2D figures to be **congruent** ($\\equiv$)."
    )
    sol = (
        f"**Step 1:** Two figures are congruent if they have the **exact same shape** AND the **exact same size** [1 Mark].\n\n"
        f"**Step 2:** All corresponding side lengths are equal and all corresponding interior angles are equal [1 Mark: Precision]."
    )
    return {
        "id": f"g7_g2d_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Exact same shape and exact same size (all corresponding sides and angles equal)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "35_congruent_shapes_definition",
        "hints": {
            "tier_1": "Do congruent shapes have the same size and same shape?",
            "tier_2": "Identical in shape and size.",
            "tier_3": "Exact same shape and exact same size."
        }
    }


def arch_36_similar_shapes_definition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Define what it means for two 2D figures to be **similar** ($\\sim$)."
    )
    sol = (
        f"**Step 1:** Two figures are similar if they have the **exact same shape** (corresponding angles are equal) but **different sizes** (one is an enlargement or reduction of the other) [1 Mark].\n\n"
        f"**Step 2:** Corresponding sides are in the **same proportion (ratio)** [1 Mark: Precision]."
    )
    return {
        "id": f"g7_g2d_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Same shape with proportional sides and equal angles, but different size",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_similar_shapes_definition",
        "hints": {
            "tier_1": "Think about enlargement: same shape, but different scale.",
            "tier_2": "Equal angles, proportional sides.",
            "tier_3": "Same shape, equal angles, proportional sides, different size."
        }
    }


def arch_37_congruence_condition_sss(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State the **SSS condition** for triangle congruence."
    )
    sol = (
        f"**Step 1:** SSS stands for **Side-Side-Side** [1 Mark].\n\n"
        f"**Step 2:** Two triangles are congruent if all three corresponding sides of one triangle are equal in length to all three corresponding sides of the second triangle [1 Mark: Definition]."
    )
    return {
        "id": f"g7_g2d_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Side-Side-Side: all three corresponding pairs of sides are equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_congruence_condition_sss",
        "hints": {
            "tier_1": "What does SSS stand for?",
            "tier_2": "Side-Side-Side.",
            "tier_3": "All three pairs of corresponding sides are equal."
        }
    }


def arch_38_congruence_condition_sas(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Why is it essential in the **SAS condition** that the angle be the **included angle**?"
    )
    sol = (
        f"**Step 1:** The included angle is the angle formed directly **between** the two known sides [1 Mark].\n\n"
        f"**Step 2:** If the angle is not between the two sides (SSA), two completely different non-congruent triangles can be constructed with the same measurements (the ambiguous case) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "The angle must be between the two sides to fix the triangle uniquely without ambiguity",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_congruence_condition_sas",
        "hints": {
            "tier_1": "What does 'included' mean in geometry?",
            "tier_2": "Trapped between the two sides.",
            "tier_3": "The angle must be directly between the two known sides."
        }
    }


def arch_39_congruence_condition_asa(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What does the abbreviation **ASA** stand for when proving triangle congruence?"
    )
    sol = (
        f"**Step 1:** ASA stands for **Angle-Side-Angle** [1 Mark].\n\n"
        f"**Step 2:** Two angles and the included side between them in one triangle are equal to the corresponding parts in another triangle [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Angle-Side-Angle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_congruence_condition_asa",
        "hints": {
            "tier_1": "A = Angle, S = Side.",
            "tier_2": "Angle-Side-Angle.",
            "tier_3": "Angle-Side-Angle."
        }
    }


def arch_40_congruence_condition_rhs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In right-angled triangle congruence, what does **RHS** stand for?"
    )
    sol = (
        f"**Step 1:** RHS stands for: **Right-angle, Hypotenuse, Side** [1 Mark].\n\n"
        f"**Step 2:** Two right-angled triangles are congruent if their hypotenuses are equal and one other pair of corresponding sides is equal [1 Mark: Full condition]."
    )
    return {
        "id": f"g7_g2d_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Right-angle, Hypotenuse, Side",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_congruence_condition_rhs",
        "hints": {
            "tier_1": "R = Right angle, H = Hypotenuse, S = Side.",
            "tier_2": "Right-angle, Hypotenuse, Side.",
            "tier_3": "Right-angle, Hypotenuse, Side."
        }
    }


def arch_41_scale_factor_similar_triangles(rng: random.Random) -> Dict[str, Any]:
    s1 = rng.choice([3, 4, 5, 6])
    k = rng.choice([2, 3, 4])
    s2 = s1 * k

    prompt = (
        f"Two triangles $\\Delta ABC$ and $\\Delta DEF$ are similar.\n"
        f"Corresponding side $AB = {s1}\\text{{ cm}}$ and $DE = {s2}\\text{{ cm}}$.\n\n"
        f"Calculate the **scale factor of enlargement** from $\\Delta ABC$ to $\\Delta DEF$."
    )
    sol = (
        f"**Step 1:** Scale factor is the ratio of corresponding side lengths: $k = \\frac{{DE}}{{AB}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$k = \\frac{{{s2}}}{{{s1}}} = \\mathbf{{{k}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{k}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_scale_factor_similar_triangles",
        "hints": {
            "tier_1": f"Divide {s2} by {s1}.",
            "tier_2": f"{s2} / {s1} = {k}.",
            "tier_3": f"{k}."
        }
    }


def arch_42_missing_side_in_similar_triangles(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 5])
    side_small = rng.choice([4, 6, 7])
    side_large = side_small * k

    prompt = (
        f"Triangle $PQR$ is similar to triangle $XYZ$ with a scale factor of **{k}**.\n\n"
        f"If side $PQ = {side_small}\\text{{ cm}}$, calculate the length of the corresponding side $XY$."
    )
    sol = (
        f"**Step 1:** Multiply the original length by the scale factor: $XY = k \\times PQ$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$XY = {k} \\times {side_small} = \\mathbf{{{side_large}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{side_large} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_missing_side_in_similar_triangles",
        "hints": {
            "tier_1": f"Multiply {side_small} by {k}.",
            "tier_2": f"{side_small} * {k} = {side_large}.",
            "tier_3": f"{side_large} cm."
        }
    }


# ==============================================================================
# CLUSTER 6: Circles and Composite 2D Geometry (43 - 50)
# ==============================================================================

def arch_43_identify_circle_lines_on_diagram(rng: random.Random) -> Dict[str, Any]:
    r_val = rng.choice([65, 68, 70, 74])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 220 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<circle cx="100" cy="100" r="{r_val}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="100" y1="100" x2="{100 + r_val}" y2="100" stroke="#2563eb" stroke-width="2.5"/>'  # OA (radius)
            f'<line x1="{100 - r_val}" y1="100" x2="{100 + r_val}" y2="100" stroke="#1e293b" stroke-width="2" stroke-dasharray="3,2"/>'  # BC (diameter)
            f'<line x1="55" y1="55" x2="145" y2="55" stroke="#10b981" stroke-width="2.5"/>'  # DE (chord)
            f'<circle cx="100" cy="100" r="3.5" fill="#ef4444"/>'
            f'<text x="95" y="93" font-size="11" font-weight="bold">O</text>'
            f'<text x="175" y="104" font-size="11" font-weight="bold" fill="#2563eb">A</text>'
            f'<text x="20" y="104" font-size="11" font-weight="bold">B</text>'
            f'<text x="50" y="50" font-size="11" font-weight="bold" fill="#10b981">D</text>'
            f'<text x="145" y="50" font-size="11" font-weight="bold" fill="#10b981">E</text>'
            f'</svg>'
        ),
        "caption": "Circle with centre O, lines OA, BC, and DE",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the circle diagram with centre $O$.\n\n"
        f"1. What geometric term describes line segment $OA$?\n"
        f"2. What geometric term describes line segment $DE$ (which does not pass through the centre)?"
    )
    sol = (
        f"**Step 1:** $OA$ joins the centre to the boundary, so it is a **radius** [1 Mark: Method].\n\n"
        f"**Step 2:** $DE$ connects two points on the boundary without passing through the centre, so it is a **chord** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Radius; 2. Chord",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "43_identify_circle_lines_on_diagram",
        "hints": {
            "tier_1": "OA goes from centre to edge. DE joins two points on the circle.",
            "tier_2": "OA is a radius; DE is a chord.",
            "tier_3": "1. Radius; 2. Chord."
        }
    }


def arch_44_radius_diameter_conversion(rng: random.Random) -> Dict[str, Any]:
    r = rng.randint(4, 16)
    d = 2 * r

    prompt = (
        f"A circular pizza has a radius of **{r} cm**.\n\n"
        f"What is the diameter of the pizza?"
    )
    sol = (
        f"**Step 1:** Diameter is twice the radius: $d = 2r$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$d = 2 \\times {r} = \\mathbf{{{d}\\text{{ cm}}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{d} cm",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_radius_diameter_conversion",
        "hints": {
            "tier_1": f"Double the radius ({r} cm).",
            "tier_2": f"2 * {r} = {d}.",
            "tier_3": f"{d} cm."
        }
    }


def arch_45_angle_in_a_semicircle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A triangle is inscribed in a circle such that one of its sides is the **diameter** of the circle.\n\n"
        f"What is the exact size of the angle subtended on the circumference opposite the diameter? State the theorem."
    )
    sol = (
        f"**Step 1:** The angle subtended by a diameter at any point on the circumference is always a **$90^\\circ$ right angle** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Theorem: **Angle in a semicircle is a right angle ($90^\\circ$)** [1 Mark: Theorem name]."
    )
    return {
        "id": f"g7_g2d_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "90° (angle in a semicircle)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_angle_in_a_semicircle",
        "hints": {
            "tier_1": "What is the angle in a semicircle?",
            "tier_2": "It is always a right angle (90°).",
            "tier_3": "90° (angle in a semicircle is 90°)."
        }
    }


def arch_46_regular_vs_irregular_polygons(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What two conditions must be satisfied for a 2D polygon to be classified as **regular**?"
    )
    sol = (
        f"**Step 1 (Sides):** All sides must be of **equal length** (equilateral) [1 Mark].\n\n"
        f"**Step 2 (Angles):** All interior angles must be of **equal size** (equiangular) [1 Mark]."
    )
    return {
        "id": f"g7_g2d_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "All sides equal length AND all interior angles equal size",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_regular_vs_irregular_polygons",
        "hints": {
            "tier_1": "Both sides and angles must be equal.",
            "tier_2": "Equilateral and equiangular.",
            "tier_3": "All sides equal and all angles equal."
        }
    }


def arch_47_pentagon_properties_and_angle_sum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"For a regular **pentagon**:\n\n"
        f"1. How many sides and how many vertices does it have?\n"
        f"2. Calculate the sum of its interior angles using $(n - 2) \\times 180^\\circ$."
    )
    sol = (
        f"**Step 1:** A pentagon has **5 sides** and **5 vertices** [1 Mark].\n\n"
        f"**Step 2:** Sum of interior angles: "
        f"$$(5 - 2) \\times 180^\\circ = 3 \\times 180^\\circ = \\mathbf{{540^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 5 sides, 5 vertices; 2. 540°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_pentagon_properties_and_angle_sum",
        "hints": {
            "tier_1": "A pentagon has 5 sides. (5 - 2) * 180°.",
            "tier_2": "3 * 180 = 540°.",
            "tier_3": "5 sides; 540°."
        }
    }


def arch_48_hexagon_properties_and_angle_sum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"For a regular **hexagon**:\n\n"
        f"1. Calculate the sum of its interior angles.\n"
        f"2. Calculate the size of each interior angle in a regular hexagon."
    )
    sol = (
        f"**Step 1:** Interior angle sum: $$(6 - 2) \\times 180^\\circ = 4 \\times 180^\\circ = \\mathbf{{720^\\circ}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Each interior angle in a regular hexagon: "
        f"$$\\frac{{720^\\circ}}{{6}} = \\mathbf{{120^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. 720°; 2. 120°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_hexagon_properties_and_angle_sum",
        "hints": {
            "tier_1": "4 * 180 = 720°. Divide 720° by 6.",
            "tier_2": "720 / 6 = 120°.",
            "tier_3": "1. 720°; 2. 120°."
        }
    }


def arch_49_number_of_diagonals_in_polygon(rng: random.Random) -> Dict[str, Any]:
    cases = [(4, "quadrilateral", 2), (5, "pentagon", 5), (6, "hexagon", 9)]
    n, name, d_count = rng.choice(cases)

    prompt = (
        f"The formula for the number of diagonals in an $n$-sided polygon is: "
        f"$$D = \\frac{{n(n - 3)}}{{2}}$$\n\n"
        f"Calculate the number of diagonals that can be drawn in a **{name}** ($n = {n}$). "
    )
    sol = (
        f"**Step 1:** Substitute $n = {n}$: $$D = \\frac{{{n}({n} - 3)}}{{2}} = \\frac{{{n} \\times {n-3}}}{{2}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** $$D = \\frac{{{n * (n - 3)}}}{{2}} = \\mathbf{{{d_count}}} \\text{{ diagonals [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{d_count}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_number_of_diagonals_in_polygon",
        "hints": {
            "tier_1": f"Plug n = {n} into n(n - 3) / 2.",
            "tier_2": f"({n} * {n - 3}) / 2 = {d_count}.",
            "tier_3": f"{d_count} diagonals."
        }
    }


def arch_50_line_symmetry_of_quadrilaterals(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("square", 4, "2 across opposite sides and 2 across diagonals"),
        ("rectangle", 2, "2 across opposite sides through midpoints"),
        ("rhombus", 2, "2 along its diagonals"),
        ("kite", 1, "1 along its main line of symmetry between the equal angles")
    ]
    shape, lines, desc = rng.choice(cases)

    prompt = (
        f"How many **lines of symmetry** does a **{shape}** have?\n"
        f"Describe where they are located."
    )
    sol = (
        f"**Step 1:** A {shape} has **{lines} line(s) of symmetry** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Location: {desc} [1 Mark: Description]."
    )
    return {
        "id": f"g7_g2d_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{lines}; {desc}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "50_line_symmetry_of_quadrilaterals",
        "hints": {
            "tier_1": f"How many ways can you fold a {shape} exactly onto itself?",
            "tier_2": f"It has {lines} lines.",
            "tier_3": f"{lines} lines of symmetry."
        }
    }
