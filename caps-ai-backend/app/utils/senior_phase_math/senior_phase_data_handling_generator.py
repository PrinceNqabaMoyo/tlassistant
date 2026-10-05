import random
import sympy as sp
from typing import Dict, Any, List
import statistics

class SeniorPhaseDataHandlingGenerator:
    """Generator for Grade 7, 8, and 9 Statistics (mean, median, mode, range)."""
    
    def generate(self, grade: int = 7, mode: str = "data_handling", seed: int = None) -> Dict[str, Any]:
        rng = random.Random(seed)
        
        # Subskills: mean, median, mode, range
        subskills = ['mean', 'median', 'mode', 'range']
        subskill = rng.choice(subskills)
        
        n = rng.randint(5, 10)
        data = [rng.randint(1, 20) for _ in range(n)]
        
        data_str = ", ".join(map(str, data))
        sorted_data = sorted(data)
        
        if subskill == 'mean':
            mean_val = sum(data) / n
            question = f"Calculate the mean of the following data set: {data_str}"
            ans_str = f"{mean_val:.2f}".rstrip('0').rstrip('.').replace('.', '{,}')
            steps = [
                f"\\text{{Sum of data}} = " + " + ".join(map(str, data)) + f" = {sum(data)}",
                f"\\text{{Number of values}} (n) = {n}",
                f"\\text{{Mean}} = \\frac{{{sum(data)}}}{{{n}}} = {ans_str}"
            ]
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["To find the mean, add all the values together and divide by the number of values."]
            }
            
        elif subskill == 'median':
            median_val = statistics.median(data)
            question = f"Calculate the median of the following data set: {data_str}"
            ans_str = f"{float(median_val):.1f}".rstrip('0').rstrip('.').replace('.', '{,}')
            steps = [
                f"\\text{{1. Order the data from smallest to largest: }} " + ", ".join(map(str, sorted_data)),
                f"\\text{{2. Find the middle value. Since n = }} {n},"
            ]
            if n % 2 == 1:
                steps.append(f"\\text{{The middle value is }} {ans_str}.")
            else:
                mid1 = sorted_data[n//2 - 1]
                mid2 = sorted_data[n//2]
                steps.append(f"\\text{{The median is the average of the two middle values: }} \\frac{{{mid1} + {mid2}}}{{2}} = {ans_str}.")
                
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["To find the median, first order the data from smallest to largest. Then find the middle value."]
            }
            
        elif subskill == 'mode':
            # ensure there is a clear mode
            data.append(rng.choice(data))
            n += 1
            data_str = ", ".join(map(str, data))
            
            freq = {}
            for x in data:
                freq[x] = freq.get(x, 0) + 1
            max_freq = max(freq.values())
            modes = [k for k, v in freq.items() if v == max_freq]
            modes.sort()
            
            question = f"Determine the mode of the following data set: {data_str}"
            ans_str = ", ".join(map(str, modes))
            
            steps = [
                f"\\text{{The mode is the value(s) that appear most frequently.}}",
                f"\\text{{Frequencies: }} " + ", ".join([f"{k}: {v}" for k, v in sorted(freq.items())]),
                f"\\text{{The highest frequency is }} {max_freq}.",
                f"\\text{{Mode(s) = }} {ans_str}"
            ]
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["The mode is the value that appears most often in a data set."]
            }
            
        else: # range
            range_val = max(data) - min(data)
            question = f"Calculate the range of the following data set: {data_str}"
            ans_str = str(range_val)
            steps = [
                f"\\text{{Range}} = \\text{{Maximum value}} - \\text{{Minimum value}}",
                f"\\text{{Range}} = {max(data)} - {min(data)}",
                f"\\text{{Range}} = {ans_str}"
            ]
            return {
                "question": question,
                "solution_steps": steps,
                "final_answer": ans_str,
                "hints": ["The range is the difference between the largest and smallest values in the data set."]
            }
