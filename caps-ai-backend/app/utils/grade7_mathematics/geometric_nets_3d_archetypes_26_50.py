"""Grade 7 Mathematics - Geometry of 3D Objects: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Geometry of 3D objects.md
Focus: 2D Geometric nets (valid vs invalid, opposite faces), SVG diagrams of nets, surface area from nets, Platonic solids, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_cube_net_latin_cross(side: int = 4) -> str:
    """Return clean 2D static SVG diagram of a Latin cross net for a cube."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240" width="100%" height="220" style="background:#ffffff;">\n'
        '  <!-- 4 vertical squares in column at x=100 -->\n'
        '  <rect x="100" y="20" width="50" height="50" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="125" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A</text>\n'
        '  <rect x="100" y="70" width="50" height="50" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="125" y="100" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">B</text>\n'
        '  <rect x="100" y="120" width="50" height="50" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="125" y="150" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">C</text>\n'
        '  <rect x="100" y="170" width="50" height="50" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="125" y="200" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">D</text>\n'
        '  <!-- 2 flanking squares at y=70 (left x=50, right x=150) -->\n'
        '  <rect x="50" y="70" width="50" height="50" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="75" y="100" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">E</text>\n'
        '  <rect x="150" y="70" width="50" height="50" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        '  <text x="175" y="100" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">F</text>\n'
        f'  <text x="160" y="232" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Latin Cross Net (edge = {side} cm)</text>\n'
        '</svg>'
    )


