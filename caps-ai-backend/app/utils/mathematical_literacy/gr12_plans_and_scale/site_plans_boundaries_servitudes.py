"""Subskills 33-40: Site Plans, Boundaries & Municipal Bylaws for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Reading erf boundary dimensions and calculating stand area on 1:500 site plan."""
    scale = 500
    plan_l_cm = r.choice([6.0, 7.0, 8.0])
    plan_w_cm = r.choice([4.0, 4.5, 5.0])

    real_l_m = (plan_l_cm * scale) / 100.0
    real_w_m = (plan_w_cm * scale) / 100.0
    erf_area_m2 = real_l_m * real_w_m

    prompt = (
        f"Refer to the municipal site cadastral plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A rectangular residential erf (stand) has boundary lengths of {_fmt(plan_l_cm, 1)} cm along the street frontage and {_fmt(plan_w_cm, 1)} cm along the side on paper.\n\n"
        f"Calculate the actual area of the erf in square metres (m²)."
    )
    d_spec_33 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "dimensions": {"width_m": 25, "length_m": 40},
        "rooms": [{"name": "Stand", "width": 25, "length": 40}],
        "title": f"Erf Stand Plan ({_fmt(plan_l_cm, 1)} cm × {_fmt(plan_w_cm, 1)} cm)",
        "boundary": {"width": plan_w_cm * 10, "length": plan_l_cm * 10},
        "annotations": [{"text": f"Front: {_fmt(plan_l_cm, 1)} cm"}, {"text": f"Side: {_fmt(plan_w_cm, 1)} cm"}],
    }

    correct_ans = f"{_fmt(erf_area_m2, 0)} m²"
    custom_opts = [
        correct_ans,
        f"{_fmt(erf_area_m2 * 1.5, 0)} m²",
        f"{_fmt(erf_area_m2 / 2, 0)} m²",
        f"{_fmt(plan_l_cm * plan_w_cm * 10, 0)} m²",
    ]

    t1 = f"Calculate the real length: {_fmt(plan_l_cm, 1)} cm × {scale} ÷ 100 = {_fmt(real_l_m, 1)} m."
    t2 = f"Calculate the real width: {_fmt(plan_w_cm, 1)} cm × {scale} ÷ 100 = {_fmt(real_w_m, 1)} m."
    t3 = f"Erf Area = {_fmt(real_l_m, 1)} m × {_fmt(real_w_m, 1)} m = {_fmt(erf_area_m2, 0)} m²."

    explanation = [
        f"Step 1: Real frontage length = {_fmt(plan_l_cm, 1)} cm × {scale} = {_fmt(plan_l_cm * scale, 0)} cm = {_fmt(real_l_m, 1)} m [1 Mark: Method].",
        f"Step 2: Real side width = {_fmt(plan_w_cm, 1)} cm × {scale} = {_fmt(plan_w_cm * scale, 0)} cm = {_fmt(real_w_m, 1)} m [1 Mark: Method].",
        f"Step 3: Total erf area = {_fmt(real_l_m, 1)} m × {_fmt(real_w_m, 1)} m = {_fmt(erf_area_m2, 0)} m² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_33",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_33,
    )


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Calculating building footprint coverage percentage against municipal limit (max 50%)."""
    erf_area_m2 = r.choice([600.0, 750.0, 800.0, 1000.0])
    house_footprint_m2 = r.choice([180.0, 220.0, 280.0])
    garage_footprint_m2 = r.choice([40.0, 50.0, 60.0])
    total_footprint_m2 = house_footprint_m2 + garage_footprint_m2

    coverage_pct = (total_footprint_m2 / erf_area_m2) * 100.0
    max_bylaw_pct = 50.0
    compliant = coverage_pct <= max_bylaw_pct

    status = (
        f"{_fmt(coverage_pct, 1)}% (Compliant: ≤ 50% municipal maximum coverage)"
        if compliant
        else f"{_fmt(coverage_pct, 1)}% (Non-compliant: exceeds 50% municipal maximum coverage)"
    )

    prompt = (
        f"Refer to the site plan and building footprint shown in the diagram. "
        f"Municipal town planning regulations dictate that total building coverage on a suburban stand "
        f"may NOT exceed 50% of the total erf area.\n"
        f"A homeowner plans to build on an erf measuring {_fmt(erf_area_m2, 0)} m² with dwelling footprint {_fmt(house_footprint_m2, 0)} m² "
        f"and double garage footprint {_fmt(garage_footprint_m2, 0)} m².\n\n"
        f"Calculate the site coverage percentage and state whether the plan complies with municipal bylaws."
    )
    d_spec_34 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "dimensions": {"width_m": 25, "length_m": 40},
        "rooms": [{"name": "Stand", "width": 25, "length": 40}],
        "title": f"Erf Building Footprint ({int(erf_area_m2)} m² Stand)",
        "boundary": {"width": 80, "length": 100},
        "buildings": [{"name": "Dwelling", "area": house_footprint_m2}, {"name": "Garage", "area": garage_footprint_m2}],
    }

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"{_fmt((house_footprint_m2 / erf_area_m2) * 100.0, 1)}% (Compliant: excludes garage)",
        f"{_fmt(coverage_pct * 1.2, 1)}% (Non-compliant: exceeds 50% limit)",
        f"{_fmt(coverage_pct * 0.8, 1)}% (Compliant: ≤ 50% municipal maximum coverage)",
    ]

    t1 = f"Add the dwelling and garage footprints: {_fmt(house_footprint_m2, 0)} + {_fmt(garage_footprint_m2, 0)} = {_fmt(total_footprint_m2, 0)} m²."
    t2 = f"Divide total footprint by erf area ({_fmt(erf_area_m2, 0)} m²) and multiply by 100."
    t3 = f"Coverage % = ({_fmt(total_footprint_m2, 0)} ÷ {_fmt(erf_area_m2, 0)}) × 100 = {_fmt(coverage_pct, 1)}%. Compare to 50%."

    explanation = [
        f"Step 1: Calculate total built footprint: {_fmt(house_footprint_m2, 0)} + {_fmt(garage_footprint_m2, 0)} = {_fmt(total_footprint_m2, 0)} m² [1 Mark: Method].",
        f"Step 2: Calculate coverage percentage: ({_fmt(total_footprint_m2, 0)} ÷ {_fmt(erf_area_m2, 0)}) × 100 = {_fmt(coverage_pct, 1)}% [1 Mark: Method].",
        f"Step 3: State percentage and compliance: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_34",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_34,
    )


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Checking municipal building line setback compliance (front 4.5 m, sides 2.0 m)."""
    scale = 200
    # Standard front setback = 4.5 m (4 500 mm). At 1:200 = 22.5 mm = 2.25 cm
    # Side setback = 2.0 m (2 000 mm). At 1:200 = 10.0 mm = 1.0 cm
    measured_front_cm = r.choice([1.8, 2.3, 2.8])  # 3.6 m, 4.6 m, 5.6 m
    actual_front_m = (measured_front_cm * scale) / 100.0

    compliant = actual_front_m >= 4.5
    status = (
        f"Compliant: actual front setback is {_fmt(actual_front_m, 2)} m (≥ 4,50 m street building line)"
        if compliant
        else f"Non-compliant: actual front setback is {_fmt(actual_front_m, 2)} m (< 4,50 m street building line encroachment)"
    )

    prompt = (
        f"Refer to the site development plan shown in the diagram (scale ratio 1 : {scale}). "
        f"Municipal scheme bylaws establish a mandatory street building line setback of 4,50 m. "
        f"On the plan, the distance between the street boundary peg and the closest external wall measures {_fmt(measured_front_cm, 1)} cm on paper.\n\n"
        f"Determine whether this proposal complies with the street building line setback requirement."
    )
    d_spec_35 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "dimensions": {"width_m": 25, "length_m": 40},
        "rooms": [{"name": "Stand", "width": 25, "length": 40}],
        "title": f"Building Line Setbacks (Scale 1 : {scale})",
        "boundary": {"width": 80, "length": 100},
        "setback": {"front_cm": measured_front_cm, "real_front_m": actual_front_m},
    }

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"Compliant: all street setbacks greater than 2,00 m are automatically approved",
        f"Non-compliant: regulations require a minimum front setback of 10,00 m for all residential homes",
        f"Compliant: {_fmt(measured_front_cm, 1)} cm on a site plan automatically represents 5,00 m",
    ]

    t1 = f"Calculate actual front setback: {_fmt(measured_front_cm, 1)} cm × {scale} = {_fmt(measured_front_cm * scale, 0)} cm = {_fmt(actual_front_m, 2)} m."
    t2 = f"Compare {_fmt(actual_front_m, 2)} m against the mandatory 4,50 m building line."
    t3 = f"{status}."

    explanation = [
        f"Step 1: Calculate actual ground distance: {_fmt(measured_front_cm, 1)} cm × {scale} = {_fmt(measured_front_cm * scale, 0)} cm = {_fmt(actual_front_m, 2)} m [1 Mark: Method].",
        f"Step 2: Compare with mandatory 4,50 m municipal building line [1 Mark: Method].",
        f"Step 3: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_35",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_35,
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Municipal sewer / stormwater servitude easement clearance calculation."""
    stand_depth_m = r.choice([30.0, 35.0, 40.0])
    servitude_width_m = 2.0  # 2.0 m municipal sewer servitude along rear boundary
    house_rear_setback_m = r.choice([1.5, 2.5, 3.0])

    encroaching = house_rear_setback_m < servitude_width_m
    status = (
        f"Encroaching by {_fmt(servitude_width_m - house_rear_setback_m, 2)} m: illegal to build within the 2,0 m municipal servitude"
        if encroaching
        else f"Clear of servitude: building is positioned {_fmt(house_rear_setback_m - servitude_width_m, 2)} m outside the 2,0 m municipal easement"
    )

    prompt = (
        f"A municipal sewer servitude of 2,00 m runs across the entire rear boundary of a residential property.\n"
        f"No permanent building, swimming pool, or foundation may be constructed over a registered municipal servitude.\n"
        f"A homeowner proposes building an entertainment lapa located {_fmt(house_rear_setback_m, 2)} m from the rear boundary fence.\n\n"
        f"Evaluate whether this construction is legally permitted without municipal servitude relaxation."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        "Permitted: all lapas with thatch or timber poles are exempt from servitude restrictions",
        "Illegal: servitudes extend 10,0 m from every boundary wall",
        "Permitted: the homeowner owns the entire erf and can build anywhere on the property",
    ]

    t1 = f"Compare the proposed structure distance ({_fmt(house_rear_setback_m, 2)} m) to the servitude width (2,00 m)."
    t2 = "If the building is closer to the boundary than 2,00 m, it encroaches onto the servitude."
    t3 = f"{status}."

    explanation = [
        f"Step 1: Identify registered servitude width = 2,00 m from boundary [1 Mark: Method].",
        f"Step 2: Compare proposed lapa distance ({_fmt(house_rear_setback_m, 2)} m) against the 2,00 m servitude boundary [1 Mark: Method].",
        f"Step 3: State the legal and spatial conclusion: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_36",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Driveway vehicular turning circle radius and access gate width."""
    # Standard emergency vehicle / passenger car turning radius: outer radius = 6.0 m
    # Turning head circle diameter = 12.0 m
    turning_radius_m = 6.0
    turning_diameter_m = 2 * turning_radius_m
    scale = 200
    plan_diameter_cm = (turning_diameter_m * 100.0) / scale

    turning_radius_m = r.choice([5.0, 6.0, 7.5])
    turning_diameter_m = 2 * turning_radius_m
    scale = r.choice([100, 200, 250])
    plan_diameter_cm = (turning_diameter_m * 100.0) / scale
    prompt = (
        f"Refer to the site plan shown in the diagram (scale ratio 1 : {scale}). "
        f"To allow passenger vehicles to turn around on site, a circular turning head has an outer radius of {_fmt(turning_radius_m, 1)} m.\n\n"
        f"What is the DIAMETER of this vehicular turning circle on the scale drawing, in centimetres?"
    )
    d_spec_37 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "dimensions": {"width_m": 25, "length_m": 40},
        "rooms": [{"name": "Stand", "width": 25, "length": 40}],
        "title": f"Driveway Turning Circle (Scale 1 : {scale})",
        "boundary": {"width": 80, "length": 100},
        "turning_circle": {"radius_m": turning_radius_m, "diameter_m": turning_diameter_m, "plan_cm": plan_diameter_cm},
    }

    correct_ans = f"{_fmt(plan_diameter_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(plan_diameter_cm / 2, 1)} cm",
        f"{_fmt(plan_diameter_cm * 2, 1)} cm",
        f"{_fmt(turning_radius_m, 1)} cm",
    ]

    t1 = f"Calculate the ground diameter: Diameter = 2 × Radius = 2 × {_fmt(turning_radius_m, 1)} m = {_fmt(turning_diameter_m, 1)} m."
    t2 = f"Convert to centimetres: {_fmt(turning_diameter_m, 1)} m × 100 = {_fmt(turning_diameter_m * 100, 0)} cm."
    t3 = f"Divide by scale denominator ({scale}): {_fmt(turning_diameter_m * 100, 0)} ÷ {scale} = {_fmt(plan_diameter_cm, 1)} cm."

    explanation = [
        f"Step 1: Calculate actual ground diameter: 2 × {_fmt(turning_radius_m, 1)} m = {_fmt(turning_diameter_m, 1)} m = {_fmt(turning_diameter_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Apply scale 1 : {scale}: {_fmt(turning_diameter_m * 100, 0)} cm ÷ {scale} [1 Mark: Method].",
        f"Step 3: Diameter on site plan = {_fmt(plan_diameter_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_37,
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Boundary fence / wall perimeter calculation deducting driveway and pedestrian gates."""
    erf_l_m = r.choice([30.0, 35.0, 40.0])
    erf_w_m = r.choice([20.0, 25.0])
    driveway_gate_w_m = 3.5
    pedestrian_gate_w_m = 1.0

    total_erf_perimeter_m = 2 * (erf_l_m + erf_w_m)
    net_fence_perimeter_m = total_erf_perimeter_m - (driveway_gate_w_m + pedestrian_gate_w_m)

    prompt = (
        f"Refer to the property boundary diagram shown. "
        f"A homeowner is erecting a perimeter security wall around a property measuring {_fmt(erf_l_m, 1)} m long by {_fmt(erf_w_m, 1)} m wide, "
        f"with driveway gate {_fmt(driveway_gate_w_m, 1)} m and pedestrian gate {_fmt(pedestrian_gate_w_m, 1)} m.\n\n"
        f"Calculate the TOTAL net linear metres of brick wall to be constructed."
    )
    d_spec_38 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "dimensions": {"width_m": 25, "length_m": 40},
        "rooms": [{"name": "Stand", "width": 25, "length": 40}],
        "title": f"Erf Boundary Fence ({int(erf_l_m)} m × {int(erf_w_m)} m)",
        "boundary": {"width": erf_w_m, "length": erf_l_m},
        "gates": [{"name": "Driveway", "width": driveway_gate_w_m}, {"name": "Pedestrian", "width": pedestrian_gate_w_m}],
    }

    correct_ans = f"{_fmt(net_fence_perimeter_m, 1)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(total_erf_perimeter_m, 1)} m",
        f"{_fmt(net_fence_perimeter_m - 5.0, 1)} m",
        f"{_fmt((erf_l_m + erf_w_m), 1)} m",
    ]

    t1 = f"Calculate the full rectangular perimeter: 2 × ({_fmt(erf_l_m, 1)} + {_fmt(erf_w_m, 1)})."
    t2 = f"Deduct the gate openings: {_fmt(driveway_gate_w_m, 1)} m + {_fmt(pedestrian_gate_w_m, 1)} m = 4,5 m."
    t3 = f"Full perimeter = {_fmt(total_erf_perimeter_m, 1)} m. Net wall = {_fmt(total_erf_perimeter_m, 1)} - 4,5 = {_fmt(net_fence_perimeter_m, 1)} m."

    explanation = [
        f"Step 1: Calculate total erf perimeter: 2 × ({_fmt(erf_l_m, 1)} + {_fmt(erf_w_m, 1)}) = {_fmt(total_erf_perimeter_m, 1)} m [1 Mark: Method].",
        f"Step 2: Total gate opening deduction: {_fmt(driveway_gate_w_m, 1)} m + {_fmt(pedestrian_gate_w_m, 1)} m = 4,5 m [1 Mark: Method].",
        f"Step 3: Net boundary wall length = {_fmt(total_erf_perimeter_m, 1)} m - 4,5 m = {_fmt(net_fence_perimeter_m, 1)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_38",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_38,
    )


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Orientation of living rooms towards True North for passive solar heating."""
    prompt = (
        "In South Africa (located in the Southern Hemisphere), environmental building regulations (SANS 10400-XA) "
        "strongly recommend that primary living areas (lounges and main bedrooms) be orientated with their largest "
        "glazed windows facing TRUE NORTH.\n\n"
        "What is the physical and scientific justification for this orientation?"
    )

    correct_ans = "The sun arcs across the northern sky in the Southern hemisphere; North-facing windows capture maximum warm winter sunlight and avoid harsh morning/afternoon summer heat"
    custom_opts = [
        correct_ans,
        "North-facing rooms are protected from all atmospheric wind in South Africa",
        "It aligns with magnetic field lines to prevent static electrical interference in appliances",
        "It is an ancient superstition with zero effect on thermal temperature or energy consumption",
    ]

    t1 = "Recall solar path dynamics in the Southern Hemisphere."
    t2 = "In winter, the sun is low in the northern sky, shining directly into North-facing rooms to provide natural heating."
    t3 = "The scientific reason is maximizing passive solar winter warmth and natural daylight."

    explanation = [
        f"Step 1: Understand Southern hemisphere solar geometry: the sun traverses the northern sky [1 Mark: Method].",
        f"Step 2: Recognize seasonal variation: low winter sun penetrates deep into North rooms; high summer sun is blocked by roof eaves [1 Mark: Method].",
        f"Step 3: State the energy efficiency and thermal justification [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_39",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Stormwater run-off drainage slope away from foundation walls."""
    # SANS 10400 standard: Ground must slope away from building at minimum 1:50 (2%) for first 1.5 m (or 50 mm fall over 1 m)
    run_distance_m = r.choice([1.5, 2.0, 2.5])
    slope_gradient = 0.02  # 2% or 1:50
    min_vertical_fall_mm = (run_distance_m * slope_gradient) * 1000.0

    prompt = (
        f"Under South African Building Regulations (SANS 10400 Part F: Site Drainage), the finished ground level "
        f"surrounding a concrete foundation slab must fall away from the building at a MINIMUM slope gradient of 1 : 50 (2%) "
        f"to prevent rainwater ponding and foundation subsiding.\n\n"
        f"Over a horizontal distance of {_fmt(run_distance_m, 1)} m away from the external wall, "
        f"what is the MINIMUM vertical ground level drop (fall) required in millimetres (mm)?"
    )

    correct_ans = f"{_fmt(min_vertical_fall_mm, 0)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(min_vertical_fall_mm * 2, 0)} mm",
        f"{_fmt(min_vertical_fall_mm / 2, 0)} mm",
        f"{_fmt(run_distance_m * 10, 0)} mm",
    ]

    t1 = "Convert the horizontal distance to millimetres (multiply by 1 000)."
    t2 = f"Divide the horizontal millimetres by 50 (since the gradient is 1 : 50)."
    t3 = f"Horizontal = {_fmt(run_distance_m, 1)} m × 1 000 = {_fmt(run_distance_m * 1000, 0)} mm. Fall = {_fmt(run_distance_m * 1000, 0)} ÷ 50 = {_fmt(min_vertical_fall_mm, 0)} mm."

    explanation = [
        f"Step 1: Convert run to mm: {_fmt(run_distance_m, 1)} m × 1 000 = {_fmt(run_distance_m * 1000, 0)} mm [1 Mark: Method].",
        f"Step 2: Apply gradient 1 : 50: Fall = Run ÷ 50 = {_fmt(run_distance_m * 1000, 0)} mm ÷ 50 [1 Mark: Method].",
        f"Step 3: Minimum required vertical ground fall = {_fmt(min_vertical_fall_mm, 0)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_40",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )
