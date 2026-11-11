"""Grade 8 Mathematics — Geometry of 3D Objects Archetypes 01 to 25.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/02. Geometry of 3D objects.md

Archetypes covering:
  - 01 to 10: Polyhedra classification vs curved solids, prisms (triangular, rectangular, cube, pentagonal, hexagonal, octagonal), general n-gon prism formulas.
  - 11 to 20: Pyramids (tetrahedron, square, rectangular, pentagonal, hexagonal), general n-gon pyramid formulas, apex, prism vs pyramid comparison.
  - 21 to 25: Euler's formula (F + V - E = 2), verification for cube, triangular prism, square pyramid, finding faces/vertices/edges algebraically.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# ----------------------------------------------------------------------
# 01. Classify Polyhedron vs Curved Solids
# ----------------------------------------------------------------------
def arch_01_classify_polyhedron_vs_curved_solids(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Classify the following 3D objects into **Polyhedra** (flat polygonal faces) and **Curved Solids**:\n\n"
        "Objects: Cube, Cylinder, Triangular Prism, Sphere, Cone, Rectangular Prism"
    )
    sol = (
        "**Definitions:**\n"
        "- A **polyhedron** is a 3D solid bounded strictly by flat polygon faces.\n"
        "- A **curved solid** contains one or more curved surfaces.\n\n"
        "**Classification:**\n"
        "- **Polyhedra:** Cube, Triangular Prism, Rectangular Prism\n"
        "- **Curved Solids:** Cylinder, Sphere, Cone"
    )
    ans = "Polyhedra: Cube, Triangular Prism, Rectangular Prism; Curved Solids: Cylinder, Sphere, Cone"
    return {
        "id": f"g8_3d_poly_vs_curv_{rng.randint(100000, 999999)}",
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
        "subskill": "01_classify_polyhedron_vs_curved_solids",
        "learning_objective_id": "math_g8_3d_poly_vs_curv",
        "hints": {
            "tier_1": "Polyhedra have only flat polygonal faces.",
            "tier_2": "Cylinders, cones, and spheres have curved surfaces.",
            "tier_3": ans,
        },
        "misconception_tags": ["classifying_cylinder_as_polyhedron"],
    }


# ----------------------------------------------------------------------
# 02. Identify Faces, Vertices, Edges Definitions
# ----------------------------------------------------------------------
def arch_02_identify_faces_vertices_edges_definitions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In three-dimensional geometry, polyhedra are defined by three distinct components:\n\n"
        "1. Define what a **face** of a polyhedron is.\n"
        "2. Define what an **edge** is.\n"
        "3. Define what a **vertex** is (and state its plural form)."
    )
    sol = (
        "**Definitions:**\n"
        "1. **Face:** A flat polygonal surface bounding a 3D solid.\n"
        "2. **Edge:** The straight line segment where two faces meet.\n"
        "3. **Vertex:** The corner point where three or more edges intersect. The plural form is **vertices**."
    )
    ans = "1. flat polygonal surface; 2. line segment where two faces meet; 3. corner point where edges meet (plural: vertices)"
    return {
        "id": f"g8_3d_fve_defs_{rng.randint(100000, 999999)}",
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
        "subskill": "02_identify_faces_vertices_edges_definitions",
        "learning_objective_id": "math_g8_3d_fve_defs",
        "hints": {
            "tier_1": "Faces are flat surfaces; edges are line segments; vertices are corners.",
            "tier_2": "Vertices is the plural of vertex.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_edges_with_vertices"],
    }


# ----------------------------------------------------------------------
# 03. Triangular Prism Properties
# ----------------------------------------------------------------------
def arch_03_triangular_prism_properties_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a standard **triangular prism**:\n\n"
        "1. Describe the shapes of its faces (bases and lateral faces).\n"
        "2. State the number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Face Shapes:**\n"
        "- 2 congruent parallel triangular bases.\n"
        "- 3 rectangular lateral faces connecting the bases.\n\n"
        "**2. Count:**\n"
        "- Faces: \\(F = 5\\)\n"
        "- Vertices: \\(V = 6\\)\n"
        "- Edges: \\(E = 9\\)"
    )
    ans = "1. 2 triangular bases and 3 rectangular lateral faces; 2. F = 5, V = 6, E = 9"
    return {
        "id": f"g8_3d_tri_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "03_triangular_prism_properties_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_tri_prism",
        "hints": {
            "tier_1": "A triangular prism has 2 triangular bases and 3 rectangle sides.",
            "tier_2": "F = 2 + 3 = 5; V = 2 * 3 = 6; E = 3 * 3 = 9.",
            "tier_3": "F = 5, V = 6, E = 9.",
        },
        "misconception_tags": ["confusing_triangular_prism_with_triangular_pyramid"],
    }


# ----------------------------------------------------------------------
# 04. Rectangular Prism (Cuboid) Properties
# ----------------------------------------------------------------------
def arch_04_rectangular_prism_cuboid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **rectangular prism (cuboid)**:\n\n"
        "1. Describe the shape of all its faces.\n"
        "2. State the count of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Face Shapes:** 6 rectangular faces, where opposite pairs of faces are congruent and parallel.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 6\\)\n"
        "- Vertices: \\(V = 8\\)\n"
        "- Edges: \\(E = 12\\)"
    )
    ans = "1. 6 rectangular faces (opposite pairs congruent); 2. F = 6, V = 8, E = 12"
    return {
        "id": f"g8_3d_cuboid_{rng.randint(100000, 999999)}",
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
        "subskill": "04_rectangular_prism_cuboid_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_cuboid",
        "hints": {
            "tier_1": "Think of a typical cardboard shoebox.",
            "tier_2": "F = 6, V = 8, E = 12.",
            "tier_3": ans,
        },
        "misconception_tags": ["counting_only_visible_edges_of_cuboid"],
    }


# ----------------------------------------------------------------------
# 05. Cube Properties: All Faces Congruent Squares
# ----------------------------------------------------------------------
def arch_05_cube_properties_all_faces_congruent_squares(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A **cube** is a special type of rectangular prism:\n\n"
        "1. What distinguishing geometric property makes a cube unique among rectangular prisms?\n"
        "2. State the values of \\(F\\), \\(V\\), and \\(E\\) for a cube."
    )
    sol = (
        "**1. Distinguishing Property:** All \\(6\\) faces are identical, congruent **squares**, "
        "and all \\(12\\) edges are of equal length.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 6\\)\n"
        "- Vertices: \\(V = 8\\)\n"
        "- Edges: \\(E = 12\\)"
    )
    ans = "1. all 6 faces are congruent squares and all 12 edges are equal in length; 2. F = 6, V = 8, E = 12"
    return {
        "id": f"g8_3d_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "05_cube_properties_all_faces_congruent_squares",
        "learning_objective_id": "math_g8_3d_cube",
        "hints": {
            "tier_1": "A cube has square faces of equal size.",
            "tier_2": "F = 6, V = 8, E = 12.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_cube_has_different_counts_of_FVE_than_cuboid"],
    }


# ----------------------------------------------------------------------
# 06. Pentagonal Prism Properties
# ----------------------------------------------------------------------
def arch_06_pentagonal_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **pentagonal prism** whose bases are 5-sided polygons:\n\n"
        "1. Describe the shapes of its two bases and its lateral faces.\n"
        "2. State the total number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Shapes:**\n"
        "- 2 congruent pentagonal bases.\n"
        "- 5 rectangular lateral faces.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 5 + 2 = 7\\)\n"
        "- Vertices: \\(V = 2 \\times 5 = 10\\)\n"
        "- Edges: \\(E = 3 \\times 5 = 15\\)"
    )
    ans = "1. 2 pentagons and 5 rectangles; 2. F = 7, V = 10, E = 15"
    return {
        "id": f"g8_3d_penta_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "06_pentagonal_prism_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_penta_prism",
        "hints": {
            "tier_1": "For an n-gonal prism: F = n + 2, V = 2n, E = 3n.",
            "tier_2": "Here n = 5.",
            "tier_3": "F = 7, V = 10, E = 15.",
        },
        "misconception_tags": ["multiplying_faces_by_3_instead_of_adding_2"],
    }


# ----------------------------------------------------------------------
# 07. Hexagonal Prism Properties
# ----------------------------------------------------------------------
def arch_07_hexagonal_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **hexagonal prism** with 6-sided polygon bases:\n\n"
        "1. How many faces, vertices, and edges does it possess?\n"
        "2. Show how the general prism formulas \\(F = n + 2\\), \\(V = 2n\\), and \\(E = 3n\\) verify these numbers."
    )
    sol = (
        "**1. Counts:**\n"
        "- Faces: \\(F = 8\\)\n"
        "- Vertices: \\(V = 12\\)\n"
        "- Edges: \\(E = 18\\)\n\n"
        "**2. Formula Verification for \\(n = 6\\):**\n"
        "- \\(F = 6 + 2 = 8\\)\n"
        "- \\(V = 2 \\times 6 = 12\\)\n"
        "- \\(E = 3 \\times 6 = 18\\)"
    )
    ans = "1. F = 8, V = 12, E = 18; 2. F = 6 + 2 = 8, V = 2(6) = 12, E = 3(6) = 18"
    return {
        "id": f"g8_3d_hexa_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "07_hexagonal_prism_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_hexa_prism",
        "hints": {
            "tier_1": "A hexagon has 6 sides (n = 6).",
            "tier_2": "F = 6 + 2 = 8; V = 2 * 6 = 12; E = 3 * 6 = 18.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_hexagon_sides_with_octagon"],
    }


# ----------------------------------------------------------------------
# 08. Octagonal Prism Properties
# ----------------------------------------------------------------------
def arch_08_octagonal_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "An **octagonal prism** has two octagonal bases (each with 8 sides):\n\n"
        "1. Calculate the number of faces (\\(F\\)).\n"
        "2. Calculate the number of vertices (\\(V\\)).\n"
        "3. Calculate the number of edges (\\(E\\))."
    )
    sol = (
        "**For an \\(n = 8\\) prism:**\n"
        "1. \\(F = n + 2 = 8 + 2 = 10\\) faces\n"
        "2. \\(V = 2n = 2 \\times 8 = 16\\) vertices\n"
        "3. \\(E = 3n = 3 \\times 8 = 24\\) edges"
    )
    ans = "F = 10, V = 16, E = 24"
    return {
        "id": f"g8_3d_octa_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "08_octagonal_prism_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_octa_prism",
        "hints": {
            "tier_1": "An octagon has n = 8 sides.",
            "tier_2": "F = 8 + 2; V = 2 * 8; E = 3 * 8.",
            "tier_3": "F = 10, V = 16, E = 24.",
        },
        "misconception_tags": ["adding_instead_of_multiplying_for_edges"],
    }


# ----------------------------------------------------------------------
# 09. General Prism Algebraic Formulas For N-Gon
# ----------------------------------------------------------------------
def arch_09_general_prism_algebraic_formulas_n_gon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "For any prism with an \\(n\\)-sided polygon base:\n\n"
        "Write algebraic expressions in terms of \\(n\\) for:\n"
        "1. Number of faces (\\(F\\))\n"
        "2. Number of vertices (\\(V\\))\n"
        "3. Number of edges (\\(E\\))"
    )
    sol = (
        "**General Formulas for an \\(n\\)-gonal Prism:**\n"
        "1. **Faces:** \\(F = n + 2\\) (2 bases + \\(n\\) rectangular sides)\n"
        "2. **Vertices:** \\(V = 2n\\) (\\(n\\) vertices on bottom base + \\(n\\) vertices on top base)\n"
        "3. **Edges:** \\(E = 3n\\) (\\(n\\) top edges + \\(n\\) bottom edges + \\(n\\) vertical connecting edges)"
    )
    ans = "1. F = n + 2; 2. V = 2n; 3. E = 3n"
    return {
        "id": f"g8_3d_gen_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "09_general_prism_algebraic_formulas_n_gon",
        "learning_objective_id": "math_g8_3d_gen_prism",
        "hints": {
            "tier_1": "2 bases add to the n lateral faces: F = n + 2.",
            "tier_2": "Vertices appear on both top and bottom bases: V = 2n.",
            "tier_3": "F = n + 2, V = 2n, E = 3n.",
        },
        "misconception_tags": ["confusing_prism_formulas_with_pyramid_formulas"],
    }


# ----------------------------------------------------------------------
# 10. Prism Cross Section Parallel to Base
# ----------------------------------------------------------------------
def arch_10_prism_cross_section_parallel_to_base(rng: random.Random) -> Dict[str, Any]:
    poly = rng.choice(["triangle", "rectangle", "hexagon", "pentagon"])
    prompt = (
        f"A right prism has a **{poly}** as its base.\n"
        f"A plane cuts through the prism parallel to its base.\n\n"
        f"1. What 2D shape is the resulting cross-section?\n"
        f"2. How does the size and shape of this cross-section compare to the prism's base?"
    )
    sol = (
        f"**1. Cross-section Shape:** A **{poly}**.\n\n"
        f"**2. Comparison:** It is **identical (congruent)** in both size and shape to the base. "
        f"A prism has a constant uniform cross-section throughout its entire height."
    )
    ans = f"1. {poly}; 2. congruent / identical in size and shape"
    return {
        "id": f"g8_3d_prism_cross_{rng.randint(100000, 999999)}",
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
        "subskill": "10_prism_cross_section_parallel_to_base",
        "learning_objective_id": "math_g8_3d_prism_cross",
        "hints": {
            "tier_1": "Prisms have uniform cross-sections along their length.",
            "tier_2": f"Cutting parallel to the base yields a shape identical to the base.",
            "tier_3": f"{poly}; congruent / identical.",
        },
        "misconception_tags": ["thinking_cross_section_shrinks_like_in_a_pyramid"],
    }


# ----------------------------------------------------------------------
# 11. Triangular Pyramid (Tetrahedron) Properties
# ----------------------------------------------------------------------
def arch_11_triangular_pyramid_tetrahedron_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **triangular pyramid** (also known as a tetrahedron):\n\n"
        "1. Describe the shape of all its faces.\n"
        "2. State the number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Face Shapes:** All 4 faces are **triangles** (1 triangular base and 3 triangular lateral faces).\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 4\\)\n"
        "- Vertices: \\(V = 4\\)\n"
        "- Edges: \\(E = 6\\)"
    )
    ans = "1. 4 triangles; 2. F = 4, V = 4, E = 6"
    return {
        "id": f"g8_3d_tetra_{rng.randint(100000, 999999)}",
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
        "subskill": "11_triangular_pyramid_tetrahedron_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_tetra",
        "hints": {
            "tier_1": "A pyramid has only 1 base.",
            "tier_2": "F = 3 + 1 = 4; V = 3 + 1 = 4; E = 2 * 3 = 6.",
            "tier_3": "F = 4, V = 4, E = 6.",
        },
        "misconception_tags": ["confusing_triangular_pyramid_with_triangular_prism"],
    }


# ----------------------------------------------------------------------
# 12. Square-Based Pyramid Properties
# ----------------------------------------------------------------------
def arch_12_square_based_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **square-based pyramid** (like the ancient Egyptian pyramids):\n\n"
        "1. Describe the shape and number of all its faces.\n"
        "2. State the count of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Face Shapes:** \\(1\\) square base and \\(4\\) triangular lateral faces that meet at the apex.\n\n"
        "**2. Counts:**\n"
        "- Faces: \\(F = 5\\) (\\(4 + 1\\))\n"
        "- Vertices: \\(V = 5\\) (\\(4\\) base corners + \\(1\\) apex)\n"
        "- Edges: \\(E = 8\\) (\\(4\\) base edges + \\(4\\) sloping edges)"
    )
    ans = "1. 1 square base and 4 triangular lateral faces; 2. F = 5, V = 5, E = 8"
    return {
        "id": f"g8_3d_sq_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "12_square_based_pyramid_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_sq_pyr",
        "hints": {
            "tier_1": "Base is a square (n = 4).",
            "tier_2": "F = 4 + 1 = 5; V = 4 + 1 = 5; E = 2 * 4 = 8.",
            "tier_3": "F = 5, V = 5, E = 8.",
        },
        "misconception_tags": ["forgetting_to_count_the_apex_as_a_vertex"],
    }


# ----------------------------------------------------------------------
# 13. Rectangular Pyramid Properties
# ----------------------------------------------------------------------
def arch_13_rectangular_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **rectangular pyramid**:\n\n"
        "1. How many faces does it have, and what are their shapes?\n"
        "2. State the number of vertices and edges."
    )
    sol = (
        "**1. Faces:** \\(5\\) faces in total: \\(1\\) rectangular base and \\(4\\) triangular lateral faces.\n\n"
        "**2. Vertices and Edges:**\n"
        "- Vertices: \\(V = 5\\) (\\(4\\) base vertices + \\(1\\) apex)\n"
        "- Edges: \\(E = 8\\) (\\(4\\) base edges + \\(4\\) slant edges)"
    )
    ans = "1. 5 faces (1 rectangle and 4 triangles); 2. V = 5, E = 8"
    return {
        "id": f"g8_3d_rect_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "13_rectangular_pyramid_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_rect_pyr",
        "hints": {
            "tier_1": "A rectangular base has 4 sides, so n = 4.",
            "tier_2": "F = 5, V = 5, E = 8.",
            "tier_3": ans,
        },
        "misconception_tags": ["assuming_rectangular_pyramid_has_more_edges_than_square_pyramid"],
    }


# ----------------------------------------------------------------------
# 14. Pentagonal Pyramid Properties
# ----------------------------------------------------------------------
def arch_14_pentagonal_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **pentagonal pyramid**:\n\n"
        "1. Identify the shape of the base.\n"
        "2. State the total number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\))."
    )
    sol = (
        "**1. Base shape:** A **pentagon** (\\(5\\) sides).\n\n"
        "**2. Counts (using \\(n = 5\\)):**\n"
        "- Faces: \\(F = n + 1 = 5 + 1 = 6\\)\n"
        "- Vertices: \\(V = n + 1 = 5 + 1 = 6\\)\n"
        "- Edges: \\(E = 2n = 2 \\times 5 = 10\\)"
    )
    ans = "1. pentagon; 2. F = 6, V = 6, E = 10"
    return {
        "id": f"g8_3d_penta_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "14_pentagonal_pyramid_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_penta_pyr",
        "hints": {
            "tier_1": "For an n-gonal pyramid: F = n + 1, V = n + 1, E = 2n.",
            "tier_2": "Here n = 5.",
            "tier_3": "F = 6, V = 6, E = 10.",
        },
        "misconception_tags": ["multiplying_edges_by_3_instead_of_2_for_pyramid"],
    }


# ----------------------------------------------------------------------
# 15. Hexagonal Pyramid Properties
# ----------------------------------------------------------------------
def arch_15_hexagonal_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a **hexagonal pyramid**:\n\n"
        "1. State the number of faces (\\(F\\)).\n"
        "2. State the number of vertices (\\(V\\)).\n"
        "3. State the number of edges (\\(E\\))."
    )
    sol = (
        "**For a hexagonal pyramid (\\(n = 6\\)):**\n"
        "1. \\(F = n + 1 = 6 + 1 = 7\\)\n"
        "2. \\(V = n + 1 = 6 + 1 = 7\\)\n"
        "3. \\(E = 2n = 2 \\times 6 = 12\\)"
    )
    ans = "F = 7, V = 7, E = 12"
    return {
        "id": f"g8_3d_hexa_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "15_hexagonal_pyramid_faces_vertices_edges",
        "learning_objective_id": "math_g8_3d_hexa_pyr",
        "hints": {
            "tier_1": "Hexagon has 6 sides (n = 6).",
            "tier_2": "F = 6 + 1; V = 6 + 1; E = 2 * 6.",
            "tier_3": "F = 7, V = 7, E = 12.",
        },
        "misconception_tags": ["using_prism_formulas_instead_of_pyramid"],
    }


# ----------------------------------------------------------------------
# 16. General Pyramid Algebraic Formulas For N-Gon
# ----------------------------------------------------------------------
def arch_16_general_pyramid_algebraic_formulas_n_gon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "For any pyramid with an \\(n\\)-sided polygon base:\n\n"
        "Write algebraic expressions in terms of \\(n\\) for:\n"
        "1. Number of faces (\\(F\\))\n"
        "2. Number of vertices (\\(V\\))\n"
        "3. Number of edges (\\(E\\))"
    )
    sol = (
        "**General Formulas for an \\(n\\)-gonal Pyramid:**\n"
        "1. **Faces:** \\(F = n + 1\\) (1 base + \\(n\\) triangular lateral faces)\n"
        "2. **Vertices:** \\(V = n + 1\\) (\\(n\\) base vertices + 1 apex)\n"
        "3. **Edges:** \\(E = 2n\\) (\\(n\\) base perimeter edges + \\(n\\) slant edges meeting at apex)"
    )
    ans = "1. F = n + 1; 2. V = n + 1; 3. E = 2n"
    return {
        "id": f"g8_3d_gen_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "16_general_pyramid_algebraic_formulas_n_gon",
        "learning_objective_id": "math_g8_3d_gen_pyr",
        "hints": {
            "tier_1": "A pyramid has 1 base polygon + n triangle sides.",
            "tier_2": "Apex adds 1 vertex to the n base vertices.",
            "tier_3": "F = n + 1, V = n + 1, E = 2n.",
        },
        "misconception_tags": ["writing_3n_for_edges_of_pyramid"],
    }


# ----------------------------------------------------------------------
# 17. Apex of Pyramid Definition and Properties
# ----------------------------------------------------------------------
def arch_17_apex_of_pyramid_definition_and_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the geometry of pyramids, the term **apex** is frequently used:\n\n"
        "1. Define what the apex of a pyramid is.\n"
        "2. Do prisms possess an apex? Explain why or why not."
    )
    sol = (
        "**1. Apex Definition:** The apex is the single top vertex of a pyramid where all the triangular lateral faces meet, "
        "positioned opposite to the base.\n\n"
        "**2. Prisms:** **No**, prisms do not have an apex because they have two parallel congruent bases connected "
        "by rectangular sides, rather than tapering to a single point."
    )
    ans = "1. top vertex opposite the base where triangular lateral faces meet; 2. no, prisms have two parallel bases"
    return {
        "id": f"g8_3d_apex_{rng.randint(100000, 999999)}",
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
        "subskill": "17_apex_of_pyramid_definition_and_properties",
        "learning_objective_id": "math_g8_3d_apex",
        "hints": {
            "tier_1": "Apex is the peak/point at the top of a pyramid.",
            "tier_2": "Prisms have two flat ends, not a single peak point.",
            "tier_3": ans,
        },
        "misconception_tags": ["claiming_prisms_have_an_apex"],
    }


# ----------------------------------------------------------------------
# 18. Compare Prism vs Pyramid Properties
# ----------------------------------------------------------------------
def arch_18_compare_prism_vs_pyramid_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Contrast the fundamental geometric structural differences between a **prism** and a **pyramid**:\n\n"
        "1. Compare their bases (number and relationship).\n"
        "2. Compare the shape of their lateral faces."
    )
    sol = (
        "**1. Bases:**\n"
        "- A **prism** has **two** identical, congruent, parallel bases.\n"
        "- A **pyramid** has only **one** base.\n\n"
        "**2. Lateral Faces:**\n"
        "- A prism's lateral faces are **parallelograms / rectangles**.\n"
        "- A pyramid's lateral faces are **triangles** meeting at the apex."
    )
    ans = "1. prism has 2 parallel congruent bases, pyramid has 1 base; 2. prism has rectangular lateral faces, pyramid has triangular lateral faces"
    return {
        "id": f"g8_3d_comp_prism_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "18_compare_prism_vs_pyramid_properties",
        "learning_objective_id": "math_g8_3d_comp_prism_pyr",
        "hints": {
            "tier_1": "Count the number of bases: prism has 2, pyramid has 1.",
            "tier_2": "Look at the sides: prism has rectangles, pyramid has triangles.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_pyramids_have_two_bases"],
    }


# ----------------------------------------------------------------------
# 19. Right Pyramid vs Oblique Pyramid Concept
# ----------------------------------------------------------------------
def arch_19_right_pyramid_vs_oblique_pyramid_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Pyramids are classified as either **right** or **oblique**:\n\n"
        "1. Define what a **right pyramid** is with respect to the position of its apex and the center of its base.\n"
        "2. How does an **oblique pyramid** differ?"
    )
    sol = (
        "**1. Right Pyramid:** In a right pyramid, the apex lies directly above the geometric center (centroid) "
        "of the base; the altitude line dropped from the apex meets the base at a right angle (\\(90^\\circ\\)) at the center.\n\n"
        "**2. Oblique Pyramid:** In an oblique pyramid, the apex is tilted or shifted away from the center of the base, "
        "so the line connecting the apex to the center is not perpendicular to the base."
    )
    ans = "1. apex is directly above the center of base forming 90° with base; 2. apex is tilted/shifted away from center"
    return {
        "id": f"g8_3d_right_vs_oblique_{rng.randint(100000, 999999)}",
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
        "subskill": "19_right_pyramid_vs_oblique_pyramid_concept",
        "learning_objective_id": "math_g8_3d_right_vs_oblique",
        "hints": {
            "tier_1": "'Right' means perpendicular (90°).",
            "tier_2": "Apex directly above center vs slanted/tilted.",
            "tier_3": ans,
        },
        "misconception_tags": ["thinking_oblique_pyramids_cannot_exist"],
    }


# ----------------------------------------------------------------------
# 20. Pyramid Cross Section Parallel to Base
# ----------------------------------------------------------------------
def arch_20_pyramid_cross_section_parallel_to_base(rng: random.Random) -> Dict[str, Any]:
    poly = rng.choice(["square", "triangle", "pentagon"])
    prompt = (
        f"A right pyramid has a **{poly}** as its base.\n"
        f"A horizontal plane cuts through the pyramid halfway up its height parallel to the base.\n\n"
        f"1. What 2D shape is the cross-section?\n"
        f"2. Is this cross-section congruent to the base, or similar to the base? Explain."
    )
    sol = (
        f"**1. Cross-section Shape:** A **{poly}**.\n\n"
        f"**2. Congruent or Similar:** It is **similar** to the base, but **not congruent**. "
        f"Because the pyramid tapers towards the apex, cutting parallel to the base yields a smaller scaled version "
        f"of the base polygon (same angles, proportional sides)."
    )
    ans = f"1. {poly}; 2. similar (smaller version, not congruent because pyramid tapers)"
    return {
        "id": f"g8_3d_pyr_cross_{rng.randint(100000, 999999)}",
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
        "subskill": "20_pyramid_cross_section_parallel_to_base",
        "learning_objective_id": "math_g8_3d_pyr_cross",
        "hints": {
            "tier_1": "The cross-section has the same polygon shape as the base.",
            "tier_2": "Because the pyramid tapers, the cross-section is smaller: similar, not congruent.",
            "tier_3": f"{poly}; similar.",
        },
        "misconception_tags": ["thinking_pyramid_cross_section_is_congruent_to_base"],
    }


# ----------------------------------------------------------------------
# 21. Euler's Formula Statement and Variables
# ----------------------------------------------------------------------
def arch_21_eulers_formula_statement_and_variables(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Leonhard Euler discovered a famous mathematical relationship connecting the parts of any convex polyhedron:\n\n"
        "1. State **Euler's Formula** for polyhedra.\n"
        "2. Identify what each letter in the formula represents."
    )
    sol = (
        "**1. Euler's Formula:**\n"
        "\\[ F + V - E = 2 \\quad \\text{or} \\quad F + V = E + 2 \\]\n\n"
        "**2. Variable Identification:**\n"
        "- \\(F\\) = Number of **Faces**\n"
        "- \\(V\\) = Number of **Vertices**\n"
        "- \\(E\\) = Number of **Edges**"
    )
    ans = "1. F + V - E = 2 (or F + V = E + 2); 2. F = faces, V = vertices, E = edges"
    return {
        "id": f"g8_3d_euler_stmt_{rng.randint(100000, 999999)}",
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
        "subskill": "21_eulers_formula_statement_and_variables",
        "learning_objective_id": "math_g8_3d_euler_stmt",
        "hints": {
            "tier_1": "Euler's formula relates Faces, Vertices, and Edges.",
            "tier_2": "F + V - E = 2.",
            "tier_3": ans,
        },
        "misconception_tags": ["writing_F_plus_E_minus_V_equals_2"],
    }


# ----------------------------------------------------------------------
# 22. Euler's Formula Verify Cube and Cuboid
# ----------------------------------------------------------------------
def arch_22_eulers_formula_verify_cube_and_cuboid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Verify Euler's Formula for a rectangular prism (cuboid) where \\(F = 6\\), \\(V = 8\\), and \\(E = 12\\):\n\n"
        "1. Write down Euler's Formula.\n"
        "2. Substitute the values and show that the left-hand side equals 2."
    )
    sol = (
        "**1. Euler's Formula:** \\(F + V - E = 2\\)\n\n"
        "**2. Substitution:**\n"
        "\\[ \\text{LHS} = 6 + 8 - 12 = 14 - 12 = 2 \\]\n"
        "Since \\(\\text{LHS} = \\text{RHS} = 2\\), Euler's formula is verified for the cuboid."
    )
    ans = "F + V - E = 6 + 8 - 12 = 2 (verified)"
    return {
        "id": f"g8_3d_euler_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "22_eulers_formula_verify_cube_and_cuboid",
        "learning_objective_id": "math_g8_3d_euler_cube",
        "hints": {
            "tier_1": "Add F and V, then subtract E.",
            "tier_2": "6 + 8 - 12.",
            "tier_3": "14 - 12 = 2.",
        },
        "misconception_tags": ["subtracting_vertices_instead_of_edges"],
    }


# ----------------------------------------------------------------------
# 23. Euler's Formula Verify Triangular Prism
# ----------------------------------------------------------------------
def arch_23_eulers_formula_verify_triangular_prism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A triangular prism has \\(F = 5\\) faces and \\(V = 6\\) vertices.\n\n"
        "1. How many edges (\\(E\\)) does it have?\n"
        "2. Demonstrate step-by-step that these values satisfy Euler's Formula \\(F + V - E = 2\\)."
    )
    sol = (
        "**1. Number of Edges:** \\(E = 9\\).\n\n"
        "**2. Verification:**\n"
        "\\[ F + V - E = 5 + 6 - 9 = 11 - 9 = 2 \\]\n"
        "The formula holds true."
    )
    ans = "1. E = 9; 2. 5 + 6 - 9 = 11 - 9 = 2"
    return {
        "id": f"g8_3d_euler_tri_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "23_eulers_formula_verify_triangular_prism",
        "learning_objective_id": "math_g8_3d_euler_tri_prism",
        "hints": {
            "tier_1": "A triangular prism has 9 edges.",
            "tier_2": "5 + 6 - 9 = 2.",
            "tier_3": ans,
        },
        "misconception_tags": ["miscounting_edges_of_triangular_prism"],
    }


# ----------------------------------------------------------------------
# 24. Euler's Formula Verify Square Pyramid
# ----------------------------------------------------------------------
def arch_24_eulers_formula_verify_square_pyramid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A square-based pyramid has \\(5\\) faces and \\(5\\) vertices.\n\n"
        "1. State the number of edges (\\(E\\)).\n"
        "2. Substitute into \\(F + V - E\\) to verify Euler's formula."
    )
    sol = (
        "**1. Edges:** \\(E = 8\\) (\\(4\\) base edges + \\(4\\) slant edges).\n\n"
        "**2. Verification:**\n"
        "\\[ F + V - E = 5 + 5 - 8 = 10 - 8 = 2 \\]\n"
        "Euler's formula is satisfied."
    )
    ans = "1. E = 8; 2. 5 + 5 - 8 = 10 - 8 = 2"
    return {
        "id": f"g8_3d_euler_sq_pyr_{rng.randint(100000, 999999)}",
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
        "subskill": "24_eulers_formula_verify_square_pyramid",
        "learning_objective_id": "math_g8_3d_euler_sq_pyr",
        "hints": {
            "tier_1": "Square pyramid has 8 edges.",
            "tier_2": "5 + 5 - 8 = 2.",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_edges_instead_of_subtracting_in_euler"],
    }


# ----------------------------------------------------------------------
# 25. Euler's Formula: Find Faces Given Vertices and Edges
# ----------------------------------------------------------------------
def arch_25_eulers_formula_find_faces_given_vertices_and_edges(rng: random.Random) -> Dict[str, Any]:
    # (v, e) -> f = e - v + 2
    v, e, name = rng.choice([
        (10, 15, "pentagonal prism"),
        (12, 18, "hexagonal prism"),
        (6, 10, "pentagonal pyramid"),
        (7, 12, "hexagonal pyramid"),
        (20, 30, "dodecahedron"),
    ])
    f = e - v + 2

    prompt = (
        f"A polyhedron has **\\(V = {v}\\)** vertices and **\\(E = {e}\\)** edges.\n\n"
        f"1. Rearrange Euler's Formula \\(F + V - E = 2\\) to make \\(F\\) the subject of the formula.\n"
        f"2. Calculate the number of faces (\\(F\\)) of this polyhedron."
    )
    sol = (
        f"**1. Formula rearrangement:**\n"
        f"\\[ F = E - V + 2 \\]\n\n"
        f"**2. Calculation:**\n"
        f"\\[ F = {e} - {v} + 2 = {e - v} + 2 = {f} \\]\n"
        f"The polyhedron has **{f}** faces."
    )
    ans = f"1. F = E - V + 2; 2. F = {f}"
    return {
        "id": f"g8_3d_find_f_{rng.randint(100000, 999999)}",
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
        "subskill": "25_eulers_formula_find_faces_given_vertices_and_edges",
        "learning_objective_id": "math_g8_3d_find_f",
        "hints": {
            "tier_1": "F = E - V + 2.",
            "tier_2": f"F = {e} - {v} + 2.",
            "tier_3": f"F = {f}.",
        },
        "misconception_tags": ["subtracting_2_instead_of_adding_2_in_rearrangement"],
    }
