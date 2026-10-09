"""
Grade 7 Mathematics - Geometry of 3D Objects & Geometric Nets Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.

Topics Covered (Grade 7 Term 3 / Senior Phase CAPS):
- Geometric Nets of 3D Polyhedra and Prisms (Cube, Rectangular Prism, Triangular Prism, Square Pyramid, Cylinder, Cone)
- Identification of Valid vs. Invalid Nets (e.g. overlapping faces, missing base)
- Polyhedra Properties: Faces (F), Vertices (V), Edges (E)
- Euler's Formula for Convex Polyhedra: F + V - E = 2
- Total Surface Area derived directly from the 2D Net
"""

from __future__ import annotations
import random
import math
from typing import Any, Dict, List, Optional


# Standard 3D Shapes Catalog with authentic CAPS properties
POLYHEDRA_CATALOG = {
    "cube": {
        "name": "Cube",
        "faces": 6,
        "vertices": 8,
        "edges": 12,
        "face_shapes": "6 congruent squares",
        "net_type": "6 square faces arranged without overlapping folds",
        "valid_net_patterns": [
            "T-shape (Latin Cross with 4 squares in a line and 2 flanking squares)",
            "Step pattern (1-4-1 layout)",
            "2-3-1 zigzag layout"
        ],
        "invalid_net_example": "5 squares in a row with 1 flap (cannot fold into a 3D box)",
        "net_spec": {
            "kind": "cube_net",
            "boxes": [
                {"x": 1, "y": 0, "w": 1, "h": 1, "label": "Top"},
                {"x": 0, "y": 1, "w": 1, "h": 1, "label": "Left"},
                {"x": 1, "y": 1, "w": 1, "h": 1, "label": "Base"},
                {"x": 2, "y": 1, "w": 1, "h": 1, "label": "Right"},
                {"x": 3, "y": 1, "w": 1, "h": 1, "label": "Back"},
                {"x": 1, "y": 2, "w": 1, "h": 1, "label": "Front"}
            ]
        }
    },
    "rectangular_prism": {
        "name": "Rectangular Prism (Cuboid)",
        "faces": 6,
        "vertices": 8,
        "edges": 12,
        "face_shapes": "3 pairs of identical rectangles (or 4 rectangles and 2 squares)",
        "net_type": "6 rectangular faces matching opposite dimensions",
        "valid_net_patterns": ["Cross pattern with central spine of 4 rectangles and 2 side flaps"],
        "invalid_net_example": "Flaps on the same side that overlap upon folding",
        "net_spec": {
            "kind": "rectangular_prism_net",
            "boxes": [
                {"x": 1, "y": 0, "w": 1, "h": 1, "label": "Top Base"},
                {"x": 0, "y": 1, "w": 1, "h": 2, "label": "Side A"},
                {"x": 1, "y": 1, "w": 1, "h": 2, "label": "Front"},
                {"x": 2, "y": 1, "w": 1, "h": 2, "label": "Side B"},
                {"x": 3, "y": 1, "w": 1, "h": 2, "label": "Back"},
                {"x": 1, "y": 3, "w": 1, "h": 1, "label": "Bottom Base"}
            ]
        }
    },
    "triangular_prism": {
        "name": "Right Triangular Prism",
        "faces": 5,
        "vertices": 6,
        "edges": 9,
        "face_shapes": "2 congruent triangular bases and 3 rectangular lateral faces",
        "net_type": "3 rectangles joined side-by-side with 1 triangle attached to each end of a rectangle",
        "valid_net_patterns": ["Central spine of 3 rectangles with 2 triangular flaps on opposite sides"],
        "invalid_net_example": "Both triangles attached to the same rectangle on the same side",
        "net_spec": {
            "kind": "triangular_prism_net",
            "boxes": [
                {"x": 0, "y": 1, "w": 1.2, "h": 2, "label": "Face 1"},
                {"x": 1.2, "y": 1, "w": 1.5, "h": 2, "label": "Base Rect"},
                {"x": 2.7, "y": 1, "w": 1.2, "h": 2, "label": "Face 2"}
            ],
            "triangles": [
                {"points": [[1.2, 1], [2.7, 1], [1.95, 0]], "label": "Triangle 1"},
                {"points": [[1.2, 3], [2.7, 3], [1.95, 4]], "label": "Triangle 2"}
            ]
        }
    },
    "square_pyramid": {
        "name": "Square-Based Pyramid",
        "faces": 5,
        "vertices": 5,
        "edges": 8,
        "face_shapes": "1 square base and 4 isosceles triangular lateral faces",
        "net_type": "1 central square base with 4 triangular flaps branching outward like a star",
        "valid_net_patterns": ["Star pattern (square in center, 4 triangles attached to the 4 edges)"],
        "invalid_net_example": "Only 3 triangles attached to the square base",
        "net_spec": {
            "kind": "square_pyramid_net",
            "boxes": [
                {"x": 1, "y": 1, "w": 1.5, "h": 1.5, "label": "Square Base"}
            ],
            "triangles": [
                {"points": [[1, 1], [2.5, 1], [1.75, 0]], "label": "North Face"},
                {"points": [[2.5, 1], [2.5, 2.5], [3.5, 1.75]], "label": "East Face"},
                {"points": [[1, 2.5], [2.5, 2.5], [1.75, 3.5]], "label": "South Face"},
                {"points": [[1, 1], [1, 2.5], [0, 1.75]], "label": "West Face"}
            ]
        }
    },
    "cylinder": {
        "name": "Right Cylinder",
        "faces": 3, # 2 flat circular faces + 1 curved lateral surface
        "vertices": 0,
        "edges": 2, # 2 circular curved edges
        "face_shapes": "2 congruent circular bases and 1 rectangular lateral face",
        "net_type": "1 large rectangle flanked by 2 identical circles with circumference matching rectangle width",
        "valid_net_patterns": ["1 rectangle with a circle on the top edge and a circle on the bottom edge"],
        "invalid_net_example": "Circles attached on the same side with mismatched circumference",
        "net_spec": {
            "kind": "cylinder_net",
            "boxes": [
                {"x": 0.5, "y": 1, "w": 3.14, "h": 1.8, "label": "Lateral Surface (Width = 2πr)"}
            ],
            "circles": [
                {"cx": 1.5, "cy": 0.5, "r": 0.5, "label": "Top Base"},
                {"cx": 2.5, "cy": 3.3, "r": 0.5, "label": "Bottom Base"}
            ]
        }
    }
}


