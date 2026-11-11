"""Grade 8 Mathematics — Surface Area & Volume of 3D Objects Archetypes (01 to 25).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/01. Surface area and volume of 3D objects.md

Archetypes covered:
  01. Concept: Surface area vs volume definitions and units distinction.
  02. Cube: Surface area given side length s (6 * s²).
  03. Cube: Surface area of open-top container (5 * s²).
  04. Cube: Find side length s given total surface area.
  05. Cube: Volume given side length s (s³).
  06. Cube: Find side length s from volume using cube root.
  07. Rectangular prism: Surface area integer dimensions (2(lb + lh + bh)).
  08. Rectangular prism: Surface area of open-top box (lb + 2lh + 2bh).
  09. Rectangular prism: Surface area using base perimeter formula (2*base_area + P*h).
  10. Rectangular prism: Volume integer dimensions (l * b * h).
  11. Rectangular prism: Find height given volume, length, and breadth.
  12. Rectangular prism: Find breadth given volume, length, and height.
  13. Triangular prism: Surface area with right-angled triangular base.
  14. Triangular prism: Surface area with isosceles triangular base.
  15. Triangular prism: Surface area with equilateral triangular base.
  16. Triangular prism: Volume with right-angled triangular base (1/2 * b * h_tri * H).
  17. Triangular prism: Volume with isosceles triangular base.
  18. Triangular prism: Find height of prism given volume and base area.
  19. Triangular prism: Find triangle height given volume and base length.
  20. Triangular prism: Distinguish triangle perpendicular height from prism height.
  21. Unfolding: Surface area of cube from face dimensions.
  22. Unfolding: Surface area of rectangular prism from flat face dimensions.
  23. Unfolding: Surface area of triangular prism from flat face dimensions.
  24. Conversion: Cubic centimetres to cubic millimetres (multiply by 1 000).
  25. Conversion: Cubic millimetres to cubic centimetres (divide by 1 000).

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .measurement_3d_svg import (
    draw_cube_3d_svg,
    draw_rectangular_prism_3d_svg,
    draw_triangular_prism_3d_svg,
)


def _fmt_dec(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 01. Concept: Surface Area vs Volume Definition Distinction
# ----------------------------------------------------------------------
def arch_01_concept_surface_area_vs_volume_definition_distinction(rng: random.Random) -> Dict[str, Any]:
    obj_name = rng.choice(["wooden block", "storage crate", "gift box", "cardboard carton"])
    prompt = (
        f"Consider a closed 3D {obj_name}.\n\n"
        f"1. State the precise mathematical difference between the **surface area** and the **volume** of the object.\n"
        f"2. Give the standard metric units used to measure each quantity."
    )
    sol = (
        f"**1. Conceptual Distinction:**\n"
        f"- **Surface Area:** The total area of all the outer flat surfaces (faces) of the 3D object added together. It measures 2D boundary coverage.\n"
        f"- **Volume:** The amount of 3D space occupied by the object itself (or the space enclosed within it).\n\n"
        f"**2. Metric Units:**\n"
        f"- Surface Area is measured in square units: \\(\\text{{mm}}^2, \\text{{cm}}^2, \\text{{m}}^2\\).\n"
        f"- Volume is measured in cubic units: \\(\\text{{mm}}^3, \\text{{cm}}^3, \\text{{m}}^3\\)."
    )
    ans = "1. Surface area is the total outer boundary area of all faces; volume is the 3D space occupied; 2. Area in square units (cm²), volume in cubic units (cm³)"
    return {
        "id": f"g8_meas_concept_{rng.randint(100000, 999999)}",
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
        "subskill": "01_concept_surface_area_vs_volume_definition_distinction",
        "learning_objective_id": "math_g8_meas_concept",
        "hints": {
            "tier_1": "Surface area relates to the faces outside; volume relates to 3D space inside/taken up.",
            "tier_2": "Area uses power 2 (cm²); volume uses power 3 (cm³).",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_square_and_cubic_units"],
    }


# ----------------------------------------------------------------------
# 02. Cube: Surface Area Given Side Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_cube_surface_area_given_side_length(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 7, 8, 9, 10, 12])
    face_area = s * s
    total_sa = 6 * face_area
    svg = draw_cube_3d_svg(s, seed=rng.randint(100, 999999))

    prompt = (
        f"A solid cube has an edge length of \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"Calculate the total surface area of the cube in \\(\\text{{cm}}^2\\), showing formula and substitution."
    )
    sol = (
        f"**Calculation of Total Surface Area:**\n"
        f"A cube has 6 identical square faces:\n"
        f"\\[ \\text{{Total Surface Area}} = 6s^2 \\]\n"
        f"\\[ = 6 \\times ({s})^2 = 6 \\times {face_area} = {total_sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_cube_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "02_cube_surface_area_given_side_length",
        "learning_objective_id": "math_g8_meas_cube_sa",
        "hints": {
            "tier_1": f"Each face has area {s}² = {face_area} cm².",
            "tier_2": f"Multiply the face area by 6 faces: 6 × {face_area}.",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["multiplying_by_4_instead_of_6_for_closed_cube"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Cube: Surface Area Open-Top Container (WITH SVG)
# ----------------------------------------------------------------------
def arch_03_cube_surface_area_open_top_five_faces(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 5, 6, 8, 10, 11])
    face_area = s * s
    sa_open = 5 * face_area
    svg = draw_cube_3d_svg(s, seed=rng.randint(100, 999999))

    prompt = (
        f"An open-top cubic storage bin without a lid has side edges of \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"Calculate the total exterior surface area of this open container in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Surface Area of Open Cube:**\n"
        f"Since the bin has no lid (open top), it has only 5 square faces (1 bottom + 4 sides):\n"
        f"\\[ \\text{{Surface Area}} = 5s^2 \\]\n"
        f"\\[ = 5 \\times ({s})^2 = 5 \\times {face_area} = {sa_open}\\text{{ cm}}^2 \\]"
    )
    ans = f"{sa_open} cm²"
    return {
        "id": f"g8_meas_cube_open_{rng.randint(100000, 999999)}",
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
        "subskill": "03_cube_surface_area_open_top_five_faces",
        "learning_objective_id": "math_g8_meas_cube_open",
        "hints": {
            "tier_1": "An open container has only 5 faces (no lid).",
            "tier_2": f"Area = 5 × ({s}²) = 5 × {face_area}.",
            "tier_3": f"{sa_open} cm².",
        },
        "misconception_tags": ["including_sixth_face_on_open_container"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Cube: Find Side Length from Surface Area
# ----------------------------------------------------------------------
def arch_04_cube_find_side_length_from_surface_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    total_sa = 6 * s * s
    face_area = s * s

    prompt = (
        f"A closed cube has a total surface area of \\({total_sa}\\text{{ cm}}^2\\).\n\n"
        f"Determine the length of one edge \\(s\\) of the cube, showing all working."
    )
    sol = (
        f"**Finding Edge Length s:**\n"
        f"\\[ 6s^2 = {total_sa} \\]\n"
        f"\\[ s^2 = \\frac{{{total_sa}}}{{6}} = {face_area} \\]\n"
        f"\\[ s = \\sqrt{{{face_area}}} = {s}\\text{{ cm}} \\]"
    )
    ans = f"{s} cm"
    return {
        "id": f"g8_meas_cube_edge_{rng.randint(100000, 999999)}",
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
        "subskill": "04_cube_find_side_length_from_surface_area",
        "learning_objective_id": "math_g8_meas_cube_edge",
        "hints": {
            "tier_1": "Divide total surface area by 6 to find the area of one face.",
            "tier_2": f"s² = {total_sa} / 6 = {face_area}.",
            "tier_3": f"s = √{face_area} = {s} cm.",
        },
        "misconception_tags": ["taking_square_root_before_dividing_by_6"],
    }


# ----------------------------------------------------------------------
# 05. Cube: Volume Given Side Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_cube_volume_given_side_length(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    volume = s * s * s
    svg = draw_cube_3d_svg(s, seed=rng.randint(100, 999999))

    prompt = (
        f"A solid wooden cube has an edge length of \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"Calculate the volume of the cube in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Calculation of Volume:**\n"
        f"\\[ V = s^3 = s \\times s \\times s \\]\n"
        f"\\[ V = {s} \\times {s} \\times {s} = {volume}\\text{{ cm}}^3 \\]"
    )
    ans = f"{volume} cm³"
    return {
        "id": f"g8_meas_cube_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "05_cube_volume_given_side_length",
        "learning_objective_id": "math_g8_meas_cube_vol",
        "hints": {
            "tier_1": f"Volume = {s} × {s} × {s}.",
            "tier_2": f"{s}² = {s*s}, then multiply by {s}.",
            "tier_3": f"{volume} cm³.",
        },
        "misconception_tags": ["multiplying_by_3_instead_of_cubing"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Cube: Find Side Length from Volume Cube Root
# ----------------------------------------------------------------------
def arch_06_cube_find_side_length_from_volume_cube_root(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4, 5, 6, 7, 8, 10])
    volume = s * s * s

    prompt = (
        f"The volume of a metal cube is \\({volume}\\text{{ cm}}^3\\).\n\n"
        f"Determine the edge length \\(s\\) of the cube, stating the appropriate radical operation."
    )
    sol = (
        f"**Finding Side Length from Volume:**\n"
        f"\\[ V = s^3 = {volume} \\]\n"
        f"\\[ s = \\sqrt[3]{{{volume}}} = {s}\\text{{ cm}} \\]"
    )
    ans = f"{s} cm"
    return {
        "id": f"g8_meas_cbrt_{rng.randint(100000, 999999)}",
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
        "subskill": "06_cube_find_side_length_from_volume_cube_root",
        "learning_objective_id": "math_g8_meas_cbrt",
        "hints": {
            "tier_1": "Take the cube root of the volume: s = ∛V.",
            "tier_2": f"Find a number that multiplied by itself three times equals {volume}.",
            "tier_3": f"{s} cm.",
        },
        "misconception_tags": ["taking_square_root_instead_of_cube_root"],
    }


# ----------------------------------------------------------------------
# 07. Rectangular Prism: Surface Area Integer Dimensions (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_rectangular_prism_surface_area_integer_dimensions(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([6, 8, 10, 12])
    b = rng.choice([3, 4, 5])
    h = rng.choice([2, 3, 4])
    sa = 2 * (l * b + l * h + b * h)
    svg = draw_rectangular_prism_3d_svg(l, b, h, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A closed rectangular prism has length \\(l = {l}\\text{{ cm}}\\), breadth \\(b = {b}\\text{{ cm}}\\), "
        f"and height \\(h = {h}\\text{{ cm}}\\).\n\n"
        f"Calculate the total surface area in \\(\\text{{cm}}^2\\), showing the full formula and substitution."
    )
    sol = (
        f"**Calculation of Total Surface Area:**\n"
        f"\\[ \\text{{Total Surface Area}} = 2(lb + lh + bh) \\]\n"
        f"\\[ = 2(({l})({b}) + ({l})({h}) + ({b})({h})) \\]\n"
        f"\\[ = 2({l*b} + {l*h} + {b*h}) = 2({l*b + l*h + b*h}) = {sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{sa} cm²"
    return {
        "id": f"g8_meas_rect_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "07_rectangular_prism_surface_area_integer_dimensions",
        "learning_objective_id": "math_g8_meas_rect_sa",
        "hints": {
            "tier_1": f"Calculate pairs of faces: {l*b}, {l*h}, {b*h}.",
            "tier_2": f"Add face areas: {l*b} + {l*h} + {b*h} = {l*b + l*h + b*h}, then multiply by 2.",
            "tier_3": f"{sa} cm².",
        },
        "misconception_tags": ["adding_dimensions_instead_of_face_areas"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Rectangular Prism: Surface Area Open-Top Box (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_rectangular_prism_surface_area_open_top_box(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([7, 9, 10, 14])
    b = rng.choice([4, 5, 6])
    h = rng.choice([3, 4, 5])
    # Open top: 1 bottom (lb) + 2 side long (2lh) + 2 side short (2bh)
    sa_open = l * b + 2 * l * h + 2 * b * h
    svg = draw_rectangular_prism_3d_svg(l, b, h, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"An open-top rectangular planter box has length \\(l = {l}\\text{{ cm}}\\), breadth \\(b = {b}\\text{{ cm}}\\), "
        f"and depth \\(h = {h}\\text{{ cm}}\\). The box does not have a lid.\n\n"
        f"Calculate the total outside surface area of the box."
    )
    sol = (
        f"**Surface Area of Open Box:**\n"
        f"The open box has 5 faces: 1 bottom base and 4 vertical side faces:\n"
        f"\\[ \\text{{Surface Area}} = lb + 2lh + 2bh \\]\n"
        f"\\[ = ({l})({b}) + 2({l})({h}) + 2({b})({h}) \\]\n"
        f"\\[ = {l*b} + {2*l*h} + {2*b*h} = {sa_open}\\text{{ cm}}^2 \\]"
    )
    ans = f"{sa_open} cm²"
    return {
        "id": f"g8_meas_rect_open_{rng.randint(100000, 999999)}",
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
        "subskill": "08_rectangular_prism_surface_area_open_top_box",
        "learning_objective_id": "math_g8_meas_rect_open",
        "hints": {
            "tier_1": "Calculate 1 bottom base (lb) and 4 sides: 2lh + 2bh.",
            "tier_2": f"Base = {l*b}, sides = {2*l*h} + {2*b*h}.",
            "tier_3": f"{sa_open} cm².",
        },
        "misconception_tags": ["accidentally_including_the_open_top_face"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Rectangular Prism: Surface Area Using Base Perimeter Formula
# ----------------------------------------------------------------------
def arch_09_rectangular_prism_surface_area_base_perimeter_formula(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([8, 10, 15])
    b = rng.choice([4, 6, 8])
    h = rng.choice([5, 7, 10])
    base_area = l * b
    base_perimeter = 2 * (l + b)
    lateral_area = base_perimeter * h
    total_sa = 2 * base_area + lateral_area
    svg = draw_rectangular_prism_3d_svg(l, b, h, unit="m", seed=rng.randint(100, 999999))

    prompt = (
        f"A rectangular storage container has floor measurements \\(l = {l}\\text{{ m}}\\) and \\(b = {b}\\text{{ m}}\\), "
        f"with vertical clearance \\(h = {h}\\text{{ m}}\\).\n\n"
        f"1. Find the rim distance around the bottom and the bottom face coverage.\n"
        f"2. Using the formula \\(\\text{{Total SA}} = 2 \\times (\\text{{Bottom Area}}) + (\\text{{Rim Distance}}) \\times h\\), "
        f"determine the total exterior surface area."
    )
    sol = (
        f"**1. Base Calculations:**\n"
        f"- Base Area \\(= l \\times b = {l} \\times {b} = {base_area}\\text{{ m}}^2\\)\n"
        f"- Perimeter of Base \\(= 2(l + b) = 2({l} + {b}) = 2({l+b}) = {base_perimeter}\\text{{ m}}\\)\n\n"
        f"**2. Total Surface Area:**\n"
        f"\\[ \\text{{Total Surface Area}} = 2 \\times {base_area} + ({base_perimeter} \\times {h}) \\]\n"
        f"\\[ = {2*base_area} + {lateral_area} = {total_sa}\\text{{ m}}^2 \\]"
    )
    ans = f"1. Base area = {base_area} m², perimeter = {base_perimeter} m; 2. Total surface area = {total_sa} m²"
    return {
        "id": f"g8_meas_p_form_{rng.randint(100000, 999999)}",
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
        "subskill": "09_rectangular_prism_surface_area_base_perimeter_formula",
        "learning_objective_id": "math_g8_meas_p_form",
        "hints": {
            "tier_1": f"Base area = {l} × {b}; Perimeter = 2 × ({l} + {b}).",
            "tier_2": f"Surface area = 2 × {base_area} + {base_perimeter} × {h}.",
            "tier_3": f"{total_sa} m².",
        },
        "misconception_tags": ["forgetting_to_multiply_base_area_by_2_for_top_and_bottom"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Rectangular Prism: Volume Integer Dimensions (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_rectangular_prism_volume_integer_dimensions(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([7, 8, 9, 11, 12])
    b = rng.choice([3, 4, 5, 6])
    h = rng.choice([2, 4, 5, 8])
    vol = l * b * h
    svg = draw_rectangular_prism_3d_svg(l, b, h, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A rectangular prism has length \\(l = {l}\\text{{ cm}}\\), breadth \\(b = {b}\\text{{ cm}}\\), "
        f"and height \\(h = {h}\\text{{ cm}}\\).\n\n"
        f"Calculate the volume of the prism in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Calculation of Volume:**\n"
        f"\\[ V = l \\times b \\times h \\]\n"
        f"\\[ V = {l} \\times {b} \\times {h} = {l*b} \\times {h} = {vol}\\text{{ cm}}^3 \\]"
    )
    ans = f"{vol} cm³"
    return {
        "id": f"g8_meas_rect_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "10_rectangular_prism_volume_integer_dimensions",
        "learning_objective_id": "math_g8_meas_rect_vol",
        "hints": {
            "tier_1": f"Volume = length × breadth × height = {l} × {b} × {h}.",
            "tier_2": f"{l*b} × {h}.",
            "tier_3": f"{vol} cm³.",
        },
        "misconception_tags": ["adding_dimensions_instead_of_multiplying_for_volume"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Rectangular Prism: Find Height Given Volume, Length, Breadth
# ----------------------------------------------------------------------
def arch_11_rectangular_prism_find_height_given_volume_length_breadth(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([8, 10, 12, 15])
    b = rng.choice([4, 5, 6])
    h = rng.choice([3, 5, 7, 9])
    vol = l * b * h
    base_area = l * b

    prompt = (
        f"A rectangular prism has a volume of \\({vol}\\text{{ cm}}^3\\), a length of \\({l}\\text{{ cm}}\\), "
        f"and a breadth of \\({b}\\text{{ cm}}\\).\n\n"
        f"Determine the height \\(h\\) of the prism."
    )
    sol = (
        f"**Finding Height h:**\n"
        f"\\[ V = l \\times b \\times h \\]\n"
        f"\\[ {vol} = {l} \\times {b} \\times h = {base_area} \\times h \\]\n"
        f"\\[ h = \\frac{{{vol}}}{{{base_area}}} = {h}\\text{{ cm}} \\]"
    )
    ans = f"{h} cm"
    return {
        "id": f"g8_meas_find_h_{rng.randint(100000, 999999)}",
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
        "subskill": "11_rectangular_prism_find_height_given_volume_length_breadth",
        "learning_objective_id": "math_g8_meas_find_h",
        "hints": {
            "tier_1": f"Base area = {l} × {b} = {base_area} cm².",
            "tier_2": f"Height = Volume / Base Area = {vol} / {base_area}.",
            "tier_3": f"{h} cm.",
        },
        "misconception_tags": ["dividing_by_length_only_instead_of_base_area"],
    }


# ----------------------------------------------------------------------
# 12. Rectangular Prism: Find Breadth Given Volume, Length, Height
# ----------------------------------------------------------------------
def arch_12_rectangular_prism_find_breadth_given_volume_length_height(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([9, 10, 14, 16])
    b = rng.choice([3, 4, 6, 8])
    h = rng.choice([2, 5, 6])
    vol = l * b * h
    face_area = l * h

    prompt = (
        f"The volume of a rectangular carton is \\({vol}\\text{{ cm}}^3\\). "
        f"Its length is \\({l}\\text{{ cm}}\\) and its height is \\({h}\\text{{ cm}}\\).\n\n"
        f"Calculate the breadth \\(b\\) of the carton."
    )
    sol = (
        f"**Finding Breadth b:**\n"
        f"\\[ V = l \\times b \\times h \\]\n"
        f"\\[ {vol} = ({l} \\times {h}) \\times b = {face_area} \\times b \\]\n"
        f"\\[ b = \\frac{{{vol}}}{{{face_area}}} = {b}\\text{{ cm}} \\]"
    )
    ans = f"{b} cm"
    return {
        "id": f"g8_meas_find_b_{rng.randint(100000, 999999)}",
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
        "subskill": "12_rectangular_prism_find_breadth_given_volume_length_height",
        "learning_objective_id": "math_g8_meas_find_b",
        "hints": {
            "tier_1": f"Multiply length by height: {l} × {h} = {face_area}.",
            "tier_2": f"Breadth = {vol} / {face_area}.",
            "tier_3": f"{b} cm.",
        },
        "misconception_tags": ["inverting_division_order"],
    }


# ----------------------------------------------------------------------
# 13. Triangular Prism: Right-Angled Base Surface Area (WITH SVG)
# ----------------------------------------------------------------------
def arch_13_triangular_prism_right_angled_base_surface_area(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    b_tri = 6 * k
    h_tri = 8 * k
    hyp = 10 * k
    l_prism = 12 * k

    tri_area = (b_tri * h_tri) // 2
    two_triangles = 2 * tri_area
    rect1 = b_tri * l_prism
    rect2 = h_tri * l_prism
    rect3 = hyp * l_prism
    total_sa = two_triangles + rect1 + rect2 + rect3
    svg = draw_triangular_prism_3d_svg(b_tri, h_tri, hyp, l_prism, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A right triangular prism has triangular end bases with perpendicular sides of "
        f"\\({b_tri}\\text{{ cm}}\\) and \\({h_tri}\\text{{ cm}}\\), and hypotenuse \\({hyp}\\text{{ cm}}\\). "
        f"The length of the prism is \\({l_prism}\\text{{ cm}}\\).\n\n"
        f"Calculate the total surface area of the prism in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Calculation of Surface Area of Triangular Prism:**\n"
        f"1. Area of 2 triangular bases:\n"
        f"\\[ 2 \\times \\left(\\frac{{1}}{{2}} \\times {b_tri} \\times {h_tri}\\right) = {two_triangles}\\text{{ cm}}^2 \\]\n"
        f"2. Area of 3 rectangular lateral faces:\n"
        f"\\[ (\\text{{Perimeter of triangle}}) \\times \\text{{length of prism}} \\]\n"
        f"\\[ ({b_tri} + {h_tri} + {hyp}) \\times {l_prism} = {b_tri + h_tri + hyp} \\times {l_prism} = {rect1 + rect2 + rect3}\\text{{ cm}}^2 \\]\n"
        f"3. Total Surface Area:\n"
        f"\\[ {two_triangles} + {rect1 + rect2 + rect3} = {total_sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_tri_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "13_triangular_prism_right_angled_base_surface_area",
        "learning_objective_id": "math_g8_meas_tri_sa",
        "hints": {
            "tier_1": f"Sum the areas of 2 triangles ({two_triangles} cm²) and 3 rectangles.",
            "tier_2": f"Lateral area = ({b_tri} + {h_tri} + {hyp}) × {l_prism} = {rect1 + rect2 + rect3} cm².",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["forgetting_one_of_the_three_rectangular_faces"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Triangular Prism: Isosceles Base Surface Area (WITH SVG)
# ----------------------------------------------------------------------
def arch_14_triangular_prism_isosceles_base_surface_area(rng: random.Random) -> Dict[str, Any]:
    b_tri = 10
    h_tri = 12
    side_tri = 13  # 5-12-13 half triangle
    l_prism = rng.choice([15, 20])

    tri_area = (b_tri * h_tri) // 2
    two_triangles = 2 * tri_area
    lateral_area = (b_tri + 2 * side_tri) * l_prism
    total_sa = two_triangles + lateral_area
    svg = draw_triangular_prism_3d_svg(b_tri, h_tri, side_tri, l_prism, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A triangular prism has an isosceles triangular base with base edge \\({b_tri}\\text{{ cm}}\\), "
        f"equal sloping sides of \\({side_tri}\\text{{ cm}}\\), and perpendicular height \\({h_tri}\\text{{ cm}}\\). "
        f"The prism length is \\({l_prism}\\text{{ cm}}\\).\n\n"
        f"Calculate the total surface area of the prism."
    )
    sol = (
        f"**Calculation of Isosceles Prism Surface Area:**\n"
        f"1. Area of 2 triangular faces:\n"
        f"\\[ 2 \\times \\left(\\frac{{1}}{{2}} \\times {b_tri} \\times {h_tri}\\right) = {two_triangles}\\text{{ cm}}^2 \\]\n"
        f"2. Area of 3 rectangular faces:\n"
        f"\\[ (\\text{{Perimeter}}) \\times \\text{{length}} = ({b_tri} + {side_tri} + {side_tri}) \\times {l_prism} \\]\n"
        f"\\[ = {b_tri + 2*side_tri} \\times {l_prism} = {lateral_area}\\text{{ cm}}^2 \\]\n"
        f"3. Total Surface Area:\n"
        f"\\[ {two_triangles} + {lateral_area} = {total_sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_iso_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "14_triangular_prism_isosceles_base_surface_area",
        "learning_objective_id": "math_g8_meas_iso_sa",
        "hints": {
            "tier_1": f"Two triangles: {b_tri} × {h_tri} = {two_triangles} cm².",
            "tier_2": f"Three rectangles: ({b_tri} + 2×{side_tri}) × {l_prism} = {lateral_area} cm².",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["using_slant_height_instead_of_perpendicular_height_for_triangle_area"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Triangular Prism: Equilateral Base Surface Area
# ----------------------------------------------------------------------
def arch_15_triangular_prism_equilateral_base_surface_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([6, 8, 10])
    h_tri = round(s * math.sqrt(3) / 2, 1)
    l_prism = rng.choice([12, 15, 20])

    tri_area = round(0.5 * s * h_tri, 1)
    two_triangles = round(2 * tri_area, 1)
    lateral_area = 3 * s * l_prism
    total_sa = round(two_triangles + lateral_area, 1)

    prompt = (
        f"An equilateral triangular prism has cross-sectional triangular sides of length \\({s}\\text{{ cm}}\\) "
        f"and perpendicular height \\({_fmt_dec(h_tri)}\\text{{ cm}}\\). The length of the prism is \\({l_prism}\\text{{ cm}}\\).\n\n"
        f"Calculate the total surface area of the prism in \\(\\text{{cm}}^2\\) (round off to 1 decimal place)."
    )
    sol = (
        f"**Calculation for Equilateral Prism:**\n"
        f"1. Area of 2 triangular bases:\n"
        f"\\[ 2 \\times \\left(\\frac{{1}}{{2}} \\times {s} \\times {_fmt_dec(h_tri)}\\right) = {_fmt_dec(two_triangles)}\\text{{ cm}}^2 \\]\n"
        f"2. Area of 3 congruent rectangular faces:\n"
        f"\\[ 3 \\times ({s} \\times {l_prism}) = 3 \\times {s * l_prism} = {lateral_area}\\text{{ cm}}^2 \\]\n"
        f"3. Total Surface Area:\n"
        f"\\[ {_fmt_dec(two_triangles)} + {lateral_area} = {_fmt_dec(total_sa)}\\text{{ cm}}^2 \\]"
    )
    ans = f"{_fmt_dec(total_sa)} cm²"
    return {
        "id": f"g8_meas_eq_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "15_triangular_prism_equilateral_base_surface_area",
        "learning_objective_id": "math_g8_meas_eq_sa",
        "hints": {
            "tier_1": f"All 3 rectangular faces are identical: 3 × ({s} × {l_prism}).",
            "tier_2": f"Add the two triangular faces: 2 × (0,5 × {s} × {_fmt_dec(h_tri)}).",
            "tier_3": f"{_fmt_dec(total_sa)} cm².",
        },
        "misconception_tags": ["using_side_length_as_perpendicular_height"],
    }


# ----------------------------------------------------------------------
# 16. Triangular Prism: Right-Angled Base Volume (WITH SVG)
# ----------------------------------------------------------------------
def arch_16_triangular_prism_right_angled_base_volume(rng: random.Random) -> Dict[str, Any]:
    b_tri = rng.choice([4, 6, 8, 10])
    h_tri = rng.choice([3, 5, 7, 9])
    hyp = round(math.sqrt(b_tri * b_tri + h_tri * h_tri), 1)
    l_prism = rng.choice([10, 12, 15, 20])

    base_area = 0.5 * b_tri * h_tri
    vol = int(base_area * l_prism)
    svg = draw_triangular_prism_3d_svg(b_tri, h_tri, hyp, l_prism, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A right triangular prism has a triangular base with perpendicular sides \\({b_tri}\\text{{ cm}}\\) "
        f"and \\({h_tri}\\text{{ cm}}\\). The length (height of prism) is \\({l_prism}\\text{{ cm}}\\).\n\n"
        f"Calculate the volume of the prism in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Calculation of Volume of Triangular Prism:**\n"
        f"\\[ V = \\text{{Area of triangular base}} \\times \\text{{height of prism}} \\]\n"
        f"\\[ = \\left(\\frac{{1}}{{2}} \\times {b_tri} \\times {h_tri}\\right) \\times {l_prism} \\]\n"
        f"\\[ = {_fmt_dec(base_area)} \\times {l_prism} = {vol}\\text{{ cm}}^3 \\]"
    )
    ans = f"{vol} cm³"
    return {
        "id": f"g8_meas_tri_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "16_triangular_prism_right_angled_base_volume",
        "learning_objective_id": "math_g8_meas_tri_vol",
        "hints": {
            "tier_1": f"Base area = 1/2 × {b_tri} × {h_tri} = {_fmt_dec(base_area)} cm².",
            "tier_2": f"Volume = Base Area × Prism Length = {_fmt_dec(base_area)} × {l_prism}.",
            "tier_3": f"{vol} cm³.",
        },
        "misconception_tags": ["forgetting_the_half_in_triangular_base_area"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 17. Triangular Prism: Isosceles Base Volume (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_triangular_prism_isosceles_base_volume(rng: random.Random) -> Dict[str, Any]:
    b_tri = rng.choice([6, 8, 12])
    h_tri = rng.choice([4, 6, 8])
    side = round(math.sqrt((b_tri / 2) ** 2 + h_tri ** 2), 1)
    l_prism = rng.choice([14, 16, 20])

    base_area = int(0.5 * b_tri * h_tri)
    vol = base_area * l_prism
    svg = draw_triangular_prism_3d_svg(b_tri, h_tri, side, l_prism, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"An isosceles triangular prism has a cross-section with base \\({b_tri}\\text{{ cm}}\\) "
        f"and perpendicular height \\({h_tri}\\text{{ cm}}\\). The length of the prism is \\({l_prism}\\text{{ cm}}\\).\n\n"
        f"Calculate the volume of the prism."
    )
    sol = (
        f"**Volume Calculation:**\n"
        f"\\[ V = \\text{{Area of base}} \\times H \\]\n"
        f"\\[ = \\left(\\frac{{1}}{{2}} \\times {b_tri} \\times {h_tri}\\right) \\times {l_prism} \\]\n"
        f"\\[ = {base_area} \\times {l_prism} = {vol}\\text{{ cm}}^3 \\]"
    )
    ans = f"{vol} cm³"
    return {
        "id": f"g8_meas_iso_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "17_triangular_prism_isosceles_base_volume",
        "learning_objective_id": "math_g8_meas_iso_vol",
        "hints": {
            "tier_1": f"Base area = 1/2 × {b_tri} × {h_tri} = {base_area}.",
            "tier_2": f"Volume = {base_area} × {l_prism}.",
            "tier_3": f"{vol} cm³.",
        },
        "misconception_tags": ["using_slant_edge_instead_of_perpendicular_height"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 18. Triangular Prism: Find Prism Length Given Volume & Base Area
# ----------------------------------------------------------------------
def arch_18_triangular_prism_find_height_given_volume_and_base_area(rng: random.Random) -> Dict[str, Any]:
    base_area = rng.choice([15, 20, 24, 30, 36])
    l_prism = rng.choice([8, 10, 12, 15])
    vol = base_area * l_prism

    prompt = (
        f"A triangular prism has a volume of \\({vol}\\text{{ cm}}^3\\). "
        f"The cross-sectional triangular base has an area of \\({base_area}\\text{{ cm}}^2\\).\n\n"
        f"Calculate the length (height) of the prism."
    )
    sol = (
        f"**Finding Length of Triangular Prism:**\n"
        f"\\[ V = \\text{{Base Area}} \\times H \\]\n"
        f"\\[ {vol} = {base_area} \\times H \\]\n"
        f"\\[ H = \\frac{{{vol}}}{{{base_area}}} = {l_prism}\\text{{ cm}} \\]"
    )
    ans = f"{l_prism} cm"
    return {
        "id": f"g8_meas_tri_h_{rng.randint(100000, 999999)}",
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
        "subskill": "18_triangular_prism_find_height_given_volume_and_base_area",
        "learning_objective_id": "math_g8_meas_tri_h",
        "hints": {
            "tier_1": "Divide volume by base area.",
            "tier_2": f"H = {vol} / {base_area}.",
            "tier_3": f"{l_prism} cm.",
        },
        "misconception_tags": ["multiplying_by_half_again"],
    }


# ----------------------------------------------------------------------
# 19. Triangular Prism: Find Triangle Height Given Volume and Base Length
# ----------------------------------------------------------------------
def arch_19_triangular_prism_find_triangle_height_given_volume_and_base_length(rng: random.Random) -> Dict[str, Any]:
    b_tri = rng.choice([6, 8, 10])
    h_tri = rng.choice([4, 6, 8])
    l_prism = rng.choice([10, 15])
    base_area = (b_tri * h_tri) // 2
    vol = base_area * l_prism

    prompt = (
        f"A triangular prism has a volume of \\({vol}\\text{{ cm}}^3\\) and length \\({l_prism}\\text{{ cm}}\\). "
        f"The base edge of the triangular face is \\({b_tri}\\text{{ cm}}\\).\n\n"
        f"Calculate the perpendicular height \\(h_\\Delta\\) of the triangular face."
    )
    sol = (
        f"**Step-by-Step Calculation:**\n"
        f"1. Find area of triangular base:\n"
        f"\\[ \\text{{Base Area}} = \\frac{{V}}{{H}} = \\frac{{{vol}}}{{{l_prism}}} = {base_area}\\text{{ cm}}^2 \\]\n"
        f"2. Solve for perpendicular height \\(h_\\Delta\\):\n"
        f"\\[ \\frac{{1}}{{2}} \\times {b_tri} \\times h_\\Delta = {base_area} \\]\n"
        f"\\[ {b_tri // 2} \\times h_\\Delta = {base_area} \\implies h_\\Delta = \\frac{{{base_area}}}{{{b_tri // 2}}} = {h_tri}\\text{{ cm}} \\]"
    )
    ans = f"{h_tri} cm"
    return {
        "id": f"g8_meas_tri_htri_{rng.randint(100000, 999999)}",
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
        "subskill": "19_triangular_prism_find_triangle_height_given_volume_and_base_length",
        "learning_objective_id": "math_g8_meas_tri_htri",
        "hints": {
            "tier_1": f"Base Area = {vol} / {l_prism} = {base_area} cm².",
            "tier_2": f"1/2 × {b_tri} × h = {base_area}.",
            "tier_3": f"{h_tri} cm.",
        },
        "misconception_tags": ["forgetting_the_factor_of_2_when_rearranging_triangle_area"],
    }


# ----------------------------------------------------------------------
# 20. Triangular Prism: Distinguish Triangle Height vs Prism Height
# ----------------------------------------------------------------------
def arch_20_triangular_prism_distinguish_triangle_height_vs_prism_height(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Learners often confuse the two different heights in a triangular prism:\n"
        "- The perpendicular height of the triangular face (\\(h_\\Delta\\))\n"
        "- The height (or length) of the prism (\\(H\\))\n\n"
        "Explain the geometric difference between these two measurements and how each is used in the volume formula "
        "\\(V = \\frac{1}{2} b \\cdot h_\\Delta \\cdot H\\)."
    )
    sol = (
        "**Clear Geometric Distinction:**\n"
        "1. **Perpendicular Height of Triangle (\\(h_\\Delta\\)):** The 2D vertical distance from the base edge of the triangular "
        "cross-section to the opposite vertex perpendicular to that base. It is used strictly to calculate the 2D cross-sectional area "
        "\\(\\text{Base Area} = \\frac{1}{2} b \\cdot h_\\Delta\\).\n\n"
        "2. **Height / Length of the Prism (\\(H\\)):** The 3D perpendicular distance separating the two identical parallel triangular "
        "bases along the prism's lateral axis. It represents the extrusion distance that converts the 2D area into a 3D volume: "
        "\\(V = \\text{Base Area} \\times H\\)."
    )
    ans = "h_triangle is the 2D height within the triangular face; H_prism is the 3D distance between the two triangular bases"
    return {
        "id": f"g8_meas_two_h_{rng.randint(100000, 999999)}",
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
        "subskill": "20_triangular_prism_distinguish_triangle_height_vs_prism_height",
        "learning_objective_id": "math_g8_meas_two_h",
        "hints": {
            "tier_1": "One height is inside the 2D triangle; the other connects the two triangular ends.",
            "tier_2": "h_triangle is used for face area; H_prism is the length of the 3D solid.",
            "tier_3": ans,
        },
        "misconception_tags": ["swapping_triangle_height_and_prism_length"],
    }


# ----------------------------------------------------------------------
# 21. Unfolding: Surface Area of Cube from Face Dimensions
# ----------------------------------------------------------------------
def arch_21_net_of_cube_calculate_surface_area_from_faces(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 5, 7, 9, 11])
    face_a = s * s
    total_sa = 6 * face_a

    prompt = (
        f"A flat pattern designed to fold into a closed cube consists of six connected square sections, "
        f"each measuring \\({s}\\text{{ cm}}\\) by \\({s}\\text{{ cm}}\\).\n\n"
        f"Calculate the total area of the flat pattern, which equals the total surface area of the folded cube."
    )
    sol = (
        f"**Calculation of Pattern Area:**\n"
        f"1. Area of one square section: \\({s} \\times {s} = {face_a}\\text{{ cm}}^2\\)\n"
        f"2. Total area of all 6 congruent sections: \\(6 \\times {face_a} = {total_sa}\\text{{ cm}}^2\\)\n\n"
        f"This equals the total surface area of the closed cube."
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_net_cube_{rng.randint(100000, 999999)}",
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
        "subskill": "21_net_of_cube_calculate_surface_area_from_faces",
        "learning_objective_id": "math_g8_meas_net_cube",
        "hints": {
            "tier_1": f"Each square is {s} × {s} = {face_a} cm².",
            "tier_2": f"Multiply by 6.",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["miscounting_number_of_faces"],
    }


# ----------------------------------------------------------------------
# 22. Unfolding: Surface Area of Rectangular Prism from Flat Face Dimensions
# ----------------------------------------------------------------------
def arch_22_net_of_rectangular_prism_calculate_surface_area_from_faces(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([6, 8, 10])
    b = rng.choice([3, 4, 5])
    h = rng.choice([2, 3])
    sa = 2 * (l * b + l * h + b * h)

    prompt = (
        f"A flat cardboard layout unfolds a rectangular box into six rectangles:\n"
        f"- Two rectangles measuring \\({l}\\text{{ cm}} \\times {b}\\text{{ cm}}\\)\n"
        f"- Two rectangles measuring \\({l}\\text{{ cm}} \\times {h}\\text{{ cm}}\\)\n"
        f"- Two rectangles measuring \\({b}\\text{{ cm}} \\times {h}\\text{{ cm}}\\)\n\n"
        f"Calculate the total area of the six rectangles to find the total surface area of the box."
    )
    sol = (
        f"**Calculation of Total Face Areas:**\n"
        f"\\[ 2({l} \\times {b}) + 2({l} \\times {h}) + 2({b} \\times {h}) \\]\n"
        f"\\[ = 2({l*b}) + 2({l*h}) + 2({b*h}) = {2*l*b} + {2*l*h} + {2*b*h} = {sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{sa} cm²"
    return {
        "id": f"g8_meas_net_rect_{rng.randint(100000, 999999)}",
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
        "subskill": "22_net_of_rectangular_prism_calculate_surface_area_from_faces",
        "learning_objective_id": "math_g8_meas_net_rect",
        "hints": {
            "tier_1": f"Add the areas of the 3 pairs of rectangles.",
            "tier_2": f"2({l*b}) + 2({l*h}) + 2({b*h}) = {sa}.",
            "tier_3": f"{sa} cm².",
        },
        "misconception_tags": ["forgetting_to_double_each_pair_of_rectangles"],
    }


# ----------------------------------------------------------------------
# 23. Unfolding: Surface Area of Triangular Prism from Flat Face Dimensions
# ----------------------------------------------------------------------
def arch_23_net_of_triangular_prism_calculate_surface_area_from_faces(rng: random.Random) -> Dict[str, Any]:
    b = 6
    h_tri = 8
    hyp = 10
    l_prism = rng.choice([10, 14])

    two_tri = b * h_tri
    rects = (b + h_tri + hyp) * l_prism
    total_sa = two_tri + rects

    prompt = (
        f"A flat pattern folds into a right triangular prism. It consists of:\n"
        f"- Two identical right-angled triangles with legs \\({b}\\text{{ cm}}\\) and \\({h_tri}\\text{{ cm}}\\), and hypotenuse \\({hyp}\\text{{ cm}}\\)\n"
        f"- Three rectangles of length \\({l_prism}\\text{{ cm}}\\) having widths \\({b}\\text{{ cm}}\\), \\({h_tri}\\text{{ cm}}\\), and \\({hyp}\\text{{ cm}}\\)\n\n"
        f"Determine the total surface area by calculating the sum of the areas of all five pieces."
    )
    sol = (
        f"**Sum of All 5 Faces:**\n"
        f"1. Area of 2 triangles: \\(2 \\times (\\frac{{1}}{{2}} \\times {b} \\times {h_tri}) = {two_tri}\\text{{ cm}}^2\\)\n"
        f"2. Area of 3 rectangles: \\(({b} + {h_tri} + {hyp}) \\times {l_prism} = {b+h_tri+hyp} \\times {l_prism} = {rects}\\text{{ cm}}^2\\)\n"
        f"3. Total Surface Area: \\({two_tri} + {rects} = {total_sa}\\text{{ cm}}^2\\)"
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_net_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "23_net_of_triangular_prism_calculate_surface_area_from_faces",
        "learning_objective_id": "math_g8_meas_net_tri",
        "hints": {
            "tier_1": f"Triangles: {two_tri} cm²; Rectangles: ({b}+{h_tri}+{hyp}) × {l_prism} = {rects} cm².",
            "tier_2": f"Total = {two_tri} + {rects}.",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["missing_the_hypotenuse_face"],
    }


# ----------------------------------------------------------------------
# 24. Conversion: Cubic cm to Cubic mm
# ----------------------------------------------------------------------
def arch_24_convert_cubic_cm_to_cubic_mm(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.choice([3, 7, 15, 24, 50, 125])
    mm3 = cm3 * 1000

    prompt = (
        f"Convert \\({cm3}\\text{{ cm}}^3\\) into cubic millimetres (\\(\\text{{mm}}^3\\)).\n\n"
        f"Explain why the conversion factor is \\(1\\,000\\)."
    )
    sol = (
        f"**Unit Conversion Explanation:**\n"
        f"Because \\(1\\text{{ cm}} = 10\\text{{ mm}}\\):\n"
        f"\\[ 1\\text{{ cm}}^3 = 1\\text{{ cm}} \\times 1\\text{{ cm}} \\times 1\\text{{ cm}} = 10\\text{{ mm}} \\times 10\\text{{ mm}} \\times 10\\text{{ mm}} = 1\\,000\\text{{ mm}}^3 \\]\n"
        f"Therefore, multiply by \\(1\\,000\\):\n"
        f"\\[ {cm3}\\text{{ cm}}^3 = {cm3} \\times 1\\,000 = {mm3}\\text{{ mm}}^3 \\]"
    )
    ans = f"{mm3} mm³"
    return {
        "id": f"g8_meas_cm3_mm3_{rng.randint(100000, 999999)}",
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
        "subskill": "24_convert_cubic_cm_to_cubic_mm",
        "learning_objective_id": "math_g8_meas_cm3_mm3",
        "hints": {
            "tier_1": "1 cm³ = 10 mm × 10 mm × 10 mm = 1 000 mm³.",
            "tier_2": f"Multiply {cm3} by 1 000.",
            "tier_3": f"{mm3} mm³.",
        },
        "misconception_tags": ["multiplying_by_10_or_100_instead_of_1000"],
    }


# ----------------------------------------------------------------------
# 25. Conversion: Cubic mm to Cubic cm
# ----------------------------------------------------------------------
def arch_25_convert_cubic_mm_to_cubic_cm(rng: random.Random) -> Dict[str, Any]:
    cm3_val = rng.choice([4, 18, 25, 45, 150, 750])
    mm3 = cm3_val * 1000
    if rng.choice([True, False]):
        # Test decimal result
        mm3 = rng.choice([250, 450, 1250, 3750])
        cm3_str = _fmt_dec(mm3 / 1000.0, 3)
    else:
        cm3_str = str(cm3_val)

    prompt = (
        f"Convert \\({mm3}\\text{{ mm}}^3\\) into cubic centimetres (\\(\\text{{cm}}^3\\))."
    )
    sol = (
        f"**Conversion Calculation:**\n"
        f"Since \\(1\\,000\\text{{ mm}}^3 = 1\\text{{ cm}}^3\\), divide by \\(1\\,000\\):\n"
        f"\\[ \\frac{{{mm3}}}{{1\\,000}} = {cm3_str}\\text{{ cm}}^3 \\]"
    )
    ans = f"{cm3_str} cm³"
    return {
        "id": f"g8_meas_mm3_cm3_{rng.randint(100000, 999999)}",
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
        "subskill": "25_convert_cubic_mm_to_cubic_cm",
        "learning_objective_id": "math_g8_meas_mm3_cm3",
        "hints": {
            "tier_1": "Divide by 1 000 to convert mm³ to cm³.",
            "tier_2": f"{mm3} / 1 000.",
            "tier_3": f"{cm3_str} cm³.",
        },
        "misconception_tags": ["dividing_by_100_instead_of_1000"],
    }
