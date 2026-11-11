"""Subskills 19 to 27: Surface Area of Cylinders & Curved Forms for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Total surface area of a closed cylindrical tin can."""
    radius_cm = round(r.choice([3.5, 4.0, 4.5, 5.0]), 1)
    height_cm = round(r.choice([10.0, 11.5, 12.0, 14.0]), 1)
    pi_val = 3.142

    prompt = (
        f"A food cannery manufactures closed cylindrical tin cans for baked beans.\n"
        f"Each can has a base radius of **{_fmt(radius_cm)} cm** and a height of **{_fmt(height_cm)} cm**.\n\n"
        f"Calculate the **total surface area** of sheet metal required to manufacture one closed tin can.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Total Surface Area}} = 2\\pi r^2 + 2\\pi r h$. Round to 2 decimal places)*"
    )

    two_ends = round(2 * pi_val * (radius_cm ** 2), 2)
    curved_area = round(2 * pi_val * radius_cm * height_cm, 2)
    total_sa = round(two_ends + curved_area, 2)

    correct_ans = f"{_fmt(total_sa)} cm²"

    # Distractor: Only curved area (no lids)
    dist_curved = f"{_fmt(curved_area)} cm²"
    # Distractor: Only 1 end
    one_end = round(pi_val * (radius_cm ** 2) + curved_area, 2)
    dist_one = f"{_fmt(one_end)} cm²"

    custom_opts = [
        correct_ans,
        dist_curved,
        dist_one,
        f"{_fmt(round(total_sa + 25.0, 2))} cm²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the 2 circular circular ends [1 mark]:\n"
        f"2 Circular Ends = 2 × $\\pi \\times r^2$ = 2 × 3,142 × ({_fmt(radius_cm)})² = {_fmt(two_ends)} cm².\n\n"
        f"Step 2: Calculate the curved surface area [1 mark]:\n"
        f"Curved Area = 2 × $\\pi \\times r \\times h$ = 2 × 3,142 × {_fmt(radius_cm)} × {_fmt(height_cm)} = {_fmt(curved_area)} cm².\n\n"
        f"Step 3: Sum to determine total surface area [1 mark]:\n"
        f"Total SA = {_fmt(two_ends)} cm² + {_fmt(curved_area)} cm² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_19",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the area of 2 circular lids (2πr²) to the curved side area (2πrh).",
        tier_2=f"Lids = 2 × 3,142 × {radius_cm}² = {two_ends} cm². Curved = 2 × 3,142 × {radius_cm} × {height_cm} = {curved_area} cm².",
        tier_3=f"Total Surface Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Curved surface area of an open cylindrical concrete culvert / drainage pipe."""
    diameter_m = round(r.choice([0.6, 0.8, 1.0, 1.2]), 2)
    radius_m = round(diameter_m / 2.0, 3)
    pipe_len_m = round(r.choice([2.4, 3.0, 4.0, 5.0]), 1)
    pi_val = 3.142

    prompt = (
        f"A civil engineering contractor is laying an **open-ended hollow cylindrical concrete storm-water pipe**.\n"
        f"The pipe has an inner diameter of **{_fmt(diameter_m)} m** and a length of **{_fmt(pipe_len_m)} m**.\n\n"
        f"Calculate the **internal curved surface area** of the pipe that comes into contact with flowing storm-water.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Curved Surface Area}} = 2\\pi r h$ or $\\pi d h$. Round to 2 decimal places)*"
    )

    curved_sa = round(pi_val * diameter_m * pipe_len_m, 2)
    correct_ans = f"{_fmt(curved_sa)} m²"

    # Distractor: Included closed ends
    two_ends = round(2 * pi_val * (radius_m ** 2), 2)
    dist_closed = f"{_fmt(round(curved_sa + two_ends, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_closed,
        f"{_fmt(round(curved_sa / 2, 2))} m²",
        f"{_fmt(round(curved_sa + 4.2, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State formula for curved surface area of a hollow open cylinder [1 mark]:\n"
        f"Curved Surface Area = $\\pi \\times d \\times h$ (or 2 × $\\pi \\times r \\times h$).\n\n"
        f"Step 2: Substitute diameter and pipe length [1 mark]:\n"
        f"Curved Area = 3,142 × {_fmt(diameter_m)} m × {_fmt(pipe_len_m)} m.\n\n"
        f"Step 3: Stated answer with units [1 mark]:\n"
        f"Curved Surface Area = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_20",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Because the storm-water pipe is open at both ends, calculate only the curved area: π × d × length.",
        tier_2=f"Curved Area = 3,142 × {diameter_m} × {pipe_len_m}.",
        tier_3=f"Curved Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Surface area of an open-top cylindrical water trough / bucket."""
    radius_m = round(r.choice([0.4, 0.5, 0.6, 0.75]), 2)
    height_m = round(r.choice([0.6, 0.8, 1.0, 1.2]), 2)
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is galvanising an **open-top cylindrical livestock water trough** (has a bottom circular base, but NO top lid).\n"
        f"The trough has a radius of **{_fmt(radius_m)} m** and a depth (height) of **{_fmt(height_m)} m**.\n\n"
        f"Calculate the **exterior surface area** of the trough that will be coated.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Surface Area}} = \\pi r^2 + 2\\pi r h$. Round to 2 decimal places)*"
    )

    base_area = round(pi_val * (radius_m ** 2), 2)
    curved_area = round(2 * pi_val * radius_m * height_m, 2)
    total_sa = round(base_area + curved_area, 2)

    correct_ans = f"{_fmt(total_sa)} m²"

    # Distractor: Included top lid (2 bases)
    dist_with_lid = f"{_fmt(round(total_sa + base_area, 2))} m²"
    # Distractor: Only curved area
    dist_curved = f"{_fmt(curved_area)} m²"

    custom_opts = [
        correct_ans,
        dist_with_lid,
        dist_curved,
        f"{_fmt(round(total_sa + 1.5, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the single circular base [1 mark]:\n"
        f"Base = $\\pi \\times r^2$ = 3,142 × ({_fmt(radius_m)})² = {_fmt(base_area)} m².\n\n"
        f"Step 2: Calculate the curved surface area [1 mark]:\n"
        f"Curved Area = 2 × $\\pi \\times r \\times h$ = 2 × 3,142 × {_fmt(radius_m)} × {_fmt(height_m)} = {_fmt(curved_area)} m².\n\n"
        f"Step 3: Sum base and curved area [1 mark]:\n"
        f"Total Area = {_fmt(base_area)} m² + {_fmt(curved_area)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_21",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="An open-top cylinder includes only 1 circular base plus the curved wall: πr² + 2πrh.",
        tier_2=f"Base = 3,142 × {radius_m}² = {base_area} m². Curved = 2 × 3,142 × {radius_m} × {height_m} = {curved_area} m².",
        tier_3=f"Total Surface Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Tin can paper label area calculation (curved wall plus glue overlap)."""
    diameter_cm = round(r.choice([7.0, 8.0, 10.0]), 1)
    height_cm = round(r.choice([10.5, 11.0, 12.5]), 1)
    overlap_cm = 1.5  # cm glue flap overlap
    pi_val = 3.142

    prompt = (
        f"A packaging plant prints rectangular paper labels to wrap around cylindrical food cans.\n"
        f"Each can has a diameter of **{_fmt(diameter_cm)} cm** and a height of **{_fmt(height_cm)} cm**.\n"
        f"The label must wrap completely around the circumference of the can plus an extra **{_fmt(overlap_cm)} cm** overlap to allow for glue adhesion.\n\n"
        f"Calculate the **total area of paper** needed for one can label.\n"
        f"*(Use $\\pi = 3,142$. Formula: $\\text{{Label Length}} = (\\pi \\times d) + \\text{{overlap}}$; $\\text{{Label Area}} = \\text{{Length}} \\times \\text{{height}}$. Round to 2 decimal places)*"
    )

    circumference = round(pi_val * diameter_cm, 2)
    label_length = round(circumference + overlap_cm, 2)
    label_area = round(label_length * height_cm, 2)

    correct_ans = f"{_fmt(label_area)} cm²"

    # Distractor: Forgot overlap
    dist_no_overlap = f"{_fmt(round(circumference * height_cm, 2))} cm²"

    custom_opts = [
        correct_ans,
        dist_no_overlap,
        f"{_fmt(round(label_area / 2, 2))} cm²",
        f"{_fmt(round(label_area + 20.0, 2))} cm²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the circumference of the can [1 mark]:\n"
        f"Circumference = $\\pi \\times d$ = 3,142 × {_fmt(diameter_cm)} cm = {_fmt(circumference)} cm.\n\n"
        f"Step 2: Add the glue overlap to find total label length [1 mark]:\n"
        f"Label Length = {_fmt(circumference)} cm + {_fmt(overlap_cm)} cm = {_fmt(label_length)} cm.\n\n"
        f"Step 3: Multiply label length by can height [1 mark]:\n"
        f"Label Area = {_fmt(label_length)} cm × {_fmt(height_cm)} cm = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_22",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the can circumference (π × d), add the glue overlap, then multiply by the can height.",
        tier_2=f"Circumference = 3,142 × {diameter_cm} = {circumference} cm. Length = {circumference} + {overlap_cm} = {label_length} cm.",
        tier_3=f"Label Area = {label_length} × {height_cm} = {correct_ans}.",
        r=r,
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Painting the exterior curved side and top lid of a farm silo / cylindrical fuel tank."""
    radius_m = round(r.choice([1.5, 2.0, 2.5]), 1)
    height_m = round(r.choice([4.0, 5.0, 6.0]), 1)
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} needs to apply protective anti-rust paint to an exterior cylindrical diesel fuel tank on a farm.\n"
        f"The tank sits on a solid concrete foundation, so only the **curved vertical side** and the **flat circular top lid** will be painted.\n"
        f"The tank has a radius of **{_fmt(radius_m)} m** and a height of **{_fmt(height_m)} m**.\n\n"
        f"Calculate the **total paintable exterior surface area** of the tank.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Area}} = \\pi r^2 + 2\\pi r h$. Round to 2 decimal places)*"
    )

    lid_area = round(pi_val * (radius_m ** 2), 2)
    curved_area = round(2 * pi_val * radius_m * height_m, 2)
    total_area = round(lid_area + curved_area, 2)

    correct_ans = f"{_fmt(total_area)} m²"

    custom_opts = [
        correct_ans,
        f"{_fmt(round(total_area + lid_area, 2))} m²",  # Included bottom
        f"{_fmt(curved_area)} m²",  # Forgot lid
        f"{_fmt(round(total_area + 6.5, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the circular top lid [1 mark]:\n"
        f"Top Lid = $\\pi \\times r^2$ = 3,142 × ({_fmt(radius_m)})² = {_fmt(lid_area)} m².\n\n"
        f"Step 2: Calculate the curved cylindrical side area [1 mark]:\n"
        f"Curved Area = 2 × $\\pi \\times r \\times h$ = 2 × 3,142 × {_fmt(radius_m)} × {_fmt(height_m)} = {_fmt(curved_area)} m².\n\n"
        f"Step 3: Sum lid and curved side [1 mark]:\n"
        f"Total Paintable Area = {_fmt(lid_area)} m² + {_fmt(curved_area)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_23",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the top circular lid (πr²) plus the curved side wall (2πrh). The bottom is resting on concrete.",
        tier_2=f"Lid = {lid_area} m². Curved wall = {curved_area} m².",
        tier_3=f"Total = {correct_ans}.",
        r=r,
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Painting the internal walls and circular floor of a cylindrical splash pool."""
    diameter_m = round(r.choice([3.6, 4.2, 5.0]), 1)
    radius_m = round(diameter_m / 2.0, 2)
    depth_m = round(r.choice([1.1, 1.2, 1.35]), 2)
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"A municipal recreation centre contracts {name} to repaint the inside of a circular children's splash pool.\n"
        f"The pool has an interior diameter of **{_fmt(diameter_m)} m** and a uniform depth of **{_fmt(depth_m)} m**.\n"
        f"The painting job requires coating the **circular floor** and the **vertical curved inner wall**.\n\n"
        f"Calculate the **total internal surface area** that must be painted.\n"
        f"*(Use $\\pi = 3,142$. Round to 2 decimal places)*"
    )

    floor_area = round(pi_val * (radius_m ** 2), 2)
    wall_area = round(2 * pi_val * radius_m * depth_m, 2)
    total_pool_sa = round(floor_area + wall_area, 2)

    correct_ans = f"{_fmt(total_pool_sa)} m²"

    custom_opts = [
        correct_ans,
        f"{_fmt(round(total_pool_sa + floor_area, 2))} m²",
        f"{_fmt(wall_area)} m²",
        f"{_fmt(round(total_pool_sa + 4.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the radius and floor area [1 mark]:\n"
        f"Radius = {_fmt(diameter_m)} m ÷ 2 = {_fmt(radius_m)} m.\n"
        f"Floor Area = $\\pi \\times r^2$ = 3,142 × ({_fmt(radius_m)})² = {_fmt(floor_area)} m².\n\n"
        f"Step 2: Calculate the curved wall area [1 mark]:\n"
        f"Wall Area = 2 × $\\pi \\times r \\times h$ = 2 × 3,142 × {_fmt(radius_m)} × {_fmt(depth_m)} = {_fmt(wall_area)} m².\n\n"
        f"Step 3: Sum floor and wall area [1 mark]:\n"
        f"Total Interior Area = {_fmt(floor_area)} m² + {_fmt(wall_area)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_24",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Radius = diameter ÷ 2. Area = circular floor (πr²) + curved wall (2πrh).",
        tier_2=f"Floor = 3,142 × {radius_m}² = {floor_area} m². Wall = 2 × 3,142 × {radius_m} × {depth_m} = {wall_area} m².",
        tier_3=f"Total = {correct_ans}.",
        r=r,
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Thermal insulation jacket surface area for a cylindrical hot water geyser."""
    diameter_cm = round(r.choice([45.0, 50.0, 55.0]), 1)
    height_cm = round(r.choice([110.0, 125.0, 140.0]), 1)
    pi_val = 3.142

    prompt = (
        f"To reduce electricity consumption, Eskom recommends wrapping an insulating blanket jacket around a domestic hot water geyser.\n"
        f"The geyser is cylindrical with diameter **{_fmt(diameter_cm)} cm** and height **{_fmt(height_cm)} cm**.\n"
        f"The blanket covers the **entire curved circumference** of the geyser plus the **top circular cap** (pipes enter through the bottom).\n\n"
        f"Calculate the **area of thermal insulation blanket** needed in **square metres (m²)**.\n"
        f"*(Use $\\pi = 3,142$ and convert cm² to m² by dividing by 10 000. Round to 2 decimal places)*"
    )

    radius_cm = diameter_cm / 2.0
    top_cap_cm2 = pi_val * (radius_cm ** 2)
    curved_cm2 = 2 * pi_val * radius_cm * height_cm
    total_cm2 = top_cap_cm2 + curved_cm2
    total_m2 = round(total_cm2 / 10000.0, 2)

    correct_ans = f"{_fmt(total_m2)} m²"

    # Distractor: Divided by 100 instead of 10 000
    dist_div100 = f"{_fmt(round(total_cm2 / 100.0, 2))} m²"
    # Distractor: Closed ends
    closed_m2 = round((total_cm2 + top_cap_cm2) / 10000.0, 2)

    custom_opts = [
        correct_ans,
        dist_div100,
        f"{_fmt(closed_m2)} m²",
        f"{_fmt(round(total_m2 + 0.85, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area in cm² for top cap and curved sides [1 mark]:\n"
        f"Top Cap = $\\pi \\times r^2$ = 3,142 × ({_fmt(radius_cm)})² = {_fmt(top_cap_cm2, 2)} cm².\n"
        f"Curved Side = 2 × $\\pi \\times r \\times h$ = 2 × 3,142 × {_fmt(radius_cm)} × {_fmt(height_cm)} = {_fmt(curved_cm2, 2)} cm².\n"
        f"Total cm² = {_fmt(top_cap_cm2 + curved_cm2, 2)} cm².\n\n"
        f"Step 2: Convert cm² to m² by dividing by 10 000 (since 1 m² = 10 000 cm²) [1 mark]:\n"
        f"Area in m² = {_fmt(total_cm2, 2)} ÷ 10 000 = {_fmt(total_m2)} m².\n\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_25",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total area in cm² (top circle + curved wall), then convert to m² by dividing by 10 000.",
        tier_2=f"Total cm² = {top_cap_cm2:.1f} + {curved_cm2:.1f} = {total_cm2:.1f} cm². Divide by 10 000.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Cylindrical grain silo corrugated iron sheet requirements with sheet sizing."""
    diameter_m = round(r.choice([4.0, 5.0, 6.0]), 1)
    height_m = round(r.choice([5.0, 6.0, 8.0]), 1)
    sheet_width_m = 0.85  # effective cover width after overlap
    sheet_len_m = round(height_m / 2.0, 1)  # 2 rows of vertical sheets
    pi_val = 3.142

    prompt = (
        f"A Free State farmer is cladding the curved vertical walls of a circular grain silo with corrugated iron sheets.\n"
        f"The silo has a diameter of **{_fmt(diameter_m)} m** and a wall height of **{_fmt(height_m)} m**.\n"
        f"The circumference will be clad using 2 vertical tiers of corrugated iron sheets.\n"
        f"Each corrugated sheet has an effective coverage width of **0,85 m** after corrugation overlap.\n\n"
        f"Calculate the **circumference** of the silo and determine the **minimum number of sheets** needed per tier.\n"
        f"*(Use $\\pi = 3,142$. Round sheets up to the next whole sheet)*"
    )

    circumference = round(pi_val * diameter_m, 2)
    sheets_per_tier = int(round(circumference / sheet_width_m + 0.499))

    correct_ans = f"Circumference: {_fmt(circumference)} m; {sheets_per_tier} sheets per tier"

    custom_opts = [
        correct_ans,
        f"Circumference: {_fmt(circumference)} m; {sheets_per_tier - 4} sheets per tier",
        f"Circumference: {_fmt(round(circumference / 2, 2))} m; {sheets_per_tier} sheets per tier",
        f"Circumference: {_fmt(circumference)} m; {sheets_per_tier * 2} sheets per tier",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the silo circumference [1 mark]:\n"
        f"Circumference = $\\pi \\times d$ = 3,142 × {_fmt(diameter_m)} m = {_fmt(circumference)} m.\n\n"
        f"Step 2: Divide circumference by the effective sheet width [1 mark]:\n"
        f"Sheets = {_fmt(circumference)} m ÷ 0,85 m = {circumference / sheet_width_m:.2f} sheets.\n\n"
        f"Step 3: Round up to ensure complete coverage [1 mark]:\n"
        f"Sheets per tier = {sheets_per_tier} sheets.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_26",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Circumference = π × d. Then divide circumference by effective sheet width (0,85 m) and round up.",
        tier_2=f"Circumference = 3,142 × {diameter_m} = {circumference} m. Sheets = {circumference} ÷ 0,85.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Ratio of curved surface area to total surface area in low vs tall cylinders."""
    r_val = 2.0  # m
    h_val = 8.0  # m (tall cylinder)
    pi_val = 3.142

    prompt = (
        f"An industrial tank manufacturer compares the curved surface area and the end caps for a tall storage cylinder "
        f"with radius $r = 2\\text{{ m}}$ and height $h = 8\\text{{ m}}$.\n\n"
        f"Calculate what percentage of the **total surface area** is accounted for by the **curved wall** alone.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Formula}}: \\text{{Percentage}} = \\frac{{2\\pi r h}}{{2\\pi r^2 + 2\\pi r h}} \\times 100$. Round to 1 decimal place)*"
    )

    # 2*pi*r*h / (2*pi*r^2 + 2*pi*r*h) = h / (r + h) = 8 / (2 + 8) = 8 / 10 = 80.0%
    pct = round((h_val / (r_val + h_val)) * 100, 1)

    correct_ans = f"{_fmt(pct)}%"

    custom_opts = [
        correct_ans,
        f"{_fmt(round(100.0 - pct, 1))}%",
        f"{_fmt(round(pct / 2, 1))}%",
        f"{_fmt(round(pct + 10.0, 1))}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Notice that 2πr cancels out from the fraction [1 mark]:\n"
        f"Percentage = [h ÷ (r + h)] × 100%.\n\n"
        f"Step 2: Substitute radius = 2 m and height = 8 m [1 mark]:\n"
        f"Ratio = 8 ÷ (2 + 8) = 8 ÷ 10 = 0,80.\n\n"
        f"Step 3: Convert to percentage [1 mark]:\n"
        f"Curved Area Percentage = 0,80 × 100% = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_27",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The proportion of curved area simplifies to h ÷ (r + h).",
        tier_2=f"h ÷ (r + h) = 8 ÷ (2 + 8) = 8 ÷ 10 = 0,8.",
        tier_3=f"Percentage = {correct_ans}.",
        r=r,
    )