def _svg_cube_net_invalid_five_row(side: int = 4) -> str:
    """Return clean 2D static SVG diagram of an invalid cube net with 5 squares in a row."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 140" width="100%" height="140" style="background:#ffffff;">\n'
        '  <!-- 5 horizontal squares in row -->\n'
        '  <rect x="20" y="30" width="50" height="50" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        '  <rect x="70" y="30" width="50" height="50" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        '  <rect x="120" y="30" width="50" height="50" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        '  <rect x="170" y="30" width="50" height="50" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        '  <rect x="220" y="30" width="50" height="50" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        '  <!-- 1 square above -->\n'
        '  <rect x="120" y="0" width="50" height="30" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <text x="170" y="115" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Proposed Net (edge = {side} cm)</text>\n'
        '</svg>'
    )


# 26. General pyramid formula for n-gon
def arch_26_general_pyramid_formula_for_n_gon(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = n + 1, Vertices = n + 1, Edges = 2n"
    prompt = (
        "For any pyramid with an \\(n\\)-sided polygon base:\n\n"
        "State general algebraic formulas in terms of \\(n\\) for:\n"
        "1. Number of faces (\\(F\\))\n"
        "2. Number of vertices (\\(V\\))\n"
        "3. Number of edges (\\(E\\))"
    )
    sol = (
        "**General Formulas for an \\(n\\)-gonal Pyramid:**\n"
        "1. **Faces:** \\(F = n + 1\\) (1 base + \\(n\\) triangular sides)\n"
        "2. **Vertices:** \\(V = n + 1\\) (\\(n\\) base corners + 1 apex)\n"
        "3. **Edges:** \\(E = 2n\\) (\\(n\\) base edges + \\(n\\) edges meeting at apex)\n\n"
        "*(Notice: \\(F + V - E = (n + 1) + (n + 1) - 2n = 2\\), satisfying Euler's formula!)*"
    )
    return {
        "id": f"g7_g3d_26_{rng.randint(100000, 999999)}",
        "subskill": "26_general_pyramid_formula_for_n_gon",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_g3d_26",
        "hints": {"tier_1": "Base has n sides. Plus 1 apex.", "tier_2": "F = n+1, V = n+1, E = 2n.", "tier_3": ans},
        "misconception_tags": ["pyramid_general_formula_error"]
    }


# 27. Valid cube net Latin cross SVG
def arch_27_valid_cube_net_latin_cross_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.randint(3, 9)
    ans = "Yes, it folds into a cube because 4 squares form the four lateral faces and the 2 flanking squares form the top and bottom bases."
    svg = _svg_cube_net_latin_cross(side)
    prompt = (
        f"Inspect the net of six squares (each of edge {side} cm) shown below:\n\n"
        "Will this flat net fold into a closed cube? Explain why or why not."
    )
    sol = (
        "**Conclusion:** **Yes**, this is the standard **Latin Cross** net of a cube.\n\n"
        "**Explanation:**\n"
        "- It contains exactly 6 congruent squares.\n"
        "- The 4 vertical squares (A, B, C, D) fold to wrap around the four sides of the cube.\n"
        "- The 2 side flaps (E and F) fold up to become the left and right faces without any overlap."
    )
    return {
        "id": f"g7_g3d_27_{rng.randint(100000, 999999)}",
        "subskill": "27_valid_cube_net_latin_cross_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_27",
        "hints": {"tier_1": "Visualize folding along the lines.", "tier_2": "The Latin cross is a valid cube net.", "tier_3": ans},
        "misconception_tags": ["misjudging_valid_cube_net_as_invalid"]
    }


# 28. Valid cube net step pattern SVG
def arch_28_valid_cube_net_step_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "11 distinct nets"
    prompt = (
        "How many distinct (non-congruent) valid nets can be formed by 6 connected squares to make a cube?"
    )
    sol = (
        "**Fact:**\n"
        "There are exactly **11 distinct valid nets** of a cube (known as hexomino nets).\n"
        "Any other arrangement of 6 squares will either overlap or fail to close the cube."
    )
    return {
        "id": f"g7_g3d_28_{rng.randint(100000, 999999)}",
        "subskill": "28_valid_cube_net_step_pattern_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_28",
        "hints": {"tier_1": "It is a standard geometric property of hexominoes.", "tier_2": "There are 11 valid nets.", "tier_3": ans},
        "misconception_tags": ["guessing_incorrect_number_of_cube_nets"]
    }


# 29. Invalid cube net overlapping faces SVG
def arch_29_invalid_cube_net_overlapping_faces_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "No, because two faces will overlap on the same side, leaving one face of the cube open."
    prompt = (
        "If a net has 6 squares, but both the top and bottom flaps are attached to the same side of a row of squares, "
        "will it fold into a closed cube? Explain."
    )
    sol = (
        "**Reasoning:**\n"
        "**No**, it will not form a closed cube.\n"
        "When folded, the two flaps attached to the same position will fold onto the exact same face (overlap), "
        "leaving the opposite side completely open."
    )
    return {
        "id": f"g7_g3d_29_{rng.randint(100000, 999999)}",
        "subskill": "29_invalid_cube_net_overlapping_faces_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_29",
        "hints": {"tier_1": "Will any faces overlap?", "tier_2": "Two faces overlap, so it cannot close.", "tier_3": ans},
        "misconception_tags": ["failing_to_detect_overlapping_faces_in_net"]
    }


# 30. Invalid cube net five in a row SVG
def arch_30_invalid_cube_net_five_in_a_row_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.randint(3, 9)
    ans = "No, a cube only has 4 lateral sides, so 5 squares in a straight row will overlap."
    svg = _svg_cube_net_invalid_five_row(side)
    prompt = (
        f"Inspect the proposed net (edge = {side} cm) below:\n\n"
        "Can this shape fold into a cube? Explain why or why not."
    )
    sol = (
        "**Reasoning:**\n"
        "**No**, it cannot fold into a cube.\n"
        "A cube only has 4 lateral faces around its perimeter. Having 5 squares in a row means the 5th square "
        "will fold over and overlap the 1st square, leaving one end of the cube with no face."
    )
    return {
        "id": f"g7_g3d_30_{rng.randint(100000, 999999)}",
        "subskill": "30_invalid_cube_net_five_in_a_row_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_30",
        "hints": {"tier_1": "A cube cannot have 5 squares wrapped around 4 sides.", "tier_2": "The 5th square overlaps.", "tier_3": ans},
        "misconception_tags": ["thinking_any_six_squares_form_a_cube_net"]
    }


# 31. Opposite faces in cube net
def arch_31_opposite_faces_in_cube_net(rng: random.Random) -> Dict[str, Any]:
    ans = "Face B is opposite Face D; Face A is opposite Face C; Face E is opposite Face F."
    prompt = (
        "In a Latin Cross net of a cube, the 4 squares in the central vertical column are labeled from top to bottom "
        "as A, B, C, D. The left flap attached to B is E, and the right flap attached to B is F.\n\n"
        "When folded into a cube, which face is opposite:\n"
        "1. Face A?\n"
        "2. Face B?\n"
        "3. Face E?"
    )
    sol = (
        "**Folding Analysis:**\n"
        "In a row or column of squares in a net, alternating squares become opposite faces:\n"
        "1. Opposite **Face A** is **Face C** (skipping B).\n"
        "2. Opposite **Face B** is **Face D** (skipping C).\n"
        "3. Opposite **Face E** is **Face F** (the two side wings fold up facing each other)."
    )
    return {
        "id": f"g7_g3d_31_{rng.randint(100000, 999999)}",
        "subskill": "31_opposite_faces_in_cube_net",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_g3d_31",
        "hints": {"tier_1": "Alternating squares in a strip fold to opposite sides.", "tier_2": "A opposite C, B opposite D, E opposite F.", "tier_3": ans},
        "misconception_tags": ["identifying_adjacent_faces_as_opposite"]
    }


# 32. Net of rectangular prism matching
def arch_32_net_of_rectangular_prism_matching(rng: random.Random) -> Dict[str, Any]:
    l, b, h = rng.randint(6, 10), rng.randint(4, 5), rng.randint(2, 3)
    ans = "Rectangular Prism"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="180" style="background:#ffffff;">'
        '<rect x="100" y="20" width="80" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="60" width="80" height="30" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="90" width="80" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="130" width="80" height="30" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="60" y="90" width="40" height="40" fill="#dbeafe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="180" y="90" width="40" height="40" fill="#dbeafe" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="140" y="185" text-anchor="middle" font-size="11" fill="#0f172a">Net ({l} cm × {b} cm × {h} cm)</text>'
        '</svg>'
    )
    prompt = (
        f"A 2D net consists of 6 rectangular faces arranged in three pairs of congruent rectangles ({l} cm, {b} cm, {h} cm).\n\n"
        "Name the 3D solid that will be formed when this net is folded."
    )
    sol = (
        "**Conclusion:**\n"
        "The solid formed is a **Rectangular Prism** (or cuboid)."
    )
    return {
        "id": f"g7_g3d_32_{rng.randint(100000, 999999)}",
        "subskill": "32_net_of_rectangular_prism_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_32",
        "hints": {"tier_1": "6 rectangular faces in 3 congruent pairs.", "tier_2": "Rectangular prism.", "tier_3": ans},
        "misconception_tags": ["confusing_rectangular_prism_net_with_triangular_prism"]
    }


# 33. Net of triangular prism matching
def arch_33_net_of_triangular_prism_matching(rng: random.Random) -> Dict[str, Any]:
    l, b = rng.randint(6, 12), rng.randint(3, 5)
    ans = "Triangular Prism"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="180" style="background:#ffffff;">'
        '<rect x="60" y="70" width="60" height="60" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>'
        '<rect x="120" y="70" width="60" height="60" fill="#c7d2fe" stroke="#4338ca" stroke-width="2"/>'
        '<rect x="180" y="70" width="60" height="60" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>'
        '<polygon points="120,70 180,70 150,25" fill="#ede9fe" stroke="#4338ca" stroke-width="2"/>'
        '<polygon points="120,130 180,130 150,175" fill="#ede9fe" stroke="#4338ca" stroke-width="2"/>'
        f'<text x="150" y="192" text-anchor="middle" font-size="11" fill="#0f172a">Length = {l} cm, Base = {b} cm</text>'
        '</svg>'
    )
    prompt = (
        f"A net is composed of two identical triangles (base {b} cm) and three rectangles (length {l} cm).\n\n"
        "What 3D shape does this net fold into?"
    )
    sol = (
        "**Analysis:**\n"
        "The two congruent triangles serve as the two parallel bases, and the three rectangles fold around "
        "to form the lateral sides of a **Triangular Prism**."
    )
    return {
        "id": f"g7_g3d_33_{rng.randint(100000, 999999)}",
        "subskill": "33_net_of_triangular_prism_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_33",
        "hints": {"tier_1": "2 triangles + 3 rectangles.", "tier_2": "Triangular prism.", "tier_3": ans},
        "misconception_tags": ["calling_triangular_prism_a_pyramid"]
    }


# 34. Net of square pyramid matching
def arch_34_net_of_square_pyramid_matching(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 10)
    ans = "Square-based Pyramid"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 220" width="100%" height="190" style="background:#ffffff;">'
        '<rect x="100" y="80" width="60" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,80 160,80 130,30" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,140 160,140 130,190" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,80 100,140 50,110" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="160,80 160,140 210,110" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        f'<text x="130" y="212" text-anchor="middle" font-size="11" fill="#0f172a">Square base = {s} cm</text>'
        '</svg>'
    )
    prompt = (
        f"A net has a square ({s} cm × {s} cm) in the centre with four isosceles triangles attached to each of its four edges.\n\n"
        "Identify the 3D solid that this net forms."
    )
    sol = (
        "**Analysis:**\n"
        "The central square is the base, and the four triangular flaps fold upward to meet at a single apex.\n"
        "This forms a **Square-based Pyramid**."
    )
    return {
        "id": f"g7_g3d_34_{rng.randint(100000, 999999)}",
        "subskill": "34_net_of_square_pyramid_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_34",
        "hints": {"tier_1": "Square base + 4 triangles meeting at apex.", "tier_2": "Square-based pyramid.", "tier_3": ans},
        "misconception_tags": ["confusing_square_pyramid_with_tetrahedron"]
    }


# 35. Net of tetrahedron matching
def arch_35_net_of_tetrahedron_matching(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 10)
    ans = "Tetrahedron (Triangular Pyramid)"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 200" width="100%" height="180" style="background:#ffffff;">'
        '<polygon points="130,30 70,140 190,140" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        '<polygon points="100,85 160,85 130,140" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="130" y="175" text-anchor="middle" font-size="11" fill="#0f172a">4 Equilateral Triangles (side = {s} cm)</text>'
        '</svg>'
    )
    prompt = (
        f"A net is made of 4 congruent equilateral triangles of side length {s} cm.\n\n"
        "Name the 3D solid formed when this net is assembled."
    )
    sol = (
        "**Conclusion:**\n"
        "The solid formed is a **Regular Tetrahedron** (or triangular-based pyramid)."
    )
    return {
        "id": f"g7_g3d_35_{rng.randint(100000, 999999)}",
        "subskill": "35_net_of_tetrahedron_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_35",
        "hints": {"tier_1": "4 equilateral triangles.", "tier_2": "Tetrahedron.", "tier_3": ans},
        "misconception_tags": ["calling_tetrahedron_a_triangular_prism"]
    }


# 36. Net of cylinder matching
def arch_36_cylinder_net_surface_area(rng: random.Random) -> Dict[str, Any]:
    ans = "1 rectangle (whose length equals circumference 2*pi*r) and 2 circles (bases)"
    prompt = (
        "Describe the shapes that make up the flat **net of a cylinder**."
    )
    sol = (
        "**Components of a Cylinder Net:**\n"
        "1. **One rectangle:** This forms the curved side surface when rolled up. Its length is equal to the circumference of the circular base (\\(2\\pi r\\)), and its width is the height of the cylinder (\\(h\\)).\n"
        "2. **Two circles:** These form the flat top and bottom circular bases."
    )
    return {
        "id": f"g7_g3d_36_{rng.randint(100000, 999999)}",
        "subskill": "36_cylinder_net_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_36",
        "hints": {"tier_1": "Unroll the curved surface of a can.", "tier_2": "1 rectangle + 2 circles.", "tier_3": ans},
        "misconception_tags": ["thinking_cylinder_side_unrolls_into_a_circle"]
    }


# 37. Net of cone matching
def arch_37_net_of_cone_matching(rng: random.Random) -> Dict[str, Any]:
    r = rng.randint(3, 8)
    ans = "1 circular base and 1 sector of a circle"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 180" width="100%" height="160" style="background:#ffffff;">'
        '<path d="M 100,90 L 180,40 A 90,90 0 0,1 180,140 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<circle cx="65" cy="90" r="30" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        f'<text x="130" y="168" text-anchor="middle" font-size="11" fill="#0f172a">Cone Net (radius r = {r} cm)</text>'
        '</svg>'
    )
    prompt = (
        f"What two 2D shapes constitute the net of a **Cone** with base radius {r} cm?"
    )
    sol = (
        "**Components of a Cone Net:**\n"
        "1. A **circle** (the flat base of the cone).\n"
        "2. A **sector of a circle** (a pie-slice shape that rolls up into the cone's slanting lateral surface)."
    )
    return {
        "id": f"g7_g3d_37_{rng.randint(100000, 999999)}",
        "subskill": "37_net_of_cone_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_37",
        "hints": {"tier_1": "1 circle + 1 sector.", "tier_2": "Sector of a circle.", "tier_3": ans},
        "misconception_tags": ["thinking_cone_side_is_a_triangle"]
    }


# 38. Surface area from net triangular prism
def arch_38_surface_area_from_net(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([8, 10, 12])
    tri_area = 12
    rect_sum = l * 6 + l * 5 + l * 5
    total_sa = 2 * tri_area + rect_sum
    ans = f"{total_sa} cm^2"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="180" style="background:#ffffff;">'
        '<rect x="60" y="70" width="60" height="60" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>'
        '<rect x="120" y="70" width="60" height="60" fill="#c7d2fe" stroke="#4338ca" stroke-width="2"/>'
        '<rect x="180" y="70" width="60" height="60" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>'
        '<polygon points="120,70 180,70 150,25" fill="#ede9fe" stroke="#4338ca" stroke-width="2"/>'
        '<polygon points="120,130 180,130 150,175" fill="#ede9fe" stroke="#4338ca" stroke-width="2"/>'
        f'<text x="150" y="192" text-anchor="middle" font-size="11" fill="#0f172a">Triangular Prism Net (length = {l} cm)</text>'
        '</svg>'
    )
    prompt = (
        "A flat net of a triangular prism has the following face dimensions:\n"
        "- Two triangular bases: each with base \\(6\\text{ cm}\\) and height \\(4\\text{ cm}\\)\n"
        f"- Three rectangular side faces measuring: \\({l}\\text{{ cm}} \\times 6\\text{{ cm}}\\), "
        f"\\({l}\\text{{ cm}} \\times 5\\text{{ cm}}\\), and \\({l}\\text{{ cm}} \\times 5\\text{{ cm}}\\)\n\n"
        "Calculate the total surface area directly from this net."
    )
    sol = (
        "**Step 1:** Calculate area of the 2 triangular faces:\n"
        "$$\\text{Area of 1 triangle} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 6 \\times 4 = 12\\text{ cm}^2$$\n"
        "$$\\text{Two triangles} = 2 \\times 12 = 24\\text{ cm}^2$$\n\n"
        "**Step 2:** Calculate area of the 3 rectangular faces:\n"
        f"- Rectangle 1: \\({l} \\times 6 = {l*6}\\text{{ cm}}^2\\)\n"
        f"- Rectangle 2: \\({l} \\times 5 = {l*5}\\text{{ cm}}^2\\)\n"
        f"- Rectangle 3: \\({l} \\times 5 = {l*5}\\text{{ cm}}^2\\)\n"
        f"$$\\text{{Sum of rectangles}} = {l*6} + {l*5} + {l*5} = {rect_sum}\\text{{ cm}}^2$$\n\n"
        "**Step 3:** Total Surface Area:\n"
        f"$$\\text{{Total SA}} = 24 + {rect_sum} = \\mathbf{{{total_sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_g3d_38_{rng.randint(100000, 999999)}",
        "subskill": "38_surface_area_from_net",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_g3d_38",
        "hints": {"tier_1": f"2 triangles = 24. 3 rectangles = {rect_sum}.", "tier_2": f"24 + {rect_sum} = {total_sa}.", "tier_3": ans},
        "misconception_tags": ["forgetting_half_in_triangle_area_calculation"]
    }


# 39. Surface area from net square pyramid
def arch_39_surface_area_from_net_square_pyramid(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([6, 8, 10])
    sh = rng.choice([8, 10, 12])
    base_a = s * s
    tri_a = (s * sh) // 2
    total_sa = base_a + 4 * tri_a
    ans = f"{total_sa} cm^2"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 220" width="100%" height="190" style="background:#ffffff;">'
        '<rect x="100" y="80" width="60" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,80 160,80 130,30" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,140 160,140 130,190" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="100,80 100,140 50,110" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        '<polygon points="160,80 160,140 210,110" fill="#fde68a" stroke="#d97706" stroke-width="2"/>'
        f'<text x="130" y="212" text-anchor="middle" font-size="11" fill="#0f172a">Base = {s} cm, Slant = {sh} cm</text>'
        '</svg>'
    )
    prompt = (
        "The net of a square-based pyramid consists of:\n"
        f"- One square base measuring \\({s}\\text{{ cm}} \\times {s}\\text{{ cm}}\\)\n"
        f"- Four congruent triangular flaps, each with base \\({s}\\text{{ cm}}\\) and slant height \\({sh}\\text{{ cm}}\\)\n\n"
        "Calculate the total surface area of the pyramid."
    )
    sol = (
        "**Step 1:** Base area:\n"
        f"$$\\text{{Base}} = {s} \\times {s} = {base_a}\\text{{ cm}}^2$$\n\n"
        "**Step 2:** Area of 4 triangular faces:\n"
        f"$$\\text{{Area of 1 triangle}} = \\frac{{1}}{{2}} \\times {s} \\times {sh} = {tri_a}\\text{{ cm}}^2$$\n"
        f"$$\\text{{Four triangles}} = 4 \\times {tri_a} = {4 * tri_a}\\text{{ cm}}^2$$\n\n"
        "**Step 3:** Total Surface Area:\n"
        f"$$\\text{{Total SA}} = {base_a} + {4 * tri_a} = \\mathbf{{{total_sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_g3d_39_{rng.randint(100000, 999999)}",
        "subskill": "39_surface_area_from_net_square_pyramid",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_g3d_39",
        "hints": {"tier_1": f"Base = {base_a}. 4 triangles = 4 × {tri_a} = {4*tri_a}.", "tier_2": f"{base_a} + {4*tri_a} = {total_sa}.", "tier_3": ans},
        "misconception_tags": ["pyramid_surface_area_triangle_sum_error"]
    }


# 40. Surface area from net cylinder numeric
def arch_40_surface_area_from_net_cylinder_numeric(rng: random.Random) -> Dict[str, Any]:
    h = rng.choice([8, 10, 12])
    curved = int(round(31.4 * h))
    bases = 157
    total_sa = curved + bases
    ans = f"{total_sa} cm^2"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 200" width="100%" height="180" style="background:#ffffff;">'
        '<circle cx="140" cy="35" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<rect x="70" y="65" width="140" height="65" fill="#e0f2fe" stroke="#2563eb" stroke-width="2"/>'
        '<circle cx="140" cy="160" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="140" y="102" text-anchor="middle" font-size="11" fill="#1e3a8a">31,4 cm × {h} cm</text>'
        '</svg>'
    )
    prompt = (
        f"The net of a cylinder consists of a rectangle measuring \\(31{{,}}4\\text{{ cm}} \\times {h}\\text{{ cm}}\\) "
        "and two circular bases each having an area of \\(78{,}5\\text{ cm}^2\\).\n\n"
        "Calculate the total surface area of the cylinder."
    )
    sol = (
        "**Step 1:** Curved surface area (rectangle):\n"
        f"$$\\text{{Curved Area}} = 31{{,}}4 \\times {h} = {curved}\\text{{ cm}}^2$$\n\n"
        "**Step 2:** Two circular bases:\n"
        "$$\\text{Bases Area} = 2 \\times 78{,}5 = 157\\text{ cm}^2$$\n\n"
        "**Step 3:** Total Surface Area:\n"
        f"$$\\text{{Total SA}} = {curved} + 157 = \\mathbf{{{total_sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_g3d_40_{rng.randint(100000, 999999)}",
        "subskill": "40_surface_area_from_net_cylinder_numeric",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_40",
        "hints": {"tier_1": f"Rectangle = {curved}. Two circles = 157.", "tier_2": f"{curved} + 157 = {total_sa}.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_include_both_circular_bases"]
    }


# 41. Platonic solids definition
def arch_41_platonic_solids_definition(rng: random.Random) -> Dict[str, Any]:
    ans = "Tetrahedron, Cube (Hexahedron), Octahedron, Dodecahedron, Icosahedron"
    prompt = (
        "Name all **five Platonic solids** (regular polyhedra whose faces are identical regular polygons)."
    )
    sol = (
        "**The Five Platonic Solids:**\n"
        "1. **Tetrahedron** (4 equilateral triangles)\n"
        "2. **Cube / Hexahedron** (6 squares)\n"
        "3. **Octahedron** (8 equilateral triangles)\n"
        "4. **Dodecahedron** (12 regular pentagons)\n"
        "5. **Icosahedron** (20 equilateral triangles)"
    )
    return {
        "id": f"g7_g3d_41_{rng.randint(100000, 999999)}",
        "subskill": "41_platonic_solids_definition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_41",
        "hints": {"tier_1": "4, 6, 8, 12, 20 faces.", "tier_2": "Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron.", "tier_3": ans},
        "misconception_tags": ["listing_pyramid_or_prism_as_platonic_solid"]
    }


# 42. Identifying 3D object from face description
def arch_42_identifying_3d_object_from_face_description(rng: random.Random) -> Dict[str, Any]:
    ans = "Square-based Pyramid"
    prompt = (
        "Identify the 3D solid from the riddle:\n\n"
        "\"I have exactly 5 faces. One of my faces is a square, and the other four are triangles. "
        "I have 5 vertices and 8 edges. What am I?\""
    )
    sol = (
        "**Answer:** **Square-based Pyramid** (or Square Pyramid).\n"
        "- 1 square base + 4 triangular faces = 5 faces\n"
        "- 4 base vertices + 1 apex = 5 vertices\n"
        "- 4 base edges + 4 slant edges = 8 edges."
    )
    return {
        "id": f"g7_g3d_42_{rng.randint(100000, 999999)}",
        "subskill": "42_identifying_3d_object_from_face_description",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_42",
        "hints": {"tier_1": "1 square + 4 triangles.", "tier_2": "Square-based pyramid.", "tier_3": ans},
        "misconception_tags": ["riddle_shape_identification_error"]
    }


# 43. Identifying 3D object from two hexagonal bases
def arch_43_identifying_3d_object_from_two_hexagonal_bases(rng: random.Random) -> Dict[str, Any]:
    ans = "Hexagonal Prism"
    prompt = (
        "A 3D solid has 2 parallel congruent hexagonal bases and 6 rectangular side faces.\n\n"
        "What is the name of this object?"
    )
    sol = (
        "**Answer:** **Hexagonal Prism**.\n"
        "A prism is named after the shape of its two identical parallel bases (here, hexagons)."
    )
    return {
        "id": f"g7_g3d_43_{rng.randint(100000, 999999)}",
        "subskill": "43_identifying_3d_object_from_two_hexagonal_bases",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_43",
        "hints": {"tier_1": "Two hexagonal bases means hexagonal prism.", "tier_2": "Hexagonal Prism.", "tier_3": ans},
        "misconception_tags": ["naming_prism_as_pyramid"]
    }


# 44. Common misconception confusing vertex and apex
def arch_44_common_misconception_confusing_vertex_and_apex(rng: random.Random) -> Dict[str, Any]:
    ans = "A vertex is any corner point where edges meet; an apex is the specific top vertex of a pyramid where all triangular faces meet."
    prompt = (
        "Explain the distinction between the terms **vertex** and **apex** in 3D geometry."
    )
    sol = (
        "**Distinction:**\n"
        "- A **vertex** is any point where two or more edges meet (corners of any polygon or polyhedron).\n"
        "- An **apex** is a specialized vertex: the topmost point of a pyramid (or cone) directly opposite the base, "
        "where all the triangular side faces intersect."
    )
    return {
        "id": f"g7_g3d_44_{rng.randint(100000, 999999)}",
        "subskill": "44_common_misconception_confusing_vertex_and_apex",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_44",
        "hints": {"tier_1": "All apexes are vertices, but not all vertices are apexes.", "tier_2": "Apex is the peak of a pyramid.", "tier_3": ans},
        "misconception_tags": ["confusing_vertex_and_apex_definitions"]
    }


# 45. Common misconception counting cylinder as polyhedron
def arch_45_common_misconception_counting_cylinder_as_polyhedron(rng: random.Random) -> Dict[str, Any]:
    ans = "False: A polyhedron must have only flat polygon faces; a cylinder has a curved surface."
    prompt = (
        "True or False: \"A cylinder is a type of prism because it has two parallel circular bases.\"\n\n"
        "State True or False and explain your reasoning."
    )
    sol = (
        "**Answer:** **False**.\n\n"
        "**Reasoning:**\n"
        "By mathematical definition, a **prism is a polyhedron**, meaning all its faces must be flat **polygons** (straight-sided shapes like triangles, rectangles, etc.).\n"
        "A circle is not a polygon (it has curved boundary), and a cylinder has a curved side surface, so it is classified as a curved solid, not a prism or polyhedron."
    )
    return {
        "id": f"g7_g3d_45_{rng.randint(100000, 999999)}",
        "subskill": "45_common_misconception_counting_cylinder_as_polyhedron",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_45",
        "hints": {"tier_1": "Can a prism have curved faces?", "tier_2": "False. Circles are not polygons.", "tier_3": ans},
        "misconception_tags": ["classifying_cylinder_as_prism"]
    }


# 46. Common misconception cube net six squares assumption
def arch_46_common_misconception_cube_net_six_squares_assumption(rng: random.Random) -> Dict[str, Any]:
    ans = "False: Out of 35 possible arrangements of 6 connected squares (hexominoes), only 11 can fold into a cube."
    prompt = (
        "A learner says: \"Any shape made of 6 connected squares will fold into a cube.\"\n\n"
        "Is the learner correct? Explain mathematically."
    )
    sol = (
        "**Answer:** **No (False)**.\n\n"
        "**Explanation:**\n"
        "There are 35 different arrangements of 6 connected squares (called hexominoes).\n"
        "However, only **11 of these arrangements** can fold into a closed 3D cube without overlapping faces."
    )
    return {
        "id": f"g7_g3d_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_misconception_cube_net_six_squares_assumption",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_46",
        "hints": {"tier_1": "Think of 6 squares in a straight row.", "tier_2": "Only 11 out of 35 arrangements fold into cubes.", "tier_3": ans},
        "misconception_tags": ["assuming_all_six_square_hexominoes_are_cube_nets"]
    }


# 47. Right prism vs oblique prism concept
def arch_47_right_prism_vs_oblique_prism_concept(rng: random.Random) -> Dict[str, Any]:
    ans = "In a right prism, the lateral faces are perpendicular (90 degrees) to the bases; in an oblique prism, the sides are slanted."
    prompt = (
        "What is the difference between a **right prism** and an **oblique prism**?"
    )
    sol = (
        "**Difference:**\n"
        "- In a **right prism**, the lateral edges and rectangular side faces meet the bases at right angles (\\(90^\\circ\\)).\n"
        "- In an **oblique prism**, the lateral edges are slanted (not perpendicular to the bases), so the side faces are parallelograms instead of rectangles."
    )
    return {
        "id": f"g7_g3d_47_{rng.randint(100000, 999999)}",
        "subskill": "47_right_prism_vs_oblique_prism_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_47",
        "hints": {"tier_1": "Right angle (90°) vs slanted.", "tier_2": "Right prism edges are perpendicular to base.", "tier_3": ans},
        "misconception_tags": ["oblique_prism_definition_error"]
    }


# 48. Cross sections of 3D solids
def arch_48_cross_sections_of_3d_solids(rng: random.Random) -> Dict[str, Any]:
    ans = "Square"
    prompt = (
        "If a cube is cut with a flat slice parallel to its base, what 2D geometric shape is the cross-section?"
    )
    sol = (
        "**Answer:** **Square**.\n"
        "Any cut through a prism parallel to its base produces a cross-section that is identical (congruent) to the base. "
        "Since the base of a cube is a square, the cross-section is a square."
    )
    return {
        "id": f"g7_g3d_48_{rng.randint(100000, 999999)}",
        "subskill": "48_cross_sections_of_3d_solids",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Square", "Rectangle", "Triangle", "Circle"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_48",
        "hints": {"tier_1": "Parallel to the base.", "tier_2": "A cross-section parallel to the base is identical to the base.", "tier_3": ans},
        "misconception_tags": ["cross_section_shape_misidentification"]
    }


# 49. Building 3D nets tabs and assembly
def arch_49_building_3d_nets_tabs_and_assembly(rng: random.Random) -> Dict[str, Any]:
    ans = "Tabs provide overlapping flaps where glue can be applied to join adjacent edges together."
    prompt = (
        "When drawing a net on cardboard to cut out and construct a physical 3D model, "
        "why must extra **tabs (flaps)** be included along some edges?"
    )
    sol = (
        "**Explanation:**\n"
        "Without tabs, adjacent edges would merely touch with no overlapping surface to apply adhesive.\n"
        "**Tabs** provide small flaps for applying glue or tape so that touching edges can be securely joined together."
    )
    return {
        "id": f"g7_g3d_49_{rng.randint(100000, 999999)}",
        "subskill": "49_building_3d_nets_tabs_and_assembly",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_49",
        "hints": {"tier_1": "How do you glue paper together?", "tier_2": "Tabs provide surface area for glue.", "tier_3": ans},
        "misconception_tags": ["counting_glue_tabs_as_part_of_surface_area"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_geometric_net_identification(rng: random.Random) -> Dict[str, Any]:
    ans = "a) F=5, V=6, E=9; b) Triangular Prism; c) F+V-E = 5+6-9 = 2; d) Total SA = 108 cm^2"
    prompt = (
        "**Grade 7 Geometry of 3D Objects Comprehensive Diagnostic Autopsy**\n\n"
        "A 3D polyhedron has 2 triangular faces and 3 rectangular faces.\n\n"
        "1. State the number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\)).\n"
        "2. Name this polyhedron.\n"
        "3. Verify Euler's formula (\\(F + V - E = 2\\)) for this solid.\n"
        "4. If each triangular face has area \\(12\\text{ cm}^2\\) and each of the three rectangular faces "
        "has area \\(28\\text{ cm}^2\\), calculate the total surface area."
    )
    sol = (
        "**Question 1:** \\(F = 5\\), \\(V = 6\\), \\(E = 9\\).\n\n"
        "**Question 2:** **Triangular Prism**.\n\n"
        "**Question 3:**\n"
        "$$F + V - E = 5 + 6 - 9 = 11 - 9 = \\mathbf{2}$$\n\n"
        "**Question 4:**\n"
        "$$\\text{Total SA} = 2(12) + 3(28) = 24 + 84 = \\mathbf{108}\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_g3d_50_{rng.randint(100000, 999999)}",
        "subskill": "50_geometric_net_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_g3d_50",
        "hints": {
            "tier_1": "1: F=5, V=6, E=9. 2: Triangular prism. 3: 5+6-9=2. 4: 2(12)+3(28).",
            "tier_2": "F=5, V=6, E=9, Triangular Prism, Euler holds, SA = 108 cm^2.",
            "tier_3": ans
        },
        "misconception_tags": [
            "triangular_prism_property_confusion",
            "eulers_formula_evaluation_error",
            "surface_area_net_multiplication_error"
        ]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
