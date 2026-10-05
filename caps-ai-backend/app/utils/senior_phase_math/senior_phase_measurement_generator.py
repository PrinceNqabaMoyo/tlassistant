import random
import sympy as sp
from typing import Dict, Any, List

class SeniorPhaseMeasurementGenerator:
    """Generator for Grade 7, 8, and 9 Perimeter, Area, Surface Area & Volume."""
    
    def generate(self, grade: int = 7, mode: str = "measurement", seed: int = None) -> Dict[str, Any]:
        rng = random.Random(seed)
        
        # Determine 2D vs 3D based on mode and grade, simplify by randomly choosing subskill
        subskills = ['2d_rectangle', '2d_triangle', '3d_prism', '3d_cylinder']
        subskill = rng.choice(subskills)
        
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
            ans_str = str(area)
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Use the formula for the area of a rectangle: Area = length × breadth."]
            }
            
        elif subskill == '2d_triangle':
            base = rng.randint(4, 18)
            height = rng.randint(5, 20)
            area = 0.5 * base * height
            question = f"Calculate the area of a triangle with a base of {base} cm and a perpendicular height of {height} cm."
            ans_str = f"{area:.2f}".rstrip('0').rstrip('.').replace('.', '{,}')
            steps = [
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times b \\times h",
                f"\\text{{Area}} = \\frac{{1}}{{2}} \\times {base} \\times {height}",
                f"\\text{{Area}} = {ans_str} \\text{{ cm}}^2"
            ]
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Use the formula for the area of a triangle: Area = 1/2 × base × height."]
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
            ans_str = str(vol)
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Use the formula for the volume of a rectangular prism: Volume = length × width × height."]
            }
            
        else: # 3d_cylinder
            r = rng.randint(2, 10)
            h = rng.randint(5, 20)
            vol = sp.pi * r**2 * h
            vol_float = float(vol)
            ans_str = f"{vol_float:.2f}".replace('.', '{,}')
            question = f"Calculate the volume of a cylinder with a radius of {r} cm and a height of {h} cm. (Use $\\pi \\approx 3,14159$)"
            steps = [
                f"\\text{{Volume}} = \\pi r^2 h",
                f"\\text{{Volume}} = \\pi ({r})^2 ({h})",
                f"\\text{{Volume}} = {r**2 * h}\\pi",
                f"\\text{{Volume}} \\approx {ans_str} \\text{{ cm}}^3"
            ]
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Use the formula for the volume of a cylinder: Volume = pi × r^2 × h."]
            }
