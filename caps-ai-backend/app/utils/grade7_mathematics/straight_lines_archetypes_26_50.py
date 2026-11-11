"""Grade 7 Mathematics - Geometry of Straight Lines: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Geometry of straight lines.md
"""
import random
import math
from typing import Dict, Any, List


def _svg_wrap(inner: str, width: int = 400, height: int = 240) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{inner}'
        f'</svg>'
    )


# 26. Alternate interior angles Z-shape identification
def arch_26_alternate_interior_angles_z_shape_identification(rng: random.Random) -> Dict[str, Any]:
    tx1 = rng.choice([250, 260, 270, 280])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="{tx1}" y1="30" x2="{400 - tx1}" y2="210" stroke="#1e293b" stroke-width="3"/>'
        # Top interior angle (bottom-left at top intersection)
        f'<text x="210" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠1</text>'
        # Bottom interior angle (top-right at bottom intersection)
        f'<text x="180" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠2</text>'
    )
    prompt = (
        "Two parallel lines are crossed by a transversal. Angles ∠1 and ∠2 lie inside the parallel lines on opposite sides of the transversal.\n\n"
        "1. What is the specific geometric name for this pair of angles?\n"
        "2. Which letter of the alphabet (F, Z, or C) is used as a visual memory aid for alternate angles?\n"
        "3. If the lines are parallel, what is the relationship between the sizes of ∠1 and ∠2?"
    )
    sol = (
        "**Step 1:** Angles between two lines on opposite sides of a transversal are **alternate interior angles**.\n\n"
        "**Step 2:** The letter **Z** (or N) forms the visual aid for alternate angles.\n\n"
        "**Step 3:** Since the lines are parallel, alternate interior angles are **equal** [$\\text{{alt }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = "1. Alternate interior angles; 2. Z; 3. Equal"
    return {
        "id": f"g7_line_26_{rng.randint(100000, 999999)}",
        "subskill": "26_alternate_interior_angles_z_shape_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check Position", "body": "Angles lie inside the parallel lines and on alternate sides of the transversal."},
                {"title": "Z-Shape Aid", "body": "They form a Z-pattern."},
                {"title": "Conclusion", "body": "Alternate angles are equal when lines are parallel."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_26",
        "hints": {
            "tier_1": "Trace the path from ∠1 along the transversal to ∠2: what letter does it trace?",
            "tier_2": "It traces a Z: alternate interior angles.",
            "tier_3": "1. Alternate interior angles, 2. Z, 3. Equal."
        },
        "misconception_tags": ["confused_alternate_and_corresponding"]
    }


# 27. Alternate interior angles solve for x
def arch_27_alternate_interior_angles_solve_for_x(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([42, 53, 67, 73, 118, 127])
    l1 = "PQ"
    l2 = "RS"
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="260" y1="30" x2="140" y2="210" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="35" y="75" font-family="sans-serif" font-size="14" font-weight="bold">P</text>'
        f'<text x="360" y="75" font-family="sans-serif" font-size="14" font-weight="bold">Q</text>'
        f'<text x="35" y="175" font-family="sans-serif" font-size="14" font-weight="bold">R</text>'
        f'<text x="360" y="175" font-family="sans-serif" font-size="14" font-weight="bold">S</text>'
        f'<text x="210" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle}°</text>'
        f'<text x="180" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the diagram, {l1} // {l2}. One interior angle is given as {angle}°.\n\n"
        f"Calculate the value of $x$, stating the full geometric reason."
    )
    sol = (
        f"**Step 1:** The angles lie between the parallel lines on opposite sides of the transversal (Z-shape).\n\n"
        f"**Step 2:** Alternate interior angles are equal when lines are parallel:\n"
        f"$$x = {angle}^\\circ \\text{{ [alt }}\\angle\\text{{s, }}{l1} // {l2}\\text{{]}}$$"
    )
    ans = f"x = {angle}° [alt ∠s, {l1} // {l2}]"
    return {
        "id": f"g7_line_27_{rng.randint(100000, 999999)}",
        "subskill": "27_alternate_interior_angles_solve_for_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Trace Z", "body": f"Trace the Z from the {angle}° angle to angle x."},
                {"title": "State Equality", "body": f"x = {angle}° [alt ∠s, {l1} // {l2}]."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_27",
        "hints": {
            "tier_1": "Notice the Z-formation inside the parallel lines.",
            "tier_2": "Alternate interior angles are equal when lines are parallel.",
            "tier_3": f"x = {angle}° [alt ∠s, {l1} // {l2}]."
        },
        "misconception_tags": ["subtracted_alternate_angles_from_180"]
    }


# 28. Co-interior angles C-shape identification
def arch_28_co_interior_angles_c_shape_identification(rng: random.Random) -> Dict[str, Any]:
    tx1 = rng.choice([110, 120, 130, 140])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="{tx1}" y1="20" x2="{400 - tx1}" y2="220" stroke="#1e293b" stroke-width="3"/>'
        # Interior right angles
        f'<text x="200" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠A</text>'
        f'<text x="250" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">∠B</text>'
    )
    prompt = (
        "Two parallel lines are crossed by a transversal. Angles ∠A and ∠B lie inside the parallel lines on the SAME side of the transversal.\n\n"
        "1. What is the geometric name for this angle pair?\n"
        "2. Which letter of the alphabet (F, Z, or C/U) represents co-interior angles?\n"
        "3. Are ∠A and ∠B equal or supplementary?"
    )
    sol = (
        "**Step 1:** Angles between two parallel lines on the same side of a transversal are **co-interior angles**.\n\n"
        "**Step 2:** The letter **C** (or U) represents co-interior angles.\n\n"
        "**Step 3:** Co-interior angles between parallel lines are **supplementary** (they add up to $180^\\circ$) [$\\text{{co-int }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = "1. Co-interior angles; 2. C; 3. Supplementary (add to 180°)"
    return {
        "id": f"g7_line_28_{rng.randint(100000, 999999)}",
        "subskill": "28_co_interior_angles_c_shape_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Same Side", "body": "Both angles sit between the parallel lines on the right side of the transversal."},
                {"title": "C-Shape", "body": "This forms a C-shape: co-interior angles."},
                {"title": "Supplementary", "body": "They add to 180°, they are not equal unless both are 90°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_28",
        "hints": {
            "tier_1": "Angles on the same interior side form a C-shape.",
            "tier_2": "Co-interior angles add up to 180° (supplementary).",
            "tier_3": "1. Co-interior angles, 2. C, 3. Supplementary."
        },
        "misconception_tags": ["co_interior_assumed_equal"]
    }


# 29. Co-interior angles solve supplementary
def arch_29_co_interior_angles_solve_supplementary(rng: random.Random) -> Dict[str, Any]:
    angle_given = rng.choice([65, 75, 85, 105, 115, 125])
    unknown = 180 - angle_given
    l1 = "MN"
    l2 = "OP"
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="120" y1="20" x2="280" y2="220" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="35" y="75" font-family="sans-serif" font-size="14" font-weight="bold">M</text>'
        f'<text x="360" y="75" font-family="sans-serif" font-size="14" font-weight="bold">N</text>'
        f'<text x="35" y="175" font-family="sans-serif" font-size="14" font-weight="bold">O</text>'
        f'<text x="360" y="175" font-family="sans-serif" font-size="14" font-weight="bold">P</text>'
        f'<text x="200" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle_given}°</text>'
        f'<text x="250" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
    )
    prompt = (
        f"In the diagram, {l1} // {l2}. One co-interior angle is {angle_given}°.\n\n"
        f"Calculate the value of $x$, giving the geometric reason."
    )
    sol = (
        f"**Step 1:** Identify the angle pair:\n"
        f"The two angles are co-interior between parallel lines [$\\text{{co-int }}\\angle\\text{{s, }}{l1} // {l2}$].\n\n"
        f"**Step 2:** Co-interior angles are supplementary:\n"
        f"$$x + {angle_given}^\\circ = 180^\\circ$$\n"
        f"$$x = 180^\\circ - {angle_given}^\\circ = {unknown}^\\circ$$\n\n"
        f"**Conclusion:** $x = {unknown}^\\circ$ [$\\text{{co-int }}\\angle\\text{{s, }}{l1} // {l2}$]."
    )
    ans = f"x = {unknown}° [co-int ∠s, {l1} // {l2}]"
    return {
        "id": f"g7_line_29_{rng.randint(100000, 999999)}",
        "subskill": "29_co_interior_angles_solve_supplementary",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Identify Co-interior", "body": "Both angles lie inside on the same side of the transversal."},
                {"title": "Set up Sum", "body": f"x + {angle_given}° = 180° [co-int ∠s, {l1} // {l2}]."},
                {"title": "Solve x", "body": f"x = 180° - {angle_given}° = {unknown}°."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_29",
        "hints": {
            "tier_1": "Do co-interior angles equal each other or add to 180°?",
            "tier_2": f"They add to 180°. Subtract {angle_given} from 180.",
            "tier_3": f"x = {unknown}° [co-int ∠s, {l1} // {l2}]."
        },
        "misconception_tags": ["co_interior_equality_fallacy"]
    }


# 30. Parallel lines mixed angle pair identification
def arch_30_parallel_lines_mixed_angle_pair_identification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Match each angle pair relationship with its defining property when lines are parallel:\n\n"
        "1. Corresponding angles (F-shape)\n"
        "2. Alternate interior angles (Z-shape)\n"
        "3. Co-interior angles (C-shape)\n\n"
        "Choose from:\n"
        "A) Angles add up to 180° (supplementary)\n"
        "B) Angles are equal\n"
        "C) Angles are equal"
    )
    sol = (
        "**1. Corresponding angles (F-shape):** Equal (Property B/C).\n"
        "**2. Alternate interior angles (Z-shape):** Equal (Property B/C).\n"
        "**3. Co-interior angles (C-shape):** Supplementary / add to 180° (Property A)."
    )
    ans = "1: Equal, 2: Equal, 3: Supplementary (add to 180°)"
    return {
        "id": f"g7_line_30_{rng.randint(100000, 999999)}",
        "subskill": "30_parallel_lines_mixed_angle_pair_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_30",
        "hints": {
            "tier_1": "Remember F and Z give equal angles, while C gives supplementary angles.",
            "tier_2": "FUN (F = equal, U/C = 180°, N/Z = equal).",
            "tier_3": "Corresponding: Equal; Alternate: Equal; Co-interior: Supplementary."
        },
        "misconception_tags": ["confused_angle_pair_theorems"]
    }