def _generate_net_identification_question(rng: random.Random) -> Dict[str, Any]:
    """Generates a question identifying which 3D shape folds from a given 2D net."""
    shape_key = rng.choice(["cube", "rectangular_prism", "triangular_prism", "square_pyramid", "cylinder"])
    shape = POLYHEDRA_CATALOG[shape_key]
    
    distractors = [s["name"] for k, s in POLYHEDRA_CATALOG.items() if k != shape_key]
    rng.shuffle(distractors)
    chosen_distractors = distractors[:3]
    
    options = [shape["name"]] + chosen_distractors
    rng.shuffle(options)
    correct_idx = options.index(shape["name"])
    correct_letter = chr(65 + correct_idx)
    
    options_latex = [f"\\textbf{{{chr(65 + i)}}}~{opt}" for i, opt in enumerate(options)]
    options_str = "\n".join(f"{chr(65 + i)}. {opt}" for i, opt in enumerate(options))
    
    prompt = (
        f"A learner cuts out a 2D geometric net composed of **{shape['face_shapes']}**.\n\n"
        f"When folded along its crease lines without any overlapping faces, which 3D solid will this net form?\n\n"
        f"{options_str}"
    )
    
    sol = (
        f"**Step 1:** Analyze the faces in the net:\n\n"
        f"The net contains **{shape['face_shapes']}**.\n\n"
        f"**Step 2:** Match to 3D solid:\n\n"
        f"A **{shape['name']}** has exactly {shape['faces']} faces consisting of {shape['face_shapes']}.\n\n"
        f"$$\\therefore \\text{{Correct Answer is }} \\mathbf{{{correct_letter}}}:~{shape['name']}$$"
    )
    
    return {
        "id": f"g7_math_net_id_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "prompt_latex": prompt,
        "options": options,
        "options_latex": options_latex,
        "correct_option": correct_letter,
        "correct_answer": shape["name"],
        "answer_latex": f"\\mathbf{{{correct_letter}}}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "geometric_net_identification",
        "learning_objective_id": "math_g7_3d_nets_identification",
        "diagram_spec": shape["net_spec"],
        "misconception_tags": [
            "net_overlapping_faces_misconception",
            "confusing_prism_with_pyramid",
            "cylinder_net_lateral_length_slip"
        ],
        "diagnostic_tags": ["spatial_reasoning", "geometric_nets"],
        "minimum_mastery_score": 75,
        "keywords": ["geometric net", "3D solid", shape["name"].lower(), "faces", "folding"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify face composition from net description", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Eliminate inconsistent 3D geometric polyhedra", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct selection of folded 3D solid", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Count the total number of faces and look closely at the shape of the bases.",
            "tier_2": f"The net consists of {shape['face_shapes']}. Pyramids have triangular sides meeting at an apex, while prisms have rectangular lateral faces.",
            "tier_3": f"Folding {shape['face_shapes']} forms a {shape['name']} ({correct_letter})."
        }
    }


