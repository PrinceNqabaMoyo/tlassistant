"""
Grade 8 Mathematics - Whole Numbers Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Whole numbers.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Properties of Operations (01 - 10)
# ==============================================================================

def arch_01_commutative_property_addition_verification(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(145, 980)
    b = rng.randint(120, 890)
    total = a + b

    prompt = (
        f"Consider the two whole numbers **{a}** and **{b}**.\n\n"
        f"1. Calculate the sum: $${a} + {b}$$.\n"
        f"2. Calculate the sum: $${b} + {a}$$.\n"
        f"3. Name the property of operations that states the order of addition does not change the result."
    )
    sol = (
        f"**Step 1:** Calculate ${a} + {b} = {total}$ [1 Mark].\n\n"
        f"**Step 2:** Calculate ${b} + {a} = {total}$ [1 Mark].\n\n"
        f"**Step 3:** The property is the **commutative property of addition** [1 Mark].\n\n"
        f"$$\\therefore {a} + {b} = {b} + {a} = {total} \\text{{ (Commutative Property)}}$$"
    )
    ans = f"1. {total}; 2. {total}; 3. Commutative property of addition"
    return {
        "id": f"g8_wn_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "01_commutative_property_addition_verification",
        "hints": {
            "tier_1": "Calculate both sums and check if they are identical.",
            "tier_2": "The property that allows switching the order is called the commutative property.",
            "tier_3": f"Both sums equal {total}. The property is the Commutative Property of Addition."
        },
        "misconception_tags": ["associative_commutative_confusion"]
    }


def arch_02_commutative_property_multiplication_verification(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(14, 48)
    b = rng.randint(12, 35)
    prod = a * b

    prompt = (
        f"1. Evaluate $${a} \\times {b}$$.\n"
        f"2. Evaluate $${b} \\times {a}$$.\n"
        f"3. State the property of operations demonstrated."
    )
    sol = (
        f"**Step 1:** ${a} \\times {b} = {prod}$ [1 Mark].\n\n"
        f"**Step 2:** ${b} \\times {a} = {prod}$ [1 Mark].\n\n"
        f"**Step 3:** This demonstrates the **commutative property of multiplication** [1 Mark].\n\n"
        f"$$\\therefore {a} \\times {b} = {b} \\times {a} = {prod}$$"
    )
    ans = f"1. {prod}; 2. {prod}; 3. Commutative property of multiplication"
    return {
        "id": f"g8_wn_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "02_commutative_property_multiplication_verification",
        "hints": {
            "tier_1": "Multiplication order can be swapped without changing the product.",
            "tier_2": f"Calculate {a} × {b}.",
            "tier_3": f"Both products equal {prod}. The property is Commutative Property of Multiplication."
        },
        "misconception_tags": ["multiplication_order_error"]
    }


def arch_03_associative_property_addition_grouping(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(25, 80)
    b = rng.randint(15, 60)
    c = rng.randint(12, 45)
    total = a + b + c

    prompt = (
        f"Verify the **associative property of addition** for the numbers $a = {a}$, $b = {b}$, and $c = {c}$:\n\n"
        f"1. Calculate $$({a} + {b}) + {c}$$.\n"
        f"2. Calculate $${a} + ({b} + {c})$$.\n"
        f"3. State whether grouping affects the final sum."
    )
    sol = (
        f"**Step 1:** $({a} + {b}) + {c} = {a + b} + {c} = {total}$ [1 Mark].\n\n"
        f"**Step 2:** ${a} + ({b} + {c}) = {a} + {b + c} = {total}$ [1 Mark].\n\n"
        f"**Step 3:** Grouping brackets do **not** affect the final sum in addition [1 Mark].\n\n"
        f"$$\\therefore ({a} + {b}) + {c} = {a} + ({b} + {c}) = {total}$$"
    )
    ans = f"1. {total}; 2. {total}; 3. Grouping does not affect the sum"
    return {
        "id": f"g8_wn_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "03_associative_property_addition_grouping",
        "hints": {
            "tier_1": "Evaluate inside the parentheses first for each calculation.",
            "tier_2": f"({a} + {b}) = {a + b}, then add {c}.",
            "tier_3": f"Both equal {total}."
        },
        "misconception_tags": ["associative_distributive_confusion"]
    }


def arch_04_associative_property_multiplication_grouping(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 9)
    b = rng.randint(3, 8)
    c = rng.randint(2, 6)
    prod = a * b * c

    prompt = (
        f"Verify the **associative property of multiplication** for $${a} \\times {b} \\times {c}$$:\n\n"
        f"1. Calculate $$({a} \\times {b}) \\times {c}$$.\n"
        f"2. Calculate $${a} \\times ({b} \\times {c})$$.\n"
        f"3. State how this property aids in mental mathematics."
    )
    p1 = a * b
    p2 = b * c
    sol = (
        f"**Step 1:** $({a} \\times {b}) \\times {c} = {p1} \\times {c} = {prod}$ [1 Mark].\n\n"
        f"**Step 2:** ${a} \\times ({b} \\times {c}) = {a} \\times {p2} = {prod}$ [1 Mark].\n\n"
        f"**Step 3:** It allows factors to be grouped into multiples of 10 or simpler pairs to calculate mentally [1 Mark].\n\n"
        f"$$\\therefore ({a} \\times {b}) \\times {c} = {a} \\times ({b} \\times {c}) = {prod}$$"
    )
    ans = f"1. {prod}; 2. {prod}; 3. Allows grouping factors into convenient pairs for easier calculation"
    return {
        "id": f"g8_wn_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "04_associative_property_multiplication_grouping",
        "hints": {
            "tier_1": "Calculate each bracket first.",
            "tier_2": f"({a} × {b}) = {p1}. Then {p1} × {c}.",
            "tier_3": f"Both bracket groupings yield {prod}."
        },
        "misconception_tags": ["grouping_bracket_multiplication_error"]
    }


def arch_05_distributive_property_multiplication_over_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(4, 9)
    b = rng.randint(20, 70)
    c = rng.randint(3, 9)
    ans = a * (b + c)

    prompt = (
        f"Apply the **distributive property of multiplication over addition** to evaluate:\n\n"
        f"$${a} \\times ({b} + {c})$$\n\n"
        f"1. Expand the expression using the distributive law.\n"
        f"2. Calculate the final value."
    )
    t1 = a * b
    t2 = a * c
    sol = (
        f"**Step 1:** Distribute ${a}$ to both terms inside the brackets:\n"
        f"$${a} \\times ({b} + {c}) = ({a} \\times {b}) + ({a} \\times {c})$$ [1 Mark]\n\n"
        f"**Step 2:** Multiply and add:\n"
        f"$$= {t1} + {t2} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {ans}$$"
    )
    ans_text = f"1. ({a} × {b}) + ({a} × {c}) = {t1} + {t2}; 2. {ans}"
    return {
        "id": f"g8_wn_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_text,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "05_distributive_property_multiplication_over_addition",
        "hints": {
            "tier_1": "Multiply the outside factor by each number inside the brackets.",
            "tier_2": f"{a} × {b} = {t1} and {a} × {c} = {t2}.",
            "tier_3": f"{t1} + {t2} = {ans}."
        },
        "misconception_tags": ["partial_distribution_error"]
    }


def arch_06_distributive_property_multiplication_over_subtraction(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(5, 9)
    b = rng.randint(30, 90)
    c = rng.randint(2, 8)
    ans = a * (b - c)

    prompt = (
        f"Use the distributive property to evaluate:\n\n"
        f"$${a} \\times ({b} - {c})$$\n\n"
        f"Show the expanded step and the final answer."
    )
    t1 = a * b
    t2 = a * c
    sol = (
        f"**Step 1:** Expand using the distributive property:\n"
        f"$${a} \\times ({b} - {c}) = ({a} \\times {b}) - ({a} \\times {c})$$ [1 Mark]\n\n"
        f"**Step 2:** Calculate:\n"
        f"$$= {t1} - {t2} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore {ans}$$"
    )
    ans_text = f"({t1}) - ({t2}) = {ans}"
    return {
        "id": f"g8_wn_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_text,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "06_distributive_property_multiplication_over_subtraction",
        "hints": {
            "tier_1": "Distribute multiplication over subtraction: a(b - c) = ab - ac.",
            "tier_2": f"{a} × {b} = {t1} and {a} × {c} = {t2}.",
            "tier_3": f"{t1} - {t2} = {ans}."
        },
        "misconception_tags": ["subtraction_sign_in_distribution_error"]
    }


def arch_07_additive_identity_and_zero_property(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(350, 4800)
    prompt = (
        f"For the whole number **{n}**:\n\n"
        f"1. What is the value of $${n} + 0$$?\n"
        f"2. What is the value of $${n} \\times 0$$?\n"
        f"3. Name the identity element for addition."
    )
    sol = (
        f"**Step 1:** ${n} + 0 = {n}$ [1 Mark].\n\n"
        f"**Step 2:** ${n} \\times 0 = 0$ [1 Mark].\n\n"
        f"**Step 3:** The identity element for addition is **0** (zero) [1 Mark].\n\n"
        f"$$\\therefore {n} + 0 = {n}, \\quad {n} \\times 0 = 0, \\quad \\text{{Identity element}} = 0$$"
    )
    ans = f"1. {n}; 2. 0; 3. 0"
    return {
        "id": f"g8_wn_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "07_additive_identity_and_zero_property",
        "hints": {
            "tier_1": "Adding zero leaves a number unchanged; multiplying by zero always yields zero.",
            "tier_2": "The number that leaves any number unchanged under addition is 0.",
            "tier_3": f"{n} + 0 = {n}, {n} × 0 = 0, Identity is 0."
        },
        "misconception_tags": ["multiplying_by_zero_equals_number_error"]
    }


def arch_08_multiplicative_identity_element(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(280, 5600)
    prompt = (
        f"1. What is the value of $${n} \\times 1$$?\n"
        f"2. What is the value of $${n} \\div 1$$?\n"
        f"3. Name the identity element for multiplication."
    )
    sol = (
        f"**Step 1:** ${n} \\times 1 = {n}$ [1 Mark].\n\n"
        f"**Step 2:** ${n} \\div 1 = {n}$ [1 Mark].\n\n"
        f"**Step 3:** The identity element for multiplication is **1** [1 Mark].\n\n"
        f"$$\\therefore {n} \\times 1 = {n}, \\quad {n} \\div 1 = {n}, \\quad \\text{{Identity}} = 1$$"
    )
    ans = f"1. {n}; 2. {n}; 3. 1"
    return {
        "id": f"g8_wn_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "08_multiplicative_identity_element",
        "hints": {
            "tier_1": "Multiplying or dividing by 1 preserves the number.",
            "tier_2": "The identity element for multiplication is 1.",
            "tier_3": f"Values are {n}, {n}, and 1."
        },
        "misconception_tags": ["multiplicative_identity_zero_confusion"]
    }


def arch_09_division_by_zero_undefined_concept(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(15, 95)
    prompt = (
        f"Evaluate and explain the difference between:\n\n"
        f"1. $$0 \\div {n}$$\n"
        f"2. $${n} \\div 0$$\n\n"
        f"State which expression is defined and which is undefined."
    )
    sol = (
        f"**Step 1:** $0 \\div {n} = 0$ because $0 \\times {n} = 0$. This expression is **defined** [1 Mark].\n\n"
        f"**Step 2:** ${n} \\div 0$ is **undefined** because there is no number $k$ such that $k \\times 0 = {n}$ [1 Mark].\n\n"
        f"$$\\therefore 0 \\div {n} = 0 \\text{{ (defined)}}, \\quad {n} \\div 0 \\text{{ is undefined}}$$"
    )
    ans = f"1. 0 (defined); 2. Undefined (division by zero is impossible)"
    return {
        "id": f"g8_wn_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "09_division_by_zero_undefined_concept",
        "hints": {
            "tier_1": "Zero divided by any non-zero number is zero.",
            "tier_2": "Division by zero is impossible and considered undefined in mathematics.",
            "tier_3": f"0 ÷ {n} = 0; {n} ÷ 0 is undefined."
        },
        "misconception_tags": ["division_by_zero_equals_zero_error"]
    }


def arch_10_mental_math_compensation_strategy(rng: random.Random) -> Dict[str, Any]:
    tens = rng.choice([50, 60, 70, 80, 90, 100])
    k = rng.choice([1, 2, 3])
    b = tens - k
    a = rng.randint(45, 95)
    total = a + b

    prompt = (
        f"Demonstrate the mental math **compensation strategy** to calculate:\n\n"
        f"$${a} + {b}$$\n\n"
        f"1. Show how adding {k} to {b} to make a friendly multiple of 10 ({tens}) and subtracting {k} from {a} simplifies the calculation.\n"
        f"2. State the final sum."
    )
    a_comp = a - k
    sol = (
        f"**Step 1:** Compensation strategy:\n"
        f"$${a} + {b} = ({a} - {k}) + ({b} + {k}) = {a_comp} + {tens}$$ [1 Mark]\n\n"
        f"**Step 2:** Calculate:\n"
        f"$${a_comp} + {tens} = {total}$$ [1 Mark]\n\n"
        f"$$\\therefore {total}$$"
    )
    ans = f"1. ({a} - {k}) + ({b} + {k}) = {a_comp} + {tens}; 2. {total}"
    return {
        "id": f"g8_wn_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "10_mental_math_compensation_strategy",
        "hints": {
            "tier_1": f"Add {k} to {b} to reach {tens}, and subtract {k} from {a}.",
            "tier_2": f"{a_comp} + {tens} is easier to calculate mentally.",
            "tier_3": f"Final sum is {total}."
        },
        "misconception_tags": ["compensation_one_sided_addition_error"]
    }


# ==============================================================================
# CLUSTER 2: Prime Numbers, Factors & Multiples (11 - 20)
# ==============================================================================

def arch_11_prime_vs_composite_classification(rng: random.Random) -> Dict[str, Any]:
    primes = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    composites = [25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 65, 77, 85, 91, 93, 95]
    p_choice = rng.choice(primes)
    c_choice = rng.choice(composites)

    prompt = (
        f"Classify the following two numbers as either **prime** or **composite** and justify with their factors:\n\n"
        f"1. Number **{p_choice}**\n"
        f"2. Number **{c_choice}**"
    )
    # Find factors of c_choice
    c_factors = [d for d in range(1, c_choice + 1) if c_choice % d == 0]
    c_fac_str = ", ".join(str(f) for f in c_factors)
    sol = (
        f"**Step 1:** **{p_choice}** has only two distinct factors: $1$ and ${p_choice}$. Therefore, it is a **prime number** [1 Mark].\n\n"
        f"**Step 2:** **{c_choice}** has more than two factors (Factors: ${c_fac_str}$). Therefore, it is a **composite number** [1 Mark].\n\n"
        f"$$\\therefore {p_choice} \\text{{ is prime; }} {c_choice} \\text{{ is composite}}$$"
    )
    ans = f"1. {p_choice}: Prime (only factors 1 and {p_choice}); 2. {c_choice}: Composite (factors: {c_fac_str})"
    return {
        "id": f"g8_wn_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "11_prime_vs_composite_classification",
        "hints": {
            "tier_1": "A prime number has exactly two factors: 1 and itself.",
            "tier_2": "A composite number has more than two factors.",
            "tier_3": f"{p_choice} is prime; {c_choice} is composite."
        },
        "misconception_tags": ["odd_number_assumed_prime_error"]
    }


def arch_12_prime_factorization_factor_tree(rng: random.Random) -> Dict[str, Any]:
    e2 = rng.randint(1, 3)
    e3 = rng.randint(1, 3)
    e5 = rng.randint(1, 2)
    val = (2 ** e2) * (3 ** e3) * (5 ** e5)

    prompt = (
        f"Express the whole number **{val}** as a product of its prime factors in exponential form."
    )
    exp_parts = []
    if e2 > 0: exp_parts.append(f"2^{{{e2}}}" if e2 > 1 else "2")
    if e3 > 0: exp_parts.append(f"3^{{{e3}}}" if e3 > 1 else "3")
    if e5 > 0: exp_parts.append(f"5^{{{e5}}}" if e5 > 1 else "5")
    exp_str = " \\times ".join(exp_parts)
    text_ans = " × ".join(exp_parts).replace("^{", "^").replace("}", "")

    sol = (
        f"**Step 1:** Decompose {val} by successive prime division:\n"
        f"- Factors of 2: count = {e2}\n"
        f"- Factors of 3: count = {e3}\n"
        f"- Factors of 5: count = {e5} [1 Mark: Method]\n\n"
        f"**Step 2:** Write in index (exponential) form:\n"
        f"$${val} = {exp_str}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {val} = {exp_str}$$"
    )
    return {
        "id": f"g8_wn_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": text_ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "12_prime_factorization_factor_tree",
        "hints": {
            "tier_1": "Divide by the smallest prime number (2, 3, 5) repeatedly.",
            "tier_2": "Count how many times each prime divides the number evenly.",
            "tier_3": f"{val} = {text_ans}."
        },
        "misconception_tags": ["composite_factors_in_prime_factorization"]
    }


def arch_13_prime_factorization_division_ladder(rng: random.Random) -> Dict[str, Any]:
    val = rng.choice([72, 108, 144, 180, 216, 252, 300, 360, 450])
    temp = val
    primes_count: Dict[int, int] = {}
    for p in [2, 3, 5, 7]:
        while temp % p == 0:
            primes_count[p] = primes_count.get(p, 0) + 1
            temp //= p
    if temp > 1:
        primes_count[temp] = 1

    exp_terms = [f"{p}^{{{c}}}" if c > 1 else f"{p}" for p, c in sorted(primes_count.items())]
    exp_str = " \\times ".join(exp_terms)
    text_ans = " × ".join(exp_terms).replace("^{", "^").replace("}", "")

    prompt = (
        f"Using the ladder method (continuous prime division), express **{val}** as a product of prime factors in index notation."
    )
    sol = (
        f"**Step 1:** Successively divide by prime factors:\n"
        f"Prime counts: {primes_count} [1 Mark: Method]\n\n"
        f"**Step 2:** Express in index notation:\n"
        f"$${val} = {exp_str}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {val} = {exp_str}$$"
    )
    return {
        "id": f"g8_wn_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": text_ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "13_prime_factorization_division_ladder",
        "hints": {
            "tier_1": "Set up a vertical ladder and divide by primes on the left.",
            "tier_2": "Collect all prime divisors and write in exponential notation.",
            "tier_3": f"{val} = {text_ans}."
        },
        "misconception_tags": ["ladder_division_stopping_prematurely"]
    }


def arch_14_highest_common_factor_two_numbers_ladder(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([6, 12, 18, 24])
    mult1 = rng.choice([2, 3, 5, 7])
    mult2 = rng.choice([4, 5, 7, 11])
    while math.gcd(mult1, mult2) != 1:
        mult2 = rng.choice([5, 7, 11])
    n1 = common * mult1
    n2 = common * mult2
    hcf = math.gcd(n1, n2)

    prompt = (
        f"Determine the **Highest Common Factor (HCF)** of **{n1}** and **{n2}** by using prime factorisation."
    )
    sol = (
        f"**Step 1:** Write the prime factorisations of both numbers [1 Mark: Method].\n\n"
        f"**Step 2:** Take the lowest power of each common prime factor:\n"
        f"$$\\text{{HCF}}({n1}, {n2}) = {hcf}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore \\text{{HCF}} = {hcf}$$"
    )
    return {
        "id": f"g8_wn_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(hcf),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "14_highest_common_factor_two_numbers_ladder",
        "hints": {
            "tier_1": "Find the prime factors of both numbers.",
            "tier_2": "Multiply together the lowest powers of the prime factors that appear in both.",
            "tier_3": f"HCF({n1}, {n2}) = {hcf}."
        },
        "misconception_tags": ["hcf_lcm_confusion"]
    }


def arch_15_lowest_common_multiple_two_numbers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([8, 12, 15, 18, 20])
    b = rng.choice([10, 14, 16, 24, 25])
    lcm = math.lcm(a, b)

    prompt = (
        f"Find the **Lowest Common Multiple (LCM)** of **{a}** and **{b}** using prime factors."
    )
    sol = (
        f"**Step 1:** Write down the prime factor decomposition of each number [1 Mark].\n\n"
        f"**Step 2:** The LCM is found by taking the highest power of every prime factor that appears in either number:\n"
        f"$$\\text{{LCM}}({a}, {b}) = {lcm}$$ [1 Mark]\n\n"
        f"$$\\therefore \\text{{LCM}} = {lcm}$$"
    )
    return {
        "id": f"g8_wn_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(lcm),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "15_lowest_common_multiple_two_numbers",
        "hints": {
            "tier_1": "Prime factorize both numbers.",
            "tier_2": "Select the highest power of each prime factor and multiply them together.",
            "tier_3": f"LCM({a}, {b}) = {lcm}."
        },
        "misconception_tags": ["lcm_lower_power_error"]
    }


def arch_16_hcf_and_lcm_three_numbers(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 6])
    n1 = base * 4
    n2 = base * 6
    n3 = base * 10
    hcf = math.gcd(n1, math.gcd(n2, n3))
    lcm = math.lcm(n1, math.lcm(n2, n3))

    prompt = (
        f"For the three whole numbers **{n1}**, **{n2}**, and **{n3}**:\n\n"
        f"1. Determine their Highest Common Factor (HCF).\n"
        f"2. Determine their Lowest Common Multiple (LCM)."
    )
    sol = (
        f"**Step 1:** Find prime factors of each number.\n"
        f"Common prime factors give $\\text{{HCF}} = {hcf}$ [1 Mark].\n\n"
        f"**Step 2:** Highest powers of all prime factors give $\\text{{LCM}} = {lcm}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{HCF}} = {hcf}, \\quad \\text{{LCM}} = {lcm}$$"
    )
    ans = f"1. HCF = {hcf}; 2. LCM = {lcm}"
    return {
        "id": f"g8_wn_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "16_hcf_and_lcm_three_numbers",
        "hints": {
            "tier_1": "HCF must divide all 3 numbers. LCM must be a multiple of all 3 numbers.",
            "tier_2": f"Find GCD and LCM of {n1}, {n2}, {n3}.",
            "tier_3": f"HCF = {hcf}, LCM = {lcm}."
        },
        "misconception_tags": ["three_numbers_hcf_miscalculation"]
    }


def arch_17_divisibility_rules_composite_application(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(120, 950)
    # create a number divisible by 6 (divisible by 2 and 3)
    val = k * 6
    digits = [int(c) for c in str(val)]
    d_sum = sum(digits)

    prompt = (
        f"Consider the whole number **{val}**.\n\n"
        f"1. State whether it is divisible by 2 and explain why.\n"
        f"2. Calculate the sum of its digits and state whether it is divisible by 3.\n"
        f"3. Conclude whether **{val}** is divisible by 6."
    )
    sol = (
        f"**Step 1:** The last digit is ${digits[-1]}$ (even), so {val} is **divisible by 2** [1 Mark].\n\n"
        f"**Step 2:** Sum of digits = ${' + '.join(str(d) for d in digits)} = {d_sum}$. "
        f"Since ${d_sum}$ is divisible by 3, {val} is **divisible by 3** [1 Mark].\n\n"
        f"**Step 3:** A number divisible by both 2 and 3 is **divisible by 6** [1 Mark].\n\n"
        f"$$\\therefore \\text{{Divisible by 6}}$$"
    )
    ans = f"1. Divisible by 2 (last digit {digits[-1]} is even); 2. Sum = {d_sum}, divisible by 3; 3. Yes, divisible by 6"
    return {
        "id": f"g8_wn_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "17_divisibility_rules_composite_application",
        "hints": {
            "tier_1": "Rule for 2: Last digit must be even. Rule for 3: Sum of digits must be a multiple of 3.",
            "tier_2": "A number divisible by both 2 and 3 is divisible by 6.",
            "tier_3": f"Sum of digits is {d_sum}. Yes, divisible by 6."
        },
        "misconception_tags": ["divisibility_rule_confusion"]
    }


def arch_18_word_problem_hcf_maximum_equal_packaging(rng: random.Random) -> Dict[str, Any]:
    common = rng.choice([12, 15, 18, 20])
    a_mult = rng.choice([3, 4, 5])
    b_mult = rng.choice([6, 7, 8])
    while math.gcd(a_mult, b_mult) != 1:
        b_mult += 1
    item_a = common * a_mult
    item_b = common * b_mult
    hcf = math.gcd(item_a, item_b)

    prompt = (
        f"A community feeding scheme receives a donation of **{item_a} apples** and **{item_b} oranges**. "
        f"They want to pack food hampers such that each hamper contains the exact same number of apples "
        f"and oranges, with no fruit leftover.\n\n"
        f"1. What is the greatest number of identical food hampers they can pack?\n"
        f"2. How many apples and oranges will be in each hamper?"
    )
    apples_each = item_a // hcf
    oranges_each = item_b // hcf
    sol = (
        f"**Step 1:** The greatest number of hampers is the $\\text{{HCF}}({item_a}, {item_b})$:\n"
        f"$$\\text{{HCF}}({item_a}, {item_b}) = {hcf} \\text{{ hampers}}$$ [1 Mark]\n\n"
        f"**Step 2:** Number in each hamper:\n"
        f"- Apples: ${item_a} \\div {hcf} = {apples_each}$\n"
        f"- Oranges: ${item_b} \\div {hcf} = {oranges_each}$ [1 Mark]\n\n"
        f"$$\\therefore {hcf} \\text{{ hampers ({apples_each} apples and {oranges_each} oranges each)}}$$"
    )
    ans = f"1. {hcf} hampers; 2. {apples_each} apples and {oranges_each} oranges per hamper"
    return {
        "id": f"g8_wn_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "18_word_problem_hcf_maximum_equal_packaging",
        "hints": {
            "tier_1": "Finding the greatest number of identical sets requires the HCF.",
            "tier_2": f"Find HCF({item_a}, {item_b}).",
            "tier_3": f"Maximum hampers = {hcf}."
        },
        "misconception_tags": ["hcf_word_problem_operation_confusion"]
    }


def arch_19_word_problem_lcm_repeating_cycle_alignment(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([12, 15, 20])
    t2 = rng.choice([18, 24, 30])
    lcm = math.lcm(t1, t2)

    prompt = (
        f"Two lighthouses along the KwaZulu-Natal coastline flash at regular intervals. "
        f"Lighthouse A flashes every **{t1} seconds**, while Lighthouse B flashes every **{t2} seconds**. "
        f"Both lighthouses flash simultaneously at 20:00.\n\n"
        f"After how many seconds will they next flash at the exact same moment?"
    )
    sol = (
        f"**Step 1:** The next simultaneous flash occurs at the $\\text{{LCM}}({t1}, {t2})$ [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate LCM:\n"
        f"$$\\text{{LCM}}({t1}, {t2}) = {lcm} \\text{{ seconds}}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {lcm} \\text{{ seconds (or {lcm // 60} minutes and {lcm % 60} seconds)}}$$"
    )
    ans = f"{lcm} seconds"
    return {
        "id": f"g8_wn_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "19_word_problem_lcm_repeating_cycle_alignment",
        "hints": {
            "tier_1": "Events that repeat at fixed cycles sync up at their Lowest Common Multiple (LCM).",
            "tier_2": f"Find LCM({t1}, {t2}).",
            "tier_3": f"Next simultaneous flash is after {lcm} seconds."
        },
        "misconception_tags": ["lcm_word_problem_multiplication_fallback"]
    }


def arch_20_co_prime_numbers_verification(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([8, 9, 14, 15, 16, 21, 25])
    p2 = rng.choice([27, 28, 33, 35, 49])
    while math.gcd(p1, p2) != 1:
        p2 += 1
    gcd_val = math.gcd(p1, p2)

    prompt = (
        f"1. Determine the Highest Common Factor (HCF) of **{p1}** and **{p2}**.\n"
        f"2. Based on your answer, state whether **{p1}** and **{p2}** are **co-prime (relatively prime)** numbers, and define what co-prime means."
    )
    sol = (
        f"**Step 1:** $\\text{{HCF}}({p1}, {p2}) = {gcd_val}$ [1 Mark].\n\n"
        f"**Step 2:** Because their highest common factor is $1$, **{p1}** and **{p2}** are **co-prime** numbers. "
        f"Two numbers are co-prime if they share no common factor other than $1$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{HCF}} = 1; \\text{{ They are co-prime}}$$"
    )
    ans = f"1. HCF = 1; 2. Yes, they are co-prime because their only common factor is 1"
    return {
        "id": f"g8_wn_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "20_co_prime_numbers_verification",
        "hints": {
            "tier_1": "Find the factors of each number.",
            "tier_2": "If the only common factor is 1, the numbers are co-prime.",
            "tier_3": f"HCF = 1. Yes, they are co-prime."
        },
        "misconception_tags": ["co_prime_requires_prime_numbers_misconception"]
    }


# ==============================================================================
# CLUSTER 3: Multi-Digit Addition & Subtraction (21 - 25)
# ==============================================================================

def arch_21_expanded_notation_6_digit_whole_number(rng: random.Random) -> Dict[str, Any]:
    d5 = rng.randint(1, 9)
    d4 = rng.randint(0, 9)
    d3 = rng.randint(1, 9)
    d2 = rng.randint(0, 9)
    d1 = rng.randint(1, 9)
    d0 = rng.randint(1, 9)
    val = d5 * 100000 + d4 * 10000 + d3 * 1000 + d2 * 100 + d1 * 10 + d0

    prompt = (
        f"Write the whole number **{val:,}** in expanded notation using powers of 10."
    )
    parts = []
    if d5: parts.append(f"({d5} \\times 10^5)")
    if d4: parts.append(f"({d4} \\times 10^4)")
    if d3: parts.append(f"({d3} \\times 10^3)")
    if d2: parts.append(f"({d2} \\times 10^2)")
    if d1: parts.append(f"({d1} \\times 10^1)")
    if d0: parts.append(f"({d0} \\times 10^0)")
    exp_str = " + ".join(parts)
    text_ans = " + ".join(parts).replace("\\times", "×")

    sol = (
        f"**Step 1:** Break each digit into its place value representation:\n"
        f"$${val:,} = {exp_str}$$ [2 Marks]\n\n"
        f"$$\\therefore {exp_str}$$"
    )
    return {
        "id": f"g8_wn_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": text_ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "21_expanded_notation_6_digit_whole_number",
        "hints": {
            "tier_1": "Hundred thousands is 10^5, ten thousands is 10^4, thousands is 10^3, etc.",
            "tier_2": "Write each non-zero digit multiplied by its power of 10.",
            "tier_3": f"{val:,} = {text_ans}."
        },
        "misconception_tags": ["power_of_ten_index_off_by_one"]
    }


def arch_22_place_value_and_face_value_identification(rng: random.Random) -> Dict[str, Any]:
    val = rng.randint(1200000, 8900000)
    val_str = f"{val:,}"
    digits = [c for c in str(val)]
    # Pick a random digit
    target_idx = rng.randint(0, len(digits) - 2)
    target_digit = int(digits[target_idx])
    power = len(digits) - 1 - target_idx
    place_val = target_digit * (10 ** power)

    place_names = {
        0: "Units", 1: "Tens", 2: "Hundreds", 3: "Thousands",
        4: "Ten Thousands", 5: "Hundred Thousands", 6: "Millions"
    }
    p_name = place_names.get(power, "Position")

    prompt = (
        f"For the whole number **{val_str}**:\n\n"
        f"1. What is the face value of the digit **{target_digit}** at position {p_name}?\n"
        f"2. What is the total place value of this digit?"
    )
    sol = (
        f"**Step 1:** Face value is simply the digit itself: **{target_digit}** [1 Mark].\n\n"
        f"**Step 2:** Place value = $\\text{{Face value}} \\times \\text{{Position value}} = {target_digit} \\times 10^{power} = {place_val:,}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{Face value}} = {target_digit}, \\quad \\text{{Place value}} = {place_val:,}$$"
    )
    ans = f"1. Face value = {target_digit}; 2. Place value = {place_val:,}"
    return {
        "id": f"g8_wn_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_place_value_and_face_value_identification",
        "hints": {
            "tier_1": "Face value is the digit itself. Place value is what the digit is worth based on its column.",
            "tier_2": f"Position is {p_name} ({10**power:,}).",
            "tier_3": f"Face value = {target_digit}; Place value = {place_val:,}."
        },
        "misconception_tags": ["face_value_place_value_confusion"]
    }


def arch_23_rounding_off_to_nearest_100_and_1000(rng: random.Random) -> Dict[str, Any]:
    val = rng.randint(14500, 98900)
    r100 = round(val / 100) * 100
    r1000 = round(val / 1000) * 1000

    prompt = (
        f"Round off the whole number **{val:,}**:\n\n"
        f"1. To the nearest 100.\n"
        f"2. To the nearest 1 000."
    )
    sol = (
        f"**Step 1:** Nearest 100: Look at tens digit. Rounded value = **{r100:,}** [1 Mark].\n\n"
        f"**Step 2:** Nearest 1 000: Look at hundreds digit. Rounded value = **{r1000:,}** [1 Mark].\n\n"
        f"$$\\therefore \\text{{Nearest 100}} = {r100:,}, \\quad \\text{{Nearest 1000}} = {r1000:,}$$"
    )
    ans = f"1. {r100:,}; 2. {r1000:,}"
    return {
        "id": f"g8_wn_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "23_rounding_off_to_nearest_100_and_1000",
        "hints": {
            "tier_1": "For nearest 100, inspect the tens digit (≥5 rounds up).",
            "tier_2": "For nearest 1 000, inspect the hundreds digit.",
            "tier_3": f"Nearest 100 = {r100:,}; Nearest 1000 = {r1000:,}."
        },
        "misconception_tags": ["rounding_benchmark_digit_slip"]
    }


def arch_24_rounding_off_to_nearest_10000_and_100000(rng: random.Random) -> Dict[str, Any]:
    val = rng.randint(245000, 985000)
    r10k = round(val / 10000) * 10000
    r100k = round(val / 100000) * 100000

    prompt = (
        f"Round off the number **{val:,}**:\n\n"
        f"1. To the nearest 10 000.\n"
        f"2. To the nearest 100 000."
    )
    sol = (
        f"**Step 1:** To the nearest 10 000: Look at thousands digit: **{r10k:,}** [1 Mark].\n\n"
        f"**Step 2:** To the nearest 100 000: Look at ten-thousands digit: **{r100k:,}** [1 Mark].\n\n"
        f"$$\\therefore \\text{{Nearest 10 000}} = {r10k:,}, \\quad \\text{{Nearest 100 000}} = {r100k:,}$$"
    )
    ans = f"1. {r10k:,}; 2. {r100k:,}"
    return {
        "id": f"g8_wn_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "24_rounding_off_to_nearest_10000_and_100000",
        "hints": {
            "tier_1": "Inspect the digit immediately to the right of the target place value.",
            "tier_2": "5 or more rounds up; 4 or less rounds down.",
            "tier_3": f"Nearest 10k: {r10k:,}; Nearest 100k: {r100k:,}."
        },
        "misconception_tags": ["rounding_large_numbers_truncation_error"]
    }


def arch_25_column_addition_with_multiple_carries(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(25600, 89700)
    n2 = rng.randint(14500, 68900)
    total = n1 + n2

    prompt = (
        f"Calculate the exact sum using vertical column addition, showing all carry figures:\n\n"
        f"$$\\begin{{array}}{{r@{{\\quad}}l}}\n"
        f"& {n1:,} \\\\\n"
        f"+ & {n2:,} \\\\\n"
        f"\\hline\n"
        f"\\end{{array}}$$"
    )
    sol = (
        f"**Step 1:** Align columns by place value and add from units to ten-thousands, carrying over when sum $\\ge 10$ [1 Mark: Method].\n\n"
        f"**Step 2:** Sum: $${n1:,} + {n2:,} = {total:,}$$ [1 Mark: Accuracy]\n\n"
        f"$$\\therefore {total:,}$$"
    )
    ans = f"{total:,}"
    return {
        "id": f"g8_wn_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "25_column_addition_with_multiple_carries",
        "hints": {
            "tier_1": "Add column by column starting from the units on the far right.",
            "tier_2": "Remember to carry forward groups of 10 to the next column on the left.",
            "tier_3": f"Final sum is {total:,}."
        },
        "misconception_tags": ["column_addition_carry_omission"]
    }
