"""Grade 9 Mathematics - Area and Perimeter of 2D Shapes Archetypes 26 to 50
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Area and perimeter of 2D shapes
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/03. Area and perimeter of 2D shapes.md
  - Chapter 14: Annuli, sectors, composite figures, shaded regions, unit conversions
    (linear and area, hectares), scaling factor effects ($k$ and $k^2$), real-world SA
    applications (fencing, tiling, painting), and diagnostic error analysis.

Covers Archetypes 26 - 50:
  26: Area of circular ring (annulus / washer: pi*(R^2 - r^2))
  27: Arc length of circle sector
  28: Area of circle sector
  29: Perimeter of L-shaped composite figure
  30: Area of L-shaped composite figure
  31: Area of T-shaped or U-shaped composite polygon
  32: Composite rectangle with triangular gable area
  33: Composite rectangle with semicircular end perimeter (running track / Norman window)
  34: Composite rectangle with semicircular end area
  35: Shaded area: square minus inscribed circle
  36: Shaded area: circle minus inscribed square
  37: Shaded area: rectangle minus internal rectangle border path
  38: Linear unit conversions: mm, cm, m, km
  39: Area unit conversions: mm² to cm² and m²
  40: Area unit conversions: m² to hectares and km²
  41: Effect of multiplying dimensions by factor k on perimeter (factor k)
  42: Effect of multiplying dimensions by factor k on area (factor k²)
  43: Calculate linear scale factor k given ratio of areas (k = sqrt(ratio))
  44: Contextual real-world fencing cost perimeter application
  45: Contextual real-world turfing or tiling cost area application
  46: Contextual wall painting area deducting door and window openings
  47: Diagnostic error analysis: confusing perimeter and area
  48: Diagnostic error analysis: using slanted side as perpendicular height
  49: Diagnostic error analysis: omitting diameter boundary in semicircle perimeter
  50: Compound multi-stage park layout synthesis challenge
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.area_perimeter_2d_svg import (
    draw_circle_figure_svg,
    draw_composite_shape_svg,
)


def arch_26_area_of_circular_ring_annulus_washer(rng: random.Random) -> Dict[str, Any]:
    """Area of circular ring / annulus: A = pi * (R^2 - r^2)."""
    # Use Pythagorean triple like 3-4-5 or 6-8-10 so R^2 - r^2 is clean
    # R=14, r=7 => R^2 - r^2 = 196 - 49 = 147 => (22/7)*147 = 22*21 = 462
    r_in, r_out, area = rng.choice([
        (7, 14, 462),
        (7, 21, 1232),
        (14, 21, 770),
    ])
    seed_val = rng.randint(1000, 999999)
    svg = draw_circle_figure_svg(r_out, kind="annulus", r_inner=r_in, label_inner=f"r = {r_in} cm", label_outer=f"R = {r_out} cm", seed=seed_val)

    prompt = (
        f"Refer to the circular ring (annulus / washer) below with inner radius **${r_in}\\text{{ cm}}$** "
        f"and outer radius **${r_out}\\text{{ cm}}$**:\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area of the shaded ring** in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "26_area_of_circular_ring_annulus_washer",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = pi * (R^2 - r^2)", "marks": 1},
            {"step": f"Calculate: (22/7) * ({r_out}^2 - {r_in}^2) = (22/7) * ({r_out**2 - r_in**2}) = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Subtract the inner circle area from the outer circle area: $\\text{Area} = \\pi R^2 - \\pi r^2 = \\pi(R^2 - r^2)$.",
            f"Calculate ${r_out}^2 - {r_in}^2 = {r_out**2} - {r_in**2} = {r_out**2 - r_in**2}$.",
            f"Multiply by $\\frac{{22}}{{7}}$: $\\text{{Area}} = {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["annulus_squared_difference_error", "subtracted_radii_before_squaring"],
    }


def arch_27_arc_length_of_circle_sector(rng: random.Random) -> Dict[str, Any]:
    """Arc length of sector: s = (theta / 360) * 2 * pi * r."""
    # theta in [60, 90, 120, 180]
    # For theta = 90, r = 14 => (90/360) * 2 * (22/7) * 14 = (1/4) * 88 = 22
    # For theta = 60, r = 21 => (60/360) * 2 * (22/7) * 21 = (1/6) * 132 = 22
    # For theta = 120, r = 21 => (120/360) * 132 = 44
    theta, r, arc = rng.choice([
        (90, 14, 22),
        (60, 21, 22),
        (120, 21, 44),
        (180, 14, 44),
    ])

    prompt = (
        f"A circular sector has a central angle of **${theta}^\\circ$** and a radius of **${r}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **length of the curved arc** in centimetres."
    )

    return {
        "subskill": "27_arc_length_of_circle_sector",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(arc),
        "sample_answer": f"{arc} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State arc length formula: Arc = (theta / 360) * 2 * pi * r", "marks": 1},
            {"step": f"Calculate: ({theta}/360) * 2 * (22/7) * {r} = {arc} cm", "marks": 1},
        ],
        "hints": [
            "Formula for arc length: $\\text{Arc} = \\frac{\\theta}{360^\\circ} \\times 2\\pi r$.",
            f"Fraction of circle: $\\frac{{{theta}}}{{360}} = \\frac{{{theta // math.gcd(theta, 360)}}}{{{360 // math.gcd(theta, 360)}}}$.",
            f"Arc length $= {arc}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["sector_arc_length_formula_error", "fraction_of_circumference_error"],
    }


def arch_28_area_of_circle_sector(rng: random.Random) -> Dict[str, Any]:
    """Area of sector: A = (theta / 360) * pi * r^2."""
    theta, r, area = rng.choice([
        (90, 14, 154),   # (1/4) * (22/7) * 196 = (1/4) * 616 = 154
        (60, 21, 231),   # (1/6) * (22/7) * 441 = (1/6) * 1386 = 231
        (120, 21, 462),  # (1/3) * 1386 = 462
        (45, 28, 308),   # (1/8) * (22/7) * 784 = (1/8) * 2464 = 308
    ])

    prompt = (
        f"A sector of a circle has a central angle of **${theta}^\\circ$** and a radius of **${r}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area of the sector** in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "28_area_of_circle_sector",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State sector area formula: Area = (theta / 360) * pi * r^2", "marks": 1},
            {"step": f"Calculate: ({theta}/360) * (22/7) * {r}^2 = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Formula for area of a sector: $\\text{Area} = \\frac{\\theta}{360^\\circ} \\times \\pi r^2$.",
            f"Full circle area: $\\frac{{22}}{{7}} \\times {r}^2 = {area * 360 // theta}\\text{{ cm}}^2$.",
            f"Multiply by fraction: $\\frac{{{theta}}}{{360}} \\times {area * 360 // theta} = {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["sector_area_formula_error", "confused_arc_length_with_sector_area"],
    }


def arch_29_perimeter_of_l_shaped_composite_figure(rng: random.Random) -> Dict[str, Any]:
    """Perimeter of L-shaped figure: P = 2*(W + H)."""
    w = rng.randint(12, 22)
    h = rng.randint(10, 18)
    # L-shape perimeter is always equal to the perimeter of the bounding rectangle: 2*(W + H)
    perimeter = 2 * (w + h)
    cut_w = rng.randint(4, w - 4)
    cut_h = rng.randint(4, h - 4)
    seed_val = rng.randint(1000, 999999)
    svg = draw_composite_shape_svg("l_shape", w, h, label_w=f"Total Width = {w} m", label_h=f"Total Height = {h} m", extra_label=f"Cutout: {cut_w}m x {cut_h}m", seed=seed_val)

    prompt = (
        f"Refer to the L-shaped floor plan below. The overall total width is **${w}\\text{{ m}}$** and the "
        f"overall total height is **${h}\\text{{ m}}$**:\n\n"
        f"Calculate the **total perimeter** of the L-shaped floor plan in metres."
    )

    return {
        "subskill": "29_perimeter_of_l_shaped_composite_figure",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that sum of horizontal and vertical steps equals 2 * (Width + Height)", "marks": 1},
            {"step": f"Calculate: 2 * ({w} + {h}) = 2 * {w + h} = {perimeter} metres", "marks": 1},
        ],
        "hints": [
            "In an L-shaped figure with perpendicular corners, the sum of all horizontal edges is $2 \\times \\text{Width}$, and vertical edges is $2 \\times \\text{Height}$.",
            f"Perimeter $= 2(W + H) = 2({w} + {h})$.",
            f"Perimeter $= {perimeter}\\text{{ m}}$.",
        ],
        "misconception_tags": ["l_shape_perimeter_inner_edge_subtraction_error"],
    }


def arch_30_area_of_l_shaped_composite_figure(rng: random.Random) -> Dict[str, Any]:
    """Area of L-shaped figure: outer rectangle minus cutout."""
    w = rng.randint(14, 22)
    h = rng.randint(12, 18)
    cut_w = rng.randint(5, w - 5)
    cut_h = rng.randint(4, h - 4)
    area = (w * h) - (cut_w * cut_h)
    seed_val = rng.randint(1000, 999999)
    svg = draw_composite_shape_svg("l_shape", w, h, label_w=f"{w} m", label_h=f"{h} m", extra_label=f"Cutout: {cut_w}m x {cut_h}m", seed=seed_val)

    prompt = (
        f"An L-shaped room has overall bounding dimensions of **${w}\\text{{ m}} \\times {h}\\text{{ m}}$**.\n"
        f"A rectangular corner cutout measuring **${cut_w}\\text{{ m}} \\times {cut_h}\\text{{ m}}$** is removed:\n\n"
        f"Calculate the **area** of the room in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "30_area_of_l_shaped_composite_figure",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate bounding rectangle area: {w} * {h} = {w * h} m^2", "marks": 1},
            {"step": f"Calculate cutout area: {cut_w} * {cut_h} = {cut_w * cut_h} m^2", "marks": 1},
            {"step": f"Subtract: {w * h} - {cut_w * cut_h} = {area} m^2", "marks": 1},
        ],
        "hints": [
            "Use the subtraction method: $\\text{Area} = \\text{Bounding Rectangle} - \\text{Corner Cutout}$.",
            f"Bounding area $= {w} \\times {h} = {w * h}\\text{{ m}}^2$. Cutout $= {cut_w} \\times {cut_h} = {cut_w * cut_h}\\text{{ m}}^2$.",
            f"Net area $= {w * h} - {cut_w * cut_h} = {area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["composite_area_cutout_addition_instead_of_subtraction"],
    }


def arch_31_area_of_t_shaped_or_u_shaped_composite_polygon(rng: random.Random) -> Dict[str, Any]:
    """Area of T-shaped polygon split into top bar and stem."""
    bar_l = rng.randint(12, 18)
    bar_w = rng.randint(3, 5)
    stem_h = rng.randint(6, 12)
    stem_w = rng.randint(4, 6)
    area = (bar_l * bar_w) + (stem_h * stem_w)

    prompt = (
        f"A T-shaped paved area consists of two non-overlapping rectangles:\n"
        f"- The top horizontal bar measures **${bar_l}\\text{{ m}} \\times {bar_w}\\text{{ m}}$**.\n"
        f"- The vertical stem measures **${stem_h}\\text{{ m}} \\times {stem_w}\\text{{ m}}$**.\n\n"
        f"Calculate the **total area** of the T-shaped paved region in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "31_area_of_t_shaped_or_u_shaped_composite_polygon",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(area),
        "sample_answer": f"{area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate top bar area: {bar_l} * {bar_w} = {bar_l * bar_w} m^2", "marks": 1},
            {"step": f"Calculate stem area: {stem_h} * {stem_w} = {stem_h * stem_w} m^2", "marks": 1},
            {"step": f"Add areas: {bar_l * bar_w} + {stem_h * stem_w} = {area} m^2", "marks": 1},
        ],
        "hints": [
            "Divide the composite shape into two simple rectangles and add their areas.",
            f"Top bar: ${bar_l} \\times {bar_w} = {bar_l * bar_w}$. Stem: ${stem_h} \\times {stem_w} = {stem_h * stem_w}$.",
            f"Total area $= {bar_l * bar_w} + {stem_h * stem_w} = {area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["composite_shape_partitioning_error"],
    }


def arch_32_composite_rectangle_with_triangular_gable_area(rng: random.Random) -> Dict[str, Any]:
    """Area of house side wall (rectangle + triangular roof gable)."""
    w = rng.choice([6, 8, 10, 12])
    h_wall = rng.randint(4, 8)
    h_roof = rng.choice([2, 3, 4, 5])
    area_rect = w * h_wall
    area_tri = (w * h_roof) // 2
    total_area = area_rect + area_tri

    prompt = (
        f"The end wall of a building is shaped as a rectangle surmounted by a triangular roof gable:\n"
        f"- The rectangular wall has width **${w}\\text{{ m}}$** and height **${h_wall}\\text{{ m}}$**.\n"
        f"- The triangular gable has base **${w}\\text{{ m}}$** and perpendicular height **${h_roof}\\text{{ m}}$**.\n\n"
        f"Calculate the **total surface area** of the wall in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "32_composite_rectangle_with_triangular_gable_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(total_area),
        "sample_answer": f"{total_area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate rectangle area: {w} * {h_wall} = {area_rect} m^2", "marks": 1},
            {"step": f"Calculate triangle gable area: 1/2 * {w} * {h_roof} = {area_tri} m^2", "marks": 1},
            {"step": f"Add: {area_rect} + {area_tri} = {total_area} m^2", "marks": 1},
        ],
        "hints": [
            "Calculate the area of the rectangle and the triangle separately, then add them together.",
            f"Wall area $= {w} \\times {h_wall} = {area_rect}\\text{{ m}}^2$.",
            f"Roof gable area $= \\frac{{1}}{{2}} \\times {w} \\times {h_roof} = {area_tri}\\text{{ m}}^2$.",
            f"Total area $= {area_rect} + {area_tri} = {total_area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["forgot_to_halve_gable_triangle_area"],
    }


def arch_33_composite_rectangle_with_semicircular_end_perimeter(rng: random.Random) -> Dict[str, Any]:
    """Perimeter of running track (rectangle + two semicircular ends): P = 2*L + pi*d."""
    # Two semicircles form 1 full circle circumference: C = pi * d = 22 * 2k = 44k when d = 14k
    k = rng.choice([1, 2])
    d = 14 * k
    length = rng.randint(40, 80)
    circle_c = 44 * k
    total_p = 2 * length + circle_c
    seed_val = rng.randint(1000, 999999)
    svg = draw_composite_shape_svg("running_track", length, d, label_w=f"Straight = {length} m", label_h=f"{d} m", seed=seed_val)

    prompt = (
        f"A sports running track consists of a central rectangle with two semicircular ends:\n"
        f"- Length of each straight side = **${length}\\text{{ m}}$**\n"
        f"- Diameter of each semicircular end = **${d}\\text{{ m}}$**\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **total outer perimeter (track length)** in metres."
    )

    return {
        "subskill": "33_composite_rectangle_with_semicircular_end_perimeter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(total_p),
        "sample_answer": f"{total_p} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that two semicircular ends form one complete circle: Circumference = pi * d", "marks": 1},
            {"step": f"Calculate circle circumference: (22/7) * {d} = {circle_c} m", "marks": 1},
            {"step": f"Add the two straight sides: {circle_c} + 2 * {length} = {total_p} m", "marks": 1},
        ],
        "hints": [
            "The two semicircular ends combine to form one complete circle of diameter $d$: $C = \\pi d$.",
            f"Curved distance $= \\frac{{22}}{{7}} \\times {d} = {circle_c}\\text{{ m}}$.",
            f"Add the two straight sides ($2 \\times {length} = {2 * length}\\text{{ m}}$): Total $= {total_p}\\text{{ m}}$.",
        ],
        "misconception_tags": ["included_internal_dividing_diameters_in_perimeter"],
    }


def arch_34_composite_rectangle_with_semicircular_end_area(rng: random.Random) -> Dict[str, Any]:
    """Area of Norman window (rectangle with one semicircular top)."""
    # Width of rectangle = diameter = 14k => r = 7k
    # Semicircle area = 1/2 * (22/7) * (7k)^2 = 77 * k^2
    k = rng.choice([1, 2])
    d = 14 * k
    r = 7 * k
    h_rect = rng.randint(15, 25)
    area_rect = d * h_rect
    area_semi = 77 * (k**2)
    total_area = area_rect + area_semi

    prompt = (
        f"A church window (Norman window) consists of a rectangle topped with a semicircle:\n"
        f"- The rectangular base has width **${d}\\text{{ cm}}$** and height **${h_rect}\\text{{ cm}}$**.\n"
        f"- The top is a semicircle with diameter **${d}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **total area** of the window in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "34_composite_rectangle_with_semicircular_end_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(total_area),
        "sample_answer": f"{total_area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate rectangle area: {d} * {h_rect} = {area_rect} cm^2", "marks": 1},
            {"step": f"Calculate semicircle area: 1/2 * (22/7) * {r}^2 = {area_semi} cm^2", "marks": 1},
            {"step": f"Add areas: {area_rect} + {area_semi} = {total_area} cm^2", "marks": 1},
        ],
        "hints": [
            f"Radius of the semicircle is half the width: $r = \\frac{{{d}}}{{2}} = {r}\\text{{ cm}}$.",
            f"Rectangle area $= {d} \\times {h_rect} = {area_rect}\\text{{ cm}}^2$.",
            f"Semicircle area $= \\frac{{1}}{{2}} \\times \\frac{{22}}{{7}} \\times {r}^2 = {area_semi}\\text{{ cm}}^2$.",
            f"Total area $= {total_area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["norman_window_area_formula_error"],
    }


def arch_35_shaded_area_square_minus_inscribed_circle(rng: random.Random) -> Dict[str, Any]:
    """Shaded area between square of side 2r and inscribed circle."""
    # Side s = 14k => r = 7k
    # Square = s^2 = 196k^2
    # Circle = pi * r^2 = (22/7) * 49k^2 = 154k^2
    # Shaded difference = 196k^2 - 154k^2 = 42k^2
    k = rng.choice([1, 2, 3])
    s = 14 * k
    r = 7 * k
    area_sq = s * s
    area_circ = 154 * (k**2)
    shaded = area_sq - area_circ
    seed_val = rng.randint(1000, 999999)
    svg = draw_composite_shape_svg("square_minus_circle", s, s, label_w=f"{s} cm", label_h=f"{s} cm", seed=seed_val)

    prompt = (
        f"Refer to the figure below. A circular disk is cut out from a square sheet of metal with side length **${s}\\text{{ cm}}$**:\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area of the remaining (shaded) metal** in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "35_shaded_area_square_minus_inscribed_circle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(shaded),
        "sample_answer": f"{shaded} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate square area: {s}^2 = {area_sq} cm^2", "marks": 1},
            {"step": f"Calculate inscribed circle area: (22/7) * {r}^2 = {area_circ} cm^2", "marks": 1},
            {"step": f"Subtract: {area_sq} - {area_circ} = {shaded} cm^2", "marks": 1},
        ],
        "hints": [
            f"The inscribed circle has diameter equal to the side of the square (${s}\\text{{ cm}}$), so radius $r = {r}\\text{{ cm}}$.",
            f"Square area $= {s}^2 = {area_sq}\\text{{ cm}}^2$. Circle area $= \\frac{{22}}{{7}} \\times {r}^2 = {area_circ}\\text{{ cm}}^2$.",
            f"Shaded area $= {area_sq} - {area_circ} = {shaded}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["shaded_area_cutout_error", "inscribed_circle_radius_identification_error"],
    }


def arch_36_shaded_area_circle_minus_inscribed_square(rng: random.Random) -> Dict[str, Any]:
    """Shaded area of circle of radius r minus square inscribed inside it (diagonal = 2r)."""
    # Circle radius r = 7k => Circle area = 154 k^2
    # Inscribed square has diagonal d = 2r = 14k => Square area = 1/2 * d^2 = 1/2 * (14k)^2 = 98 k^2
    # Shaded = 154k^2 - 98k^2 = 56k^2
    k = rng.choice([1, 2])
    r = 7 * k
    area_circ = 154 * (k**2)
    area_sq = 98 * (k**2)
    shaded = area_circ - area_sq

    prompt = (
        f"A circular target with radius **${r}\\text{{ cm}}$** has a square bullseye inscribed inside it "
        f"(the diagonal of the square is equal to the diameter of the circle, **${2 * r}\\text{{ cm}}$**).\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **shaded area** outside the square but inside the circle "
        f"in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "36_shaded_area_circle_minus_inscribed_square",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(shaded),
        "sample_answer": f"{shaded} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate circle area: (22/7) * {r}^2 = {area_circ} cm^2", "marks": 1},
            {"step": f"Calculate inscribed square area using diagonal: 1/2 * ({2 * r})^2 = {area_sq} cm^2", "marks": 1},
            {"step": f"Subtract: {area_circ} - {area_sq} = {shaded} cm^2", "marks": 1},
        ],
        "hints": [
            f"Circle area $= \\frac{{22}}{{7}} \\times {r}^2 = {area_circ}\\text{{ cm}}^2$.",
            f"The diagonal of the inscribed square is $2r = {2 * r}\\text{{ cm}}$. Area $= \\frac{{1}}{{2}} d^2 = {area_sq}\\text{{ cm}}^2$.",
            f"Shaded difference $= {area_circ} - {area_sq} = {shaded}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["inscribed_square_area_from_diagonal_error"],
    }


def arch_37_shaded_area_rectangle_minus_internal_rectangle_path(rng: random.Random) -> Dict[str, Any]:
    """Area of border path: outer rectangle minus inner lawn."""
    l_in = rng.randint(10, 16)
    b_in = rng.randint(6, 10)
    w_path = rng.choice([1, 2])
    l_out = l_in + 2 * w_path
    b_out = b_in + 2 * w_path
    area_out = l_out * b_out
    area_in = l_in * b_in
    path_area = area_out - area_in

    prompt = (
        f"A rectangular lawn measures **${l_in}\\text{{ m}}$** by **${b_in}\\text{{ m}}$**.\n"
        f"A paved walkway of width **${w_path}\\text{{ m}}$** surrounds the entire lawn on all sides.\n\n"
        f"Calculate the **area of the paved walkway** in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "37_shaded_area_rectangle_minus_internal_rectangle_path",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(path_area),
        "sample_answer": f"{path_area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Determine outer dimensions: {l_in} + 2({w_path}) = {l_out} m and {b_in} + 2({w_path}) = {b_out} m", "marks": 1},
            {"step": f"Calculate outer area: {l_out} * {b_out} = {area_out} m^2", "marks": 1},
            {"step": f"Calculate inner lawn area: {l_in} * {b_in} = {area_in} m^2", "marks": 1},
            {"step": f"Subtract: {area_out} - {area_in} = {path_area} m^2", "marks": 1},
        ],
        "hints": [
            f"The border adds ${w_path}\\text{{ m}}$ to both sides, so outer length is ${l_in} + 2({w_path}) = {l_out}\\text{{ m}}$.",
            f"Outer area $= {l_out} \\times {b_out} = {area_out}\\text{{ m}}^2$. Inner area $= {l_in} \\times {b_in} = {area_in}\\text{{ m}}^2$.",
            f"Path area $= {area_out} - {area_in} = {path_area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["added_path_width_once_instead_of_twice", "border_area_calculation_error"],
    }


def arch_38_linear_unit_conversion_mm_cm_m_km(rng: random.Random) -> Dict[str, Any]:
    """Linear unit conversion between mm, cm, m, km."""
    conversion_type = rng.choice(["m_to_cm", "cm_to_mm", "km_to_m", "mm_to_cm"])
    if conversion_type == "m_to_cm":
        val = rng.randint(3, 15)
        ans = val * 100
        prompt = f"Convert **${val}\\text{{ metres}}$** into centimetres ($\\text{{cm}}$)."
        unit = "cm"
        exp = f"{val} * 100 = {ans} cm"
    elif conversion_type == "cm_to_mm":
        val = rng.randint(12, 45)
        ans = val * 10
        prompt = f"Convert **${val}\\text{{ cm}}$** into millimetres ($\\text{{mm}}$)."
        unit = "mm"
        exp = f"{val} * 10 = {ans} mm"
    elif conversion_type == "km_to_m":
        val = rng.randint(2, 9)
        ans = val * 1000
        prompt = f"Convert **${val}\\text{{ km}}$** into metres ($\\text{{m}}$)."
        unit = "m"
        exp = f"{val} * 1000 = {ans} m"
    else:
        ans = rng.randint(15, 60)
        val = ans * 10
        prompt = f"Convert **${val}\\text{{ mm}}$** into centimetres ($\\text{{cm}}$)."
        unit = "cm"
        exp = f"{val} / 10 = {ans} cm"

    return {
        "subskill": "38_linear_unit_conversion_mm_cm_m_km",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(ans),
        "sample_answer": f"{ans} {unit}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply linear conversion factor: {exp}", "marks": 1},
        ],
        "hints": [
            "$1\\text{ m} = 100\\text{ cm}$, $1\\text{ cm} = 10\\text{ mm}$, $1\\text{ km} = 1000\\text{ m}$.",
            f"Calculation: {exp}.",
            f"Answer: **{ans}**.",
        ],
        "misconception_tags": ["metric_linear_conversion_factor_error"],
    }


def arch_39_area_unit_conversion_mm2_to_cm2_and_m2(rng: random.Random) -> Dict[str, Any]:
    """Area unit conversions: 1 cm^2 = 100 mm^2 or 1 m^2 = 10 000 cm^2."""
    conv = rng.choice(["cm2_to_mm2", "m2_to_cm2", "mm2_to_cm2"])
    if conv == "cm2_to_mm2":
        val = rng.randint(4, 15)
        ans = val * 100
        prompt = f"Convert **${val}\\text{{ cm}}^2$** into square millimetres ($\\text{{mm}}^2$)."
        unit = "mm²"
        factor = "10^2 = 100"
    elif conv == "m2_to_cm2":
        val = rng.randint(2, 8)
        ans = val * 10000
        prompt = f"Convert **${val}\\text{{ m}}^2$** into square centimetres ($\\text{{cm}}^2$)."
        unit = "cm²"
        factor = "100^2 = 10 000"
    else:
        base = rng.randint(5, 25)
        val = base * 100
        ans = base
        prompt = f"Convert **${val}\\text{{ mm}}^2$** into square centimetres ($\\text{{cm}}^2$)."
        unit = "cm²"
        factor = "divide by 100"

    return {
        "subskill": "39_area_unit_conversion_mm2_to_cm2_and_m2",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(ans),
        "sample_answer": f"{ans} {unit}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply area squared conversion factor ({factor})", "marks": 1},
            {"step": f"Result: {ans} {unit}", "marks": 1},
        ],
        "hints": [
            "Remember that area units square the linear factor: $1\\text{ cm}^2 = 10^2 = 100\\text{ mm}^2$, and $1\\text{ m}^2 = 100^2 = 10\\,000\\text{ cm}^2$.",
            f"Use conversion factor: {factor}.",
            f"Answer: **{ans}**.",
        ],
        "misconception_tags": ["used_linear_factor_for_area_units", "area_metric_conversion_error"],
    }


def arch_40_area_unit_conversion_m2_to_hectares_and_km2(rng: random.Random) -> Dict[str, Any]:
    """Hectares conversion: 1 hectare (ha) = 10 000 m^2."""
    ha_val = rng.randint(2, 9)
    m2_val = ha_val * 10000

    prompt = (
        f"A farm paddock has an area of **${m2_val}\\text{{ m}}^2$**.\n\n"
        f"Convert this area into **hectares (ha)** (recall: $1\\text{{ ha}} = 10\\,000\\text{{ m}}^2$)."
    )

    return {
        "subskill": "40_area_unit_conversion_m2_to_hectares_and_km2",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(ha_val),
        "sample_answer": f"{ha_val} ha",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State hectare definition: 1 ha = 10 000 m^2", "marks": 1},
            {"step": f"Calculate: {m2_val} / 10 000 = {ha_val} ha", "marks": 1},
        ],
        "hints": [
            "One hectare is equivalent to $10\\,000\\text{ m}^2$.",
            f"Divide by $10\\,000$: ${m2_val} \\div 10\\,000$.",
            f"Area $= {ha_val}\\text{{ ha}}$.",
        ],
        "misconception_tags": ["hectare_conversion_factor_error"],
    }


def arch_41_effect_of_scaling_dimensions_by_k_on_perimeter(rng: random.Random) -> Dict[str, Any]:
    """Multiplying dimensions by k multiplies perimeter by k."""
    k = rng.choice([2, 3, 4, 5])
    orig_p = rng.randint(15, 40)
    new_p = orig_p * k

    prompt = (
        f"A polygon has an initial perimeter of **${orig_p}\\text{{ cm}}$**.\n"
        f"All side lengths of the polygon are multiplied by a scale factor of **$k = {k}$**.\n\n"
        f"Calculate the **new perimeter** of the enlarged polygon in centimetres."
    )

    return {
        "subskill": "41_effect_of_scaling_dimensions_by_k_on_perimeter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(new_p),
        "sample_answer": f"{new_p} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recall property: when dimensions scale by k, perimeter scales by k: P' = k * P", "marks": 1},
            {"step": f"Calculate: {k} * {orig_p} = {new_p} cm", "marks": 1},
        ],
        "hints": [
            "Perimeter is a one-dimensional (linear) measurement, so it scales by the exact same factor $k$.",
            f"Multiply original perimeter by $k$: ${orig_p} \\times {k}$.",
            f"New perimeter $= {new_p}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["squared_perimeter_scale_factor_error", "linear_scaling_property_error"],
    }


def arch_42_effect_of_scaling_dimensions_by_k_on_area(rng: random.Random) -> Dict[str, Any]:
    """Multiplying dimensions by k multiplies area by k^2."""
    k = rng.choice([2, 3, 4])
    orig_area = rng.randint(10, 30)
    new_area = orig_area * (k**2)

    prompt = (
        f"A 2D shape has an area of **${orig_area}\\text{{ cm}}^2$**.\n"
        f"All linear dimensions of the shape are enlarged by a factor of **$k = {k}$**.\n\n"
        f"Calculate the **new area** of the enlarged shape in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "42_effect_of_scaling_dimensions_by_k_on_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(new_area),
        "sample_answer": f"{new_area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recall scaling law: when linear dimensions scale by k, area scales by k^2: A' = k^2 * A", "marks": 1},
            {"step": f"Calculate: {k}^2 * {orig_area} = {k**2} * {orig_area} = {new_area} cm^2", "marks": 1},
        ],
        "hints": [
            "Area is a two-dimensional measurement, so it scales by $k^2$ (not just $k$).",
            f"Scale factor squared $= {k}^2 = {k**2}$.",
            f"New area $= {orig_area} \\times {k**2} = {new_area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["multiplied_area_by_k_instead_of_k_squared", "area_scaling_law_violation"],
    }


def arch_43_calculate_scale_factor_given_ratio_of_areas(rng: random.Random) -> Dict[str, Any]:
    """Given area ratio, find linear scale factor k = sqrt(ratio)."""
    k = rng.choice([2, 3, 4, 5])
    area_ratio = k**2

    prompt = (
        f"When an architect enlarges a house floor plan, the area of the floor plan increases by a factor "
        f"of **${area_ratio}$**.\n\n"
        f"By what factor **$k$** were the linear dimensions (length and breadth) multiplied?\n"
        f"(State the value of $k$)."
    )

    return {
        "subskill": "43_calculate_scale_factor_given_ratio_of_areas",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(k),
        "sample_answer": f"k = {k}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State relation: Area ratio = k^2 => k = √(Area ratio)", "marks": 1},
            {"step": f"Calculate: k = √({area_ratio}) = {k}", "marks": 1},
        ],
        "hints": [
            "Because $\\text{Area ratio} = k^2$, take the square root to find the linear scale factor $k$.",
            f"$k = \\sqrt{{{area_ratio}}}$.",
            f"$k = {k}$.",
        ],
        "misconception_tags": ["halved_area_ratio_instead_of_square_root"],
    }


def arch_44_contextual_fencing_cost_perimeter_application(rng: random.Random) -> Dict[str, Any]:
    """Contextual fencing cost = Perimeter * cost per metre."""
    l = rng.randint(20, 50)
    b = rng.randint(15, l - 5)
    perimeter = 2 * (l + b)
    rate = rng.choice([45, 60, 80, 120])  # R per metre
    cost = perimeter * rate

    prompt = (
        f"A farmer encloses a rectangular field measuring **${l}\\text{{ m}}$** by **${b}\\text{{ m}}$** with wire fencing.\n"
        f"The wire fencing costs **R{rate} per metre**.\n\n"
        f"Calculate the **total cost** to fence the field in Rands (R)."
    )

    return {
        "subskill": "44_contextual_fencing_cost_perimeter_application",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(cost),
        "sample_answer": f"R{cost}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate perimeter: 2 * ({l} + {b}) = {perimeter} metres", "marks": 1},
            {"step": f"Calculate cost: {perimeter} * R{rate} = R{cost}", "marks": 1},
        ],
        "hints": [
            "Fencing surrounds the perimeter of the field.",
            f"Perimeter $= 2({l} + {b}) = {perimeter}\\text{{ m}}$.",
            f"Total cost $= {perimeter} \\times \\text{{R}}{rate} = \\text{{R}}{cost}$.",
        ],
        "misconception_tags": ["used_area_instead_of_perimeter_for_fencing"],
    }


def arch_45_contextual_turfing_or_tiling_cost_area_application(rng: random.Random) -> Dict[str, Any]:
    """Contextual turfing / tiling cost = Area * rate per m^2."""
    l = rng.randint(8, 15)
    b = rng.randint(5, 10)
    area = l * b
    rate = rng.choice([75, 85, 120, 150])  # R per m^2
    total_cost = area * rate

    prompt = (
        f"A homeowner installs instant roll-on lawn for a rectangular garden measuring **${l}\\text{{ m}}$** by **${b}\\text{{ m}}$**.\n"
        f"The instant lawn costs **R{rate} per square metre ($\\text{{m}}^2$)**.\n\n"
        f"Calculate the **total cost** of turfing the garden in Rands (R)."
    )

    return {
        "subskill": "45_contextual_turfing_or_tiling_cost_area_application",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(total_cost),
        "sample_answer": f"R{total_cost}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate area: {l} * {b} = {area} m^2", "marks": 1},
            {"step": f"Calculate total cost: {area} * R{rate} = R{total_cost}", "marks": 1},
        ],
        "hints": [
            "Lawn covers the surface area of the garden.",
            f"Area $= {l} \\times {b} = {area}\\text{{ m}}^2$.",
            f"Total cost $= {area} \\times \\text{{R}}{rate} = \\text{{R}}{total_cost}$.",
        ],
        "misconception_tags": ["used_perimeter_instead_of_area_for_turf"],
    }


def arch_46_contextual_painting_walls_deducting_doors_windows(rng: random.Random) -> Dict[str, Any]:
    """Paintable wall area = Total wall area minus door and window openings."""
    wall_l = rng.randint(6, 10)
    wall_h = rng.randint(3, 4)
    total_wall = wall_l * wall_h
    door_area = 2  # 2m x 1m standard door
    window_area = 2  # 2m x 1m standard window
    net_area = total_wall - (door_area + window_area)

    prompt = (
        f"A bedroom wall measures **${wall_l}\\text{{ m}}$** long and **${wall_h}\\text{{ m}}$** high.\n"
        f"The wall contains a door with an area of **${door_area}\\text{{ m}}^2$** and a window with an "
        f"area of **${window_area}\\text{{ m}}^2$**.\n\n"
        f"Calculate the **net area of wall surface to be painted** in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "46_contextual_painting_walls_deducting_doors_windows",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(net_area),
        "sample_answer": f"{net_area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate gross wall area: {wall_l} * {wall_h} = {total_wall} m^2", "marks": 1},
            {"step": f"Subtract openings: {total_wall} - ({door_area} + {window_area}) = {net_area} m^2", "marks": 1},
        ],
        "hints": [
            f"Gross wall area $= {wall_l} \\times {wall_h} = {total_wall}\\text{{ m}}^2$.",
            f"Unpainted openings $= {door_area} + {window_area} = {door_area + window_area}\\text{{ m}}^2$.",
            f"Paintable area $= {total_wall} - {door_area + window_area} = {net_area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["forgot_to_deduct_openings_in_wall_paint"],
    }


def arch_47_error_analysis_confusing_perimeter_and_area(rng: random.Random) -> Dict[str, Any]:
    """Diagnose error of stating perimeter units (cm) for area (cm^2) or formula confusion."""
    l = rng.randint(6, 12)
    b = rng.randint(4, l - 1)
    wrong_p = 2 * (l + b)
    correct_area = l * b

    prompt = (
        f"A learner is asked to calculate the **area** of a rectangle measuring **${l}\\text{{ cm}}$** by **${b}\\text{{ cm}}$**.\n"
        f"The learner answers: **${wrong_p}\\text{{ cm}}$**.\n\n"
        f"1. Explain the conceptual error the learner made.\n"
        f"2. Calculate the **correct area** in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "47_error_analysis_confusing_perimeter_and_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(correct_area),
        "sample_answer": f"{correct_area} cm² (learner calculated perimeter instead of area)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Diagnose error: learner calculated perimeter (2*(l+b)) instead of area (l*b)", "marks": 1},
            {"step": f"Calculate correct area: {l} * {b} = {correct_area} cm^2", "marks": 1},
        ],
        "hints": [
            f"The value ${wrong_p}$ comes from $2({l} + {b})$, which is the perimeter.",
            "Area requires multiplication: $l \\times b$.",
            f"Correct area $= {correct_area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["perimeter_instead_of_area_misconception", "units_confusion_cm_vs_cm2"],
    }


def arch_48_error_analysis_slanted_side_used_as_perpendicular_height(rng: random.Random) -> Dict[str, Any]:
    """Diagnose why multiplying base by slant height gives an incorrect (overestimated) area."""
    prompt = (
        f"When calculating the area of a parallelogram with base $b = 10\\text{{ cm}}$, slanted side $s = 6\\text{{ cm}}$, "
        f"and perpendicular height $h = 5\\text{{ cm}}$:\n\n"
        f"Why is calculating $10 \\times 6 = 60\\text{{ cm}}^2$ mathematically incorrect?\n"
        f"State: **the slanted side is not perpendicular to the base**"
    )

    return {
        "subskill": "48_error_analysis_slanted_side_used_as_perpendicular_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the slanted side is not perpendicular to the base",
        "sample_answer": "the slanted side is not perpendicular to the base",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain that area of a parallelogram requires perpendicular height, and the hypotenuse/slanted side is always strictly longer than perpendicular height", "marks": 1},
        ],
        "hints": [
            "In any slanted parallelogram, the perpendicular height is shorter than the slanted side.",
            "Using the slanted side overestimates the true surface area.",
            "Answer: **the slanted side is not perpendicular to the base**.",
        ],
        "misconception_tags": ["slanted_side_vs_perpendicular_height", "parallelogram_altitude_rigor"],
    }


def arch_49_error_analysis_forgetting_flat_base_in_semicircle_perimeter(rng: random.Random) -> Dict[str, Any]:
    """Diagnose why calculating only pi*r for semicircle perimeter is incomplete."""
    prompt = (
        f"A learner calculates the perimeter of a closed semicircular garden with radius $r = 7\\text{{ m}}$ as:\n"
        f"$$\\text{{Perimeter}} = \\pi r = \\frac{{22}}{{7}} \\times 7 = 22\\text{{ m}}$$\n\n"
        f"What part of the garden boundary did the learner forget to include?\n"
        f"State: **the diameter**"
    )

    return {
        "subskill": "49_error_analysis_forgetting_flat_base_in_semicircle_perimeter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the diameter",
        "sample_answer": "the diameter",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that pi * r gives only the curved boundary arc, omitting the flat straight diameter line", "marks": 1},
        ],
        "hints": [
            "A closed semicircle has two boundaries: the curved arc and the straight diameter line across the bottom.",
            "The learner only calculated the curved arc.",
            "Answer: **the diameter**.",
        ],
        "misconception_tags": ["omitted_straight_edge_in_semicircle", "boundary_completeness_error"],
    }


def arch_50_compound_multi_stage_park_layout_synthesis(rng: random.Random) -> Dict[str, Any]:
    """Compound synthesis: rectangular park with circular flower bed and paved path."""
    l = rng.choice([20, 25, 30])
    b = rng.choice([14, 18, 20])
    park_area = l * b
    # Circular flowerbed with radius 7m in center => area = (22/7)*49 = 154 m^2
    r_flower = 7
    flower_area = 154
    turf_area = park_area - flower_area

    prompt = (
        f"A city park is designed in the shape of a rectangle measuring **${l}\\text{{ m}}$** by **${b}\\text{{ m}}$**.\n"
        f"In the center of the park, a circular flower bed with radius **${r_flower}\\text{{ m}}$** is constructed.\n"
        f"The rest of the park is covered in lawn grass.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area of the lawn grass** in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "50_compound_multi_stage_park_layout_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(turf_area),
        "sample_answer": f"{turf_area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate rectangular park area: {l} * {b} = {park_area} m^2", "marks": 1},
            {"step": f"Calculate circular flowerbed area: (22/7) * {r_flower}^2 = {flower_area} m^2", "marks": 1},
            {"step": f"Subtract flowerbed from park: {park_area} - {flower_area} = {turf_area} m^2", "marks": 1},
        ],
        "hints": [
            f"Total park area $= {l} \\times {b} = {park_area}\\text{{ m}}^2$.",
            f"Flower bed area $= \\frac{{22}}{{7}} \\times {r_flower}^2 = {flower_area}\\text{{ m}}^2$.",
            f"Lawn area $= {park_area} - {flower_area} = {turf_area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["compound_synthesis_area_subtraction_error"],
    }
