"""Subskills 10 to 18: Surface Area of Rectangular and Triangular Prisms for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Total surface area of a closed rectangular cardboard box."""
    length = r.randint(40, 80)  # cm
    width = r.randint(25, 50)   # cm
    height = r.randint(20, 45)  # cm

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is manufacturing a closed rectangular cardboard storage box with dimensions:\n"
        f"- Length ($l$) = **{length} cm**\n"
        f"- Width ($w$) = **{width} cm**\n"
        f"- Height ($h$) = **{height} cm**\n\n"
        f"Calculate the **total surface area** of cardboard required to assemble one closed box (excluding flap overlap).\n"
        f"*(Formula: $\\text{{Total Surface Area}} = 2(l \\times w + l \\times h + w \\times h)$)*"
    )

    lw = length * width
    lh = length * height
    wh = width * height
    sa_cm2 = 2 * (lw + lh + wh)

    correct_ans = f"{_fmt(sa_cm2)} cm²"

    # Distractor 1: Forgot factor of 2
    dist_no_2 = f"{_fmt(lw + lh + wh)} cm²"
    # Distractor 2: Volume calculation
    vol = length * width * height
    dist_vol = f"{_fmt(vol)} cm²"

    custom_opts = [
        correct_ans,
        dist_no_2,
        dist_vol,
        f"{_fmt(sa_cm2 + 500)} cm²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of each pair of opposing faces [1 mark]:\n"
        f"- Top & Bottom: 2 × ({length} cm × {width} cm) = 2 × {_fmt(lw)} = {_fmt(2 * lw)} cm².\n"
        f"- Front & Back: 2 × ({length} cm × {height} cm) = 2 × {_fmt(lh)} = {_fmt(2 * lh)} cm².\n"
        f"- Left & Right: 2 × ({width} cm × {height} cm) = 2 × {_fmt(wh)} = {_fmt(2 * wh)} cm².\n\n"
        f"Step 2: Sum all three pairs [1 mark]:\n"
        f"Total Surface Area = 2({_fmt(lw)} + {_fmt(lh)} + {_fmt(wh)}) = 2 × {_fmt(lw + lh + wh)} cm².\n\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_10",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the area of the three distinct rectangular faces: (l × w), (l × h), and (w × h). Add them and multiply by 2.",
        tier_2=f"lw = {lw}, lh = {lh}, wh = {wh}. Sum = {lw + lh + wh}. Multiply by 2.",
        tier_3=f"Total Surface Area = 2 × {lw + lh + wh} = {correct_ans}.",
        r=r,
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Surface area of an open-top rectangular toy chest / planter box."""
    length = round(r.choice([1.2, 1.5, 1.8, 2.0]), 2)  # m
    width = round(r.choice([0.6, 0.8, 1.0]), 2)        # m
    height = round(r.choice([0.5, 0.6, 0.75]), 2)      # m

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is building an **open-top wooden planter box** with no lid for a community garden.\n"
        f"The planter has outer measurements: length = **{_fmt(length)} m**, width = **{_fmt(width)} m**, and height = **{_fmt(height)} m**.\n\n"
        f"Calculate the **exterior surface area** of wood that requires waterproof sealant (the bottom base and the 4 vertical sides, with NO top lid).\n"
        f"*(Formula: $\\text{{Surface Area}} = (l \\times w) + 2(l \\times h) + 2(w \\times h)$)*"
    )

    base_area = round(length * width, 4)
    long_sides = round(2 * (length * height), 4)
    short_sides = round(2 * (width * height), 4)
    total_sa = round(base_area + long_sides + short_sides, 2)

    correct_ans = f"{_fmt(total_sa)} m²"

    # Distractor 1: Closed box with top lid
    closed_sa = round(2 * base_area + long_sides + short_sides, 2)
    # Distractor 2: No base (only 4 sides)
    no_base = round(long_sides + short_sides, 2)

    custom_opts = [
        correct_ans,
        f"{_fmt(closed_sa)} m²",
        f"{_fmt(no_base)} m²",
        f"{_fmt(round(total_sa + 1.2, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the single bottom base [1 mark]:\n"
        f"Base = length × width = {_fmt(length)} m × {_fmt(width)} m = {_fmt(base_area, 2)} m².\n\n"
        f"Step 2: Calculate the area of the 4 vertical sides [1 mark]:\n"
        f"Long sides = 2 × ({_fmt(length)} × {_fmt(height)}) = {_fmt(long_sides, 2)} m².\n"
        f"Short sides = 2 × ({_fmt(width)} × {_fmt(height)}) = {_fmt(short_sides, 2)} m².\n"
        f"Sides total = {_fmt(long_sides + short_sides, 2)} m².\n\n"
        f"Step 3: Sum base and vertical sides [1 mark]:\n"
        f"Total Area = {_fmt(base_area, 2)} + {_fmt(long_sides + short_sides, 2)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_11",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Because the box has no lid, include only 1 base: Area = (l × w) + 2(l × h) + 2(w × h).",
        tier_2=f"Base = {base_area:.2f}. Two long sides = {long_sides:.2f}. Two short sides = {short_sides:.2f}.",
        tier_3=f"Total area = {correct_ans}.",
        r=r,
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Four interior walls of a rectangular classroom for painting."""
    length = r.randint(7, 10)  # m
    width = r.randint(5, 7)    # m
    height = round(r.choice([2.8, 3.0, 3.2]), 1)  # m

    name = r.choice(SA_NAMES)

    prompt = (
        f"A school maintenance team needs to repaint the **four interior walls** of a rectangular classroom.\n"
        f"The classroom is **{length} m** long, **{width} m** wide, and has a ceiling height of **{_fmt(height)} m**.\n"
        f"(The floor and ceiling will NOT be painted).\n\n"
        f"Calculate the **gross wall surface area** of the 4 vertical walls.\n"
        f"*(Formula: $\\text{{Wall Area}} = 2 \\times (l + w) \\times h$)*"
    )

    perimeter = 2 * (length + width)
    wall_area = round(perimeter * height, 2)

    correct_ans = f"{_fmt(wall_area)} m²"

    # Distractor 1: Included floor and ceiling
    floor_ceil = 2 * (length * width)
    total_sa = round(wall_area + floor_ceil, 2)
    # Distractor 2: Only 2 walls
    half_walls = round((length + width) * height, 2)

    custom_opts = [
        correct_ans,
        f"{_fmt(total_sa)} m²",
        f"{_fmt(half_walls)} m²",
        f"{_fmt(round(wall_area + 15.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate room perimeter [1 mark]:\n"
        f"Perimeter = 2({length} m + {width} m) = 2({length + width}) = {perimeter} m.\n\n"
        f"Step 2: Multiply perimeter by wall height [1 mark]:\n"
        f"Wall Area = Perimeter × height = {perimeter} m × {_fmt(height)} m.\n\n"
        f"Step 3: Stated answer with units [1 mark]:\n"
        f"Wall Area = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_12",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The 4 walls equal the room's perimeter multiplied by the ceiling height: 2(l + w) × h.",
        tier_2=f"Perimeter = 2({length} + {width}) = {perimeter} m. Multiply by {height} m.",
        tier_3=f"Wall Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Total surface area of a triangular prism camping tent."""
    # Triangular prism: 2 equilateral/isosceles triangular ends, 2 sloped roof faces, 1 flat floor
    tri_base = round(r.choice([1.6, 2.0, 2.4]), 1)  # m
    tri_height = round(r.choice([1.2, 1.5, 1.8]), 1) # m
    tent_length = round(r.choice([2.2, 2.5, 3.0]), 1) # m
    
    # Slanted side length via Pythagoras: s = sqrt((b/2)^2 + h^2)
    half_b = tri_base / 2.0
    slant_side = round(math.sqrt(half_b ** 2 + tri_height ** 2), 2)

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is inspecting a triangular prism two-pole canvas camping tent.\n"
        f"The tent dimensions are:\n"
        f"- Triangular ends: base = **{_fmt(tri_base)} m**, vertical height = **{_fmt(tri_height)} m**, each slant side = **{_fmt(slant_side)} m**.\n"
        f"- Length of the tent ridge = **{_fmt(tent_length)} m**.\n\n"
        f"Calculate the **total surface area** of canvas and groundsheet required to manufacture this complete enclosed tent (2 triangular ends, 2 sloped sides, and 1 rectangular floor).\n"
        f"*(Formulas: $\\text{{Triangle Area}} = \\frac{{1}}{{2}} b \\times h$; $\\text{{Rectangle Area}} = l \\times w$. Round to 2 decimal places)*"
    )

    area_two_triangles = round(2 * (0.5 * tri_base * tri_height), 2)
    area_two_slopes = round(2 * (tent_length * slant_side), 2)
    area_floor = round(tent_length * tri_base, 2)
    total_canvas = round(area_two_triangles + area_two_slopes + area_floor, 2)

    correct_ans = f"{_fmt(total_canvas)} m²"

    # Distractor without floor
    dist_no_floor = f"{_fmt(round(area_two_triangles + area_two_slopes, 2))} m²"
    # Distractor only 1 triangle
    dist_one_tri = f"{_fmt(round(area_two_triangles/2 + area_two_slopes + area_floor, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_no_floor,
        dist_one_tri,
        f"{_fmt(round(total_canvas + 2.5, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the 2 triangular ends [1 mark]:\n"
        f"Ends = 2 × (0,5 × {_fmt(tri_base)} m × {_fmt(tri_height)} m) = {_fmt(area_two_triangles)} m².\n\n"
        f"Step 2: Calculate the area of the 2 sloped roof sides [1 mark]:\n"
        f"Sloped sides = 2 × ({_fmt(tent_length)} m × {_fmt(slant_side)} m) = {_fmt(area_two_slopes)} m².\n\n"
        f"Step 3: Calculate floor and sum all 5 faces [1 mark]:\n"
        f"Floor = {_fmt(tent_length)} m × {_fmt(tri_base)} m = {_fmt(area_floor)} m².\n"
        f"Total Area = {_fmt(area_two_triangles)} + {_fmt(area_two_slopes)} + {_fmt(area_floor)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_13",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Sum the 5 faces: 2 triangular ends + 2 rectangular sloped sides + 1 rectangular floor.",
        tier_2=f"Ends = {area_two_triangles} m². Slopes = {area_two_slopes} m². Floor = {area_floor} m².",
        tier_3=f"Total Surface Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Triangular prism roof truss surface area (gable ends and pitch faces, excluding floor)."""
    ridge_length = r.randint(10, 16)  # m
    gable_base = r.choice([6.0, 7.0, 8.0])  # m
    gable_height = round(r.choice([2.0, 2.4, 2.8]), 1)  # m
    rafter_length = round(r.choice([3.6, 4.0, 4.5]), 1)  # m (slant of each roof pitch)

    prompt = (
        f"A roofing contractor is sheeting a pitched gable roof shaped as a triangular prism.\n"
        f"The roof measurements are:\n"
        f"- Ridge length: **{ridge_length} m**\n"
        f"- Two pitched roof sides: each rafter slope is **{_fmt(rafter_length)} m** long\n"
        f"- Two vertical triangular gable ends: base = **{_fmt(gable_base)} m**, height = **{_fmt(gable_height)} m**\n\n"
        f"Calculate the **exterior surface area** of the roof (2 pitched rectangular sides + 2 triangular gable ends, excluding the ceiling/attic floor).\n"
        f"*(Round to 2 decimal places)*"
    )

    two_pitches = round(2 * (ridge_length * rafter_length), 2)
    two_gables = round(2 * (0.5 * gable_base * gable_height), 2)
    total_roof_sa = round(two_pitches + two_gables, 2)

    correct_ans = f"{_fmt(total_roof_sa)} m²"

    # Distractor: Only pitches
    dist_pitches_only = f"{_fmt(two_pitches)} m²"
    # Distractor: Added attic floor
    attic_floor = round(ridge_length * gable_base, 2)
    dist_with_floor = f"{_fmt(round(total_roof_sa + attic_floor, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_pitches_only,
        dist_with_floor,
        f"{_fmt(round(total_roof_sa + 10.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the 2 pitched roof sides [1 mark]:\n"
        f"Pitch Area = 2 × ({ridge_length} m × {_fmt(rafter_length)} m) = {_fmt(two_pitches)} m².\n\n"
        f"Step 2: Calculate the area of the 2 vertical triangular gable ends [1 mark]:\n"
        f"Gable Area = 2 × (0,5 × {_fmt(gable_base)} m × {_fmt(gable_height)} m) = {_fmt(two_gables)} m².\n\n"
        f"Step 3: Sum the exterior roof faces [1 mark]:\n"
        f"Total Roof Area = {_fmt(two_pitches)} m² + {_fmt(two_gables)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_14",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the area of the 2 pitched rectangular slopes and add the 2 triangular gable ends.",
        tier_2=f"Pitches = 2 × ({ridge_length} × {rafter_length}) = {two_pitches} m². Gables = 2 × (0,5 × {gable_base} × {gable_height}) = {two_gables} m².",
        tier_3=f"Total = {two_pitches} + {two_gables} = {correct_ans}.",
        r=r,
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Exterior plastering area of a rectangular building foundation wall."""
    length = r.randint(12, 20)  # m
    width = r.randint(8, 14)    # m
    plinth_height = round(r.choice([0.45, 0.60, 0.75]), 2)  # m height of exposed foundation plinth

    name = r.choice(SA_NAMES)

    prompt = (
        f"A bricklayer must plaster the exterior exposed foundation plinth walls around a new house.\n"
        f"The house foundation is a rectangle measuring **{length} m** long by **{width} m** wide.\n"
        f"The foundation plinth rises **{_fmt(plinth_height)} m** above ground level all the way around the exterior perimeter.\n\n"
        f"Calculate the **total exterior surface area** that must be plastered."
    )

    perimeter = 2 * (length + width)
    plaster_area = round(perimeter * plinth_height, 2)

    correct_ans = f"{_fmt(plaster_area)} m²"

    # Distractor: perimeter only
    dist_p = f"{_fmt(perimeter)} m²"
    # Distractor: length * width
    dist_lw = f"{_fmt(length * width)} m²"

    custom_opts = [
        correct_ans,
        dist_p,
        dist_lw,
        f"{_fmt(round(plaster_area + 5.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the exterior perimeter of the foundation [1 mark]:\n"
        f"Perimeter = 2({length} m + {width} m) = 2({length + width}) = {perimeter} m.\n\n"
        f"Step 2: Multiply perimeter by the exposed plinth height [1 mark]:\n"
        f"Plaster Area = Perimeter × height = {perimeter} m × {_fmt(plinth_height)} m.\n\n"
        f"Step 3: Stated answer with units [1 mark]:\n"
        f"Plaster Area = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_15",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The vertical plinth area equals perimeter multiplied by plinth height.",
        tier_2=f"Perimeter = 2({length} + {width}) = {perimeter} m. Area = {perimeter} × {plinth_height}.",
        tier_3=f"Plaster Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Surface area comparison of two rectangular prisms with identical volume."""
    # Volume = 64 cm3: Cube 4x4x4 vs Box 8x4x2
    cube_s = 4
    sa_cube = 6 * (cube_s ** 2)  # 6 * 16 = 96 cm2

    box_l, box_w, box_h = 8, 4, 2
    sa_box = 2 * (box_l * box_w + box_l * box_h + box_w * box_h)  # 2*(32 + 16 + 8) = 2*56 = 112 cm2

    prompt = (
        f"A packaging company compares two closed cardboard containers that both hold exactly **64 cm³** of product:\n"
        f"- **Container A (Cube)**: dimensions **4 cm × 4 cm × 4 cm**.\n"
        f"- **Container B (Elongated Box)**: dimensions **8 cm × 4 cm × 2 cm**.\n\n"
        f"Calculate the **total surface area** of each container, and determine which shape uses **LESS cardboard**."
    )

    diff = sa_box - sa_cube
    correct_ans = f"Container A uses {_fmt(diff)} cm² less cardboard (A = {_fmt(sa_cube)} cm² vs B = {_fmt(sa_box)} cm²)"

    opt_b = f"Container B uses {_fmt(diff)} cm² less cardboard (B = {_fmt(sa_cube)} cm² vs A = {_fmt(sa_box)} cm²)"
    opt_c = f"Both containers require identical surface area because their volumes are equal ({_fmt(sa_cube)} cm² each)"
    opt_d = f"Container A uses 32 cm² more cardboard than Container B"

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Calculate surface area of Container A (Cube) [1 mark]:\n"
        f"SA(A) = 6 × (4 cm)² = 6 × 16 = {_fmt(sa_cube)} cm².\n\n"
        f"Step 2: Calculate surface area of Container B (Box) [1 mark]:\n"
        f"SA(B) = 2(8×4 + 8×2 + 4×2) = 2(32 + 16 + 8) = 2 × 56 = {_fmt(sa_box)} cm².\n\n"
        f"Step 3: Compare surface areas [1 mark]:\n"
        f"Difference = {_fmt(sa_box)} cm² - {_fmt(sa_cube)} cm² = {_fmt(diff)} cm².\n"
        f"Container A (the cube) is more compact and uses {diff} cm² less cardboard."
    )

    return _build_question_payload(
        subskill_id="subskill_16",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the surface area of both objects: Cube SA = 6s²; Box SA = 2(lw + lh + wh).",
        tier_2=f"Cube = 6 × 16 = {sa_cube} cm². Box = 2(32 + 16 + 8) = {sa_box} cm².",
        tier_3=f"Conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Gift wrapping paper requirement with percentage overlap allowance."""
    l = r.randint(20, 35)  # cm
    w = r.randint(15, 25)  # cm
    h = r.randint(8, 15)   # cm
    overlap_pct = r.choice([15, 20])

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is wrapping a rectangular gift box measuring **{l} cm** long, **{w} cm** wide, and **{h} cm** high.\n"
        f"To allow for folding edges and tape overlap, an additional **{overlap_pct}%** of wrapping paper is required above the exact box surface area.\n\n"
        f"Calculate the **minimum area of wrapping paper** required in cm².\n"
        f"*(Round to the nearest whole cm²)*"
    )

    exact_sa = 2 * (l * w + l * h + w * h)
    paper_needed = int(round(exact_sa * (1 + overlap_pct / 100.0)))

    correct_ans = f"{_fmt(paper_needed)} cm²"

    custom_opts = [
        correct_ans,
        f"{_fmt(exact_sa)} cm²",
        f"{_fmt(int(round(exact_sa * 1.5)))} cm²",
        f"{_fmt(paper_needed + 250)} cm²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the exact total surface area of the box [1 mark]:\n"
        f"SA = 2({l}×{w} + {l}×{h} + {w}×{h}) = 2({l*w} + {l*h} + {w*h}) = {_fmt(exact_sa)} cm².\n\n"
        f"Step 2: Add {overlap_pct}% overlap allowance [1 mark]:\n"
        f"Paper = {_fmt(exact_sa)} × (1 + {overlap_pct} ÷ 100) = {_fmt(exact_sa)} × {1 + overlap_pct/100:.2f}.\n\n"
        f"Step 3: Stated answer rounded to nearest integer [1 mark]:\n"
        f"Paper Required = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_17",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the exact surface area: 2(lw + lh + wh), then increase it by the overlap percentage.",
        tier_2=f"Exact SA = {exact_sa} cm². Multiply by {1 + overlap_pct/100:.2f}.",
        tier_3=f"Result = {correct_ans}.",
        r=r,
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Surface area of a stepped rectangular display podium (composite faces)."""
    # 2 tiers: Lower step (L1 x W1 x H1), Upper step centered (L2 x W2 x H2)
    l1, w1, h1 = 120, 80, 25  # cm
    l2, w2, h2 = 80, 50, 25   # cm

    prompt = (
        f"An exhibition booth uses a two-tiered stepped wooden display podium:\n"
        f"- **Lower Tier Base**: **120 cm** long, **80 cm** wide, **25 cm** high.\n"
        f"- **Upper Tier Step**: **80 cm** long, **50 cm** wide, **25 cm** high, centered on top of the lower tier.\n\n"
        f"Calculate the **total exposed surface area** of the podium requiring painting (all vertical sides plus all horizontal top faces; the underneath floor base is NOT painted).\n"
        f"*(Hint: The total horizontal top exposed area equals the area of the lower tier top face!)*"
    )

    # All vertical sides:
    vert_1 = 2 * (l1 + w1) * h1  # 2 * 200 * 25 = 10 000 cm2
    vert_2 = 2 * (l2 + w2) * h2  # 2 * 130 * 25 = 6 500 cm2
    total_vert = vert_1 + vert_2 # 16 500 cm2

    # Top faces: Upper step top (l2*w2) + exposed lower shelf (l1*w1 - l2*w2) = l1*w1
    total_horizontal = l1 * w1   # 120 * 80 = 9 600 cm2

    total_painted = total_vert + total_horizontal # 26 100 cm2
    correct_ans = f"{_fmt(total_painted)} cm²"

    custom_opts = [
        correct_ans,
        f"{_fmt(total_painted + l1 * w1)} cm²", # Added floor
        f"{_fmt(total_vert)} cm²", # Forgot top
        f"{_fmt(total_painted - 3000)} cm²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of all vertical side faces [1 mark]:\n"
        f"- Lower tier vertical sides: 2({l1} + {w1}) × {h1} = 2({l1+w1}) × {h1} = {_fmt(vert_1)} cm².\n"
        f"- Upper tier vertical sides: 2({l2} + {w2}) × {h2} = 2({l2+w2}) × {h2} = {_fmt(vert_2)} cm².\n"
        f"Total vertical area = {_fmt(vert_1)} + {_fmt(vert_2)} = {_fmt(total_vert)} cm².\n\n"
        f"Step 2: Calculate the horizontal upward-facing surfaces [1 mark]:\n"
        f"Combined horizontal top surfaces = Lower tier top ({l1} × {w1}) = {_fmt(total_horizontal)} cm².\n\n"
        f"Step 3: Sum vertical and horizontal painted areas [1 mark]:\n"
        f"Total Exposed Surface Area = {_fmt(total_vert)} cm² + {_fmt(total_horizontal)} cm² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_18",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add all vertical faces from both steps, plus the horizontal top surfaces.",
        tier_2=f"Verticals = {vert_1} + {vert_2} = {total_vert} cm². Top horizontal surfaces = {total_horizontal} cm².",
        tier_3=f"Total area = {total_vert} + {total_horizontal} = {correct_ans}.",
        r=r,
    )
