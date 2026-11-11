"""Grade 8 Mathematics - Geometry of 2D Shapes Archetypes (26 to 50).
Covers:
  - Circles: Radius, diameter, chord, tangent, sector, segment.
  - Congruence and Similarity: Conditions (SSS, SAS, AAS, RHS, AAA), scale factor calculations.
  - Polygons: Convex/concave, interior/exterior angle formulas for regular and irregular polygons.
  - Multi-step composite geometric proofs and angle deduction.
Strictly zero-LLM, deterministic execution parameterized by random.Random.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .geometry_2d_shapes_svg import (
    draw_circle_svg,
    draw_quadrilateral_svg,
    draw_regular_polygon_svg,
    draw_similar_triangles_svg,
    draw_triangle_svg,
)


# ----------------------------------------------------------------------
# 26. Circle Parts Identification Radius Diameter Chord (WITH SVG)
# ----------------------------------------------------------------------
def arch_26_circle_parts_identification_radius_diameter_chord(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["radius", "diameter", "chord"])
    svg = draw_circle_svg(highlight=choice, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given circle with centre \\(O\\), a line segment is highlighted.\n\n"
        f"1. Name the highlighted geometric feature (radius, diameter, or chord).\n"
        f"2. Define this feature in words relative to the centre and circumference."
    )
    if choice == "radius":
        def_txt = "A line segment from the centre to any point on the circumference."
        ans = "1. Radius; 2. Line segment from centre to circumference"
    elif choice == "diameter":
        def_txt = "A straight line segment passing through the centre connecting two points on the circumference."
        ans = "1. Diameter; 2. Straight line segment passing through centre connecting two points on circumference"
    else:
        def_txt = "A line segment connecting any two points on the circumference without necessarily passing through the centre."
        ans = "1. Chord; 2. Line segment connecting two points on the circumference"

    sol = f"**1. Feature:** {choice.capitalize()}.\n\n**2. Definition:** {def_txt}"
    return {
        "id": f"g8_circ_parts_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_circle_parts_identification_radius_diameter_chord",
        "learning_objective_id": "math_g8_circ_parts",
        "hints": {
            "tier_1": "Recall: radius goes from center to edge, diameter goes edge-to-edge through center.",
            "tier_2": f"Inspect the highlighted line in the circle ({choice}).",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["confusing_chord_and_diameter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 27. Circle Radius Diameter Relationship Calculations (WITH SVG)
# ----------------------------------------------------------------------
def arch_27_circle_radius_diameter_relationship_calculations(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([3.5, 4.0, 7.5, 8.0, 11.0, 14.5])
    d = 2 * r
    svg = draw_circle_svg(radius_val=r, highlight="radius", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given circle with centre \\(O\\), the radius is \\(r = {r}\\) cm.\n\n"
        f"1. Write down the algebraic formula relating diameter \\(d\\) and radius \\(r\\).\n"
        f"2. Calculate the diameter \\(d\\) of this circle in cm.\n"
        f"3. If another concentric circle has diameter **{2 * d} cm**, what is its radius?"
    )
    sol = (
        f"**1. Formula:** \\(d = 2r\\) or \\(r = \\frac{{d}}{{2}}\\).\n\n"
        f"**2. Diameter:**\n"
        f"\\[ d = 2 \\times {r} = {d} \\text{{ cm}} \\]\n\n"
        f"**3. Concentric circle radius:**\n"
        f"\\[ r_2 = \\frac{{{2 * d}}}{{2}} = {d} \\text{{ cm}} \\]"
    )
    ans = f"1. d = 2r; 2. {d} cm; 3. {d} cm"
    return {
        "id": f"g8_circ_rd_calc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "27_circle_radius_diameter_relationship_calculations",
        "learning_objective_id": "math_g8_circ_rd_calc",
        "hints": {
            "tier_1": "Diameter is always double the radius.",
            "tier_2": f"2 × {r} = {d} cm.",
            "tier_3": f"Diameter = {d} cm; concentric radius = {d} cm.",
        },
        "misconception_tags": ["dividing_by_2_instead_of_multiplying_to_find_diameter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 28. Circle Tangent And Secant Definitions (WITH SVG)
# ----------------------------------------------------------------------
def arch_28_circle_tangent_and_secant_definitions(rng: random.Random) -> Dict[str, Any]:
    svg = draw_circle_svg(highlight="tangent", seed=rng.randint(100, 999999))

    prompt = (
        f"The given diagram displays a circle with centre \\(O\\) and a straight line touching the circumference.\n\n"
        f"1. What is the geometric name of a line that touches a circle at exactly one point?\n"
        f"2. What angle does this line make with the radius drawn to the point of contact?\n"
        f"3. Contrast this with a **secant line**."
    )
    sol = (
        f"**1. Geometric Name:** Tangent line.\n\n"
        f"**2. Angle with radius:** \\(90^\\circ\\) (right angle; \\(\\text{{radius }} \\perp \\text{{ tangent}}\\)).\n\n"
        f"**3. Contrast with secant:** A tangent touches the circle at exactly 1 point, whereas a secant line intersects the circle at 2 distinct points."
    )
    ans = "1. Tangent; 2. 90° (perpendicular); 3. tangent touches at 1 point, secant cuts through 2 points"
    return {
        "id": f"g8_circ_tangent_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "28_circle_tangent_and_secant_definitions",
        "learning_objective_id": "math_g8_circ_tangent",
        "hints": {
            "tier_1": "A line touching a circle at a single point is a tangent.",
            "tier_2": "The tangent is perpendicular to the radius at the point of contact.",
            "tier_3": "Tangent touches at 1 point at 90°; secant cuts across 2 points.",
        },
        "misconception_tags": ["confusing_tangent_with_chord"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 29. Circle Sector And Segment Identification (WITH SVG)
# ----------------------------------------------------------------------
def arch_29_circle_sector_and_segment_identification(rng: random.Random) -> Dict[str, Any]:
    svg = draw_circle_svg(highlight="sector", seed=rng.randint(100, 999999))

    prompt = (
        f"In geometry, regions of a circle are bounded by arcs and straight lines.\n\n"
        f"1. The highlighted slice in the given diagram is bounded by two radii and an arc. Name this region.\n"
        f"2. What is the region bounded by a chord and an arc called?\n"
        f"3. State the difference between a **minor arc** and a **major arc**."
    )
    sol = (
        f"**1. Region bounded by 2 radii and an arc:** Sector (like a slice of pizza).\n\n"
        f"**2. Region bounded by a chord and an arc:** Segment.\n\n"
        f"**3. Minor vs major arc:** A minor arc is less than a semicircle (less than \\(180^\\circ\\)), "
        f"whereas a major arc is greater than a semicircle (greater than \\(180^\\circ\\))."
    )
    ans = "1. Sector; 2. Segment; 3. minor arc < 180° / semicircle, major arc > 180° / semicircle"
    return {
        "id": f"g8_circ_sect_seg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "29_circle_sector_and_segment_identification",
        "learning_objective_id": "math_g8_circ_sect_seg",
        "hints": {
            "tier_1": "Sector is between two radii (pie slice); segment is cut by a chord.",
            "tier_2": "Minor arc is smaller than half a circle.",
            "tier_3": "1. Sector; 2. Segment; 3. Minor arc < semicircle, major arc > semicircle.",
        },
        "misconception_tags": ["confusing_sector_with_segment"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 30. Congruent Triangles Condition SSS (WITH SVG)
# ----------------------------------------------------------------------
def arch_30_congruent_triangles_condition_sss(rng: random.Random) -> Dict[str, Any]:
    s1, s2, s3 = rng.choice([(5, 6, 7), (6, 8, 10), (4, 7, 8)])
    lbls1 = {"base": f"{s1} cm", "left": f"{s2} cm", "right": f"{s3} cm"}
    lbls2 = {"base": f"{s1} cm", "left": f"{s2} cm", "right": f"{s3} cm"}

    svg = draw_similar_triangles_svg(
        scale=1.0,
        labels1=lbls1,
        labels2=lbls2,
        v1=("A", "B", "C"),
        v2=("D", "E", "F"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given figure, two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\) have matching side lengths:\n"
        f"\\(AB = DE = {s2}\\) cm, \\(BC = EF = {s1}\\) cm, and \\(AC = DF = {s3}\\) cm.\n\n"
        f"1. State whether \\(\\triangle ABC\\) and \\(\\triangle DEF\\) are congruent. (Answer 'Yes' or 'No')\n"
        f"2. Write down the congruency condition (reason).\n"
        f"3. Write the formal congruence statement: \\(\\triangle ABC \\equiv \\dots\\)"
    )
    sol = (
        f"**1. Congruency:** Yes, they are congruent.\n\n"
        f"**2. Condition:** SSS (Side-Side-Side).\n\n"
        f"**3. Congruence statement:** \\(\\triangle ABC \\equiv \\triangle DEF\\) (SSS)."
    )
    ans = "1. Yes; 2. SSS (Side-Side-Side); 3. triangle ABC = triangle DEF"
    return {
        "id": f"g8_cong_sss_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "30_congruent_triangles_condition_sss",
        "learning_objective_id": "math_g8_cong_sss",
        "hints": {
            "tier_1": "When all 3 pairs of corresponding sides are equal, triangles are congruent by SSS.",
            "tier_2": "Match corresponding vertices: A to D, B to E, C to F.",
            "tier_3": "Yes; SSS; triangle ABC = triangle DEF.",
        },
        "misconception_tags": ["writing_vertices_in_wrong_order_in_congruence_statement"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 31. Congruent Triangles Condition SAS (WITH SVG)
# ----------------------------------------------------------------------
def arch_31_congruent_triangles_condition_sas(rng: random.Random) -> Dict[str, Any]:
    s1, s2 = rng.choice([(6, 9), (7, 10), (8, 12)])
    inc_ang = rng.choice([40, 50, 60])

    lbls1 = {"base": f"{s1} cm", "left": f"{s2} cm"}
    lbls2 = {"base": f"{s1} cm", "left": f"{s2} cm"}
    svg = draw_similar_triangles_svg(
        scale=1.0,
        labels1=lbls1,
        labels2=lbls2,
        v1=("A", "B", "C"),
        v2=("D", "E", "F"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\), \\(AB = DE = {s2}\\) cm, "
        f"\\(BC = EF = {s1}\\) cm, and included angles \\(\\hat{{B}} = \\hat{{E}} = {inc_ang}^\\circ\\).\n\n"
        f"1. Explain what is meant by an **included angle**.\n"
        f"2. State the condition that proves \\(\\triangle ABC \\equiv \\triangle DEF\\)."
    )
    sol = (
        f"**1. Included angle:** The angle formed directly between the two given equal sides.\n\n"
        f"**2. Condition:** SAS (Side-Angle-Side; two sides and the included angle)."
    )
    ans = "1. angle formed between the two equal sides; 2. SAS (Side-Angle-Side)"
    return {
        "id": f"g8_cong_sas_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_congruent_triangles_condition_sas",
        "learning_objective_id": "math_g8_cong_sas",
        "hints": {
            "tier_1": "The angle must be between the two equal sides.",
            "tier_2": "The condition is SAS.",
            "tier_3": "Included angle is between the sides; condition is SAS.",
        },
        "misconception_tags": ["using_non_included_angle_as_sas"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Congruent Triangles Condition AAS (WITH SVG)
# ----------------------------------------------------------------------
def arch_32_congruent_triangles_condition_aas(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([40, 50, 60])
    a2 = rng.choice([60, 70, 80])
    s = rng.choice([5, 8, 12])

    lbls1 = {"base": f"{s} cm"}
    lbls2 = {"base": f"{s} cm"}
    svg = draw_similar_triangles_svg(
        scale=1.0,
        labels1=lbls1,
        labels2=lbls2,
        v1=("A", "B", "C"),
        v2=("D", "E", "F"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"Two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\) have "
        f"\\(\\hat{{A}} = \\hat{{D}} = {a1}^\\circ\\), \\(\\hat{{B}} = \\hat{{E}} = {a2}^\\circ\\), "
        f"and corresponding side \\(BC = EF = {s}\\) cm.\n\n"
        f"1. State the condition of congruency for these triangles.\n"
        f"2. Deduce the size of the remaining third angle \\(\\hat{{C}}\\)."
    )
    rem_ang = 180 - (a1 + a2)
    sol = (
        f"**1. Condition:** AAS or SAA (Angle-Angle-Side; two angles and a corresponding side).\n\n"
        f"**2. Third angle:**\n"
        f"\\[ \\hat{{C}} = 180^\\circ - ({a1}^\\circ + {a2}^\\circ) = {rem_ang}^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]"
    )
    ans = f"1. AAS (or SAA); 2. C = {rem_ang}°"
    return {
        "id": f"g8_cong_aas_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_congruent_triangles_condition_aas",
        "learning_objective_id": "math_g8_cong_aas",
        "hints": {
            "tier_1": "Two angles and a corresponding side equal means AAS.",
            "tier_2": f"Third angle is 180° - ({a1}° + {a2}°).",
            "tier_3": f"AAS; third angle = {rem_ang}°.",
        },
        "misconception_tags": ["confusing_aas_with_aaa"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 33. Congruent Triangles Condition RHS (WITH SVG)
# ----------------------------------------------------------------------
def arch_33_congruent_triangles_condition_rhs(rng: random.Random) -> Dict[str, Any]:
    hyp = rng.choice([10, 13, 17])
    side = rng.choice([6, 5, 8])

    lbls1 = {"base": f"{side} cm", "right": f"{hyp} cm"}
    lbls2 = {"base": f"{side} cm", "right": f"{hyp} cm"}
    svg = draw_similar_triangles_svg(
        scale=1.0,
        labels1=lbls1,
        labels2=lbls2,
        v1=("P", "Q", "R"),
        v2=("X", "Y", "Z"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In right-angled triangles \\(\\triangle PQR\\) and \\(\\triangle XYZ\\), \\(\\hat{{Q}} = \\hat{{Y}} = 90^\\circ\\).\n"
        f"The hypotenuses are equal: \\(PR = XZ = {hyp}\\) cm, and one leg \\(QR = YZ = {side}\\) cm.\n\n"
        f"1. State the condition of congruency for these triangles.\n"
        f"2. Explain what 'RHS' stands for in geometry."
    )
    sol = (
        f"**1. Condition:** RHS (Right-angle, Hypotenuse, Side).\n\n"
        f"**2. Explanation:**\n"
        f"- **R:** Right angle (\\(90^\\circ\\))\n"
        f"- **H:** Hypotenuse (the longest side opposite the right angle is equal)\n"
        f"- **S:** One other corresponding side (leg) is equal."
    )
    ans = "1. RHS; 2. Right-angle, Hypotenuse, Side"
    return {
        "id": f"g8_cong_rhs_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_congruent_triangles_condition_rhs",
        "learning_objective_id": "math_g8_cong_rhs",
        "hints": {
            "tier_1": "Right angle + hypotenuse + one side = RHS.",
            "tier_2": "Hypotenuse is the side opposite the 90° angle.",
            "tier_3": "Condition is RHS (Right-angle, Hypotenuse, Side).",
        },
        "misconception_tags": ["calling_rhs_sas_when_hypotenuse_is_involved"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 34. Congruent Triangles Deduce Corresponding Parts (WITH SVG)
# ----------------------------------------------------------------------
def arch_34_congruent_triangles_deduce_corresponding_parts(rng: random.Random) -> Dict[str, Any]:
    side_ab = rng.choice([7, 9, 11])
    ang_c = rng.choice([35, 45, 55])

    lbls1 = {"left": f"{side_ab} cm"}
    lbls2 = {"right": "x"}
    svg = draw_similar_triangles_svg(
        scale=1.0,
        labels1=lbls1,
        labels2=lbls2,
        v1=("A", "B", "C"),
        v2=("D", "E", "F"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"It is given that \\(\\triangle ABC \\equiv \\triangle DEF\\).\n"
        f"In \\(\\triangle ABC\\), \\(AB = {side_ab}\\) cm and \\(\\hat{{C}} = {ang_c}^\\circ\\).\n\n"
        f"1. What is the length of corresponding side \\(DE\\)?\n"
        f"2. What is the size of corresponding angle \\(\\hat{{F}}\\)?\n"
        f"3. State the principle used to determine these values."
    )
    sol = (
        f"**1. Side DE:** \\(DE = AB = {side_ab}\\) cm.\n\n"
        f"**2. Angle F:** \\(\\hat{{F}} = \\hat{{C}} = {ang_c}^\\circ\\).\n\n"
        f"**3. Principle:** Corresponding parts of congruent triangles are equal."
    )
    ans = f"1. DE = {side_ab} cm; 2. F = {ang_c}°; 3. corresponding parts of congruent triangles are equal"
    return {
        "id": f"g8_cong_parts_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "34_congruent_triangles_deduce_corresponding_parts",
        "learning_objective_id": "math_g8_cong_parts",
        "hints": {
            "tier_1": "Congruent means identical in shape and size.",
            "tier_2": "Corresponding letters match: AB matches DE, C matches F.",
            "tier_3": f"DE = {side_ab} cm, F = {ang_c}°.",
        },
        "misconception_tags": ["matching_wrong_vertices_in_congruence"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 35. Similar Triangles Condition Equiangular AAA (WITH SVG)
# ----------------------------------------------------------------------
def arch_35_similar_triangles_condition_equiangular_aaa(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([45, 50, 55])
    a2 = rng.choice([60, 65, 70])
    a3 = 180 - (a1 + a2)

    svg = draw_similar_triangles_svg(scale=1.4, seed=rng.randint(100, 999999))

    prompt = (
        f"Two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\) have interior angles:\n"
        f"\\(\\hat{{A}} = \\hat{{D}} = {a1}^\\circ\\), \\(\\hat{{B}} = \\hat{{E}} = {a2}^\\circ\\), and "
        f"\\(\\hat{{C}} = \\hat{{F}} = {a3}^\\circ\\).\n\n"
        f"1. State whether \\(\\triangle ABC\\) and \\(\\triangle DEF\\) are similar (\\(\\triangle ABC \\sim \\triangle DEF\\)).\n"
        f"2. State the condition for similarity.\n"
        f"3. Explain why having equal corresponding angles does NOT necessarily mean the triangles are congruent."
    )
    sol = (
        f"**1. Similarity:** Yes, \\(\\triangle ABC \\sim \\triangle DEF\\).\n\n"
        f"**2. Condition:** Equiangular (AAA).\n\n"
        f"**3. Why not congruent:** Similar triangles have the same shape, but one can be an enlargement or reduction of the other with different side lengths."
    )
    ans = "1. Yes; 2. AAA (equiangular); 3. same shape but can have different sizes / side lengths"
    return {
        "id": f"g8_sim_aaa_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "35_similar_triangles_condition_equiangular_aaa",
        "learning_objective_id": "math_g8_sim_aaa",
        "hints": {
            "tier_1": "Equal angles mean triangles are equiangular and therefore similar.",
            "tier_2": "AAA establishes similarity, not congruence.",
            "tier_3": "Yes; AAA; same shape but side lengths can differ.",
        },
        "misconception_tags": ["assuming_aaa_proves_congruence"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 36. Similar Triangles Proportional Sides Ratio (WITH SVG)
# ----------------------------------------------------------------------
def arch_36_similar_triangles_proportional_sides_ratio(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3])
    b1 = rng.choice([4, 5, 6])
    l1 = rng.choice([3, 4])
    r1 = rng.choice([6, 7])

    b2, l2, r2 = b1 * k, l1 * k, r1 * k

    lbls1 = {"base": f"{b1}", "left": f"{l1}", "right": f"{r1}"}
    lbls2 = {"base": f"{b2}", "left": f"{l2}", "right": f"{r2}"}
    svg = draw_similar_triangles_svg(scale=1.5, labels1=lbls1, labels2=lbls2, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given figure, \\(\\triangle ABC \\sim \\triangle DEF\\).\n"
        f"The side lengths of \\(\\triangle ABC\\) are \\(AB = {l1}\\), \\(BC = {b1}\\), and \\(AC = {r1}\\).\n"
        f"The side lengths of \\(\\triangle DEF\\) are \\(DE = {l2}\\), \\(EF = {b2}\\), and \\(DF = {r2}\\).\n\n"
        f"1. Write down the ratio of corresponding sides: \\(\\frac{{DE}}{{AB}}\\), \\(\\frac{{EF}}{{BC}}\\), and \\(\\frac{{DF}}{{AC}}\\).\n"
        f"2. Confirm that the ratio is constant and state the scale factor of enlargement."
    )
    sol = (
        f"**1. Ratios:**\n"
        f"\\[ \\frac{{DE}}{{AB}} = \\frac{{{l2}}}{{{l1}}} = {k} \\]\n"
        f"\\[ \\frac{{EF}}{{BC}} = \\frac{{{b2}}}{{{b1}}} = {k} \\]\n"
        f"\\[ \\frac{{DF}}{{AC}} = \\frac{{{r2}}}{{{r1}}} = {k} \\]\n\n"
        f"**2. Conclusion:** The ratios are all equal to **{k}**. The scale factor of enlargement is **{k}**."
    )
    ans = f"1. all ratios equal {k}; 2. constant scale factor = {k}"
    return {
        "id": f"g8_sim_prop_ratio_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "36_similar_triangles_proportional_sides_ratio",
        "learning_objective_id": "math_g8_sim_prop_ratio",
        "hints": {
            "tier_1": "Divide each side of the larger triangle by the corresponding side of the smaller triangle.",
            "tier_2": f"{l2} ÷ {l1} = {k}.",
            "tier_3": f"Scale factor is {k}.",
        },
        "misconception_tags": ["inverting_the_ratio_for_one_pair_of_sides"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 37. Similar Triangles Calculate Missing Side Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_37_similar_triangles_calculate_missing_side_length(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    ab = rng.choice([3, 4, 5])
    de = ab * k
    bc = rng.choice([5, 6, 8])
    ef = bc * k

    lbls1 = {"left": f"{ab} cm", "base": f"{bc} cm"}
    lbls2 = {"left": f"{de} cm", "base": "x"}
    svg = draw_similar_triangles_svg(scale=1.4, labels1=lbls1, labels2=lbls2, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given figure, \\(\\triangle ABC \\sim \\triangle DEF\\).\n"
        f"\\(AB = {ab}\\) cm, \\(BC = {bc}\\) cm, and \\(DE = {de}\\) cm.\n\n"
        f"1. Set up a proportion equation using corresponding sides.\n"
        f"2. Solve for \\(x = EF\\) in cm."
    )
    sol = (
        f"**Step 1: Set up proportion**\n"
        f"\\[ \\frac{{EF}}{{BC}} = \\frac{{DE}}{{AB}} \\quad (\\text{{sides in prop., }} \\triangle ABC \\sim \\triangle DEF) \\]\n"
        f"\\[ \\frac{{x}}{{{bc}}} = \\frac{{{de}}}{{{ab}}} \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ \\frac{{x}}{{{bc}}} = {k} \\implies x = {bc} \\times {k} = {ef} \\text{{ cm}} \\]"
    )
    ans = f"1. x/{bc} = {de}/{ab}; 2. x = {ef} cm"
    return {
        "id": f"g8_sim_calc_side_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "37_similar_triangles_calculate_missing_side_length",
        "learning_objective_id": "math_g8_sim_calc_side",
        "hints": {
            "tier_1": "In similar triangles, the ratio of corresponding sides is equal.",
            "tier_2": f"Find scale factor k = {de} / {ab} = {k}.",
            "tier_3": f"x = {bc} × {k} = {ef} cm.",
        },
        "misconception_tags": ["adding_scale_difference_instead_of_multiplying"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 38. Similar Triangles Scale Factor Enlargement Reduction (WITH SVG)
# ----------------------------------------------------------------------
def arch_38_similar_triangles_scale_factor_enlargement_reduction(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1.5, 2.0, 2.5, 3.0])
    orig = rng.choice([6, 8, 10])
    img = int(orig * k) if (orig * k).is_integer() else orig * k

    lbls1 = {"base": f"{orig} cm"}
    lbls2 = {"base": f"{img} cm"}
    svg = draw_similar_triangles_svg(scale=1.4, labels1=lbls1, labels2=lbls2, seed=rng.randint(100, 999999))

    prompt = (
        f"\\(\\triangle ABC\\) has base **{orig} cm** and is enlarged to similar triangle \\(\\triangle DEF\\) with base **{img} cm**.\n\n"
        f"1. Calculate the scale factor \\(k\\) of the enlargement.\n"
        f"2. If a side of \\(\\triangle ABC\\) is **4 cm**, what is the length of the corresponding side in \\(\\triangle DEF\\)?\n"
        f"3. What is the scale factor if \\(\\triangle DEF\\) is reduced back to \\(\\triangle ABC\\)?"
    )
    s2 = 4 * k
    s2_str = f"{int(s2)}" if isinstance(s2, float) and s2.is_integer() else f"{s2}"
    red_k = f"1/{k}" if k != 2.0 and k != 3.0 else ("1/2" if k == 2.0 else "1/3")
    sol = (
        f"**1. Scale factor k:**\n"
        f"\\[ k = \\frac{{{img}}}{{{orig}}} = {k} \\]\n\n"
        f"**2. Corresponding side:**\n"
        f"\\[ 4 \\times {k} = {s2_str} \\text{{ cm}} \\]\n\n"
        f"**3. Reduction scale factor:**\n"
        f"\\[ \\text{{Reduction factor}} = \\frac{{1}}{{{k}}} = {red_k} \\]"
    )
    ans = f"1. k = {k}; 2. {s2_str} cm; 3. {red_k}"
    return {
        "id": f"g8_sim_scale_fac_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "38_similar_triangles_scale_factor_enlargement_reduction",
        "learning_objective_id": "math_g8_sim_scale_fac",
        "hints": {
            "tier_1": "Scale factor = length of new side ÷ length of original side.",
            "tier_2": f"{img} ÷ {orig} = {k}.",
            "tier_3": f"k = {k}, side = {s2_str} cm, reduction = {red_k}.",
        },
        "misconception_tags": ["subtracting_lengths_to_find_scale_factor"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 39. Polygon Classification By Number Of Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_39_polygon_classification_by_number_of_sides(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 9, 10])
    names = {
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon",
    }
    name = names[n]
    svg = draw_regular_polygon_svg(n_sides=n, seed=rng.randint(100, 999999))

    prompt = (
        f"A closed 2D polygon has **{n} straight sides**.\n\n"
        f"1. Give the formal geometric name of this polygon.\n"
        f"2. How many interior angles does this polygon have?\n"
        f"3. How many vertices does this polygon have?"
    )
    sol = (
        f"**1. Name:** {name}.\n\n"
        f"**2. Interior angles:** Exactly **{n}** interior angles.\n\n"
        f"**3. Vertices:** Exactly **{n}** vertices."
    )
    ans = f"1. {name}; 2. {n}; 3. {n}"
    return {
        "id": f"g8_poly_class_sides_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "39_polygon_classification_by_number_of_sides",
        "learning_objective_id": "math_g8_poly_class_sides",
        "hints": {
            "tier_1": "Recall: 5=pentagon, 6=hexagon, 7=heptagon, 8=octagon, 9=nonagon, 10=decagon.",
            "tier_2": "In any polygon, number of sides = number of angles = number of vertices.",
            "tier_3": f"{name}, {n} angles, {n} vertices.",
        },
        "misconception_tags": ["confusing_hexagon_and_heptagon"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 40. Convex Vs Concave Polygons (WITH SVG)
# ----------------------------------------------------------------------
def arch_40_convex_vs_concave_polygons(rng: random.Random) -> Dict[str, Any]:
    svg = draw_regular_polygon_svg(n_sides=5, seed=rng.randint(100, 999999))

    prompt = (
        f"Polygons are classified as either **convex** or **concave** based on their interior angles:\n\n"
        f"1. Define a **convex polygon**.\n"
        f"2. Define a **concave polygon** and state what type of interior angle it must contain.\n"
        f"3. Can a triangle ever be concave? Explain your reasoning."
    )
    sol = (
        f"**1. Convex polygon:** A polygon where all interior angles are strictly less than \\(180^\\circ\\).\n\n"
        f"**2. Concave polygon:** A polygon that has at least one interior angle greater than \\(180^\\circ\\) (a reflex angle).\n\n"
        f"**3. Can a triangle be concave:** No, because the sum of all three interior angles of a triangle is only \\(180^\\circ\\), "
        f"so it is impossible for any single angle to exceed \\(180^\\circ\\)."
    )
    ans = "1. all interior angles < 180°; 2. at least one reflex angle (> 180°); 3. No, triangle sum is only 180°"
    return {
        "id": f"g8_poly_convex_concave_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "40_convex_vs_concave_polygons",
        "learning_objective_id": "math_g8_poly_convex_concave",
        "hints": {
            "tier_1": "Convex polygons have no reflex angles.",
            "tier_2": "Concave polygons 'cave in' with at least one angle > 180°.",
            "tier_3": "Convex: all < 180°; Concave: has reflex angle; Triangles cannot be concave.",
        },
        "misconception_tags": ["thinking_triangles_can_be_concave"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 41. Polygon Interior Angle Sum Formula (WITH SVG)
# ----------------------------------------------------------------------
def arch_41_polygon_interior_angle_sum_formula(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 10])
    poly_names = {5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 10: "decagon"}
    name = poly_names[n]
    sum_deg = (n - 2) * 180

    svg = draw_regular_polygon_svg(n_sides=n, seed=rng.randint(100, 999999))

    prompt = (
        f"The formula for the sum of the interior angles of an \\(n\\)-sided polygon is \\(S = (n - 2) \\times 180^\\circ\\).\n\n"
        f"1. Explain why the term \\((n - 2)\\) represents the number of non-overlapping triangles into which the polygon can be divided.\n"
        f"2. Calculate the sum of the interior angles of a **{name}** (\\(n = {n}\\))."
    )
    sol = (
        f"**1. Explanation:** From a single vertex, diagonals can be drawn to all other vertices except itself and the two adjacent ones, dividing the \\(n\\)-gon into \\((n - 2)\\) non-overlapping triangles. Each triangle has an angle sum of \\(180^\\circ\\).\n\n"
        f"**2. Calculation for {name}:**\n"
        f"\\[ S = ({n} - 2) \\times 180^\\circ = {n - 2} \\times 180^\\circ = {sum_deg}^\\circ \\]"
    )
    ans = f"1. divides into (n-2) triangles each with 180°; 2. {sum_deg}°"
    return {
        "id": f"g8_poly_int_sum_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "41_polygon_interior_angle_sum_formula",
        "learning_objective_id": "math_g8_poly_int_sum",
        "hints": {
            "tier_1": "Formula is (n - 2) × 180°.",
            "tier_2": f"For n = {n}: ({n} - 2) × 180° = {n - 2} × 180°.",
            "tier_3": f"Sum = {sum_deg}°.",
        },
        "misconception_tags": ["multiplying_n_by_180_without_subtracting_2"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Regular Polygon Each Interior Angle (WITH SVG)
# ----------------------------------------------------------------------
def arch_42_regular_polygon_each_interior_angle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 8])
    poly_names = {5: "pentagon", 6: "hexagon", 8: "octagon"}
    name = poly_names[n]
    tot_sum = (n - 2) * 180
    each_ang = tot_sum // n

    svg = draw_regular_polygon_svg(n_sides=n, interior_angle=f"{each_ang}°", seed=rng.randint(100, 999999))

    prompt = (
        f"A regular **{name}** has **{n} equal sides** and **{n} equal interior angles**.\n\n"
        f"1. Calculate the total sum of the interior angles.\n"
        f"2. Calculate the size of **each** interior angle in degrees."
    )
    sol = (
        f"**Step 1: Total interior angle sum**\n"
        f"\\[ S = ({n} - 2) \\times 180^\\circ = {n - 2} \\times 180^\\circ = {tot_sum}^\\circ \\]\n\n"
        f"**Step 2: Each interior angle**\n"
        f"\\[ \\text{{Each angle}} = \\frac{{{tot_sum}^\\circ}}{{{n}}} = {each_ang}^\\circ \\]"
    )
    ans = f"1. {tot_sum}°; 2. {each_ang}°"
    return {
        "id": f"g8_poly_each_int_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "42_regular_polygon_each_interior_angle",
        "learning_objective_id": "math_g8_poly_each_int",
        "hints": {
            "tier_1": "Divide the total interior angle sum by the number of sides n.",
            "tier_2": f"Total sum is {tot_sum}°. Divide by {n}.",
            "tier_3": f"Each angle = {each_ang}°.",
        },
        "misconception_tags": ["dividing_360_instead_of_interior_sum"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 43. Regular Polygon Each Exterior Angle (WITH SVG)
# ----------------------------------------------------------------------
def arch_43_regular_polygon_each_exterior_angle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 8, 9, 10])
    poly_names = {5: "pentagon", 6: "hexagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
    name = poly_names[n]
    ext_ang = 360 / n
    ext_str = f"{int(ext_ang)}" if ext_ang.is_integer() else f"{ext_ang:.1f}"

    svg = draw_regular_polygon_svg(n_sides=n, seed=rng.randint(100, 999999))

    prompt = (
        f"For any convex regular polygon, the exterior angles sum to \\(360^\\circ\\).\n\n"
        f"1. State the formula for the size of each exterior angle of a regular \\(n\\)-sided polygon.\n"
        f"2. Calculate the size of each exterior angle of a regular **{name}** (\\(n = {n}\\)).\n"
        f"3. Confirm that interior angle + exterior angle = \\(180^\\circ\\)."
    )
    int_ang = 180 - ext_ang
    int_str = f"{int(int_ang)}" if int_ang.is_integer() else f"{int_ang:.1f}"
    sol = (
        f"**1. Formula:** \\(\\text{{Each exterior angle}} = \\frac{{360^\\circ}}{{n}}\\).\n\n"
        f"**2. Calculation for {name}:**\n"
        f"\\[ \\text{{Each exterior angle}} = \\frac{{360^\\circ}}{{{n}}} = {ext_str}^\\circ \\]\n\n"
        f"**3. Confirmation:**\n"
        f"\\[ {int_str}^\\circ + {ext_str}^\\circ = 180^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]"
    )
    ans = f"1. 360/n; 2. {ext_str}°; 3. {int_str}° + {ext_str}° = 180°"
    return {
        "id": f"g8_poly_each_ext_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "43_regular_polygon_each_exterior_angle",
        "learning_objective_id": "math_g8_poly_each_ext",
        "hints": {
            "tier_1": "Divide 360° by the number of sides n.",
            "tier_2": f"360° / {n} = {ext_str}°.",
            "tier_3": f"Exterior angle = {ext_str}°; interior + exterior = 180°.",
        },
        "misconception_tags": ["dividing_180_by_n_instead_of_360"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 44. Polygon Exterior Angle Sum Always 360 (WITH SVG)
# ----------------------------------------------------------------------
def arch_44_polygon_exterior_angle_sum_always_360(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8])
    svg = draw_regular_polygon_svg(n_sides=n, seed=rng.randint(100, 999999))

    prompt = (
        f"Consider a convex polygon with **{n} sides**.\n\n"
        f"1. What is the sum of the exterior angles of this polygon?\n"
        f"2. Does the sum of exterior angles depend on the number of sides \\(n\\)? Explain."
    )
    sol = (
        f"**1. Sum of exterior angles:** Exactly \\(360^\\circ\\).\n\n"
        f"**2. Dependence on n:** No, it does NOT depend on \\(n\\). For *any* convex polygon, "
        f"one complete revolution around the perimeter turns through \\(360^\\circ\\), regardless of how many sides it has."
    )
    ans = "1. 360°; 2. No, exterior angle sum is always 360° for any convex polygon"
    return {
        "id": f"g8_poly_ext_sum_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_polygon_exterior_angle_sum_always_360",
        "learning_objective_id": "math_g8_poly_ext_sum",
        "hints": {
            "tier_1": "The exterior angles of any convex polygon always sum to 360°.",
            "tier_2": "It represents one full turn around the polygon.",
            "tier_3": "Sum = 360°; it never depends on n.",
        },
        "misconception_tags": ["multiplying_360_by_n"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 45. Regular Polygon Determine Sides From Interior Angle (WITH SVG)
# ----------------------------------------------------------------------
def arch_45_regular_polygon_determine_sides_from_interior_angle(rng: random.Random) -> Dict[str, Any]:
    n, int_ang, name = rng.choice([
        (5, 108, "pentagon"),
        (6, 120, "hexagon"),
        (8, 135, "octagon"),
        (10, 144, "decagon"),
    ])
    ext_ang = 180 - int_ang

    svg = draw_regular_polygon_svg(n_sides=n, interior_angle=f"{int_ang}°", seed=rng.randint(100, 999999))

    prompt = (
        f"Each interior angle of a regular polygon measures **{int_ang}^\\circ**.\n\n"
        f"1. Calculate the size of each exterior angle.\n"
        f"2. Use the exterior angle to determine the number of sides \\(n\\) of this polygon.\n"
        f"3. Name the polygon."
    )
    sol = (
        f"**Step 1: Each exterior angle**\n"
        f"\\[ \\text{{Exterior angle}} = 180^\\circ - {int_ang}^\\circ = {ext_ang}^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]\n\n"
        f"**Step 2: Number of sides n**\n"
        f"\\[ n = \\frac{{360^\\circ}}{{{ext_ang}^\\circ}} = {n} \\]\n\n"
        f"**Step 3: Name**\n"
        f"The polygon is a regular **{name}**."
    )
    ans = f"1. {ext_ang}°; 2. n = {n}; 3. {name}"
    return {
        "id": f"g8_poly_find_n_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "45_regular_polygon_determine_sides_from_interior_angle",
        "learning_objective_id": "math_g8_poly_find_n",
        "hints": {
            "tier_1": "Find exterior angle = 180° - interior angle.",
            "tier_2": f"360° / {ext_ang}° = {n}.",
            "tier_3": f"n = {n}, {name}.",
        },
        "misconception_tags": ["dividing_interior_angle_by_360"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 46. Composite Triangle And Straight Line Multistep (WITH SVG)
# ----------------------------------------------------------------------
def arch_46_composite_triangle_and_straight_line_multistep(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([40, 50, 60])
    ext_ang = rng.choice([110, 120, 130])
    int_c = 180 - ext_ang
    ang_b = 180 - (ang1 + int_c)

    labels = {"A": f"{ang1}°", "B": "x"}
    svg = draw_triangle_svg(
        ang1,
        ang_b,
        int_c,
        angle_labels=labels,
        ext_angle=("C", f"{ext_ang}°"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given triangle \\(ABC\\), vertex \\(C\\) lies on straight line \\(BCD\\).\n"
        f"Exterior angle \\(\\angle ACD = {ext_ang}^\\circ\\) and interior angle \\(\\hat{{A}} = {ang1}^\\circ\\).\n\n"
        f"1. Calculate interior angle \\(\\angle ACB\\) using straight line supplementary angles.\n"
        f"2. Calculate angle \\(x = \\hat{{B}}\\) using the triangle interior angle sum."
    )
    sol = (
        f"**Step 1: Calculate angle ACB**\n"
        f"\\[ \\angle ACB = 180^\\circ - {ext_ang}^\\circ = {int_c}^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]\n\n"
        f"**Step 2: Calculate angle B**\n"
        f"\\[ x = 180^\\circ - ({ang1}^\\circ + {int_c}^\\circ) = {ang_b}^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]"
    )
    ans = f"1. ACB = {int_c}°; 2. x = {ang_b}°"
    return {
        "id": f"g8_comp_tri_line_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "46_composite_triangle_and_straight_line_multistep",
        "learning_objective_id": "math_g8_comp_tri_line",
        "hints": {
            "tier_1": "Angles on a straight line sum to 180°.",
            "tier_2": f"Angle ACB = 180° - {ext_ang}° = {int_c}°.",
            "tier_3": f"x = 180° - ({ang1}° + {int_c}°) = {ang_b}°.",
        },
        "misconception_tags": ["subtracting_exterior_angle_from_triangle_sum_directly"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Composite Triangle And Parallel Lines Multistep (WITH SVG)
# ----------------------------------------------------------------------
def arch_47_composite_triangle_and_parallel_lines_multistep(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([48, 54, 62])
    ang2 = rng.choice([50, 58, 66])
    ang3 = 180 - (ang1 + ang2)

    svg = draw_triangle_svg(
        ang1,
        ang2,
        ang3,
        angle_labels={"A": "y", "B": f"{ang2}°", "C": f"{ang3}°"},
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In \\(\\triangle ABC\\), a line is drawn through vertex \\(A\\) parallel to base \\(BC\\).\n"
        f"Given \\(\\hat{{B}} = {ang2}^\\circ\\) and \\(\\hat{{C}} = {ang3}^\\circ\\):\n\n"
        f"1. State the alternate interior angle at \\(A\\) corresponding to \\(\\hat{{B}}\\).\n"
        f"2. Calculate the value of \\(y = \\hat{{A}}\\) with reason."
    )
    sol = (
        f"**1. Alternate angle:** An angle of \\({ang2}^\\circ\\) at vertex \\(A\\) is alternate to \\(\\hat{{B}}\\) "
        f"(\\(\\text{{alt. }}\\angle\\text{{s, parallel lines}}\\)).\n\n"
        f"**2. Angle y:**\n"
        f"\\[ y = 180^\\circ - ({ang2}^\\circ + {ang3}^\\circ) = {ang1}^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]"
    )
    ans = f"1. {ang2}° (alternate angles); 2. y = {ang1}° (sum of angles in triangle)"
    return {
        "id": f"g8_comp_tri_par_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "47_composite_triangle_and_parallel_lines_multistep",
        "learning_objective_id": "math_g8_comp_tri_par",
        "hints": {
            "tier_1": "Alternate angles on parallel lines are equal.",
            "tier_2": f"Subtract {ang2}° and {ang3}° from 180°.",
            "tier_3": f"y = {ang1}°.",
        },
        "misconception_tags": ["confusing_alternate_and_cointerior_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 48. Quadrilateral With Parallel Lines Multistep (WITH SVG)
# ----------------------------------------------------------------------
def arch_48_quadrilateral_with_parallel_lines_multistep(rng: random.Random) -> Dict[str, Any]:
    ang_d = rng.choice([65, 75, 80])
    ang_a = 180 - ang_d
    ang_c = rng.choice([70, 85, 90])
    ang_b = 360 - (ang_a + ang_d + ang_c)

    angles = {"A": f"{ang_a}°", "B": "x", "C": f"{ang_c}°", "D": f"{ang_d}°"}
    svg = draw_quadrilateral_svg(kind="trapezium", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In quadrilateral \\(ABCD\\), sides \\(AB \\parallel DC\\).\n"
        f"Angle \\(\\hat{{D}} = {ang_d}^\\circ\\), angle \\(\\hat{{A}} = {ang_a}^\\circ\\), and angle \\(\\hat{{C}} = {ang_c}^\\circ\\).\n\n"
        f"1. Explain why \\(\\hat{{A}} + \\hat{{D}} = 180^\\circ\\).\n"
        f"2. Calculate the value of \\(x = \\hat{{B}}\\) using co-interior angles between parallel lines."
    )
    sol = (
        f"**Step 1: Reason for A + D = 180°**\n"
        f"\\(\\hat{{A}}\\) and \\(\\hat{{D}}\\) are co-interior angles between parallel lines \\(AB \\parallel DC\\) "
        f"(\\(\\text{{co-int. }}\\angle\\text{{s, }} AB \\parallel DC\\)).\n\n"
        f"**Step 2: Calculate x**\n"
        f"Since \\(AB \\parallel DC\\), angles \\(\\hat{{B}}\\) and \\(\\hat{{C}}\\) are also co-interior:\n"
        f"\\[ x = 180^\\circ - {ang_c}^\\circ = {180 - ang_c}^\\circ \\quad (\\text{{co-int. }}\\angle\\text{{s, }} AB \\parallel DC) \\]"
    )
    ans = f"1. co-interior angles on parallel lines sum to 180°; 2. x = {180 - ang_c}°"
    return {
        "id": f"g8_quad_par_multi_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "48_quadrilateral_with_parallel_lines_multistep",
        "learning_objective_id": "math_g8_quad_par_multi",
        "hints": {
            "tier_1": "Angles between the parallel bases on the same side are co-interior and sum to 180°.",
            "tier_2": f"x = 180° - {ang_c}°.",
            "tier_3": f"x = {180 - ang_c}°.",
        },
        "misconception_tags": ["using_quadrilateral_sum_when_cointerior_is_simpler"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 49. Hierarchy Of Quadrilaterals True False Reasoning (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_49_hierarchy_of_quadrilaterals_true_false_reasoning(rng: random.Random) -> Dict[str, Any]:
    statements = [
        ("Every square is a rectangle.", True, "A square has four right angles, satisfying all definitions of a rectangle."),
        ("Every rectangle is a square.", False, "A rectangle does not necessarily have all four sides equal in length."),
        ("Every rhombus is a parallelogram.", True, "A rhombus has both pairs of opposite sides parallel and equal."),
        ("Every parallelogram is a rhombus.", False, "A parallelogram does not necessarily have all four sides equal."),
        ("Every square is a rhombus.", True, "A square has four equal sides, satisfying the definition of a rhombus."),
        ("Every trapezium is a parallelogram.", False, "A trapezium has only one pair of parallel sides, not two."),
    ]
    st1, st2 = rng.sample(statements, 2)

    prompt = (
        f"Consider the formal geometric definitions within the hierarchy of quadrilaterals:\n\n"
        f"1. Statement A: '{st1[0]}'\n"
        f"   State whether Statement A is **True** or **False**, and justify your answer.\n\n"
        f"2. Statement B: '{st2[0]}'\n"
        f"   State whether Statement B is **True** or **False**, and justify your answer."
    )
    ans1 = "True" if st1[1] else "False"
    ans2 = "True" if st2[1] else "False"
    sol = (
        f"**1. Statement A ({ans1}):** {st1[2]}\n\n"
        f"**2. Statement B ({ans2}):** {st2[2]}"
    )
    ans = f"1. {ans1}; 2. {ans2}"
    return {
        "id": f"g8_quad_hierarchy_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "49_hierarchy_of_quadrilaterals_true_false_reasoning",
        "learning_objective_id": "math_g8_quad_hierarchy",
        "hints": {
            "tier_1": "Recall the hierarchical definitions: square is most specific.",
            "tier_2": f"A is {ans1}; B is {ans2}.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["confusing_subset_and_superset_in_quadrilaterals"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 50. Geometric Proof Isosceles Triangle Base Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_50_geometric_proof_isosceles_triangle_base_angles(rng: random.Random) -> Dict[str, Any]:
    svg = draw_triangle_svg(
        50,
        65,
        65,
        angle_labels={"A": "apex", "B": "base 1", "C": "base 2"},
        side_labels={"AB": "equal", "AC": "equal"},
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In \\(\\triangle ABC\\), \\(AB = AC\\). A line is constructed from vertex \\(A\\) to midpoint \\(D\\) on base \\(BC\\):\n\n"
        f"1. State the three pairs of equal parts in \\(\\triangle ABD\\) and \\(\\triangle ACD\\).\n"
        f"2. Which congruency condition proves that \\(\\triangle ABD \\equiv \\triangle ACD\\)?\n"
        f"3. Deduce why base angles \\(\\hat{{B}}\\) and \\(\\hat{{C}}\\) must be equal."
    )
    sol = (
        f"**Step 1: Three equal parts**\n"
        f"1. \\(AB = AC\\) (given equal sides)\n"
        f"2. \\(BD = CD\\) (\\(D\\) is midpoint of \\(BC\\))\n"
        f"3. \\(AD = AD\\) (common shared side)\n\n"
        f"**Step 2: Congruency condition**\n"
        f"\\(\\triangle ABD \\equiv \\triangle ACD\\) (SSS).\n\n"
        f"**Step 3: Deduction**\n"
        f"Since the two triangles are congruent, their corresponding angles are equal: \\(\\hat{{B}} = \\hat{{C}}\\) "
        f"(\\(\\angle\\text{{s opp. equal sides}}\\))."
    )
    ans = "1. AB=AC, BD=CD, AD=AD; 2. SSS; 3. corresponding angles of congruent triangles are equal"
    return {
        "id": f"g8_iso_proof_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "50_geometric_proof_isosceles_triangle_base_angles",
        "learning_objective_id": "math_g8_iso_proof",
        "hints": {
            "tier_1": "Use the midpoint construction to split into two triangles.",
            "tier_2": "Identify 3 pairs of equal sides: SSS.",
            "tier_3": "SSS congruency proves corresponding base angles are equal.",
        },
        "misconception_tags": ["assuming_base_angles_are_equal_without_proving_it"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }
