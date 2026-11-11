"""Measurement of perimeter and area Subskills Package (52 distinct archetypes).

Covers Grade 10 Mathematical Literacy Term 3 Topic:
1. Perimeter of Polygons & Basic Shapes (Subskills 1 to 9)
2. Composite Perimeters & Boundary Applications (Subskills 10 to 18)
3. Area of Polygons & Standard Shapes (Subskills 19 to 27)
4. Composite Areas & Cutouts (Subskills 28 to 36)
5. Surface Materials, Tiling, Paving & Turf (Subskills 37 to 44)
6. Painting, Agriculture & Commercial Area Applications (Subskills 45 to 52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .perim_polygons_circles import (
    _gen_perim_square_formula_and_perimeter,
    _gen_perim_rectangle_formula_and_perimeter,
    _gen_perim_triangle_three_sides,
    _gen_perim_equilateral_and_isosceles_triangle,
    _gen_perim_right_angled_triangle_pythagoras,
    _gen_perim_circle_circumference_from_radius,
    _gen_perim_circle_circumference_from_diameter,
    _gen_perim_semicircle_total_perimeter,
    _gen_perim_quarter_circle_perimeter,
)
from .perim_composite_fencing import (
    _gen_perim_l_shaped_floor_perimeter,
    _gen_perim_u_shaped_courtyard_perimeter,
    _gen_perim_rectangle_with_semicircular_end,
    _gen_perim_running_track_two_semicircles,
    _gen_perim_garden_fencing_deducting_gate,
    _gen_perim_fencing_multiple_strands_barbed_wire,
    _gen_perim_fencing_posts_interval_spacing,
    _gen_perim_skirting_boards_deducting_doorways,
    _gen_perim_picture_frame_border_perimeter,
)
from .area_polygons_circles import (
    _gen_area_square_formula_and_calculation,
    _gen_area_rectangle_formula_and_calculation,
    _gen_area_triangle_base_and_height,
    _gen_area_right_angled_triangle,
    _gen_area_circle_from_radius,
    _gen_area_circle_from_diameter,
    _gen_area_semicircle_calculation,
    _gen_area_quarter_circle_calculation,
    _gen_area_trapezium_parallel_sides,
)
from .area_composite_cutouts import (
    _gen_area_composite_l_shape_split_rectangles,
    _gen_area_composite_t_shape_layout,
    _gen_area_rectangle_plus_semicircle_patio,
    _gen_area_rectangle_plus_triangle_gable,
    _gen_area_cutout_lawn_minus_swimming_pool,
    _gen_area_cutout_patio_minus_circular_pond,
    _gen_area_cutout_wall_minus_doors_and_windows,
    _gen_area_cutout_washer_ring_annulus,
    _gen_area_percentage_of_property_occupied,
)
from .area_tiling_paving_turf import (
    _gen_area_tiling_floor_tile_count,
    _gen_area_tiling_boxes_with_wastage,
    _gen_area_tiling_total_cost_calculation,
    _gen_area_paving_cobblestones_count,
    _gen_area_paving_batches_and_cost,
    _gen_area_turf_grass_rolls_and_wastage,
    _gen_area_carpet_roll_and_underlay_budget,
    _gen_area_swimming_pool_cover_with_overlap,
)
from .area_painting_agri_commercial import (
    _gen_area_wall_painting_perimeter_height,
    _gen_area_wall_painting_two_coats_spread_rate,
    _gen_area_wall_painting_tin_size_and_cost,
    _gen_area_garden_compost_application_rate,
    _gen_area_seedling_planting_density,
    _gen_area_fertilizer_application_budget,
    _gen_area_commercial_property_rental,
    _gen_area_municipal_property_rates_assessment,
)

DISPATCH_TABLE: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    # Cluster 1: Perimeter of Polygons & Basic Shapes (9)
    "perim_square_formula_and_perimeter": _gen_perim_square_formula_and_perimeter,
    "perim_rectangle_formula_and_perimeter": _gen_perim_rectangle_formula_and_perimeter,
    "perim_triangle_three_sides": _gen_perim_triangle_three_sides,
    "perim_equilateral_and_isosceles_triangle": _gen_perim_equilateral_and_isosceles_triangle,
    "perim_right_angled_triangle_pythagoras": _gen_perim_right_angled_triangle_pythagoras,
    "perim_circle_circumference_from_radius": _gen_perim_circle_circumference_from_radius,
    "perim_circle_circumference_from_diameter": _gen_perim_circle_circumference_from_diameter,
    "perim_semicircle_total_perimeter": _gen_perim_semicircle_total_perimeter,
    "perim_quarter_circle_perimeter": _gen_perim_quarter_circle_perimeter,

    # Cluster 2: Composite Perimeters & Practical Boundary Applications (9)
    "perim_l_shaped_floor_perimeter": _gen_perim_l_shaped_floor_perimeter,
    "perim_u_shaped_courtyard_perimeter": _gen_perim_u_shaped_courtyard_perimeter,
    "perim_rectangle_with_semicircular_end": _gen_perim_rectangle_with_semicircular_end,
    "perim_running_track_two_semicircles": _gen_perim_running_track_two_semicircles,
    "perim_garden_fencing_deducting_gate": _gen_perim_garden_fencing_deducting_gate,
    "perim_fencing_multiple_strands_barbed_wire": _gen_perim_fencing_multiple_strands_barbed_wire,
    "perim_fencing_posts_interval_spacing": _gen_perim_fencing_posts_interval_spacing,
    "perim_skirting_boards_deducting_doorways": _gen_perim_skirting_boards_deducting_doorways,
    "perim_picture_frame_border_perimeter": _gen_perim_picture_frame_border_perimeter,

    # Cluster 3: Area of Polygons & Standard Shapes (9)
    "area_square_formula_and_calculation": _gen_area_square_formula_and_calculation,
    "area_rectangle_formula_and_calculation": _gen_area_rectangle_formula_and_calculation,
    "area_triangle_base_and_height": _gen_area_triangle_base_and_height,
    "area_right_angled_triangle": _gen_area_right_angled_triangle,
    "area_circle_from_radius": _gen_area_circle_from_radius,
    "area_circle_from_diameter": _gen_area_circle_from_diameter,
    "area_semicircle_calculation": _gen_area_semicircle_calculation,
    "area_quarter_circle_calculation": _gen_area_quarter_circle_calculation,
    "area_trapezium_parallel_sides": _gen_area_trapezium_parallel_sides,

    # Cluster 4: Composite Areas & Cutouts (9)
    "area_composite_l_shape_split_rectangles": _gen_area_composite_l_shape_split_rectangles,
    "area_composite_t_shape_layout": _gen_area_composite_t_shape_layout,
    "area_rectangle_plus_semicircle_patio": _gen_area_rectangle_plus_semicircle_patio,
    "area_rectangle_plus_triangle_gable": _gen_area_rectangle_plus_triangle_gable,
    "area_cutout_lawn_minus_swimming_pool": _gen_area_cutout_lawn_minus_swimming_pool,
    "area_cutout_patio_minus_circular_pond": _gen_area_cutout_patio_minus_circular_pond,
    "area_cutout_wall_minus_doors_and_windows": _gen_area_cutout_wall_minus_doors_and_windows,
    "area_cutout_washer_ring_annulus": _gen_area_cutout_washer_ring_annulus,
    "area_percentage_of_property_occupied": _gen_area_percentage_of_property_occupied,

    # Cluster 5: Surface Materials, Tiling, Paving & Turf (8)
    "area_tiling_floor_tile_count": _gen_area_tiling_floor_tile_count,
    "area_tiling_boxes_with_wastage": _gen_area_tiling_boxes_with_wastage,
    "area_tiling_total_cost_calculation": _gen_area_tiling_total_cost_calculation,
    "area_paving_cobblestones_count": _gen_area_paving_cobblestones_count,
    "area_paving_batches_and_cost": _gen_area_paving_batches_and_cost,
    "area_turf_grass_rolls_and_wastage": _gen_area_turf_grass_rolls_and_wastage,
    "area_carpet_roll_and_underlay_budget": _gen_area_carpet_roll_and_underlay_budget,
    "area_swimming_pool_cover_with_overlap": _gen_area_swimming_pool_cover_with_overlap,

    # Cluster 6: Painting, Agriculture & Commercial Area Applications (8)
    "area_wall_painting_perimeter_height": _gen_area_wall_painting_perimeter_height,
    "area_wall_painting_two_coats_spread_rate": _gen_area_wall_painting_two_coats_spread_rate,
    "area_wall_painting_tin_size_and_cost": _gen_area_wall_painting_tin_size_and_cost,
    "area_garden_compost_application_rate": _gen_area_garden_compost_application_rate,
    "area_seedling_planting_density": _gen_area_seedling_planting_density,
    "area_fertilizer_application_budget": _gen_area_fertilizer_application_budget,
    "area_commercial_property_rental": _gen_area_commercial_property_rental,
    "area_municipal_property_rates_assessment": _gen_area_municipal_property_rates_assessment,
}

SUBSKILLS: List[str] = list(DISPATCH_TABLE.keys())


def generate(seed: Optional[int] = None, count: int = 1, subskill: Optional[str] = None) -> List[Dict[str, Any]]:
    """Generate questions for Measurement of perimeter and area."""
    r = random.Random(seed)
    questions = []

    for _ in range(count):
        if subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen]
        questions.append(fn(r))

    return questions
