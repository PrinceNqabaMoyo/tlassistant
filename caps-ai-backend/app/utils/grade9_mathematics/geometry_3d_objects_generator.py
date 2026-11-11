"""Grade 9 Mathematics — Geometry of 3D Objects Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 4: Geometry of 3D objects
- South African National Curriculum Standards (Senior Phase Mathematics)
- Properties and classification of 3D geometric figures:
  * Polyhedra vs Non-polyhedra (prisms and pyramids vs cylinders, cones, spheres)
  * Prisms vs Pyramids (bases, lateral faces, apex)
  * Faces (F), Vertices (V), and Edges (E) of polyhedra
  * Euler's Formula for polyhedra: F + V - E = 2 (or V - E + F = 2)
  * The 5 Platonic Solids (tetrahedron, hexahedron/cube, octahedron, dodecahedron, icosahedron)
  * Geometric nets of 3D objects (cube nets, rectangular prism, triangular prism, square-based pyramid, cylinder)

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'cube_net', 'triangular_prism_net', 'rectangular_prism_net', 'solid_3d')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_geometry_of_3d_objects"
LO = "math9_geometry_3d_objects"

# Polyhedra database: Name, Base, Faces, Vertices, Edges, Net Kind
POLYHEDRA_DATA = [
    {"name": "Triangular Prism", "f": 5, "v": 6, "e": 9, "net": "triangular_prism_net", "type": "prism", "base": "triangle"},
    {"name": "Rectangular Prism (Cuboid)", "f": 6, "v": 8, "e": 12, "net": "rectangular_prism_net", "type": "prism", "base": "rectangle"},
    {"name": "Cube (Hexahedron)", "f": 6, "v": 8, "e": 12, "net": "cube_net", "type": "platonic", "base": "square"},
    {"name": "Square-based Pyramid", "f": 5, "v": 5, "e": 8, "net": "square_pyramid_net", "type": "pyramid", "base": "square"},
    {"name": "Tetrahedron (Triangular Pyramid)", "f": 4, "v": 4, "e": 6, "net": "triangular_prism_net", "type": "platonic", "base": "equilateral triangle"},
    {"name": "Octahedron", "f": 8, "v": 6, "e": 12, "net": "solid_3d", "type": "platonic", "base": "equilateral triangle"},
    {"name": "Pentagonal Prism", "f": 7, "v": 10, "e": 15, "net": "solid_3d", "type": "prism", "base": "pentagon"},
    {"name": "Hexagonal Prism", "f": 8, "v": 12, "e": 18, "net": "solid_3d", "type": "prism", "base": "hexagon"},
]


def generate_grade9_geometry_3d_objects_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "eulers_formula_missing_element",
        "prism_vs_pyramid_properties",
        "platonic_solids_identification",
        "geometric_nets_identification",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_geom3d_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "eulers_formula_missing_element":
        # Euler's Formula: F + V - E = 2 (or F + V = E + 2)
        poly = r.choice(POLYHEDRA_DATA)
        f_val = poly["f"]
        v_val = poly["v"]
        e_val = poly["e"]
        name = poly["name"]
        
        # Hide one of F, V, or E
        hide_target = r.choice(["edges", "vertices", "faces"])
        if hide_target == "edges":
            question_text = (
                f"A 3D polyhedron ({name}) has $F = {f_val}$ faces and $V = {v_val}$ vertices.\n\n"
                f"1. State Euler's formula connecting the faces ($F$), vertices ($V$), and edges ($E$) of any convex polyhedron.\n"
                f"2. Use Euler's formula to calculate the number of edges ($E$) of this polyhedron."
            )
            correct_ans = str(e_val)
            steps = [
                {"id": "S1", "statement": "Euler's Formula: $F + V - E = 2$ (or $F + V = E + 2$)", "reason": "Euler's polyhedron formula", "deps": []},
                {"id": "S2", "statement": f"${f_val} + {v_val} = E + 2 \\implies {f_val + v_val} = E + 2$", "reason": "substitute given values", "deps": ["S1"]},
                {"id": "S3", "statement": f"$E = {f_val + v_val} - 2 = {e_val}$", "reason": "solve for E", "deps": ["S2"]},
            ]
            hints = [
                "Euler's formula states that for any convex polyhedron: Faces + Vertices - Edges = 2.",
                f"Substitute the given numbers: ${f_val} + {v_val} - E = 2$.",
                f"Simplify: ${f_val + v_val} - E = 2$, which gives $E = {f_val + v_val} - 2 = {e_val}$ edges.",
            ]
        elif hide_target == "vertices":
            question_text = (
                f"A 3D polyhedron ({name}) has $F = {f_val}$ faces and $E = {e_val}$ edges.\n\n"
                f"1. State Euler's formula for convex polyhedra.\n"
                f"2. Calculate the number of vertices ($V$) of this polyhedron."
            )
            correct_ans = str(v_val)
            steps = [
                {"id": "S1", "statement": "Euler's Formula: $F + V - E = 2$", "reason": "Euler's formula", "deps": []},
                {"id": "S2", "statement": f"${f_val} + V - {e_val} = 2 \\implies V - {e_val - f_val} = 2$", "reason": "substitute values", "deps": ["S1"]},
                {"id": "S3", "statement": f"$V = 2 + {e_val - f_val} = {v_val}$", "reason": "solve for V", "deps": ["S2"]},
            ]
            hints = [
                "Euler's formula: Faces + Vertices = Edges + 2.",
                f"Substitute: ${f_val} + V = {e_val} + 2 = {e_val + 2}$.",
                f"Solve for V: $V = {e_val + 2} - {f_val} = {v_val}$ vertices.",
            ]
        else:
            question_text = (
                f"A 3D polyhedron ({name}) has $V = {v_val}$ vertices and $E = {e_val}$ edges.\n\n"
                f"1. State Euler's formula for polyhedra.\n"
                f"2. Calculate the number of faces ($F$) of this polyhedron."
            )
            correct_ans = str(f_val)
            steps = [
                {"id": "S1", "statement": "Euler's Formula: $F + V = E + 2$", "reason": "Euler's formula", "deps": []},
                {"id": "S2", "statement": f"$F + {v_val} = {e_val} + 2 = {e_val + 2}$", "reason": "substitute values", "deps": ["S1"]},
                {"id": "S3", "statement": f"$F = {e_val + 2} - {v_val} = {f_val}$", "reason": "solve for F", "deps": ["S2"]},
            ]
            hints = [
                "Euler's formula: F + V = E + 2.",
                f"Substitute: $F + {v_val} = {e_val} + 2 = {e_val + 2}$.",
                f"Solve for F: $F = {e_val + 2} - {v_val} = {f_val}$ faces.",
            ]

        error_tax = [
            {
                "id": "err_wrong_euler_constant",
                "tag": "misconception_eulers_constant",
                "condition": "Used F + V - E = 0 or 1",
                "feedback": "Euler's formula for any 3D polyhedron always equals 2: F + V - E = 2 (or F + V = E + 2).",
            },
        ]

        sample_answer = (
            f"1. $F + V - E = 2$ (or $F + V = E + 2$)\n"
            f"2. " + steps[-1]["statement"]
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": poly["net"] if poly["net"] != "solid_3d" else "solid_3d",
            "type": poly["name"].lower().replace(" ", "_"),
            "caption": f"{name} (F = {f_val}, V = {v_val}, E = {e_val})",
        }

        subskill_id = "eulers_formula_missing_element"
        reason_code = "Euler's Formula (F + V - E = 2)"
        marks = 3

    elif archetype == "prism_vs_pyramid_properties":
        # Distinguish between prisms and pyramids
        is_prism = r.choice([True, False])
        n_sides = r.choice([3, 4, 5, 6])
        polygon_names = {3: "triangular", 4: "rectangular", 5: "pentagonal", 6: "hexagonal"}
        poly_name = polygon_names[n_sides]
        
        if is_prism:
            shape_name = f"{poly_name.capitalize()} Prism"
            base_desc = f"two identical parallel {poly_name} bases"
            lateral_desc = f"{n_sides} rectangular lateral faces"
            total_faces = n_sides + 2
            total_verts = 2 * n_sides
            total_edges = 3 * n_sides
            explanation = (
                f"A prism has two congruent parallel bases connected by rectangular faces. "
                f"For an n-sided base ({n_sides}): Faces = n + 2 = {total_faces}, "
                f"Vertices = 2n = {total_verts}, Edges = 3n = {total_edges}."
            )
        else:
            shape_name = f"{poly_name.capitalize()} Pyramid"
            base_desc = f"one {poly_name} base"
            lateral_desc = f"{n_sides} triangular lateral faces meeting at a common apex"
            total_faces = n_sides + 1
            total_verts = n_sides + 1
            total_edges = 2 * n_sides
            explanation = (
                f"A pyramid has one polygonal base and triangular faces that meet at an apex. "
                f"For an n-sided base ({n_sides}): Faces = n + 1 = {total_faces}, "
                f"Vertices = n + 1 = {total_verts}, Edges = 2n = {total_edges}."
            )

        question_text = (
            f"Consider a 3D object: a **{shape_name}**.\n\n"
            f"1. Describe the shape of its base(s) and lateral faces.\n"
            f"2. State the total number of faces ($F$), vertices ($V$), and edges ($E$) of this object."
        )

        steps = [
            {"id": "S1", "statement": f"Base(s): {base_desc}; Lateral faces: {lateral_desc}", "reason": "geometric definition", "deps": []},
            {"id": "S2", "statement": f"Faces: $F = {total_faces}$, Vertices: $V = {total_verts}$, Edges: $E = {total_edges}$", "reason": "formula based on n-gon base", "deps": ["S1"]},
            {"id": "S3", "statement": f"Verify Euler's formula: ${total_faces} + {total_verts} - {total_edges} = 2$", "reason": "Euler check", "deps": ["S2"]},
        ]

        hints = [
            f"A {'prism has 2 bases and rectangular lateral faces' if is_prism else 'pyramid has 1 base and triangular lateral faces meeting at an apex'}.",
            f"Base has n = {n_sides} sides.\n{'For a prism: F = n + 2, V = 2n, E = 3n' if is_prism else 'For a pyramid: F = n + 1, V = n + 1, E = 2n'}.",
            f"Faces: {total_faces}, Vertices: {total_verts}, Edges: {total_edges}.",
        ]

        error_tax = [
            {
                "id": "err_confused_prism_pyramid_faces",
                "tag": "misconception_prism_vs_pyramid",
                "condition": "Confused prism and pyramid face formulas",
                "feedback": f"Remember: A prism has 2 bases (so n + 2 faces); a pyramid has only 1 base (so n + 1 faces).",
            },
        ]

        sample_answer = (
            f"1. Base(s): {base_desc}\n"
            f"   Lateral faces: {lateral_desc}\n"
            f"2. Faces: $F = {total_faces}$\n"
            f"   Vertices: $V = {total_verts}$\n"
            f"   Edges: $E = {total_edges}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "solid_3d",
            "type": shape_name.lower().replace(" ", "_"),
            "caption": f"{shape_name} (F={total_faces}, V={total_verts}, E={total_edges})",
        }

        correct_ans = f"F={total_faces}, V={total_verts}, E={total_edges}"
        subskill_id = "prism_vs_pyramid_properties"
        reason_code = "prism and pyramid properties"
        marks = 4

    elif archetype == "platonic_solids_identification":
        # The 5 Platonic Solids
        platonic_solids = [
            {"name": "Tetrahedron", "faces": 4, "face_shape": "equilateral triangles", "verts": 4, "edges": 6},
            {"name": "Hexahedron (Cube)", "faces": 6, "face_shape": "squares", "verts": 8, "edges": 12},
            {"name": "Octahedron", "faces": 8, "face_shape": "equilateral triangles", "verts": 6, "edges": 12},
            {"name": "Dodecahedron", "faces": 12, "face_shape": "regular pentagons", "verts": 20, "edges": 30},
            {"name": "Icosahedron", "faces": 20, "face_shape": "equilateral triangles", "verts": 12, "edges": 30},
        ]
        target = r.choice(platonic_solids)

        question_text = (
            f"A regular polyhedron is one where all faces are identical regular polygons, "
            f"and the same number of faces meet at each vertex.\n\n"
            f"Identify the Platonic solid that has **{target['faces']} faces**:\n"
            f"1. Name this Platonic solid.\n"
            f"2. What is the geometric shape of each of its faces?\n"
            f"3. State its number of vertices ($V$) and edges ($E$)."
        )

        steps = [
            {"id": "S1", "statement": f"Platonic solid name: {target['name']}", "reason": f"regular polyhedron with {target['faces']} faces", "deps": []},
            {"id": "S2", "statement": f"Face shape: {target['face_shape']}", "reason": "regular face polygon", "deps": ["S1"]},
            {"id": "S3", "statement": f"Vertices $V = {target['verts']}$, Edges $E = {target['edges']}$", "reason": "Platonic solid invariants", "deps": ["S2"]},
        ]

        hints = [
            "There are exactly 5 Platonic solids: Tetrahedron (4), Cube (6), Octahedron (8), Dodecahedron (12), Icosahedron (20).",
            f"The Platonic solid with {target['faces']} faces is the {target['name']}.",
            f"Faces are {target['face_shape']}. It has {target['verts']} vertices and {target['edges']} edges.",
        ]

        error_tax = [
            {
                "id": "err_octahedron_pentagons",
                "tag": "misconception_platonic_face_shape",
                "condition": "Confused face shapes among Platonic solids",
                "feedback": "Tetrahedron, Octahedron, and Icosahedron have equilateral triangular faces; Cube has squares; Dodecahedron has regular pentagons.",
            },
        ]

        sample_answer = (
            f"1. {target['name']}\n"
            f"2. {target['face_shape']}\n"
            f"3. Vertices: $V = {target['verts']}$, Edges: $E = {target['edges']}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "solid_3d",
            "type": target["name"].lower().split()[0],
            "caption": f"Platonic Solid: {target['name']} ({target['faces']} {target['face_shape']})",
        }

        correct_ans = target["name"]
        subskill_id = "platonic_solids_identification"
        reason_code = "Platonic Solid classification"
        marks = 3

    else:
        # geometric_nets_identification
        net_choices = [
            {"solid": "Cube", "net_kind": "cube_net", "faces_desc": "6 congruent squares", "valid_arr": "T-shape or cross shape with 4 in a line and 2 on opposite sides"},
            {"solid": "Triangular Prism", "net_kind": "triangular_prism_net", "faces_desc": "3 rectangles and 2 congruent triangles", "valid_arr": "3 rectangles connected along long edges with triangular bases attached"},
            {"solid": "Rectangular Prism", "net_kind": "rectangular_prism_net", "faces_desc": "6 rectangles in 3 opposite congruent pairs", "valid_arr": "4 rectangles in a strip with 2 lid flaps"},
            {"solid": "Cylinder", "net_kind": "cylinder_net", "faces_desc": "1 rectangle and 2 circular bases", "valid_arr": "A rectangle with length equal to circumference 2*pi*r, and two circles"},
        ]
        chosen_net = r.choice(net_choices)

        question_text = (
            f"A flat 2D cardboard pattern consists of **{chosen_net['faces_desc']}**.\n\n"
            f"1. When this net is folded without overlapping, which 3D geometric solid does it form?\n"
            f"2. Explain the condition required for the dimensions of the net to fold together correctly."
        )

        steps = [
            {"id": "S1", "statement": f"3D Solid: {chosen_net['solid']}", "reason": "net geometry correspondence", "deps": []},
            {"id": "S2", "statement": f"Folding condition: {chosen_net['valid_arr']}", "reason": "edge matching criterion", "deps": ["S1"]},
        ]

        hints = [
            f"Look at the faces: {chosen_net['faces_desc']}. What 3D solid has these exact faces?",
            f"This net folds to form a {chosen_net['solid']}.",
            f"The edges that fold together must have identical lengths ({chosen_net['valid_arr']}).",
        ]

        error_tax = [
            {
                "id": "err_cylinder_net_dimension",
                "tag": "misconception_cylinder_net_length",
                "condition": "Stated that cylinder rectangle length is arbitrary",
                "feedback": "For a cylinder, the length of the rectangular curved surface MUST equal the circumference of the circular bases: l = 2πr.",
            },
        ]

        sample_answer = (
            f"1. {chosen_net['solid']}\n"
            f"2. {chosen_net['valid_arr']}"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": chosen_net["net_kind"],
            "caption": f"Net of a {chosen_net['solid']}",
        }

        correct_ans = chosen_net["solid"]
        subskill_id = "geometric_nets_identification"
        reason_code = "3D geometric nets"
        marks = 3

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct property or formula [{reason_code}]", "marks": 1},
            {"criterion": f"Correct values and deduction {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["geometry", "3D objects", "polyhedra", "Euler's formula", "Platonic solids", "nets", "prisms", "pyramids"],
        "term": 4,
        "caps_weight_percent": 8.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Classify and analyse 3D geometric objects",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_geometry_3d_objects_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
