"""Grade 7 Mathematics - Surface Area and Volume of 3D Objects: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/01. Surface area and volume of 3D objects.md
Focus: Cubes and rectangular prisms, surface area (closed and open-top), volume, unit cube counting, 3D isometric & net SVG diagrams, and metric conversions.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_cube_isometric(s: int, unit: str) -> str:
    """Return clean 2D isometric SVG diagram of a cube."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220" style="background:#ffffff;">\n'
        f'  <!-- Front Face -->\n'
        f'  <polygon points="60,110 160,110 160,200 60,200" fill="#e2e8f0" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Top Face -->\n'
        f'  <polygon points="60,110 120,50 220,50 160,110" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Right Face -->\n'
        f'  <polygon points="160,110 220,50 220,140 160,200" fill="#cbd5e1" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Dimension Labels -->\n'
        f'  <text x="110" y="216" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{s} {unit}</text>\n'
        f'  <text x="46" y="155" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="end">{s} {unit}</text>\n'
        f'  <text x="200" y="185" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="start">{s} {unit}</text>\n'
        f'  <text x="160" y="30" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Cube (all sides equal)</text>\n'
        f'</svg>'
    )


def _svg_prism_isometric(l: int, b: int, h: int, unit: str) -> str:
    """Return clean 2D isometric SVG diagram of a rectangular prism."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 220" width="100%" height="220" style="background:#ffffff;">\n'
        f'  <!-- Front Face -->\n'
        f'  <polygon points="40,110 180,110 180,190 40,190" fill="#e2e8f0" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Top Face -->\n'
        f'  <polygon points="40,110 110,50 250,50 180,110" fill="#f8fafc" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Right Face -->\n'
        f'  <polygon points="180,110 250,50 250,130 180,190" fill="#cbd5e1" stroke="#1e293b" stroke-width="2.5"/>\n'
        f'  <!-- Dimension Labels -->\n'
        f'  <text x="110" y="210" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">l = {l} {unit}</text>\n'
        f'  <text x="26" y="155" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="end">h = {h} {unit}</text>\n'
        f'  <text x="225" y="175" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="start">b = {b} {unit}</text>\n'
        f'  <text x="180" y="30" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Rectangular Prism</text>\n'
        f'</svg>'
    )


# 01. Cube surface area integer
def arch_01_cube_surface_area_integer(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 7, 8])
    sa = 6 * (s ** 2)
    ans = f"{sa} cm^2"
    prompt = (
        f"A cube has an edge length of \\({s}\\text{{ cm}}\\).\n\n"
        f"Calculate the **total surface area** of the cube."
    )
    sol = (
        f"**Step 1:** State the formula for the surface area of a cube (6 identical square faces):\n"
        f"$$\\text{{SA}} = 6s^2$$\n\n"
        f"**Step 2:** Substitute \\(s = {s}\\text{{ cm}}\\):\n"
        f"$$\\text{{SA}} = 6 \\times ({s})^2 = 6 \\times {s * s} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_01_{rng.randint(100000, 999999)}",
        "subskill": "01_cube_surface_area_integer",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_01",
        "hints": {"tier_1": f"One face area is {s} × {s}.", "tier_2": f"Multiply {s*s} by 6 faces.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_four_instead_of_six_for_cube_surface_area"]
    }


# 02. Cube surface area from face area
def arch_02_cube_surface_area_from_face_area(rng: random.Random) -> Dict[str, Any]:
    face_a = rng.choice([16, 25, 36, 49, 64])
    sa = 6 * face_a
    ans = f"{sa} cm^2"
    prompt = (
        f"The area of one face of a cube is \\({face_a}\\text{{ cm}}^2\\).\n\n"
        f"Determine the total surface area of the cube."
    )
    sol = (
        f"**Step 1:** A cube has 6 congruent square faces.\n\n"
        f"**Step 2:** Multiply the area of one face by 6:\n"
        f"$$\\text{{Total SA}} = 6 \\times {face_a} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_02_{rng.randint(100000, 999999)}",
        "subskill": "02_cube_surface_area_from_face_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_02",
        "hints": {"tier_1": "Cube has 6 faces.", "tier_2": f"6 × {face_a} = {sa}.", "tier_3": ans},
        "misconception_tags": ["squaring_face_area_again"]
    }


# 03. Cube edge from surface area
def arch_03_cube_edge_from_surface_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 8])
    sa = 6 * s * s
    ans = f"{s} cm"
    prompt = (
        f"The total surface area of a cube is \\({sa}\\text{{ cm}}^2\\).\n\n"
        f"Calculate the length of one edge \\(s\\) of the cube."
    )
    sol = (
        f"**Step 1:** Use formula \\(\\text{{SA}} = 6s^2\\):\n"
        f"$$6s^2 = {sa}$$\n\n"
        f"**Step 2:** Divide by 6 to find the area of one face:\n"
        f"$$s^2 = \\frac{{{sa}}}{{6}} = {s * s}$$\n\n"
        f"**Step 3:** Take the square root:\n"
        f"$$s = \\sqrt{{{s * s}}} = \\mathbf{{{s}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_sav_03_{rng.randint(100000, 999999)}",
        "subskill": "03_cube_edge_from_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_03",
        "hints": {"tier_1": f"Divide {sa} by 6 first.", "tier_2": f"s^2 = {s*s}, so s = {s}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_twelve_instead_of_six_for_cube_face_area"]
    }


# 04. Cube open top surface area
def arch_04_cube_open_top_surface_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 5, 6, 10])
    sa = 5 * (s ** 2)
    ans = f"{sa} cm^2"
    prompt = (
        f"An open-topped box in the shape of a cube has edge length \\({s}\\text{{ cm}}\\).\n"
        f"Because it has no lid, it consists of only 5 faces.\n\n"
        f"Calculate the total outside surface area of the box."
    )
    sol = (
        f"**Step 1:** An open box has 5 faces (1 base + 4 sides):\n"
        f"$$\\text{{SA}} = 5s^2$$\n\n"
        f"**Step 2:** Calculate:\n"
        f"$$\\text{{SA}} = 5 \\times ({s})^2 = 5 \\times {s * s} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_04_{rng.randint(100000, 999999)}",
        "subskill": "04_cube_open_top_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_04",
        "hints": {"tier_1": "Multiply face area by 5, not 6.", "tier_2": f"5 × {s*s} = {sa}.", "tier_3": ans},
        "misconception_tags": ["including_lid_face_in_open_box_surface_area"]
    }


# 05. Cube volume integer
def arch_05_cube_volume_integer(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 7])
    vol = s ** 3
    ans = f"{vol} cm^3"
    prompt = (
        f"A cube has sides measuring \\({s}\\text{{ cm}}\\).\n\n"
        f"Calculate the **volume** of the cube."
    )
    sol = (
        f"**Step 1:** State formula for volume of a cube:\n"
        f"$$V = s^3 = s \\times s \\times s$$\n\n"
        f"**Step 2:** Substitute \\(s = {s}\\text{{ cm}}\\):\n"
        f"$$V = {s} \\times {s} \\times {s} = {s * s} \\times {s} = \\mathbf{{{vol}}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_05_{rng.randint(100000, 999999)}",
        "subskill": "05_cube_volume_integer",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_05",
        "hints": {"tier_1": f"V = {s} × {s} × {s}.", "tier_2": f"{s*s} × {s} = {vol}.", "tier_3": ans},
        "misconception_tags": ["multiplying_side_by_three_instead_of_cubing"]
    }


# 06. Cube edge from volume
def arch_06_cube_edge_from_volume(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4, 5, 6])
    vol = s ** 3
    ans = f"{s} cm"
    prompt = (
        f"The volume of a wooden cube is \\({vol}\\text{{ cm}}^3\\).\n\n"
        f"Find the edge length \\(s\\) of the cube."
    )
    sol = (
        f"**Step 1:** Use formula \\(V = s^3 = {vol}\\).\n\n"
        f"**Step 2:** Find the cube root:\n"
        f"$$s = \\sqrt[3]{{{vol}}} = \\mathbf{{{s}}}\\text{{ cm}}$$\n\n"
        f"Check: \\({s} \\times {s} \\times {s} = {vol}\\)."
    )
    return {
        "id": f"g7_sav_06_{rng.randint(100000, 999999)}",
        "subskill": "06_cube_edge_from_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_06",
        "hints": {"tier_1": f"Find what number multiplied by itself three times gives {vol}.", "tier_2": f"s = {s}.", "tier_3": ans},
        "misconception_tags": ["dividing_volume_by_three_instead_of_taking_cube_root"]
    }


# 07. Cube volume and surface area comparison
def arch_07_cube_volume_and_surface_area_comparison(rng: random.Random) -> Dict[str, Any]:
    ans = "Both have numerical value 216, but units differ: V = 216 cm^3 and SA = 216 cm^2."
    prompt = (
        "A cube has edge length \\(6\\text{ cm}\\).\n\n"
        "1. Calculate its volume \\(V\\).\n"
        "2. Calculate its total surface area \\(SA\\).\n"
        "3. Compare the numerical values and units of \\(V\\) and \\(SA\\)."
    )
    sol = (
        "**Step 1:** Volume:\n"
        "$$V = 6^3 = 6 \\times 6 \\times 6 = \\mathbf{216}\\text{ cm}^3$$\n\n"
        "**Step 2:** Surface Area:\n"
        "$$\\text{SA} = 6 \\times 6^2 = 6 \\times 36 = \\mathbf{216}\\text{ cm}^2$$\n\n"
        "**Conclusion:** Both have the numerical value **216**, but volume is measured in cubic units (\\(\\text{cm}^3\\)) "
        "while surface area is measured in square units (\\(\\text{cm}^2\\))."
    )
    return {
        "id": f"g7_sav_07_{rng.randint(100000, 999999)}",
        "subskill": "07_cube_volume_and_surface_area_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_07",
        "hints": {"tier_1": "V = 6^3 = 216. SA = 6(36) = 216.", "tier_2": "Units are cm^3 vs cm^2.", "tier_3": ans},
        "misconception_tags": ["confusing_square_and_cubic_units"]
    }


# 08. Rectangular prism volume formula
def arch_08_prism_volume(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(4, 9)
    b = rng.randint(3, 6)
    h = rng.randint(2, 5)
    vol = l * b * h
    ans = f"{vol} cm^3"
    prompt = (
        f"A rectangular prism has length \\({l}\\text{{ cm}}\\), width \\({b}\\text{{ cm}}\\), and height \\({h}\\text{{ cm}}\\).\n\n"
        f"Calculate the **volume** of the prism."
    )
    sol = (
        f"**Step 1:** State the volume formula:\n"
        f"$$V = l \\times b \\times h$$\n\n"
        f"**Step 2:** Substitute values:\n"
        f"$$V = {l} \\times {b} \\times {h} = {l * b} \\times {h} = \\mathbf{{{vol}}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_08_{rng.randint(100000, 999999)}",
        "subskill": "08_prism_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_08",
        "hints": {"tier_1": f"Multiply {l} × {b} × {h}.", "tier_2": f"{l*b} × {h} = {vol}.", "tier_3": ans},
        "misconception_tags": ["adding_dimensions_instead_of_multiplying_for_volume"]
    }


# 09. Rectangular prism volume from base area
def arch_09_rectangular_prism_volume_from_base_area(rng: random.Random) -> Dict[str, Any]:
    base_a = rng.choice([24, 30, 40, 48, 60])
    h = rng.randint(4, 8)
    vol = base_a * h
    ans = f"{vol} cm^3"
    prompt = (
        f"A rectangular prism has a base area of \\({base_a}\\text{{ cm}}^2\\) and a height of \\({h}\\text{{ cm}}\\).\n\n"
        f"Calculate the volume of the prism."
    )
    sol = (
        f"**Step 1:** Use formula \\(V = \\text{{Base Area}} \\times \\text{{height}}\\):\n"
        f"$$V = {base_a} \\times {h} = \\mathbf{{{vol}}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_09_{rng.randint(100000, 999999)}",
        "subskill": "09_rectangular_prism_volume_from_base_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_09",
        "hints": {"tier_1": f"Multiply {base_a} by {h}.", "tier_2": f"{base_a} × {h} = {vol}.", "tier_3": ans},
        "misconception_tags": ["multiplying_base_area_by_extra_width_factor"]
    }


# 10. Rectangular prism height from volume
def arch_10_rectangular_prism_height_from_volume(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(5, 8)
    b = rng.randint(3, 5)
    h = rng.randint(4, 9)
    vol = l * b * h
    ans = f"{h} cm"
    prompt = (
        f"A rectangular prism has a volume of \\({vol}\\text{{ cm}}^3\\).\n"
        f"Its length is \\({l}\\text{{ cm}}\\) and its width is \\({b}\\text{{ cm}}\\).\n\n"
        f"Calculate the height \\(h\\) of the prism."
    )
    sol = (
        f"**Step 1:** Find base area:\n"
        f"$$\\text{{Base Area}} = l \\times b = {l} \\times {b} = {l * b}\\text{{ cm}}^2$$\n\n"
        f"**Step 2:** Divide volume by base area:\n"
        f"$$h = \\frac{{V}}{{{{l \\times b}}}} = \\frac{{{vol}}}{{{l * b}}} = \\mathbf{{{h}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_sav_10_{rng.randint(100000, 999999)}",
        "subskill": "10_rectangular_prism_height_from_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_10",
        "hints": {"tier_1": f"Base area = {l*b}.", "tier_2": f"Divide {vol} by {l*b}.", "tier_3": ans},
        "misconception_tags": ["dividing_volume_by_length_only"]
    }


# 11. Rectangular prism width from volume
def arch_11_rectangular_prism_width_from_volume(rng: random.Random) -> Dict[str, Any]:
    l = 10
    b = 4
    h = 6
    vol = l * b * h  # 240
    ans = "4 cm"
    prompt = (
        f"A carton has volume \\({vol}\\text{{ cm}}^3\\), length \\({l}\\text{{ cm}}\\), and height \\({h}\\text{{ cm}}\\).\n\n"
        f"Determine its width \\(b\\)."
    )
    sol = (
        f"**Step 1:** Calculate \\(l \\times h = {l} \\times {h} = {l * h}\\text{{ cm}}^2\\).\n\n"
        f"**Step 2:** Solve for width \\(b\\):\n"
        f"$$b = \\frac{{{vol}}}{{{l * h}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_sav_11_{rng.randint(100000, 999999)}",
        "subskill": "11_rectangular_prism_width_from_volume",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_11",
        "hints": {"tier_1": f"l × h = {l*h}.", "tier_2": f"{vol} / {l*h} = 4.", "tier_3": ans},
        "misconception_tags": ["subtracting_dimensions_from_volume"]
    }


# 12. Rectangular prism surface area closed
def arch_12_prism_surface_area(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(4, 8)
    b = rng.randint(3, 5)
    h = rng.randint(2, 4)
    sa = 2 * (l * b + l * h + b * h)
    ans = f"{sa} cm^2"
    prompt = (
        f"Calculate the **total surface area** of a closed rectangular prism with dimensions:\n"
        f"length \\(l = {l}\\text{{ cm}}\\), width \\(b = {b}\\text{{ cm}}\\), height \\(h = {h}\\text{{ cm}}\\)."
    )
    sol = (
        f"**Step 1:** Use surface area formula \\(\\text{{SA}} = 2(lb + lh + bh)\\):\n"
        f"- Top & bottom: \\(2(lb) = 2({l} \\times {b}) = 2({l * b}) = {2 * l * b}\\)\n"
        f"- Front & back: \\(2(lh) = 2({l} \\times {h}) = 2({l * h}) = {2 * l * h}\\)\n"
        f"- Left & right: \\(2(bh) = 2({b} \\times {h}) = 2({b * h}) = {2 * b * h}\\)\n\n"
        f"**Step 2:** Sum the three face pairs:\n"
        f"$$\\text{{SA}} = {2 * l * b} + {2 * l * h} + {2 * b * h} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_12_{rng.randint(100000, 999999)}",
        "subskill": "12_prism_surface_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_12",
        "hints": {"tier_1": "2(lb + lh + bh).", "tier_2": f"2({l*b} + {l*h} + {b*h}) = {sa}.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_double_face_pairs_in_surface_area"]
    }


# 13. Rectangular prism surface area open top
def arch_13_rectangular_prism_surface_area_open_top(rng: random.Random) -> Dict[str, Any]:
    l = 6
    b = 4
    h = 3
    # 1 bottom (lb) + 2(lh) + 2(bh) = 24 + 36 + 24 = 84
    sa = l * b + 2 * l * h + 2 * b * h
    ans = f"{sa} cm^2"
    prompt = (
        f"An open-top rectangular container has length \\({l}\\text{{ cm}}\\), width \\({b}\\text{{ cm}}\\), "
        f"and height \\({h}\\text{{ cm}}\\).\n"
        f"Because the top is open, it has only 5 faces.\n\n"
        f"Calculate the total outside surface area."
    )
    sol = (
        f"**Step 1:** Identify the 5 faces:\n"
        f"- 1 base: \\(l \\times b = {l} \\times {b} = {l * b}\\)\n"
        f"- 2 long sides: \\(2(lh) = 2({l} \\times {h}) = {2 * l * h}\\)\n"
        f"- 2 short sides: \\(2(bh) = 2({b} \\times {h}) = {2 * b * h}\\)\n\n"
        f"**Step 2:** Add all 5 face areas:\n"
        f"$$\\text{{SA}} = {l * b} + {2 * l * h} + {2 * b * h} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_13_{rng.randint(100000, 999999)}",
        "subskill": "13_rectangular_prism_surface_area_open_top",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_sav_13",
        "hints": {"tier_1": "Only 1 base face (lb), plus 2(lh) and 2(bh).", "tier_2": f"{l*b} + {2*l*h} + {2*b*h} = {sa}.", "tier_3": ans},
        "misconception_tags": ["including_sixth_top_face_in_open_box"]
    }


# 14. Rectangular prism net face sum
def arch_14_rectangular_prism_net_face_sum(rng: random.Random) -> Dict[str, Any]:
    l, b, h = rng.randint(5, 8), rng.randint(3, 5), rng.randint(2, 4)
    sa = 2 * (l * b + l * h + b * h)
    ans = f"{sa} cm^2"
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
        "The flat net of a rectangular prism consists of 6 rectangular faces:\n"
        f"- Two faces measuring \\({l}\\text{{ cm}} \\times {b}\\text{{ cm}}\\)\n"
        f"- Two faces measuring \\({l}\\text{{ cm}} \\times {h}\\text{{ cm}}\\)\n"
        f"- Two faces measuring \\({b}\\text{{ cm}} \\times {h}\\text{{ cm}}\\)\n\n"
        "Calculate the total area of the net (the surface area of the prism)."
    )
    sol = (
        "**Calculate area of each face pair:**\n"
        f"- \\(2 \\times ({l} \\times {b}) = 2 \\times {l*b} = {2*l*b}\\text{{ cm}}^2\\)\n"
        f"- \\(2 \\times ({l} \\times {h}) = 2 \\times {l*h} = {2*l*h}\\text{{ cm}}^2\\)\n"
        f"- \\(2 \\times ({b} \\times {h}) = 2 \\times {b*h} = {2*b*h}\\text{{ cm}}^2\\)\n\n"
        f"**Sum:** \\({2*l*b} + {2*l*h} + {2*b*h} = \\mathbf{{{sa}}}\\text{{ cm}}^2\\)."
    )
    return {
        "id": f"g7_sav_14_{rng.randint(100000, 999999)}",
        "subskill": "14_rectangular_prism_net_face_sum",
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
        "learning_objective_id": "math_g7_sav_14",
        "hints": {"tier_1": f"Add {2*l*b} + {2*l*h} + {2*b*h}.", "tier_2": f"{sa} cm^2.", "tier_3": ans},
        "misconception_tags": ["net_face_area_summation_error"]
    }


# 15. Count unit cubes in prism layer
def arch_15_count_unit_cubes_in_prism_layer(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(4, 6)
    b = rng.randint(3, 4)
    h = rng.randint(2, 3)
    layer = l * b
    total_cubes = layer * h
    ans = f"Layer: {layer} cubes; Total: {total_cubes} cubes"
    prompt = (
        f"A rectangular prism is built using \\(1\\text{{ cm}}^3\\) unit blocks.\n"
        f"The bottom layer is {l} cubes long and {b} cubes wide, and the model has {h} identical layers stacked high.\n\n"
        f"1. How many unit cubes are in one layer?\n"
        f"2. How many unit cubes are used in total?"
    )
    sol = (
        f"**Step 1:** Number of cubes in 1 layer = \\(l \\times b = {l} \\times {b} = \\mathbf{{{layer}}}\\text{{ cubes}}\\) (or \\({layer}\\text{{ cm}}^3\\)).\n\n"
        f"**Step 2:** Multiply by {h} layers:\n"
        f"$$\\text{{Total cubes}} = {layer} \\times {h} = \\mathbf{{{total_cubes}}}\\text{{ cubes}}$$"
    )
    return {
        "id": f"g7_sav_15_{rng.randint(100000, 999999)}",
        "subskill": "15_count_unit_cubes_in_prism_layer",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_15",
        "hints": {"tier_1": f"Layer = {l} × {b}.", "tier_2": f"Total = {layer} × {h}.", "tier_3": ans},
        "misconception_tags": ["counting_only_visible_outer_cubes"]
    }


# 16. Isometric cube SVG volume
def arch_16_isometric_cube_svg_volume(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 7, 8, 9])
    vol = s ** 3
    ans = f"{vol} cm^3"
    svg = _svg_cube_isometric(s, "cm")
    prompt = (
        "Inspect the 3D isometric representation of the cube shown below:\n\n"
        "Calculate the volume \\(V\\) of this cube."
    )
    sol = (
        f"**Step 1:** A cube has equal edges \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"**Step 2:** Apply volume formula:\n"
        f"$$V = s^3 = {s} \\times {s} \\times {s} = \\mathbf{{{vol}}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_16_{rng.randint(100000, 999999)}",
        "subskill": "16_isometric_cube_svg_volume",
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
        "learning_objective_id": "math_g7_sav_16",
        "hints": {"tier_1": f"V = {s}^3.", "tier_2": f"{s} × {s} × {s} = {vol}.", "tier_3": ans},
        "misconception_tags": ["confusing_cube_volume_with_surface_area"]
    }


# 17. Isometric rectangular prism SVG surface area
def arch_17_isometric_rectangular_prism_svg_sa(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(5, 9)
    b = rng.randint(2, 4)
    h = rng.randint(3, 6)
    sa = 2 * (l * b + l * h + b * h)
    ans = f"{sa} cm^2"
    svg = _svg_prism_isometric(l, b, h, "cm")
    prompt = (
        "Refer to the 3D diagram of the rectangular prism below:\n\n"
        "Calculate the total surface area of the prism."
    )
    sol = (
        f"**Step 1:** Identify dimensions: \\(l = {l}\\text{{ cm}}\\), \\(b = {b}\\text{{ cm}}\\), \\(h = {h}\\text{{ cm}}\\).\n\n"
        f"**Step 2:** Compute \\(\\text{{SA}} = 2(lb + lh + bh)\\):\n"
        f"$$\\text{{SA}} = 2({l} \\times {b} + {l} \\times {h} + {b} \\times {h}) = 2({l*b} + {l*h} + {b*h}) = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_17_{rng.randint(100000, 999999)}",
        "subskill": "17_isometric_rectangular_prism_svg_sa",
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
        "learning_objective_id": "math_g7_sav_17",
        "hints": {"tier_1": "2(lb + lh + bh).", "tier_2": f"2({l*b} + {l*h} + {b*h}) = {sa}.", "tier_3": ans},
        "misconception_tags": ["surface_area_from_diagram_dimension_misreading"]
    }


# 18. Isometric rectangular prism SVG volume
def arch_18_isometric_rectangular_prism_svg_volume(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(6, 10)
    b = rng.randint(3, 6)
    h = rng.randint(2, 5)
    vol = l * b * h
    ans = f"{vol} cm^3"
    svg = _svg_prism_isometric(l, b, h, "cm")
    prompt = (
        "Look at the rectangular prism shown in the diagram:\n\n"
        "Determine the volume \\(V\\) of this rectangular prism."
    )
    sol = (
        f"**Step 1:** Formula: \\(V = l \\times b \\times h\\).\n\n"
        f"**Step 2:** Calculate: \\(V = {l} \\times {b} \\times {h} = {l * b} \\times {h} = \\mathbf{{{vol}}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_18_{rng.randint(100000, 999999)}",
        "subskill": "18_isometric_rectangular_prism_svg_volume",
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
        "learning_objective_id": "math_g7_sav_18",
        "hints": {"tier_1": f"Multiply {l} × {b} × {h}.", "tier_2": f"{vol} cm^3.", "tier_3": ans},
        "misconception_tags": ["arithmetic_volume_calculation_error"]
    }


# 19. Net of cube SVG surface area
def arch_19_net_of_cube_svg_surface_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(3, 9)
    sa = 6 * (s ** 2)
    ans = f"{sa} cm^2"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 220" width="100%" height="190" style="background:#ffffff;">'
        '<rect x="100" y="20" width="45" height="45" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="100" y="65" width="45" height="45" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="100" y="110" width="45" height="45" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="100" y="155" width="45" height="45" fill="#e2e8f0" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="55" y="65" width="45" height="45" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>'
        '<rect x="145" y="65" width="45" height="45" fill="#dbeafe" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="140" y="214" text-anchor="middle" font-size="11" fill="#0f172a">Cube Net (side = {s} cm)</text>'
        '</svg>'
    )
    prompt = (
        f"The cross-shaped net of a cube has 6 congruent square flaps, each with side length \\({s}\\text{{ cm}}\\).\n\n"
        "Calculate the total area of the net."
    )
    sol = (
        f"**Step 1:** Area of 1 square face = \\({s} \\times {s} = {s*s}\\text{{ cm}}^2\\).\n\n"
        "**Step 2:** Multiply by 6 faces:\n"
        f"$$\\text{{Total SA}} = 6 \\times {s*s} = \\mathbf{{{sa}}}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_sav_19_{rng.randint(100000, 999999)}",
        "subskill": "19_net_of_cube_svg_surface_area",
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
        "learning_objective_id": "math_g7_sav_19",
        "hints": {"tier_1": f"1 face = {s} × {s} = {s*s}.", "tier_2": f"6 × {s*s} = {sa}.", "tier_3": ans},
        "misconception_tags": ["net_face_count_error"]
    }


# 20. Net of rectangular prism SVG SA
def arch_20_net_of_rectangular_prism_svg_sa(rng: random.Random) -> Dict[str, Any]:
    l, b, h = rng.randint(6, 9), rng.randint(4, 6), rng.randint(2, 4)
    sa = 2 * (l * b + l * h + b * h)
    ans = f"{sa} cm^2"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="180" style="background:#ffffff;">'
        '<rect x="100" y="20" width="80" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="60" width="80" height="30" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="90" width="80" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="100" y="130" width="80" height="30" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="60" y="90" width="40" height="40" fill="#dbeafe" stroke="#0284c7" stroke-width="2"/>'
        '<rect x="180" y="90" width="40" height="40" fill="#dbeafe" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="140" y="185" text-anchor="middle" font-size="11" fill="#0f172a">Prism Net ({l} cm × {b} cm × {h} cm)</text>'
        '</svg>'
    )
    prompt = (
        f"The unfolded net of a rectangular prism with \\(l = {l}\\text{{ cm}}\\), \\(b = {b}\\text{{ cm}}\\), "
        f"and \\(h = {h}\\text{{ cm}}\\) is laid flat on a table.\n\n"
        "Calculate the total surface area of this net."
    )
    sol = (
        "**Step 1:** Face areas in pairs:\n"
        f"- \\(2({l} \\times {b}) = 2({l*b}) = {2*l*b}\\)\n"
        f"- \\(2({l} \\times {h}) = 2({l*h}) = {2*l*h}\\)\n"
        f"- \\(2({b} \\times {h}) = 2({b*h}) = {2*b*h}\\)\n\n"
        f"**Step 2:** Total: \\({2*l*b} + {2*l*h} + {2*b*h} = \\mathbf{{{sa}}}\\text{{ cm}}^2\\)."
    )
    return {
        "id": f"g7_sav_20_{rng.randint(100000, 999999)}",
        "subskill": "20_net_of_rectangular_prism_svg_sa",
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
        "learning_objective_id": "math_g7_sav_20",
        "hints": {"tier_1": f"2({l*b} + {l*h} + {b*h}).", "tier_2": f"{2*l*b} + {2*l*h} + {2*b*h} = {sa}.", "tier_3": ans},
        "misconception_tags": ["rectangular_net_surface_area_sum_error"]
    }


# 21. Unit conversion cm3 to mm3
def arch_21_unit_conversion_cm3_to_mm3(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.randint(3, 9)
    mm3 = cm3 * 1000
    ans = f"{mm3} mm^3"
    prompt = (
        f"Convert \\({cm3}\\text{{ cm}}^3\\) into cubic millimetres (\\(\\text{{mm}}^3\\))."
    )
    sol = (
        f"**Step 1:** Recall the cubic relationship between cm and mm:\n"
        f"$$1\\text{{ cm}} = 10\\text{{ mm}}$$\n"
        f"$$1\\text{{ cm}}^3 = 10\\text{{ mm}} \\times 10\\text{{ mm}} \\times 10\\text{{ mm}} = 1\\,000\\text{{ mm}}^3$$\n\n"
        f"**Step 2:** Multiply by 1 000:\n"
        f"$${cm3} \\times 1\\,000 = \\mathbf{{{mm3}}}\\text{{ mm}}^3$$"
    )
    return {
        "id": f"g7_sav_21_{rng.randint(100000, 999999)}",
        "subskill": "21_unit_conversion_cm3_to_mm3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_21",
        "hints": {"tier_1": "1 cm^3 = 1000 mm^3.", "tier_2": f"Multiply {cm3} by 1000.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_ten_instead_of_thousand_in_cubic_conversion"]
    }


# 22. Unit conversion mm3 to cm3
def arch_22_unit_conversion_mm3_to_cm3(rng: random.Random) -> Dict[str, Any]:
    mm3 = 4500
    ans = "4,5 cm^3"
    prompt = (
        f"Convert \\({mm3}\\text{{ mm}}^3\\) to cubic centimetres (\\(\\text{{cm}}^3\\))."
    )
    sol = (
        f"**Step 1:** Since \\(1\\text{{ cm}}^3 = 1000\\text{{ mm}}^3\\), divide by 1 000:\n"
        f"$$\\frac{{{mm3}}}{{1000}} = \\mathbf{{4{{,}}5}}\\text{{ cm}}^3$$"
    )
    return {
        "id": f"g7_sav_22_{rng.randint(100000, 999999)}",
        "subskill": "22_unit_conversion_mm3_to_cm3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_22",
        "hints": {"tier_1": "Divide by 1000.", "tier_2": "4500 / 1000 = 4,5.", "tier_3": ans},
        "misconception_tags": ["dividing_by_hundred_instead_of_thousand"]
    }


# 23. Unit conversion m3 to cm3
def arch_23_unit_conversion_m3_to_cm3(rng: random.Random) -> Dict[str, Any]:
    ans = "2 000 000 cm^3"
    prompt = (
        "Convert \\(2\\text{ m}^3\\) into cubic centimetres (\\(\\text{cm}^3\\))."
    )
    sol = (
        "**Step 1:** Understand the cubic conversion:\n"
        "$$1\\text{ m} = 100\\text{ cm}$$\n"
        "$$1\\text{ m}^3 = 100\\text{ cm} \\times 100\\text{ cm} \\times 100\\text{ cm} = 1\\,000\\,000\\text{ cm}^3$$\n\n"
        "**Step 2:** Multiply by 1 000 000:\n"
        "$$2 \\times 1\\,000\\,000 = \\mathbf{2\\,000\\,000}\\text{ cm}^3$$"
    )
    return {
        "id": f"g7_sav_23_{rng.randint(100000, 999999)}",
        "subskill": "23_unit_conversion_m3_to_cm3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_23",
        "hints": {"tier_1": "1 m^3 = 1 000 000 cm^3.", "tier_2": "2 × 1 000 000 = 2 000 000.", "tier_3": ans},
        "misconception_tags": ["multiplying_by_hundred_instead_of_one_million"]
    }


# 24. Unit conversion cm3 to m3
def arch_24_unit_conversion_cm3_to_m3(rng: random.Random) -> Dict[str, Any]:
    ans = "3 m^3"
    prompt = (
        "Convert \\(3\\,000\\,000\\text{ cm}^3\\) to cubic metres (\\(\\text{m}^3\\))."
    )
    sol = (
        "**Step 1:** Divide by 1 000 000:\n"
        "$$\\frac{3\\,000\\,000}{1\\,000\\,000} = \\mathbf{3}\\text{ m}^3$$"
    )
    return {
        "id": f"g7_sav_24_{rng.randint(100000, 999999)}",
        "subskill": "24_unit_conversion_cm3_to_m3",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_sav_24",
        "hints": {"tier_1": "Divide by 1 000 000.", "tier_2": "3 000 000 / 1 000 000 = 3.", "tier_3": ans},
        "misconception_tags": ["dividing_by_thousand_instead_of_one_million"]
    }


# 25. Capacity conversion cm3 to ml
def arch_25_volume_capacity_conversion(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.choice([250, 330, 500, 750])
    ans = f"{cm3} ml"
    prompt = (
        f"A juice box has an internal volume of \\({cm3}\\text{{ cm}}^3\\).\n\n"
        f"What is its capacity in millilitres (\\(\\text{{ml}}\\))?"
    )
    sol = (
        f"**Step 1:** Use the exact equivalence between cubic centimetres and millilitres:\n"
        f"$$1\\text{{ cm}}^3 = 1\\text{{ ml}}$$\n\n"
        f"**Step 2:** Therefore:\n"
        f"$${cm3}\\text{{ cm}}^3 = \\mathbf{{{cm3}}}\\text{{ ml}}$$"
    )
    return {
        "id": f"g7_sav_25_{rng.randint(100000, 999999)}",
        "subskill": "25_volume_capacity_conversion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_sav_25",
        "hints": {"tier_1": "1 cm^3 = 1 ml.", "tier_2": f"Answer is {cm3} ml.", "tier_3": ans},
        "misconception_tags": ["thinking_one_cm3_is_not_equal_to_one_ml"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
