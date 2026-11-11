import random
import sympy as sp
from typing import Dict, Any, List

SUBSKILLS = ['hypotenuse', 'shorter_leg', 'converse', 'pythagorean_triples']

class SeniorPhasePythagorasGenerator:
    """Generator for Grade 8 and 9 Theorem of Pythagoras."""
    SUBSKILLS = SUBSKILLS
    
    def _generate_one(self, rng: random.Random, subskill: str, grade: int = 8) -> Dict[str, Any]:
        if subskill == 'hypotenuse':
            triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (7, 24, 25)]
            leg1, leg2, hyp = rng.choice(triples)
            scale = rng.choice([1, 2])
            leg1 *= scale
            leg2 *= scale
            hyp *= scale
            hyp2 = leg1**2 + leg2**2
            ans_str = f"{hyp} cm"
            question = f"In a right-angled triangle, the two shorter sides have lengths {leg1} cm and {leg2} cm. Calculate the length of the hypotenuse."
            steps = [
                f"c^2 = a^2 + b^2 \\quad \\text{{(Pythagoras)}}",
                f"c^2 = {leg1}^2 + {leg2}^2 = {leg1**2} + {leg2**2} = {hyp2}",
                f"c = \\sqrt{{{hyp2}}} = {hyp} \\text{{ cm}}"
            ]
            memo = f"1. Formula and substitution: $c^2 = {leg1}^2 + {leg2}^2 = {hyp2}$ (Pythagoras) [1]\n2. Calculated hypotenuse: ${hyp} \\text{{ cm}}$ [1]"
            hints = {
                "tier_1": "Recall the Theorem of Pythagoras: c^2 = a^2 + b^2.",
                "tier_2": f"Square {leg1} and {leg2}, add them to get {hyp2}, then take the square root.",
                "tier_3": f"Hypotenuse = {hyp} cm."
            }
        elif subskill == 'shorter_leg':
            triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
            leg1, leg2, hyp = rng.choice(triples)
            scale = rng.choice([1, 2])
            leg1 *= scale
            leg2 *= scale
            hyp *= scale
            leg2_sq = hyp**2 - leg1**2
            ans_str = f"{leg2} cm"
            question = f"The hypotenuse of a right-angled triangle is {hyp} cm and one of the other sides is {leg1} cm. Calculate the length of the unknown side."
            steps = [
                f"b^2 = c^2 - a^2 \\quad \\text{{(Pythagoras)}}",
                f"b^2 = {hyp}^2 - {leg1}^2 = {hyp**2} - {leg1**2} = {leg2_sq}",
                f"b = \\sqrt{{{leg2_sq}}} = {leg2} \\text{{ cm}}"
            ]
            memo = f"1. Subtraction: $b^2 = {hyp}^2 - {leg1}^2 = {leg2_sq}$ (Pythagoras) [1]\n2. Calculated side length: ${leg2} \\text{{ cm}}$ [1]"
            hints = {
                "tier_1": "Rearrange Pythagoras to find a shorter leg: b^2 = c^2 - a^2.",
                "tier_2": f"Subtract: {hyp**2} - {leg1**2} = {leg2_sq}, then take the square root.",
                "tier_3": f"Unknown side = {leg2} cm."
            }
        elif subskill == 'converse':
            is_right = rng.choice([True, False])
            if is_right:
                a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)])
                verdict = "Yes, it is a right-angled triangle"
            else:
                a, b = rng.choice([(3, 4), (5, 10), (6, 9), (7, 12)])
                c = int(sp.sqrt(a**2 + b**2)) + rng.choice([-1, 1, 2])
                verdict = "No, it is not a right-angled triangle"
            ans_str = verdict
            question = f"A triangle has side lengths {a} cm, {b} cm, and {c} cm. Using the converse of Pythagoras, determine whether the triangle is right-angled. (State 'Yes' or 'No' with calculation)."
            lhs = a**2 + b**2
            rhs = c**2
            eq_sym = "=" if lhs == rhs else "\\neq"
            steps = [
                f"a^2 + b^2 = {a}^2 + {b}^2 = {lhs}",
                f"c^2 = {c}^2 = {rhs}",
                f"\\text{{Since }} {lhs} {eq_sym} {rhs}, {verdict}."
            ]
            memo = f"1. Calculations: ${a}^2 + {b}^2 = {lhs}$ and $c^2 = {rhs}$ [1]\n2. Conclusion: {verdict} [1]"
            hints = {
                "tier_1": "Test if the sum of squares of the two shorter sides equals the square of the longest side.",
                "tier_2": f"Calculate {a}^2 + {b}^2 = {lhs} and {c}^2 = {rhs}.",
                "tier_3": f"{verdict} (since {lhs} {eq_sym} {rhs})."
            }
        else: # pythagorean_triples
            subskill = 'pythagorean_triples'
            triples = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17)]
            t = rng.choice(triples)
            ans_str = f"({t[0]}; {t[1]}; {t[2]})"
            question = f"Verify whether the numbers {t[0]}, {t[1]}, and {t[2]} form a Pythagorean triple."
            steps = [
                f"{t[0]}^2 + {t[1]}^2 = {t[0]**2} + {t[1]**2} = {t[0]**2 + t[1]**2}",
                f"{t[2]}^2 = {t[2]**2}",
                f"\\text{{Since }} {t[0]**2 + t[1]**2} = {t[2]**2}, \\text{{ they form a valid Pythagorean triple.}}"
            ]
            memo = f"1. Verification: ${t[0]}^2 + {t[1]}^2 = {t[2]**2}$ [1]\n2. Conclusion: Valid Pythagorean triple [1]"
            hints = {
                "tier_1": "A Pythagorean triple satisfies a^2 + b^2 = c^2 for integers.",
                "tier_2": f"Check {t[0]}^2 + {t[1]}^2 = {t[2]}^2.",
                "tier_3": "Yes, they form a Pythagorean triple."
            }

        qid = f"g{grade}_pyth_{rng.randint(100000, 999999)}"
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
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": subskill,
            "hints": hints,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp1", "desc": "Application of Pythagoras formula", "marks": 1, "editable": True},
                    {"id": "mp2", "desc": f"Accurate calculation: {ans_str}", "marks": 1, "editable": True},
                ]
            },
            "misconception_tags": [
                "add_lengths_before_squaring",
                "subtracts_when_finding_hypotenuse",
            ],
            "difficulty": "medium",
            "stage_metadata": {"grade": grade, "subskill": subskill}
        }

    def generate(self, grade: int = 8, mode: str = "pythagoras", seed: int = None, count: int = 1, subskill: str = None, **kwargs) -> List[Dict[str, Any]]:
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