# 31. Parallel lines multi-step two unknowns
def arch_31_parallel_lines_multi_step_two_unknowns(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([55, 65, 70, 75, 80])
    supp = 180 - angle
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="120" y1="20" x2="280" y2="220" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="170" y="55" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{angle}°</text>'
        f'<text x="210" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
        f'<text x="260" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#059669">y</text>'
    )
    prompt = (
        f"In the diagram, line AB // CD cut by transversal EF. The top obtuse angle is {angle}°.\n\n"
        f"1. Calculate the value of $x$ (adjacent on straight line).\n"
        f"2. Calculate the value of $y$ (corresponding to {angle}°).\n"
        f"Give geometric reasons for both answers."
    )
    sol = (
        f"**Step 1:** Solve for $x$:\n"
        f"Angles {angle}° and $x$ lie on a straight line:\n"
        f"$$x = 180^\\circ - {angle}^\\circ = {supp}^\\circ \\text{{ [}}\\angle\\text{{s on a straight line]}}$$\n\n"
        f"**Step 2:** Solve for $y$:\n"
        f"Angle $y$ and {angle}° are corresponding angles:\n"
        f"$$y = {angle}^\\circ \\text{{ [corr }}\\angle\\text{{s, AB // CD]}}$$"
    )
    ans = f"x = {supp}° [∠s on straight line], y = {angle}° [corr ∠s, AB // CD]"
    return {
        "id": f"g7_line_31_{rng.randint(100000, 999999)}",
        "subskill": "31_parallel_lines_multi_step_two_unknowns",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Find x", "body": f"x = 180° - {angle}° = {supp}° [∠s on straight line]."},
                {"title": "Find y", "body": f"y = {angle}° [corr ∠s, AB // CD]."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_geom_lines_31",
        "hints": {
            "tier_1": "Find x first using the straight line, then find y using parallel lines.",
            "tier_2": f"x = 180 - {angle} = {supp}°. y corresponds to {angle}°.",
            "tier_3": f"x = {supp}°, y = {angle}°."
        },
        "misconception_tags": ["multi_step_geometry_reason_omission"]
    }


# 32. Parallel lines algebraic corresponding equation
def arch_32_parallel_lines_algebraic_corresponding_equation(rng: random.Random) -> Dict[str, Any]:
    # 2x + 15 = 75 -> 2x = 60 -> x = 30
    x_val = rng.choice([20, 25, 30, 35])
    a = rng.choice([2, 3])
    b = rng.choice([10, 15, 20])
    total_ang = a * x_val + b
    prompt = (
        f"Two parallel lines are cut by a transversal. Two corresponding angles measure $({a}x + {b}^\\circ)$ and ${total_ang}^\\circ$.\n\n"
        f"1. Set up an algebraic equation and solve for $x$.\n"
        f"2. State the theorem justifying your equation."
    )
    sol = (
        f"**Step 1:** Corresponding angles on parallel lines are equal [$\\text{{corr }}\\angle\\text{{s, lines parallel}}$].\n\n"
        f"**Step 2:** Formulate and solve the equation:\n"
        f"$${a}x + {b} = {total_ang}$$\n"
        f"$${a}x = {total_ang} - {b} = {a * x_val}$$\n"
        f"$$x = \\frac{{{a * x_val}}}{{{a}}} = {x_val}$$\n\n"
        f"**Conclusion:** $x = {x_val}$ [$\\text{{corr }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = f"x = {x_val} [corr ∠s, lines parallel]"
    return {
        "id": f"g7_line_32_{rng.randint(100000, 999999)}",
        "subskill": "32_parallel_lines_algebraic_corresponding_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_32",
        "hints": {
            "tier_1": f"Equate the two expressions: {a}x + {b} = {total_ang}.",
            "tier_2": f"Subtract {b} then divide by {a}.",
            "tier_3": f"x = {x_val}."
        },
        "misconception_tags": ["algebraic_corresponding_angle_error"]
    }


# 33. Parallel lines algebraic alternate equation
def arch_33_parallel_lines_algebraic_alternate_equation(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([15, 20, 24, 30])
    a = rng.choice([3, 4])
    b = rng.choice([5, 12, 18])
    total_ang = a * x_val - b
    prompt = (
        f"Two alternate interior angles between parallel lines are given by $({a}x - {b}^\\circ)$ and ${total_ang}^\\circ$.\n\n"
        f"1. Solve for $x$.\n"
        f"2. Give the geometric reason."
    )
    sol = (
        f"**Step 1:** Alternate interior angles on parallel lines are equal [$\\text{{alt }}\\angle\\text{{s, lines parallel}}$].\n\n"
        f"**Step 2:** Formulate and solve the equation:\n"
        f"$${a}x - {b} = {total_ang}$$\n"
        f"$${a}x = {total_ang} + {b} = {a * x_val}$$\n"
        f"$$x = \\frac{{{a * x_val}}}{{{a}}} = {x_val}$$\n\n"
        f"**Conclusion:** $x = {x_val}$ [$\\text{{alt }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = f"x = {x_val} [alt ∠s, lines parallel]"
    return {
        "id": f"g7_line_33_{rng.randint(100000, 999999)}",
        "subskill": "33_parallel_lines_algebraic_alternate_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_33",
        "hints": {
            "tier_1": f"Equate: {a}x - {b} = {total_ang}.",
            "tier_2": f"Add {b} to both sides: {a}x = {a * x_val}.",
            "tier_3": f"x = {x_val}."
        },
        "misconception_tags": ["sign_error_solving_alternate_equation"]
    }


# 34. Parallel lines algebraic co-interior equation
def arch_34_parallel_lines_algebraic_co_interior_equation(rng: random.Random) -> Dict[str, Any]:
    # (x + 20) + (2x + 40) = 180 -> 3x + 60 = 180 -> 3x = 120 -> x = 40
    x_val = rng.choice([25, 30, 35, 40])
    c1, c2 = 1, 2
    b1 = 20
    b2 = 180 - (3 * x_val + b1)
    prompt = (
        f"Two co-interior angles between parallel lines are $(x + {b1}^\\circ)$ and $(2x + {b2}^\\circ)$.\n\n"
        f"1. Set up an equation using the co-interior angle theorem.\n"
        f"2. Solve for $x$."
    )
    sum_b = b1 + b2
    sol = (
        f"**Step 1:** Co-interior angles between parallel lines add to $180^\\circ$ [$\\text{{co-int }}\\angle\\text{{s, lines parallel}}$].\n\n"
        f"**Step 2:** Formulate and solve the equation:\n"
        f"$$(x + {b1}^\\circ) + (2x + {b2}^\\circ) = 180^\\circ$$\n"
        f"$$3x + {sum_b}^\\circ = 180^\\circ$$\n"
        f"$$3x = 180^\\circ - {sum_b}^\\circ = {3 * x_val}^\\circ$$\n"
        f"$$x = \\frac{{{3 * x_val}}}{{3}} = {x_val}^\\circ$$\n\n"
        f"**Conclusion:** $x = {x_val}^\\circ$ [$\\text{{co-int }}\\angle\\text{{s, lines parallel}}$]."
    )
    ans = f"x = {x_val}° [co-int ∠s, lines parallel]"
    return {
        "id": f"g7_line_34_{rng.randint(100000, 999999)}",
        "subskill": "34_parallel_lines_algebraic_co_interior_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_34",
        "hints": {
            "tier_1": "Do not equate them! Co-interior angles add to 180°.",
            "tier_2": f"Set (x + {b1}) + (2x + {b2}) = 180.",
            "tier_3": f"3x = {3 * x_val}, so x = {x_val}°."
        },
        "misconception_tags": ["equated_co_interior_angles"]
    }


# 35. Testing parallel lines equal alternate angles
def arch_35_testing_parallel_lines_equal_alternate_angles(rng: random.Random) -> Dict[str, Any]:
    is_parallel = rng.choice([True, False])
    ang1 = rng.choice([58, 64, 72, 81])
    ang2 = ang1 if is_parallel else ang1 + rng.choice([-6, -4, 4, 6])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="260" y1="30" x2="140" y2="210" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="35" y="75" font-family="sans-serif" font-size="14" font-weight="bold">AB</text>'
        f'<text x="35" y="175" font-family="sans-serif" font-size="14" font-weight="bold">CD</text>'
        f'<text x="210" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{ang1}°</text>'
        f'<text x="180" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{ang2}°</text>'
    )
    prompt = (
        f"In the diagram, a transversal cuts two lines AB and CD. Alternate interior angles are measured as {ang1}° and {ang2}°.\n\n"
        f"Are lines AB and CD parallel? Explain your answer with reference to the alternate angle test."
    )
    if is_parallel:
        sol = (
            f"**Step 1:** Compare the alternate interior angles:\n"
            f"Both alternate angles are equal to {ang1}°.\n\n"
            f"**Step 2:** Conclusion:\n"
            f"**Yes**, AB // CD because the alternate interior angles are equal [converse alt $\\angle$s]."
        )
        ans = f"Yes, AB // CD because alternate angles are equal ({ang1}° = {ang2}°)."
    else:
        sol = (
            f"**Step 1:** Compare the alternate interior angles:\n"
            f"The alternate angles are {ang1}° and {ang2}°, which are NOT equal ({ang1}° $\\neq$ {ang2}°).\n\n"
            f"**Step 2:** Conclusion:\n"
            f"**No**, AB is NOT parallel to CD because the alternate interior angles are not equal."
        )
        ans = f"No, AB is not parallel to CD because alternate angles are not equal ({ang1}° ≠ {ang2}°)."
    return {
        "id": f"g7_line_35_{rng.randint(100000, 999999)}",
        "subskill": "35_testing_parallel_lines_equal_alternate_angles",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check Angle Sizes", "body": f"Alternate angles are {ang1}° and {ang2}°."},
                {"title": "Compare", "body": "Are they equal?"},
                {"title": "Result", "body": ans}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_35",
        "hints": {
            "tier_1": f"Check if {ang1}° equals {ang2}°.",
            "tier_2": "Lines are parallel if and only if alternate angles are equal.",
            "tier_3": ans
        },
        "misconception_tags": ["assumed_parallel_without_equal_angles"]
    }


# 36. Testing parallel lines equal corresponding angles
def arch_36_testing_parallel_lines_equal_corresponding_angles(rng: random.Random) -> Dict[str, Any]:
    is_parallel = rng.choice([True, False])
    ang1 = rng.choice([62, 74, 85, 112])
    ang2 = ang1 if is_parallel else ang1 + rng.choice([-5, -3, 3, 5])
    prompt = (
        f"Two straight lines EF and GH are cut by a transversal. The corresponding angles are measured as {ang1}° and {ang2}°.\n\n"
        f"State whether line EF is parallel to line GH, providing full geometric justification."
    )
    if is_parallel:
        sol = f"**Yes**, EF // GH because corresponding angles are equal ({ang1}° = {ang2}°) [converse corr $\\angle$s]."
        ans = f"Yes, EF // GH because corresponding angles are equal ({ang1}° = {ang2}°)."
    else:
        sol = f"**No**, EF is NOT parallel to GH because corresponding angles are unequal ({ang1}° $\\neq$ {ang2}°)."
        ans = f"No, EF is not parallel to GH because corresponding angles are not equal ({ang1}° ≠ {ang2}°)."
    return {
        "id": f"g7_line_36_{rng.randint(100000, 999999)}",
        "subskill": "36_testing_parallel_lines_equal_corresponding_angles",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_36",
        "hints": {
            "tier_1": "Corresponding angles must be exactly equal for lines to be parallel.",
            "tier_2": f"Are {ang1}° and {ang2}° equal?",
            "tier_3": ans
        },
        "misconception_tags": ["tested_corresponding_angle_inequality"]
    }


# 37. Testing parallel lines supplementary co-interior
def arch_37_testing_parallel_lines_supplementary_co_interior(rng: random.Random) -> Dict[str, Any]:
    is_parallel = rng.choice([True, False])
    ang1 = rng.choice([65, 75, 80, 110, 120])
    ang2 = (180 - ang1) if is_parallel else (180 - ang1 + rng.choice([-8, -5, 5, 8]))
    total = ang1 + ang2
    prompt = (
        f"In a geometric figure, two interior angles on the same side of a transversal are {ang1}° and {ang2}°.\n\n"
        f"1. Calculate the sum of the two co-interior angles.\n"
        f"2. Conclude whether the two lines cut by the transversal are parallel."
    )
    if is_parallel:
        sol = (
            f"**Step 1:** Sum of angles: ${ang1}^\\circ + {ang2}^\\circ = {total}^\\circ$.\n\n"
            f"**Step 2:** Since the sum is exactly $180^\\circ$, the lines are **parallel** [converse co-int $\\angle$s]."
        )
        ans = f"1. {total}°; 2. Yes, the lines are parallel because co-interior angles sum to 180°."
    else:
        sol = (
            f"**Step 1:** Sum of angles: ${ang1}^\\circ + {ang2}^\\circ = {total}^\\circ$.\n\n"
            f"**Step 2:** Since the sum is {total}° (not $180^\\circ$), the lines are **NOT parallel**."
        )
        ans = f"1. {total}°; 2. No, the lines are not parallel because co-interior angles do not sum to 180° ({total}° ≠ 180°)."
    return {
        "id": f"g7_line_37_{rng.randint(100000, 999999)}",
        "subskill": "37_testing_parallel_lines_supplementary_co_interior",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_37",
        "hints": {
            "tier_1": f"Add {ang1} and {ang2}.",
            "tier_2": "Do they add up to exactly 180°?",
            "tier_3": ans
        },
        "misconception_tags": ["co_interior_sum_check_failure"]
    }


# 38. Parallel lines with transversal and bisector
def arch_38_parallel_lines_with_transversal_and_bisector(rng: random.Random) -> Dict[str, Any]:
    total_angle = rng.choice([60, 70, 80, 90, 100])
    half = total_angle // 2
    prompt = (
        f"Two parallel lines AB and CD are cut by transversal EF. An angle of {total_angle}° formed at the top intersection "
        f"is bisected by ray EG into two equal halves.\n\n"
        f"Calculate the size of each bisected angle."
    )
    sol = (
        f"**Step 1:** An angle bisector divides an angle into two equal parts.\n\n"
        f"**Step 2:** Each part measures:\n"
        f"$$\\frac{{{total_angle}^\\circ}}{{2}} = {half}^\\circ$$"
    )
    ans = f"{half}°"
    return {
        "id": f"g7_line_38_{rng.randint(100000, 999999)}",
        "subskill": "38_parallel_lines_with_transversal_and_bisector",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_38",
        "hints": {
            "tier_1": "What does 'bisect' mean?",
            "tier_2": f"Divide {total_angle} by 2.",
            "tier_3": f"{half}°."
        },
        "misconception_tags": ["angle_bisector_misunderstanding"]
    }


# 39. Two transversals intersecting between parallels
def arch_39_two_transversals_intersecting_between_parallels(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([35, 40, 45, 50])
    a2 = rng.choice([55, 60, 65, 70])
    # Reflex or interior angle in triangle: angle sum in triangle = 180 - (a1 + a2)
    third = 180 - (a1 + a2)
    prompt = (
        f"Two parallel lines AB and CD are intersected by two transversals that meet at point P between the parallel lines, "
        f"forming a triangle with the top parallel line. The two base angles at the top parallel line are {a1}° and {a2}°.\n\n"
        f"Calculate the interior angle at vertex P, giving the geometric reason."
    )
    sol = (
        f"**Step 1:** The angles inside the triangle formed between the lines add up to $180^\\circ$ [$\\text{{sum of }}\\angle\\text{{s in }}\\Delta$].\n\n"
        f"**Step 2:** Solve for angle P:\n"
        f"$$\\angle P = 180^\\circ - ({a1}^\\circ + {a2}^\\circ) = 180^\\circ - {a1 + a2}^\\circ = {third}^\\circ$$\n\n"
        f"**Conclusion:** $\\angle P = {third}^\\circ$ [$\\text{{sum of }}\\angle\\text{{s in }}\\Delta$]."
    )
    ans = f"{third}° [sum of ∠s in △]"
    return {
        "id": f"g7_line_39_{rng.randint(100000, 999999)}",
        "subskill": "39_two_transversals_intersecting_between_parallels",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_39",
        "hints": {
            "tier_1": "Look at the triangle formed by the lines.",
            "tier_2": f"Subtract ({a1} + {a2}) from 180°.",
            "tier_3": f"{third}°."
        },
        "misconception_tags": ["triangle_angle_sum_error"]
    }


# 40. Transversal perpendicular to parallel line
def arch_40_transversal_perpendicular_to_parallel_line(rng: random.Random) -> Dict[str, Any]:
    tx = rng.choice([145, 160, 175, 220])
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        # Perpendicular transversal
        f'<line x1="{tx}" y1="30" x2="{tx}" y2="210" stroke="#1e293b" stroke-width="3"/>'
        f'<rect x="{tx}" y="55" width="15" height="15" fill="none" stroke="#1e293b"/>'
        f'<text x="{tx+15}" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
        f'<text x="35" y="75" font-family="sans-serif" font-size="14" font-weight="bold">L1</text>'
        f'<text x="35" y="175" font-family="sans-serif" font-size="14" font-weight="bold">L2</text>'
    )
    prompt = (
        "Lines L1 and L2 are parallel. A transversal line is perpendicular to L1.\n\n"
        "1. What is the size of angle $x$ formed with L2?\n"
        "2. State the geometric reason justifying your answer."
    )
    sol = (
        "**Step 1:** If a transversal is perpendicular to one of two parallel lines, it is also perpendicular to the other.\n\n"
        "**Step 2:** Angle $x = 90^\\circ$ [$\\text{{corr }}\\angle\\text{{s, L1 // L2}}$ or $\\text{{co-int }}\\angle\\text{{s, L1 // L2}}$]."
    )
    ans = "1. 90°; 2. corr ∠s, L1 // L2 (or co-int ∠s, L1 // L2)"
    return {
        "id": f"g7_line_40_{rng.randint(100000, 999999)}",
        "subskill": "40_transversal_perpendicular_to_parallel_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Perpendicular to L1", "body": "The transversal meets L1 at 90°."},
                {"title": "Parallel Lines Property", "body": "By corresponding angles, it must meet L2 at 90° as well."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_40",
        "hints": {
            "tier_1": "Perpendicular means 90°.",
            "tier_2": "Corresponding angles on parallel lines are equal.",
            "tier_3": "x = 90°."
        },
        "misconception_tags": ["perpendicular_transversal_misconception"]
    }


# 41. Straight line with perpendicular ray and angle
def arch_41_straight_line_with_perpendicular_ray_and_angle(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([22, 33, 44, 55, 66])
    comp = 90 - angle
    prompt = (
        f"Ray OB is perpendicular to line AOC at point O. Ray OD lies in the interior of right angle BOC "
        f"such that $\\angle BOD = {angle}^\\circ$.\n\n"
        f"Calculate the size of $\\angle DOC$, giving the geometric reason."
    )
    sol = (
        f"**Step 1:** Since $OB \\perp AOC$, $\\angle BOC = 90^\\circ$.\n\n"
        f"**Step 2:** $\\angle BOD$ and $\\angle DOC$ are complementary:\n"
        f"$$\\angle DOC = 90^\\circ - {angle}^\\circ = {comp}^\\circ \\text{{ [comp }}\\angle\\text{{s]}}$$"
    )
    ans = f"{comp}° [comp ∠s]"
    return {
        "id": f"g7_line_41_{rng.randint(100000, 999999)}",
        "subskill": "41_straight_line_with_perpendicular_ray_and_angle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_41",
        "hints": {
            "tier_1": "The whole angle BOC is 90°.",
            "tier_2": f"Subtract {angle}° from 90°.",
            "tier_3": f"{comp}°."
        },
        "misconception_tags": ["complementary_calculation_error"]
    }


# 42. Geometric reasons matching straight line theorems
def arch_42_geometric_reasons_matching_straight_line_theorems(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Write down the accepted South African CAPS short geometric reason for each statement:\n\n"
        "1. Adjacent angles on a straight line add to 180°.\n"
        "2. Angles opposite each other at an intersection are equal.\n"
        "3. Angles in an F-position across parallel lines AB and CD are equal."
    )
    sol = (
        "**1.** [$\\angle\\text{{s on a straight line}}$] or [$\\text{{adj }}\\angle\\text{{s on str line}}$]\n"
        "**2.** [$\\text{{vert opp }}\\angle\\text{{s}}$]\n"
        "**3.** [$\\text{{corr }}\\angle\\text{{s, AB // CD}}$]"
    )
    ans = "1. [∠s on straight line]; 2. [vert opp ∠s]; 3. [corr ∠s, AB // CD]"
    return {
        "id": f"g7_line_42_{rng.randint(100000, 999999)}",
        "subskill": "42_geometric_reasons_matching_straight_line_theorems",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_geom_lines_42",
        "hints": {
            "tier_1": "Use standard bracketed abbreviations like [adj ∠s on str line].",
            "tier_2": "Always mention the parallel lines for parallel line theorems: [corr ∠s, AB // CD].",
            "tier_3": "1. [∠s on straight line], 2. [vert opp ∠s], 3. [corr ∠s, AB // CD]."
        },
        "misconception_tags": ["omitted_geometric_reason_abbreviation"]
    }


# 43. Spot the error angle on straight line
def arch_43_spot_the_error_angle_on_straight_line(rng: random.Random) -> Dict[str, Any]:
    given = rng.choice([40, 50, 60, 70])
    wrong_ans = 90 - given
    correct_ans = 180 - given
    prompt = (
        f"A learner was asked to find angle $x$ adjacent to {given}° on a straight line.\n"
        f"The learner wrote:\n"
        f"$$x = 90^\\circ - {given}^\\circ = {wrong_ans}^\\circ$$\n\n"
        f"1. Identify the learner's error.\n"
        f"2. Provide the correct calculation and reason."
    )
    sol = (
        f"**Step 1:** The learner confused complementary angles ($90^\\circ$) with supplementary angles on a straight line ($180^\\circ$).\n\n"
        f"**Step 2:** Correct calculation:\n"
        f"$$x = 180^\\circ - {given}^\\circ = {correct_ans}^\\circ \\text{{ [}}\\angle\\text{{s on a straight line]}}$$"
    )
    ans = f"1. Subtracted from 90° instead of 180°; 2. x = {correct_ans}° [∠s on straight line]"
    return {
        "id": f"g7_line_43_{rng.randint(100000, 999999)}",
        "subskill": "43_spot_the_error_angle_on_straight_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_43",
        "hints": {
            "tier_1": "Does a straight line equal 90° or 180°?",
            "tier_2": "The learner used 90° instead of 180°.",
            "tier_3": f"Correct x = {correct_ans}°."
        },
        "misconception_tags": ["complementary_supplementary_confusion"]
    }


# 44. Spot the error vertically opposite reason
def arch_44_spot_the_error_vertically_opposite_reason(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([45, 55, 65, 75])
    wrong = 180 - angle
    prompt = (
        f"Two intersecting lines form opposite angles $x$ and {angle}°.\n"
        f"A learner wrote: '$$x = 180^\\circ - {angle}^\\circ = {wrong}^\\circ$$ because opposite angles add up to 180°.'\n\n"
        f"1. Explain what error the learner made.\n"
        f"2. State the true value of $x$ and the correct geometric rule."
    )
    sol = (
        f"**Step 1:** The learner treated vertically opposite angles as supplementary instead of recognizing they are equal.\n\n"
        f"**Step 2:** Vertically opposite angles are equal [$\\text{{vert opp }}\\angle\\text{{s}}$], so:\n"
        f"$$x = {angle}^\\circ$$"
    )
    ans = f"1. Vertically opposite angles are equal, not supplementary; 2. x = {angle}° [vert opp ∠s]"
    return {
        "id": f"g7_line_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spot_the_error_vertically_opposite_reason",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_44",
        "hints": {
            "tier_1": "Are opposite angles equal or supplementary?",
            "tier_2": "Opposite angles are equal.",
            "tier_3": f"x = {angle}°."
        },
        "misconception_tags": ["vertically_opposite_supplementary_fallacy"]
    }


# 45. Spot the error parallel line angle assumption
def arch_45_spot_the_error_parallel_line_angle_assumption(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a test question, two lines look parallel, but neither arrow symbols ($//$) nor a statement that the lines are parallel "
        "is provided. A learner states: '$x = 60^\\circ$ because alternate angles are equal.'\n\n"
        "Explain why the learner's mark was withheld according to geometric proof standards."
    )
    sol = (
        "**Answer:** Alternate angles are only equal if the lines are confirmed to be parallel. "
        "Lines cannot be assumed to be parallel based merely on appearance; they must either have matching arrow symbols "
        "or be explicitly stated as parallel in the question premise."
    )
    ans = "We cannot assume lines are parallel based only on appearances without arrow markings or given statements."
    return {
        "id": f"g7_line_45_{rng.randint(100000, 999999)}",
        "subskill": "45_spot_the_error_parallel_line_angle_assumption",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_45",
        "hints": {
            "tier_1": "Can you trust that lines are parallel just because they look parallel?",
            "tier_2": "Parallel status must be proven or given by arrows.",
            "tier_3": "Lines must be given as parallel before applying parallel line theorems."
        },
        "misconception_tags": ["visual_assumption_of_parallelism"]
    }


# 46. Practical context clock hands straight angle
def arch_46_practical_context_clock_hands_straight_angle(rng: random.Random) -> Dict[str, Any]:
    hour = rng.choice([6, 12])
    if hour == 6:
        prompt = (
            "At exactly 06:00, the hour hand of a standard analog clock points directly down to 6, "
            "and the minute hand points directly up to 12.\n\n"
            "1. What geometric figure is formed by the two clock hands?\n"
            "2. What is the angle in degrees between the two hands?"
        )
        sol = (
            "**Step 1:** At 06:00, the two hands form a continuous straight line (or two opposite rays).\n\n"
            "**Step 2:** The angle between them is a straight angle, which measures **$180^\\circ$**."
        )
        ans = "1. Straight line (or opposite rays); 2. 180°"
    else:
        prompt = (
            "At exactly 03:00, the hour hand points at 3 and the minute hand points at 12.\n\n"
            "1. What is the relationship between the lines formed by the two clock hands?\n"
            "2. What is the angle size in degrees?"
        )
        sol = (
            "**Step 1:** The two hands meet at a right angle, meaning they are **perpendicular**.\n\n"
            "**Step 2:** The angle size is **$90^\\circ$**."
        )
        ans = "1. Perpendicular; 2. 90°"
    return {
        "id": f"g7_line_46_{rng.randint(100000, 999999)}",
        "subskill": "46_practical_context_clock_hands_straight_angle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_46",
        "hints": {
            "tier_1": "Think about whether the hands make a straight line or an L-shape.",
            "tier_2": "A straight angle is 180°; a right angle is 90°.",
            "tier_3": ans
        },
        "misconception_tags": ["clock_angle_miscalculation"]
    }


# 47. Practical context road intersection angles
def arch_47_practical_context_road_intersection_angles(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([68, 72, 76, 84])
    adj = 180 - angle
    prompt = (
        f"Two straight streets in a town intersect. One corner of the intersection forms an acute angle of {angle}°.\n\n"
        f"1. What is the angle of the street corner directly opposite to it across the intersection?\n"
        f"2. What is the angle of the adjacent street corner along the same road?"
    )
    sol = (
        f"**Step 1:** The directly opposite corner is vertically opposite, so it measures **{angle}°** [vert opp ∠s].\n\n"
        f"**Step 2:** The adjacent corner along the straight road adds to 180°:\n"
        f"$$180^\\circ - {angle}^\\circ = {adj}^\\circ \\text{{ [}}\\angle\\text{{s on a straight line]}}$$"
    )
    ans = f"1. {angle}°; 2. {adj}°"
    return {
        "id": f"g7_line_47_{rng.randint(100000, 999999)}",
        "subskill": "47_practical_context_road_intersection_angles",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_47",
        "hints": {
            "tier_1": "Opposite corners are equal; adjacent corners add to 180°.",
            "tier_2": f"Opposite = {angle}°, adjacent = 180 - {angle}.",
            "tier_3": f"1. {angle}°, 2. {adj}°."
        },
        "misconception_tags": ["practical_intersection_angle_confusion"]
    }


# 48. Practical context railway tracks and switch transversal
def arch_48_practical_context_railway_tracks_and_switch_transversal(rng: random.Random) -> Dict[str, Any]:
    switch_ang = rng.choice([25, 30, 35, 40])
    prompt = (
        f"A railway switch track crosses two parallel mainline rails at an angle of {switch_ang}° to the first rail.\n\n"
        f"1. What mathematical role does the switch track play relative to the two parallel rails?\n"
        f"2. What is the alternate angle that the switch track makes with the second rail?"
    )
    sol = (
        f"**Step 1:** The switch track cuts across two parallel lines, making it a **transversal**.\n\n"
        f"**Step 2:** By alternate interior angles on parallel lines, the alternate angle is equal to **{switch_ang}°**."
    )
    ans = f"1. Transversal; 2. {switch_ang}°"
    return {
        "id": f"g7_line_48_{rng.randint(100000, 999999)}",
        "subskill": "48_practical_context_railway_tracks_and_switch_transversal",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_48",
        "hints": {
            "tier_1": "A line crossing parallel rails is a transversal.",
            "tier_2": "Alternate angles on parallel rails are equal.",
            "tier_3": f"1. Transversal, 2. {switch_ang}°."
        },
        "misconception_tags": ["practical_parallel_rail_error"]
    }


# 49. Practical context roof truss parallel chords
def arch_49_practical_context_roof_truss_parallel_chords(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([48, 52, 58, 62])
    supp = 180 - angle
    prompt = (
        f"In a timber roof truss, the top chord and horizontal tie beam are reinforced by parallel struts.\n"
        f"A brace cutting across the parallel struts forms an interior angle of {angle}° with one strut.\n\n"
        f"Calculate the co-interior angle formed with the adjacent parallel strut, stating why."
    )
    sol = (
        f"**Step 1:** Co-interior angles between parallel struts are supplementary (sum to $180^\\circ$).\n\n"
        f"**Step 2:** Calculate the angle:\n"
        f"$$180^\\circ - {angle}^\\circ = {supp}^\\circ \\text{{ [co-int }}\\angle\\text{{s, struts parallel]}}$$"
    )
    ans = f"{supp}° [co-int ∠s, struts parallel]"
    return {
        "id": f"g7_line_49_{rng.randint(100000, 999999)}",
        "subskill": "49_practical_context_roof_truss_parallel_chords",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_geom_lines_49",
        "hints": {
            "tier_1": "Angles on the same side between parallel members are co-interior.",
            "tier_2": f"Subtract {angle} from 180.",
            "tier_3": f"{supp}°."
        },
        "misconception_tags": ["roof_truss_angle_calculation_error"]
    }


# 50. Comprehensive multi-angle proof and calculation
def arch_50_comprehensive_multi_angle_proof_and_calculation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([60, 65, 70, 75])
    b = 180 - a
    svg = _svg_wrap(
        f'<line x1="50" y1="70" x2="350" y2="70" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="3"/>'
        f'<path d="M190,65 L200,70 L190,75" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<path d="M190,165 L200,170 L190,175" fill="none" stroke="#0284c7" stroke-width="3"/>'
        f'<line x1="120" y1="20" x2="280" y2="220" stroke="#1e293b" stroke-width="3"/>'
        f'<text x="170" y="55" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563eb">{a}°</text>'
        f'<text x="210" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">w</text>'
        f'<text x="130" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">x</text>'
        f'<text x="260" y="160" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">y</text>'
        f'<text x="180" y="195" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">z</text>'
    )
    prompt = (
        f"In the diagram, line AB // CD intersected by transversal PQ. The given angle is {a}°.\n\n"
        f"Calculate the sizes of angles $w$, $x$, $y$, and $z$, giving the geometric reason for each."
    )
    sol = (
        f"**1.** $w = 180^\\circ - {a}^\\circ = {b}^\\circ$ [$\\angle\\text{{s on a straight line}}$]\n"
        f"**2.** $x = {a}^\\circ$ [$\\text{{vert opp }}\\angle\\text{{s}}$]\n"
        f"**3.** $y = {a}^\\circ$ [$\\text{{corr }}\\angle\\text{{s, AB // CD}}$]\n"
        f"**4.** $z = {b}^\\circ$ [$\\text{{alt }}\\angle\\text{{s, AB // CD}}$ or $\\text{{corr }}\\angle\\text{{s, AB // CD}}$]"
    )
    ans = f"w = {b}°, x = {a}°, y = {a}°, z = {b}°"
    return {
        "id": f"g7_line_50_{rng.randint(100000, 999999)}",
        "subskill": "50_comprehensive_multi_angle_proof_and_calculation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Straight Line", "body": f"w = 180° - {a}° = {b}° [∠s on straight line]."},
                {"title": "Vert Opp", "body": f"x = {a}° [vert opp ∠s]."},
                {"title": "Corr Angles", "body": f"y = {a}° [corr ∠s, AB // CD]."},
                {"title": "Alt Angles", "body": f"z = {b}° [alt ∠s, AB // CD]."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_geom_lines_50",
        "hints": {
            "tier_1": "Find w first with the straight line, then use parallel line rules for y and z.",
            "tier_2": f"w = {b}°, x = {a}°, y = {a}°, z = {b}°.",
            "tier_3": ans
        },
        "misconception_tags": ["comprehensive_angle_proof_reason_omission"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
