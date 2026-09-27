import random
from typing import Dict, Any, List

class SeniorPhaseGeometryGenerator:
    """Generator for Grade 7, 8, and 9 Straight lines & 2D/3D properties."""
    
    def generate(self, grade: int, mode: str, seed: int = None) -> Dict[str, Any]:
        rng = random.Random(seed)
        
        # Subskills: angles_on_line, vertically_opposite, alternate_angles
        subskills = ['angles_on_line', 'vertically_opposite', 'alternate_angles']
        subskill = rng.choice(subskills)
        
        if subskill == 'angles_on_line':
            angle1 = rng.randint(30, 150)
            angle2 = 180 - angle1
            question = f"Angles on a straight line add up to 180^\\circ. If one angle is {angle1}^\\circ, calculate the size of the adjacent angle $x$."
            steps = [
                f"x + {angle1}^\\circ = 180^\\circ \\quad \\text{{(Angles on a straight line)}}",
                f"x = 180^\\circ - {angle1}^\\circ",
                f"x = {angle2}^\\circ"
            ]
            ans_str = f"{angle2}^\\circ"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Remember that adjacent angles on a straight line add up to 180 degrees."]
            }
            
        elif subskill == 'vertically_opposite':
            angle = rng.randint(40, 140)
            question = f"Two straight lines intersect. If one angle is {angle}^\\circ, calculate the size of its vertically opposite angle $y$."
            steps = [
                f"y = {angle}^\\circ \\quad \\text{{(Vertically opposite angles are equal)}}"
            ]
            ans_str = f"{angle}^\\circ"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Vertically opposite angles are equal."]
            }
            
        else: # alternate_angles
            angle = rng.randint(50, 130)
            question = f"Two parallel lines are cut by a transversal. If one angle is {angle}^\\circ, calculate the size of its alternate angle $z$."
            steps = [
                f"z = {angle}^\\circ \\quad \\text{{(Alternate angles, parallel lines)}}"
            ]
            ans_str = f"{angle}^\\circ"
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["Alternate angles between parallel lines are equal. Look for the 'Z' shape."]
            }
