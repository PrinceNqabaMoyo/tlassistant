import random
from typing import Dict, Any, List

class SeniorPhaseTransformationsGenerator:
    """Generator for Grade 7, 8, and 9 Transformations."""
    
    def generate(self, grade: int = 7, mode: str = "transformations", seed: int = None) -> Dict[str, Any]:
        rng = random.Random(seed)
        
        # Subskills: translation, reflection_x, reflection_y
        subskills = ['translation', 'reflection_x', 'reflection_y']
        subskill = rng.choice(subskills)
        
        x = rng.randint(-10, 10)
        y = rng.randint(-10, 10)
        
        if subskill == 'translation':
            dx = rng.randint(-5, 5)
            dy = rng.randint(-5, 5)
            while dx == 0 and dy == 0:
                dx = rng.randint(-5, 5)
            
            x_new = x + dx
            y_new = y + dy
            
            dir_x = f"{abs(dx)} units {'right' if dx > 0 else 'left'}" if dx != 0 else ""
            dir_y = f"{abs(dy)} units {'up' if dy > 0 else 'down'}" if dy != 0 else ""
            
            translation_desc = " and ".join(filter(None, [dir_x, dir_y]))
            
            question = f"Point A({x}; {y}) is translated {translation_desc}. Determine the coordinates of the image A'."
            steps = [
                f"\\text{{The rule for this translation is: }} (x; y) \\rightarrow (x {dx:+}; y {dy:+})",
                f"A' = ({x} {dx:+}; {y} {dy:+})",
                f"A' = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Apply the translation to the x and y coordinates respectively."]
            }
            
        elif subskill == 'reflection_x':
            x_new = x
            y_new = -y
            question = f"Point B({x}; {y}) is reflected across the x-axis. Determine the coordinates of the image B'."
            steps = [
                f"\\text{{The rule for reflection across the x-axis is: }} (x; y) \\rightarrow (x; -y)",
                f"B' = ({x}; -({y}))",
                f"B' = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["When reflecting across the x-axis, the x-coordinate stays the same, and the y-coordinate changes its sign."]
            }
            
        else: # reflection_y
            x_new = -x
            y_new = y
            question = f"Point C({x}; {y}) is reflected across the y-axis. Determine the coordinates of the image C'."
            steps = [
                f"\\text{{The rule for reflection across the y-axis is: }} (x; y) \\rightarrow (-x; y)",
                f"C' = (-({x}); {y})",
                f"C' = ({x_new}; {y_new})"
            ]
            ans_str = f"({x_new}; {y_new})"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["When reflecting across the y-axis, the y-coordinate stays the same, and the x-coordinate changes its sign."]
            }
