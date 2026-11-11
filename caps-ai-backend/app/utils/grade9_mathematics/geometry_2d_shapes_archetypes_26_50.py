"""Grade 9 Mathematics - Geometry of 2D Shapes Archetypes 26 to 50.
Grounded strictly in curriculum_docs_auto/Mathematics_Gr9/Term 2/04. Geometry of 2D shapes.md:
Similarity of triangles (AAA, proportional sides), scale factors, formal proofs,
quadrilaterals (parallelogram, rectangle, rhombus, square, trapezium, kite),
interior angle sums (360°), diagonal properties, proving quadrilaterals,
regular polygons (interior/exterior angle sums and individual sizes), error analysis, and synthesis.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .geometry_2d_shapes_svg import (
    draw_quadrilateral_svg,
    draw_regular_polygon_svg,
)


# ----------------------------------------------------------------------
# 26. Similarity Condition AAA: Equiangular
# ----------------------------------------------------------------------
def arch_26_similarity_condition_aaa_equiangular(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(40, 70)
    b = rng.randint(40, 180 - a - 25)
    c = 180 - (a + b)

    prompt = (
        f"In \\(\\triangle ABC\\), \\(\\hat{{A}} = {a}^\\circ\\), \\(\\hat{{B}} = {b}^\\circ\\), and \\(\\hat{{C}} = {c}^\\circ\\). "
        f"In \\(\\triangle DEF\\), \\(\\hat{{D}} = {a}^\\circ\\), \\(\\hat{{E}} = {b}^\\circ\\), and \\(\\hat{{F}} = {c}^\\circ\\). "
        f"State the geometric relationship between \\(\\triangle ABC\\) and \\(\\triangle DEF\\) and the condition that justifies it."
    )
    sol = (
        f"**Analysis:**\n"
        f"1. \\(\\hat{{A}} = \\hat{{D}} = {a}^\\circ\\)\n"
        f"2. \\(\\hat{{B}} = \\hat{{E}} = {b}^\\circ\\)\n"
        f"3. \\(\\hat{{C}} = \\hat{{F}} = {c}^\\circ\\)\n\n"
        f"All three pairs of corresponding angles are equal (the triangles are equiangular).\n"
        f"Therefore, \\(\\triangle ABC \\;///\\; \\triangle DEF\\) **[AAA]** (equiangular triangles are similar)."
    )
    return {
        "id": f"g9_geom_sim_aaa_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Similar [AAA]",
        "expected_answer": "Similar [AAA]",
        "sample_answer": "The triangles are similar [AAA / equiangular].",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify relationship as similar (///)", "marks": 1},
            {"desc": "State condition as AAA (equiangular)", "marks": 1},
        ],
        "hints": [
            "Check the corresponding angles of both triangles.",
            "When all three pairs of corresponding angles are equal, the triangles have the same shape but possibly different sizes.",
            "Condition is AAA (Similar).",
        ],
    }


# ----------------------------------------------------------------------
# 27. Similarity Statement: Correct Vertex Order
# ----------------------------------------------------------------------
def arch_27_similarity_statement_correct_vertex_order(rng: random.Random) -> Dict[str, Any]:
    tri_pairs = [
        ("ABC", "DEF", "A corresponds to D, B to E, C to F"),
        ("PQR", "XYZ", "P corresponds to X, Q to Y, R to Z"),
        ("KLM", "RST", "K corresponds to R, L to S, M to T"),
        ("ABC", "FED", "A corresponds to F, B to E, C to D"),
    ]
    t1, t2, desc = rng.choice(tri_pairs)

    prompt = (
        f"Two similar triangles have corresponding vertices such that {desc}. "
        f"Write down the formal similarity statement with vertices in the correct corresponding order:\n"
        f"\\[ \\triangle {t1} \\;///\\; \\triangle \\text{{???}} \\]"
    )
    sol = (
        f"**Vertex Matching:**\n"
        f"\\({t1[0]} \\leftrightarrow {t2[0]}\\)\n"
        f"\\({t1[1]} \\leftrightarrow {t2[1]}\\)\n"
        f"\\({t1[2]} \\leftrightarrow {t2[2]}\\)\n\n"
        f"**Similarity Statement:**\n"
        f"\\[ \\triangle {t1} \\;///\\; \\triangle {t2} \\]"
    )
    return {
        "id": f"g9_geom_sim_order_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": t2,
        "expected_answer": t2,
        "sample_answer": f"\\triangle {t2}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Match vertices in corresponding order", "marks": 1},
            {"desc": f"State triangle name as {t2}", "marks": 1},
        ],
        "hints": [
            "In a similarity statement, vertices must be named in the order of equal corresponding angles.",
            f"First vertex is {t2[0]}, second is {t2[1]}, third is {t2[2]}.",
            f"The triangle name is {t2}.",
        ],
    }


# ----------------------------------------------------------------------
# 28. Similarity: Calculate Scale Factor
# ----------------------------------------------------------------------
def arch_28_similarity_calculate_scale_factor(rng: random.Random) -> Dict[str, Any]:
    s1 = rng.choice([4, 5, 6, 8])
    scale = rng.choice([2, 3, 4, 5])
    s2 = s1 * scale

    prompt = (
        f"\\(\\triangle ABC \\;///\\; \\triangle DEF\\). "
        f"If side \\(AB = {s1}\\text{{ cm}}\\) and corresponding side \\(DE = {s2}\\text{{ cm}}\\), "
        f"calculate the scale factor of enlargement from \\(\\triangle ABC\\) to \\(\\triangle DEF\\)."
    )
    sol = (
        f"**Scale Factor Formula:**\n"
        f"\\[ \\text{{Scale factor}} = \\frac{{\\text{{Side length of image }}\\triangle DEF}}{{\\text{{Side length of original }}\\triangle ABC}} \\]\n"
        f"\\[ = \\frac{{DE}}{{AB}} = \\frac{{{s2}}}{{{s1}}} = {scale} \\]\n\n"
        f"The scale factor is **{scale}**."
    )
    return {
        "id": f"g9_geom_sim_scale_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(scale),
        "expected_answer": str(scale),
        "sample_answer": str(scale),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Set up ratio DE / AB = {s2} / {s1}", "marks": 1},
            {"desc": f"Calculate scale factor = {scale}", "marks": 1},
        ],
        "hints": [
            "Divide the enlarged side length by the original side length.",
            f"Calculation: {s2} ÷ {s1}.",
            f"The scale factor is {scale}.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Similarity: Calculate Unknown Side Proportion
# ----------------------------------------------------------------------
def arch_29_similarity_calculate_unknown_side_proportion(rng: random.Random) -> Dict[str, Any]:
    # AB / DE = BC / EF => ab / de = bc / x => x = (de * bc) / ab
    ab = rng.choice([3, 4, 5, 6])
    scale = rng.choice([2, 3])
    de = ab * scale

    bc = rng.randint(4, 9)
    ef = bc * scale

    prompt = (
        f"It is given that \\(\\triangle ABC \\;///\\; \\triangle DEF\\). "
        f"Side lengths are given as \\(AB = {ab}\\text{{ cm}}\\), \\(DE = {de}\\text{{ cm}}\\), and "
        f"\\(BC = {bc}\\text{{ cm}}\\). "
        f"Calculate the length of the corresponding side \\(EF\\) in centimetres."
    )
    sol = (
        f"**Proportionality Statement | Reason:**\n"
        f"\\[ \\frac{{EF}}{{BC}} = \\frac{{DE}}{{AB}} \\quad [\\text{{corresponding sides of similar }}\\triangle\\text{{s in proportion}}] \\]\n"
        f"\\[ \\frac{{EF}}{{{bc}}} = \\frac{{{de}}}{{{ab}}} \\]\n"
        f"\\[ \\frac{{EF}}{{{bc}}} = {scale} \\]\n"
        f"\\[ EF = {bc} \\times {scale} = {ef}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_sim_prop_side_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ef} cm",
        "expected_answer": f"{ef} cm",
        "sample_answer": f"EF = {ef} cm [sides in proportion]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Set up ratio equation EF/BC = DE/AB [sides in proportion]", "marks": 1},
            {"desc": f"Substitute values: EF/{bc} = {de}/{ab}", "marks": 1},
            {"desc": f"Calculate EF = {ef} cm", "marks": 1},
        ],
        "hints": [
            "Corresponding sides of similar triangles are in proportion.",
            f"Find the ratio DE / AB: {de} ÷ {ab} = {scale}.",
            f"Multiply BC ({bc} cm) by {scale} to find EF ({ef} cm).",
        ],
    }


# ----------------------------------------------------------------------
# 30. Similarity: Formal Proof Equiangular
# ----------------------------------------------------------------------
def arch_30_similarity_formal_proof_equiangular(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(40, 65)
    b = rng.randint(45, 70)
    c = 180 - a - b

    prompt = (
        f"In \\(\\triangle ABC\\), \\(\\hat{{A}} = {a}^\\circ\\) and \\(\\hat{{B}} = {b}^\\circ\\). "
        f"In \\(\\triangle DEF\\), \\(\\hat{{D}} = {a}^\\circ\\) and \\(\\hat{{F}} = {c}^\\circ\\). "
        f"Provide the formal 2-column proof to prove that \\(\\triangle ABC \\;///\\; \\triangle DEF\\)."
    )
    sol = (
        f"**Step 1: Calculate the third angle in \\(\\triangle ABC\\).**\n"
        f"\\[ \\hat{{C}} = 180^\\circ - ({a}^\\circ + {b}^\\circ) = {c}^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n\n"
        f"**Step 2: Formal proof in \\(\\triangle ABC\\) and \\(\\triangle DEF\\):**\n"
        f"1. \\(\\hat{{A}} = \\hat{{D}} = {a}^\\circ\\) \\quad [given]\n"
        f"2. \\(\\hat{{C}} = \\hat{{F}} = {c}^\\circ\\) \\quad [proven above]\n"
        f"3. \\(\\hat{{B}} = \\hat{{E}} = {b}^\\circ\\) \\quad [third angle of triangle]\n"
        f"\\[ \\therefore \\triangle ABC \\;///\\; \\triangle DEF \\quad [\\text{{AAA}}] \\]"
    )
    return {
        "id": f"g9_geom_proof_sim_{rng.randint(100000, 999999)}",
        "question_type": "formal_proof",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "AAA",
        "expected_answer": "AAA",
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Calculate ∠C = {c}° [sum of ∠s in △]", "marks": 1},
            {"desc": "Show 2 pairs of corresponding angles equal [given]", "marks": 1},
            {"desc": "Show 3rd pair equal [3rd angle of △]", "marks": 1},
            {"desc": "Conclusion: △ABC /// △DEF [AAA]", "marks": 1},
        ],
        "hints": [
            f"Calculate angle C: 180° - ({a}° + {b}°) = {c}°.",
            "Compare angles: angle A = angle D, angle C = angle F, angle B = angle E.",
            "Conclude with reason [AAA].",
        ],
    }


# ----------------------------------------------------------------------
# 31. Similarity: Nested Triangles with Parallel Transversal
# ----------------------------------------------------------------------
def arch_31_similarity_nested_triangles_parallel_transversal(rng: random.Random) -> Dict[str, Any]:
    # Triangle ABC with DE || BC
    ad = rng.choice([3, 4, 5])
    db = rng.choice([3, 4, 5])
    ab = ad + db

    de = rng.choice([4, 6, 8])
    # BC = de * ab / ad
    # choose ad and de so bc is integer
    factor = rng.choice([2, 3])
    de = ad * factor
    bc = ab * factor

    prompt = (
        f"In \\(\\triangle ABC\\), point \\(D\\) lies on \\(AB\\) and point \\(E\\) lies on \\(AC\\) such that \\(DE \\parallel BC\\). "
        f"Given \\(AD = {ad}\\text{{ cm}}\\), \\(DB = {db}\\text{{ cm}}\\), and \\(DE = {de}\\text{{ cm}}\\), "
        f"calculate the length of \\(BC\\) in centimetres. State the geometric reason."
    )
    sol = (
        f"**Step 1: Prove \\(\\triangle ADE \\;///\\; \\triangle ABC\\).**\n"
        f"1. \\(\\hat{{A}} = \\hat{{A}}\\) \\quad [common angle]\n"
        f"2. \\(A\\hat{{D}}E = \\hat{{B}}\\) \\quad [corr \\angle\\text{{s, }} DE \\parallel BC]\n"
        f"3. \\(A\\hat{{E}}D = \\hat{{C}}\\) \\quad [corr \\angle\\text{{s, }} DE \\parallel BC]\n"
        f"\\(\\therefore \\triangle ADE \\;///\\; \\triangle ABC\\) [AAA]\n\n"
        f"**Step 2: Set up the side proportion.**\n"
        f"\\[ AB = AD + DB = {ad} + {db} = {ab}\\text{{ cm}} \\]\n"
        f"\\[ \\frac{{BC}}{{DE}} = \\frac{{AB}}{{AD}} \\quad [\\text{{sides in proportion}}] \\]\n"
        f"\\[ \\frac{{BC}}{{{de}}} = \\frac{{{ab}}}{{{ad}}} = {factor} \\]\n"
        f"\\[ BC = {de} \\times {factor} = {bc}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_sim_nested_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{bc} cm",
        "expected_answer": f"{bc} cm",
        "sample_answer": f"BC = {bc} cm [△ADE /// △ABC, sides in proportion]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": "Establish △ADE /// △ABC [AAA, corr ∠s]", "marks": 1},
            {"desc": f"Find total length AB = {ab} cm", "marks": 1},
            {"desc": f"Set up ratio BC / DE = AB / AD", "marks": 1},
            {"desc": f"Calculate BC = {bc} cm", "marks": 1},
        ],
        "hints": [
            f"Because DE is parallel to BC, the small triangle ADE is similar to triangle ABC.",
            f"Total length AB = {ad} + {db} = {ab} cm.",
            f"Multiply DE ({de} cm) by the scale factor (AB / AD) to get BC ({bc} cm).",
        ],
    }


# ----------------------------------------------------------------------
# 32. Quadrilateral Interior Angle Sum Numeric
# ----------------------------------------------------------------------
def arch_32_quadrilateral_interior_angle_sum_numeric(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(65, 115)
    b = rng.randint(70, 120)
    c = rng.randint(60, 110)
    d = 360 - (a + b + c)

    prompt = (
        f"Three interior angles of a convex quadrilateral measure "
        f"\\({a}^\\circ\\), \\({b}^\\circ\\), and \\({c}^\\circ\\). "
        f"Calculate the size of the fourth interior angle. State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\text{{Sum of interior }}\\angle\\text{{s in a quadrilateral}} = 360^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in quad}}] \\]\n"
        f"\\[ {a}^\\circ + {b}^\\circ + {c}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ {a + b + c}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ x = 360^\\circ - {a + b + c}^\\circ = {d}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_quad_sum_num_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{d}°",
        "expected_answer": f"{d}°",
        "sample_answer": f"{d}° [sum of ∠s in quad]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply theorem: sum of angles in quadrilateral = 360°", "marks": 1},
            {"desc": f"Calculate missing angle = {d}°", "marks": 1},
        ],
        "hints": [
            "The sum of interior angles in any quadrilateral is 360°.",
            f"Add the three given angles: {a}° + {b}° + {c}° = {a + b + c}°.",
            f"Subtract from 360°: 360° - {a + b + c}° = {d}°.",
        ],
    }


# ----------------------------------------------------------------------
# 33. Quadrilateral Interior Angles: Algebraic
# ----------------------------------------------------------------------
def arch_33_quadrilateral_interior_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    # Angles: k1 x, k2 x, k3 x, k4 x => sum k_i = 12, 15, 18, 20, 24
    combos = [
        (2, 3, 3, 4),   # sum = 12 -> x = 30
        (2, 3, 4, 6),   # sum = 15 -> x = 24
        (3, 4, 5, 6),   # sum = 18 -> x = 20
        (2, 4, 6, 8),   # sum = 20 -> x = 18
        (3, 5, 7, 9),   # sum = 24 -> x = 15
    ]
    k1, k2, k3, k4 = rng.choice(combos)
    k_sum = k1 + k2 + k3 + k4
    x_val = 360 // k_sum
    largest_ang = max(k1, k2, k3, k4) * x_val

    prompt = (
        f"The four interior angles of a quadrilateral are given algebraically as "
        f"\\({k1}x\\), \\({k2}x\\), \\({k3}x\\), and \\({k4}x\\). "
        f"Solve for \\(x\\) and hence calculate the size of the **largest** interior angle in degrees."
    )
    sol = (
        f"**Step 1: Set up equation with angle sum theorem.**\n"
        f"\\[ {k1}x + {k2}x + {k3}x + {k4}x = 360^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in quad}}] \\]\n"
        f"\\[ {k_sum}x = 360^\\circ \\]\n"
        f"\\[ x = 360^\\circ \\div {k_sum} = {x_val}^\\circ \\]\n\n"
        f"**Step 2: Calculate the largest angle.**\n"
        f"\\[ \\text{{Largest angle}} = {max(k1, k2, k3, k4)}({x_val}^\\circ) = {largest_ang}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_quad_alg_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{largest_ang}°",
        "expected_answer": f"{largest_ang}°",
        "sample_answer": f"x = {x_val}°, largest angle = {largest_ang}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Set up {k_sum}x = 360° with reason [sum of ∠s in quad]", "marks": 1},
            {"desc": f"Solve for x = {x_val}°", "marks": 1},
            {"desc": f"Calculate largest angle = {largest_ang}°", "marks": 1},
        ],
        "hints": [
            f"Add all four terms: {k1}x + {k2}x + {k3}x + {k4}x = 360°.",
            f"Solve for x: {k_sum}x = 360°.",
            f"Multiply x by {max(k1, k2, k3, k4)} to find the largest angle ({largest_ang}°).",
        ],
    }


# ----------------------------------------------------------------------
# 34. Parallelogram: Opposite Angles Equal (with SVG diagram)
# ----------------------------------------------------------------------
def arch_34_parallelogram_opposite_angles_equal(rng: random.Random) -> Dict[str, Any]:
    ang_a = rng.choice([65, 70, 75, 80, 110, 115, 120, 125])
    coef = rng.choice([2, 3])
    x_val = rng.randint(15, 35)
    const = ang_a - coef * x_val

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="parallelogram",
        labels=("A", "B", "C", "D"),
        extra_text=f"A = {ang_a}°, C = {coef}x {'+' if const >= 0 else '-'} {abs(const)}°",
        seed=seed_val,
    )

    sign_str = f"+ {const}" if const >= 0 else f"- {abs(const)}"
    prompt = (
        f"In parallelogram \\(ABCD\\) shown in the diagram below, \\(\\hat{{A}} = {ang_a}^\\circ\\) "
        f"and opposite angle \\(\\hat{{C}} = ({coef}x {sign_str})^\\circ\\). "
        f"Calculate the value of \\(x\\). State the geometric theorem reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{C}} = \\hat{{A}} \\quad [\\text{{opposite }}\\angle\\text{{s of a parallelogram are equal}}] \\]\n"
        f"\\[ {coef}x {sign_str} = {ang_a} \\]\n"
        f"\\[ {coef}x = {ang_a - const} \\]\n"
        f"\\[ x = {x_val} \\]"
    )
    return {
        "id": f"g9_geom_parm_opp_ang_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_val),
        "expected_answer": str(x_val),
        "sample_answer": f"x = {x_val} [opp ∠s of parm]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Equate opposite angles with reason [opp ∠s of parm]", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Opposite angles of a parallelogram are equal in size.",
            f"Set up the equation: {coef}x {sign_str} = {ang_a}.",
            f"Solve for x: x = {x_val}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 35. Parallelogram: Co-Interior Angles Supplementary
# ----------------------------------------------------------------------
def arch_35_parallelogram_cointerior_consecutive_angles_supplementary(rng: random.Random) -> Dict[str, Any]:
    ang_a = rng.choice([60, 65, 70, 75, 80])
    ang_b = 180 - ang_a

    prompt = (
        f"In parallelogram \\(ABCD\\), angle \\(\\hat{{A}} = {ang_a}^\\circ\\). "
        f"Calculate the size of consecutive adjacent angle \\(\\hat{{B}}\\). State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{A}} + \\hat{{B}} = 180^\\circ \\quad [\\text{{co-interior }}\\angle\\text{{s, }} AD \\parallel BC] \\]\n"
        f"\\[ {ang_a}^\\circ + \\hat{{B}} = 180^\\circ \\]\n"
        f"\\[ \\hat{{B}} = 180^\\circ - {ang_a}^\\circ = {ang_b}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_parm_coint_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ang_b}°",
        "expected_answer": f"{ang_b}°",
        "sample_answer": f"{ang_b}° [co-int ∠s, AD || BC]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State co-interior angles supplementary [co-int ∠s, AD || BC]", "marks": 1},
            {"desc": f"Calculate ∠B = {ang_b}°", "marks": 1},
        ],
        "hints": [
            "Consecutive interior angles in a parallelogram are co-interior between parallel sides and add to 180°.",
            f"Subtract angle A ({ang_a}°) from 180°.",
            f"Angle B is {ang_b}°.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Parallelogram: Opposite Sides Equal Algebra
# ----------------------------------------------------------------------
def arch_36_parallelogram_opposite_sides_equal_algebra(rng: random.Random) -> Dict[str, Any]:
    # AB = DC: 3x - a = x + b => 2x = a + b
    x_val = rng.randint(4, 10)
    a_val = rng.randint(3, 9)
    b_val = 2 * x_val - a_val
    side_len = x_val + b_val

    prompt = (
        f"In parallelogram \\(ABCD\\), opposite sides are given as \\(AB = 3x - {a_val}\\text{{ cm}}\\) "
        f"and \\(DC = x + {b_val}\\text{{ cm}}\\). "
        f"Solve for \\(x\\) and hence calculate the length of side \\(AB\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AB = DC \\quad [\\text{{opposite sides of a parallelogram are equal}}] \\]\n"
        f"\\[ 3x - {a_val} = x + {b_val} \\]\n"
        f"\\[ 2x = {a_val + b_val} \\]\n"
        f"\\[ x = {x_val} \\]\n\n"
        f"**Side Length:**\n"
        f"\\[ AB = 3({x_val}) - {a_val} = {side_len}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_parm_sides_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{side_len} cm",
        "expected_answer": f"{side_len} cm",
        "sample_answer": f"x = {x_val}, AB = {side_len} cm [opp sides of parm]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Equate opposite sides [opp sides of parm]", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
            {"desc": f"Calculate length AB = {side_len} cm", "marks": 1},
        ],
        "hints": [
            "Opposite sides of a parallelogram are equal in length.",
            f"Solve 3x - {a_val} = x + {b_val}.",
            f"Substitute x = {x_val} to find AB = {side_len} cm.",
        ],
    }


# ----------------------------------------------------------------------
# 37. Parallelogram: Diagonals Bisect Each Other (with SVG diagram)
# ----------------------------------------------------------------------
def arch_37_parallelogram_diagonals_bisect_each_other(rng: random.Random) -> Dict[str, Any]:
    # Diagonals AC and BD intersect at M. AM = MC = a, BM = MD = b
    half_ac = rng.randint(4, 9)
    tot_ac = 2 * half_ac
    half_bd = rng.randint(5, 11)
    tot_bd = 2 * half_bd

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="parallelogram",
        labels=("A", "B", "C", "D"),
        show_diagonals=True,
        extra_text=f"Diagonals intersect at M; AM = {half_ac} cm, MD = {half_bd} cm",
        seed=seed_val,
    )

    prompt = (
        f"In parallelogram \\(ABCD\\) shown in the diagram below, diagonals \\(AC\\) and \\(BD\\) intersect at \\(M\\). "
        f"If \\(AM = {half_ac}\\text{{ cm}}\\) and \\(MD = {half_bd}\\text{{ cm}}\\), "
        f"determine the total lengths of diagonals \\(AC\\) and \\(BD\\). State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The diagonals of a parallelogram bisect each other \\([\\text{{diags of parm}}]\\).\n\n"
        f"1. \\(AC = 2 \\times AM = 2 \\times {half_ac}\\text{{ cm}} = {tot_ac}\\text{{ cm}}\\) \\quad [\\text{{diags of parm}}]\n"
        f"2. \\(BD = 2 \\times MD = 2 \\times {half_bd}\\text{{ cm}} = {tot_bd}\\text{{ cm}}\\) \\quad [\\text{{diags of parm}}]"
    )
    return {
        "id": f"g9_geom_parm_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"AC = {tot_ac} cm, BD = {tot_bd} cm",
        "expected_answer": f"AC = {tot_ac} cm, BD = {tot_bd} cm",
        "sample_answer": f"AC = {tot_ac} cm, BD = {tot_bd} cm [diags of parm]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply property that diagonals bisect each other [diags of parm]", "marks": 1},
            {"desc": f"State AC = {tot_ac} cm and BD = {tot_bd} cm", "marks": 1},
        ],
        "hints": [
            "The intersection point M is the exact midpoint of both diagonals.",
            f"Double AM ({half_ac} cm) to get diagonal AC ({tot_ac} cm).",
            f"Double MD ({half_bd} cm) to get diagonal BD ({tot_bd} cm).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 38. Rectangle Properties: Right Angles and Diagonals (with SVG diagram)
# ----------------------------------------------------------------------
def arch_38_rectangle_properties_right_angles_and_diagonals(rng: random.Random) -> Dict[str, Any]:
    # Diagonal length equation: 2x + a = x + b => x = b - a
    x_val = rng.randint(4, 10)
    a_val = rng.randint(2, 6)
    b_val = x_val + a_val
    diag_len = 2 * x_val + a_val

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="rectangle",
        labels=("A", "B", "C", "D"),
        show_diagonals=True,
        extra_text="Rectangle ABCD with diagonals AC and BD",
        seed=seed_val,
    )

    prompt = (
        f"In rectangle \\(ABCD\\) shown in the diagram below, diagonal \\(AC = 2x + {a_val}\\text{{ cm}}\\) "
        f"and diagonal \\(BD = x + {b_val}\\text{{ cm}}\\). "
        f"Solve for \\(x\\) and hence calculate the length of diagonal \\(AC\\). State the geometric property."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AC = BD \\quad [\\text{{diagonals of a rectangle are equal in length}}] \\]\n"
        f"\\[ 2x + {a_val} = x + {b_val} \\]\n"
        f"\\[ x = {b_val} - {a_val} = {x_val} \\]\n\n"
        f"**Diagonal Length:**\n"
        f"\\[ AC = 2({x_val}) + {a_val} = {diag_len}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_rect_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{diag_len} cm",
        "expected_answer": f"{diag_len} cm",
        "sample_answer": f"x = {x_val}, AC = {diag_len} cm [diags of rect equal]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Equate diagonals AC = BD [diags of rect equal]", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
            {"desc": f"Calculate diagonal length = {diag_len} cm", "marks": 1},
        ],
        "hints": [
            "In any rectangle, the diagonals are equal in length.",
            f"Set up equation: 2x + {a_val} = x + {b_val}.",
            f"Substitute x = {x_val} to get diagonal length ({diag_len} cm).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 39. Rhombus: Perpendicular Diagonals Calculation (with SVG diagram)
# ----------------------------------------------------------------------
def arch_39_rhombus_perpendicular_diagonals_calculation(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([25, 30, 35, 40, 45, 50, 55])
    # Right triangle formed by diagonals: 90 + ang1 + ang2 = 180 => ang2 = 90 - ang1
    ang2 = 90 - ang1

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="rhombus",
        labels=("A", "B", "C", "D"),
        show_diagonals=True,
        extra_text="Rhombus ABCD with diagonals intersecting perpendicularly at M",
        seed=seed_val,
    )

    prompt = (
        f"In rhombus \\(ABCD\\) shown in the diagram below, diagonals \\(AC\\) and \\(BD\\) intersect at point \\(M\\). "
        f"If \\(A\\hat{{B}}M = {ang1}^\\circ\\), determine the size of angle \\(B\\hat{{A}}M\\). State all geometric reasons."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ A\\hat{{M}}B = 90^\\circ \\quad [\\text{{diagonals of a rhombus intersect perpendicularly}}] \\]\n"
        f"**In \\(\\triangle ABM\\):**\n"
        f"\\[ B\\hat{{A}}M + A\\hat{{B}}M + A\\hat{{M}}B = 180^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n"
        f"\\[ B\\hat{{A}}M + {ang1}^\\circ + 90^\\circ = 180^\\circ \\]\n"
        f"\\[ B\\hat{{A}}M = 180^\\circ - 90^\\circ - {ang1}^\\circ = {ang2}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_rhomb_perp_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ang2}°",
        "expected_answer": f"{ang2}°",
        "sample_answer": f"{ang2}° [diags of rhombus ⊥; sum of ∠s in △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "State AMB = 90° [diags of rhombus ⊥]", "marks": 1},
            {"desc": "Apply sum of angles in △ABM = 180°", "marks": 1},
            {"desc": f"Calculate BAM = {ang2}°", "marks": 1},
        ],
        "hints": [
            "The diagonals of a rhombus intersect at right angles (90°).",
            f"In right triangle ABM, the acute angles sum to 90°.",
            f"Subtract {ang1}° from 90° to find angle BAM ({ang2}°).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 40. Rhombus: Diagonals Bisect Corner Angles
# ----------------------------------------------------------------------
def arch_40_rhombus_diagonals_bisect_corner_angles(rng: random.Random) -> Dict[str, Any]:
    corner_ang = rng.choice([64, 72, 80, 100, 112, 120])
    half_ang = corner_ang // 2

    prompt = (
        f"In rhombus \\(PQRS\\), the interior angle \\(\\hat{{P}} = {corner_ang}^\\circ\\). "
        f"Diagonal \\(PR\\) is drawn. Calculate the size of angle \\(Q\\hat{{P}}R\\). State the geometric property."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The diagonals of a rhombus bisect the corner angles \\([\\text{{diagonals of rhombus bisect corner }}\\angle\\text{{s}}]\\).\n\n"
        f"\\[ Q\\hat{{P}}R = \\frac{{1}}{{2}} \\times \\hat{{P}} = \\frac{{1}}{{2}} \\times {corner_ang}^\\circ = {half_ang}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_rhomb_bisect_ang_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{half_ang}°",
        "expected_answer": f"{half_ang}°",
        "sample_answer": f"{half_ang}° [diags of rhombus bisect corner ∠s]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply property that diagonals bisect corner angles in a rhombus", "marks": 1},
            {"desc": f"Calculate half angle = {half_ang}°", "marks": 1},
        ],
        "hints": [
            "A diagonal in a rhombus splits the vertex angle exactly in half.",
            f"Divide {corner_ang}° by 2.",
            f"Result: {half_ang}°.",
        ],
    }


# ----------------------------------------------------------------------
# 41. Square: Combined Properties Calculation (with SVG diagram)
# ----------------------------------------------------------------------
def arch_41_square_combined_properties_calculation(rng: random.Random) -> Dict[str, Any]:
    side_len = rng.randint(5, 14)
    perim = 4 * side_len

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="square",
        labels=("A", "B", "C", "D"),
        show_diagonals=True,
        extra_text=f"Square ABCD, side = {side_len} cm",
        seed=seed_val,
    )

    prompt = (
        f"In square \\(ABCD\\) shown in the diagram below, side length \\(AB = {side_len}\\text{{ cm}}\\) "
        f"and diagonals intersect at \\(M\\). "
        f"State the size of angle \\(A\\hat{{M}}B\\) and calculate the perimeter of square \\(ABCD\\)."
    )
    sol = (
        f"**Step 1: Angle at intersection of diagonals.**\n"
        f"\\[ A\\hat{{M}}B = 90^\\circ \\quad [\\text{{diagonals of a square are perpendicular bisectors}}] \\]\n\n"
        f"**Step 2: Perimeter calculation.**\n"
        f"All 4 sides of a square are equal \\([\\text{{all sides of square equal}}]\\):\n"
        f"\\[ \\text{{Perimeter}} = 4 \\times {side_len}\\text{{ cm}} = {perim}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_square_comb_{rng.randint(100000, 999999)}",
        "question_type": "compound_answer",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"AMB = 90°, Perimeter = {perim} cm",
        "expected_answer": f"AMB = 90°, Perimeter = {perim} cm",
        "sample_answer": f"90° and {perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify AMB = 90° [diags of square ⊥]", "marks": 1},
            {"desc": f"Calculate perimeter = {perim} cm", "marks": 1},
        ],
        "hints": [
            "The diagonals of a square are perpendicular bisectors (90°).",
            f"Multiply the side length {side_len} cm by 4 to get perimeter ({perim} cm).",
            f"Answers: 90° and {perim} cm.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Trapezium: Co-Interior Angles Parallel Sides (with SVG diagram)
# ----------------------------------------------------------------------
def arch_42_trapezium_cointerior_angles_parallel_sides(rng: random.Random) -> Dict[str, Any]:
    ang_d = rng.choice([60, 65, 70, 75, 80])
    ang_a = 180 - ang_d

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="trapezium",
        labels=("A", "B", "C", "D"),
        extra_text=f"Trapezium ABCD with AB || DC, D = {ang_d}°",
        seed=seed_val,
    )

    prompt = (
        f"In trapezium \\(ABCD\\) shown in the diagram below, \\(AB \\parallel DC\\). "
        f"If \\(\\hat{{D}} = {ang_d}^\\circ\\), calculate the size of interior angle \\(\\hat{{A}}\\). State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{A}} + \\hat{{D}} = 180^\\circ \\quad [\\text{{co-interior }}\\angle\\text{{s, }} AB \\parallel DC] \\]\n"
        f"\\[ \\hat{{A}} = 180^\\circ - {ang_d}^\\circ = {ang_a}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_trap_coint_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ang_a}°",
        "expected_answer": f"{ang_a}°",
        "sample_answer": f"{ang_a}° [co-int ∠s, AB || DC]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply co-interior angles supplementary [co-int ∠s, AB || DC]", "marks": 1},
            {"desc": f"Calculate ∠A = {ang_a}°", "marks": 1},
        ],
        "hints": [
            "In a trapezium, angles on the non-parallel sides between parallel lines are co-interior.",
            f"Co-interior angles add to 180°: 180° - {ang_d}°.",
            f"Angle A is {ang_a}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 43. Isosceles Trapezium: Base Angles Equal
# ----------------------------------------------------------------------
def arch_43_isosceles_trapezium_base_angles_equal(rng: random.Random) -> Dict[str, Any]:
    base_ang = rng.choice([55, 60, 65, 70, 75])
    top_ang = 180 - base_ang

    prompt = (
        f"Trapezium \\(ABCD\\) is an isosceles trapezium with \\(AB \\parallel DC\\) and non-parallel sides \\(AD = BC\\). "
        f"If base angle \\(\\hat{{D}} = {base_ang}^\\circ\\), determine the size of angle \\(\\hat{{C}}\\) "
        f"and angle \\(\\hat{{A}}\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"1. \\(\\hat{{C}} = \\hat{{D}} = {base_ang}^\\circ\\) \\quad [\\text{{base }}\\angle\\text{{s of isosceles trapezium equal}}]\n"
        f"2. \\(\\hat{{A}} + \\hat{{D}} = 180^\\circ \\quad [\\text{{co-interior }}\\angle\\text{{s, }} AB \\parallel DC]\\)\n"
        f"\\[ \\hat{{A}} = 180^\\circ - {base_ang}^\\circ = {top_ang}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_iso_trap_{rng.randint(100000, 999999)}",
        "question_type": "compound_answer",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"C = {base_ang}°, A = {top_ang}°",
        "expected_answer": f"C = {base_ang}°, A = {top_ang}°",
        "sample_answer": f"{base_ang}° and {top_ang}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State base angle C = {base_ang}° [base ∠s of isosceles trap]", "marks": 1},
            {"desc": f"Calculate angle A = {top_ang}° [co-int ∠s]", "marks": 1},
        ],
        "hints": [
            "In an isosceles trapezium, the two bottom base angles are equal.",
            "Angles along the slanted side add to 180° (co-interior).",
            f"Angles: C = {base_ang}°, A = {top_ang}°.",
        ],
    }


# ----------------------------------------------------------------------
# 44. Kite Properties: Axis of Symmetry and Angles (with SVG diagram)
# ----------------------------------------------------------------------
def arch_44_kite_properties_axis_of_symmetry_and_angles(rng: random.Random) -> Dict[str, Any]:
    ang_top = rng.choice([60, 70, 80, 90])
    ang_bot = rng.choice([30, 40, 50])
    # The two non-vertex opposite angles are equal: (360 - ang_top - ang_bot) / 2
    rem = 360 - (ang_top + ang_bot)
    side_ang = rem // 2

    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg(
        quad_type="kite",
        labels=("A", "B", "C", "D"),
        show_diagonals=True,
        extra_text=f"Kite ABCD (AB = AD, BC = DC), A = {ang_top}°, C = {ang_bot}°",
        seed=seed_val,
    )

    prompt = (
        f"In kite \\(ABCD\\) shown in the diagram below, \\(AB = AD\\) and \\(BC = DC\\). "
        f"Interior angles \\(\\hat{{A}} = {ang_top}^\\circ\\) and \\(\\hat{{C}} = {ang_bot}^\\circ\\). "
        f"Calculate the size of angle \\(\\hat{{B}}\\). State all geometric reasons."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{B}} = \\hat{{D}} \\quad [\\text{{one pair of opp }}\\angle\\text{{s equal in a kite}}] \\]\n"
        f"\\[ \\hat{{A}} + \\hat{{B}} + \\hat{{C}} + \\hat{{D}} = 360^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in quad}}] \\]\n"
        f"\\[ {ang_top}^\\circ + 2\\hat{{B}} + {ang_bot}^\\circ = 360^\\circ \\]\n"
        f"\\[ 2\\hat{{B}} = 360^\\circ - ({ang_top}^\\circ + {ang_bot}^\\circ) = {rem}^\\circ \\]\n"
        f"\\[ \\hat{{B}} = {side_ang}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_kite_ang_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{side_ang}°",
        "expected_answer": f"{side_ang}°",
        "sample_answer": f"{side_ang}° [opp ∠s of kite equal; sum of ∠s in quad]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Recognize ∠B = ∠D in a kite", "marks": 1},
            {"desc": "Apply sum of angles in quadrilateral = 360°", "marks": 1},
            {"desc": f"Calculate ∠B = {side_ang}°", "marks": 1},
        ],
        "hints": [
            "In a kite, the two angles between the unequal sides are equal in measure (angle B = angle D).",
            f"Add the other two angles: {ang_top}° + {ang_bot}° = {ang_top + ang_bot}°.",
            f"Subtract from 360° and divide by 2: {rem}° ÷ 2 = {side_ang}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 45. Prove Quadrilateral is Parallelogram Conditions
# ----------------------------------------------------------------------
def arch_45_prove_quadrilateral_is_parallelogram_conditions(rng: random.Random) -> Dict[str, Any]:
    valid_conditions = [
        ("Both pairs of opposite sides are parallel.", True),
        ("Both pairs of opposite sides are equal in length.", True),
        ("Both pairs of opposite angles are equal.", True),
        ("The diagonals bisect each other.", True),
        ("One pair of opposite sides is both equal in length and parallel.", True),
        ("The diagonals are perpendicular.", False),  # True for rhombus/kite, not any parm
        ("All four sides are equal.", False),  # Proves rhombus
        ("One pair of opposite sides is parallel, and the other pair is equal.", False),  # Can be isosceles trapezium
    ]
    statement, is_valid = rng.choice(valid_conditions)
    ans = "Yes" if is_valid else "No"

    prompt = (
        f"A learner states the following condition to prove that a quadrilateral is a parallelogram:\n"
        f"\\(\"\\text{{{statement}}}\"\\)\n"
        f"Does this condition alone conclusively prove that the quadrilateral is a parallelogram? Answer 'Yes' or 'No', and justify your answer."
    )
    if is_valid:
        sol_text = f"Yes, '{statement}' is one of the five sufficient Euclidean conditions to prove a quadrilateral is a parallelogram."
    else:
        sol_text = f"No, '{statement}' does not conclusively prove a parallelogram alone (for example, a trapezium or kite could satisfy this without being a parallelogram)."

    sol = f"**Evaluation:**\n{sol_text}\n\n**Answer:** **{ans}**"

    return {
        "id": f"g9_geom_prove_parm_{rng.randint(100000, 999999)}",
        "question_type": "boolean_choice",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans}. {sol_text}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct evaluation ({ans})", "marks": 1},
            {"desc": "Provide geometric reason based on parallelogram minimum conditions", "marks": 1},
        ],
        "hints": [
            "Recall the 5 sufficient conditions for proving a quadrilateral is a parallelogram.",
            "Both pairs of opposite sides parallel, or both pairs equal, or both pairs opp angles equal, or diags bisect, or 1 pair equal AND parallel.",
            f"Answer: {ans}.",
        ],
    }



# ----------------------------------------------------------------------
# 46. Regular Polygon Interior Angle Sum (with SVG diagram)
# ----------------------------------------------------------------------
def arch_46_regular_polygon_interior_angle_sum(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 10, 12])
    names_map = {5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 10: "decagon", 12: "dodecagon"}
    p_name = names_map[n]
    angle_sum = (n - 2) * 180

    seed_val = rng.randint(1000, 999999)
    svg = draw_regular_polygon_svg(num_sides=n, seed=seed_val)

    prompt = (
        f"A regular {p_name} has {n} equal sides and {n} equal interior angles, "
        f"as shown in the diagram below. Calculate the sum of all its interior angles in degrees."
    )
    sol = (
        f"**Interior Angle Sum Formula:**\n"
        f"\\[ \\text{{Sum of interior angles}} = (n - 2) \\times 180^\\circ \\]\n\n"
        f"For a regular {p_name} with \\(n = {n}\\):\n"
        f"\\[ \\text{{Sum}} = ({n} - 2) \\times 180^\\circ = {n - 2} \\times 180^\\circ = {angle_sum}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_poly_sum_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{angle_sum}°",
        "expected_answer": f"{angle_sum}°",
        "sample_answer": f"{angle_sum}° [(n-2) × 180°]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula (n - 2) × 180° with n = {n}", "marks": 1},
            {"desc": f"Calculate sum = {angle_sum}°", "marks": 1},
        ],
        "hints": [
            "Use the formula for the sum of interior angles of an n-sided polygon: (n - 2) × 180°.",
            f"Subtract 2 from {n}: {n} - 2 = {n - 2}.",
            f"Multiply by 180°: {n - 2} × 180° = {angle_sum}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Regular Polygon Size of Each Interior Angle
# ----------------------------------------------------------------------
def arch_47_regular_polygon_size_of_each_interior_angle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 8, 9, 10, 12])
    names_map = {5: "pentagon", 6: "hexagon", 8: "octagon", 9: "nonagon", 10: "decagon", 12: "dodecagon"}
    p_name = names_map[n]
    angle_sum = (n - 2) * 180
    each_angle = angle_sum // n

    prompt = (
        f"Calculate the size of **each** interior angle of a regular {p_name} ({n} equal sides) in degrees."
    )
    sol = (
        f"**Step 1: Calculate total sum of interior angles.**\n"
        f"\\[ \\text{{Sum}} = (n - 2) \\times 180^\\circ = ({n} - 2) \\times 180^\\circ = {angle_sum}^\\circ \\]\n\n"
        f"**Step 2: Divide equally among {n} angles.**\n"
        f"\\[ \\text{{Each interior angle}} = \\frac{{{angle_sum}^\\circ}}{{{n}}} = {each_angle}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_poly_int_each_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{each_angle}°",
        "expected_answer": f"{each_angle}°",
        "sample_answer": f"{each_angle}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Find total sum = {angle_sum}°", "marks": 1},
            {"desc": f"Divide by {n} to obtain {each_angle}°", "marks": 1},
        ],
        "hints": [
            f"Calculate the total interior angle sum: ({n} - 2) × 180° = {angle_sum}°.",
            f"Divide by {n} because all angles in a regular polygon are equal.",
            f"Each interior angle is {each_angle}°.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Regular Polygon Size of Each Exterior Angle
# ----------------------------------------------------------------------
def arch_48_regular_polygon_size_of_each_exterior_angle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 8, 9, 10, 12])
    names_map = {5: "pentagon", 6: "hexagon", 8: "octagon", 9: "nonagon", 10: "decagon", 12: "dodecagon"}
    p_name = names_map[n]
    ext_angle = 360 // n

    prompt = (
        f"Calculate the size of **each** exterior angle of a regular {p_name} ({n} equal sides) in degrees."
    )
    sol = (
        f"**Exterior Angle Theorem for Polygons:**\n"
        f"The sum of all exterior angles of any convex polygon is always \\(360^\\circ\\).\n\n"
        f"For a regular polygon with \\(n = {n}\\):\n"
        f"\\[ \\text{{Each exterior angle}} = \\frac{{360^\\circ}}{{n}} = \\frac{{360^\\circ}}{{{n}}} = {ext_angle}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_poly_ext_each_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ext_angle}°",
        "expected_answer": f"{ext_angle}°",
        "sample_answer": f"{ext_angle}° [360° / n]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply exterior angle sum theorem (360° / n)", "marks": 1},
            {"desc": f"Calculate each exterior angle = {ext_angle}°", "marks": 1},
        ],
        "hints": [
            "The sum of exterior angles of any polygon is always 360°.",
            f"Divide 360° by {n}.",
            f"Each exterior angle is {ext_angle}°.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnose Geometric Congruency Error
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnose_geometric_congruency_error(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Thabo", "Sipho", "Zola", "Buhle", "Lerato", "Kagiso", "Nomsa", "Andile"])
    scenarios = [
        (
            f"{name} wrote the following conclusion in a geometry test:\n"
            f"'In \\(\\triangle ABC\\) and \\(\\triangle DEF\\), \\(\\hat{{A}} = \\hat{{D}}\\), "
            f"\\(\\hat{{B}} = \\hat{{E}}\\), and \\(\\hat{{C}} = \\hat{{F}}\\). "
            f"Therefore, \\(\\triangle ABC \\equiv \\triangle DEF\\) [AAA].'\n"
            f"Identify the mathematical misconception in {name}'s reasoning, and state the correct relationship.",
            f"**Misconception Analysis:**\n"
            f"AAA (Angle-Angle-Angle) proves **similarity** (\\(\\triangle ABC \\;///\\; \\triangle DEF\\)), "
            f"not **congruency** (\\(\\triangle ABC \\equiv \\triangle DEF\\)).\n\n"
            f"Equiangular triangles have the exact same shape, but their side lengths may be enlarged or reduced by a scale factor. "
            f"To establish congruency, at least one pair of corresponding side lengths must be proven equal.",
            "AAA proves similarity (///), not congruency (≡). At least one side must be equal to prove congruency.",
            "AAA proves similarity (same shape), not congruency (same size and shape).",
            [
                {"desc": "Identify that AAA proves similarity (///), not congruency (≡)", "marks": 1},
                {"desc": "Explain that side lengths may differ without at least one equal side", "marks": 1},
            ],
            [
                "Think about whether two triangles with the same angles must have the exact same size.",
                "AAA guarantees same shape (similar), but not same size (congruent).",
                "At least one pair of sides must be equal for congruency.",
            ],
        ),
        (
            f"{name} concluded that \\(\\triangle PQR \\equiv \\triangle XYZ\\) because two pairs of sides are equal "
            f"(\\(PQ = XY\\) and \\(QR = YZ\\)) and \\(\\hat{{P}} = \\hat{{X}}\\) (SSA).\n"
            f"Identify the mathematical error in {name}'s reasoning and explain why SSA cannot prove congruency.",
            f"**Misconception Analysis:**\n"
            f"SSA (two sides and a non-included angle) is not a valid congruency condition because it is ambiguous (the 'ambiguous case'). "
            f"The non-included side can swing to create two different non-congruent triangles (one acute, one obtuse). "
            f"To guarantee congruency, the angle must be the **included angle** (SAS), or a right angle (RHS).",
            "SSA is not a valid condition (ambiguous case). The equal angle must be included between the two sides (SAS).",
            "SSA is ambiguous and can produce two different triangles unless the angle is 90° (RHS).",
            [
                {"desc": "Identify SSA as non-valid / ambiguous case", "marks": 1},
                {"desc": "State that the angle must be the included angle (SAS) or right angle (RHS)", "marks": 1},
            ],
            [
                "Check whether the equal angle is between the two equal sides.",
                "SSA is the ambiguous case and does not guarantee a unique triangle.",
                "The angle must be included (SAS).",
            ],
        ),
        (
            f"{name} stated: 'Every parallelogram has diagonals of equal length, so if \\(ABCD\\) is a parallelogram, \\(AC = BD\\).'\n"
            f"Identify {name}'s misconception and specify which special quadrilaterals have equal diagonals.",
            f"**Misconception Analysis:**\n"
            f"In a general parallelogram, diagonals bisect each other, but they are generally **not equal in length** (one diagonal is longer than the other). "
            f"Diagonals are equal in length only in special parallelograms: namely, **rectangles** and **squares** (or isosceles trapeziums).",
            "Diagonals of a general parallelogram are not equal in length; they are equal only in rectangles and squares.",
            "Diagonals bisect each other in a parallelogram, but are only equal in rectangles and squares.",
            [
                {"desc": "State that diagonals are not equal in a general parallelogram", "marks": 1},
                {"desc": "Identify rectangles and squares as having equal diagonals", "marks": 1},
            ],
            [
                "Recall whether a slanted parallelogram has equal diagonals.",
                "Diagonals bisect each other, but are unequal unless all angles are 90°.",
                "Rectangles and squares have equal diagonals.",
            ],
        ),
    ]
    prompt, sol, cor_ans, exp_ans, schema, hints = rng.choice(scenarios)

    return {
        "id": f"g9_geom_err_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": cor_ans,
        "expected_answer": exp_ans,
        "sample_answer": cor_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": schema,
        "hints": hints,
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Geometry 2D Synthesis
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_geometry_2d_synthesis(rng: random.Random) -> Dict[str, Any]:
    # In quadrilateral ABCD, AB || DC and AD = BC (isosceles trapezium).
    # Triangle ABD is formed by diagonal BD.
    # Given angle D = 70°, find angle A, angle C, and angle BDC.
    choices = [
        (65, 115, 65, 50),
        (70, 110, 70, 40),
        (75, 105, 75, 30),
        (60, 120, 60, 60),
        (80, 100, 80, 20),
    ]
    base_d, top_a, base_c, diff = rng.choice(choices)

    prompt = (
        f"In quadrilateral \\(ABCD\\), \\(AB \\parallel DC\\) and \\(AD = BC\\) (an isosceles trapezium). "
        f"The interior angle \\(\\hat{{D}} = {base_d}^\\circ\\). "
        f"Calculate the size of interior angle \\(\\hat{{A}}\\) and interior angle \\(\\hat{{C}}\\). "
        f"Provide full geometric statements and reasons."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"1. \\(\\hat{{A}} + \\hat{{D}} = 180^\\circ \\quad [\\text{{co-interior }}\\angle\\text{{s, }} AB \\parallel DC]\\)\n"
        f"\\[ \\hat{{A}} = 180^\\circ - {base_d}^\\circ = {top_a}^\\circ \\]\n\n"
        f"2. \\(\\hat{{C}} = \\hat{{D}} = {base_c}^\\circ \\quad [\\text{{base }}\\angle\\text{{s of isosceles trapezium equal, }} AD = BC]\n"
        f"Therefore, \\(\\hat{{A}} = {top_a}^\\circ\\) and \\(\\hat{{C}} = {base_c}^\\circ\\)."
    )
    return {
        "id": f"g9_geom_synth_mult_{rng.randint(100000, 999999)}",
        "question_type": "compound_answer",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"A = {top_a}°, C = {base_c}°",
        "expected_answer": f"A = {top_a}°, C = {base_c}°",
        "sample_answer": f"A = {top_a}°, C = {base_c}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate angle A = {top_a}° [co-int ∠s, AB || DC]", "marks": 1},
            {"desc": f"State angle C = {base_c}° [base ∠s of isosceles trapezium]", "marks": 1},
            {"desc": "Provide correct geometric reasons for both deductions", "marks": 1},
        ],
        "hints": [
            "Use co-interior angles between parallel lines AB and DC to find angle A.",
            "Use the property that base angles of an isosceles trapezium are equal to find angle C.",
            f"Answers: A = {top_a}°, C = {base_c}°.",
        ],
    }
