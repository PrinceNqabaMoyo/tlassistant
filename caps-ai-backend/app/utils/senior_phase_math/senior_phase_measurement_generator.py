import random
import sympy as sp
from typing import Dict, Any, List

SUBSKILLS = ['2d_rectangle', '2d_triangle', '2d_circle', '3d_prism', '3d_cylinder']

class SeniorPhaseMeasurementGenerator:
    """Generator for Grade 7, 8, and 9 Perimeter, Area, Surface Area & Volume."""
    SUBSKILLS = SUBSKILLS
    
    def _generate_one(self, rng: random.Random, subskill: str, grade: int = 7) -> Dict[str, Any]:
        if subskill == '2d_rectangle':
            l = rng.randint(5, 20)
            b = rng.randint(3, 15)
            area = l * b
            question = f"Calculate the area of a rectangle with length {l} cm and breadth {b} cm."
            steps = [
                f"\\text{{Area}} = l \\times b",
                f"\\text{{Area}} = {l} \\times {b}",
                f"\\text{{Area}} = {area} \\text{{ cm}}^2"
            ]
            ans_str = f"{area} cm^2"
            memo = f"1. Formula and substitution: $\\text{{Area}} = {l} \\times {b}$ [1]\n2. Calculated area: ${area} \\text{{ cm}}^2$ [1]"
            hints = {
                "tier_1": "Use the formula for the area of a rectangle: Area = length × breadth.",
                "tier_2": f"Multiply {l} by {b}.",
                "tier_3": f"Area = {area} cm^2."
            }
        elif subskill == '2d_triangle':
            base = rng.randint(4, 18)
            height = rng.randint(5, 20)
            area = 0.5 * base * height
            ans_val = f"{area:.2f}".rstrip('0').rstrip('.').replace('.', '{,}')
            question = f"Calculate the area of a triangle with a base of {base} cm and a perpendicular height of {height} cm."
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times b \\times h",
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times {base} \\times {height}",
                f"\\text{{Area}} = {ans_val} \\text{{ cm}}^2"
            ]
            ans_str = f"{ans_val} cm^2"
            memo = f"1. Formula and substitution: $\\frac{{1}}{{2}} \\times {base} \\times {height}$ [1]\n2. Calculated area: ${ans_val} \\text{{ cm}}^2$ [1]"
            hints = {
                "tier_1": "Use the formula for the area of a triangle: Area = 1/2 × base × height.",
                "tier_2": f"Multiply 1/2 × {base} × {height}.",
                "tier_3": f"Area = {ans_val} cm^2."
            }
        elif subskill == '2d_circle':
            r = rng.randint(3, 14)
            c = round(2 * 3.14 * r, 2)
            c_str = f"{c:.2f}".rstrip('0').rstrip('.').replace('.', '{,}')
            question = f"Calculate the circumference of a circle with radius $r = {r}\\text{{ cm}}$. (Use $\\pi \\approx 3,14$)"
            steps = [
                f"C = 2\\pi r",
                f"C = 2 \\times 3,14 \\times {r}",
                f"C \\approx {c_str} \\text{{ cm}}"
            ]
            ans_str = f"{c_str} cm"
            memo = f"1. Formula and substitution: $2 \\times 3,14 \\times {r}$ [1]\n2. Calculated circumference: ${c_str} \\text{{ cm}}$ [1]"
            hints = {
                "tier_1": "Use the circumference formula: C = 2πr.",
                "tier_2": f"Multiply 2 × 3,14 × {r}.",
                "tier_3": f"C = {c_str} cm."
            }
        elif subskill == '3d_prism':
            l = rng.randint(4, 15)
            w = rng.randint(3, 10)
            h = rng.randint(5, 20)
            vol = l * w * h
            question = f"Calculate the volume of a rectangular prism with length {l} cm, width {w} cm, and height {h} cm."
            steps = [
                f"\\text{{Volume}} = l \\times w \\times h",
                f"\\text{{Volume}} = {l} \\times {w} \\times {h}",
                f"\\text{{Volume}} = {vol} \\text{{ cm}}^3"
            ]
            ans_str = f"{vol} cm^3"
            memo = f"1. Formula and substitution: ${l} \\times {w} \\times {h}$ [1]\n2. Calculated volume: ${vol} \\text{{ cm}}^3$ [1]"
            hints = {
                "tier_1": "Use the formula for the volume of a rectangular prism: Volume = length × width × height.",
                "tier_2": f"Multiply {l} × {w} × {h}.",
                "tier_3": f"Volume = {vol} cm^3."
            }
        else: # 3d_cylinder
            subskill = '3d_cylinder'
            r = rng.randint(2, 10)
            h = rng.randint(5, 20)
            vol = sp.pi * r**2 * h
            vol_float = float(vol)
            ans_val = f"{vol_float:.2f}".replace('.', '{,}')
            question = f"Calculate the volume of a cylinder with radius $r = {r}\\text{{ cm}}$ and height $h = {h}\\text{{ cm}}$. (Use $\\pi \\approx 3,14159$)"
            steps = [
                f"\\text{{Volume}} = \\pi r^2 h",
                f"\\text{{Volume}} = \\pi ({r})^2 ({h})",
                f"\\text{{Volume}} = {r**2 * h}\\pi",
                f"\\text{{Volume}} \\approx {ans_val} \\text{{ cm}}^3"
            ]
            ans_str = f"{ans_val} cm^3"
            memo = f"1. Formula and substitution: $\\pi \\times {r}^2 \\times {h}$ [1]\n2. Calculated volume: ${ans_val} \\text{{ cm}}^3$ [1]"
            hints = {
                "tier_1": "Use the formula for the volume of a cylinder: Volume = π × r^2 × h.",
                "tier_2": f"Calculate π × {r}^2 × {h}.",
                "tier_3": f"Volume = {ans_val} cm^3."
            }

        qid = f"g{grade}_meas_{rng.randint(100000, 999999)}"
        return {
            "id": qid,
            "question_id": qid,
            "question": question,
            "prompt": question,
            "question_type": "short_answer",
            "modality": "math",
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
                    {"id": "mp1", "desc": "Correct geometric formula and substitution", "marks": 1, "editable": True},
                    {"id": "mp2", "desc": f"Accurate calculation: {ans_str}", "marks": 1, "editable": True},
                ]
            },
            "misconception_tags": [
                "confuses_perimeter_and_area",
                "confuses_surface_area_and_volume",
            ],
            "difficulty": "medium",
            "stage_metadata": {"grade": grade, "subskill": subskill}
        }

    def generate(self, grade: int = 7, mode: str = "measurement", seed: int = None, count: int = 1, subskill: str = None, **kwargs) -> List[Dict[str, Any]]:
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
