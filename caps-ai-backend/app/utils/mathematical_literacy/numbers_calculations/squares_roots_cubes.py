"""Cluster 3: Squares, Square Roots & Cubes (8 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_num_pwr_square_area_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    side_m = round(r.choice([3.5, 4.0, 4.5, 5.0, 6.5, 7.2]), 1)
    area = round(side_m ** 2, 2)
    ans_str = f"{_fmt(area)} m²"

    prompt = (
        f"{name} constructs a square raised vegetable garden bed for growing spinach and carrots in Polokwane.\n\n"
        f"Each side of the square garden measures **{_fmt(side_m, 1)} metres**.\n\n"
        f"Calculate the **ground surface area** of the square garden bed."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The area of a square is the side length squared ($s^2$):\n"
        f"  $$\\text{{Area}} = s^2 = s \\times s$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Area}} = {_fmt(side_m, 1)} \\times {_fmt(side_m, 1)} = {_fmt(side_m, 1)}^2 = {_fmt(area)}\\text{{ m}}^2$.\n"
        f"✓ **[1 Mark: Method – squaring side length]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct area with units]**"
    )
    return _make_q(
        subskill="num_pwr_square_area_calculation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – side squared", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply the side length by itself: {_fmt(side_m, 1)} × {_fmt(side_m, 1)}.",
            "tier_2": f"{side_m}² = {area}.",
            "tier_3": f"Surface area = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_square_root_side_from_area(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    side_m = r.choice([6, 7, 8, 9, 11, 12, 14, 15])
    area = side_m ** 2
    ans_str = f"{side_m} m"

    prompt = (
        f"{name} has a square lawn with a total area of **{area} m²**.\n\n"
        f"{name} needs to purchase wire fencing to line one complete side of the lawn.\n\n"
        f"Calculate the **length of one side** of the square lawn by finding the square root of the area."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Because $\\text{{Area}} = s^2$, the side length is the square root of the area:\n"
        f"  $$s = \\sqrt{{\\text{{Area}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $s = \\sqrt{{{area}}} = {side_m}\\text{{ m}}$.\n"
        f"✓ **[1 Mark: Method – taking square root of area]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct side length with units]**"
    )
    return _make_q(
        subskill="num_pwr_square_root_side_from_area",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – square root of area", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Find what number multiplied by itself equals {area}.",
            "tier_2": f"√{area} = {side_m}.",
            "tier_3": f"Side length = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_cube_volume_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    side_m = round(r.choice([1.2, 1.5, 1.8, 2.0, 2.4]), 1)
    vol = round(side_m ** 3, 3)
    ans_str = f"{_fmt(vol, 3)} m³"

    prompt = (
        f"{name} installs a cubic rainwater storage tank next to a rural homestead.\n\n"
        f"The internal dimensions of the tank form an exact cube with side length **{_fmt(side_m, 1)} metres**.\n\n"
        f"Calculate the **internal volume (capacity)** of the cubic tank in cubic metres ($m^3$)."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The volume of a cube is the cube of its edge length ($s^3$):\n"
        f"  $$\\text{{Volume}} = s^3 = s \\times s \\times s$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Volume}} = {_fmt(side_m, 1)} \\times {_fmt(side_m, 1)} \\times {_fmt(side_m, 1)} = {_fmt(side_m, 1)}^3 = {_fmt(vol, 3)}\\text{{ m}}^3$.\n"
        f"✓ **[1 Mark: Method – calculating cube of edge length]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume with units]**"
    )
    return _make_q(
        subskill="num_pwr_cube_volume_calculation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – side cubed", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply {_fmt(side_m, 1)} by itself three times: {_fmt(side_m, 1)} × {_fmt(side_m, 1)} × {_fmt(side_m, 1)}.",
            "tier_2": f"{side_m}³ = {vol}.",
            "tier_3": f"Volume = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_cube_root_dimension_from_volume(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    dim_m = r.choice([2, 3, 4, 5])
    vol = dim_m ** 3
    ans_str = f"{dim_m} m"

    prompt = (
        f"A prefabricated cubic concrete silage pit on a dairy farm has an internal volume of **{vol} m³**.\n\n"
        f"Calculate the **length of one edge** of the silage pit by finding the cube root of the volume."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The edge length of a cube is given by the cube root of its volume:\n"
        f"  $$s = \\sqrt[3]{{\\text{{Volume}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $s = \\sqrt[3]{{{vol}}} = {dim_m}\\text{{ m}}$.\n"
        f"✓ **[1 Mark: Method – taking cube root of volume]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct edge dimension with units]**"
    )
    return _make_q(
        subskill="num_pwr_cube_root_dimension_from_volume",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – cube root of volume", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Find what number multiplied by itself three times equals {vol}.",
            "tier_2": f"∛{vol} = {dim_m}.",
            "tier_3": f"Edge dimension = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_square_difference_border(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    outer_side = r.choice([8, 10, 12])
    inner_side = outer_side - 2
    outer_area = outer_side ** 2
    inner_area = inner_side ** 2
    border_area = outer_area - inner_area
    ans_str = f"{border_area} m²"

    prompt = (
        f"{name} designs a paved garden patio. The overall paved area is a square with side length **{outer_side} metres**.\n\n"
        f"In the exact centre, there is an unpaved square flowerbed with side length **{inner_side} metres**.\n\n"
        f"Calculate the **net area of the paved border** ($s_{{\\text{{outer}}}}^2 - s_{{\\text{{inner}}}}^2$)."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Net paved area is the difference between the outer square area and the inner flowerbed area:\n"
        f"  $$\\text{{Paved Area}} = s_{{\\text{{outer}}}}^2 - s_{{\\text{{inner}}}}^2$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• Outer Area: ${outer_side}^2 = {outer_area}\\text{{ m}}^2$.\n"
        f"• Inner Area: ${inner_side}^2 = {inner_area}\\text{{ m}}^2$.\n"
        f"• Net Paved Area: ${outer_area} - {inner_area} = {border_area}\\text{{ m}}^2$.\n"
        f"✓ **[1 Mark: Method – calculating both square areas and subtracting inner from outer]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct border area with units]**"
    )
    return _make_q(
        subskill="num_pwr_square_difference_border",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – outer_area - inner_area", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Outer area = {outer_side}² = {outer_area}. Inner area = {inner_side}² = {inner_area}.",
            "tier_2": f"Subtract inner area from outer area: {outer_area} - {inner_area}.",
            "tier_3": f"Border area = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_pythagoras_hypotenuse_simple(r: random.Random) -> Dict[str, Any]:
    triples = [
        (3, 4, 5),
        (6, 8, 10),
        (5, 12, 13),
        (9, 12, 15)
    ]
    a, b, c = r.choice(triples)
    ans_str = f"{c} m"

    prompt = (
        f"A builder measures the two perpendicular sides of a right-angled corner foundation as **{a} metres** and **{b} metres**.\n\n"
        f"Using the Theorem of Pythagoras ($c = \\sqrt{{a^2 + b^2}}$), calculate the diagonal (hypotenuse) distance to verify that the corner is square."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• According to the Theorem of Pythagoras:\n"
        f"  $$c^2 = a^2 + b^2 \\implies c = \\sqrt{{a^2 + b^2}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $a^2 = {a}^2 = {a**2}$.\n"
        f"• $b^2 = {b}^2 = {b**2}$.\n"
        f"• $c^2 = {a**2} + {b**2} = {c**2}$.\n"
        f"• $c = \\sqrt{{{c**2}}} = {c}\\text{{ m}}$.\n"
        f"✓ **[1 Mark: Method – squaring sides, adding, and taking square root]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct hypotenuse length with units]**"
    )
    return _make_q(
        subskill="num_pwr_pythagoras_hypotenuse_simple",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – √(a² + b²)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Square both sides: {a}² = {a**2} and {b}² = {b**2}.",
            "tier_2": f"Add them: {a**2} + {b**2} = {c**2}. Take the square root: √{c**2}.",
            "tier_3": f"Diagonal = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_square_scale_factor_area(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    orig_side = r.choice([4, 5, 6])
    scale_factor = r.choice([2, 3])
    orig_area = orig_side ** 2
    new_area = (orig_side * scale_factor) ** 2
    ans_str = f"{new_area} m²"

    prompt = (
        f"{name}'s original square courtyard has a side length of **{orig_side} metres** (area = {orig_area} m²).\n\n"
        f"{name} decides to double all linear dimensions by a scale factor of **{scale_factor}**.\n\n"
        f"Calculate the **new area** of the enlarged courtyard ($A_{{\\text{{new}}}} = k^2 \\times A_{{\\text{{orig}}}}$)."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• When linear dimensions scale by factor $k$, area scales by $k^2$:\n"
        f"  $$\\text{{Area}}_{{\\text{{new}}}} = k^2 \\times \\text{{Area}}_{{\\text{{orig}}}}$$\n"
        f"• Alternatively, calculate new side length $s_{{\\text{{new}}}} = {orig_side} \\times {scale_factor} = {orig_side * scale_factor}$ m, then square it.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• New side: ${orig_side} \\times {scale_factor} = {orig_side * scale_factor}\\text{{ m}}$.\n"
        f"• New Area: ${orig_side * scale_factor}^2 = {new_area}\\text{{ m}}^2$ (or ${scale_factor}^2 \\times {orig_area} = {scale_factor**2} \\times {orig_area} = {new_area}\\text{{ m}}^2$).\n"
        f"✓ **[1 Mark: Method – applying scale factor squared to area or squaring new side length]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct scaled area with units]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": orig_side * scale_factor,
        "width": orig_side * scale_factor,
        "shape": "scaled_square",
        "title": f"Scaled Courtyard (Factor {scale_factor})",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="num_pwr_square_scale_factor_area",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – k² × orig_area", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"The new side is {orig_side} × {scale_factor} = {orig_side * scale_factor} m.",
            "tier_2": f"Square the new side: {orig_side * scale_factor}² = {new_area}.",
            "tier_3": f"New area = {ans_str}."
        },
        r=r
    )

def _gen_num_pwr_cube_scale_factor_volume(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    orig_side = r.choice([2, 3])
    scale_factor = r.choice([2, 3])
    factor_word = "doubled" if scale_factor == 2 else "tripled"
    orig_vol = orig_side ** 3
    new_vol = (orig_side * scale_factor) ** 3
    ratio = new_vol // orig_vol
    ans_str = f"{ratio} times"

    prompt = (
        f"A factory manufactures cubic packing boxes. When the side length of a cubic box is **{factor_word}** (scale factor $k = {scale_factor}$):\n\n"
        f"By how many times does the **volume (holding capacity)** of the box increase?"
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• When the linear dimensions of a 3D object are scaled by factor $k$, its volume scales by $k^3$:\n"
        f"  $$\\text{{Volume Factor}} = k^3$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• For $k = {scale_factor}$:\n"
        f"  $$\\text{{Volume Factor}} = {scale_factor}^3 = {ratio}\\text{{ times}}$$\n"
        f"✓ **[1 Mark: Method – cubing the linear scale factor k³]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume scaling factor]**"
    )
    custom_opts = [f"{ratio} times", f"{scale_factor ** 2} times", f"{scale_factor} times", f"{ratio + 2} times"]
    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_3d",
        "length": orig_side * scale_factor,
        "width": orig_side * scale_factor,
        "height": orig_side * scale_factor,
        "shape": "scaled_cube",
        "title": f"Scaled Cube (Side: {orig_side * scale_factor} m, Factor {scale_factor})",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="num_pwr_cube_scale_factor_volume",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – k³ volume scaling", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Volume scales by the cube of the scale factor: k³.",
            "tier_2": "Calculate 2³ = 2 × 2 × 2 = 8.",
            "tier_3": f"Volume increase = {ans_str}."
        },
        options=custom_opts,
        r=r
    )
