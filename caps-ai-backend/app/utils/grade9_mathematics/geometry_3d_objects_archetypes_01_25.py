"""Grade 9 Mathematics — Geometry of 3D Objects Archetypes 01 to 25 (CAPS Term 4).
Classification of 3D Objects, Faces/Vertices/Edges, Prisms vs Pyramids, Platonic Solids, and Euler's Formula.
100% AST Pure: Python math and random only, zero LLM authority.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.geometry_3d_objects_svg import (
    draw_polyhedron_3d_svg,
    draw_3d_net_svg,
)


# -----------------------------------------------------------------------------
# Archetype 01: Classify Polyhedron vs Non-Polyhedron
# -----------------------------------------------------------------------------
def arch_01_classify_polyhedron_vs_non_polyhedron(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("cylinder", "Cylinder", "Non-polyhedron", "It has a curved lateral surface, whereas a polyhedron must have only flat polygonal faces."),
        ("cone", "Cone", "Non-polyhedron", "It has a curved lateral surface tapering to an apex, so it is not a polyhedron."),
        ("cube", "Cube (Hexahedron)", "Polyhedron", "All 6 of its faces are flat polygons (squares) with no curved surfaces."),
        ("triangular_prism", "Triangular Prism", "Polyhedron", "All 5 of its faces (2 triangles and 3 rectangles) are flat polygons."),
        ("square_pyramid", "Square-based Pyramid", "Polyhedron", "All 5 of its faces (1 square base and 4 triangles) are flat polygons."),
        ("octahedron", "Regular Octahedron", "Polyhedron", "All 8 of its faces are flat equilateral triangles."),
    ]
    solid_key, solid_name, classification, reason = rng.choice(choices)
    svg = draw_polyhedron_3d_svg(solid_key, seed=seed, title=solid_name)

    prompt = (
        f"Examine the 3D solid shown in the diagram ({solid_name}). "
        f"Classify whether this 3D solid is a 'Polyhedron' or a 'Non-polyhedron'."
    )
    sol = (
        f"Definition: A polyhedron is a three-dimensional object whose surface is formed exclusively "
        f"by flat polygonal faces (no curved surfaces).\n"
        f"For the {solid_name}: {reason}\n"
        f"Therefore, the object is classified as a **{classification}**."
    )

    return {
        "subskill": "01_classify_polyhedron_vs_non_polyhedron",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": classification,
        "expected_answer": classification,
        "sample_answer": f"{classification} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct classification: {classification}", "marks": 1},
            {"desc": "Provide geometric reason regarding flat faces vs curved surfaces", "marks": 1},
        ],
        "hints": [
            "A polyhedron has only flat polygon faces and straight edges.",
            "If an object has any curved surface (like a cylinder, cone, or sphere), it is a non-polyhedron.",
            f"The answer is {classification}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 02: Identify Faces, Vertices, Edges of a Cube / Rectangular Prism
# -----------------------------------------------------------------------------
def arch_02_identify_faces_vertices_edges_cube(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    solid_key = rng.choice(["cube", "rectangular_prism"])
    name = "cube" if solid_key == "cube" else "rectangular prism (cuboid)"

    svg = draw_polyhedron_3d_svg(solid_key, seed=seed, title=name.title())

    if target == "faces":
        ans = "6"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "8"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "12"
        q_target = "number of edges (E)"
    else:
        ans = "F = 6, V = 8, E = 12"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"Refer to the 3D solid shown in the diagram ({name}). "
        f"Determine the {q_target} for this polyhedron."
    )
    sol = (
        f"For a {name}:\n"
        f"• Faces (F): 6 flat quadrilateral faces (top, bottom, front, back, left, right).\n"
        f"• Vertices (V): 8 corner points where three edges meet.\n"
        f"• Edges (E): 12 straight line segments where two faces meet.\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "02_identify_faces_vertices_edges_cube",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A rectangular prism has 6 faces.",
            "It has 8 corners (vertices) and 12 straight edges.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 03: Faces, Vertices, Edges of a Triangular Prism
# -----------------------------------------------------------------------------
def arch_03_identify_faces_vertices_edges_triangular_prism(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("triangular_prism", seed=seed, title="Triangular Prism")

    if target == "faces":
        ans = "5"
        q_target = "total number of faces (F)"
    elif target == "vertices":
        ans = "6"
        q_target = "total number of vertices (V)"
    elif target == "edges":
        ans = "9"
        q_target = "total number of edges (E)"
    else:
        ans = "F = 5, V = 6, E = 9"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"Examine the triangular prism shown in the diagram. "
        f"Determine the {q_target}."
    )
    sol = (
        f"For a triangular prism:\n"
        f"• Bases: 2 parallel congruent triangular faces.\n"
        f"• Lateral faces: 3 rectangular faces connecting the corresponding sides.\n"
        f"• Total Faces (F) = 2 + 3 = 5 faces.\n"
        f"• Vertices (V) = 3 on top triangle + 3 on bottom triangle = 6 vertices.\n"
        f"• Edges (E) = 3 + 3 (on the triangles) + 3 (lateral edges) = 9 edges.\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "03_identify_faces_vertices_edges_triangular_prism",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A triangular prism has 2 triangular bases and 3 rectangular sides.",
            "Count: F = 2 + 3 = 5; V = 3 * 2 = 6; E = 3 * 3 = 9.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 04: Faces, Vertices, Edges of a Square-based Pyramid
# -----------------------------------------------------------------------------
def arch_04_identify_faces_vertices_edges_square_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Square-Based Pyramid")

    if target == "faces":
        ans = "5"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "5"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "8"
        q_target = "number of edges (E)"
    else:
        ans = "F = 5, V = 5, E = 8"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"Refer to the square-based pyramid shown in the diagram. "
        f"Determine the {q_target}."
    )
    sol = (
        f"For a square-based pyramid:\n"
        f"• Base: 1 flat square base.\n"
        f"• Lateral faces: 4 triangular faces meeting at the apex.\n"
        f"• Total Faces (F) = 1 + 4 = 5.\n"
        f"• Vertices (V) = 4 on the base + 1 apex = 5.\n"
        f"• Edges (E) = 4 base edges + 4 slant edges to the apex = 8.\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "04_identify_faces_vertices_edges_square_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A square pyramid has 1 square base and 4 triangular faces.",
            "Count: F = 1 + 4 = 5, V = 4 + 1 = 5, E = 4 + 4 = 8.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 05: Faces, Vertices, Edges of a Regular Tetrahedron
# -----------------------------------------------------------------------------
def arch_05_identify_faces_vertices_edges_tetrahedron(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("tetrahedron", seed=seed, title="Regular Tetrahedron")

    if target == "faces":
        ans = "4"
        q_target = "total number of faces (F)"
    elif target == "vertices":
        ans = "4"
        q_target = "total number of vertices (V)"
    elif target == "edges":
        ans = "6"
        q_target = "total number of edges (E)"
    else:
        ans = "F = 4, V = 4, E = 6"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"Examine the regular tetrahedron (triangular-based pyramid) shown in the diagram. "
        f"Determine the {q_target}."
    )
    sol = (
        f"A regular tetrahedron is a Platonic solid whose surface consists of 4 congruent equilateral triangles:\n"
        f"• Faces (F): 4 triangular faces (1 base + 3 lateral).\n"
        f"• Vertices (V): 3 at the triangular base + 1 apex = 4 vertices.\n"
        f"• Edges (E): 3 base edges + 3 lateral edges = 6 edges.\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "05_identify_faces_vertices_edges_tetrahedron",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A tetrahedron is a pyramid with a triangular base.",
            "All 4 faces are equilateral triangles.",
            f"F = 4, V = 4, E = 6. The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 06: Faces, Vertices, Edges of a Pentagonal Prism
# -----------------------------------------------------------------------------
def arch_06_identify_faces_vertices_edges_pentagonal_prism(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("cube", seed=seed, title="Pentagonal Prism")

    if target == "faces":
        ans = "7"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "10"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "15"
        q_target = "number of edges (E)"
    else:
        ans = "F = 7, V = 10, E = 15"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"A right prism has a pentagon ($5$-sided polygon) as its base. "
        f"Determine the {q_target} of this pentagonal prism."
    )
    sol = (
        f"For a prism with an $n$-sided base ($n = 5$ for a pentagon):\n"
        f"• Faces (F) = $n + 2 = 5 + 2 = 7$ (2 pentagonal bases + 5 rectangular faces).\n"
        f"• Vertices (V) = $2n = 2 \\times 5 = 10$ (5 on each base).\n"
        f"• Edges (E) = $3n = 3 \\times 5 = 15$ (5 top + 5 bottom + 5 vertical edges).\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "06_identify_faces_vertices_edges_pentagonal_prism",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "For an n-gonal prism: F = n + 2, V = 2n, E = 3n.",
            "Substitute n = 5 for a pentagonal prism.",
            f"F = 7, V = 10, E = 15. The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 07: Faces, Vertices, Edges of a Hexagonal Prism
# -----------------------------------------------------------------------------
def arch_07_identify_faces_vertices_edges_hexagonal_prism(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("hexagonal_prism", seed=seed, title="Hexagonal Prism")

    if target == "faces":
        ans = "8"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "12"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "18"
        q_target = "number of edges (E)"
    else:
        ans = "F = 8, V = 12, E = 18"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"Examine the hexagonal prism shown in the diagram. "
        f"Determine the {q_target} of this polyhedron."
    )
    sol = (
        f"For a hexagonal prism (base has $n = 6$ sides):\n"
        f"• Faces (F) = $n + 2 = 6 + 2 = 8$ (2 hexagonal bases + 6 rectangular sides).\n"
        f"• Vertices (V) = $2n = 2 \\times 6 = 12$ (6 on top hexagon + 6 on bottom hexagon).\n"
        f"• Edges (E) = $3n = 3 \\times 6 = 18$ (6 top + 6 bottom + 6 vertical).\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "07_identify_faces_vertices_edges_hexagonal_prism",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A hexagon has 6 sides (n = 6).",
            "Formula for prism: F = n + 2 = 8, V = 2n = 12, E = 3n = 18.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 08: Faces, Vertices, Edges of a Pentagonal Pyramid
# -----------------------------------------------------------------------------
def arch_08_identify_faces_vertices_edges_pentagonal_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Pentagonal Pyramid")

    if target == "faces":
        ans = "6"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "6"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "10"
        q_target = "number of edges (E)"
    else:
        ans = "F = 6, V = 6, E = 10"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"A pyramid has a pentagon ($5$-sided polygon) as its base. "
        f"Determine the {q_target} of this pentagonal pyramid."
    )
    sol = (
        f"For a pyramid with an $n$-sided base ($n = 5$ for a pentagon):\n"
        f"• Faces (F) = $n + 1 = 5 + 1 = 6$ (1 pentagonal base + 5 triangular faces).\n"
        f"• Vertices (V) = $n + 1 = 5 + 1 = 6$ (5 base vertices + 1 apex).\n"
        f"• Edges (E) = $2n = 2 \\times 5 = 10$ (5 base edges + 5 slant edges to the apex).\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "08_identify_faces_vertices_edges_pentagonal_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "For an n-gonal pyramid: F = n + 1, V = n + 1, E = 2n.",
            "Substitute n = 5 for a pentagonal pyramid.",
            f"F = 6, V = 6, E = 10. The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 09: Faces, Vertices, Edges of a Hexagonal Pyramid
# -----------------------------------------------------------------------------
def arch_09_identify_faces_vertices_edges_hexagonal_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges", "all"])
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Hexagonal Pyramid")

    if target == "faces":
        ans = "7"
        q_target = "number of faces (F)"
    elif target == "vertices":
        ans = "7"
        q_target = "number of vertices (V)"
    elif target == "edges":
        ans = "12"
        q_target = "number of edges (E)"
    else:
        ans = "F = 7, V = 7, E = 12"
        q_target = "number of faces (F), vertices (V), and edges (E)"

    prompt = (
        f"A pyramid has a hexagon ($6$-sided polygon) as its base. "
        f"Determine the {q_target} of this hexagonal pyramid."
    )
    sol = (
        f"For a pyramid with an $n$-sided base ($n = 6$ for a hexagon):\n"
        f"• Faces (F) = $n + 1 = 6 + 1 = 7$ (1 hexagonal base + 6 triangular faces).\n"
        f"• Vertices (V) = $n + 1 = 6 + 1 = 7$ (6 base corners + 1 apex).\n"
        f"• Edges (E) = $2n = 2 \\times 6 = 12$ (6 base edges + 6 slant edges).\n"
        f"Therefore, the {q_target} is {ans}."
    )

    return {
        "subskill": "09_identify_faces_vertices_edges_hexagonal_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "For an n-gonal pyramid: F = n + 1, V = n + 1, E = 2n.",
            "Substitute n = 6 for a hexagonal pyramid.",
            f"F = 7, V = 7, E = 12. The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 10: General Formula for n-gonal Prism
# -----------------------------------------------------------------------------
def arch_10_general_formula_n_gonal_prism(rng: random.Random, seed: int) -> Dict[str, Any]:
    n = rng.choice([7, 8, 9, 10, 12])
    target = rng.choice(["faces", "vertices", "edges"])

    if target == "faces":
        ans = str(n + 2)
        q_target = "number of faces (F)"
        formula = "n + 2"
    elif target == "vertices":
        ans = str(2 * n)
        q_target = "number of vertices (V)"
        formula = "2n"
    else:
        ans = str(3 * n)
        q_target = "number of edges (E)"
        formula = "3n"

    svg = draw_polyhedron_3d_svg("cube", seed=seed, title=f"{n}-Gonal Prism")

    prompt = (
        f"Consider a right prism whose base is a polygon with $n = {n}$ sides. "
        f"Using the general geometric formula for an $n$-gonal prism, calculate the total {q_target}."
    )
    sol = (
        f"For any prism with an $n$-sided base:\n"
        f"• Faces: $F = n + 2$\n"
        f"• Vertices: $V = 2n$\n"
        f"• Edges: $E = 3n$\n"
        f"Given $n = {n}$, the {q_target} is:\n"
        f"${formula} = {ans}$.\n"
        f"Therefore, the {q_target} is ${ans}$."
    )

    return {
        "subskill": "10_general_formula_n_gonal_prism",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula {formula}", "marks": 1},
            {"desc": f"Compute answer: {ans}", "marks": 1},
        ],
        "hints": [
            "For a prism: F = n + 2, V = 2n, E = 3n.",
            f"Here, n = {n}.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 11: General Formula for n-gonal Pyramid
# -----------------------------------------------------------------------------
def arch_11_general_formula_n_gonal_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    n = rng.choice([7, 8, 9, 10, 12])
    target = rng.choice(["faces", "vertices", "edges"])

    if target == "faces":
        ans = str(n + 1)
        q_target = "number of faces (F)"
        formula = "n + 1"
    elif target == "vertices":
        ans = str(n + 1)
        q_target = "number of vertices (V)"
        formula = "n + 1"
    else:
        ans = str(2 * n)
        q_target = "number of edges (E)"
        formula = "2n"

    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title=f"{n}-Gonal Pyramid")

    prompt = (
        f"Consider a pyramid whose base is a polygon with $n = {n}$ sides. "
        f"Using the general geometric formula for an $n$-gonal pyramid, calculate the total {q_target}."
    )
    sol = (
        f"For any pyramid with an $n$-sided base:\n"
        f"• Faces: $F = n + 1$\n"
        f"• Vertices: $V = n + 1$\n"
        f"• Edges: $E = 2n$\n"
        f"Given $n = {n}$, the {q_target} is:\n"
        f"${formula} = {ans}$.\n"
        f"Therefore, the {q_target} is ${ans}$."
    )

    return {
        "subskill": "11_general_formula_n_gonal_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula {formula}", "marks": 1},
            {"desc": f"Compute answer: {ans}", "marks": 1},
        ],
        "hints": [
            "For a pyramid: F = n + 1, V = n + 1, E = 2n.",
            f"Here, n = {n}.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 12: Distinguish Prism vs Pyramid
# -----------------------------------------------------------------------------
def arch_12_distinguish_prism_vs_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("How many parallel congruent bases does a prism have?", "2", "A prism always has exactly 2 parallel congruent bases."),
        ("What shape are the lateral faces of a right prism?", "Rectangles", "The lateral faces connecting the two parallel bases of a right prism are rectangles."),
        ("How many bases does a pyramid have?", "1", "A pyramid has exactly 1 polygonal base opposite a single apex vertex."),
        ("What shape are the lateral faces of a pyramid?", "Triangles", "The lateral faces of a pyramid are triangles that all meet at a common apex point."),
    ]
    q_text, ans, reason = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("triangular_prism", seed=seed, title="Prism vs Pyramid Properties")

    prompt = f"In 3D geometry, distinguishing between prisms and pyramids is fundamental. {q_text}"
    sol = f"{ans}.\nExplanation: {reason}"

    return {
        "subskill": "12_distinguish_prism_vs_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct answer: {ans}", "marks": 1},
            {"desc": "Provide geometric property explanation", "marks": 1},
        ],
        "hints": [
            "Prisms have 2 parallel bases and rectangular lateral faces.",
            "Pyramids have 1 base and triangular lateral faces meeting at an apex.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 13: Identification of the 5 Platonic Solids
# -----------------------------------------------------------------------------
def arch_13_platonic_solids_identification(rng: random.Random, seed: int) -> Dict[str, Any]:
    solids = [
        ("tetrahedron", "Tetrahedron", 4, "equilateral triangle"),
        ("cube", "Cube (Hexahedron)", 6, "square"),
        ("octahedron", "Octahedron", 8, "equilateral triangle"),
        ("dodecahedron", "Dodecahedron", 12, "regular pentagon"),
        ("icosahedron", "Icosahedron", 20, "equilateral triangle"),
    ]
    s_key, s_name, n_faces, f_shape = rng.choice(solids)
    svg = draw_polyhedron_3d_svg("octahedron" if s_key in ("octahedron", "dodecahedron", "icosahedron") else s_key, seed=seed, title=s_name)

    prompt = (
        f"A Platonic solid is a regular convex polyhedron whose faces are congruent regular polygons, "
        f"with the same number of faces meeting at each vertex. "
        f"Name the Platonic solid that has exactly {n_faces} faces."
    )
    sol = (
        f"The 5 Platonic solids and their face counts are:\n"
        f"1. Tetrahedron (4 faces)\n"
        f"2. Hexahedron / Cube (6 faces)\n"
        f"3. Octahedron (8 faces)\n"
        f"4. Dodecahedron (12 faces)\n"
        f"5. Icosahedron (20 faces)\n"
        f"Therefore, the Platonic solid with {n_faces} faces is the **{s_name}**."
    )

    return {
        "subskill": "13_platonic_solids_identification",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": s_name,
        "expected_answer": s_name,
        "sample_answer": s_name,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify correct Platonic solid: {s_name}", "marks": 2},
        ],
        "hints": [
            "Prefixes: tetra- (4), hexa- (6), octa- (8), dodeca- (12), icosa- (20).",
            f"The solid with {n_faces} faces is the {s_name}.",
            f"Answer: {s_name}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 14: Platonic Solids Face Polygon Shapes
# -----------------------------------------------------------------------------
def arch_14_platonic_solid_face_shapes(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("tetrahedron", "Tetrahedron", "Equilateral triangle", "4 equilateral triangles meet 3 at each vertex"),
        ("cube", "Cube (Hexahedron)", "Square", "6 squares meet 3 at each vertex"),
        ("octahedron", "Octahedron", "Equilateral triangle", "8 equilateral triangles meet 4 at each vertex"),
        ("dodecahedron", "Dodecahedron", "Regular pentagon", "12 regular pentagons meet 3 at each vertex"),
        ("icosahedron", "Icosahedron", "Equilateral triangle", "20 equilateral triangles meet 5 at each vertex"),
    ]
    s_key, s_name, face_shape, reason = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("octahedron" if "octa" in s_key or "icosa" in s_key else ("cube" if s_key == "cube" else "tetrahedron"), seed=seed, title=s_name)

    prompt = (
        f"Consider the Platonic solid: **{s_name}**. "
        f"What regular 2D polygon forms every face of this Platonic solid? "
        f"(Choose from: 'Equilateral triangle', 'Square', or 'Regular pentagon')."
    )
    sol = (
        f"In a {s_name}:\n"
        f"Every face is a congruent {face_shape}.\n"
        f"Details: {reason}.\n"
        f"Therefore, the face shape is **{face_shape}**."
    )

    return {
        "subskill": "14_platonic_solid_face_shapes",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": face_shape,
        "expected_answer": face_shape,
        "sample_answer": face_shape,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct face polygon: {face_shape}", "marks": 2},
        ],
        "hints": [
            "Three Platonic solids have triangular faces: tetrahedron, octahedron, icosahedron.",
            "The cube has squares, and the dodecahedron has pentagons.",
            f"For the {s_name}, each face is an {face_shape}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 15: Platonic Solids Faces Count
# -----------------------------------------------------------------------------
def arch_15_platonic_solids_faces_count(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Tetrahedron", 4),
        ("Cube (Hexahedron)", 6),
        ("Octahedron", 8),
        ("Dodecahedron", 12),
        ("Icosahedron", 20),
    ]
    name, faces = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("cube", seed=seed, title=name)

    prompt = f"State the exact number of faces that make up a regular **{name}**."
    sol = (
        f"The prefix indicates the face count:\n"
        f"A **{name}** has exactly ${faces}$ congruent faces.\n"
        f"Therefore, the number of faces is ${faces}$."
    )

    return {
        "subskill": "15_platonic_solids_faces_count",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(faces),
        "expected_answer": str(faces),
        "sample_answer": str(faces),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct face count: {faces}", "marks": 2},
        ],
        "hints": [
            f"Recall the Greek numerical prefix in '{name}'.",
            f"The answer is {faces}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 16: Vertices and Edges of Higher Platonic Solids
# -----------------------------------------------------------------------------
def arch_16_platonic_solid_vertices_edges(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Octahedron", "vertices", "6", "F = 8, E = 12, V = 6"),
        ("Octahedron", "edges", "12", "F = 8, V = 6, E = 12"),
        ("Dodecahedron", "vertices", "20", "F = 12, E = 30, V = 20"),
        ("Dodecahedron", "edges", "30", "F = 12, V = 20, E = 30"),
        ("Icosahedron", "vertices", "12", "F = 20, E = 30, V = 12"),
        ("Icosahedron", "edges", "30", "F = 20, V = 12, E = 30"),
    ]
    solid_name, param, ans, details = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("octahedron", seed=seed, title=solid_name)

    prompt = (
        f"Determine the number of **{param}** in a regular **{solid_name}**."
    )
    sol = (
        f"For a regular {solid_name}:\n"
        f"Parameters: {details}.\n"
        f"Euler's Formula check: $V - E + F = 2$.\n"
        f"Therefore, the number of {param} is **{ans}**."
    )

    return {
        "subskill": "16_platonic_solid_vertices_edges",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct {param} count: {ans}", "marks": 2},
        ],
        "hints": [
            f"Recall the F, V, E values for an {solid_name}.",
            f"Euler's formula: V - E + F = 2.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 17: Geometric Proof of Exactly 5 Platonic Solids
# -----------------------------------------------------------------------------
def arch_17_platonic_solids_vertex_angle_sum_proof(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("regular hexagons", 120, 3, 360, "Three regular hexagon angles sum to 3 × 120° = 360°. Since a 3D vertex requires the angle sum to be strictly less than 360°, three hexagons lie flat and cannot fold into a 3D corner."),
        ("regular octagons", 135, 3, 405, "Three regular octagon angles sum to 3 × 135° = 405°, which exceeds 360° and cannot form a vertex."),
    ]
    poly_name, interior_ang, n_meet, tot_ang, reason = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("cube", seed=seed, title="Platonic Solid Vertex Angle Constraint")

    prompt = (
        f"Why is it geometrically impossible to construct a regular Platonic solid whose faces are {poly_name}?\n"
        f"Calculate the sum of interior angles if {n_meet} {poly_name} meet at a single vertex (in degrees)."
    )
    sol = (
        f"1. Each interior angle of a {poly_name[:-1]} is ${interior_ang}^\\circ$.\n"
        f"2. At least {n_meet} faces must meet at a 3D vertex: ${n_meet} \\times {interior_ang}^\\circ = {tot_ang}^\\circ$.\n"
        f"3. For a polyhedron vertex to close into 3D space, the sum of angles meeting at each vertex must be strictly LESS than $360^\\circ$.\n"
        f"4. Because ${tot_ang}^\\circ \\ge 360^\\circ$, {reason}\n"
        f"Therefore, the angle sum is ${tot_ang}^\\circ$."
    )

    return {
        "subskill": "17_platonic_solids_vertex_angle_sum_proof",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(tot_ang),
        "expected_answer": str(tot_ang),
        "sample_answer": f"{tot_ang}° ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate angle sum at vertex: {tot_ang}°", "marks": 2},
            {"desc": "State condition that angle sum must be strictly < 360°", "marks": 1},
        ],
        "hints": [
            f"Multiply the interior angle ({interior_ang}°) by {n_meet}.",
            f"{n_meet} * {interior_ang}° = {tot_ang}°.",
            "Since this is >= 360°, the faces lie flat and cannot form a 3D vertex.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 18: Euler's Formula Verification for Prisms
# -----------------------------------------------------------------------------
def arch_18_euler_formula_verification_prisms(rng: random.Random, seed: int) -> Dict[str, Any]:
    prisms = [
        ("triangular prism", 3, 5, 6, 9),
        ("rectangular prism (cuboid)", 4, 6, 8, 12),
        ("pentagonal prism", 5, 7, 10, 15),
        ("hexagonal prism", 6, 8, 12, 18),
    ]
    name, n, f_val, v_val, e_val = rng.choice(prisms)
    svg = draw_polyhedron_3d_svg("triangular_prism" if n == 3 else ("hexagonal_prism" if n == 6 else "cube"), seed=seed, title=name.title())

    prompt = (
        f"Euler's formula states that for any convex polyhedron: $V - E + F = 2$.\n"
        f"Verify Euler's formula for a **{name}** by calculating the value of $V - E + F$."
    )
    sol = (
        f"For a {name}:\n"
        f"• Number of faces $F = {f_val}$\n"
        f"• Number of vertices $V = {v_val}$\n"
        f"• Number of edges $E = {e_val}$\n"
        f"Substituting into Euler's formula:\n"
        f"$V - E + F = {v_val} - {e_val} + {f_val} = {v_val - e_val} + {f_val} = 2$.\n"
        f"The formula is verified as $2 = 2$."
    )

    return {
        "subskill": "18_euler_formula_verification_prisms",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": "2",
        "expected_answer": "2",
        "sample_answer": f"V - E + F = {v_val} - {e_val} + {f_val} = 2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify F = {f_val}, V = {v_val}, E = {e_val}", "marks": 1},
            {"desc": "Substitute and evaluate to 2", "marks": 1},
        ],
        "hints": [
            f"For a {name}: F = {f_val}, V = {v_val}, E = {e_val}.",
            f"Compute V - E + F = {v_val} - {e_val} + {f_val}.",
            "Euler's formula always evaluates to 2.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 19: Euler's Formula Verification for Pyramids
# -----------------------------------------------------------------------------
def arch_19_euler_formula_verification_pyramids(rng: random.Random, seed: int) -> Dict[str, Any]:
    pyramids = [
        ("triangular pyramid (tetrahedron)", 3, 4, 4, 6),
        ("square-based pyramid", 4, 5, 5, 8),
        ("pentagonal pyramid", 5, 6, 6, 10),
        ("hexagonal pyramid", 6, 7, 7, 12),
    ]
    name, n, f_val, v_val, e_val = rng.choice(pyramids)
    svg = draw_polyhedron_3d_svg("square_pyramid" if n >= 4 else "tetrahedron", seed=seed, title=name.title())

    prompt = (
        f"Euler's formula states: $V - E + F = 2$.\n"
        f"Verify Euler's formula for a **{name}** by calculating $V - E + F$."
    )
    sol = (
        f"For a {name}:\n"
        f"• Number of faces $F = {f_val}$\n"
        f"• Number of vertices $V = {v_val}$\n"
        f"• Number of edges $E = {e_val}$\n"
        f"Substituting into Euler's formula:\n"
        f"$V - E + F = {v_val} - {e_val} + {f_val} = {v_val - e_val + f_val} = 2$.\n"
        f"The formula holds true."
    )

    return {
        "subskill": "19_euler_formula_verification_pyramids",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": "2",
        "expected_answer": "2",
        "sample_answer": f"V - E + F = {v_val} - {e_val} + {f_val} = 2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correctly identify F = {f_val}, V = {v_val}, E = {e_val}", "marks": 1},
            {"desc": "Evaluate V - E + F = 2", "marks": 1},
        ],
        "hints": [
            f"For a {name}: F = {f_val}, V = {v_val}, E = {e_val}.",
            f"V - E + F = {v_val} - {e_val} + {f_val}.",
            "The result is 2.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 20: Euler's Formula Verification for Platonic Solids
# -----------------------------------------------------------------------------
def arch_20_euler_formula_verification_platonic_solids(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Octahedron", 8, 6, 12),
        ("Dodecahedron", 12, 20, 30),
        ("Icosahedron", 20, 12, 30),
    ]
    name, f_val, v_val, e_val = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("octahedron", seed=seed, title=name)

    prompt = (
        f"A regular **{name}** has $F = {f_val}$ faces, $V = {v_val}$ vertices, and $E = {e_val}$ edges.\n"
        f"Substitute these values into Euler's formula $V - E + F$ and verify that the result equals $2$."
    )
    sol = (
        f"Euler's formula: $V - E + F = 2$.\n"
        f"Substitute the given parameters for the {name}:\n"
        f"$V - E + F = {v_val} - {e_val} + {f_val} = {v_val - e_val} + {f_val} = 2$.\n"
        f"This confirms Euler's formula holds for the {name}."
    )

    return {
        "subskill": "20_euler_formula_verification_platonic_solids",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": "2",
        "expected_answer": "2",
        "sample_answer": f"{v_val} - {e_val} + {f_val} = 2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Substitute values: {v_val} - {e_val} + {f_val}", "marks": 1},
            {"desc": "Evaluate to 2", "marks": 1},
        ],
        "hints": [
            "Substitute V, E, and F into V - E + F.",
            f"{v_val} - {e_val} + {f_val} = {v_val - e_val + f_val}.",
            "The answer is 2.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 21: Solve for Edges Using Euler's Formula
# -----------------------------------------------------------------------------
def arch_21_euler_formula_solve_edges(rng: random.Random, seed: int) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 9, 10])
    is_prism = rng.choice([True, False])
    if is_prism:
        f_val = n + 2
        v_val = 2 * n
        e_val = 3 * n
        poly_desc = f"prism with an {n}-sided base"
    else:
        f_val = n + 1
        v_val = n + 1
        e_val = 2 * n
        poly_desc = f"pyramid with an {n}-sided base"

    svg = draw_polyhedron_3d_svg("cube" if is_prism else "square_pyramid", seed=seed, title="Solve Edges E")

    prompt = (
        f"A polyhedron has $F = {f_val}$ faces and $V = {v_val}$ vertices. "
        f"Using Euler's formula ($V - E + F = 2$), calculate the total number of edges ($E$)."
    )
    sol = (
        f"Starting with Euler's formula: $V - E + F = 2$\n"
        f"Rearranging to solve for $E$:\n"
        f"$E = V + F - 2$\n"
        f"Substitute $V = {v_val}$ and $F = {f_val}$:\n"
        f"$E = {v_val} + {f_val} - 2 = {v_val + f_val} - 2 = {e_val}$.\n"
        f"Therefore, the polyhedron has ${e_val}$ edges."
    )

    return {
        "subskill": "21_euler_formula_solve_edges",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(e_val),
        "expected_answer": str(e_val),
        "sample_answer": str(e_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Rearrange Euler's formula: E = V + F - 2", "marks": 1},
            {"desc": f"Calculate E = {e_val}", "marks": 1},
        ],
        "hints": [
            "Euler's formula: V - E + F = 2.",
            "Rearrange: E = V + F - 2.",
            f"E = {v_val} + {f_val} - 2 = {e_val}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 22: Solve for Vertices Using Euler's Formula
# -----------------------------------------------------------------------------
def arch_22_euler_formula_solve_vertices(rng: random.Random, seed: int) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 9, 10])
    is_prism = rng.choice([True, False])
    if is_prism:
        f_val = n + 2
        v_val = 2 * n
        e_val = 3 * n
    else:
        f_val = n + 1
        v_val = n + 1
        e_val = 2 * n

    svg = draw_polyhedron_3d_svg("cube" if is_prism else "square_pyramid", seed=seed, title="Solve Vertices V")

    prompt = (
        f"A polyhedron has $F = {f_val}$ faces and $E = {e_val}$ edges. "
        f"Using Euler's formula ($V - E + F = 2$), determine the number of vertices ($V$)."
    )
    sol = (
        f"Starting with Euler's formula: $V - E + F = 2$\n"
        f"Rearrange to solve for $V$:\n"
        f"$V = E + 2 - F$\n"
        f"Substitute $E = {e_val}$ and $F = {f_val}$:\n"
        f"$V = {e_val} + 2 - {f_val} = {e_val + 2} - {f_val} = {v_val}$.\n"
        f"Therefore, the polyhedron has ${v_val}$ vertices."
    )

    return {
        "subskill": "22_euler_formula_solve_vertices",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(v_val),
        "expected_answer": str(v_val),
        "sample_answer": str(v_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Rearrange formula: V = E + 2 - F", "marks": 1},
            {"desc": f"Calculate V = {v_val}", "marks": 1},
        ],
        "hints": [
            "Euler's formula: V - E + F = 2.",
            "Rearrange: V = E + 2 - F.",
            f"V = {e_val} + 2 - {f_val} = {v_val}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 23: Solve for Faces Using Euler's Formula
# -----------------------------------------------------------------------------
def arch_23_euler_formula_solve_faces(rng: random.Random, seed: int) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7, 8, 9, 10])
    is_prism = rng.choice([True, False])
    if is_prism:
        f_val = n + 2
        v_val = 2 * n
        e_val = 3 * n
    else:
        f_val = n + 1
        v_val = n + 1
        e_val = 2 * n

    svg = draw_polyhedron_3d_svg("cube" if is_prism else "square_pyramid", seed=seed, title="Solve Faces F")

    prompt = (
        f"A polyhedron has $V = {v_val}$ vertices and $E = {e_val}$ edges. "
        f"Using Euler's formula ($V - E + F = 2$), determine the number of faces ($F$)."
    )
    sol = (
        f"Starting with Euler's formula: $V - E + F = 2$\n"
        f"Rearrange to solve for $F$:\n"
        f"$F = E + 2 - V$\n"
        f"Substitute $E = {e_val}$ and $V = {v_val}$:\n"
        f"$F = {e_val} + 2 - {v_val} = {e_val + 2} - {v_val} = {f_val}$.\n"
        f"Therefore, the polyhedron has ${f_val}$ faces."
    )

    return {
        "subskill": "23_euler_formula_solve_faces",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(f_val),
        "expected_answer": str(f_val),
        "sample_answer": str(f_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Rearrange formula: F = E + 2 - V", "marks": 1},
            {"desc": f"Calculate F = {f_val}", "marks": 1},
        ],
        "hints": [
            "Euler's formula: V - E + F = 2.",
            "Rearrange: F = E + 2 - V.",
            f"F = {e_val} + 2 - {v_val} = {f_val}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 24: Properties of a Cylinder (Curved Solid)
# -----------------------------------------------------------------------------
def arch_24_curved_solids_cylinder_properties(rng: random.Random, seed: int) -> Dict[str, Any]:
    questions = [
        ("How many flat circular bases does a closed cylinder have?", "2", "A closed cylinder has 2 identical parallel circular flat bases."),
        ("How many vertices (sharp corner points) does a cylinder have?", "0", "A cylinder has no vertices (0 corners)."),
        ("How many curved circular edges does a closed cylinder have?", "2", "A cylinder has 2 curved edges where the curved lateral surface meets the top and bottom circular bases."),
        ("Does Euler's formula (V - E + F = 2) apply to a cylinder?", "No", "Euler's formula applies exclusively to polyhedra with flat faces; it does not apply to solids with curved surfaces like cylinders."),
    ]
    q_text, ans, reason = rng.choice(questions)
    svg = draw_polyhedron_3d_svg("cylinder", seed=seed, title="Cylinder Properties")

    prompt = f"Refer to the cylinder shown in the diagram. {q_text}"
    sol = f"{ans}.\nReason: {reason}"

    return {
        "subskill": "24_curved_solids_cylinder_properties",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct property value: {ans}", "marks": 1},
            {"desc": "Provide geometric reasoning", "marks": 1},
        ],
        "hints": [
            "A cylinder has 2 circular bases and 1 curved lateral surface.",
            "It has 0 vertices and 2 curved edges.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 25: Properties of Cones and Spheres
# -----------------------------------------------------------------------------
def arch_25_curved_solids_cone_sphere_properties(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("cone", "Cone", "How many flat faces does a cone have?", "1", "A cone has exactly 1 flat circular base."),
        ("cone", "Cone", "How many vertices (apex) does a cone have?", "1", "A cone has 1 vertex at its apex."),
        ("sphere", "Sphere", "How many flat faces does a sphere have?", "0", "A sphere is entirely curved with 0 flat faces."),
        ("sphere", "Sphere", "How many edges does a sphere have?", "0", "A sphere has no edges (0 edges)."),
        ("sphere", "Sphere", "How many vertices does a sphere have?", "0", "A sphere has no corners/vertices (0 vertices)."),
    ]
    s_key, s_name, q_text, ans, reason = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("cone" if s_key == "cone" else "cylinder", seed=seed, title=f"{s_name} Properties")

    prompt = f"Consider the 3D curved solid: **{s_name}**. {q_text}"
    sol = f"{ans}.\nReason: {reason}"

    return {
        "subskill": "25_curved_solids_cone_sphere_properties",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 1},
            {"desc": "Provide geometric reasoning", "marks": 1},
        ],
        "hints": [
            f"Think about the flat vs curved parts of a {s_name}.",
            f"{reason}",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }
