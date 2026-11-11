import random
import statistics
from typing import Dict, Any, List

SUBSKILLS = ['mean', 'median', 'mode', 'range', 'extremes_and_outliers']

class SeniorPhaseDataHandlingGenerator:
    """Generator for Grade 7, 8, and 9 Statistics (mean, median, mode, range, extremes)."""
    SUBSKILLS = SUBSKILLS
    
    def _generate_one(self, rng: random.Random, subskill: str, grade: int = 7) -> Dict[str, Any]:
        n = rng.randint(5, 9)
        data = [rng.randint(1, 20) for _ in range(n)]
        data_str = ", ".join(map(str, data))
        sorted_data = sorted(data)
        
        if subskill == 'mean':
            total = sum(data)
            mean_val = total / n
            ans_str = f"{mean_val:.2f}".rstrip('0').rstrip('.').replace('.', '{,}')
            question = f"Calculate the mean of the following data set: $${data_str}$$"
            steps = [
                f"\\text{{Sum of data}} = " + " + ".join(map(str, data)) + f" = {total}",
                f"\\text{{Number of values}} (n) = {n}",
                f"\\text{{Mean}} = \\frac{{{total}}}{{{n}}} = {ans_str}"
            ]
            memo = f"1. Sum values: $\\sum x = {total}$ [1]\n2. Mean: $\\frac{{{total}}}{{{n}}} = {ans_str}$ [1]"
            hints = {
                "tier_1": "To find the mean, add all the values together and divide by the number of values.",
                "tier_2": f"Add the numbers to get {total}, then divide by {n}.",
                "tier_3": f"Mean = {ans_str}."
            }
        elif subskill == 'median':
            median_val = statistics.median(data)
            ans_str = f"{float(median_val):.1f}".rstrip('0').rstrip('.').replace('.', '{,}')
            question = f"Calculate the median of the following data set: $${data_str}$$"
            steps = [
                f"\\text{{1. Order the data from smallest to largest: }} " + ", ".join(map(str, sorted_data)),
                f"\\text{{2. Find the middle value (n = {n}):}}"
            ]
            if n % 2 == 1:
                steps.append(f"\\text{{The middle value is }} {ans_str}.")
            else:
                mid1 = sorted_data[n//2 - 1]
                mid2 = sorted_data[n//2]
                steps.append(f"\\text{{Average middle values: }} \\frac{{{mid1} + {mid2}}}{{2}} = {ans_str}.")
            memo = f"1. Ordered list: {', '.join(map(str, sorted_data))} [1]\n2. Median value: ${ans_str}$ [1]"
            hints = {
                "tier_1": "First order the data from smallest to largest, then find the middle value.",
                "tier_2": f"Ordered: {', '.join(map(str, sorted_data))}.",
                "tier_3": f"Median = {ans_str}."
            }
        elif subskill == 'mode':
            data.append(rng.choice(data))
            data_str = ", ".join(map(str, data))
            freq = {}
            for x in data:
                freq[x] = freq.get(x, 0) + 1
            max_freq = max(freq.values())
            modes = [k for k, v in freq.items() if v == max_freq]
            modes.sort()
            ans_str = ", ".join(map(str, modes))
            question = f"Determine the mode of the following data set: $${data_str}$$"
            steps = [
                f"\\text{{Frequencies: }} " + ", ".join([f"{k}: {v}" for k, v in sorted(freq.items())]),
                f"\\text{{Highest frequency is }} {max_freq}.",
                f"\\text{{Mode(s) = }} {ans_str}"
            ]
            memo = f"1. Frequency inspection: value(s) with highest count ({max_freq}) [1]\n2. Mode(s): ${ans_str}$ [1]"
            hints = {
                "tier_1": "The mode is the value that appears most often.",
                "tier_2": f"Find which number appears {max_freq} times.",
                "tier_3": f"Mode = {ans_str}."
            }
        elif subskill == 'range':
            min_v = min(data)
            max_v = max(data)
            range_val = max_v - min_v
            ans_str = str(range_val)
            question = f"Calculate the range of the following data set: $${data_str}$$"
            steps = [
                f"\\text{{Maximum value}} = {max_v}",
                f"\\text{{Minimum value}} = {min_v}",
                f"\\text{{Range}} = {max_v} - {min_v} = {ans_str}"
            ]
            memo = f"1. Identify max ({max_v}) and min ({min_v}): ${max_v} - {min_v}$ [1]\n2. Calculated range: ${ans_str}$ [1]"
            hints = {
                "tier_1": "Range is the difference between the maximum and minimum values.",
                "tier_2": f"Subtract {min_v} from {max_v}.",
                "tier_3": f"Range = {ans_str}."
            }
        else: # extremes_and_outliers
            subskill = 'extremes_and_outliers'
            min_v = min(data)
            max_v = max(data)
            ans_str = f"Min: {min_v}, Max: {max_v}"
            question = f"Identify the minimum (lowest) and maximum (highest) values in this data set: $${data_str}$$"
            steps = [
                f"\\text{{Ordered data: }} " + ", ".join(map(str, sorted_data)),
                f"\\text{{Lowest value (Min)}} = {min_v}",
                f"\\text{{Highest value (Max)}} = {max_v}"
            ]
            memo = f"1. Minimum: ${min_v}$ [1]\n2. Maximum: ${max_v}$ [1]"
            hints = {
                "tier_1": "Find the smallest and largest values in the list.",
                "tier_2": f"Look at the sorted list: {sorted_data[0]} to {sorted_data[-1]}.",
                "tier_3": f"Min = {min_v}, Max = {max_v}."
            }

        qid = f"g{grade}_stat_{rng.randint(100000, 999999)}"
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
            "term": 4,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "subskill": subskill,
            "hints": hints,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp1", "desc": "Method / formula application", "marks": 1, "editable": True},
                    {"id": "mp2", "desc": f"Accurate final answer: {ans_str}", "marks": 1, "editable": True},
                ]
            },
            "misconception_tags": [
                "confuses_mean_and_median",
                "median_without_ordering_data",
            ],
            "difficulty": "medium",
            "stage_metadata": {"grade": grade, "subskill": subskill}
        }

    def generate(self, grade: int = 7, mode: str = "data_handling", seed: int = None, count: int = 1, subskill: str = None, **kwargs) -> List[Dict[str, Any]]:
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
