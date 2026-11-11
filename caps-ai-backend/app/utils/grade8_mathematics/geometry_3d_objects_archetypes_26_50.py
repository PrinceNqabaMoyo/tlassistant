"""Grade 8 Mathematics — Geometry of 3D Objects Archetypes 26 to 50.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/02. Geometry of 3D objects.md

Archetypes covering:
  - 26 to 30: Euler's formula applications (find vertices, find edges, non-polyhedra check, algebraic proofs for n-gon prisms and pyramids).
  - 31 to 40: Platonic solids (definition, tetrahedron, cube, octahedron, dodecahedron, icosahedron, why only 5 exist, dual polyhedra, applications).
  - 41 to 50: Nets of 3D objects (valid Latin cross, T-cross, invalid nets, opposite faces, triangular prism net, square pyramid net, cylinder/cone nets, truncated solids).

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _draw_cube_net_latin_cross_svg(side: int = 4, seed: int = 101) -> str:
    """Renders a 2D static SVG of a valid Latin cross net for a cube with face labels A-F."""
    rng = random.Random(seed)
    w, h = 320, 240
    sq = 45
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">\n'
        f'  <!-- 4 vertical squares in column at x=135 -->\n'
        f'  <rect x="135" y="15" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="157" y="43" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A</text>\n'
        f'  <rect x="135" y="60" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="157" y="88" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">B</text>\n'
        f'  <rect x="135" y="105" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="157" y="133" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">C</text>\n'
        f'  <rect x="135" y="150" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="157" y="178" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">D</text>\n'
        f'  <!-- 2 flanking squares at y=60 (left x=90, right x=180) -->\n'
        f'  <rect x="90" y="60" width="{sq}" height="{sq}" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="112" y="88" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">E</text>\n'
        f'  <rect x="180" y="60" width="{sq}" height="{sq}" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="202" y="88" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">F</text>\n'
        f'  <text x="160" y="220" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Cube Net (side = {side} cm)</text>\n'
        f'</svg>'
    )


def _draw_cube_net_t_cross_svg(side: int = 4, seed: int = 101) -> str:
    """Renders a 2D static SVG of a valid T-cross net for a cube."""
    w, h = 320, 240
    sq = 45
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">\n'
        f'  <rect x="135" y="15" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <rect x="90" y="60" width="{sq}" height="{sq}" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <rect x="135" y="60" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <rect x="180" y="60" width="{sq}" height="{sq}" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <rect x="225" y="60" width="{sq}" height="{sq}" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <rect x="135" y="105" width="{sq}" height="{sq}" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>\n'
        f'  <text x="160" y="200" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Valid T-Pattern Cube Net (edge = {side} cm)</text>\n'
        f'</svg>'
    )


def _draw_cube_net_invalid_five_row_svg(side: int = 4, seed: int = 101) -> str:
    """Renders a 2D static SVG of an invalid cube net with 5 squares in a single row."""
    w, h = 340, 160
    sq = 45
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">\n'
        f'  <rect x="40" y="50" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <rect x="85" y="50" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <rect x="130" y="50" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <rect x="175" y="50" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <rect x="220" y="50" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <rect x="130" y="5" width="{sq}" height="{sq}" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>\n'
        f'  <text x="170" y="135" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Invalid Net (5 squares in a row, edge = {side} cm)</text>\n'
        f'</svg>'
    )


def _draw_triangular_prism_net_svg(b: int = 3, h_val: int = 5, seed: int = 101) -> str:
    """Renders a 2D static SVG of a triangular prism net (3 rectangles + 2 triangles)."""
    w, h = 320, 220
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">\n'
        f'  <rect x="110" y="20" width="100" height="45" fill="#f8fafc" stroke="#334155" stroke-width="1.5"/>\n'
        f'  <rect x="110" y="65" width="100" height="45" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>\n'
        f'  <rect x="110" y="110" width="100" height="45" fill="#f8fafc" stroke="#334155" stroke-width="1.5"/>\n'
        f'  <polygon points="110,65 50,87 110,110" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>\n'
        f'  <polygon points="210,65 270,87 210,110" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>\n'
        f'  <text x="160" y="195" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Triangular Prism Net (base={b} cm, height={h_val} cm)</text>\n'
        f'</svg>'
    )


def _draw_square_pyramid_net_svg(base_side: int = 4, slant: int = 5, seed: int = 101) -> str:
    """Renders a 2D static SVG of a square pyramid net (1 square + 4 triangles)."""
    w, h = 300, 240
    cx, cy = 150, 110
    s = 50
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:sans-serif;">\n'
        f'  <rect x="{cx - s/2}" y="{cy - s/2}" width="{s}" height="{s}" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>\n'
        f'  <polygon points="{cx - s/2},{cy - s/2} {cx + s/2},{cy - s/2} {cx},{cy - s/2 - 45}" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>\n'
        f'  <polygon points="{cx - s/2},{cy + s/2} {cx + s/2},{cy + s/2} {cx},{cy + s/2 + 45}" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>\n'
        f'  <polygon points="{cx - s/2},{cy - s/2} {cx - s/2},{cy + s/2} {cx - s/2 - 45},{cy}" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>\n'
        f'  <polygon points="{cx + s/2},{cy - s/2} {cx + s/2},{cy + s/2} {cx + s/2 + 45},{cy}" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>\n'
        f'  <text x="150" y="220" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Square Pyramid Net (base = {base_side} cm, slant = {slant} cm)</text>\n'
        f'</svg>'
    )


# ----------------------------------------------------------------------
# 26. Euler's Formula: Find Vertices Given Faces and Edges
# ----------------------------------------------------------------------
def arch_26_eulers_formula_find_vertices_given_faces_and_edges(rng: random.Random) -> Dict[str, Any]:
    f, e, name = rng.choice([
        (6, 12, "octahedron"),
        (8, 12, "hexahedron / cube"),
        (7, 12, "hexagonal pyramid"),
        (8, 18, "hexagonal prism"),
        (12, 30, "icosahedron"),
    ])
    v = e - f + 2

    prompt = (
        f"A closed polyhedron has **\\(F = {f}\\)** faces and **\\(E = {e}\\)** edges.\n\n"
        f"1. Rearrange Euler's Formula \\(F + V - E = 2\\) to express \\(V\\) as the subject.\n"
        f"2. Calculate the number of vertices (\\(V\\)) of this polyhedron."
    )
    sol = (
        f"**1. Subject formula:**\n"
        f"\\[ V = E - F + 2 \\]\n\n"
        f"**2. Calculation:**\n"
        f"\\[ V = {e} - {f} + 2 = {e - f} + 2 = {v} \\]\n"
        f"The polyhedron has **{v}** vertices."
    )
    ans = f"1. V = E - F + 2; 2. V = {v}"
    return {
        "id": f"g8_3d_find_v_{rng.randint(100000, 999999)}",
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
        "subskill": "26_eulers_formula_find_vertices_given_faces_and_edges",
        "learning_objective_id": "math_g8_3d_find_v",
        "hints": {
            "tier_1": "V = E - F + 2.",
            "tier_2": f"V = {e} - {f} + 2.",
            "tier_3": f"V = {v}.",
        },
        "misconception_tags": ["subtracting_e_instead_of_f_when_rearranging"],
    }


# ----------------------------------------------------------------------
# 27. Euler's Formula: Find Edges Given Faces and Vertices
# ----------------------------------------------------------------------
def arch_27_eulers_formula_find_edges_given_faces_and_vertices(rng: random.Random) -> Dict[str, Any]:
    f, v, name = rng.choice([
        (5, 6, "triangular prism"),
        (5, 5, "square pyramid"),
        (6, 6, "pentagonal pyramid"),
        (7, 10, "pentagonal prism"),
        (12, 20, "dodecahedron"),
    ])
    e = f + v - 2

    prompt = (
        f"A polyhedron has **\\(F = {f}\\)** faces and **\\(V = {v}\\)** vertices.\n\n"
        f"1. Make \\(E\\) the subject of Euler's Formula \\(F + V - E = 2\\).\n"
        f"2. Calculate the number of edges (\\(E\\)) of this polyhedron."
    )
    sol = (
        f"**1. Subject formula:**\n"
        f"\\[ E = F + V - 2 \\]\n\n"
        f"**2. Calculation:**\n"
        f"\\[ E = {f} + {v} - 2 = {f + v} - 2 = {e} \\]\n"
        f"The polyhedron has **{e}** edges."
    )
    ans = f"1. E = F + V - 2; 2. E = {e}"
    return {
        "id": f"g8_3d_find_e_{rng.randint(100000, 999999)}",
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
        "subskill": "27_eulers_formula_find_edges_given_faces_and_vertices",
        "learning_objective_id": "math_g8_3d_find_e",
        "hints": {
            "tier_1": "E = F + V - 2.",
            "tier_2": f"E = {f} + {v} - 2.",
            "tier_3": f"E = {e}.",
        },
        "misconception_tags": ["adding_2_instead_of_subtracting_2_for_edges"],
    }


# ----------------------------------------------------------------------
# 28. Euler's Formula Non-Polyhedra Inapplicability
# ----------------------------------------------------------------------
def arch_28_eulers_formula_non_polyhedra_inapplicability(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["cylinder", "cone", "sphere"])
    prompt = (
        f"A learner attempts to apply Euler's Formula \\(F + V - E = 2\\) to a **{obj}**.\n\n"
        f"1. Can Euler's Formula for polyhedra be applied to a {obj}? Answer Yes or No.\n"
        f"2. Explain why Euler's Formula applies strictly to polyhedra and not curved surfaces."
    )
    sol = (
        f"**1. Applicability:** **No**.\n\n"
        f"**2. Explanation:** Euler's formula is strictly valid for convex **polyhedra** (3D objects bounded "
        f"exclusively by flat polygon faces and straight line edges). A {obj} contains curved surfaces and circular "
        f"edges, where vertices and edges are not defined in the Euclidean polyhedral sense."
    )
    ans = f"1. No; 2. Euler's formula applies only to polyhedra with flat faces and straight edges, not curved solids like a {obj}"
    return {
        "id": f"g8_3d_euler_inapp_{rng.randint(100000, 999999)}",
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
        "subskill": "28_eulers_formula_non_polyhedra_inapplicability",
        "learning_objective_id": "math_g8_3d_euler_inapp",
        "hints": {
            "tier_1": "Euler's formula only works for polyhedra.",
            "tier_2": f"A {obj} has curved surfaces, not polygonal flat faces.",
            "tier_3": ans,
        },
        "misconception_tags": ["applying_euler_formula_to_curved_solids"],
    }


# ----------------------------------------------------------------------
# 29. Euler's Formula Algebraic Proof for N-Gon Prism
# ----------------------------------------------------------------------
def arch_29_eulers_formula_algebraic_proof_n_gon_prism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Prove algebraically that Euler's Formula \\(F + V - E = 2\\) holds true for **any prism** "
        "having an \\(n\\)-sided polygon base:\n\n"
        "1. Write down the algebraic formulas for \\(F\\), \\(V\\), and \\(E\\) in terms of \\(n\\).\n"
        "2. Substitute these expressions into \\(F + V - E\\) and simplify."
    )
    sol = (
        "**1. Prism formulas in terms of \\(n\\):**\n"
        "- \\(F = n + 2\\)\n"
        "- \\(V = 2n\\)\n"
        "- \\(E = 3n\\)\n\n"
        "**2. Algebraic Proof:**\n"
        "\\[ F + V - E = (n + 2) + 2n - 3n \\]\n"
        "\\[ = (n + 2n - 3n) + 2 = 0 + 2 = 2 \\]\n"
        "Since the result is identically 2 for all \\(n \\ge 3\\), Euler's formula is proved for every prism."
    )
    ans = "1. F = n + 2, V = 2n, E = 3n; 2. (n+2) + 2n - 3n = 2"
    return {
        "id": f"g8_3d_proof_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "29_eulers_formula_algebraic_proof_n_gon_prism",
        "learning_objective_id": "math_g8_3d_proof_prism",
        "hints": {
            "tier_1": "Substitute F = n + 2, V = 2n, E = 3n into F + V - E.",
            "tier_2": "Combine like terms: n + 2n - 3n cancels out to 0.",
            "tier_3": "(n + 2) + 2n - 3n = 2.",
        },
        "misconception_tags": ["incorrectly_combining_algebraic_terms_in_proof"],
    }


# ----------------------------------------------------------------------
# 30. Euler's Formula Algebraic Proof for N-Gon Pyramid
# ----------------------------------------------------------------------
def arch_30_eulers_formula_algebraic_proof_n_gon_pyramid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Prove algebraically that Euler's Formula \\(F + V - E = 2\\) holds true for **any pyramid** "
        "with an \\(n\\)-sided polygon base:\n\n"
        "1. State \\(F\\), \\(V\\), and \\(E\\) in terms of \\(n\\).\n"
        "2. Substitute into \\(F + V - E\\) and show that the result equals 2."
    )
    sol = (
        "**1. Pyramid formulas in terms of \\(n\\):**\n"
        "- \\(F = n + 1\\)\n"
        "- \\(V = n + 1\\)\n"
        "- \\(E = 2n\\)\n\n"
        "**2. Algebraic Proof:**\n"
        "\\[ F + V - E = (n + 1) + (n + 1) - 2n \\]\n"
        "\\[ = 2n + 2 - 2n = 2 \\]\n"
        "The \\(2n\\) terms cancel, leaving identically 2 for all \\(n \\ge 3\\)."
    )
    ans = "1. F = n + 1, V = n + 1, E = 2n; 2. (n+1) + (n+1) - 2n = 2"
    return {
        "id": f"g8_3d_proof_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "30_eulers_formula_algebraic_proof_n_gon_pyramid",
        "learning_objective_id": "math_g8_3d_proof_pyr",
        "hints": {
            "tier_1": "F = n + 1, V = n + 1, E = 2n.",
            "tier_2": "(n + 1) + (n + 1) - 2n = 2n + 2 - 2n = 2.",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_the_constant_1_in_faces_and_vertices"],
    }


# ----------------------------------------------------------------------
# 31. Platonic Solids: Definition and Criteria
# ----------------------------------------------------------------------
def arch_31_platonic_solids_definition_and_criteria(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A **Platonic solid** (regular polyhedron) is a highly symmetric geometric solid:\n\n"
        "1. State the two specific mathematical criteria that must be satisfied for a solid to be a Platonic solid.\n"
        "2. How many Platonic solids exist in three-dimensional space?"
    )
    sol = (
        "**1. Two Criteria:**\n"
        "- All faces are **congruent regular polygons** (identical in size and shape with equal sides and equal angles).\n"
        "- The **exact same number of faces** meet at each vertex.\n\n"
        "**2. Total Count:** Exactly **5** Platonic solids exist."
    )
    ans = "1. all faces are congruent regular polygons and same number of faces meet at each vertex; 2. 5"
    return {
        "id": f"g8_3d_platonic_def_{rng.randint(100000, 999999)}",
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
        "subskill": "31_platonic_solids_definition_and_criteria",
        "learning_objective_id": "math_g8_3d_platonic_def",
        "hints": {
            "tier_1": "Faces must be regular polygons of the exact same size.",
            "tier_2": "There are exactly 5 Platonic solids.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_any_prism_is_a_platonic_solid"],
    }


# ----------------------------------------------------------------------
# 32. Platonic Solid: Regular Tetrahedron
# ----------------------------------------------------------------------
def arch_32_platonic_solid_regular_tetrahedron(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the **regular tetrahedron**:\n\n"
        "1. What 2D regular polygon forms all of its faces, and how many are there?\n"
        "2. State its values of \\(F\\), \\(V\\), and \\(E\\)."
    )
    sol = (
        "**1. Face Shape and Count:** \\(4\\) congruent **equilateral triangles**.\n\n"
        "**2. Properties:**\n"
        "- Faces: \\(F = 4\\)\n"
        "- Vertices: \\(V = 4\\) (3 faces meet at each vertex)\n"
        "- Edges: \\(E = 6\\)"
    )
    ans = "1. 4 equilateral triangles; 2. F = 4, V = 4, E = 6"
    return {
        "id": f"g8_3d_plat_tetra_{rng.randint(100000, 999999)}",
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
        "subskill": "32_platonic_solid_regular_tetrahedron",
        "learning_objective_id": "math_g8_3d_plat_tetra",
        "hints": {
            "tier_1": "'Tetra' means four.",
            "tier_2": "F = 4, V = 4, E = 6.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_tetrahedron_faces_are_right_angled_triangles"],
    }


# ----------------------------------------------------------------------
# 33. Platonic Solid: Cube (Regular Hexahedron)
# ----------------------------------------------------------------------
def arch_33_platonic_solid_cube_hexahedron(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the **regular hexahedron** (commonly known as a cube):\n\n"
        "1. What polygon forms its faces, and how many faces meet at each vertex?\n"
        "2. State its values of \\(F\\), \\(V\\), and \\(E\\)."
    )
    sol = (
        "**1. Face Shape:** Congruent **squares**. Exactly **3** square faces meet at each vertex.\n\n"
        "**2. Properties:**\n"
        "- Faces: \\(F = 6\\)\n"
        "- Vertices: \\(V = 8\\)\n"
        "- Edges: \\(E = 12\\)"
    )
    ans = "1. congruent squares (3 meet at each vertex); 2. F = 6, V = 8, E = 12"
    return {
        "id": f"g8_3d_plat_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "33_platonic_solid_cube_hexahedron",
        "learning_objective_id": "math_g8_3d_plat_cube",
        "hints": {
            "tier_1": "Hexahedron means 6 faces (squares).",
            "tier_2": "F = 6, V = 8, E = 12.",
            "tier_3": ans,
        },
        "misconception_tags": ["calling_a_cuboid_a_platonic_solid"],
    }


# ----------------------------------------------------------------------
# 34. Platonic Solid: Regular Octahedron
# ----------------------------------------------------------------------
def arch_34_platonic_solid_regular_octahedron(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the **regular octahedron**:\n\n"
        "1. Describe the shape of its faces and state how many faces meet at each vertex.\n"
        "2. State its values of \\(F\\), \\(V\\), and \\(E\\)."
    )
    sol = (
        "**1. Face Shape and Vertices:** \\(8\\) congruent **equilateral triangles**. Exactly **4** faces meet at each vertex.\n\n"
        "**2. Properties:**\n"
        "- Faces: \\(F = 8\\)\n"
        "- Vertices: \\(V = 6\\)\n"
        "- Edges: \\(E = 12\\)"
    )
    ans = "1. 8 equilateral triangles (4 meet at each vertex); 2. F = 8, V = 6, E = 12"
    return {
        "id": f"g8_3d_plat_octa_{rng.randint(100000, 999999)}",
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
        "subskill": "34_platonic_solid_regular_octahedron",
        "learning_objective_id": "math_g8_3d_plat_octa",
        "hints": {
            "tier_1": "'Octa' means 8 faces.",
            "tier_2": "F = 8, V = 6, E = 12.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_octahedron_with_eight_sided_prism"],
    }


# ----------------------------------------------------------------------
# 35. Platonic Solid: Regular Dodecahedron
# ----------------------------------------------------------------------
def arch_35_platonic_solid_regular_dodecahedron(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the **regular dodecahedron**:\n\n"
        "1. What polygon forms its faces, and how many faces does it possess?\n"
        "2. State its values of \\(V\\) and \\(E\\)."
    )
    sol = (
        "**1. Face Shape and Count:** \\(12\\) congruent **regular pentagons**.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 12\\)\n"
        "- Vertices: \\(V = 20\\) (\\(3\\) pentagons meet at each vertex)\n"
        "- Edges: \\(E = 30\\)"
    )
    ans = "1. 12 regular pentagons; 2. V = 20, E = 30"
    return {
        "id": f"g8_3d_plat_dodec_{rng.randint(100000, 999999)}",
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
        "subskill": "35_platonic_solid_regular_dodecahedron",
        "learning_objective_id": "math_g8_3d_plat_dodec",
        "hints": {
            "tier_1": "'Dodeca' means 12.",
            "tier_2": "Faces are pentagons; F = 12, V = 20, E = 30.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_dodecahedron_faces_are_hexagons"],
    }


# ----------------------------------------------------------------------
# 36. Platonic Solid: Regular Icosahedron
# ----------------------------------------------------------------------
def arch_36_platonic_solid_regular_icosahedron(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the **regular icosahedron**:\n\n"
        "1. Describe the shape of its faces and state how many faces meet at each vertex.\n"
        "2. State its values of \\(F\\), \\(V\\), and \\(E\\)."
    )
    sol = (
        "**1. Face Shape:** \\(20\\) congruent **equilateral triangles**. Exactly **5** triangles meet at each vertex.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 20\\)\n"
        "- Vertices: \\(V = 12\\)\n"
        "- Edges: \\(E = 30\\)"
    )
    ans = "1. 20 equilateral triangles (5 meet at each vertex); 2. F = 20, V = 12, E = 30"
    return {
        "id": f"g8_3d_plat_icos_{rng.randint(100000, 999999)}",
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
        "subskill": "36_platonic_solid_regular_icosahedron",
        "learning_objective_id": "math_g8_3d_plat_icos",
        "hints": {
            "tier_1": "'Icosa' means 20 faces.",
            "tier_2": "F = 20, V = 12, E = 30.",
            "tier_3": ans,
        },
        "misconception_tags": ["swapping_vertices_and_faces_between_dodecahedron_and_icosahedron"],
    }


# ----------------------------------------------------------------------
# 37. Why Only Five Platonic Solids Exist
# ----------------------------------------------------------------------
def arch_37_platonic_solids_why_only_five_exist(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In geometry, it is proven that only five Platonic solids can exist in 3D space.\n\n"
        "1. What condition regarding the sum of interior angles meeting at a vertex must be satisfied to form a 3D corner?\n"
        "2. Explain why regular hexagons cannot form a Platonic solid."
    )
    sol = (
        "**1. Angle Condition:** At least 3 faces must meet at a vertex, and the sum of their interior angles "
        "must be strictly **less than 360°** to fold up into three dimensions.\n\n"
        "**2. Hexagons:** The interior angle of a regular hexagon is **120°**. If 3 hexagons meet at a vertex:\n"
        "\\[ 3 \\times 120^\\circ = 360^\\circ \\]\n"
        "Since the angle sum is exactly 360°, the hexagons lie completely flat (forming a flat tessellation) "
        "and cannot fold up to form a 3D vertex."
    )
    ans = "1. sum of angles at vertex must be < 360°; 2. 3 x 120° = 360°, lying completely flat with no space to fold"
    return {
        "id": f"g8_3d_why_five_{rng.randint(100000, 999999)}",
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
        "subskill": "37_platonic_solids_why_only_five_exist",
        "learning_objective_id": "math_g8_3d_why_five",
        "hints": {
            "tier_1": "Angles at a 3D vertex must add up to less than 360°.",
            "tier_2": "3 hexagons have 3 x 120° = 360°, which lies completely flat.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_more_than_five_regular_polyhedra_exist"],
    }


# ----------------------------------------------------------------------
# 38. Platonic Solids Dual Polyhedra Pairs
# ----------------------------------------------------------------------
def arch_38_platonic_solids_dual_polyhedra_pairs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two polyhedra are called **duals** if connecting the centers of adjacent faces of one solid "
        "forms the vertices of the other solid.\n\n"
        "1. What is the dual polyhedron of a **cube**?\n"
        "2. What is the dual polyhedron of a **regular dodecahedron**?\n"
        "3. Which Platonic solid is **self-dual** (its dual is an identical solid)?"
    )
    sol = (
        "**1. Dual of a Cube:** The **regular octahedron** (a cube's 6 faces become an octahedron's 6 vertices).\n\n"
        "**2. Dual of a Dodecahedron:** The **regular icosahedron** (12 faces become 12 vertices).\n\n"
        "**3. Self-dual solid:** The **regular tetrahedron** (connecting the centers of its 4 triangular faces forms a smaller tetrahedron)."
    )
    ans = "1. regular octahedron; 2. regular icosahedron; 3. regular tetrahedron"
    return {
        "id": f"g8_3d_duals_{rng.randint(100000, 999999)}",
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
        "subskill": "38_platonic_solids_dual_polyhedra_pairs",
        "learning_objective_id": "math_g8_3d_duals",
        "hints": {
            "tier_1": "Faces of one solid match vertices of its dual.",
            "tier_2": "Cube (6 faces) <-> Octahedron (6 vertices).",
            "tier_3": "1. Octahedron; 2. Icosahedron; 3. Tetrahedron.",
        },
        "misconception_tags": ["thinking_the_cube_is_self_dual"],
    }


# ----------------------------------------------------------------------
# 39. Platonic Solids Euler Verification Table
# ----------------------------------------------------------------------
def arch_39_platonic_solids_euler_verification_table(rng: random.Random) -> Dict[str, Any]:
    solid, f, v, e = rng.choice([
        ("regular tetrahedron", 4, 4, 6),
        ("cube", 6, 8, 12),
        ("regular octahedron", 8, 6, 12),
        ("regular dodecahedron", 12, 20, 30),
        ("regular icosahedron", 20, 12, 30),
    ])

    prompt = (
        f"Consider the Platonic solid named the **{solid}**:\n\n"
        f"1. State its number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\)).\n"
        f"2. Calculate \\(F + V - E\\) to verify Euler's formula."
    )
    sol = (
        f"**1. Properties of {solid}:**\n"
        f"- \\(F = {f}\\)\n"
        "- \\(V = {v}\\)\n"
        f"- \\(E = {e}\\)\n\n"
        f"**2. Euler's Verification:**\n"
        f"\\[ F + V - E = {f} + {v} - {e} = {f + v} - {e} = 2 \\]"
    )
    ans = f"1. F = {f}, V = {v}, E = {e}; 2. {f} + {v} - {e} = 2"
    return {
        "id": f"g8_3d_plat_euler_{rng.randint(100000, 999999)}",
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
        "subskill": "39_platonic_solids_euler_verification_table",
        "learning_objective_id": "math_g8_3d_plat_euler",
        "hints": {
            "tier_1": f"Recall F, V, E for {solid}.",
            "tier_2": f"{f} + {v} - {e} must equal 2.",
            "tier_3": ans,
        },
        "misconception_tags": ["misremembering_edge_count_of_platonic_solids"],
    }


# ----------------------------------------------------------------------
# 40. Platonic Solids Real World Examples
# ----------------------------------------------------------------------
def arch_40_platonic_solids_real_world_examples(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Platonic solids appear across natural science, minerals, and recreational games:\n\n"
        "1. Give an example of a Platonic solid used in board games or gambling dice.\n"
        "2. Explain why Platonic solids are uniquely suited for fair multi-sided dice."
    )
    sol = (
        "**1. Examples:** A standard 6-sided die is a **cube**; 20-sided dice (d20) are **regular icosahedra**; "
        "8-sided dice (d8) are **regular octahedra**; 12-sided dice (d12) are **regular dodecahedra**.\n\n"
        "**2. Fair Dice Explanation:** Because Platonic solids are **isohedral (face-transitive)** with identical "
        "congruent faces and equal angles meeting at every vertex, each face has an exactly equal probability of landing face-up."
    )
    ans = "1. standard 6-sided cube or 20-sided icosahedron die; 2. all faces are congruent and symmetrically identical, giving equal probability"
    return {
        "id": f"g8_3d_plat_real_{rng.randint(100000, 999999)}",
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
        "subskill": "40_platonic_solids_real_world_examples",
        "learning_objective_id": "math_g8_3d_plat_real",
        "hints": {
            "tier_1": "Think of dice used in role-playing games.",
            "tier_2": "Because all faces are identical, every roll is equally likely (fair).",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_non_regular_solids_make_fair_dice"],
    }


# ----------------------------------------------------------------------
# 41. Valid Cube Net Latin Cross (WITH SVG)
# ----------------------------------------------------------------------
def arch_41_valid_cube_net_latin_cross_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.choice([3, 4, 5, 6])
    svg = _draw_cube_net_latin_cross_svg(side=side, seed=rng.randint(100, 999999))

    prompt = (
        f"A flat arrangement of 6 connected squares has side length **{side} cm**:\n\n"
        f"1. Explain why this Latin cross arrangement forms a valid net that folds into a closed cube.\n"
        f"2. Calculate the total surface area of the folded cube in cm²."
    )
    area = 6 * (side * side)
    sol = (
        f"**1. Validity Explanation:** The 4 vertical squares fold to form the 4 lateral sides, while the two "
        f"flanking horizontal squares fold over to form the top and bottom bases without overlapping.\n\n"
        f"**2. Total Surface Area:**\n"
        f"\\[ \\text{{Area of 1 face}} = {side} \\times {side} = {side * side} \\text{{ cm}}^2 \\]\n"
        f"\\[ \\text{{Total Area}} = 6 \\times {side * side} = {area} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. folds without overlap into 4 sides plus top and bottom; 2. {area} cm²"
    return {
        "id": f"g8_3d_net_latin_{rng.randint(100000, 999999)}",
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
        "subskill": "41_valid_cube_net_latin_cross_svg",
        "learning_objective_id": "math_g8_3d_net_latin",
        "hints": {
            "tier_1": "A cube has 6 identical square faces.",
            "tier_2": f"Area = 6 * ({side}²).",
            "tier_3": f"{area} cm².",
        },
        "misconception_tags": ["multiplying_by_4_instead_of_6_for_cube_surface_area"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Valid Cube Net T-Cross Pattern (WITH SVG)
# ----------------------------------------------------------------------
def arch_42_valid_cube_net_t_cross_pattern_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.choice([2, 4, 5])
    svg = _draw_cube_net_t_cross_svg(side=side, seed=rng.randint(100, 999999))

    prompt = (
        f"Consider a T-pattern arrangement of 6 connected squares with edge **{side} cm**:\n\n"
        f"1. How many total distinct valid net arrangements exist for a cube?\n"
        f"2. What is the total perimeter of a single face of this cube in cm?"
    )
    p_face = 4 * side
    sol = (
        f"**1. Total Distinct Cube Nets:** Exactly **11** unique valid hexomino nets exist for a cube.\n\n"
        f"**2. Face Perimeter:**\n"
        f"\\[ P = 4 \\times {side} = {p_face} \\text{{ cm}} \\]"
    )
    ans = f"1. 11; 2. {p_face} cm"
    return {
        "id": f"g8_3d_net_t_{rng.randint(100000, 999999)}",
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
        "subskill": "42_valid_cube_net_t_cross_pattern_svg",
        "learning_objective_id": "math_g8_3d_net_t",
        "hints": {
            "tier_1": "There are 11 mathematically distinct nets for a cube.",
            "tier_2": f"Perimeter of 1 square face is 4 * {side}.",
            "tier_3": f"11; {p_face} cm.",
        },
        "misconception_tags": ["thinking_only_one_or_two_cube_nets_exist"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 43. Invalid Cube Net Overlapping Faces (WITH SVG)
# ----------------------------------------------------------------------
def arch_43_invalid_cube_net_overlapping_faces_svg(rng: random.Random) -> Dict[str, Any]:
    side = rng.choice([3, 4, 6])
    svg = _draw_cube_net_invalid_five_row_svg(side=side, seed=rng.randint(100, 999999))

    prompt = (
        f"A learner proposes an arrangement containing 5 squares in a single horizontal row and 1 attached square:\n\n"
        f"1. Explain why this arrangement cannot fold into a cube.\n"
        f"2. What is the maximum number of squares in a row that a valid cube net may have?"
    )
    sol = (
        f"**1. Why Invalid:** A cube has only 4 lateral sides around its perimeter. Folding 5 squares in a row "
        f"causes the fifth square to overlap directly onto the first square, leaving one side of the cube completely open.\n\n"
        f"**2. Maximum Squares in a Row:** A valid cube net can have at most **4** squares in a straight row."
    )
    ans = "1. 5 squares in a row causes two faces to overlap leaving one side open; 2. 4"
    return {
        "id": f"g8_3d_net_invalid_{rng.randint(100000, 999999)}",
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
        "subskill": "43_invalid_cube_net_overlapping_faces_svg",
        "learning_objective_id": "math_g8_3d_net_invalid",
        "hints": {
            "tier_1": "A cube only needs 4 squares to wrap around.",
            "tier_2": "5 squares in a row will overlap.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_any_six_connected_squares_make_a_cube_net"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 44. Cube Net Opposite Faces Identification (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_44_cube_net_opposite_faces_identification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a standard Latin cross net of a cube, six square faces are labeled A, B, C, D in a vertical column "
        "and E, F flanking face B on the left and right:\n\n"
        "1. When folded into a cube, which face is directly opposite to face **B**?\n"
        "2. Which face is directly opposite to face **E**?"
    )
    sol = (
        "**1. Opposite Face B:** Face **D** (in a column of squares, faces separated by one square fold opposite each other: A is opposite C, and B is opposite D).\n\n"
        "**2. Opposite Face E:** Face **F** (the two flanking wings fold upwards to form opposite vertical walls)."
    )
    ans = "1. Face D; 2. Face F"
    return {
        "id": f"g8_3d_net_opp_{rng.randint(100000, 999999)}",
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
        "subskill": "44_cube_net_opposite_faces_identification",
        "learning_objective_id": "math_g8_3d_net_opp",
        "hints": {
            "tier_1": "Faces with one square between them in a strip end up opposite.",
            "tier_2": "B and D are separated by C; E and F are the two flanking wings.",
            "tier_3": "1. Face D; 2. Face F.",
        },
        "misconception_tags": ["pairing_adjacent_faces_as_opposite"],
    }


# ----------------------------------------------------------------------
# 45. Net of Triangular Prism Identification (WITH SVG)
# ----------------------------------------------------------------------
def arch_45_net_of_triangular_prism_identification_svg(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4])
    h_val = rng.choice([5, 6, 8])
    svg = _draw_triangular_prism_net_svg(b=b, h_val=h_val, seed=rng.randint(100, 999999))

    prompt = (
        f"A net of a solid consists of 3 rectangular faces and 2 triangular faces with base {b} cm and height {h_val} cm:\n\n"
        f"1. Name the 3D solid that folds from this net.\n"
        f"2. How many edges will the assembled solid have?"
    )
    sol = (
        f"**1. 3D Solid:** A **triangular prism**.\n\n"
        f"**2. Edge Count:** A triangular prism has \\(3 \\times 3 = 9\\) edges."
    )
    ans = "1. triangular prism; 2. 9"
    return {
        "id": f"g8_3d_net_tri_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "45_net_of_triangular_prism_identification_svg",
        "learning_objective_id": "math_g8_3d_net_tri_prism",
        "hints": {
            "tier_1": "3 rectangles + 2 triangles forms a triangular prism.",
            "tier_2": "A triangular prism has 9 edges.",
            "tier_3": "Triangular prism; 9 edges.",
        },
        "misconception_tags": ["confusing_triangular_prism_net_with_pyramid_net"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 46. Net of Square Pyramid Identification (WITH SVG)
# ----------------------------------------------------------------------
def arch_46_net_of_square_pyramid_identification_svg(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([4, 6])
    sl = rng.choice([5, 8])
    svg = _draw_square_pyramid_net_svg(base_side=b, slant=sl, seed=rng.randint(100, 999999))

    prompt = (
        f"A net consists of a central square of side **{b} cm** with 4 identical isosceles triangles "
        f"attached to each of its four edges:\n\n"
        f"1. Name the 3D object produced by folding this net.\n"
        f"2. How many vertices will the folded solid have?"
    )
    sol = (
        f"**1. 3D Object:** A **square-based pyramid**.\n\n"
        f"**2. Vertex Count:** The 4 base corners plus the single apex give **\\(5\\) vertices**."
    )
    ans = "1. square-based pyramid; 2. 5"
    return {
        "id": f"g8_3d_net_sq_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "46_net_of_square_pyramid_identification_svg",
        "learning_objective_id": "math_g8_3d_net_sq_pyr",
        "hints": {
            "tier_1": "1 square base and 4 triangles make a square pyramid.",
            "tier_2": "Square pyramid has 4 base vertices + 1 apex = 5.",
            "tier_3": "Square-based pyramid; 5 vertices.",
        },
        "misconception_tags": ["forgetting_apex_in_folded_pyramid_vertex_count"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Net of Cylinder Components (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_47_net_of_cylinder_components(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([3, 7, 10])
    h_val = rng.choice([10, 15, 20])

    prompt = (
        f"When a cylinder with base radius **\\(r = {r}\\) cm** and height **\\(h = {h_val}\\) cm** is unrolled into a flat net:\n\n"
        f"1. List all 2D shapes that comprise the complete net.\n"
        f"2. What dimensions (length and width) does the unrolled curved lateral surface form?"
    )
    sol = (
        f"**1. Net Components:** Two congruent **circles** (top and bottom bases) and one **rectangle** (curved surface).\n\n"
        f"**2. Rectangle Dimensions:**\n"
        f"- Length = circumference of the circular base = \\(2 \\pi r = 2 \\pi ({r}) = {2 * r} \\pi\\) cm.\n"
        f"- Width = height of cylinder = \\({h_val}\\) cm."
    )
    ans = f"1. 2 circles and 1 rectangle; 2. length = 2*pi*r ({2*r}*pi cm) and width = {h_val} cm"
    return {
        "id": f"g8_3d_net_cyl_{rng.randint(100000, 999999)}",
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
        "subskill": "47_net_of_cylinder_components",
        "learning_objective_id": "math_g8_3d_net_cyl",
        "hints": {
            "tier_1": "A cylinder net has 2 circles and a rectangle.",
            "tier_2": "The rectangle length equals the circumference of the circle: 2*pi*r.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_unrolled_cylinder_surface_is_a_circle"],
    }


# ----------------------------------------------------------------------
# 48. Net of Cone Components (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_48_net_of_cone_components(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When cutting along the slant height and base to unroll a right circular cone flat:\n\n"
        "1. What shape forms the flat base of the cone?\n"
        "2. What geometric shape forms the unrolled curved lateral surface of the cone?"
    )
    sol = (
        "**1. Base Shape:** A **circle**.\n\n"
        "**2. Lateral Surface Shape:** A **sector of a circle** (a wedge-shaped piece of a circle bounded by two radii and an arc)."
    )
    ans = "1. circle; 2. sector of a circle"
    return {
        "id": f"g8_3d_net_cone_{rng.randint(100000, 999999)}",
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
        "subskill": "48_net_of_cone_components",
        "learning_objective_id": "math_g8_3d_net_cone",
        "hints": {
            "tier_1": "The base is a circular disc.",
            "tier_2": "The curved side unrolls into a sector (pie slice) of a larger circle.",
            "tier_3": "Circle; sector of a circle.",
        },
        "misconception_tags": ["thinking_cone_lateral_net_is_a_triangle"],
    }


# ----------------------------------------------------------------------
# 49. Truncated Polyhedra: Cutting Corners of Cube (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_49_truncated_polyhedra_cutting_corners_of_cube(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A carpenter takes a solid wooden cube (6 square faces, 8 vertices) and saws off each of its **8 corners (vertices)** "
        "with small flat cuts:\n\n"
        "1. What shape do the 8 cut corners become on the new solid?\n"
        "2. What shape do the original 6 square faces become after their 4 corners are clipped?\n"
        "3. How many total faces does this truncated cube possess?"
    )
    sol = (
        "**1. Cut corners:** Slicing off each vertex creates a **triangle** (\\(8\\) equilateral triangles in total).\n\n"
        "**2. Original square faces:** Clipping all 4 corners of a square turns it into an **octagon** (\\(8\\)-sided polygon).\n\n"
        "**3. Total Faces:** \\(6\\) octagons + \\(8\\) triangles = **14 faces**."
    )
    ans = "1. triangles; 2. regular octagons; 3. 14 faces"
    return {
        "id": f"g8_3d_trunc_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "49_truncated_polyhedra_cutting_corners_of_cube",
        "learning_objective_id": "math_g8_3d_trunc_cube",
        "hints": {
            "tier_1": "Each sliced vertex becomes a triangle.",
            "tier_2": "Cutting 4 corners of a 4-sided square produces an 8-sided octagon.",
            "tier_3": "Triangles; octagons; 14 faces.",
        },
        "misconception_tags": ["assuming_corners_remain_vertices"],
    }


# ----------------------------------------------------------------------
# 50. 3D Spatial Reasoning Packaging Box Construction (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_50_3d_spatial_reasoning_packaging_box_construction(rng: random.Random) -> Dict[str, Any]:
    l_val = rng.choice([10, 15, 20])
    w_val = rng.choice([6, 8, 12])
    h_val = rng.choice([4, 5])

    prompt = (
        f"A packaging company manufactures a closed rectangular cardboard box with length **{l_val} cm**, "
        f"width **{w_val} cm**, and height **{h_val} cm**:\n\n"
        f"1. How many pairs of congruent opposite rectangular faces comprise the box?\n"
        f"2. Calculate the total surface area of cardboard needed for this box (excluding glue flaps) in cm²."
    )
    area = 2 * (l_val * w_val + l_val * h_val + w_val * h_val)
    sol = (
        f"**1. Opposite Face Pairs:** Exactly **3 pairs** (top/bottom, front/back, left/right).\n\n"
        f"**2. Total Surface Area:**\n"
        f"\\[ A = 2(lw + lh + wh) \\]\n"
        f"\\[ = 2({l_val} \\times {w_val} + {l_val} \\times {h_val} + {w_val} \\times {h_val}) \\]\n"
        f"\\[ = 2({l_val * w_val} + {l_val * h_val} + {w_val * h_val}) \\]\n"
        f"\\[ = 2({l_val * w_val + l_val * h_val + w_val * h_val}) = {area} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. 3 pairs; 2. {area} cm²"
    return {
        "id": f"g8_3d_box_pkg_{rng.randint(100000, 999999)}",
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
        "subskill": "50_3d_spatial_reasoning_packaging_box_construction",
        "learning_objective_id": "math_g8_3d_box_pkg",
        "hints": {
            "tier_1": "Surface area = 2(lw + lh + wh).",
            "tier_2": f"2({l_val * w_val} + {l_val * h_val} + {w_val * h_val}).",
            "tier_3": f"{area} cm².",
        },
        "misconception_tags": ["forgetting_to_multiply_by_2_for_each_pair_of_faces"],
    }
