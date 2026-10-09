"""Grade 8 Mathematics — Surface Area & Volume of 3D Objects (Deterministic 6-Pillar Generator).
Authentic CAPS exam generator covering:
- Surface Area of rectangular prisms: SA = 2(lb + lh + bh) and triangular prisms.
- Volume of rectangular prisms: V = l * b * h.
- Volume of triangular prisms: V = 1/2 * b * h_triangle * H_prism.
- Unit conversions: cm^3 to litres and ml (1 cm^3 = 1 ml, 1 000 cm^3 = 1 litre).
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


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


TOPIC = "grade8_math_measurement_3d"
LO = "g8_math_measurement_3d"


def generate_rectangular_prism(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    l = r.randint(10, 25)
    b = r.randint(6, 15)
    h = r.randint(4, 12)
    
    # Volume and Surface Area
    volume_cm3 = l * b * h
    volume_litres = volume_cm3 / 1000.0
    
    sa_cm2 = 2 * (l * b + l * h + b * h)
    
    vol_litres_str = _fmt_sa(volume_litres, 3)
    
    prompt = (
        f"A closed rectangular container has length \\(l = {l}\\text{{ cm}}\\), "
        f"breadth \\(b = {b}\\text{{ cm}}\\), and height \\(h = {h}\\text{{ cm}}\\).\n\n"
        f"1. Write down the formula for the total surface area of a rectangular prism.\n"
        f"2. Calculate the total surface area of the container in \\(\\text{{cm}}^2\\).\n"
        f"3. Calculate the volume (capacity) of the container in \\(\\text{{cm}}^3\\).\n"
        f"4. Convert the volume into litres, given that \\(1\\text{{ litre}} = 1\\,000\\text{{ cm}}^3\\)."
    )
    prompt_latex = (
        rf"\text{{Rectangular Prism: }} l = {l}\text{{ cm}}, \quad b = {b}\text{{ cm}}, \quad h = {h}\text{{ cm}}." "\n\n"
        r"\text{Calculate total surface area } (SA), \text{ volume } (V), \text{ and capacity in litres.}"
    )
    answer_latex = (
        r"\text{1. } SA = 2(l \times b + l \times h + b \times h)" "\n"
        rf"\text{{2. }} SA = 2(({l})({b}) + ({l})({h}) + ({b})({h})) = 2({l*b} + {l*h} + {b*h}) = 2({l*b + l*h + b*h}) = {sa_cm2}\text{{ cm}}^2" "\n"
        rf"\text{{3. }} V = l \times b \times h = {l} \times {b} \times {h} = {volume_cm3}\text{{ cm}}^3" "\n"
        rf"\text{{4. Capacity}} = \frac{{{volume_cm3}}}{{1\,000}} = {vol_litres_str}\text{{ litres}}"
    )
    sample_answer = (
        f"1. Surface area formula: SA = 2(lb + lh + bh)\n"
        f"2. SA = 2({l} x {b} + {l} x {h} + {b} x {h}) = 2({l*b} + {l*h} + {b*h}) = 2({l*b + l*h + b*h}) = {sa_cm2} cm².\n"
        f"3. Volume: V = l x b x h = {l} x {b} x {h} = {volume_cm3} cm³.\n"
        f"4. Capacity in litres = {volume_cm3} / 1 000 = {vol_litres_str} litres."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "State surface area formula: SA = 2(lb + lh + bh)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct surface area calculation: {sa_cm2} cm² with units", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct volume calculation: {volume_cm3} cm³ with units", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Accurate conversion to litres: {vol_litres_str} litres", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "Surface area has 6 faces (3 pairs of equal rectangles). Volume is base area multiplied by height: l x b x h.",
        "tier_2": "SA = 2(lb + lh + bh). Capacity in litres = volume in cm³ divided by 1 000.",
        "tier_3": f"SA = 2({l*b} + {l*h} + {b*h}) = {sa_cm2} cm². V = {l} x {b} x {h} = {volume_cm3} cm³. Litres = {vol_litres_str} L.",
    }
    return {
        "id": f"g8_meas_rect_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "rectangular_prism_surface_area_volume",
        "learning_objective_id": f"{LO}_rectangular_prism",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["confusing_surface_area_with_volume", "capacity_conversion_by_100_instead_of_1000"],
        "keywords": ["surface area", "volume", "capacity", "rectangular prism", "litres"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": mode,
        "difficulty": "medium",
        "marks": 5,
    }


def generate_triangular_prism(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    # Right-angled triangular base: sides a, b, hypotenuse c
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    a, b, c = r.choice(triples)
    scale = r.choice([1, 2])
    a, b, c = a * scale, b * scale, c * scale
    
    prism_length = r.randint(10, 20)
    
    # Area of triangular base = 1/2 * a * b
    base_area = int(0.5 * a * b)
    volume_cm3 = base_area * prism_length
    
    # Surface area = 2 * (base_area) + (perimeter of triangle * prism_length)
    tri_perimeter = a + b + c
    lateral_area = tri_perimeter * prism_length
    total_sa = 2 * base_area + lateral_area
    
    prompt = (
        f"A right-angled triangular prism has a base with perpendicular sides \\(a = {a}\\text{{ cm}}\\) "
        f"and \\(b = {b}\\text{{ cm}}\\), and hypotenuse \\(c = {c}\\text{{ cm}}\\). "
        f"The length of the prism is \\(H = {prism_length}\\text{{ cm}}\\).\n\n"
        f"1. Calculate the area of the triangular base in \\(\\text{{cm}}^2\\).\n"
        f"2. Calculate the volume of the triangular prism in \\(\\text{{cm}}^3\\).\n"
        f"3. Calculate the total surface area of the prism by summing the areas of the 2 triangular bases and 3 rectangular faces."
    )
    prompt_latex = (
        rf"\text{{Triangular Prism: Base perpendicular sides }} a = {a}\text{{ cm}}, \, b = {b}\text{{ cm}}, \, c = {c}\text{{ cm}}; \, H = {prism_length}\text{{ cm}}." "\n\n"
        r"\text{Calculate base area, volume } (V = \text{Base Area} \times H), \text{ and total surface area } (SA)."
    )
    answer_latex = (
        rf"\text{{1. Base Area}} = \frac{{1}}{{2}} \times {a} \times {b} = {base_area}\text{{ cm}}^2" "\n"
        rf"\text{{2. Volume}} = \text{{Base Area}} \times H = {base_area} \times {prism_length} = {volume_cm3}\text{{ cm}}^3" "\n"
        rf"\text{{3. }} SA = 2(\text{{Base Area}}) + (a + b + c) \times H = 2({base_area}) + ({tri_perimeter})({prism_length}) = {2*base_area} + {lateral_area} = {total_sa}\text{{ cm}}^2"
    )
    sample_answer = (
        f"1. Area of triangular base = 1/2 x base x height = 1/2 x {a} x {b} = {base_area} cm².\n"
        f"2. Volume = Area of base x height of prism = {base_area} x {prism_length} = {volume_cm3} cm³.\n"
        f"3. Total Surface Area:\n"
        f"   - Two triangular ends = 2 x {base_area} = {2*base_area} cm².\n"
        f"   - Three rectangular faces = ({a} + {b} + {c}) x {prism_length} = {tri_perimeter} x {prism_length} = {lateral_area} cm².\n"
        f"   - Total SA = {2*base_area} + {lateral_area} = {total_sa} cm²."
    )
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate triangular base area: {base_area} cm²", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate volume: {volume_cm3} cm³", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Calculate lateral area: {lateral_area} cm²", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate total surface area: {total_sa} cm²", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": 1}],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "tier_1": "The base is a right-angled triangle: Area = 1/2 x a x b. The volume is Base Area x Prism Length.",
        "tier_2": "Total surface area has 5 faces: 2 triangular bases + 3 rectangular sides: SA = 2(1/2 x a x b) + (a + b + c) x H.",
        "tier_3": f"Base area = {base_area} cm². Volume = {base_area} x {prism_length} = {volume_cm3} cm³. Total SA = {total_sa} cm².",
    }
    return {
        "id": f"g8_meas_tri_{random.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "triangular_prism_surface_area_volume",
        "learning_objective_id": f"{LO}_triangular_prism",
        "prompt": prompt,
        "prompt_latex": prompt_latex,
        "answer_latex": answer_latex,
        "sample_answer": sample_answer,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["forgetting_half_in_triangle_area", "omitting_one_of_the_rectangular_faces"],
        "keywords": ["triangular prism", "surface area", "volume", "base area"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": mode,
        "difficulty": "medium",
        "marks": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    r = _rng(seed)
    if archetype == "rectangular":
        return generate_rectangular_prism(r, mode=mode)
    elif archetype == "triangular":
        return generate_triangular_prism(r, mode=mode)
    else:
        choice = r.choice(["rectangular", "triangular"])
        if choice == "rectangular":
            return generate_rectangular_prism(r, mode=mode)
        else:
            return generate_triangular_prism(r, mode=mode)
