"""
Grade 7 Mathematics - Geometry of 2D Shapes Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of 2D shapes.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Triangle Classification & Properties (01 - 08)
# ==============================================================================

def arch_01_classify_triangle_by_sides(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("equilateral", (6, 6, 6), "Equilateral triangle", "all three sides are equal in length"),
        ("isosceles", (7, 7, 4), "Isosceles triangle", "two sides are equal in length"),
        ("scalene", (5, 7, 9), "Scalene triangle", "all three sides have different lengths")
    ]
    kind, sides, name, reason = rng.choice(cases)
    a, b, c = sides

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 220 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,130 180,130 110,35" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="110" y="148" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{c} cm</text>'
            f'<text x="65" y="80" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="end">{a} cm</text>'
            f'<text x="155" y="80" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="start">{b} cm</text>'
            f'</svg>'
        ),
        "caption": f"Triangle with side lengths {a} cm, {b} cm, and {c} cm",
        "diagram_role": "context"
    }

    prompt = (
        f"A triangle has side lengths of **{a} cm**, **{b} cm**, and **{c} cm**.\n\n"
        f"1. Classify this triangle according to its side lengths.\n"
        f"2. Give a geometric reason for your answer."
    )
    sol = (
        f"**Step 1:** The triangle is an **{name}** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Reason: {reason} [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "01_classify_triangle_by_sides",
        "hints": {
            "tier_1": f"Compare sides: {a}, {b}, and {c}.",
            "tier_2": f"It is an {name}.",
            "tier_3": f"{name} because {reason}."
        }
    }


def arch_02_classify_triangle_by_angles(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ((60, 70, 50), "Acute-angled triangle", "all three interior angles are less than 90°"),
        ((90, 55, 35), "Right-angled triangle", "one interior angle is exactly 90°"),
        ((115, 40, 25), "Obtuse-angled triangle", "one interior angle is greater than 90°")
    ]
    angles, name, reason = rng.choice(cases)
    a1, a2, a3 = angles

    prompt = (
        f"A triangle has interior angles measuring **{a1}°**, **{a2}°**, and **{a3}°**.\n\n"
        f"1. Classify this triangle according to its angles.\n"
        f"2. Give a geometric reason for your classification."
    )
    sol = (
        f"**Step 1:** The triangle is an **{name}** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Reason: {reason} [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "02_classify_triangle_by_angles",
        "hints": {
            "tier_1": f"Look at the largest angle: {max(a1, a2, a3)}°.",
            "tier_2": f"It is an {name}.",
            "tier_3": f"{name} because {reason}."
        }
    }


def arch_03_equilateral_triangle_angle_property(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In an equilateral triangle $\\Delta ABC$, all three sides are equal ($AB = BC = CA$).\n\n"
        f"1. Calculate the exact size of each interior angle.\n"
        f"2. State the geometric reason supporting your calculation."
    )
    sol = (
        f"**Step 1:** The interior angles of any triangle sum to $180^\\circ$. In an equilateral triangle, all three angles are equal: "
        f"$$\\frac{{180^\\circ}}{{3}} = \\mathbf{{60^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"**Step 2:** Reason: In an equilateral triangle, all three interior angles are equal and sum to $180^\\circ$ [1 Mark: Reason]."
    )
    return {
        "id": f"g7_g2d_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "60°; all angles equal and sum to 180°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "03_equilateral_triangle_angle_property",
        "hints": {
            "tier_1": "Divide 180° by 3.",
            "tier_2": "180 / 3 = 60°.",
            "tier_3": "Each angle is 60°."
        }
    }


def arch_04_isosceles_base_angle_property(rng: random.Random) -> Dict[str, Any]:
    top_y = rng.choice([25, 30, 35, 40])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,130 160,130 100,{top_y}" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="68" y1="78" x2="72" y2="82" stroke="#ef4444" stroke-width="2"/>'
            f'<line x1="128" y1="78" x2="132" y2="82" stroke="#ef4444" stroke-width="2"/>'
            f'<text x="100" y="{top_y - 8}" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>'
            f'<text x="30" y="142" font-size="12" font-weight="bold" fill="#0f172a">B</text>'
            f'<text x="165" y="142" font-size="12" font-weight="bold" fill="#0f172a">C</text>'
            f'</svg>'
        ),
        "caption": "Isosceles triangle ABC with AB = AC",
        "diagram_role": "context"
    }

    prompt = (
        f"In triangle $ABC$, side $AB = AC$ (as indicated by the tick marks).\n\n"
        f"Which two angles in $\\Delta ABC$ are equal to each other? State the geometric theorem."
    )
    sol = (
        f"**Step 1:** The angles opposite the equal sides are equal: $$\\mathbf{{\\hat{{B}} = \\hat{{C}}}} \\text{{ [1 Mark: Accuracy]}}$$\n\n"
        f"**Step 2:** Theorem / Reason: **Angles opposite equal sides in an isosceles triangle are equal** [1 Mark: Reason]."
    )
    return {
        "id": f"g7_g2d_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Angle B = Angle C; angles opposite equal sides are equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "04_isosceles_base_angle_property",
        "hints": {
            "tier_1": "The base angles opposite the equal sides are equal.",
            "tier_2": "Angle B and Angle C.",
            "tier_3": "Angle B = Angle C (angles opposite equal sides are equal)."
        }
    }


def arch_05_right_angled_isosceles_angles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A triangle is both **right-angled** and **isosceles**.\n\n"
        f"Calculate the size of each of the other two non-right angles, showing all working."
    )
    sol = (
        f"**Step 1:** The right angle is $90^\\circ$. The sum of the remaining two angles is $180^\\circ - 90^\\circ = 90^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** Since the triangle is isosceles, the other two angles are equal: "
        f"$$\\frac{{90^\\circ}}{{2}} = \\mathbf{{45^\\circ}} \\text{{ each [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "45° each",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_right_angled_isosceles_angles",
        "hints": {
            "tier_1": "The two equal angles must add up to 90°.",
            "tier_2": "90 / 2 = 45°.",
            "tier_3": "45° each."
        }
    }


def arch_06_scalene_triangle_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Can an equilateral triangle have a right angle? Can a scalene triangle have a right angle?\n"
        f"Explain both answers."
    )
    sol = (
        f"**Step 1 (Equilateral):** **No.** In an equilateral triangle, every angle must equal $60^\\circ$, so none can be $90^\\circ$ [1 Mark].\n\n"
        f"**Step 2 (Scalene):** **Yes.** A right-angled triangle can have three unequal sides (e.g. side lengths 3 cm, 4 cm, 5 cm) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_geo_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Equilateral: No (all angles are 60°); Scalene: Yes (e.g. 3-4-5 right triangle)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_scalene_triangle_properties",
        "hints": {
            "tier_1": "Equilateral angles are always 60°. Can a triangle have sides 3, 4, 5 with a 90° angle?",
            "tier_2": "Equilateral no; Scalene yes.",
            "tier_3": "Equilateral cannot; Scalene can."
        }
    }


def arch_07_geometric_impossibility_two_obtuse_angles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner attempts to draw a triangle containing two obtuse angles (each greater than 90°).\n\n"
        f"Explain mathematically why it is impossible for any triangle to have two obtuse angles."
    )
    sol = (
        f"**Step 1:** An obtuse angle is strictly greater than $90^\\circ$. Two obtuse angles would sum to: "
        f"$$\\text{{Sum}} > 90^\\circ + 90^\\circ = 180^\\circ \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** But the sum of ALL THREE interior angles of a triangle must equal exactly $180^\\circ$. Two obtuse angles alone would already exceed $180^\\circ$ before adding the third angle, making a triangle impossible [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Two obtuse angles sum to > 180°, which exceeds the total sum of angles in a triangle (180°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "07_geometric_impossibility_two_obtuse_angles",
        "hints": {
            "tier_1": "What is the sum of angles in any triangle? What is 91° + 91°?",
            "tier_2": "Two angles > 90° already exceed 180°.",
            "tier_3": "Sum exceeds 180°, which violates the triangle angle sum theorem."
        }
    }


def arch_08_adjacent_vs_opposite_sides(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([15, 20, 25, 30])
    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,120 180,120 {180+dx},40 {40+dx},40" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="{30+dx}" y="32" font-size="12" font-weight="bold">A</text>'
            f'<text x="{185+dx}" y="32" font-size="12" font-weight="bold">B</text>'
            f'<text x="185" y="138" font-size="12" font-weight="bold">C</text>'
            f'<text x="30" y="138" font-size="12" font-weight="bold">D</text>'
            f'</svg>'
        ),
        "caption": "Quadrilateral ABCD",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to quadrilateral $ABCD$.\n\n"
        f"1. Name the side that is **opposite** to side $AB$.\n"
        f"2. Name two sides that are **adjacent** (next to) side $AB$."
    )
    sol = (
        f"**Step 1:** The side opposite to $AB$ across the quadrilateral is **$DC$** (or $CD$) [1 Mark: Method].\n\n"
        f"**Step 2:** The adjacent sides that share a corner vertex with $AB$ are **$AD$** (meets at vertex $A$) and **$BC$** (meets at vertex $B$) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. CD (or DC); 2. AD and BC",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "08_adjacent_vs_opposite_sides",
        "hints": {
            "tier_1": "Opposite side does not touch AB. Adjacent sides share vertices A or B.",
            "tier_2": "Opposite is DC. Adjacent are AD and BC.",
            "tier_3": "1. DC; 2. AD and BC."
        }
    }


# ==============================================================================
# CLUSTER 2: Triangle Interior Angles Calculation (09 - 16)
# ==============================================================================

def arch_09_missing_angle_scalene_triangle(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([42, 48, 55, 62, 68])
    a2 = rng.choice([38, 45, 52, 58])
    a3 = 180 - (a1 + a2)

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 220 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="30,130 190,130 130,35" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="50" y="122" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>'
            f'<text x="160" y="122" font-size="12" font-weight="bold" fill="#2563eb">{a2}°</text>'
            f'<text x="130" y="55" font-size="13" font-weight="bold" fill="#ef4444">x</text>'
            f'</svg>'
        ),
        "caption": f"Triangle with two known angles of {a1}° and {a2}°",
        "diagram_role": "context"
    }

    prompt = (
        f"In the triangle shown, two interior angles measure **{a1}°** and **{a2}°**.\n\n"
        f"Calculate the value of the third interior angle $x$, stating the geometric reason."
    )
    sol = (
        f"**Step 1:** The sum of interior angles of a triangle is $180^\\circ$ [1 Mark: Reason (sum of $\\angle$s in $\\Delta$)].\n\n"
        f"**Step 2:** $$x = 180^\\circ - ({a1}^\\circ + {a2}^\\circ) = 180^\\circ - {a1 + a2}^\\circ = \\mathbf{{{a3}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a3}° (sum of angles in triangle = 180°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "09_missing_angle_scalene_triangle",
        "hints": {
            "tier_1": f"Add {a1}° and {a2}°, then subtract from 180°.",
            "tier_2": f"180 - ({a1} + {a2}) = {a3}.",
            "tier_3": f"{a3}°."
        }
    }


def arch_10_missing_acute_angle_right_triangle(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([28, 35, 42, 55, 63, 72])
    a2 = 90 - a1

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,130 170,130 40,30" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<rect x="40" y="115" width="15" height="15" fill="none" stroke="#ef4444" stroke-width="2"/>'
            f'<text x="140" y="122" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>'
            f'<text x="50" y="55" font-size="13" font-weight="bold" fill="#ef4444">y</text>'
            f'</svg>'
        ),
        "caption": f"Right-angled triangle with one acute angle of {a1}°",
        "diagram_role": "context"
    }

    prompt = (
        f"In a right-angled triangle, one of the acute angles measures **{a1}°**.\n\n"
        f"Calculate the value of the other acute angle $y$, giving a reason."
    )
    sol = (
        f"**Step 1:** The acute angles of a right triangle are complementary ($90^\\circ$) [1 Mark: Reason].\n\n"
        f"**Step 2:** $$y = 90^\\circ - {a1}^\\circ = \\mathbf{{{a2}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{a2}° (sum of angles in right triangle = 180°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "10_missing_acute_angle_right_triangle",
        "hints": {
            "tier_1": f"Subtract {a1}° from 90°.",
            "tier_2": f"90 - {a1} = {a2}.",
            "tier_3": f"{a2}°."
        }
    }


def arch_11_base_angles_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    vertex_angle = rng.choice([40, 50, 70, 80, 100])
    base_angle = (180 - vertex_angle) // 2

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,130 160,130 100,30" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="100" y="50" font-size="12" font-weight="bold" fill="#2563eb" text-anchor="middle">{vertex_angle}°</text>'
            f'<text x="50" y="122" font-size="12" font-weight="bold" fill="#ef4444">x</text>'
            f'<text x="140" y="122" font-size="12" font-weight="bold" fill="#ef4444">x</text>'
            f'</svg>'
        ),
        "caption": f"Isosceles triangle with vertex angle = {vertex_angle}°",
        "diagram_role": "context"
    }

    prompt = (
        f"In an isosceles triangle, the vertex angle between the two equal sides measures **{vertex_angle}°**.\n\n"
        f"Calculate the size of each of the two equal base angles ($x$), stating the geometric reasons."
    )
    sol = (
        f"**Step 1:** Base angles are equal (angles opposite equal sides). Sum of angles in triangle is $180^\\circ$ [1 Mark: Reason].\n\n"
        f"**Step 2:** $$2x = 180^\\circ - {vertex_angle}^\\circ = {180 - vertex_angle}^\\circ \\implies x = \\frac{{{180 - vertex_angle}^\\circ}}{{2}} = \\mathbf{{{base_angle}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{base_angle}° each",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "11_base_angles_isosceles_triangle",
        "hints": {
            "tier_1": f"Subtract {vertex_angle}° from 180°, then divide by 2.",
            "tier_2": f"({180 - vertex_angle}) / 2 = {base_angle}.",
            "tier_3": f"{base_angle}°."
        }
    }


def arch_12_vertex_angle_isosceles_from_base(rng: random.Random) -> Dict[str, Any]:
    base_angle = rng.choice([35, 45, 55, 65, 70])
    vertex_angle = 180 - 2 * base_angle

    prompt = (
        f"In an isosceles triangle, one of the equal base angles measures **{base_angle}°**.\n\n"
        f"Calculate the size of the vertex angle between the two equal sides."
    )
    sol = (
        f"**Step 1:** Both base angles are equal: ${base_angle}^\\circ$ each, totaling $2 \\times {base_angle}^\\circ = {2 * base_angle}^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\text{{Vertex angle}} = 180^\\circ - {2 * base_angle}^\\circ = \\mathbf{{{vertex_angle}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{vertex_angle}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_vertex_angle_isosceles_from_base",
        "hints": {
            "tier_1": f"Double {base_angle}° and subtract from 180°.",
            "tier_2": f"180 - (2 * {base_angle}) = {vertex_angle}.",
            "tier_3": f"{vertex_angle}°."
        }
    }


def arch_13_exterior_angle_of_triangle(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([40, 50, 60, 65])
    a2 = rng.choice([35, 45, 55])
    ext = a1 + a2

    svg_diag = {
        "kind": "inline_svg",
        "svg": (
            f'<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
            f'<polygon points="40,110 160,110 110,30" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>'
            f'<line x1="160" y1="110" x2="220" y2="110" stroke="#1e293b" stroke-width="2.5"/>'
            f'<text x="55" y="102" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>'
            f'<text x="110" y="50" font-size="12" font-weight="bold" fill="#2563eb">{a2}°</text>'
            f'<text x="175" y="102" font-size="12" font-weight="bold" fill="#ef4444">e</text>'
            f'</svg>'
        ),
        "caption": f"Exterior angle e of a triangle with opposite interior angles {a1}° and {a2}°",
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the triangle diagram with extended base line.\n\n"
        f"Two interior opposite angles measure **{a1}°** and **{a2}°**.\n"
        f"Calculate the exterior angle $e$, stating the geometric theorem."
    )
    sol = (
        f"**Step 1:** The exterior angle of a triangle equals the sum of the two opposite interior angles [1 Mark: Theorem (ext $\\angle$ of $\\Delta$)].\n\n"
        f"**Step 2:** $$e = {a1}^\\circ + {a2}^\\circ = \\mathbf{{{ext}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ext}° (exterior angle = sum of opposite interior angles)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": svg_diag,
        "subskill": "13_exterior_angle_of_triangle",
        "hints": {
            "tier_1": f"Add the two interior opposite angles: {a1}° + {a2}°.",
            "tier_2": f"{a1} + {a2} = {ext}.",
            "tier_3": f"{ext}°."
        }
    }


def arch_14_equilateral_triangle_solve_variable(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([2, 3, 4])
    ans_x = 60 // mult

    prompt = (
        f"In an equilateral triangle, one of the interior angles is given as $({mult}x)^\\circ$.\n\n"
        f"Solve for $x$, giving a geometric reason."
    )
    sol = (
        f"**Step 1:** Every angle in an equilateral triangle is exactly $60^\\circ$ [1 Mark: Reason].\n\n"
        f"**Step 2:** Set up equation: $${mult}x = 60^\\circ \\implies x = \\frac{{60^\\circ}}{{{mult}}} = \\mathbf{{{ans_x}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"x = {ans_x}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_equilateral_triangle_solve_variable",
        "hints": {
            "tier_1": f"Set {mult}x equal to 60°.",
            "tier_2": f"60 / {mult} = {ans_x}.",
            "tier_3": f"x = {ans_x}."
        }
    }


def arch_15_algebraic_angles_in_triangle(rng: random.Random) -> Dict[str, Any]:
    # Angles: 2x, 3x, 4x => 9x = 180 => x = 20
    prompt = (
        f"The three interior angles of a triangle are expressed as $2x$, $3x$, and $4x$.\n\n"
        f"1. Solve for $x$.\n"
        f"2. Calculate the size of the largest angle in the triangle."
    )
    sol = (
        f"**Step 1:** Sum of angles in triangle $= 180^\\circ$:\n"
        f"$$2x + 3x + 4x = 180^\\circ \\implies 9x = 180^\\circ \\implies x = \\mathbf{{20^\\circ}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Largest angle is $4x$: $$4 \\times 20^\\circ = \\mathbf{{80^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. x = 20°; 2. 80°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_algebraic_angles_in_triangle",
        "hints": {
            "tier_1": "Add 2x + 3x + 4x = 9x. Set equal to 180°.",
            "tier_2": "180 / 9 = 20. Largest is 4 * 20 = 80°.",
            "tier_3": "x = 20°; largest angle is 80°."
        }
    }


def arch_16_overlapping_composite_triangles(rng: random.Random) -> Dict[str, Any]:
    a = 50
    b = 60
    # Two adjacent triangles sharing a side
    prompt = (
        f"Two triangles $ABD$ and $CBD$ meet along line segment $BD$.\n"
        f"In $\\Delta ABD$, $\\hat{{A}} = 50^\\circ$ and $\\angle ABD = 60^\\circ$.\n\n"
        f"Calculate the size of $\\angle ADB$."
    )
    ans = 180 - (50 + 60)  # 70
    sol = (
        f"**Step 1:** Focus on $\\Delta ABD$ where sum of angles is $180^\\circ$ [1 Mark: Method].\n\n"
        f"**Step 2:** $$\\angle ADB = 180^\\circ - (50^\\circ + 60^\\circ) = 180^\\circ - 110^\\circ = \\mathbf{{{ans}^\\circ}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_g2d_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_overlapping_composite_triangles",
        "hints": {
            "tier_1": "Look only inside triangle ABD.",
            "tier_2": "180 - (50 + 60) = 70.",
            "tier_3": f"{ans}°."
        }
    }


# ==============================================================================
# CLUSTER 3: Quadrilateral Classification & Properties (17 - 25)
# ==============================================================================

def arch_17_properties_of_rectangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State three fundamental geometric properties of a **rectangle** concerning its angles, opposite sides, and diagonals."
    )
    sol = (
        f"**Step 1 (Angles):** All four interior angles are equal to **$90^\\circ$ (right angles)** [1 Mark].\n\n"
        f"**Step 2 (Sides & Diagonals):** Opposite sides are equal in length and parallel; diagonals are **equal in length** and bisect each other [1 Mark]."
    )
    return {
        "id": f"g7_g2d_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "All 4 angles are 90°; opposite sides equal/parallel; diagonals equal and bisect each other",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_properties_of_rectangle",
        "hints": {
            "tier_1": "Think about right angles, opposite sides, and diagonals.",
            "tier_2": "4 right angles, opposite sides parallel and equal, diagonals equal.",
            "tier_3": "4 right angles; opposite sides equal and parallel; diagonals equal."
        }
    }


def arch_18_properties_of_square(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State two properties that a **square** has that a standard rectangle does NOT necessarily have."
    )
    sol = (
        f"**Step 1:** In a square, **all four sides are equal in length** (a rectangle only requires opposite sides to be equal) [1 Mark].\n\n"
        f"**Step 2:** The diagonals of a square **bisect each other at right angles ($90^\\circ$)** [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "All 4 sides are equal; diagonals intersect at 90°",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_properties_of_square",
        "hints": {
            "tier_1": "Are all 4 sides of a rectangle equal? Do rectangle diagonals meet at 90°?",
            "tier_2": "A square has all 4 sides equal and diagonals perpendicular.",
            "tier_3": "All 4 sides equal; diagonals perpendicular (90°)."
        }
    }


def arch_19_properties_of_parallelogram(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a parallelogram $ABCD$, state the geometric relationship between:\n"
        f"1. Opposite sides $AB$ and $CD$\n"
        f"2. Opposite angles $\\hat{{A}}$ and $\\hat{{C}}$"
    )
    sol = (
        f"**Step 1:** Opposite sides are **equal in length and parallel** ($AB = CD$ and $AB \\parallel CD$) [1 Mark].\n\n"
        f"**Step 2:** Opposite angles are **equal in size** ($\\hat{{A}} = \\hat{{C}}$) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Opposite sides equal and parallel; 2. Opposite angles are equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_properties_of_parallelogram",
        "hints": {
            "tier_1": "Parallelogram: opposite sides are parallel/equal; opposite angles are equal.",
            "tier_2": "AB || CD and AB = CD. Angle A = Angle C.",
            "tier_3": "1. Equal and parallel; 2. Equal."
        }
    }


def arch_20_properties_of_rhombus(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A rhombus is a special type of parallelogram.\n\n"
        f"1. How do all four side lengths of a rhombus compare?\n"
        f"2. At what angle do the diagonals of a rhombus intersect each other?"
    )
    sol = (
        f"**Step 1:** In a rhombus, **all four sides are equal in length** [1 Mark].\n\n"
        f"**Step 2:** The diagonals intersect at **$90^\\circ$ (perpendicular to each other)** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_g2d_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. All four sides are equal; 2. 90° (perpendicular)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_properties_of_rhombus",
        "hints": {
            "tier_1": "A rhombus is a pushed-over square.",
            "tier_2": "All 4 sides equal; diagonals meet at 90°.",
            "tier_3": "1. All 4 sides equal; 2. 90°."
        }
    }


def arch_21_properties_of_trapezium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What is the defining geometric feature that distinguishes a **trapezium** from other quadrilaterals?"
    )
    sol = (
        f"**Step 1:** A trapezium is a quadrilateral with **exactly one pair of opposite sides parallel** [2 Marks: Precise definition]."
    )
    return {
        "id": f"g7_g2d_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "It has exactly one pair of opposite sides parallel",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_properties_of_trapezium",
        "hints": {
            "tier_1": "How many pairs of parallel sides does a trapezium have?",
            "tier_2": "Exactly one pair.",
            "tier_3": "Exactly one pair of opposite sides parallel."
        }
    }


def arch_22_properties_of_kite(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"State two key geometric properties of a **kite** regarding its sides and diagonals."
    )
    sol = (
        f"**Step 1 (Sides):** A kite has **two pairs of adjacent sides equal in length** [1 Mark].\n\n"
        f"**Step 2 (Diagonals):** Its diagonals intersect at **right angles ($90^\\circ$)**, and the longer diagonal bisects the shorter diagonal [1 Mark]."
    )
    return {
        "id": f"g7_g2d_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Two pairs of adjacent sides equal; diagonals perpendicular (90°)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_properties_of_kite",
        "hints": {
            "tier_1": "Think of a traditional flying kite shape.",
            "tier_2": "Two pairs of adjacent sides equal, diagonals meet at 90°.",
            "tier_3": "Two pairs of adjacent sides equal; diagonals intersect at 90°."
        }
    }


def arch_23_distinguish_square_from_rhombus(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Both a square and a rhombus have four sides of equal length.\n\n"
        f"What is the key geometric difference between a square and a rhombus?"
    )
    sol = (
        f"**Step 1:** A square must have **four right angles ($90^\\circ$)** [1 Mark].\n\n"
        f"**Step 2:** A standard rhombus does NOT have right angles (its interior angles are acute and obtuse) [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "A square has four 90° right angles; a rhombus does not have to have right angles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_distinguish_square_from_rhombus",
        "hints": {
            "tier_1": "Look at the interior corners.",
            "tier_2": "Square has 90° angles; rhombus has acute/obtuse angles.",
            "tier_3": "Square has 90° angles; rhombus does not."
        }
    }


def arch_24_distinguish_rectangle_from_parallelogram(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Why is every rectangle a parallelogram, but not every parallelogram is a rectangle?"
    )
    sol = (
        f"**Step 1:** Every rectangle has opposite sides parallel and equal, which satisfies the definition of a parallelogram [1 Mark].\n\n"
        f"**Step 2:** However, a rectangle specifically requires all four angles to be **$90^\\circ$**, whereas a general parallelogram can have non-right angles [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "A rectangle has opposite sides parallel, but a parallelogram does not necessarily have 90° right angles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_distinguish_rectangle_from_parallelogram",
        "hints": {
            "tier_1": "What special angle property does a rectangle have?",
            "tier_2": "A rectangle has 90° angles.",
            "tier_3": "A rectangle requires 90° angles; general parallelograms do not."
        }
    }


def arch_25_quadrilateral_hierarchy_true_false(rng: random.Random) -> Dict[str, Any]:
    statements = [
        ("Every square is a rectangle.", "True", "A square has 4 right angles and opposite sides parallel/equal"),
        ("Every rectangle is a square.", "False", "A rectangle does not necessarily have all 4 sides equal"),
        ("Every square is a rhombus.", "True", "A square has 4 equal sides and opposite sides parallel"),
        ("Every parallelogram is a trapezium.", "False", "A trapezium has only one pair of parallel sides, whereas a parallelogram has two")
    ]
    stmt, ans, reason = rng.choice(statements)

    prompt = (
        f"State whether the following statement is **True** or **False**, and give a reason:\n\n"
        f"\"{stmt}\""
    )
    sol = (
        f"**Step 1:** The statement is **{ans}** [1 Mark: Accuracy].\n\n"
        f"**Step 2:** Reason: {reason} [1 Mark: Reasoning]."
    )
    return {
        "id": f"g7_g2d_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{ans}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_quadrilateral_hierarchy_true_false",
        "hints": {
            "tier_1": "Consider the definitions of both shapes.",
            "tier_2": f"It is {ans}.",
            "tier_3": f"{ans} because {reason}."
        }
    }
