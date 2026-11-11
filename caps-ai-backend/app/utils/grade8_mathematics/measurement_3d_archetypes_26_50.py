"""Grade 8 Mathematics — Surface Area & Volume of 3D Objects Archetypes (26 to 50).
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 4/01. Surface area and volume of 3D objects.md

Archetypes covered:
  26. Conversion: Cubic metres to cubic centimetres (multiply by 1 000 000).
  27. Conversion: Cubic centimetres to cubic metres (divide by 1 000 000).
  28. Conversion: Mixed cubic units addition (m³ and cm³).
  29. Capacity: Definition and conceptual relationship to volume.
  30. Capacity: Convert cubic centimetres to millilitres (1 cm³ = 1 ml).
  31. Capacity: Convert cubic centimetres to litres (1 000 cm³ = 1 L).
  32. Capacity: Convert litres to cubic centimetres (multiply by 1 000).
  33. Capacity: Convert cubic metres to kilolitres (1 m³ = 1 kl).
  34. Capacity: Convert kilolitres to litres (1 kl = 1 000 L).
  35. Application: Fish tank capacity in litres (WITH SVG).
  36. Application: Swimming pool volume and capacity in kilolitres (WITH SVG).
  37. Application: Internal vs external dimensions and wall thickness (WITH SVG).
  38. Application: Hollow container holding capacity with wall thickness.
  39. Displacement: Water displacement volume by submerged metal solid.
  40. Displacement: Water level rise in rectangular prism container from added object.
  41. Scaling: Doubling edge of cube increases surface area by factor of 4 (2²).
  42. Scaling: Doubling edge of cube increases volume by factor of 8 (2³).
  43. Scaling: Tripling all dimensions of rectangular prism increases volume by 27 (3³).
  44. Synthesis: Rectangular prisms with equal volume having different surface areas.
  45. Composite 3D: Volume of cube mounted on rectangular prism (WITH SVG).
  46. Composite 3D: Surface area of cube mounted on rectangular prism (WITH SVG).
  47. Composite 3D: Volume of L-shaped prism from decomposed rectangular blocks.
  48. Context: Paint coverage for room walls and ceiling excluding floor.
  49. Packaging: Maximum number of small cubic boxes fitting into large packing carton.
  50. Rate of filling: Time to fill a water reservoir given constant tap flow rate.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .measurement_3d_svg import (
    draw_composite_prism_svg,
    draw_rectangular_prism_3d_svg,
    draw_tank_water_svg,
)


def _fmt_dec(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


# ----------------------------------------------------------------------
# 26. Conversion: Cubic Metres to Cubic Centimetres
# ----------------------------------------------------------------------
def arch_26_convert_cubic_m_to_cubic_cm(rng: random.Random) -> Dict[str, Any]:
    m3 = rng.choice([2, 3, 5, 8, 12])
    cm3 = m3 * 1000000

    prompt = (
        f"Convert \\({m3}\\text{{ m}}^3\\) into cubic centimetres (\\(\\text{{cm}}^3\\)).\n\n"
        f"Show why the conversion factor is \\(1\\,000\\,000\\)."
    )
    sol = (
        f"**Conversion Explanation:**\n"
        f"Since \\(1\\text{{ m}} = 100\\text{{ cm}}\\):\n"
        f"\\[ 1\\text{{ m}}^3 = 100\\text{{ cm}} \\times 100\\text{{ cm}} \\times 100\\text{{ cm}} = 1\\,000\\,000\\text{{ cm}}^3 \\]\n"
        f"Therefore, multiply by \\(1\\,000\\,000\\):\n"
        f"\\[ {m3}\\text{{ m}}^3 = {m3} \\times 1\\,000\\,000 = {cm3:,}\\text{{ cm}}^3 \\]".replace(",", " ")
    )
    ans = f"{cm3:,} cm³".replace(",", " ")
    return {
        "id": f"g8_meas_m3_cm3_{rng.randint(100000, 999999)}",
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
        "subskill": "26_convert_cubic_m_to_cubic_cm",
        "learning_objective_id": "math_g8_meas_m3_cm3",
        "hints": {
            "tier_1": "1 m³ = 100 cm × 100 cm × 100 cm = 1 000 000 cm³.",
            "tier_2": f"Multiply {m3} by 1 000 000.",
            "tier_3": f"{cm3} cm³.",
        },
        "misconception_tags": ["multiplying_by_100_instead_of_1000000"],
    }


# ----------------------------------------------------------------------
# 27. Conversion: Cubic Centimetres to Cubic Metres
# ----------------------------------------------------------------------
def arch_27_convert_cubic_cm_to_cubic_m(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.choice([2500000, 4000000, 7500000, 15000000])
    m3_val = cm3 / 1000000.0
    m3_str = _fmt_dec(m3_val, 3)

    prompt = (
        f"Convert \\({cm3:,}\\text{{ cm}}^3\\) into cubic metres (\\(\\text{{m}}^3\\)).".replace(",", " ")
    )
    sol = (
        f"**Conversion Calculation:**\n"
        f"Since \\(1\\,000\\,000\\text{{ cm}}^3 = 1\\text{{ m}}^3\\), divide by \\(1\\,000\\,000\\):\n"
        f"\\[ \\frac{{{cm3}}}{{1\\,000\\,000}} = {m3_str}\\text{{ m}}^3 \\]"
    )
    ans = f"{m3_str} m³"
    return {
        "id": f"g8_meas_cm3_m3_{rng.randint(100000, 999999)}",
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
        "subskill": "27_convert_cubic_cm_to_cubic_m",
        "learning_objective_id": "math_g8_meas_cm3_m3",
        "hints": {
            "tier_1": "Divide by 1 000 000 to convert cm³ to m³.",
            "tier_2": f"{cm3} / 1 000 000.",
            "tier_3": f"{m3_str} m³.",
        },
        "misconception_tags": ["dividing_by_1000_instead_of_1000000"],
    }


# ----------------------------------------------------------------------
# 28. Conversion: Mixed Cubic Units Addition
# ----------------------------------------------------------------------
def arch_28_convert_mixed_cubic_units_addition(rng: random.Random) -> Dict[str, Any]:
    m3 = rng.choice([2, 4, 7, 10])
    cm3 = rng.choice([65, 120, 450, 800])
    total_cm3 = m3 * 1000000 + cm3

    prompt = (
        f"Calculate the following sum, giving your final answer in \\(\\text{{cm}}^3\\):\n\n"
        f"\\[ {m3}\\text{{ m}}^3 + {cm3}\\text{{ cm}}^3 \\]"
    )
    sol = (
        f"**Step-by-Step Calculation:**\n"
        f"1. Convert \\({m3}\\text{{ m}}^3\\) to \\(\\text{{cm}}^3\\):\n"
        f"\\[ {m3}\\text{{ m}}^3 = {m3} \\times 1\\,000\\,000 = {m3*1000000:,}\\text{{ cm}}^3 \\]\n"
        f"2. Add \\({cm3}\\text{{ cm}}^3\\):\n"
        f"\\[ {m3*1000000:,} + {cm3} = {total_cm3:,}\\text{{ cm}}^3 \\]".replace(",", " ")
    )
    ans = f"{total_cm3:,} cm³".replace(",", " ")
    return {
        "id": f"g8_meas_add_units_{rng.randint(100000, 999999)}",
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
        "subskill": "28_convert_mixed_cubic_units_addition",
        "learning_objective_id": "math_g8_meas_add_units",
        "hints": {
            "tier_1": f"First convert {m3} m³ to cm³: multiply by 1 000 000.",
            "tier_2": f"{m3*1000000} + {cm3}.",
            "tier_3": f"{total_cm3} cm³.",
        },
        "misconception_tags": ["adding_values_directly_without_converting_to_common_units"],
    }


# ----------------------------------------------------------------------
# 29. Capacity: Definition & Relation to Volume
# ----------------------------------------------------------------------
def arch_29_capacity_definition_and_relation_to_volume(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the scientific and mathematical difference between the **volume** of a container "
        "and the **capacity** of the container. Provide an everyday example illustrating when the two are different."
    )
    sol = (
        "**Difference Between Volume and Capacity:**\n"
        "1. **Volume:** The amount of physical 3D space that the exterior of the object occupies in the environment.\n"
        "2. **Capacity:** The volume of liquid or gas that can be held *inside* the hollow interior of the container.\n\n"
        "**Illustrative Example:**\n"
        "A thick-walled wooden chest or glass vase has an external volume determined by its outer dimensions. "
        "Because the walls and base have thickness, the space inside (its capacity) is smaller than the total space "
        "the object takes up externally."
    )
    ans = "Volume is space taken up by the object externally; capacity is the amount of fluid it can hold internally (reduced by wall thickness)"
    return {
        "id": f"g8_meas_cap_def_{rng.randint(100000, 999999)}",
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
        "subskill": "29_capacity_definition_and_relation_to_volume",
        "learning_objective_id": "math_g8_meas_cap_def",
        "hints": {
            "tier_1": "Volume is outer space occupied; capacity is inner space available to hold contents.",
            "tier_2": "Wall thickness creates a difference between external volume and internal capacity.",
            "tier_3": ans,
        },
        "misconception_tags": ["treating_volume_and_capacity_as_identical_in_thick_walled_objects"],
    }


# ----------------------------------------------------------------------
# 30. Capacity: Convert Cubic cm to Millilitres
# ----------------------------------------------------------------------
def arch_30_convert_cubic_cm_to_millilitres(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.choice([45, 120, 350, 750, 1500])
    ml = cm3

    prompt = (
        f"A medical syringe holds \\({cm3}\\text{{ cm}}^3\\) of liquid.\n\n"
        f"State the capacity of this liquid in millilitres (\\(\\text{{ml}}\\)), explaining the exact conversion relation."
    )
    sol = (
        f"**Equivalence Between cm³ and ml:**\n"
        f"By standard metric definition, \\(1\\text{{ cm}}^3 = 1\\text{{ ml}}\\).\n"
        f"Therefore:\n"
        f"\\[ {cm3}\\text{{ cm}}^3 = {ml}\\text{{ ml}} \\]"
    )
    ans = f"{ml} ml"
    return {
        "id": f"g8_meas_cm3_ml_{rng.randint(100000, 999999)}",
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
        "subskill": "30_convert_cubic_cm_to_millilitres",
        "learning_objective_id": "math_g8_meas_cm3_ml",
        "hints": {
            "tier_1": "1 cubic centimetre is identically equal to 1 millilitre: 1 cm³ = 1 ml.",
            "tier_2": f"The numerical value is unchanged.",
            "tier_3": f"{ml} ml.",
        },
        "misconception_tags": ["dividing_by_10_or_1000_unnecessarily"],
    }


# ----------------------------------------------------------------------
# 31. Capacity: Convert Cubic cm to Litres
# ----------------------------------------------------------------------
def arch_31_convert_cubic_cm_to_litres(rng: random.Random) -> Dict[str, Any]:
    cm3 = rng.choice([2000, 3500, 4800, 6000, 12500])
    litres = cm3 / 1000.0
    litres_str = _fmt_dec(litres, 2)

    prompt = (
        f"A rectangular juice container has an internal volume of \\({cm3}\\text{{ cm}}^3\\).\n\n"
        f"Convert this capacity into litres (\\(\\text{{L}}\\)), knowing that \\(1\\,000\\text{{ cm}}^3 = 1\\text{{ litre}}\\)."
    )
    sol = (
        f"**Conversion to Litres:**\n"
        f"\\[ \\text{{Capacity in Litres}} = \\frac{{{cm3}}}{{1\\,000}} = {litres_str}\\text{{ litres}} \\]"
    )
    ans = f"{litres_str} litres"
    return {
        "id": f"g8_meas_cm3_l_{rng.randint(100000, 999999)}",
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
        "subskill": "31_convert_cubic_cm_to_litres",
        "learning_objective_id": "math_g8_meas_cm3_l",
        "hints": {
            "tier_1": "Divide by 1 000 to convert cm³ to litres.",
            "tier_2": f"{cm3} / 1 000.",
            "tier_3": f"{litres_str} litres.",
        },
        "misconception_tags": ["multiplying_instead_of_dividing_by_1000"],
    }


# ----------------------------------------------------------------------
# 32. Capacity: Convert Litres to Cubic cm
# ----------------------------------------------------------------------
def arch_32_convert_litres_to_cubic_cm(rng: random.Random) -> Dict[str, Any]:
    litres = rng.choice([1.5, 2.0, 3.25, 4.5, 5.0])
    cm3 = int(litres * 1000)
    litres_str = _fmt_dec(litres, 2)

    prompt = (
        f"A bottle contains \\({litres_str}\\text{{ litres}}\\) of cooking oil.\n\n"
        f"Calculate the equivalent volume in cubic centimetres (\\(\\text{{cm}}^3\\))."
    )
    sol = (
        f"**Conversion from Litres to cm³:**\n"
        f"Since \\(1\\text{{ litre}} = 1\\,000\\text{{ cm}}^3\\), multiply by \\(1\\,000\\):\n"
        f"\\[ {litres_str} \\times 1\\,000 = {cm3}\\text{{ cm}}^3 \\]"
    )
    ans = f"{cm3} cm³"
    return {
        "id": f"g8_meas_l_cm3_{rng.randint(100000, 999999)}",
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
        "subskill": "32_convert_litres_to_cubic_cm",
        "learning_objective_id": "math_g8_meas_l_cm3",
        "hints": {
            "tier_1": "Multiply litres by 1 000 to get cm³.",
            "tier_2": f"{litres_str} × 1 000.",
            "tier_3": f"{cm3} cm³.",
        },
        "misconception_tags": ["dividing_by_1000"],
    }


# ----------------------------------------------------------------------
# 33. Capacity: Convert Cubic Metres to Kilolitres
# ----------------------------------------------------------------------
def arch_33_convert_cubic_m_to_kilolitres(rng: random.Random) -> Dict[str, Any]:
    m3 = rng.choice([4, 8, 12, 25, 60])
    kl = m3

    prompt = (
        f"A municipal water reservoir has an internal volume of \\({m3}\\text{{ m}}^3\\).\n\n"
        f"1. State the capacity of the reservoir in kilolitres (\\(\\text{{kl}}\\)).\n"
        f"2. Explain the conversion equivalence between \\(\\text{{m}}^3\\) and \\(\\text{{kl}}\\)."
    )
    sol = (
        f"**Equivalence Between m³ and kl:**\n"
        f"1. \\(1\\text{{ m}}^3 = 1\\,000\\text{{ litres}} = 1\\text{{ kl}}\\).\n"
        f"2. Therefore, the numerical value is identical:\n"
        f"\\[ {m3}\\text{{ m}}^3 = {kl}\\text{{ kl}} \\]"
    )
    ans = f"1. {kl} kl; 2. 1 m³ = 1 000 litres = 1 kl"
    return {
        "id": f"g8_meas_m3_kl_{rng.randint(100000, 999999)}",
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
        "subskill": "33_convert_cubic_m_to_kilolitres",
        "learning_objective_id": "math_g8_meas_m3_kl",
        "hints": {
            "tier_1": "1 cubic metre holds exactly 1 kilolitre (1 m³ = 1 kl).",
            "tier_2": f"The capacity is {m3} kl.",
            "tier_3": f"{kl} kl.",
        },
        "misconception_tags": ["multiplying_by_1000_unnecessarily"],
    }


# ----------------------------------------------------------------------
# 34. Capacity: Convert Kilolitres to Litres
# ----------------------------------------------------------------------
def arch_34_convert_kilolitres_to_litres(rng: random.Random) -> Dict[str, Any]:
    kl = rng.choice([3, 5, 8.5, 12, 16.5])
    litres = int(kl * 1000)
    kl_str = _fmt_dec(kl, 1)

    prompt = (
        f"A rainwater tank holds \\({kl_str}\\text{{ kl}}\\) of water.\n\n"
        f"Convert this capacity into litres."
    )
    sol = (
        f"**Conversion from kl to Litres:**\n"
        f"The prefix 'kilo' means 1 000:\n"
        f"\\[ 1\\text{{ kl}} = 1\\,000\\text{{ litres}} \\]\n"
        f"\\[ {kl_str} \\times 1\\,000 = {litres:,}\\text{{ litres}} \\]".replace(",", " ")
    )
    ans = f"{litres:,} litres".replace(",", " ")
    return {
        "id": f"g8_meas_kl_l_{rng.randint(100000, 999999)}",
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
        "subskill": "34_convert_kilolitres_to_litres",
        "learning_objective_id": "math_g8_meas_kl_l",
        "hints": {
            "tier_1": "Multiply kilolitres by 1 000 to get litres.",
            "tier_2": f"{kl_str} × 1 000.",
            "tier_3": f"{litres} litres.",
        },
        "misconception_tags": ["dividing_by_1000"],
    }


# ----------------------------------------------------------------------
# 35. Application: Fish Tank Capacity in Litres (WITH SVG)
# ----------------------------------------------------------------------
def arch_35_capacity_fish_tank_volume_in_litres(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([50, 60, 80])
    b = rng.choice([30, 40])
    h = 40
    water_h = rng.choice([25, 30, 35])

    water_cm3 = l * b * water_h
    litres = water_cm3 / 1000.0
    litres_str = _fmt_dec(litres, 1)
    svg = draw_tank_water_svg(l, b, h, water_h, seed=rng.randint(100, 999999))

    prompt = (
        f"A glass aquarium has internal length \\({l}\\text{{ cm}}\\) and breadth \\({b}\\text{{ cm}}\\). "
        f"It is filled with water to a depth of \\({water_h}\\text{{ cm}}\\).\n\n"
        f"1. Calculate the volume of water in \\(\\text{{cm}}^3\\).\n"
        f"2. Determine the volume of water in litres."
    )
    sol = (
        f"**Calculation of Water Volume & Capacity:**\n"
        f"1. Volume of water: \\(V = l \\times b \\times \\text{{depth}}\\)\n"
        f"\\[ V = {l} \\times {b} \\times {water_h} = {water_cm3:,}\\text{{ cm}}^3 \\]\n"
        f"2. Capacity in litres:\n"
        f"\\[ \\text{{Litres}} = \\frac{{{water_cm3}}}{{1\\,000}} = {litres_str}\\text{{ litres}} \\]".replace(",", " ")
    )
    ans = f"1. {water_cm3:,} cm³; 2. {litres_str} litres".replace(",", " ")
    return {
        "id": f"g8_meas_tank_{rng.randint(100000, 999999)}",
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
        "subskill": "35_capacity_fish_tank_volume_in_litres",
        "learning_objective_id": "math_g8_meas_tank",
        "hints": {
            "tier_1": f"Use water depth ({water_h} cm), not the full tank height.",
            "tier_2": f"Volume = {l} × {b} × {water_h} = {water_cm3} cm³.",
            "tier_3": f"Litres = {water_cm3} / 1 000 = {litres_str} litres.",
        },
        "misconception_tags": ["using_total_tank_height_instead_of_water_depth"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 36. Application: Swimming Pool Volume & Capacity in kl (WITH SVG)
# ----------------------------------------------------------------------
def arch_36_capacity_swimming_pool_volume_in_kilolitres(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([8, 10, 12])
    b = rng.choice([4, 5, 6])
    h = 2
    vol_m3 = l * b * h
    kl = vol_m3
    svg = draw_rectangular_prism_3d_svg(l, b, h, unit="m", seed=rng.randint(100, 999999))

    prompt = (
        f"A community swimming pool has a rectangular prism shape of length \\({l}\\text{{ m}}\\), "
        f"breadth \\({b}\\text{{ m}}\\), and uniform depth \\({h}\\text{{ m}}\\).\n\n"
        f"1. Calculate the volume of the pool in \\(\\text{{m}}^3\\).\n"
        f"2. Determine the capacity of the pool in kilolitres (\\(\\text{{kl}}\\)).\n"
        f"3. How many litres of water are needed to fill the pool completely?"
    )
    sol = (
        f"**Pool Calculations:**\n"
        f"1. Volume: \\(V = l \\times b \\times h = {l} \\times {b} \\times {h} = {vol_m3}\\text{{ m}}^3\\)\n"
        f"2. Capacity in kl: Since \\(1\\text{{ m}}^3 = 1\\text{{ kl}}\\), the capacity is \\({kl}\\text{{ kl}}\\).\n"
        f"3. Capacity in litres: \\({kl} \\times 1\\,000 = {kl*1000:,}\\text{{ litres}}\\).".replace(",", " ")
    )
    ans = f"1. {vol_m3} m³; 2. {kl} kl; 3. {kl*1000:,} litres".replace(",", " ")
    return {
        "id": f"g8_meas_pool_{rng.randint(100000, 999999)}",
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
        "subskill": "36_capacity_swimming_pool_volume_in_kilolitres",
        "learning_objective_id": "math_g8_meas_pool",
        "hints": {
            "tier_1": f"Volume = {l} × {b} × {h} = {vol_m3} m³.",
            "tier_2": "1 m³ = 1 kl = 1 000 litres.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_litres_and_kilolitres_scale"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 37. Application: Internal vs External Dimensions Wall Thickness (WITH SVG)
# ----------------------------------------------------------------------
def arch_37_internal_vs_external_dimensions_wall_thickness(rng: random.Random) -> Dict[str, Any]:
    ext_l = 30
    ext_b = 20
    ext_h = 10
    t = rng.choice([1, 2])

    int_l = ext_l - 2 * t
    int_b = ext_b - 2 * t
    int_h = ext_h - t  # open top box, bottom only

    ext_vol = ext_l * ext_b * ext_h
    int_vol = int_l * int_b * int_h
    svg = draw_rectangular_prism_3d_svg(ext_l, ext_b, ext_h, unit="cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A solid wooden storage box has exterior dimensions of \\({ext_l}\\text{{ cm}} \\times {ext_b}\\text{{ cm}} \\times {ext_h}\\text{{ cm}}\\). "
        f"The wooden sides and base are each \\({t}\\text{{ cm}}\\) thick, and the box has no lid.\n\n"
        f"1. Determine the internal length, breadth, and depth of the box.\n"
        f"2. Calculate the interior holding capacity in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Step-by-Step Internal Measurement Analysis:**\n"
        f"1. Accounting for wall thickness:\n"
        f"- Length has two side walls: \\(\\text{{Internal Length}} = {ext_l} - 2({t}) = {int_l}\\text{{ cm}}\\)\n"
        f"- Breadth has two side walls: \\(\\text{{Internal Breadth}} = {ext_b} - 2({t}) = {int_b}\\text{{ cm}}\\)\n"
        f"- Height has only one bottom base (open top): \\(\\text{{Internal Depth}} = {ext_h} - {t} = {int_h}\\text{{ cm}}\\)\n\n"
        f"2. Interior Holding Capacity:\n"
        f"\\[ V = {int_l} \\times {int_b} \\times {int_h} = {int_vol:,}\\text{{ cm}}^3 \\]".replace(",", " ")
    )
    ans = f"1. {int_l} cm × {int_b} cm × {int_h} cm; 2. {int_vol:,} cm³".replace(",", " ")
    return {
        "id": f"g8_meas_thick_{rng.randint(100000, 999999)}",
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
        "subskill": "37_internal_vs_external_dimensions_wall_thickness",
        "learning_objective_id": "math_g8_meas_thick",
        "hints": {
            "tier_1": f"Subtract 2 × {t} for length and breadth, but only 1 × {t} for depth (no lid).",
            "tier_2": f"Inside dims: {int_l} × {int_b} × {int_h}.",
            "tier_3": f"{int_vol} cm³.",
        },
        "misconception_tags": ["subtracting_thickness_only_once_from_length_and_breadth"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 38. Application: Hollow Container Holding Capacity with Wall Thickness
# ----------------------------------------------------------------------
def arch_38_hollow_container_capacity_given_wall_thickness(rng: random.Random) -> Dict[str, Any]:
    l_ext = 40
    b_ext = 30
    h_ext = 20
    t = 1

    l_int = l_ext - 2 * t
    b_int = b_ext - 2 * t
    h_int = h_ext - 2 * t  # closed box

    int_vol = l_int * b_int * h_int
    litres = int_vol / 1000.0
    litres_str = _fmt_dec(litres, 2)

    prompt = (
        f"A closed cooler box has external measurements \\({l_ext}\\text{{ cm}} \\times {b_ext}\\text{{ cm}} \\times {h_ext}\\text{{ cm}}\\). "
        f"All walls, top lid, and base are \\({t}\\text{{ cm}}\\) thick.\n\n"
        f"Calculate the internal capacity of the cooler box in litres."
    )
    sol = (
        f"**Calculation of Closed Cooler Box Capacity:**\n"
        f"1. Internal dimensions:\n"
        f"- Length: \\({l_ext} - 2 = {l_int}\\text{{ cm}}\\)\n"
        f"- Breadth: \\({b_ext} - 2 = {b_int}\\text{{ cm}}\\)\n"
        f"- Height: \\({h_ext} - 2 = {h_int}\\text{{ cm}}\\)\n\n"
        f"2. Internal volume: \\({l_int} \\times {b_int} \\times {h_int} = {int_vol}\\text{{ cm}}^3\\)\n"
        f"3. Capacity in litres: \\(\\frac{{{int_vol}}}{{1\\,000}} = {litres_str}\\text{{ litres}}\\)"
    )
    ans = f"{litres_str} litres"
    return {
        "id": f"g8_meas_closed_thick_{rng.randint(100000, 999999)}",
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
        "subskill": "38_hollow_container_capacity_given_wall_thickness",
        "learning_objective_id": "math_g8_meas_closed_thick",
        "hints": {
            "tier_1": "Subtract 2 cm from all 3 dimensions because the cooler is closed.",
            "tier_2": f"Inside: {l_int} × {b_int} × {h_int} = {int_vol} cm³.",
            "tier_3": f"{litres_str} litres.",
        },
        "misconception_tags": ["subtracting_thickness_twice_from_open_box_or_once_from_closed_box"],
    }


# ----------------------------------------------------------------------
# 39. Displacement: Water Displacement Volume by Submerged Solid
# ----------------------------------------------------------------------
def arch_39_water_displacement_by_submerged_solid_object(rng: random.Random) -> Dict[str, Any]:
    init_vol = rng.choice([250, 300, 400])
    solid_vol = rng.choice([35, 50, 75, 120])
    final_vol = init_vol + solid_vol

    prompt = (
        f"A measuring cylinder initially contains \\({init_vol}\\text{{ ml}}\\) of water. "
        f"An irregularly shaped metal stone is gently lowered until completely submerged in the water. "
        f"The water level rises to \\({final_vol}\\text{{ ml}}\\).\n\n"
        f"1. Explain the scientific principle of water displacement.\n"
        f"2. Calculate the volume of the metal stone in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**1. Principle of Displacement:**\n"
        f"An insoluble submerged solid displaces a volume of water equal to the volume of the solid itself.\n\n"
        f"**2. Volume Calculation:**\n"
        f"\\[ \\text{{Volume of stone}} = \\text{{Final level}} - \\text{{Initial level}} \\]\n"
        f"\\[ = {final_vol} - {init_vol} = {solid_vol}\\text{{ ml}} \\]\n"
        f"Since \\(1\\text{{ ml}} = 1\\text{{ cm}}^3\\):\n"
        f"\\[ \\text{{Volume}} = {solid_vol}\\text{{ cm}}^3 \\]"
    )
    ans = f"1. Submerged object pushes aside water equal to its own volume; 2. {solid_vol} cm³"
    return {
        "id": f"g8_meas_disp_stone_{rng.randint(100000, 999999)}",
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
        "subskill": "39_water_displacement_by_submerged_solid_object",
        "learning_objective_id": "math_g8_meas_disp_stone",
        "hints": {
            "tier_1": f"Subtract initial level ({init_vol} ml) from final level ({final_vol} ml).",
            "tier_2": f"{final_vol} - {init_vol} = {solid_vol} ml.",
            "tier_3": f"{solid_vol} cm³.",
        },
        "misconception_tags": ["confusing_millilitres_with_cubic_millimetres"],
    }


# ----------------------------------------------------------------------
# 40. Displacement: Water Level Rise in Rectangular Container
# ----------------------------------------------------------------------
def arch_40_water_level_rise_in_rectangular_container_from_added_object(rng: random.Random) -> Dict[str, Any]:
    l = 20
    b = 10
    base_area = l * b  # 200 cm²
    rise = rng.choice([2, 3, 4])
    obj_vol = base_area * rise

    prompt = (
        f"A rectangular tank with base \\({l}\\text{{ cm}} \\times {b}\\text{{ cm}}\\) contains water. "
        f"When a dense block is submerged in the tank, the water level rises by \\({rise}\\text{{ cm}}\\) "
        f"without overflowing.\n\n"
        f"Calculate the volume of the submerged block in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Calculation of Displaced Volume:**\n"
        f"The volume of the block equals the volume of the water column raised:\n"
        f"\\[ V = \\text{{Base Area of Tank}} \\times \\text{{Rise in Water Level}} \\]\n"
        f"\\[ = ({l} \\times {b}) \\times {rise} = {base_area} \\times {rise} = {obj_vol}\\text{{ cm}}^3 \\]"
    )
    ans = f"{obj_vol} cm³"
    return {
        "id": f"g8_meas_rise_{rng.randint(100000, 999999)}",
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
        "subskill": "40_water_level_rise_in_rectangular_container_from_added_object",
        "learning_objective_id": "math_g8_meas_rise",
        "hints": {
            "tier_1": f"Base area of tank = {l} × {b} = {base_area} cm².",
            "tier_2": f"Volume = Base Area × water rise = {base_area} × {rise}.",
            "tier_3": f"{obj_vol} cm³.",
        },
        "misconception_tags": ["using_total_height_of_tank_instead_of_rise"],
    }


# ----------------------------------------------------------------------
# 41. Scaling: Doubling Edge of Cube Increases Surface Area Fourfold
# ----------------------------------------------------------------------
def arch_41_doubling_side_of_cube_effect_on_surface_area_fourfold(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4, 5])
    s2 = 2 * s
    sa1 = 6 * s * s
    sa2 = 6 * s2 * s2

    prompt = (
        f"A cube has side length \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"1. Calculate the total surface area of this cube.\n"
        f"2. If every side length is doubled to \\({s2}\\text{{ cm}}\\), calculate the new total surface area.\n"
        f"3. State by what factor the surface area increased and explain why."
    )
    sol = (
        f"**1. Original Surface Area:** \\(6 \\times ({s})^2 = 6 \\times {s*s} = {sa1}\\text{{ cm}}^2\\)\n\n"
        f"**2. Doubled Surface Area:** \\(6 \\times ({s2})^2 = 6 \\times {s2*s2} = {sa2}\\text{{ cm}}^2\\)\n\n"
        f"**3. Factor of Increase:**\n"
        f"\\[ \\frac{{{sa2}}}{{{sa1}}} = \\frac{{6 \\times (2s)^2}}{{6s^2}} = 2^2 = 4 \\]\n"
        f"The surface area increases by a factor of **4** (quadruples) because area depends on the square of linear dimensions."
    )
    ans = f"1. {sa1} cm²; 2. {sa2} cm²; 3. Factor of 4 (2²)"
    return {
        "id": f"g8_meas_scale_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "41_doubling_side_of_cube_effect_on_surface_area_fourfold",
        "learning_objective_id": "math_g8_meas_scale_sa",
        "hints": {
            "tier_1": f"Original: 6 × {s}² = {sa1}. Doubled: 6 × {s2}² = {sa2}.",
            "tier_2": f"{sa2} / {sa1} = 4.",
            "tier_3": "Factor of 4.",
        },
        "misconception_tags": ["assuming_surface_area_doubles_when_dimensions_double"],
    }


# ----------------------------------------------------------------------
# 42. Scaling: Doubling Edge of Cube Increases Volume Eightfold
# ----------------------------------------------------------------------
def arch_42_doubling_side_of_cube_effect_on_volume_eightfold(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([2, 3, 4])
    s2 = 2 * s
    v1 = s ** 3
    v2 = s2 ** 3

    prompt = (
        f"A cube has side length \\(s = {s}\\text{{ cm}}\\).\n\n"
        f"1. Calculate the original volume \\(V_1\\).\n"
        f"2. Calculate the new volume \\(V_2\\) when the side length is doubled to \\({s2}\\text{{ cm}}\\).\n"
        f"3. By what factor has the volume increased?"
    )
    sol = (
        f"**1. Original Volume:** \\(V_1 = {s}^3 = {v1}\\text{{ cm}}^3\\)\n\n"
        f"**2. Doubled Volume:** \\(V_2 = ({s2})^3 = {v2}\\text{{ cm}}^3\\)\n\n"
        f"**3. Factor of Increase:**\n"
        f"\\[ \\frac{{V_2}}{{V_1}} = \\frac{{(2s)^3}}{{s^3}} = 2^3 = 8 \\]\n"
        f"The volume increases by a factor of **8** (eightfold) because volume scales with the cube of linear dimensions."
    )
    ans = f"1. {v1} cm³; 2. {v2} cm³; 3. Factor of 8 (2³)"
    return {
        "id": f"g8_meas_scale_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "42_doubling_side_of_cube_effect_on_volume_eightfold",
        "learning_objective_id": "math_g8_meas_scale_vol",
        "hints": {
            "tier_1": f"Original: {s}³ = {v1}. Doubled: {s2}³ = {v2}.",
            "tier_2": f"{v2} / {v1} = 8.",
            "tier_3": "Factor of 8.",
        },
        "misconception_tags": ["assuming_volume_doubles_when_dimensions_double"],
    }


# ----------------------------------------------------------------------
# 43. Scaling: Tripling Dimensions of Rectangular Prism
# ----------------------------------------------------------------------
def arch_43_tripling_dimensions_of_rectangular_prism_effect_on_volume(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([2, 3])
    b = 2
    h = 4
    v1 = l * b * h
    v2 = (3 * l) * (3 * b) * (3 * h)

    prompt = (
        f"A rectangular shipping container has dimensions \\({l}\\text{{ m}} \\times {b}\\text{{ m}} \\times {h}\\text{{ m}}\\).\n\n"
        f"If the length, breadth, and height are all tripled (multiplied by 3), "
        f"determine the new volume and the factor by which the volume has increased."
    )
    sol = (
        f"**Analysis of Tripled Dimensions:**\n"
        f"1. Original volume: \\(V_1 = {l} \\times {b} \\times {h} = {v1}\\text{{ m}}^3\\)\n"
        f"2. New dimensions: \\({3*l}\\text{{ m}} \\times {3*b}\\text{{ m}} \\times {3*h}\\text{{ m}}\\)\n"
        f"3. New volume: \\(V_2 = {3*l} \\times {3*b} \\times {3*h} = {v2}\\text{{ m}}^3\\)\n"
        f"4. Ratio: \\(\\frac{{{v2}}}{{{v1}}} = 3^3 = 27\\).\n"
        f"The volume increases by a factor of **27**."
    )
    ans = f"New volume = {v2} m³, factor of increase = 27 (3³)"
    return {
        "id": f"g8_meas_triple_{rng.randint(100000, 999999)}",
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
        "subskill": "43_tripling_dimensions_of_rectangular_prism_effect_on_volume",
        "learning_objective_id": "math_g8_meas_triple",
        "hints": {
            "tier_1": "When all 3 dimensions are scaled by k, the volume is scaled by k³.",
            "tier_2": f"3³ = 27.",
            "tier_3": f"{v2} m³, factor 27.",
        },
        "misconception_tags": ["multiplying_by_3_instead_of_27"],
    }


# ----------------------------------------------------------------------
# 44. Synthesis: Same Volume Different Surface Areas
# ----------------------------------------------------------------------
def arch_44_same_volume_different_surface_areas_comparison_table(rng: random.Random) -> Dict[str, Any]:
    vol = 24
    # Prism A: 12 x 2 x 1 -> V=24, SA = 2(24 + 12 + 2) = 76
    sa_a = 2 * (12 * 2 + 12 * 1 + 2 * 1)
    # Prism B: 4 x 3 x 2 -> V=24, SA = 2(12 + 8 + 6) = 52
    sa_b = 2 * (4 * 3 + 4 * 2 + 3 * 2)

    prompt = (
        f"Consider two different rectangular prisms, both having a volume of exactly \\(24\\text{{ m}}^3\\):\n"
        f"- **Prism A:** dimensions \\(12\\text{{ m}} \\times 2\\text{{ m}} \\times 1\\text{{ m}}\\)\n"
        f"- **Prism B:** dimensions \\(4\\text{{ m}} \\times 3\\text{{ m}} \\times 2\\text{{ m}}\\)\n\n"
        f"1. Calculate the total surface area of Prism A.\n"
        f"2. Calculate the total surface area of Prism B.\n"
        f"3. What important mathematical principle does this demonstrate regarding surface area and volume?"
    )
    sol = (
        f"**1. Surface Area of Prism A:**\n"
        f"\\[ SA_A = 2(12 \\times 2 + 12 \\times 1 + 2 \\times 1) = 2(24 + 12 + 2) = {sa_a}\\text{{ m}}^2 \\]\n\n"
        f"**2. Surface Area of Prism B:**\n"
        f"\\[ SA_B = 2(4 \\times 3 + 4 \\times 2 + 3 \\times 2) = 2(12 + 8 + 6) = {sa_b}\\text{{ m}}^2 \\]\n\n"
        f"**3. Mathematical Principle:**\n"
        f"3D objects having the identical volume do NOT necessarily have the same surface area. "
        f"Longer, flatter shapes have greater surface area than more compact (cubical) shapes of equal volume."
    )
    ans = f"1. SA_A = {sa_a} m²; 2. SA_B = {sa_b} m²; 3. Objects with identical volume can have different surface areas"
    return {
        "id": f"g8_meas_same_v_{rng.randint(100000, 999999)}",
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
        "subskill": "44_same_volume_different_surface_areas_comparison_table",
        "learning_objective_id": "math_g8_meas_same_v",
        "hints": {
            "tier_1": f"Calculate SA for Prism A ({sa_a} m²) and Prism B ({sa_b} m²).",
            "tier_2": "Notice that Prism B is more compact and has less surface area.",
            "tier_3": ans,
        },
        "misconception_tags": ["believing_equal_volume_guarantees_equal_surface_area"],
    }


# ----------------------------------------------------------------------
# 45. Composite 3D: Volume of Cube Glued to Rectangular Prism (WITH SVG)
# ----------------------------------------------------------------------
def arch_45_composite_object_cube_glued_to_rectangular_prism_volume(rng: random.Random) -> Dict[str, Any]:
    base_l = rng.choice([10, 12, 14])
    base_b = rng.choice([6, 8])
    base_h = rng.choice([4, 5])
    cube_s = rng.choice([3, 4])

    v_base = base_l * base_b * base_h
    v_cube = cube_s ** 3
    v_total = v_base + v_cube
    svg = draw_composite_prism_svg(base_l, base_b, base_h, cube_s, seed=rng.randint(100, 999999))

    prompt = (
        f"A composite sculpture consists of a solid wooden cube of edge \\(s = {cube_s}\\text{{ cm}}\\) "
        f"glued firmly on top of a larger rectangular prism of dimensions \\({base_l}\\text{{ cm}} \\times {base_b}\\text{{ cm}} \\times {base_h}\\text{{ cm}}\\).\n\n"
        f"Calculate the total volume of the composite object in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Calculation of Composite Volume:**\n"
        f"1. Volume of rectangular prism base: \\(V_1 = {base_l} \\times {base_b} \\times {base_h} = {v_base}\\text{{ cm}}^3\\)\n"
        f"2. Volume of top cube: \\(V_2 = {cube_s}^3 = {v_cube}\\text{{ cm}}^3\\)\n"
        f"3. Total Volume: \\(V = V_1 + V_2 = {v_base} + {v_cube} = {v_total}\\text{{ cm}}^3\\)"
    )
    ans = f"{v_total} cm³"
    return {
        "id": f"g8_meas_comp_vol_{rng.randint(100000, 999999)}",
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
        "subskill": "45_composite_object_cube_glued_to_rectangular_prism_volume",
        "learning_objective_id": "math_g8_meas_comp_vol",
        "hints": {
            "tier_1": f"Base volume = {v_base} cm³; Cube volume = {cube_s}³ = {v_cube} cm³.",
            "tier_2": f"Add the two volumes: {v_base} + {v_cube}.",
            "tier_3": f"{v_total} cm³.",
        },
        "misconception_tags": ["subtracting_the_glued_face_from_volume"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 46. Composite 3D: Surface Area Cube Glued on Rectangular Prism (WITH SVG)
# ----------------------------------------------------------------------
def arch_46_composite_object_cube_glued_to_rectangular_prism_surface_area(rng: random.Random) -> Dict[str, Any]:
    base_l = 10
    base_b = 6
    base_h = 4
    cube_s = 3

    sa_base = 2 * (base_l * base_b + base_l * base_h + base_b * base_h)  # 2(60 + 40 + 24) = 248
    sa_cube = 6 * cube_s * cube_s  # 6 * 9 = 54
    contact_area = cube_s * cube_s  # 9
    # Total SA = SA_base + SA_cube - 2 * contact_area
    total_sa = sa_base + sa_cube - 2 * contact_area  # 248 + 54 - 18 = 284
    svg = draw_composite_prism_svg(base_l, base_b, base_h, cube_s, seed=rng.randint(100, 999999))

    prompt = (
        f"A cube of edge \\({cube_s}\\text{{ cm}}\\) is glued squarely onto the top face of a rectangular block "
        f"measuring \\({base_l}\\text{{ cm}} \\times {base_b}\\text{{ cm}} \\times {base_h}\\text{{ cm}}\\).\n\n"
        f"Calculate the total exposed surface area of the combined solid in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Calculation of Composite Surface Area:**\n"
        f"When two solids are glued together, the contact face is hidden on BOTH solids, so subtract \\(2 \\times \\text{{contact area}}\\) from the sum of their individual surface areas:\n\n"
        f"1. Separate Surface Area of base block: \\(2(10 \\times 6 + 10 \\times 4 + 6 \\times 4) = 2(60 + 40 + 24) = {sa_base}\\text{{ cm}}^2\\)\n"
        f"2. Separate Surface Area of cube: \\(6 \\times {cube_s}^2 = 6 \\times {contact_area} = {sa_cube}\\text{{ cm}}^2\\)\n"
        f"3. Contact face area: \\({cube_s} \\times {cube_s} = {contact_area}\\text{{ cm}}^2\\)\n"
        f"4. Total Exposed Surface Area:\n"
        f"\\[ SA = {sa_base} + {sa_cube} - 2({contact_area}) = {sa_base + sa_cube} - {2*contact_area} = {total_sa}\\text{{ cm}}^2 \\]"
    )
    ans = f"{total_sa} cm²"
    return {
        "id": f"g8_meas_comp_sa_{rng.randint(100000, 999999)}",
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
        "subskill": "46_composite_object_cube_glued_to_rectangular_prism_surface_area",
        "learning_objective_id": "math_g8_meas_comp_sa",
        "hints": {
            "tier_1": f"Sum of separate surface areas: {sa_base} + {sa_cube} = {sa_base + sa_cube}.",
            "tier_2": f"Subtract 2 × contact area (2 × {contact_area} = {2*contact_area}).",
            "tier_3": f"{total_sa} cm².",
        },
        "misconception_tags": ["subtracting_contact_area_only_once_instead_of_twice"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Composite 3D: Volume of L-Shaped Prism
# ----------------------------------------------------------------------
def arch_47_composite_object_l_shaped_prism_volume(rng: random.Random) -> Dict[str, Any]:
    l1 = rng.choice([6, 8])
    b = 4
    h1 = 6

    l2 = 4
    h2 = 2

    # Block 1: l1 x b x h1
    v1 = l1 * b * h1
    # Block 2: l2 x b x h2
    v2 = l2 * b * h2
    v_total = v1 + v2

    prompt = (
        f"An L-shaped concrete step can be decomposed into two joined rectangular blocks sharing breadth \\({b}\\text{{ m}}\\):\n"
        f"- Main standing block: length \\({l1}\\text{{ m}}\\), breadth \\({b}\\text{{ m}}\\), height \\({h1}\\text{{ m}}\\)\n"
        f"- Extended foot block: length \\({l2}\\text{{ m}}\\), breadth \\({b}\\text{{ m}}\\), height \\({h2}\\text{{ m}}\\)\n\n"
        f"Calculate the total volume of concrete needed for the step in \\(\\text{{m}}^3\\)."
    )
    sol = (
        f"**Volume by Decomposition:**\n"
        f"1. Volume of main block: \\(V_1 = {l1} \\times {b} \\times {h1} = {v1}\\text{{ m}}^3\\)\n"
        f"2. Volume of foot block: \\(V_2 = {l2} \\times {b} \\times {h2} = {v2}\\text{{ m}}^3\\)\n"
        f"3. Total Volume: \\(V_1 + V_2 = {v1} + {v2} = {v_total}\\text{{ m}}^3\\)"
    )
    ans = f"{v_total} m³"
    return {
        "id": f"g8_meas_l_prism_{rng.randint(100000, 999999)}",
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
        "subskill": "47_composite_object_l_shaped_prism_volume",
        "learning_objective_id": "math_g8_meas_l_prism",
        "hints": {
            "tier_1": f"Split into 2 blocks: {l1}×{b}×{h1} and {l2}×{b}×{h2}.",
            "tier_2": f"{v1} + {v2}.",
            "tier_3": f"{v_total} m³.",
        },
        "misconception_tags": ["multiplying_composite_dimensions_directly"],
    }


# ----------------------------------------------------------------------
# 48. Context: Paint Coverage for Room Walls and Ceiling
# ----------------------------------------------------------------------
def arch_48_cost_of_painting_walls_and_ceiling_of_room_surface_area(rng: random.Random) -> Dict[str, Any]:
    l = 6
    b = 4
    h = 3
    # 4 walls: 2(lh + bh) = 2(18 + 12) = 60 m²
    walls_area = 2 * (l * h + b * h)
    # Ceiling: lb = 24 m²
    ceiling_area = l * b
    total_area = walls_area + ceiling_area  # 84 m²

    door_window = rng.choice([4, 6, 8])
    paint_area = total_area - door_window
    coverage = 10  # m² per litre
    litres_needed = math.ceil(paint_area / coverage)

    prompt = (
        f"A classroom has length \\({l}\\text{{ m}}\\), breadth \\({b}\\text{{ m}}\\), and height \\({h}\\text{{ m}}\\). "
        f"A painter paints the four walls and the ceiling, but NOT the floor. "
        f"The door and windows account for \\({door_window}\\text{{ m}}^2\\) that will not be painted.\n\n"
        f"1. Calculate the total wall area.\n"
        f"2. Calculate the ceiling area.\n"
        f"3. Calculate the actual area of surface to be painted.\n"
        f"4. If 1 litre of paint covers \\({coverage}\\text{{ m}}^2\\), how many 1-litre tins must be purchased?"
    )
    sol = (
        f"**1. Walls Area:** \\(2(lh + bh) = 2({l}\\times{h} + {b}\\times{h}) = 2({l*h} + {b*h}) = {walls_area}\\text{{ m}}^2\\)\n"
        f"**2. Ceiling Area:** \\(l \\times b = {l} \\times {b} = {ceiling_area}\\text{{ m}}^2\\)\n"
        f"**3. Net Area:** \\(({walls_area} + {ceiling_area}) - {door_window} = {total_area} - {door_window} = {paint_area}\\text{{ m}}^2\\)\n"
        f"**4. Paint Tins:** \\(\\frac{{{paint_area}}}{{{coverage}}} = {_fmt_dec(paint_area/coverage, 1)}\\) tins \\(\\implies {litres_needed}\\) whole tins (rounded up)."
    )
    ans = f"1. {walls_area} m²; 2. {ceiling_area} m²; 3. {paint_area} m²; 4. {litres_needed} tins"
    return {
        "id": f"g8_meas_paint_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "subskill": "48_cost_of_painting_walls_and_ceiling_of_room_surface_area",
        "learning_objective_id": "math_g8_meas_paint",
        "hints": {
            "tier_1": f"Walls: {walls_area} m²; Ceiling: {ceiling_area} m².",
            "tier_2": f"Subtract {door_window} m² for door/windows: {paint_area} m².",
            "tier_3": f"{paint_area} / {coverage} = {paint_area/coverage} -> {litres_needed} tins.",
        },
        "misconception_tags": ["including_the_floor_area_in_painting_calculations"],
    }


# ----------------------------------------------------------------------
# 49. Packaging: Maximum Number of Small Cubes in Large Box
# ----------------------------------------------------------------------
def arch_49_packaging_number_of_small_cubes_fitting_into_large_box(rng: random.Random) -> Dict[str, Any]:
    cube_s = 5  # cm
    carton_l = rng.choice([30, 40, 50])
    carton_b = rng.choice([20, 30])
    carton_h = rng.choice([15, 20])

    fit_l = carton_l // cube_s
    fit_b = carton_b // cube_s
    fit_h = carton_h // cube_s
    total_cubes = fit_l * fit_b * fit_h

    prompt = (
        f"A factory packs small cubic gift boxes with edges of \\({cube_s}\\text{{ cm}}\\) into a large shipping carton "
        f"measuring \\({carton_l}\\text{{ cm}} \\times {carton_b}\\text{{ cm}} \\times {carton_h}\\text{{ cm}}\\).\n\n"
        f"Calculate the maximum number of gift boxes that can fit neatly inside the shipping carton without empty fractional spaces."
    )
    sol = (
        f"**Calculation by Layer Dimensions:**\n"
        f"- Number along length: \\({carton_l} \\div {cube_s} = {fit_l}\\)\n"
        f"- Number along breadth: \\({carton_b} \\div {cube_s} = {fit_b}\\)\n"
        f"- Number along height: \\({carton_h} \\div {cube_s} = {fit_h}\\)\n\n"
        f"Total capacity: \\({fit_l} \\times {fit_b} \\times {fit_h} = {total_cubes}\\) boxes."
    )
    ans = f"{total_cubes} boxes"
    return {
        "id": f"g8_meas_pack_{rng.randint(100000, 999999)}",
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
        "subskill": "49_packaging_number_of_small_cubes_fitting_into_large_box",
        "learning_objective_id": "math_g8_meas_pack",
        "hints": {
            "tier_1": f"Divide each carton dimension by {cube_s} cm: {fit_l}, {fit_b}, {fit_h}.",
            "tier_2": f"Multiply: {fit_l} × {fit_b} × {fit_h}.",
            "tier_3": f"{total_cubes} boxes.",
        },
        "misconception_tags": ["dividing_carton_volume_by_cube_volume_when_dimensions_do_not_divide_evenly"],
    }


# ----------------------------------------------------------------------
# 50. Rate of Filling: Tank Water Filling Time
# ----------------------------------------------------------------------
def arch_50_rate_of_filling_tank_with_water_given_tap_flow_rate(rng: random.Random) -> Dict[str, Any]:
    l = 100
    b = 50
    h = 40
    vol_cm3 = l * b * h  # 200 000 cm³
    capacity_l = vol_cm3 // 1000  # 200 litres

    flow_rate = rng.choice([10, 20, 25])  # litres per minute
    time_mins = capacity_l // flow_rate

    prompt = (
        f"A rectangular reservoir has dimensions \\({l}\\text{{ cm}} \\times {b}\\text{{ cm}} \\times {h}\\text{{ cm}}\\). "
        f"A garden tap delivers water into the empty reservoir at a constant flow rate of \\({flow_rate}\\text{{ litres per minute}}\\).\n\n"
        f"1. Calculate the capacity of the reservoir in litres.\n"
        f"2. How many minutes will it take for the tap to fill the reservoir completely?"
    )
    sol = (
        f"**1. Capacity Calculation:**\n"
        f"\\[ V = {l} \\times {b} \\times {h} = {vol_cm3:,}\\text{{ cm}}^3 \\]\n"
        f"\\[ \\text{{Capacity}} = \\frac{{{vol_cm3}}}{{1\\,000}} = {capacity_l}\\text{{ litres}} \\]\n\n"
        f"**2. Time to Fill:**\n"
        f"\\[ \\text{{Time}} = \\frac{{\\text{{Capacity}}}}{{\\text{{Flow Rate}}}} = \\frac{{{capacity_l}}}{{{flow_rate}}} = {time_mins}\\text{{ minutes}} \\]".replace(",", " ")
    )
    ans = f"1. {capacity_l} litres; 2. {time_mins} minutes"
    return {
        "id": f"g8_meas_flow_{rng.randint(100000, 999999)}",
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
        "subskill": "50_rate_of_filling_tank_with_water_given_tap_flow_rate",
        "learning_objective_id": "math_g8_meas_flow",
        "hints": {
            "tier_1": f"Volume in cm³ = {vol_cm3}; Capacity in litres = {capacity_l} L.",
            "tier_2": f"Divide capacity by flow rate: {capacity_l} / {flow_rate}.",
            "tier_3": f"{time_mins} minutes.",
        },
        "misconception_tags": ["dividing_by_volume_in_cm3_instead_of_litres"],
    }
