import random
from typing import Dict, Any, List

SUBSKILLS = ['translation', 'reflection_x', 'reflection_y', 'lines_of_symmetry', 'enlargement_scale_factor']

class SeniorPhaseTransformationsGenerator:
    """Generator for Grade 7, 8, and 9 Transformations."""
    SUBSKILLS = SUBSKILLS
    
    def _generate_one(self, rng: random.Random, subskill: str, grade: int = 7) -> Dict[str, Any]:
        x = rng.randint(-8, 8)
        y = rng.randint(-8, 8)
        
        if subskill == 'translation':
            dx = rng.choice([-4, -3, -2, 2, 3, 4])
            dy = rng.choice([-4, -3, -2, 2, 3, 4])
            x_new = x + dx
            y_new = y + dy
            dir_x = f"{abs(dx)} units {'right' if dx > 0 else 'left'}"
            dir_y = f"{abs(dy)} units {'up' if dy > 0 else 'down'}"
            question = f"Point A({x}; {y}) is translated {dir_x} and {dir_y}. Determine the coordinates of image A'. (Format as '(x; y)', e.g. '(2; -3)')."
            steps = [
                f"\\text{{Translation rule: }} (x; y) \\rightarrow (x {dx:+}; y {dy:+})",
                f"A' = ({x} {dx:+}; {y} {dy:+})",
                f"A' = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            memo = f"1. Translation rule: $(x {dx:+}; y {dy:+})$ [1]\n2. Image coordinates: $({x_new}; {y_new})$ [1]"
            hints = {
                "tier_1": "Apply the translation to the x and y coordinates respectively.",
                "tier_2": f"Add {dx} to {x} and {dy} to {y}.",
                "tier_3": f"A' = ({x_new}; {y_new})."
            }
        elif subskill == 'reflection_x':
            x_new = x
            y_new = -y
            question = f"Point B({x}; {y}) is reflected across the x-axis. Determine the coordinates of image B'. (Format as '(x; y)', e.g. '(2; -3)')."
            steps = [
                f"\\text{{Reflection across x-axis rule: }} (x; y) \\rightarrow (x; -y)",
                f"B' = ({x}; -({y})) = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            memo = f"1. Rule: $(x; -y)$ [1]\n2. Image coordinates: $({x_new}; {y_new})$ [1]"
            hints = {
                "tier_1": "When reflecting across the x-axis, x stays the same and y inverts sign.",
                "tier_2": f"Change sign of y={y}: -({y}) = {y_new}.",
                "tier_3": f"B' = ({x_new}; {y_new})."
            }
        elif subskill == 'reflection_y':
            x_new = -x
            y_new = y
            question = f"Point C({x}; {y}) is reflected across the y-axis. Determine the coordinates of image C'. (Format as '(x; y)', e.g. '(2; -3)')."
            steps = [
                f"\\text{{Reflection across y-axis rule: }} (x; y) \\rightarrow (-x; y)",
                f"C' = (-({x}); {y}) = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            memo = f"1. Rule: $(-x; y)$ [1]\n2. Image coordinates: $({x_new}; {y_new})$ [1]"
            hints = {
                "tier_1": "When reflecting across the y-axis, y stays the same and x inverts sign.",
                "tier_2": f"Change sign of x={x}: -({x}) = {x_new}.",
                "tier_3": f"C' = ({x_new}; {y_new})."
            }
        elif subskill == 'lines_of_symmetry':
            shapes = [
                ("an equilateral triangle", 3),
                ("a rectangle", 2),
                ("a square", 4),
                ("an isosceles triangle", 1),
                ("a regular hexagon", 6)
            ]
            s_name, s_count = rng.choice(shapes)
            question = f"How many lines of symmetry does {s_name} have?"
            ans_str = str(s_count)
            steps = [
                f"\\text{{A line of symmetry folds the shape into two matching halves.}}",
                f"\\text{{{s_name.capitalize()} has exactly {s_count} lines of symmetry.}}"
            ]
            memo = f"1. Recognition of symmetry properties [1]\n2. Number of lines of symmetry: {s_count} [1]"
            hints = {
                "tier_1": "Think about how many ways you can fold the shape so both halves match exactly.",
                "tier_2": f"{s_name.capitalize()} has lines through sides or vertices.",
                "tier_3": f"Answer: {s_count} lines."
            }
        else: # enlargement_scale_factor
            subskill = 'enlargement_scale_factor'
            base_len = rng.randint(3, 10)
            k = rng.choice([2, 3, 4])
            new_len = base_len * k
            question = f"A rectangle has side length {base_len} cm. It is enlarged by a scale factor of $k = {k}$. Calculate the side length of the enlarged image."
            steps = [
                f"\\text{{Image side length}} = \\text{{Original length}} \\times k",
                f"\\text{{Image side length}} = {base_len} \\times {k} = {new_len} \\text{{ cm}}"
            ]
            ans_str = f"{new_len} cm"
            memo = f"1. Multiplication by scale factor: ${base_len} \\times {k}$ [1]\n2. Calculated length: ${new_len} \\text{{ cm}}$ [1]"
            hints = {
                "tier_1": "Multiply the original length by the scale factor k.",
                "tier_2": f"Calculate {base_len} × {k}.",
                "tier_3": f"Image length = {new_len} cm."
            }

        qid = f"g{grade}_trans_{rng.randint(100000, 999999)}"
        diag_spec = {
            "kind": "coordinate_transformation" if subskill in ("translation", "reflection_x", "reflection_y") else "geometry_diagram",
            "diagram_role": "context",
            "subskill": subskill,
            "points": {"P": [x, y]} if subskill in ("translation", "reflection_x", "reflection_y") else {},
            "grid": {"x_min": -10, "x_max": 10, "y_min": -10, "y_max": 10}
        }
        return {
            "id": qid,
            "question_id": qid,
            "question": question,
            "prompt": question,
            "question_type": "short_answer",
            "modality": "math",
            "diagram_spec": diag_spec,
            "solution_steps": steps,
            "worked_solution": memo,
            "canonical_solution": {
                "steps": steps,
                "final_latex": ans_str,
            },
            "sample_answer": ans_str,
            "correct_answer": ans_str,
            "explanation": memo,
            "solution": memo,
            "marks": 2,
            "total_marks": 2,
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": subskill,
            "hints": hints,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp1", "desc": "Method / geometric rule applied", "marks": 1, "editable": True},
                    {"id": "mp2", "desc": f"Accurate final answer: {ans_str}", "marks": 1, "editable": True},
                ]
            },
            "misconception_tags": [
                "confuses_x_and_y_reflection",
                "adds_scale_factor_instead_of_multiplying",
            ],
            "difficulty": "medium",
            "stage_metadata": {"grade": grade, "subskill": subskill}
        }

    def generate(self, grade: int = 7, mode: str = "transformations", seed: int = None, count: int = 1, subskill: str = None, **kwargs) -> List[Dict[str, Any]]:
        rng = random.Random(seed) if seed is not None else random.Random()
        questions = []
        target_sub = str(subskill or "").strip().lower()
        for i in range(count):
            if target_sub in SUBSKILLS:
                cur_sub = target_sub
            else:
                cur_sub = SUBSKILLS[i % len(SUBSKILLS)]
            questions.append(self._generate_one(rng, cur_sub, grade=grade))
        return questions
