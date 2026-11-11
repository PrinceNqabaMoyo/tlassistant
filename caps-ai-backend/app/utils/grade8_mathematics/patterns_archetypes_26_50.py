"""
Grade 8 Mathematics - Numeric and Geometric Patterns Archetypes 26 to 50.
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/04. Numeric and geometric patterns.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import (
    draw_dot_pattern_stages_svg,
    draw_matchstick_pattern_svg,
)


def arch_26_verify_whether_number_belongs_to_linear_sequence(rng: random.Random) -> Dict[str, Any]:
    d = rng.randint(4, 7)
    c = rng.randint(2, 6)
    # T_n = d*n + c
    is_member = rng.choice([True, False])
    if is_member:
        n_val = rng.randint(12, 28)
        test_val = d * n_val + c
        ans = "Yes"
        reason = f"n = ({test_val} - {c}) / {d} = {n_val}, which is a whole number."
    else:
        n_val = rng.randint(12, 28)
        test_val = d * n_val + c + rng.choice([1, 2])
        ans = "No"
        rem = (test_val - c) % d
        reason = f"({test_val} - {c}) / {d} does not yield an integer (remainder {rem})."

    seq_terms = [d * n + c for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in seq_terms) + "; \\dots"

    return {
        "title": "Verifying Sequence Membership",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "26_verify_whether_number_belongs_to_linear_sequence",
        "difficulty": "hard",
        "question_text": (
            f"Consider the arithmetic sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Determine whether the number **{test_val}** is a term in this sequence. Answer **Yes** or **No**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"Set up T_n = {d}n + {c} = {test_val} (1 mark)",
            f"Evaluate position n: {reason} (1 mark)",
            f"State conclusion: {ans} (1 mark)",
        ],
        "hints": [
            f"Write the general formula: $T_n = {d}n + {c}$.",
            f"Set ${d}n + {c} = {test_val}$ and solve for $n$.",
            f"If $n$ is a positive integer, the number is in the sequence; otherwise it is not.",
        ],
        "misconception_tags": ["divisibility_membership_misunderstanding"],
        "diagram_spec": None,
    }


def arch_27_matchstick_squares_in_row_diagram_formula(rng: random.Random) -> Dict[str, Any]:
    stages = 3
    svg = draw_matchstick_pattern_svg(shape="square", stages=stages, seed=rng.randint(1, 1000000))
    n_target = rng.choice([10, 12, 15, 20])
    ans_matches = 3 * n_target + 1

    return {
        "title": "Matchstick Pattern (Squares in a Row)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "27_matchstick_squares_in_row_diagram_formula",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the illustration below showing matchstick square frames joined in a row:\n\n"
            f"* Stage 1: 4 matchsticks\n"
            f"* Stage 2: 7 matchsticks\n"
            f"* Stage 3: 10 matchsticks\n\n"
            f"Find the algebraic expression for matchsticks $M$ in terms of $n$, and evaluate for **Stage {n_target}**."
        ),
        "correct_answer": str(ans_matches),
        "marking_schema": [
            "Derive general rule M = 3n + 1 (2 marks)",
            f"Substitute n = {n_target}: M = 3({n_target}) + 1 = {ans_matches} (1 mark)",
        ],
        "hints": [
            "Notice that adding each new square adds 3 additional matches.",
            "The rule is $M = 3n + 1$.",
            f"For Stage {n_target}: $M = 3({n_target}) + 1 = {ans_matches}$.",
        ],
        "misconception_tags": ["shared_matchstick_perimeter_overlap_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_28_matchstick_triangles_in_row_diagram_formula(rng: random.Random) -> Dict[str, Any]:
    stages = 3
    svg = draw_matchstick_pattern_svg(shape="triangle", stages=stages, seed=rng.randint(1, 1000000))
    n_target = rng.choice([12, 15, 25, 30])
    ans_matches = 2 * n_target + 1

    return {
        "title": "Matchstick Pattern (Triangles in a Row)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "28_matchstick_triangles_in_row_diagram_formula",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the figure showing matchsticks forming a row of connected triangles:\n\n"
            f"* Stage 1 (1 triangle) = 3 matches\n"
            f"* Stage 2 (2 triangles) = 5 matches\n"
            f"* Stage 3 (3 triangles) = 7 matches\n\n"
            f"Determine the number of matchsticks needed to build **Stage {n_target}**."
        ),
        "correct_answer": str(ans_matches),
        "marking_schema": [
            "Derive formula M = 2n + 1 (1 mark)",
            f"Calculate M = 2({n_target}) + 1 = {ans_matches} (1 mark)",
        ],
        "hints": [
            "First triangle takes 3 matches; every additional triangle shares 1 side and takes only 2 matches.",
            "Formula: $M = 2n + 1$.",
            f"For $n = {n_target}$: $M = 2({n_target}) + 1 = {ans_matches}$.",
        ],
        "misconception_tags": ["triangle_shared_edge_neglect"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_29_matchstick_hexagons_in_row_diagram_formula(rng: random.Random) -> Dict[str, Any]:
    stages = 3
    svg = draw_matchstick_pattern_svg(shape="hexagon", stages=stages, seed=rng.randint(1, 1000000))
    n_target = rng.choice([8, 10, 14, 20])
    ans_matches = 5 * n_target + 1

    return {
        "title": "Matchstick Pattern (Hexagons in a Row)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "29_matchstick_hexagons_in_row_diagram_formula",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the figure showing regular hexagons joined in a chain using matchsticks:\n\n"
            f"* Stage 1 (1 hexagon) = 6 matchsticks\n"
            f"* Stage 2 (2 hexagons) = 11 matchsticks\n"
            f"* Stage 3 (3 hexagons) = 16 matchsticks\n\n"
            f"Find the total number of matchsticks required to construct **Stage {n_target}**."
        ),
        "correct_answer": str(ans_matches),
        "marking_schema": [
            "Identify constant difference d = 5 (1 mark)",
            "Derive formula M = 5n + 1 (1 mark)",
            f"Calculate M for n = {n_target}: 5({n_target}) + 1 = {ans_matches} (1 mark)",
        ],
        "hints": [
            "The difference between stages is $11 - 6 = 5$.",
            "General term $M = 5n + 1$.",
            f"For Stage {n_target}: $M = 5({n_target}) + 1 = {ans_matches}$.",
        ],
        "misconception_tags": ["hexagon_chain_rule_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_30_matchstick_fences_or_posts_diagram_formula(rng: random.Random) -> Dict[str, Any]:
    # Fence sections: 1 section = 5 rails/posts, 2 sections = 9 rails, 3 sections = 13 rails (4n + 1)
    svg = draw_matchstick_pattern_svg(shape="square", stages=3, seed=rng.randint(1, 1000000))
    n_sections = rng.choice([15, 20, 25, 30])
    ans_rails = 4 * n_sections + 1

    return {
        "title": "Fence Post and Rail Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "30_matchstick_fences_or_posts_diagram_formula",
        "difficulty": "medium",
        "question_text": (
            f"A timber fence is built in sequential sections:\n\n"
            f"* 1 section requires 5 poles\n"
            f"* 2 sections require 9 poles\n"
            f"* 3 sections require 13 poles\n\n"
            f"Determine the algebraic rule for the number of poles $P$ in terms of sections $n$, "
            f"and calculate the number of poles needed to construct a fence of **{n_sections} sections**."
        ),
        "correct_answer": str(ans_rails),
        "marking_schema": [
            "Derive linear rule P = 4n + 1 (2 marks)",
            f"Calculate poles for n = {n_sections}: 4({n_sections}) + 1 = {ans_rails} (1 mark)",
        ],
        "hints": [
            "Observe the difference between consecutive sections: $9 - 5 = 4$.",
            "Rule: $P = 4n + 1$.",
            f"Substitute $n = {n_sections}$: $P = 4({n_sections}) + 1 = {ans_rails}$.",
        ],
        "misconception_tags": ["linear_fence_post_formula_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_31_dot_pattern_triangular_arrangement_diagram(rng: random.Random) -> Dict[str, Any]:
    # Triangular dots: 1, 3, 6, 10
    svg = draw_dot_pattern_stages_svg([1, 3, 6], seed=rng.randint(1, 1000000))
    stage_target = rng.choice([5, 6, 7])
    ans_dots = (stage_target * (stage_target + 1)) // 2

    return {
        "title": "Triangular Dot Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "31_dot_pattern_triangular_arrangement_diagram",
        "difficulty": "hard",
        "question_text": (
            f"Refer to the figure showing the first three stages of a triangular dot pattern:\n\n"
            f"* Stage 1: 1 dot\n"
            f"* Stage 2: 3 dots\n"
            f"* Stage 3: 6 dots\n\n"
            f"Calculate the number of dots needed to construct **Stage {stage_target}**."
        ),
        "correct_answer": str(ans_dots),
        "marking_schema": [
            "Recognize triangular numbers progression (+2, +3, +4, +5...) (1 mark)",
            f"Calculate Stage {stage_target} dots = {ans_dots} (2 marks)",
        ],
        "hints": [
            "Stage 1 = 1",
            "Stage 2 = 1 + 2 = 3",
            "Stage 3 = 1 + 2 + 3 = 6",
            f"Stage {stage_target} is the sum of integers from 1 up to {stage_target}: $\\frac{{{stage_target} \\times ({stage_target} + 1)}}{{2}} = {ans_dots}$.",
        ],
        "misconception_tags": ["triangular_sum_formula_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_32_dot_pattern_square_grid_diagram(rng: random.Random) -> Dict[str, Any]:
    # Square grids: 1, 4, 9, 16 dots
    svg = draw_dot_pattern_stages_svg([1, 4, 9], kind="grid", seed=rng.randint(1, 1000000))
    stage_target = rng.choice([8, 10, 12])
    ans_dots = stage_target ** 2

    return {
        "title": "Square Grid Dot Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "32_dot_pattern_square_grid_diagram",
        "difficulty": "easy",
        "question_text": (
            f"Study the dot array diagrams below:\n\n"
            f"* Stage 1: $1 \\times 1 = 1$ dot\n"
            f"* Stage 2: $2 \\times 2 = 4$ dots\n"
            f"* Stage 3: $3 \\times 3 = 9$ dots\n\n"
            f"Find the algebraic formula for dots $D$ at stage $n$, and calculate the total count of dots in **Stage {stage_target}**."
        ),
        "correct_answer": str(ans_dots),
        "marking_schema": [
            "Identify general rule D_n = n^2 (1 mark)",
            f"Evaluate for n = {stage_target}: {stage_target}^2 = {ans_dots} (1 mark)",
        ],
        "hints": [
            "Each stage forms a square array of $n \\times n$ dots.",
            "The formula is $D = n^2$.",
            f"For Stage {stage_target}: $D = {stage_target}^2 = {ans_dots}$.",
        ],
        "misconception_tags": ["square_area_power_confusion"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_33_dot_pattern_l_shape_diagram(rng: random.Random) -> Dict[str, Any]:
    # L-shapes: Stage 1 = 1 dot, Stage 2 = 3 dots, Stage 3 = 5 dots (2n - 1)
    svg = draw_dot_pattern_stages_svg([1, 3, 5], seed=rng.randint(1, 1000000))
    stage_target = rng.choice([15, 20, 25])
    ans_dots = 2 * stage_target - 1

    return {
        "title": "L-Shaped Dot Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "33_dot_pattern_l_shape_diagram",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the figure showing L-shaped dot arrangements:\n\n"
            f"* Stage 1: 1 dot\n"
            f"* Stage 2: 3 dots\n"
            f"* Stage 3: 5 dots\n\n"
            f"Determine the number of dots in **Stage {stage_target}**."
        ),
        "correct_answer": str(ans_dots),
        "marking_schema": [
            "Identify odd number sequence with common difference d = 2 (1 mark)",
            f"Deduce general rule D = 2n - 1 (1 mark)",
            f"Evaluate Stage {stage_target}: 2({stage_target}) - 1 = {ans_dots} (1 mark)",
        ],
        "hints": [
            "The pattern forms consecutive odd numbers: 1, 3, 5, 7...",
            "Formula: $T_n = 2n - 1$.",
            f"For $n = {stage_target}$: $T_{{{stage_target}}} = 2({stage_target}) - 1 = {ans_dots}$.",
        ],
        "misconception_tags": ["odd_number_general_rule_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_34_dot_pattern_cross_plus_diagram(rng: random.Random) -> Dict[str, Any]:
    # Cross pattern: 1 center dot + 4 branches of length n -> 4n + 1 dots
    svg = draw_dot_pattern_stages_svg([5, 9, 13], seed=rng.randint(1, 1000000))
    stage_target = rng.choice([10, 14, 20])
    ans_dots = 4 * stage_target + 1

    return {
        "title": "Cross/Plus Dot Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "34_dot_pattern_cross_plus_diagram",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the figure showing expanding cross patterns formed by dots:\n\n"
            f"* Stage 1: 5 dots (1 center + 4 branches of 1)\n"
            f"* Stage 2: 9 dots (1 center + 4 branches of 2)\n"
            f"* Stage 3: 13 dots (1 center + 4 branches of 3)\n\n"
            f"Calculate the number of dots in **Stage {stage_target}**."
        ),
        "correct_answer": str(ans_dots),
        "marking_schema": [
            "Derive general formula D = 4n + 1 (1 mark)",
            f"Compute dots for n = {stage_target}: 4({stage_target}) + 1 = {ans_dots} (1 mark)",
        ],
        "hints": [
            "Notice that each branch grows by 1 dot per stage in 4 directions.",
            "Formula: $D = 4n + 1$.",
            f"For Stage {stage_target}: $D = 4({stage_target}) + 1 = {ans_dots}$.",
        ],
        "misconception_tags": ["cross_pattern_symmetry_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_35_tile_pattern_border_around_square_diagram(rng: random.Random) -> Dict[str, Any]:
    # Border of unit tiles around an n x n square: (n+2)^2 - n^2 = 4n + 4
    svg = draw_dot_pattern_stages_svg([8, 12, 16], kind="grid", seed=rng.randint(1, 1000000))
    n_size = rng.choice([5, 6, 8, 10])
    ans_border = 4 * n_size + 4

    return {
        "title": "Border Tile Pattern Around Square",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "35_tile_pattern_border_around_square_diagram",
        "difficulty": "hard",
        "question_text": (
            f"Consider square swimming pools surrounded by a single border of 1 m paving tiles:\n\n"
            f"* A pool of $1\\text{{ m}} \\times 1\\text{{ m}}$ ($n=1$) requires 8 border tiles\n"
            f"* A pool of $2\\text{{ m}} \\times 2\\text{{ m}}$ ($n=2$) requires 12 border tiles\n"
            f"* A pool of $3\\text{{ m}} \\times 3\\text{{ m}}$ ($n=3$) requires 16 border tiles\n\n"
            f"Derive the formula for border tiles $B$ and calculate the number of border tiles needed for a **{n_size} m by {n_size} m pool** ($n={n_size}$)."
        ),
        "correct_answer": str(ans_border),
        "marking_schema": [
            "Identify common difference d = 4 (1 mark)",
            "Derive rule B = 4n + 4 (1 mark)",
            f"Substitute n = {n_size}: 4({n_size}) + 4 = {ans_border} (1 mark)",
        ],
        "hints": [
            "Subtract consecutive tile counts: $12 - 8 = 4$.",
            "Rule: $B = 4n + 4$ (4 sides of length $n$ plus 4 corner tiles).",
            f"For $n = {n_size}$: $B = 4({n_size}) + 4 = {ans_border}$.",
        ],
        "misconception_tags": ["corner_tile_overlap_count_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_36_tile_pattern_two_color_ratio_progression(rng: random.Random) -> Dict[str, Any]:
    # Tile pattern with yellow center tiles (constant 4) and blue surrounding tiles (6n)
    n_stage = rng.choice([6, 8, 10])
    yellow_const = 4
    blue_rate = rng.choice([4, 6])
    ans_blue = blue_rate * n_stage

    return {
        "title": "Two-Color Tile Pattern Growth",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "36_tile_pattern_two_color_ratio_progression",
        "difficulty": "medium",
        "question_text": (
            f"Decorative floor designs combine yellow and blue tiles:\n\n"
            f"* Every design has a constant {yellow_const} yellow center tiles.\n"
            f"* The number of blue outer tiles grows according to the sequence: ${blue_rate};\\ {2 * blue_rate};\\ {3 * blue_rate};\\ \\dots$\n\n"
            f"Calculate the number of blue tiles required for **Design {n_stage}**."
        ),
        "correct_answer": str(ans_blue),
        "marking_schema": [
            f"Recognize blue tiles rule T_n = {blue_rate}n (1 mark)",
            f"Calculate for n = {n_stage}: {blue_rate}({n_stage}) = {ans_blue} (1 mark)",
        ],
        "hints": [
            f"The blue tiles increase by {blue_rate} in each design.",
            f"The rule for blue tiles is $B = {blue_rate}n$.",
            f"For Design {n_stage}: $B = {blue_rate} \\times {n_stage} = {ans_blue}$.",
        ],
        "misconception_tags": ["variable_vs_constant_tile_confusion"],
        "diagram_spec": None,
    }


def arch_37_perimeter_of_joined_unit_squares_in_row_diagram(rng: random.Random) -> Dict[str, Any]:
    # Perimeter of n unit squares in a row: P = 2n + 2
    svg = draw_matchstick_pattern_svg(shape="square", stages=3, seed=rng.randint(1, 1000000))
    n_squares = rng.choice([12, 16, 25, 40])
    ans_p = 2 * n_squares + 2

    return {
        "title": "Perimeter of Unit Squares in a Row",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "37_perimeter_of_joined_unit_squares_in_row_diagram",
        "difficulty": "medium",
        "question_text": (
            f"Study the diagram below showing adjacent unit blocks ($1\\text{{ cm}} \\times 1\\text{{ cm}}$) aligned side by side:\n\n"
            f"* 1 block: Perimeter = $4\\text{{ cm}}$\n"
            f"* 2 blocks: Perimeter = $6\\text{{ cm}}$\n"
            f"* 3 blocks: Perimeter = $8\\text{{ cm}}$\n\n"
            f"Calculate the outer boundary perimeter (in cm) of a chain containing **{n_squares} blocks**."
        ),
        "correct_answer": str(ans_p),
        "marking_schema": [
            "Derive perimeter formula P = 2n + 2 (2 marks)",
            f"Compute P for n = {n_squares}: 2({n_squares}) + 2 = {ans_p} cm (1 mark)",
        ],
        "hints": [
            "Each new square adds 2 units to the outer perimeter (top and bottom), while the 2 ends stay 1 unit each.",
            "Formula: $P = 2n + 2$.",
            f"For $n = {n_squares}$: $P = 2({n_squares}) + 2 = {ans_p}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["perimeter_internal_boundary_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_38_perimeter_of_joined_equilateral_triangles_diagram(rng: random.Random) -> Dict[str, Any]:
    # Perimeter of n equilateral unit triangles joined in a row: P = n + 2
    svg = draw_matchstick_pattern_svg(shape="triangle", stages=3, seed=rng.randint(1, 1000000))
    n_triangles = rng.choice([15, 20, 30])
    ans_p = n_triangles + 2

    return {
        "title": "Perimeter of Joined Equilateral Triangles",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "38_perimeter_of_joined_equilateral_triangles_diagram",
        "difficulty": "medium",
        "question_text": (
            f"Refer to the figure showing equilateral triangles with side length $1\\text{{ cm}}$ joined side-to-side:\n\n"
            f"* 1 triangle: Perimeter = $3\\text{{ cm}}$\n"
            f"* 2 triangles joined: Perimeter = $4\\text{{ cm}}$\n"
            f"* 3 triangles joined: Perimeter = $5\\text{{ cm}}$\n\n"
            f"Calculate the perimeter (in cm) for **{n_triangles} joined triangles**."
        ),
        "correct_answer": str(ans_p),
        "marking_schema": [
            "Identify progression with constant difference d = 1 (1 mark)",
            "Derive general term P = n + 2 (1 mark)",
            f"Evaluate for n = {n_triangles}: {n_triangles} + 2 = {ans_p} cm (1 mark)",
        ],
        "hints": [
            "Each additional triangle adds 1 unit of exposed perimeter.",
            "Formula: $P = n + 2$.",
            f"For $n = {n_triangles}$: $P = {n_triangles} + 2 = {ans_p}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["perimeter_triangle_chain_miscount"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_39_matchstick_count_for_specific_large_figure_number(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5])
    c = 1
    # M = d*n + c
    stage = rng.choice([50, 75, 100])
    ans_matches = d * stage + c

    return {
        "title": "Large Stage Matchstick Calculation (n = 50 or 100)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "39_matchstick_count_for_specific_large_figure_number",
        "difficulty": "hard",
        "question_text": (
            f"A geometric pattern rule is determined to be:\n\n"
            f"$$M = {d}n + {c}$$\n\n"
            f"where $M$ is the number of matchsticks and $n$ is the stage number.\n"
            f"Calculate the total number of matchsticks required to construct **Stage {stage}**."
        ),
        "correct_answer": str(ans_matches),
        "marking_schema": [
            f"Substitute n = {stage} into M = {d}n + {c} (1 mark)",
            f"Compute M = {d}({stage}) + {c} = {ans_matches} (1 mark)",
        ],
        "hints": [
            f"Replace $n$ with {stage} in the formula.",
            f"$M = {d} \\times {stage} + {c}$.",
            f"$M = {d * stage} + {c} = {ans_matches}$.",
        ],
        "misconception_tags": ["large_number_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_40_figure_number_from_total_matchsticks_budget(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5])
    c = 1
    n_stage = rng.randint(25, 60)
    total_m = d * n_stage + c

    return {
        "title": "Finding Figure Number from Matchstick Budget",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "40_figure_number_from_total_matchsticks_budget",
        "difficulty": "hard",
        "question_text": (
            f"A learner has a box containing **{total_m} matchsticks**.\n"
            f"The pattern requires $M = {d}n + {c}$ matchsticks for Stage $n$.\n"
            f"If all {total_m} matchsticks are used, determine which **Stage number ($n$)** was constructed."
        ),
        "correct_answer": str(n_stage),
        "marking_schema": [
            f"Set up equation {d}n + {c} = {total_m} (1 mark)",
            f"Solve for n: {d}n = {total_m - c} => n = {n_stage} (2 marks)",
        ],
        "hints": [
            f"Set the formula equal to {total_m}: ${d}n + {c} = {total_m}$.",
            f"Subtract {c}: ${d}n = {total_m - c}$.",
            f"Divide by {d}: $n = \\frac{{{total_m - c}}}{{{d}}} = {n_stage}$.",
        ],
        "misconception_tags": ["equation_inverse_operations_error"],
        "diagram_spec": None,
    }


def arch_41_parking_fee_or_taxi_fare_linear_pattern_context(rng: random.Random) -> Dict[str, Any]:
    fixed = rng.randint(10, 25)
    hourly = rng.randint(5, 12)
    hours = rng.randint(4, 9)
    total_cost = fixed + hourly * hours

    return {
        "title": "Real-World Linear Pattern (Parking Fee)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "41_parking_fee_or_taxi_fare_linear_pattern_context",
        "difficulty": "medium",
        "question_text": (
            f"A parking garage charges an entry fee of $\\text{{R}}{fixed}$ plus $\\text{{R}}{hourly}$ for every hour parked.\n\n"
            f"Determine the general formula $C = {hourly}h + {fixed}$ for the total cost $C$ after $h$ hours, "
            f"and calculate the total parking fee (in Rand) for **{hours} hours**."
        ),
        "correct_answer": f"R{total_cost}",
        "marking_schema": [
            f"Set up linear cost formula C = {hourly}h + {fixed} (1 mark)",
            f"Substitute h = {hours}: C = {hourly}({hours}) + {fixed} = {total_cost} (1 mark)",
        ],
        "hints": [
            f"The cost increases by R{hourly} per hour from a base fee of R{fixed}.",
            f"Multiply {hourly} by {hours} hours: R{hourly * hours}.",
            f"Add the fixed entry fee of R{fixed}: $\\text{{R}}{hourly * hours} + \\text{{R}}{fixed} = \\text{{R}}{total_cost}$.",
        ],
        "misconception_tags": ["fixed_vs_variable_cost_confusion"],
        "diagram_spec": None,
    }


def arch_42_cellphone_call_cost_fixed_plus_per_minute_pattern(rng: random.Random) -> Dict[str, Any]:
    base_sub = rng.choice([50, 99, 150])
    rate_pm = rng.choice([1.5, 2.0, 2.5])
    mins = rng.choice([30, 40, 50, 60])
    total = base_sub + rate_pm * mins
    rate_str = str(rate_pm).replace(".", ",")

    return {
        "title": "Cellphone Tariff Linear Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "42_cellphone_call_cost_fixed_plus_per_minute_pattern",
        "difficulty": "medium",
        "question_text": (
            f"A cellphone contract has a monthly subscription of $\\text{{R}}{base_sub}$ plus a call charge of $\\text{{R}}{rate_str}$ per minute.\n\n"
            f"Calculate the total account (in Rand) for a month in which **{mins} minutes** of calls were made."
        ),
        "correct_answer": f"R{int(total) if total.is_integer() else total}",
        "marking_schema": [
            f"Compute call charges: {mins} * {rate_str} = R{int(rate_pm * mins)} (1 mark)",
            f"Add subscription: R{base_sub} + R{int(rate_pm * mins)} = R{int(total)} (1 mark)",
        ],
        "hints": [
            f"Call cost = ${mins} \\times \\text{{R}}{rate_str} = \\text{{R}}{int(rate_pm * mins)}$.",
            f"Add base fee: $\\text{{R}}{base_sub} + \\text{{R}}{int(rate_pm * mins)} = \\text{{R}}{int(total)}$.",
        ],
        "misconception_tags": ["rate_multiplication_error"],
        "diagram_spec": None,
    }


def arch_43_water_tank_draining_or_filling_rate_pattern(rng: random.Random) -> Dict[str, Any]:
    initial = rng.randint(400, 800)
    drain_rate = rng.randint(15, 35)
    hours = rng.randint(3, 8)
    remaining = initial - drain_rate * hours

    return {
        "title": "Water Tank Draining Pattern (Negative Rate)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "43_water_tank_draining_or_filling_rate_pattern",
        "difficulty": "medium",
        "question_text": (
            f"A water reservoir contains **{initial} litres** of water. Water is pumped out at a constant rate of **{drain_rate} litres per hour**.\n\n"
            f"Determine the volume of water remaining in the tank after **{hours} hours**."
        ),
        "correct_answer": str(remaining),
        "marking_schema": [
            f"Calculate volume drained: {drain_rate} * {hours} = {drain_rate * hours} L (1 mark)",
            f"Calculate remaining volume: {initial} - {drain_rate * hours} = {remaining} L (1 mark)",
        ],
        "hints": [
            f"Formula: $V = {initial} - {drain_rate}t$.",
            f"Water drained in {hours} hours = ${drain_rate} \\times {hours} = {drain_rate * hours}\\text{{ L}}$.",
            f"Remaining water = ${initial} - {drain_rate * hours} = {remaining}\\text{{ L}}$.",
        ],
        "misconception_tags": ["rate_subtraction_reversal_error"],
        "diagram_spec": None,
    }


def arch_44_savings_account_constant_weekly_deposit_pattern(rng: random.Random) -> Dict[str, Any]:
    initial = rng.randint(50, 200)
    weekly = rng.randint(20, 50)
    weeks = rng.randint(8, 16)
    total_savings = initial + weekly * weeks

    return {
        "title": "Weekly Savings Growth Pattern",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "44_savings_account_constant_weekly_deposit_pattern",
        "difficulty": "easy",
        "question_text": (
            f"A learner opens a savings account with an opening balance of $\\text{{R}}{initial}$ and deposits $\\text{{R}}{weekly}$ every week.\n\n"
            f"Calculate the total savings (in Rand) accumulated after **{weeks} weeks**."
        ),
        "correct_answer": f"R{total_savings}",
        "marking_schema": [
            f"Calculate total weekly deposits: {weekly} * {weeks} = R{weekly * weeks} (1 mark)",
            f"Add opening balance: R{initial} + R{weekly * weeks} = R{total_savings} (1 mark)",
        ],
        "hints": [
            f"Weekly savings = ${weekly} \\times {weeks} = \\text{{R}}{weekly * weeks}$.",
            f"Total = $\\text{{R}}{initial} + \\text{{R}}{weekly * weeks} = \\text{{R}}{total_savings}$.",
        ],
        "misconception_tags": ["arithmetic_savings_slip"],
        "diagram_spec": None,
    }


def arch_45_comparing_two_growth_patterns_break_even_stage(rng: random.Random) -> Dict[str, Any]:
    # Option A: 20 + 5n
    # Option B: 50 + 2n
    # Break even: 20 + 5n = 50 + 2n => 3n = 30 => n = 10
    n_break = rng.choice([5, 8, 10, 12])
    diff_rate = rng.choice([2, 3, 4])
    base_a = 15
    base_b = base_a + diff_rate * n_break
    rate_a = 8
    rate_b = rate_a - diff_rate

    # Option A: C_A = rate_a * n + base_a
    # Option B: C_B = rate_b * n + base_b
    # At n_break, rate_a * n + base_a = rate_b * n + base_b

    return {
        "title": "Comparing Two Patterns (Break-Even Stage)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "45_comparing_two_growth_patterns_break_even_stage",
        "difficulty": "hard",
        "question_text": (
            f"Two gym payment plans offer the following rates:\n\n"
            f"* **Plan A:** $\\text{{R}}{base_a}$ joining fee + $\\text{{R}}{rate_a}$ per visit\n"
            f"* **Plan B:** $\\text{{R}}{base_b}$ joining fee + $\\text{{R}}{rate_b}$ per visit\n\n"
            f"Calculate the number of visits ($n$) for which both plans cost exactly the same amount."
        ),
        "correct_answer": str(n_break),
        "marking_schema": [
            f"Set up equation {rate_a}n + {base_a} = {rate_b}n + {base_b} (1 mark)",
            f"Solve for n: {diff_rate}n = {base_b - base_a} => n = {n_break} (2 marks)",
        ],
        "hints": [
            f"Set the two costs equal: ${rate_a}n + {base_a} = {rate_b}n + {base_b}$.",
            f"Subtract ${rate_b}n$ from both sides: ${diff_rate}n + {base_a} = {base_b}$.",
            f"Subtract ${base_a}$: ${diff_rate}n = {base_b - base_a}$, so $n = {n_break}$.",
        ],
        "misconception_tags": ["simultaneous_pattern_comparison_error"],
        "diagram_spec": None,
    }


def arch_46_geometric_sequence_general_term_powers_of_two(rng: random.Random) -> Dict[str, Any]:
    # 2, 4, 8, 16, 32... T_n = 2^n
    terms = [2 ** n for n in range(1, 6)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_formula = "T_n = 2^n"

    return {
        "title": "General Term Formula (Powers of 2)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "46_geometric_sequence_general_term_powers_of_two",
        "difficulty": "medium",
        "question_text": (
            f"Consider the doubling sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Write down the general term formula ($T_n$) in terms of position $n$."
        ),
        "correct_answer": ans_formula,
        "marking_schema": [
            "Identify repeated multiplication by 2 (1 mark)",
            "State general term T_n = 2^n (1 mark)",
        ],
        "hints": [
            "Notice $T_1 = 2^1 = 2$, $T_2 = 2^2 = 4$, $T_3 = 2^3 = 8$.",
            "The base is 2 and the exponent is the position $n$.",
            "Therefore, $T_n = 2^n$.",
        ],
        "misconception_tags": ["linear_vs_exponential_rule_confusion"],
        "diagram_spec": None,
    }


def arch_47_geometric_sequence_general_term_powers_of_three(rng: random.Random) -> Dict[str, Any]:
    # 3, 9, 27, 81... T_n = 3^n
    terms = [3 ** n for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_formula = "T_n = 3^n"

    return {
        "title": "General Term Formula (Powers of 3)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "47_geometric_sequence_general_term_powers_of_three",
        "difficulty": "medium",
        "question_text": (
            f"Consider the tripling sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Formulate the general term ($T_n$) in terms of $n$."
        ),
        "correct_answer": ans_formula,
        "marking_schema": [
            "Identify repeated tripling by 3 (1 mark)",
            "State general formula T_n = 3^n (1 mark)",
        ],
        "hints": [
            "Observe: $T_1 = 3^1, T_2 = 3^2, T_3 = 3^3, T_4 = 3^4$.",
            "Each term is 3 raised to the power $n$.",
            "The formula is $T_n = 3^n$.",
        ],
        "misconception_tags": ["powers_of_three_base_error"],
        "diagram_spec": None,
    }


def arch_48_quadratic_pattern_shifted_squares_general_formula(rng: random.Random) -> Dict[str, Any]:
    shift = rng.choice([1, 2, 3])
    terms = [(n ** 2) + shift for n in range(1, 6)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    ans_formula = f"T_n = n^2 + {shift}"

    return {
        "title": "General Term of Shifted Square Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "48_quadratic_pattern_shifted_squares_general_formula",
        "difficulty": "hard",
        "question_text": (
            f"A sequence of numbers is given by:\n\n"
            f"$${seq_str}$$\n\n"
            f"Notice that the first differences are not constant. Compare each term to the perfect square numbers ($1, 4, 9, 16, 25\\dots$) "
            f"and write down the general rule $T_n$ in terms of $n$."
        ),
        "correct_answer": ans_formula,
        "marking_schema": [
            "Recognize perfect squares offset by constant (1 mark)",
            f"State general rule T_n = n^2 + {shift} (2 marks)",
        ],
        "hints": [
            f"Compare $T_1 = {terms[0]}$ to $1^2 = 1$: difference is +{shift}.",
            f"Compare $T_2 = {terms[1]}$ to $2^2 = 4$: difference is +{shift}.",
            f"Each term is $n^2 + {shift}$.",
        ],
        "misconception_tags": ["quadratic_shift_miscalculation"],
        "diagram_spec": None,
    }


def arch_49_cubic_pattern_shifted_cubes_general_formula(rng: random.Random) -> Dict[str, Any]:
    shift = rng.choice([1, -1])
    terms = [(n ** 3) + shift for n in range(1, 5)]
    seq_str = "; ".join(str(t) for t in terms) + "; \\dots"
    sign_str = f"+ {shift}" if shift > 0 else "- 1"
    ans_formula = f"T_n = n^3 {sign_str}"

    return {
        "title": "General Term of Shifted Cube Sequence",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "49_cubic_pattern_shifted_cubes_general_formula",
        "difficulty": "hard",
        "question_text": (
            f"Examine the sequence:\n\n"
            f"$${seq_str}$$\n\n"
            f"Compare each term to the cubes of natural numbers ($1^3=1, 2^3=8, 3^3=27, 4^3=64$) "
            f"and formulate the general rule $T_n$ in terms of $n$."
        ),
        "correct_answer": ans_formula,
        "marking_schema": [
            "Recognize cubic base numbers n^3 (1 mark)",
            f"Identify offset {sign_str} (1 mark)",
            f"State general term T_n = n^3 {sign_str} (1 mark)",
        ],
        "hints": [
            f"Evaluate $n^3$: $1^3=1, 2^3=8, 3^3=27, 4^3=64$.",
            f"Observe that every term is exactly {abs(shift)} {'greater' if shift > 0 else 'less'} than $n^3$.",
            f"Therefore, $T_n = n^3 {sign_str}$.",
        ],
        "misconception_tags": ["cube_offset_sign_error"],
        "diagram_spec": None,
    }


def arch_50_pattern_representation_translation_table_rule_graph(rng: random.Random) -> Dict[str, Any]:
    m = rng.randint(2, 5)
    c = rng.randint(1, 4)
    # y = mx + c
    x_val = 6
    ans_val = m * x_val + c

    return {
        "title": "Pattern Representation Translation (Rule to Calculation)",
        "topic": "Numeric and geometric patterns",
        "grade": 8,
        "term": 1,
        "subskill": "50_pattern_representation_translation_table_rule_graph",
        "difficulty": "medium",
        "question_text": (
            f"A pattern is represented in three equivalent mathematical forms:\n\n"
            f"1. **Verbal:** Start with ${c}$ and add ${m}$ for every step.\n"
            f"2. **Algebraic rule:** $y = {m}x + {c}$\n"
            f"3. **Table:** $(1; {m+c}), (2; {2*m+c}), (3; {3*m+c})$\n\n"
            f"Calculate the value of $y$ when $x = {x_val}$."
        ),
        "correct_answer": str(ans_val),
        "marking_schema": [
            f"Substitute x = {x_val} into y = {m}x + {c} (1 mark)",
            f"Compute y = {m}({x_val}) + {c} = {ans_val} (1 mark)",
        ],
        "hints": [
            f"Use the algebraic rule $y = {m}x + {c}$.",
            f"Substitute $x = {x_val}$: $y = {m}({x_val}) + {c}$.",
            f"$y = {m * x_val} + {c} = {ans_val}$.",
        ],
        "misconception_tags": ["multiple_representations_translation_error"],
        "diagram_spec": None,
    }
