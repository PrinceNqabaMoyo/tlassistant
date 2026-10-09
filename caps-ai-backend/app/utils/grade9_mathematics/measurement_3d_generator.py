"""Grade 9 Mathematics - Measurement of 3D Objects Generator.
Covers:
  - Surface Area of Right Cylinders (closed & open): SA = 2*pi*r^2 + 2*pi*r*h
  - Volume of Right Cylinders: V = pi*r^2*h
  - Surface Area and Volume of Right Triangular and Rectangular Prisms
  - Capacity and Unit Conversions (cm^3 to ml/litres, m^3 to kilolitres)

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _format_sa_num(val: float, decimals: int = 2) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


def generate_grade9_measurement_3d_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "measurement_3d_cylinders"

    archetype = r.choice(["cylinder_volume", "cylinder_surface_area", "cylinder_open_tank", "triangular_prism"])
    if subskill == "elementary_base_area":
        archetype = "elementary_base_area"
    elif subskill == "elementary_curved_surface":
        archetype = "elementary_curved_surface"

    if archetype == "elementary_base_area":
        radius = r.choice([3, 4, 5, 7, 10, 14])
        area = math.pi * (radius ** 2)
        area_str = _format_sa_num(area, 2)
        prompt = (
            f"Calculate the area of the circular base of a cylinder with radius \\(r = {radius}\\text{{ cm}}\\). "
            r"Use $\pi \approx 3{,}142$ or your calculator $\pi$ key. Round your answer to two decimal places."
        )
        sample_answer = rf"A = \pi r^2 = \pi ({radius})^2 \approx {area_str}\text{{ cm}}^2"
        return {
            "id": f"g9_meas3d_base_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Measurement of 3D Objects",
            "subskill": "elementary_base_area",
            "learning_objective_id": "g9_meas3d_base_area",
            "archetype": "elementary_base_area",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": area_str,
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Correct circular base formula A = pi * r^2", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Accurate calculation and rounding", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "rounding_error", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Recall that the base of a cylinder is a simple circle with radius r.",
                "tier_2": r"Apply $A = \pi r^2$ using the given radius.",
                "tier_3": rf"Substitute $r = {radius}$: $A = \pi \times {radius}^2 \approx {area_str}\text{{ cm}}^2$.",
            },
            "misconception_tags": ["diameter_instead_of_radius", "forgot_square_radius"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "elementary_curved_surface":
        radius = r.choice([3, 4, 5, 7, 10])
        height = r.choice([6, 8, 12, 15, 20])
        curved_area = 2 * math.pi * radius * height
        curved_str = _format_sa_num(curved_area, 2)
        prompt = (
            f"Calculate the curved (lateral) surface area of a cylinder with radius \\(r = {radius}\\text{{ cm}}\\) "
            f"and height \\(h = {height}\\text{{ cm}}\\). Round your answer to two decimal places."
        )
        sample_answer = rf"\text{{Area}}_{{\text{{curved}}}} = 2\pi rh = 2\pi ({radius})({height}) \approx {curved_str}\text{{ cm}}^2"
        return {
            "id": f"g9_meas3d_curved_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Measurement of 3D Objects",
            "subskill": "elementary_curved_surface",
            "learning_objective_id": "g9_meas3d_curved_area",
            "archetype": "elementary_curved_surface",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": curved_str,
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Curved surface area formula 2*pi*r*h", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Accurate calculation", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "The curved surface when unrolled forms a rectangle with width 2*pi*r and length h.",
                "tier_2": r"Use the formula $\text{Area} = 2\pi rh$.",
                "tier_3": rf"Multiply $2 \times \pi \times {radius} \times {height} \approx {curved_str}\text{{ cm}}^2$.",
            },
            "misconception_tags": ["forgot_factor_of_two", "included_circular_bases"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "cylinder_surface_area":
        radius = r.choice([3, 5, 7, 8, 10])
        height = r.choice([10, 12, 14, 15, 20])
        total_sa = 2 * math.pi * radius * (radius + height)
        sa_str = _format_sa_num(total_sa, 2)
        base_area = math.pi * (radius ** 2)
        curved_area = 2 * math.pi * radius * height

        prompt = (
            f"A closed cylindrical metal container has a radius of \\(r = {radius}\\text{{ cm}}\\) and a height of \\(h = {height}\\text{{ cm}}\\).\n\n"
            f"1. Calculate the total surface area of the cylinder.\n"
            f"2. Give your answer correct to two decimal places."
        )
        sample_answer = rf"\text{{Total SA}} = 2\pi r^2 + 2\pi rh = 2\pi({radius})^2 + 2\pi({radius})({height}) \approx {sa_str}\text{{ cm}}^2"
        return {
            "id": f"g9_meas3d_sa_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Measurement of 3D Objects",
            "subskill": "surface_area_cylinder",
            "learning_objective_id": "g9_meas3d_surface_area",
            "archetype": "cylinder_surface_area",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": sa_str,
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": "Closed cylinder SA formula 2*pi*r^2 + 2*pi*r*h", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Correct substitution of radius and height", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Circular bases plus curved area calculation", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Final total with correct rounding", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_units", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "A closed cylinder has two circular ends (top and bottom) and one curved rectangular surface.",
                "tier_2": r"Use $\text{Total SA} = 2\pi r^2 + 2\pi rh$ or $2\pi r(r + h)$.",
                "tier_3": rf"Substitute: $2\pi({radius})^2 + 2\pi({radius})({height}) \approx {_format_sa_num(2*base_area, 2)} + {_format_sa_num(curved_area, 2)} = {sa_str}\text{{ cm}}^2$.",
            },
            "misconception_tags": ["forgot_both_circular_bases", "diameter_instead_of_radius", "volume_surface_area_confusion"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "cylinder_open_tank":
        diameter = r.choice([6, 8, 10, 14])
        radius = diameter / 2
        height = r.choice([5, 10, 15, 20])
        # Open tank: 1 circular base + curved surface area
        sa_open = (math.pi * (radius ** 2)) + (2 * math.pi * radius * height)
        sa_str = _format_sa_num(sa_open, 2)
        vol = math.pi * (radius ** 2) * height
        litres = vol / 1000
        litres_str = _format_sa_num(litres, 2)

        prompt = (
            f"An open cylindrical water tank (without a top lid) has a base diameter of \\(d = {diameter}\\text{{ cm}}\\) "
            f"and a height of \\(h = {height}\\text{{ cm}}\\).\n\n"
            f"1. Calculate the outer surface area of the tank that needs to be waterproofed (one base plus curved surface).\n"
            f"2. Determine its maximum capacity in litres, knowing that \\(1\\ 000\\text{{ cm}}^3 = 1\\text{{ litre}}\\).\n"
            f"Round both answers to two decimal places."
        )
        sample_answer = (
            rf"r = \frac{{{diameter}}}{{2}} = {int(radius)}\text{{ cm}};\ "
            rf"\text{{SA}} = \pi({int(radius)})^2 + 2\pi({int(radius)})({height}) \approx {sa_str}\text{{ cm}}^2;\ "
            rf"V = \pi({int(radius)})^2({height}) \approx {_format_sa_num(vol, 2)}\text{{ cm}}^3 \implies \frac{{{_format_sa_num(vol, 2)}}}{{1\,000}} = {litres_str}\text{{ litres}}"
        )
        return {
            "id": f"g9_meas3d_open_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Measurement of 3D Objects",
            "subskill": "open_cylinder_capacity",
            "learning_objective_id": "g9_meas3d_open_cylinder",
            "archetype": "cylinder_open_tank",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": sa_str,
            "marks": 5,
            "marking_schema": {
                "total_marks": 5,
                "marking_points": [
                    {"id": "mp_1", "desc": "Radius = diameter / 2", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Open cylinder SA formula (one base)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Accurate surface area calculation", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Volume calculation V = pi * r^2 * h", "marks": 1, "editable": True},
                    {"id": "mp_5", "desc": "Capacity conversion (divide cm^3 by 1000 to get litres)", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Watch out: the tank has NO lid, so include only ONE circular base. Also, divide diameter by 2 to get the radius.",
                "tier_2": r"Apply $\text{SA} = \pi r^2 + 2\pi rh$. Then find volume $V = \pi r^2 h$ and divide by $1\,000$ for litres.",
                "tier_3": rf"Radius is ${int(radius)}\text{{ cm}}$. $\text{{SA}} \approx {sa_str}\text{{ cm}}^2$, and Capacity $\approx {litres_str}\text{{ litres}}$.",
            },
            "misconception_tags": ["diameter_instead_of_radius", "used_two_bases_for_open_tank", "linear_unit_conversion_error"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 5,
            "mode": mode,
            "difficulty": "hard",
        }

    else:
        # Triangular Prism
        base_tri = r.choice([6, 8, 10, 12])
        height_tri = r.choice([4, 5, 6, 8])
        length_prism = r.choice([12, 15, 20, 25])
        tri_area = 0.5 * base_tri * height_tri
        vol = tri_area * length_prism
        vol_str = _format_sa_num(vol, 0)

        prompt = (
            f"A right prism has a right-angled triangular base with perpendicular sides of \\({base_tri}\\text{{ cm}}\\) "
            f"and \\({height_tri}\\text{{ cm}}\\). The length of the prism is \\({length_prism}\\text{{ cm}}\\).\n\n"
            f"1. Calculate the area of the triangular base.\n"
            f"2. Calculate the volume of the triangular prism."
        )
        sample_answer = rf"\text{{Base Area}} = \frac{{1}}{{2}}({base_tri})({height_tri}) = {int(tri_area)}\text{{ cm}}^2;\ V = {int(tri_area)} \times {length_prism} = {vol_str}\text{{ cm}}^3"
        return {
            "id": f"g9_meas3d_tri_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Measurement of 3D Objects",
            "subskill": "volume_triangular_prism",
            "learning_objective_id": "g9_meas3d_triangular_prism",
            "archetype": "triangular_prism",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": vol_str,
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": "Base triangular area formula 1/2 * b * h", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Calculation of base area", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Prism volume calculation V = Base Area * length", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Recall that the volume of any right prism is Base Area multiplied by Length.",
                "tier_2": r"First find the area of the triangular cross-section: $\frac{1}{2} \times \text{base} \times \text{height}$.",
                "tier_3": rf"$\text{{Area}} = \frac{{1}}{{2}} \times {base_tri} \times {height_tri} = {int(tri_area)}\text{{ cm}}^2$. Multiply by ${length_prism}$: $V = {vol_str}\text{{ cm}}^3$.",
            },
            "misconception_tags": ["forgot_half_factor", "volume_surface_area_confusion"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade9_measurement_3d_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
