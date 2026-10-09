"""Grade 8 Mathematics — Geometry of 3D Objects Generator.
Deterministic 6-pillar CAPS question generator covering:
- Polyhedra classification vs curved surfaces (spheres, cones, cylinders).
- Prisms and Pyramids: Faces (F), Vertices (V), Edges (E).
- Euler's Formula for Polyhedra: F + V - E = 2 (or V - E + F = 2).
- Platonic Solids: Regular Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron.
- Nets of 3D geometric figures.

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


POLYHEDRA_PROPERTIES = [
    {
        "name": "Triangular prism",
        "type": "Prism",
        "base": "Triangle",
        "faces": 5,
        "vertices": 6,
        "edges": 9,
        "face_shapes": "2 congruent triangles and 3 rectangles",
    },
    {
        "name": "Rectangular prism (Cuboid)",
        "type": "Prism",
        "base": "Rectangle",
        "faces": 6,
        "vertices": 8,
        "edges": 12,
        "face_shapes": "6 rectangles (opposite faces congruent)",
    },
    {
        "name": "Cube",
        "type": "Prism / Platonic solid",
        "base": "Square",
        "faces": 6,
        "vertices": 8,
        "edges": 12,
        "face_shapes": "6 congruent squares",
    },
    {
        "name": "Pentagonal prism",
        "type": "Prism",
        "base": "Pentagon",
        "faces": 7,
        "vertices": 10,
        "edges": 15,
        "face_shapes": "2 congruent pentagons and 5 rectangles",
    },
    {
        "name": "Hexagonal prism",
        "type": "Prism",
        "base": "Hexagon",
        "faces": 8,
        "vertices": 12,
        "edges": 18,
        "face_shapes": "2 congruent hexagons and 6 rectangles",
    },
    {
        "name": "Triangular pyramid (Tetrahedron)",
        "type": "Pyramid",
        "base": "Triangle",
        "faces": 4,
        "vertices": 4,
        "edges": 6,
        "face_shapes": "4 triangles",
    },
    {
        "name": "Square-based pyramid",
        "type": "Pyramid",
        "base": "Square",
        "faces": 5,
        "vertices": 5,
        "edges": 8,
        "face_shapes": "1 square base and 4 isosceles triangles",
    },
    {
        "name": "Pentagonal pyramid",
        "type": "Pyramid",
        "base": "Pentagon",
        "faces": 6,
        "vertices": 6,
        "edges": 10,
        "face_shapes": "1 pentagon base and 5 triangles",
    },
    {
        "name": "Hexagonal pyramid",
        "type": "Pyramid",
        "base": "Hexagon",
        "faces": 7,
        "vertices": 7,
        "edges": 12,
        "face_shapes": "1 hexagon base and 6 triangles",
    },
]

PLATONIC_SOLIDS = [
    {
        "name": "Regular Tetrahedron",
        "faces": 4,
        "vertices": 4,
        "edges": 6,
        "face_shape": "Equilateral triangles",
        "faces_meeting_at_vertex": 3,
    },
    {
        "name": "Cube (Regular Hexahedron)",
        "faces": 6,
        "vertices": 8,
        "edges": 12,
        "face_shape": "Squares",
        "faces_meeting_at_vertex": 3,
    },
    {
        "name": "Regular Octahedron",
        "faces": 8,
        "vertices": 6,
        "edges": 12,
        "face_shape": "Equilateral triangles",
        "faces_meeting_at_vertex": 4,
    },
    {
        "name": "Regular Dodecahedron",
        "faces": 12,
        "vertices": 20,
        "edges": 30,
        "face_shape": "Regular pentagons",
        "faces_meeting_at_vertex": 3,
    },
    {
        "name": "Regular Icosahedron",
        "faces": 20,
        "vertices": 12,
        "edges": 30,
        "face_shape": "Equilateral triangles",
        "faces_meeting_at_vertex": 5,
    },
]


def _build_euler_drill(r: random.Random) -> Dict[str, Any]:
    poly = r.choice(POLYHEDRA_PROPERTIES)
    target = r.choice(["edges", "vertices", "faces"])

    f, v, e = poly["faces"], poly["vertices"], poly["edges"]

    if target == "edges":
        prompt = (
            f"A {poly['name']} is a convex polyhedron with **{f} faces** and **{v} vertices**.\n\n"
            f"Use Euler's formula for convex polyhedra, $F + V - E = 2$, to calculate the number of edges ($E$)."
        )
        sol = (
            f"$F + V - E = 2$\n"
            f"${f} + {v} - E = 2$\n"
            f"${f + v} - E = 2$\n"
            f"$E = {f + v} - 2 = {e}$ edges."
        )
        correct_ans = str(e)
        mp = [
            {"id": "mp1", "desc": f"Substitute into Euler's formula: {f} + {v} - E = 2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Solve for E = {e}", "marks": 1, "editable": True},
        ]
        h1 = "Euler's formula relates Faces, Vertices, and Edges: $F + V - E = 2$."
        h2 = f"Substitute $F = {f}$ and $V = {v}$ into the equation and solve for $E$."
        h3 = f"${f} + {v} - E = 2 \\implies {f + v} - 2 = E \\implies E = {e}$."
    elif target == "vertices":
        prompt = (
            f"A {poly['name']} has **{f} faces** and **{e} edges**.\n\n"
            f"Use Euler's formula, $F + V - E = 2$, to determine the number of vertices ($V$)."
        )
        sol = (
            f"$F + V - E = 2$\n"
            f"${f} + V - {e} = 2$\n"
            f"$V - {e - f} = 2$\n"
            f"$V = 2 + {e - f} = {v}$ vertices."
        )
        correct_ans = str(v)
        mp = [
            {"id": "mp1", "desc": f"Substitute into Euler's formula: {f} + V - {e} = 2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Solve for V = {v}", "marks": 1, "editable": True},
        ]
        h1 = "Euler's formula: $F + V - E = 2$."
        h2 = f"Substitute $F = {f}$ and $E = {e}$ into $F + V - E = 2$."
        h3 = f"${f} + V - {e} = 2 \\implies V = 2 + {e} - {f} = {v}$."
    else:
        prompt = (
            f"A {poly['name']} has **{v} vertices** and **{e} edges**.\n\n"
            f"Use Euler's formula, $F + V - E = 2$, to determine the number of faces ($F$)."
        )
        sol = (
            f"$F + V - E = 2$\n"
            f"$F + {v} - {e} = 2$\n"
            f"$F - {e - v} = 2$\n"
            f"$F = 2 + {e - v} = {f}$ faces."
        )
        correct_ans = str(f)
        mp = [
            {"id": "mp1", "desc": f"Substitute into Euler's formula: F + {v} - {e} = 2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Solve for F = {f}", "marks": 1, "editable": True},
        ]
        h1 = "Euler's formula states: $F + V - E = 2$."
        h2 = f"Substitute $V = {v}$ and $E = {e}$ into the formula."
        h3 = f"$F + {v} - {e} = 2 \\implies F = 2 + {e} - {v} = {f}$."

    return {
        "id": f"g8_math_3d_euler_{r.randint(10000, 99999)}",
        "type": "numeric",
        "prompt": prompt,
        "correct_answer": correct_ans,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 2,
            "marking_points": mp,
            "deductions": [{"rule": "sign_error_euler", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {"tier_1": h1, "tier_2": h2, "tier_3": h3},
        "misconception_tags": ["eulers_formula_sign_error", "confused_vertex_and_edge"],
        "term": 3,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 3,
    }


def _build_platonic_drill(r: random.Random) -> Dict[str, Any]:
    solid = r.choice(PLATONIC_SOLIDS)
    aspect = r.choice(["face_shape", "faces_count", "euler_verify"])

    if aspect == "face_shape":
        prompt = (
            f"The **{solid['name']}** is one of the five Platonic solids.\n\n"
            f"What geometric shape forms all the faces of a {solid['name']}?"
        )
        sol = f"Every face of a {solid['name']} is a **{solid['face_shape']}**."
        correct_ans = solid["face_shape"]
        mp = [{"id": "mp1", "desc": f"State face shape: {solid['face_shape']}", "marks": 1, "editable": True}]
        h1 = "A Platonic solid is a regular polyhedron whose faces are all congruent regular polygons."
        h2 = f"Recall the shape of the regular polygons making up a {solid['name']}."
        h3 = f"The faces are {solid['face_shape']}."
    elif aspect == "faces_count":
        prompt = (
            f"How many faces does a **{solid['name']}** have?"
        )
        sol = f"A {solid['name']} has **{solid['faces']}** faces."
        correct_ans = str(solid["faces"])
        mp = [{"id": "mp1", "desc": f"State number of faces: {solid['faces']}", "marks": 1, "editable": True}]
        h1 = "The name of a regular polyhedron often gives a clue to its number of faces (e.g. tetra = 4, hexa = 6, octa = 8, dodeca = 12, icosa = 20)."
        h2 = f"Determine the face count for {solid['name']}."
        h3 = f"Faces = {solid['faces']}."
    else:
        prompt = (
            f"A {solid['name']} has $F = {solid['faces']}$ faces and $V = {solid['vertices']}$ vertices.\n\n"
            f"1. Use Euler's formula to find the number of edges ($E$).\n"
            f"2. Verify that $F + V - E = 2$."
        )
        sol = (
            f"$F + V - E = 2$\n"
            f"${solid['faces']} + {solid['vertices']} - E = 2$\n"
            f"${solid['faces'] + solid['vertices']} - E = 2$\n"
            f"$E = {solid['edges']}$ edges.\n"
            f"Verification: ${solid['faces']} + {solid['vertices']} - {solid['edges']} = {solid['faces'] + solid['vertices'] - solid['edges']} = 2$."
        )
        correct_ans = str(solid["edges"])
        mp = [
            {"id": "mp1", "desc": f"Substitute F={solid['faces']}, V={solid['vertices']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Solve E={solid['edges']}", "marks": 1, "editable": True},
        ]
        h1 = "Apply Euler's formula: $F + V - E = 2$."
        h2 = f"Compute $E = F + V - 2 = {solid['faces']} + {solid['vertices']} - 2$."
        h3 = f"$E = {solid['faces'] + solid['vertices']} - 2 = {solid['edges']}$."

    return {
        "id": f"g8_math_3d_platonic_{r.randint(10000, 99999)}",
        "type": "short_answer",
        "prompt": prompt,
        "correct_answer": correct_ans,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": len(mp),
            "marking_points": mp,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {"tier_1": h1, "tier_2": h2, "tier_3": h3},
        "misconception_tags": ["platonic_solids_confusion", "confused_faces_and_vertices"],
        "term": 3,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 3,
    }


def _build_polyhedra_vs_curved_drill(r: random.Random) -> Dict[str, Any]:
    items = [
        ("Cone", False, "It has a curved lateral surface and is not bounded exclusively by flat polygonal faces."),
        ("Cylinder", False, "It has a curved lateral surface and is not bounded exclusively by flat polygonal faces."),
        ("Sphere", False, "It has a continuous curved surface with zero flat faces."),
        ("Triangular prism", True, "It is bounded entirely by flat polygonal faces (2 triangles and 3 rectangles)."),
        ("Cube", True, "It is bounded entirely by 6 flat square faces."),
        ("Square-based pyramid", True, "It is bounded entirely by flat faces (1 square base and 4 triangular faces)."),
        ("Hexagonal prism", True, "It is bounded entirely by flat polygonal faces (2 hexagons and 6 rectangles)."),
    ]
    name, is_poly, explanation = r.choice(items)

    prompt = (
        f"Consider the 3D object: **{name}**.\n\n"
        f"1. Is a {name} classified as a **polyhedron**? (Answer: Yes or No)\n"
        f"2. Give a geometric reason for your answer."
    )
    ans = "Yes" if is_poly else "No"
    sol = (
        f"Answer: **{ans}**\n\n"
        f"Reason: {explanation}"
    )

    return {
        "id": f"g8_math_3d_classify_{r.randint(10000, 99999)}",
        "type": "short_answer",
        "prompt": prompt,
        "correct_answer": ans,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct classification ({ans})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Valid geometric reason referring to flat polygonal faces vs curved surfaces", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "A polyhedron is a 3D solid bounded exclusively by flat polygonal faces.",
            "tier_2": "Objects with curved surfaces (like spheres, cones, cylinders) cannot be polyhedra.",
            "tier_3": f"{name} {'is' if is_poly else 'is not'} a polyhedron because {explanation}",
        },
        "misconception_tags": ["curved_surface_classified_as_polyhedron"],
        "term": 3,
        "caps_weight_percent": 6,
        "suggested_duration_mins": 2,
    }


def _build_compound_exam_question(r: random.Random) -> Dict[str, Any]:
    poly = r.choice(POLYHEDRA_PROPERTIES)
    f, v, e = poly["faces"], poly["vertices"], poly["edges"]

    prompt = (
        f"Examine the 3D geometric object: **{poly['name']}**.\n\n"
        f"1. Classify whether this object is a **prism** or a **pyramid**.\n"
        f"2. State the number of faces ($F$), vertices ($V$), and edges ($E$).\n"
        f"3. State the shapes of the faces.\n"
        f"4. Verify Euler's formula for this solid by evaluating $F + V - E$."
    )

    sol = (
        f"1. Classification: **{poly['type']}**\n"
        f"2. Number of elements:\n"
        f"   - Faces ($F$) = ${f}$\n"
        f"   - Vertices ($V$) = ${v}$\n"
        f"   - Edges ($E$) = ${e}$\n"
        f"3. Face shapes: {poly['face_shapes']}\n"
        f"4. Euler's formula verification:\n"
        f"   $F + V - E = {f} + {v} - {e} = {f + v} - {e} = 2$.\n"
        f"   The formula holds true."
    )

    return {
        "id": f"g8_math_3d_compound_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"F={f}, V={v}, E={e}, F+V-E=2",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct classification: {poly['type']}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Faces count: {f}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Vertices count: {v}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Edges count: {e}", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Face shapes: {poly['face_shapes']}", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Verification: F + V - E = 2", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "prism_vs_pyramid_confusion", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Identify whether the solid has two identical parallel bases (prism) or one base tapering to an apex (pyramid).",
            "tier_2": "Count the flat faces, corner vertices, and straight edges where two faces meet.",
            "tier_3": f"For a {poly['name']}: $F = {f}$, $V = {v}$, $E = {e}$. Then $F + V - E = {f} + {v} - {e} = 2$.",
        },
        "misconception_tags": [
            "prism_vs_pyramid_faces_inversion",
            "confused_vertex_and_edge",
            "eulers_formula_sign_error",
        ],
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)

    if mode == "elementary_euler":
        return _build_euler_drill(r)
    elif mode == "elementary_platonic":
        return _build_platonic_drill(r)
    elif mode == "elementary_classify":
        return _build_polyhedra_vs_curved_drill(r)
    elif mode == "compound":
        return _build_compound_exam_question(r)
    else:
        # Default random rotation across archetypes
        choice = r.choice(["compound", "euler", "platonic", "classify"])
        if choice == "compound":
            return _build_compound_exam_question(r)
        elif choice == "euler":
            return _build_euler_drill(r)
        elif choice == "platonic":
            return _build_platonic_drill(r)
        else:
            return _build_polyhedra_vs_curved_drill(r)