def _generate_eulers_formula_question(rng: random.Random) -> Dict[str, Any]:
    """Generates a question on Euler's formula (F + V - E = 2) for Grade 7/8/9."""
    poly_key = rng.choice(["cube", "rectangular_prism", "triangular_prism", "square_pyramid"])
    poly = POLYHEDRA_CATALOG[poly_key]
    
    # Randomly choose which variable is the unknown: F, V, or E
    unknown = rng.choice(["faces", "vertices", "edges"])
    
    F = poly["faces"]
    V = poly["vertices"]
    E = poly["edges"]
    
    if unknown == "faces":
        target_val = F
        prompt = (
            f"A convex polyhedron has **{V} vertices** and **{E} edges**.\n\n"
            f"1. State Euler's formula relating faces ($F$), vertices ($V$), and edges ($E$) for polyhedra.\n"
            f"2. Use Euler's formula to calculate the number of faces ($F$) of this 3D shape.\n"
            f"3. Name the 3D shape that matches these properties."
        )
        sol = (
            f"**Step 1:** Euler's Formula is:\n\n"
            f"$$F + V - E = 2$$\n\n"
            f"**Step 2:** Substitute the known values $V = {V}$ and $E = {E}$:\n\n"
            f"$$F + {V} - {E} = 2$$\n\n"
            f"$$F + ({V - E}) = 2$$\n\n"
            f"$$F = 2 - ({V - E}) = {target_val}$$\n\n"
            f"$$\\therefore F = {target_val}\\text{{ faces}}$$\n\n"
            f"**Step 3:** The shape with {F} faces, {V} vertices, and {E} edges is a **{poly['name']}**."
        )
    elif unknown == "vertices":
        target_val = V
        prompt = (
            f"A 3D polyhedron (a {poly['name']}) has **{F} faces** and **{E} edges**.\n\n"
            f"1. State Euler's formula for convex polyhedra.\n"
            f"2. Calculate the number of vertices ($V$) of this 3D solid.\n"
            f"3. How many faces meet at each base corner?"
        )
        sol = (
            f"**Step 1:** Euler's Formula is:\n\n"
            f"$$F + V - E = 2$$\n\n"
            f"**Step 2:** Substitute $F = {F}$ and $E = {E}$:\n\n"
            f"$${F} + V - {E} = 2$$\n\n"
            f"$$V + ({F - E}) = 2$$\n\n"
            f"$$V = 2 - ({F - E}) = {target_val}$$\n\n"
            f"$$\\therefore V = {target_val}\\text{{ vertices}}$$\n\n"
            f"**Step 3:** Three faces meet at each vertex."
        )
    else: # edges
        target_val = E
        prompt = (
            f"A {poly['name']} has **{F} faces** and **{V} vertices**.\n\n"
            f"1. State Euler's formula relating faces, vertices, and edges.\n"
            f"2. Calculate the number of edges ($E$) using Euler's formula.\n"
            f"3. Verify your answer by counting the edges on its 2D net."
        )
        sol = (
            f"**Step 1:** Euler's Formula is:\n\n"
            f"$$F + V - E = 2$$\n\n"
            f"**Step 2:** Substitute $F = {F}$ and $V = {V}$:\n\n"
            f"$${F} + {V} - E = 2$$\n\n"
            f"$${F + V} - E = 2$$\n\n"
            f"$$E = {F + V} - 2 = {target_val}$$\n\n"
            f"$$\\therefore E = {target_val}\\text{{ edges}}$$\n\n"
            f"**Step 3:** When folded from the net, the shape has {target_val} edges."
        )
    
    return {
        "id": f"g7_math_euler_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(target_val),
        "answer_latex": f"{target_val}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "subskill": "eulers_formula_calculation",
        "learning_objective_id": "math_g7_3d_polyhedra_eulers_formula",
        "diagram_spec": poly["net_spec"],
        "misconception_tags": [
            "eulers_formula_subtraction_slip",
            "confusing_edges_with_vertices",
            "sign_error_transposition"
        ],
        "diagnostic_tags": ["polyhedra_properties", "eulers_formula"],
        "minimum_mastery_score": 75,
        "keywords": ["Euler's formula", "faces", "vertices", "edges", poly["name"].lower()],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of Euler's formula (F + V - E = 2)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct algebraic substitution of given parameters", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accurate rearrangement and evaluation of unknown", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Accurate identification or verification", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Recall the formula connecting faces, vertices, and edges for any 3D polyhedron.",
            "tier_2": f"Euler's Formula is F + V - E = 2. Substitute the two given numbers into this equation.",
            "tier_3": f"Substitute into F + V - E = 2 to find the missing value: answer is {target_val}."
        }
    }


