import random
import sympy as sp
from typing import Dict, Any, List

class SeniorPhasePythagorasGenerator:
    """Generator for Grade 8 and 9 Theorem of Pythagoras."""
    
    def generate(self, grade: int, mode: str, seed: int = None) -> Dict[str, Any]:
        rng = random.Random(seed)
        
        # Subskills: hypotenuse, shorter_leg, converse
        subskills = ['hypotenuse', 'shorter_leg', 'converse']
        subskill = rng.choice(subskills)
        
        if subskill == 'hypotenuse':
            leg1 = rng.randint(3, 12)
            leg2 = rng.randint(4, 16)
            hyp2 = leg1**2 + leg2**2
            hyp = sp.sqrt(hyp2)
            
            question = f"In a right-angled triangle, the lengths of the two shorter sides are {leg1} cm and {leg2} cm. Calculate the length of the hypotenuse."
            
            if hyp.is_Integer:
                ans_str = str(hyp)
            else:
                ans_float = float(hyp)
                ans_str = f"{ans_float:.2f}".replace('.', '{,}')
                
            steps = [
                f"c^2 = a^2 + b^2",
                f"c^2 = {leg1}^2 + {leg2}^2",
                f"c^2 = {leg1**2} + {leg2**2}",
                f"c^2 = {hyp2}",
                f"c = \\sqrt{{{hyp2}}}",
                f"c \\approx {ans_str} \\text{{ cm}}"
            ]
            
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": [
                    "Recall the Theorem of Pythagoras: in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
                    "Substitute the given lengths into the formula: $c^2 = a^2 + b^2$.",
                    "Don't forget to take the square root at the end to find the length."
                ]
            }
            
        elif subskill == 'shorter_leg':
            hyp = rng.randint(5, 20)
            leg1 = rng.randint(3, hyp - 1)
            leg2_sq = hyp**2 - leg1**2
            leg2 = sp.sqrt(leg2_sq)
            
            question = f"The hypotenuse of a right-angled triangle is {hyp} cm and one of the other sides is {leg1} cm. Calculate the length of the unknown side."
            
            if leg2.is_Integer:
                ans_str = str(leg2)
            else:
                ans_float = float(leg2)
                ans_str = f"{ans_float:.2f}".replace('.', '{,}')
                
            steps = [
                f"c^2 = a^2 + b^2",
                f"{hyp}^2 = {leg1}^2 + b^2",
                f"{hyp**2} = {leg1**2} + b^2",
                f"b^2 = {hyp**2} - {leg1**2}",
                f"b^2 = {leg2_sq}",
                f"b = \\sqrt{{{leg2_sq}}}",
                f"b \\approx {ans_str} \\text{{ cm}}"
            ]
            
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": [
                    "Write down the Theorem of Pythagoras: $c^2 = a^2 + b^2$.",
                    "Substitute the hypotenuse and the known side.",
                    "Rearrange the formula to solve for the unknown shorter side."
                ]
            }
            
        else: # converse
            # generate triplet that may or may not be right angled
            is_right = rng.choice([True, False])
            if is_right:
                m = rng.randint(2, 5)
                n = rng.randint(1, m-1)
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                sides = sorted([a, b, c])
            else:
                a = rng.randint(3, 10)
                b = rng.randint(4, 12)
                c = rng.randint(max(a, b) + 1, a + b - 1)
                sides = sorted([a, b, c])
                if sides[0]**2 + sides[1]**2 == sides[2]**2:
                    # inadvertently got a right angle, change it slightly
                    sides[2] += 1
            
            question = f"A triangle has side lengths {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. Determine whether this triangle is a right-angled triangle."
            
            lhs = sides[0]**2 + sides[1]**2
            rhs = sides[2]**2
            
            steps = [
                f"Identify the longest side as the possible hypotenuse: c = {sides[2]}",
                f"Calculate c^2 = {sides[2]}^2 = {rhs}",
                f"Calculate a^2 + b^2 = {sides[0]}^2 + {sides[1]}^2 = {sides[0]**2} + {sides[1]**2} = {lhs}"
            ]
            
            if lhs == rhs:
                ans_str = "Yes"
                steps.append(f"Since {lhs} = {rhs}, the triangle is right-angled (Converse of Pythagoras).")
            else:
                ans_str = "No"
                steps.append(f"Since {lhs} \\neq {rhs}, the triangle is not right-angled.")
                
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": [
                    "To check if a triangle is right-angled, use the Converse of the Theorem of Pythagoras.",
                    "Square the longest side and compare it to the sum of the squares of the other two sides.",
                    "If they are equal, the triangle is right-angled."
                ]
            }
