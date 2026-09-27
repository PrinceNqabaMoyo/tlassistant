"""
SAMO Olympiad Round 1 Problem Generator (Layer F)
-------------------------------------------------
100% Deterministic, SymPy-backed, zero-LLM problem generator for
South African Mathematics Olympiad (SAMO) Junior & Senior Round 1.

Categories:
1. Number Theory (divisibility, prime factorisation, modular arithmetic, trailing zeros)
2. Combinatorics & Counting (pigeonhole principle, permutations, grid paths)
3. Geometry & Invariants (angle chasing, cyclic chords, area ratios, parity)
4. Algebraic Telescoping & Inequalities (telescoping series, AM-GM bounding, symmetric equations)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
import sympy as sp


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


# -------------------------------------------------------------
# 1. Number Theory Generators
# -------------------------------------------------------------
def _gen_number_theory(r: random.Random, division: str = "junior") -> Dict[str, Any]:
    archetype = r.choice(["trailing_zeros", "modular_remainder", "divisibility_digit"])
    
    if archetype == "trailing_zeros":
        # Count trailing zeros of n! by Legendre's formula
        n = r.choice([25, 50, 75, 100, 125])
        # zeros = sum(n // 5^k)
        zeros = 0
        p = 5
        while p <= n:
            zeros += n // p
            p *= 5
            
        opts = [zeros - 2, zeros - 1, zeros, zeros + 1, zeros + 2]
        r.shuffle(opts)
        correct_idx = opts.index(zeros)
        
        return {
            "id": f"samo_nt_zeros_{n}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "number_theory",
            "technique_tags": ["legendre_formula", "prime_factorisation_of_factorials"],
            "prompt": f"How many trailing zeros are there at the end of the decimal representation of ${n}!$?",
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": zeros,
            "hint": "A trailing zero is produced by a factor of $10 = 2 \\times 5$. Count how many times 5 divides into the product.",
            "solution_steps": [
                f"Trailing zeros equal the power of 5 in the prime factorisation of ${n}!$.",
                f"Using Legendre's formula: $\\lfloor {n}/5 \\rfloor + \\lfloor {n}/25 \\rfloor + \\dots = {zeros}$.",
                f"Therefore, there are {zeros} trailing zeros.",
            ]
        }
    
    elif archetype == "modular_remainder":
        # Remainder of a^b mod m using Euler's totient or small cycles
        base = r.choice([2, 3, 7])
        exp = r.choice([2024, 2025, 2026, 2027])
        mod = r.choice([5, 10, 13])
        ans = pow(base, exp, mod)
        
        opts = list(set([ans, (ans + 1) % mod, (ans + 2) % mod, (ans + 3) % mod, (ans + 4) % mod]))
        while len(opts) < 5:
            opts.append((max(opts) + 1) % 15)
        r.shuffle(opts)
        correct_idx = opts.index(ans)
        
        return {
            "id": f"samo_nt_mod_{base}_{exp}_{mod}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "number_theory",
            "technique_tags": ["modular_arithmetic", "cycles_of_powers"],
            "prompt": f"What is the remainder when ${base}^{{{exp}}}$ is divided by ${mod}$?",
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": ans,
            "hint": f"Look for a repeating cycle of remainders when raising ${base}$ to consecutive integer powers modulo ${mod}$.",
            "solution_steps": [
                f"Compute consecutive powers modulo {mod} to find the cycle period.",
                f"The exponent {exp} reduces according to the period.",
                f"Evaluating the reduced exponent gives remainder {ans}.",
            ]
        }
    
    else: # divisibility_digit
        k = r.choice([2, 3, 4, 5])
        ans_d = r.choice([1, 2, 4, 7, 8])
        # A 6-digit number 573_82 is divisible by 9
        # Sum of digits + d = multiple of 9
        target_sum = 9 * k
        given_sum = target_sum - ans_d
        d1, d2, d3, d4 = 5, 7, (given_sum - 14) // 2, (given_sum - 14) - (given_sum - 14) // 2
        
        opts = [ans_d, (ans_d + 1) % 10, (ans_d + 2) % 10, (ans_d + 3) % 10, (ans_d + 4) % 10]
        r.shuffle(opts)
        correct_idx = opts.index(ans_d)
        
        return {
            "id": f"samo_nt_div_{ans_d}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "number_theory",
            "technique_tags": ["divisibility_rules", "digital_root"],
            "prompt": f"If the number $57{d3}d{d4}2$ is divisible by $9$, what is the single digit $d$?",
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": ans_d,
            "hint": "A positive integer is divisible by 9 if and only if the sum of its digits is a multiple of 9.",
            "solution_steps": [
                f"Sum of known digits: $5 + 7 + {d3} + {d4} + 2 = {given_sum}$.",
                f"The total sum ${given_sum} + d$ must be a multiple of $9$.",
                f"The unique decimal digit $d \\in \\{{0,1,\\dots,9\\}}$ satisfying this is $d = {ans_d}$.",
            ]
        }


# -------------------------------------------------------------
# 2. Combinatorics & Counting
# -------------------------------------------------------------
def _gen_combinatorics(r: random.Random, division: str = "junior") -> Dict[str, Any]:
    archetype = r.choice(["pigeonhole_socks", "grid_paths", "handshakes"])
    
    if archetype == "pigeonhole_socks":
        red = r.choice([10, 12, 15])
        blue = r.choice([8, 10, 14])
        green = r.choice([6, 9, 11])
        # Min socks to guarantee a matching pair = 3 + 1 = 4 socks
        pair_ans = 4
        # Min socks to guarantee at least one of each color = max(red+blue, red+green, blue+green) + 1
        two_colors_max = sum(sorted([red, blue, green])[1:]) + 1
        
        opts = [two_colors_max - 2, two_colors_max - 1, two_colors_max, two_colors_max + 1, two_colors_max + 2]
        r.shuffle(opts)
        correct_idx = opts.index(two_colors_max)
        
        return {
            "id": f"samo_comb_pigeon_{red}_{blue}_{green}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "combinatorics",
            "technique_tags": ["pigeonhole_principle", "worst_case_analysis"],
            "prompt": (
                f"A drawer contains ${red}$ red socks, ${blue}$ blue socks, and ${green}$ green socks. "
                f"What is the minimum number of socks that must be drawn in the dark to guarantee "
                f"drawing at least one sock of each color?"
            ),
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": two_colors_max,
            "hint": "Consider the worst-case scenario where you draw all socks of the two largest color groups before drawing a single sock of the remaining color.",
            "solution_steps": [
                f"Identify the two largest color groups: {sorted([red, blue, green])[2]} and {sorted([red, blue, green])[1]}.",
                f"In the worst case, you could draw all {sorted([red, blue, green])[2]} + {sorted([red, blue, green])[1]} = {two_colors_max - 1} socks without touching the third color.",
                f"The very next sock (the ${two_colors_max}^{{\\text{{th}}}}$ sock) must be of the third color.",
                f"Therefore, the minimum required is {two_colors_max}.",
            ]
        }
    
    elif archetype == "grid_paths":
        w = r.choice([3, 4, 5])
        h = r.choice([2, 3, 4])
        # Paths = (w+h)! / (w! h!)
        paths = sp.binomial(w + h, w)
        ans = int(paths)
        
        opts = [ans - 4, ans - 1, ans, ans + 2, ans + 6]
        r.shuffle(opts)
        correct_idx = opts.index(ans)
        
        return {
            "id": f"samo_comb_grid_{w}_{h}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "combinatorics",
            "technique_tags": ["grid_paths", "combinations_binomial"],
            "prompt": (
                f"A robot moves on a grid from $(0,0)$ to $({w},{h})$ taking steps only one unit East or one unit North. "
                f"How many distinct paths can the robot take?"
            ),
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": ans,
            "hint": "Any path requires exactly $w$ East steps and $h$ North steps in some sequence. Choose which steps are East.",
            "solution_steps": [
                f"Total number of steps required: ${w} + {h} = {w+h}$.",
                f"The number of ways to choose the positions of the {w} East steps among the {w+h} total steps is $\\binom{{{w+h}}}{{{w}}}$.",
                f"Evaluating: $\\binom{{{w+h}}}{{{w}}} = {ans}$ paths.",
            ]
        }
    
    else: # handshakes
        n = r.choice([8, 10, 12, 15, 20])
        ans = n * (n - 1) // 2
        opts = [ans - 5, ans - 2, ans, ans + 3, ans + 7]
        r.shuffle(opts)
        correct_idx = opts.index(ans)
        
        return {
            "id": f"samo_comb_handshake_{n}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "combinatorics",
            "technique_tags": ["handshake_lemma", "combinations"],
            "prompt": f"At a mathematics convention, ${n}$ mathematicians all shake hands exactly once with every other attendee. How many total handshakes take place?",
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": ans,
            "hint": "Each pair of people shares exactly 1 handshake. How many unique pairs can be formed from $n$ individuals?",
            "solution_steps": [
                f"Each of the {n} people shakes hands with {n-1} others: ${n} \\times {n-1} = {n*(n-1)}$.",
                f"Since each handshake involves 2 people, we divide by 2 to avoid double counting.",
                f"Total handshakes: $\\frac{{{n} \\times {n-1}}}{{2}} = {ans}$.",
            ]
        }


# -------------------------------------------------------------
# 3. Geometry & Invariants
# -------------------------------------------------------------
def _gen_geometry(r: random.Random, division: str = "junior") -> Dict[str, Any]:
    archetype = r.choice(["angle_chase", "area_ratio", "circle_chords"])
    
    if archetype == "angle_chase":
        # Star polygon or intersecting secants
        points = r.choice([5, 7])
        if points == 5:
            ans = 180
            prompt = "In a standard 5-pointed star $ABCDE$, what is the sum of the five acute vertex angles $\\angle A + \\angle B + \\angle C + \\angle D + \\angle E$?"
            hint = "Use the exterior angle theorem on two inner triangles to transfer all five vertex angles into a single triangle."
        else:
            ans = 540
            prompt = "In a regular 7-pointed star, what is the sum of all inner angles at the seven vertices?"
            hint = "Partition the star into non-overlapping polygons and use angle sum formulas."
            
        opts = [ans - 90, ans - 45, ans, ans + 45, ans + 90]
        r.shuffle(opts)
        correct_idx = opts.index(ans)
        
        return {
            "id": f"samo_geom_star_{points}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "geometry",
            "technique_tags": ["exterior_angle_theorem", "angle_chasing"],
            "prompt": prompt,
            "options": [f"({chr(65+i)}) {val}^\\circ" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": ans,
            "hint": hint,
            "solution_steps": [
                f"Applying the exterior angle theorem to the interior intersecting triangles gathers the vertex angles into a triangle.",
                f"The interior angle sum of a triangle is $180^\\circ$.",
                f"The total sum of the vertex angles is ${ans}^\\circ$.",
            ]
        }
    
    else: # area_ratio
        # Triangle with median / cevian ratio
        k = r.choice([2, 3, 4])
        total_area = k * r.choice([12, 18, 24, 30])
        shaded_area = total_area // (k + 1)
        
        opts = [shaded_area - 2, shaded_area - 1, shaded_area, shaded_area + 2, shaded_area + 4]
        r.shuffle(opts)
        correct_idx = opts.index(shaded_area)
        
        return {
            "id": f"samo_geom_area_{k}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "geometry",
            "technique_tags": ["area_ratio_triangles", "cevian_theorem"],
            "prompt": (
                f"In $\\triangle ABC$, point $D$ lies on $BC$ such that $BD : DC = 1 : {k}$. "
                f"If the total area of $\\triangle ABC$ is ${total_area}\\text{{ cm}}^2$, find the area of $\\triangle ABD$."
            ),
            "options": [f"({chr(65+i)}) {val}\\text{{ cm}}^2" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": shaded_area,
            "hint": "Triangles $\\triangle ABD$ and $\\triangle ABC$ share the same perpendicular height from vertex $A$. Their areas are proportional to their bases.",
            "solution_steps": [
                f"Base $BC = BD + DC = 1 + {k} = {k+1}$ parts.",
                f"Since both triangles share the same altitude from $A$: $\\frac{{\\text{{Area}}(\\triangle ABD)}}{{\\text{{Area}}(\\triangle ABC)}} = \\frac{{BD}}{{BC}} = \\frac{{1}}{{{k+1}}}$.",
                f"Area of $\\triangle ABD = \\frac{{1}}{{{k+1}}} \\times {total_area} = {shaded_area}\\text{{ cm}}^2$.",
            ]
        }


# -------------------------------------------------------------
# 4. Algebraic Telescoping & Inequalities
# -------------------------------------------------------------
def _gen_algebra(r: random.Random, division: str = "senior") -> Dict[str, Any]:
    archetype = r.choice(["telescoping_fractions", "am_gm_minimum"])
    
    if archetype == "telescoping_fractions":
        # 1/(1*2) + 1/(2*3) + ... + 1/(n*(n+1)) = n/(n+1)
        n = r.choice([2023, 2024, 2025, 2026])
        ans_num = n
        ans_den = n + 1
        
        opts = [
            f"{n-1}/{n}",
            f"{n}/{n+1}",
            f"{n+1}/{n+2}",
            f"1/{n}",
            f"{2*n}/{2*n+1}"
        ]
        r.shuffle(opts)
        correct_idx = opts.index(f"{n}/{n+1}")
        
        return {
            "id": f"samo_alg_telescoping_{n}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "algebra",
            "technique_tags": ["telescoping_series", "partial_fractions"],
            "prompt": (
                f"Evaluate the sum:\n"
                f"$$\\frac{{1}}{{1 \\times 2}} + \\frac{{1}}{{2 \\times 3}} + \\frac{{1}}{{3 \\times 4}} + \\dots + \\frac{{1}}{{{n} \\times {n+1}}}$$"
            ),
            "options": [f"({chr(65+i)}) \\frac{{{o.split('/')[0]}}}{{{o.split('/')[1]}}}" for i, o in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": f"{n}/{n+1}",
            "hint": "Use partial fractions: $\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}$ to cause intermediate terms to cancel out.",
            "solution_steps": [
                "Rewrite each term using partial fractions: $\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}$.",
                f"The sum expands as: $\\left(1 - \\frac{{1}}{{2}}\\right) + \\left(\\frac{{1}}{{2}} - \\frac{{1}}{{3}}\\right) + \\dots + \\left(\\frac{{1}}{{{n}}} - \\frac{{1}}{{{n+1}}}\\right)$.",
                f"All intermediate terms cancel out, leaving: $1 - \\frac{{1}}{{{n+1}}} = \\frac{{{n}}}{{{n+1}}}$.",
            ]
        }
    
    else: # am_gm_minimum
        c = r.choice([4, 9, 16, 25])
        # Min of x + c/x for x > 0 is 2*sqrt(c)
        min_val = 2 * int(sp.sqrt(c))
        
        opts = [min_val - 2, min_val - 1, min_val, min_val + 2, min_val + 4]
        r.shuffle(opts)
        correct_idx = opts.index(min_val)
        
        return {
            "id": f"samo_alg_amgm_{c}",
            "competition": f"SAMO {division.capitalize()} Round 1",
            "category": "algebra",
            "technique_tags": ["am_gm_inequality", "extremal_problems"],
            "prompt": f"For all real numbers $x > 0$, what is the minimum value of the expression $x + \\frac{{{c}}}{{x}}$?",
            "options": [f"({chr(65+i)}) {val}" for i, val in enumerate(opts)],
            "correct_index": correct_idx,
            "correct_answer": min_val,
            "hint": "Apply the Arithmetic Mean - Geometric Mean (AM-GM) inequality: $\\frac{a + b}{2} \\ge \\sqrt{ab}$ for positive real numbers.",
            "solution_steps": [
                f"By the AM-GM inequality for positive reals $x$ and $\\frac{{{c}}}{{x}}$:",
                f"$$\\frac{{x + \\frac{{{c}}}{{x}}}}{{2}} \\ge \\sqrt{{x \\times \\frac{{{c}}}{{x}}}} = \\sqrt{{{c}}} = {int(sp.sqrt(c))}$$",
                f"Multiplying by 2 yields $x + \\frac{{{c}}}{{x}} \\ge {min_val}$.",
                f"Equality holds when $x = \\frac{{{c}}}{{x}} \\implies x^2 = {c} \\implies x = {int(sp.sqrt(c))}$.",
                f"The minimum value is {min_val}.",
            ]
        }


# -------------------------------------------------------------
# Main Public Generator API
# -------------------------------------------------------------
def generate_olympiad_problem(
    category: str = "random",
    division: str = "junior",
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """Emits a single deterministic SAMO Olympiad Round 1 problem."""
    r = _rng(seed)
    cat_norm = category.lower().strip()
    
    if cat_norm == "number_theory":
        return _gen_number_theory(r, division)
    elif cat_norm == "combinatorics":
        return _gen_combinatorics(r, division)
    elif cat_norm == "geometry":
        return _gen_geometry(r, division)
    elif cat_norm == "algebra":
        return _gen_algebra(r, division)
    else:
        chosen = r.choice([_gen_number_theory, _gen_combinatorics, _gen_geometry, _gen_algebra])
        return chosen(r, division)