def _generate_net_surface_area_question(rng: random.Random) -> Dict[str, Any]:
    """Generates a question deriving total surface area by calculating polygon areas on a 2D net."""
    shape_type = rng.choice(["triangular_prism", "rectangular_prism"])
    
    if shape_type == "triangular_prism":
        # Right triangular prism with base triangle legs a, b and hypotenuse c, prism length L
        a = rng.choice([3, 6, 5])
        b = rng.choice([4, 8, 12])
        c = int(math.sqrt(a**2 + b**2)) # Pythagorean triple (3,4,5), (6,8,10), (5,12,13)
        L = rng.randint(8, 15)
        
        area_tri = (a * b) // 2
        two_triangles = 2 * area_tri
        rect1 = a * L
        rect2 = b * L
        rect3 = c * L
        total_sa = two_triangles + rect1 + rect2 + rect3
        
        prompt = (
            f"The 2D geometric net of a right triangular prism is unfolded flat on a grid.\n"
            f"- It has **2 right-angled triangular bases** with legs of length **{a} cm** and **{b} cm** (hypotenuse **{c} cm**).\n"
            f"- The 3 rectangular lateral faces all have length **{L} cm**.\n\n"
            f"1. Calculate the area of one triangular base ($A_{{\\Delta}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}$).\n"
            f"2. Calculate the total area of the 3 rectangular faces ($A_{{\\text{{lateral}}}}$).\n"
            f"3. Hence, calculate the **Total Surface Area (TSA)** of the prism in $\\text{{cm}}^2$."
        )
        
        sol = (
            f"**Step 1:** Area of the 2 triangular bases:\n\n"
            f"$$\\text{{Area of 1 triangle}} = \\frac{{1}}{{2}} \\times {a} \\times {b} = {area_tri}\\text{{ cm}}^2$$\n\n"
            f"$$\\text{{Area of 2 triangles}} = 2 \\times {area_tri} = {two_triangles}\\text{{ cm}}^2$$\n\n"
            f"**Step 2:** Area of the 3 rectangular lateral faces:\n\n"
            f"$$\\text{{Rect}}_1 = {a} \\times {L} = {rect1}\\text{{ cm}}^2$$\n\n"
            f"$$\\text{{Rect}}_2 = {b} \\times {L} = {rect2}\\text{{ cm}}^2$$\n\n"
            f"$$\\text{{Rect}}_3 = {c} \\times {L} = {rect3}\\text{{ cm}}^2$$\n\n"
            f"$$\\text{{Total Lateral Area}} = {rect1} + {rect2} + {rect3} = {rect1 + rect2 + rect3}\\text{{ cm}}^2$$\n\n"
            f"**Step 3:** Total Surface Area (TSA):\n\n"
            f"$$\\text{{TSA}} = {two_triangles} + {rect1 + rect2 + rect3} = {total_sa}\\text{{ cm}}^2$$"
        )
        
        target_val = total_sa
        shape_name = "Right Triangular Prism"
    else:
        # Rectangular prism: l, w, h
        l = rng.randint(4, 8)
        w = rng.randint(3, 6)
        h = rng.randint(5, 10)
        
        pair1 = 2 * (l * w)
        pair2 = 2 * (l * h)
        pair3 = 2 * (w * h)
        total_sa = pair1 + pair2 + pair3
        
        prompt = (
            f"A rectangular packaging box unfolds into a 2D net of 6 rectangular faces.\n"
            f"The box dimensions are: length = **{l} cm**, width = **{w} cm**, and height = **{h} cm**.\n\n"
            f"1. Write down the formula for the total surface area of a rectangular prism from its net.\n"
            f"2. Calculate the combined area of the top and bottom faces ($2 \\times l \\times w$).\n"
            f"3. Hence, calculate the **Total Surface Area (TSA)** of cardboard required in $\\text{{cm}}^2$."
        )
        
        sol = (
            f"**Step 1:** Surface Area formula from 2D net:\n\n"
            f"$$\\text{{TSA}} = 2(lw + lh + wh)$$\n\n"
            f"**Step 2:** Calculate each pair of faces:\n\n"
            f"$$2(l \\times w) = 2({l} \\times {w}) = {pair1}\\text{{ cm}}^2$$\n\n"
            f"$$2(l \\times h) = 2({l} \\times {h}) = {pair2}\\text{{ cm}}^2$$\n\n"
            f"$$2(w \\times h) = 2({w} \\times {h}) = {pair3}\\text{{ cm}}^2$$\n\n"
            f"**Step 3:** Total Surface Area:\n\n"
            f"$$\\text{{TSA}} = {pair1} + {pair2} + {pair3} = {total_sa}\\text{{ cm}}^2$$"
        )
        
        target_val = total_sa
        shape_name = "Rectangular Prism"

    return {
        "id": f"g7_math_net_sa_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(target_val),
        "answer_latex": f"{target_val}\\text{{ cm}}^2",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "subskill": "surface_area_from_net",
        "learning_objective_id": "math_g7_3d_nets_surface_area",
        "diagram_spec": POLYHEDRA_CATALOG["triangular_prism" if shape_type == "triangular_prism" else "rectangular_prism"]["net_spec"],
        "misconception_tags": [
            "omitted_prism_base_in_surface_area",
            "volume_formula_used_for_surface_area",
            "forgot_to_multiply_paired_faces_by_two"
        ],
        "diagnostic_tags": ["surface_area", "geometric_nets", "measurement"],
        "minimum_mastery_score": 75,
        "keywords": ["surface area", "geometric net", shape_name.lower(), "faces", "cm²"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct formula for decomposing 2D net faces", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Calculation of base face areas", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculation of lateral rectangular face areas", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Accurate summation to Total Surface Area", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"The surface area is the sum of the areas of all flat faces on the unfolded 2D net.",
            "tier_2": f"Find the area of each polygon on the net, then add them together. Do not multiply height by base by length (that is volume).",
            "tier_3": f"Sum all faces: TSA = {target_val} cm²."
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 3D Objects & Geometric Nets Generator.
    Supports atomic micro-drills:
    - mode="elementary_net_identification"
    - mode="elementary_eulers_formula"
    - mode="elementary_surface_area"
    - mode="compound"
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    for _ in range(count):
        if mode == "elementary_net_identification" or subskill == "net_identification":
            q = _generate_net_identification_question(rng)
        elif mode == "elementary_eulers_formula" or subskill == "eulers_formula":
            q = _generate_eulers_formula_question(rng)
        elif mode == "elementary_surface_area" or subskill == "surface_area":
            q = _generate_net_surface_area_question(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                _generate_net_identification_question,
                _generate_eulers_formula_question,
                _generate_net_surface_area_question
            ])
            q = archetype(rng)
        questions.append(q)

    return questions
