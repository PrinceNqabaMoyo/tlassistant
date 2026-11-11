"""Grade 7 Mathematics - Geometry of 3D Objects: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Geometry of 3D objects.md
Focus: Polyhedra vs curved solids, prisms vs pyramids, Platonic solids, properties (F, V, E), Euler's formula, and general n-gon formulas.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Classify polyhedron vs curved solid
def arch_01_classify_polyhedron_vs_curved_solid(rng: random.Random) -> Dict[str, Any]:
    ans = "Polyhedron: Cube, Triangular Prism; Curved Solid: Cylinder, Sphere"
    prompt = (
        "Classify the following 3D shapes into **Polyhedra** (flat polygonal faces) and **Curved Solids**:\n\n"
        "Shapes: Cube, Cylinder, Triangular Prism, Sphere"
    )
    sol = (
        "**Definitions:**\n"
        "- A **polyhedron** is a 3D solid bounded strictly by flat polygon faces.\n"
        "- A **curved solid** contains one or more curved surfaces.\n\n"
        "**Classification:**\n"
        "- **Polyhedra:** Cube, Triangular Prism\n"
        "- **Curved Solids:** Cylinder, Sphere"
    )
    return {
        "id": f"g7_g3d_01_{rng.randint(100000, 999999)}",
        "subskill": "01_classify_polyhedron_vs_curved_solid",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_01",
        "hints": {"tier_1": "Polyhedra have only flat polygonal faces.", "tier_2": "Cylinder and sphere have curved surfaces.", "tier_3": ans},
        "misconception_tags": ["classifying_cylinder_as_polyhedron"]
    }


# 02. Classify prism vs pyramid distinction
def arch_02_classify_prism_vs_pyramid_distinction(rng: random.Random) -> Dict[str, Any]:
    ans = "A prism has two identical parallel bases and rectangular lateral faces; a pyramid has one base and triangular faces meeting at an apex."
    prompt = (
        "Explain the geometric differences between a **Prism** and a **Pyramid**."
    )
    sol = (
        "**Key Differences:**\n"
        "1. **Bases:** A **prism** has two congruent (identical) parallel bases, whereas a **pyramid** has only one base.\n"
        "2. **Side faces:** The lateral faces of a prism are rectangles (or parallelograms), while the lateral faces of a pyramid are triangles that meet at a common top point called the **apex**."
    )
    return {
        "id": f"g7_g3d_02_{rng.randint(100000, 999999)}",
        "subskill": "02_classify_prism_vs_pyramid_distinction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_02",
        "hints": {"tier_1": "How many bases does each have? What shape are the sides?", "tier_2": "Prism: 2 bases. Pyramid: 1 base + apex.", "tier_3": ans},
        "misconception_tags": ["confusing_prism_and_pyramid"]
    }


# 03. Cube faces vertices edges
def arch_03_cube_net(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 6, Vertices = 8, Edges = 12"
    prompt = (
        "State the number of faces (\\(F\\)), vertices (\\(V\\)), and edges (\\(E\\)) of a **Cube**, "
        "and describe the shape of its faces."
    )
    sol = (
        "**Properties of a Cube:**\n"
        "- **Faces (\\(F\\)):** 6 (all congruent squares)\n"
        "- **Vertices (\\(V\\)):** 8 corner points\n"
        "- **Edges (\\(E\\)):** 12 straight line segments\n\n"
        "Result: **Faces = 6, Vertices = 8, Edges = 12**."
    )
    return {
        "id": f"g7_g3d_03_{rng.randint(100000, 999999)}",
        "subskill": "03_cube_net",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_03",
        "hints": {"tier_1": "Think of a normal playing die.", "tier_2": "F=6, V=8, E=12.", "tier_3": ans},
        "misconception_tags": ["confusing_vertices_and_edges_of_cube"]
    }


# 04. Rectangular prism faces vertices edges
def arch_04_rectangular_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 6, Vertices = 8, Edges = 12; shape: rectangles"
    prompt = (
        "For a **Rectangular Prism** (cuboid):\n"
        "1. How many faces, vertices, and edges does it have?\n"
        "2. What geometric shape are its faces?"
    )
    sol = (
        "**Properties of a Rectangular Prism:**\n"
        "- **Faces (\\(F\\)):** 6\n"
        "- **Vertices (\\(V\\)):** 8\n"
        "- **Edges (\\(E\\)):** 12\n"
        "- **Shape:** Rectangles (with opposite faces congruent)."
    )
    return {
        "id": f"g7_g3d_04_{rng.randint(100000, 999999)}",
        "subskill": "04_rectangular_prism_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_04",
        "hints": {"tier_1": "Think of a cereal box.", "tier_2": "F=6, V=8, E=12.", "tier_3": ans},
        "misconception_tags": ["confusing_cube_and_rectangular_prism_faces"]
    }


# 05. Triangular prism faces vertices edges
def arch_05_triangular_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 5, Vertices = 6, Edges = 9"
    prompt = (
        "A **Triangular Prism** has two triangular bases.\n\n"
        "1. How many faces does it have, and what shapes are they?\n"
        "2. How many vertices and edges does it have?"
    )
    sol = (
        "**Properties of a Triangular Prism:**\n"
        "- **Faces (\\(F\\)):** 5 (2 triangular bases + 3 rectangular sides)\n"
        "- **Vertices (\\(V\\)):** 6\n"
        "- **Edges (\\(E\\)):** 9 (3 base edges + 3 top edges + 3 vertical edges)\n\n"
        "Result: **Faces = 5, Vertices = 6, Edges = 9**."
    )
    return {
        "id": f"g7_g3d_05_{rng.randint(100000, 999999)}",
        "subskill": "05_triangular_prism_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_05",
        "hints": {"tier_1": "2 triangles + 3 rectangles.", "tier_2": "F=5, V=6, E=9.", "tier_3": ans},
        "misconception_tags": ["triangular_prism_edge_count_error"]
    }


# 06. Square pyramid faces vertices edges
def arch_06_square_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 5, Vertices = 5, Edges = 8"
    prompt = (
        "Determine the number of faces, vertices, and edges of a **Square-based Pyramid**."
    )
    sol = (
        "**Properties of a Square-based Pyramid:**\n"
        "- **Faces (\\(F\\)):** 5 (1 square base + 4 triangular sides)\n"
        "- **Vertices (\\(V\\)):** 5 (4 base corners + 1 apex)\n"
        "- **Edges (\\(E\\)):** 8 (4 base edges + 4 slanting edges)\n\n"
        "Result: **Faces = 5, Vertices = 5, Edges = 8**."
    )
    return {
        "id": f"g7_g3d_06_{rng.randint(100000, 999999)}",
        "subskill": "06_square_pyramid_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_06",
        "hints": {"tier_1": "Think of the Egyptian pyramids.", "tier_2": "F=5, V=5, E=8.", "tier_3": ans},
        "misconception_tags": ["counting_apex_separately_from_vertices"]
    }


# 07. Tetrahedron faces vertices edges
def arch_07_tetrahedron_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 4, Vertices = 4, Edges = 6"
    prompt = (
        "A **Tetrahedron** (triangular-based pyramid) is made of triangles.\n\n"
        "State its number of faces, vertices, and edges."
    )
    sol = (
        "**Properties of a Tetrahedron:**\n"
        "- **Faces (\\(F\\)):** 4 (all triangles)\n"
        "- **Vertices (\\(V\\)):** 4\n"
        "- **Edges (\\(E\\)):** 6\n\n"
        "Result: **Faces = 4, Vertices = 4, Edges = 6**."
    )
    return {
        "id": f"g7_g3d_07_{rng.randint(100000, 999999)}",
        "subskill": "07_tetrahedron_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_07",
        "hints": {"tier_1": "Triangular base pyramid.", "tier_2": "F=4, V=4, E=6.", "tier_3": ans},
        "misconception_tags": ["confusing_tetrahedron_with_square_pyramid"]
    }


# 08. Pentagonal prism faces vertices edges
def arch_08_pentagonal_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 7, Vertices = 10, Edges = 15"
    prompt = (
        "A **Pentagonal Prism** has two regular pentagons as its bases.\n\n"
        "How many faces, vertices, and edges does it have?"
    )
    sol = (
        "**Properties for a 5-sided base prism (\\(n = 5\\)):**\n"
        "- **Faces:** \\(F = n + 2 = 5 + 2 = \\mathbf{7}\\)\n"
        "- **Vertices:** \\(V = 2n = 2(5) = \\mathbf{10}\\)\n"
        "- **Edges:** \\(E = 3n = 3(5) = \\mathbf{15}\\)\n\n"
        "Result: **Faces = 7, Vertices = 10, Edges = 15**."
    )
    return {
        "id": f"g7_g3d_08_{rng.randint(100000, 999999)}",
        "subskill": "08_pentagonal_prism_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_08",
        "hints": {"tier_1": "Use n-gonal prism formulas: F=n+2, V=2n, E=3n.", "tier_2": "For n=5: F=7, V=10, E=15.", "tier_3": ans},
        "misconception_tags": ["pentagonal_prism_vertex_counting_error"]
    }


# 09. Hexagonal prism faces vertices edges
def arch_09_hexagonal_prism_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 8, Vertices = 12, Edges = 18"
    prompt = (
        "Determine the number of faces, vertices, and edges of a **Hexagonal Prism**."
    )
    sol = (
        "**For \\(n = 6\\) (hexagon bases):**\n"
        "- **Faces:** \\(F = 6 + 2 = \\mathbf{8}\\) (2 hexagons + 6 rectangles)\n"
        "- **Vertices:** \\(V = 2 \\times 6 = \\mathbf{12}\\)\n"
        "- **Edges:** \\(E = 3 \\times 6 = \\mathbf{18}\\)\n\n"
        "Result: **Faces = 8, Vertices = 12, Edges = 18**."
    )
    return {
        "id": f"g7_g3d_09_{rng.randint(100000, 999999)}",
        "subskill": "09_hexagonal_prism_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_09",
        "hints": {"tier_1": "Hexagon has 6 sides.", "tier_2": "F=8, V=12, E=18.", "tier_3": ans},
        "misconception_tags": ["hexagonal_prism_edge_counting_error"]
    }


# 10. Pentagonal pyramid faces vertices edges
def arch_10_pentagonal_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 6, Vertices = 6, Edges = 10"
    prompt = (
        "For a **Pentagonal Pyramid** (with a 5-sided base):\n\n"
        "Find the number of faces, vertices, and edges."
    )
    sol = (
        "**Formulas for an \\(n\\)-sided pyramid (\\(n = 5\\)):**\n"
        "- **Faces:** \\(F = n + 1 = 5 + 1 = \\mathbf{6}\\)\n"
        "- **Vertices:** \\(V = n + 1 = 5 + 1 = \\mathbf{6}\\)\n"
        "- **Edges:** \\(E = 2n = 2(5) = \\mathbf{10}\\)\n\n"
        "Result: **Faces = 6, Vertices = 6, Edges = 10**."
    )
    return {
        "id": f"g7_g3d_10_{rng.randint(100000, 999999)}",
        "subskill": "10_pentagonal_pyramid_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_10",
        "hints": {"tier_1": "Pyramid: F = n+1, V = n+1, E = 2n.", "tier_2": "For n=5: F=6, V=6, E=10.", "tier_3": ans},
        "misconception_tags": ["confusing_pentagonal_pyramid_with_prism"]
    }


# 11. Hexagonal pyramid faces vertices edges
def arch_11_hexagonal_pyramid_faces_vertices_edges(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 7, Vertices = 7, Edges = 12"
    prompt = (
        "State the number of faces, vertices, and edges of a **Hexagonal Pyramid**."
    )
    sol = (
        "**For \\(n = 6\\) (hexagonal base pyramid):**\n"
        "- **Faces:** \\(F = 6 + 1 = \\mathbf{7}\\)\n"
        "- **Vertices:** \\(V = 6 + 1 = \\mathbf{7}\\)\n"
        "- **Edges:** \\(E = 2 \\times 6 = \\mathbf{12}\\)\n\n"
        "Result: **Faces = 7, Vertices = 7, Edges = 12**."
    )
    return {
        "id": f"g7_g3d_11_{rng.randint(100000, 999999)}",
        "subskill": "11_hexagonal_pyramid_faces_vertices_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_11",
        "hints": {"tier_1": "Base has 6 edges. Lateral edges = 6.", "tier_2": "F=7, V=7, E=12.", "tier_3": ans},
        "misconception_tags": ["pyramid_edge_counting_error"]
    }


# 12. Octahedron Platonic solid properties
def arch_12_octahedron_platonic_solid_properties(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 8, Vertices = 6, Edges = 12; shape: equilateral triangles"
    prompt = (
        "A regular **Octahedron** is one of the five Platonic solids.\n\n"
        "1. How many faces, vertices, and edges does an octahedron have?\n"
        "2. What regular polygon forms all its faces?"
    )
    sol = (
        "**Properties of a Regular Octahedron:**\n"
        "- **Faces (\\(F\\)):** 8\n"
        "- **Vertices (\\(V\\)):** 6\n"
        "- **Edges (\\(E\\)):** 12\n"
        "- **Face Shape:** Equilateral triangles (all 8 faces are congruent equilateral triangles)."
    )
    return {
        "id": f"g7_g3d_12_{rng.randint(100000, 999999)}",
        "subskill": "12_octahedron_platonic_solid_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_12",
        "hints": {"tier_1": "Octa- means 8 faces.", "tier_2": "F=8, V=6, E=12.", "tier_3": ans},
        "misconception_tags": ["confusing_octahedron_faces_with_vertices"]
    }


# 13. Dodecahedron Platonic solid properties
def arch_13_dodecahedron_platonic_solid_properties(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 12, Vertices = 20, Edges = 30; shape: regular pentagons"
    prompt = (
        "Describe the geometric properties of a regular **Dodecahedron**:\n"
        "1. Number of faces, vertices, and edges.\n"
        "2. Shape of each face."
    )
    sol = (
        "**Properties of a Regular Dodecahedron:**\n"
        "- **Faces (\\(F\\)):** 12\n"
        "- **Vertices (\\(V\\)):** 20\n"
        "- **Edges (\\(E\\)):** 30\n"
        "- **Face shape:** Regular pentagons (5-sided regular polygons)."
    )
    return {
        "id": f"g7_g3d_13_{rng.randint(100000, 999999)}",
        "subskill": "13_dodecahedron_platonic_solid_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_13",
        "hints": {"tier_1": "Dodeca- means 12 faces.", "tier_2": "F=12, V=20, E=30.", "tier_3": ans},
        "misconception_tags": ["confusing_dodecahedron_with_icosahedron"]
    }


# 14. Icosahedron Platonic solid properties
def arch_14_icosahedron_platonic_solid_properties(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = 20, Vertices = 12, Edges = 30; shape: equilateral triangles"
    prompt = (
        "State the number of faces, vertices, edges, and the face shape of a regular **Icosahedron**."
    )
    sol = (
        "**Properties of a Regular Icosahedron:**\n"
        "- **Faces (\\(F\\)):** 20 (equilateral triangles)\n"
        "- **Vertices (\\(V\\)):** 12\n"
        "- **Edges (\\(E\\)):** 30\n"
        "- **Face Shape:** Equilateral triangles."
    )
    return {
        "id": f"g7_g3d_14_{rng.randint(100000, 999999)}",
        "subskill": "14_icosahedron_platonic_solid_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_14",
        "hints": {"tier_1": "Icosa- means 20 faces.", "tier_2": "F=20, V=12, E=30.", "tier_3": ans},
        "misconception_tags": ["icosahedron_property_confusion"]
    }


# 15. Cylinder properties curved surfaces
def arch_15_cylinder_properties_curved_surfaces(rng: random.Random) -> Dict[str, Any]:
    ans = "2 circular flat faces, 1 curved surface, 2 circular edges, 0 vertices"
    prompt = (
        "Describe the surfaces, edges, and vertices of a **Cylinder**."
    )
    sol = (
        "**Properties of a Cylinder:**\n"
        "- **Flat faces:** 2 identical circular bases (top and bottom)\n"
        "- **Curved surfaces:** 1 curved side surface\n"
        "- **Edges:** 2 circular curved edges\n"
        "- **Vertices:** 0 vertices (corners)."
    )
    return {
        "id": f"g7_g3d_15_{rng.randint(100000, 999999)}",
        "subskill": "15_cylinder_properties_curved_surfaces",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_15",
        "hints": {"tier_1": "Think of a cooldrink can.", "tier_2": "2 flat circles, 1 curved surface, 0 vertices.", "tier_3": ans},
        "misconception_tags": ["thinking_a_cylinder_has_vertices"]
    }


# 16. Cone properties curved surfaces
def arch_16_cone_properties_curved_surfaces(rng: random.Random) -> Dict[str, Any]:
    ans = "1 flat circular base, 1 curved surface, 1 apex, 1 circular edge"
    prompt = (
        "What are the geometric features of a **Cone**?"
    )
    sol = (
        "**Properties of a Cone:**\n"
        "- 1 flat circular base\n"
        "- 1 curved side surface that tapers to a point\n"
        "- 1 apex (top vertex)\n"
        "- 1 circular boundary edge."
    )
    return {
        "id": f"g7_g3d_16_{rng.randint(100000, 999999)}",
        "subskill": "16_cone_properties_curved_surfaces",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_16",
        "hints": {"tier_1": "Think of an ice cream cone.", "tier_2": "1 circular base, 1 apex.", "tier_3": ans},
        "misconception_tags": ["calling_cone_a_pyramid"]
    }


# 17. Sphere properties curved surfaces
def arch_17_sphere_properties_curved_surfaces(rng: random.Random) -> Dict[str, Any]:
    ans = "1 continuous curved surface, 0 flat faces, 0 edges, 0 vertices"
    prompt = (
        "How many flat faces, curved surfaces, edges, and vertices does a **Sphere** possess?"
    )
    sol = (
        "**Properties of a Sphere:**\n"
        "- Flat faces: 0\n"
        "- Curved surface: 1 continuous surface equidistant from center\n"
        "- Edges: 0\n"
        "- Vertices: 0."
    )
    return {
        "id": f"g7_g3d_17_{rng.randint(100000, 999999)}",
        "subskill": "17_sphere_properties_curved_surfaces",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_g3d_17",
        "hints": {"tier_1": "Think of a soccer ball.", "tier_2": "0 faces, 0 edges, 0 vertices.", "tier_3": ans},
        "misconception_tags": ["thinking_sphere_has_edges"]
    }


# 18. Euler's formula verify cube
def arch_18_eulers_formula_calculation(rng: random.Random) -> Dict[str, Any]:
    ans = "F + V - E = 6 + 8 - 12 = 2. Verified."
    prompt = (
        "Verify **Euler's Formula** (\\(F + V - E = 2\\)) for a **Cube**."
    )
    sol = (
        "**Step 1:** State the counts for a cube:\n"
        "- Faces \\(F = 6\\)\n"
        "- Vertices \\(V = 8\\)\n"
        "- Edges \\(E = 12\\)\n\n"
        "**Step 2:** Substitute into Euler's formula:\n"
        "$$F + V - E = 6 + 8 - 12 = 14 - 12 = \\mathbf{2}$$\n\n"
        "Since the result equals 2, Euler's formula is **verified**."
    )
    return {
        "id": f"g7_g3d_18_{rng.randint(100000, 999999)}",
        "subskill": "18_eulers_formula_calculation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_18",
        "hints": {"tier_1": "F=6, V=8, E=12.", "tier_2": "6 + 8 - 12 = 2.", "tier_3": ans},
        "misconception_tags": ["eulers_formula_sign_error"]
    }


# 19. Euler's formula verify triangular prism
def arch_19_eulers_formula_verify_triangular_prism(rng: random.Random) -> Dict[str, Any]:
    ans = "F + V - E = 5 + 6 - 9 = 2. Verified."
    prompt = (
        "Show that Euler's formula \\(F + V - E = 2\\) holds for a **Triangular Prism**."
    )
    sol = (
        "**Step 1:** For a triangular prism: \\(F = 5\\), \\(V = 6\\), \\(E = 9\\).\n\n"
        "**Step 2:** Calculate:\n"
        "$$F + V - E = 5 + 6 - 9 = 11 - 9 = \\mathbf{2}$$\n\n"
        "The formula holds true."
    )
    return {
        "id": f"g7_g3d_19_{rng.randint(100000, 999999)}",
        "subskill": "19_eulers_formula_verify_triangular_prism",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_19",
        "hints": {"tier_1": "F=5, V=6, E=9.", "tier_2": "5 + 6 - 9 = 2.", "tier_3": ans},
        "misconception_tags": ["eulers_formula_arithmetic_mistake"]
    }


# 20. Euler's formula verify square pyramid
def arch_20_eulers_formula_verify_square_pyramid(rng: random.Random) -> Dict[str, Any]:
    ans = "F + V - E = 5 + 5 - 8 = 2. Verified."
    prompt = (
        "Verify Euler's formula for a **Square-based Pyramid**."
    )
    sol = (
        "**Step 1:** Square-based pyramid: \\(F = 5\\), \\(V = 5\\), \\(E = 8\\).\n\n"
        "**Step 2:** Evaluate:\n"
        "$$F + V - E = 5 + 5 - 8 = 10 - 8 = \\mathbf{2}$$"
    )
    return {
        "id": f"g7_g3d_20_{rng.randint(100000, 999999)}",
        "subskill": "20_eulers_formula_verify_square_pyramid",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_20",
        "hints": {"tier_1": "F=5, V=5, E=8.", "tier_2": "5 + 5 - 8 = 2.", "tier_3": ans},
        "misconception_tags": ["pyramid_euler_verification_error"]
    }


# 21. Euler's formula find edges
def arch_21_eulers_formula_find_edges(rng: random.Random) -> Dict[str, Any]:
    f_val = 8
    v_val = 12
    e_val = f_val + v_val - 2  # 18
    ans = str(e_val)
    prompt = (
        f"A certain convex polyhedron has \\({f_val}\\) faces and \\({v_val}\\) vertices.\n\n"
        f"Use Euler's formula (\\(F + V - E = 2\\)) to calculate the number of edges \\(E\\)."
    )
    sol = (
        f"**Step 1:** State Euler's formula:\n"
        f"$$F + V - E = 2$$\n\n"
        f"**Step 2:** Substitute \\(F = {f_val}\\) and \\(V = {v_val}\\):\n"
        f"$${f_val} + {v_val} - E = 2$$\n"
        f"$${f_val + v_val} - E = 2$$\n\n"
        f"**Step 3:** Solve for \\(E\\):\n"
        f"$$E = {f_val + v_val} - 2 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_g3d_21_{rng.randint(100000, 999999)}",
        "subskill": "21_eulers_formula_find_edges",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_21",
        "hints": {"tier_1": "E = F + V - 2.", "tier_2": f"E = {f_val} + {v_val} - 2 = {e_val}.", "tier_3": ans},
        "misconception_tags": ["adding_two_instead_of_subtracting_two_in_euler_edge_formula"]
    }


# 22. Euler's formula find vertices
def arch_22_eulers_formula_find_vertices(rng: random.Random) -> Dict[str, Any]:
    f_val = 7
    e_val = 15
    v_val = e_val + 2 - f_val  # 10
    ans = str(v_val)
    prompt = (
        f"A polyhedron has \\({f_val}\\) faces and \\({e_val}\\) edges.\n\n"
        f"Determine its number of vertices \\(V\\) using Euler's formula."
    )
    sol = (
        f"**Step 1:** Rearrange Euler's formula for vertices:\n"
        f"$$V = E + 2 - F$$\n\n"
        f"**Step 2:** Substitute values:\n"
        f"$$V = {e_val} + 2 - {f_val} = {e_val + 2} - {f_val} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_g3d_22_{rng.randint(100000, 999999)}",
        "subskill": "22_eulers_formula_find_vertices",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_22",
        "hints": {"tier_1": "V = E + 2 - F.", "tier_2": f"V = {e_val} + 2 - {f_val} = {v_val}.", "tier_3": ans},
        "misconception_tags": ["euler_vertex_calculation_error"]
    }


# 23. Euler's formula find faces
def arch_23_eulers_formula_find_faces(rng: random.Random) -> Dict[str, Any]:
    v_val = 6
    e_val = 10
    f_val = e_val + 2 - v_val  # 6
    ans = str(f_val)
    prompt = (
        f"A polyhedron has \\({v_val}\\) vertices and \\({e_val}\\) edges.\n\n"
        f"Calculate the number of faces \\(F\\) of this solid."
    )
    sol = (
        f"**Step 1:** Rearrange Euler's formula:\n"
        f"$$F = E + 2 - V$$\n\n"
        f"**Step 2:** Substitute:\n"
        f"$$F = {e_val} + 2 - {v_val} = {e_val + 2} - {v_val} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_g3d_23_{rng.randint(100000, 999999)}",
        "subskill": "23_eulers_formula_find_faces",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_23",
        "hints": {"tier_1": "F = E + 2 - V.", "tier_2": f"F = {e_val} + 2 - {v_val} = {f_val}.", "tier_3": ans},
        "misconception_tags": ["euler_face_calculation_error"]
    }


# 24. Euler's formula applicability check
def arch_24_eulers_formula_applicability_check(rng: random.Random) -> Dict[str, Any]:
    ans = "No, Euler's formula applies only to polyhedra (solids with flat polygon faces), not to curved solids like cylinders."
    prompt = (
        "A student attempts to use Euler's formula \\(F + V - E = 2\\) on a cylinder.\n\n"
        "Can Euler's formula be used for a cylinder? Explain why or why not."
    )
    sol = (
        "**Explanation:**\n"
        "**No**, Euler's formula applies strictly to **convex polyhedra** (solids whose faces are flat polygons meeting at straight edges and sharp vertices).\n"
        "A cylinder is a curved solid with a curved side surface and circular boundary edges, so the polyhedron formula does not apply."
    )
    return {
        "id": f"g7_g3d_24_{rng.randint(100000, 999999)}",
        "subskill": "24_eulers_formula_applicability_check",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_g3d_24",
        "hints": {"tier_1": "Is a cylinder a polyhedron?", "tier_2": "Euler's formula only works for flat-faced polyhedra.", "tier_3": ans},
        "misconception_tags": ["applying_euler_formula_to_curved_surfaces"]
    }


# 25. General prism formula for n-gon
def arch_25_general_prism_formula_for_n_gon(rng: random.Random) -> Dict[str, Any]:
    ans = "Faces = n + 2, Vertices = 2n, Edges = 3n"
    prompt = (
        "For any right prism whose base is a polygon with \\(n\\) sides:\n\n"
        "Write general algebraic formulas in terms of \\(n\\) for:\n"
        "1. Number of faces \\(F\\)\n"
        "2. Number of vertices \\(V\\)\n"
        "3. Number of edges \\(E\\)"
    )
    sol = (
        "**General Formulas for an \\(n\\)-gonal Prism:**\n"
        "1. **Faces:** \\(F = n + 2\\) (2 bases + \\(n\\) rectangular sides)\n"
        "2. **Vertices:** \\(V = 2n\\) (\\(n\\) at bottom base + \\(n\\) at top base)\n"
        "3. **Edges:** \\(E = 3n\\) (\\(n\\) at bottom + \\(n\\) at top + \\(n\\) vertical joining edges)\n\n"
        "*(Notice: \\(F + V - E = (n + 2) + 2n - 3n = 2\\), which satisfies Euler's formula!)*"
    )
    return {
        "id": f"g7_g3d_25_{rng.randint(100000, 999999)}",
        "subskill": "25_general_prism_formula_for_n_gon",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_g3d_25",
        "hints": {"tier_1": "Bases give 2 faces, 2n vertices, 2n edges.", "tier_2": "F = n+2, V = 2n, E = 3n.", "tier_3": ans},
        "misconception_tags": ["general_prism_formula_variable_confusion"]
    }
