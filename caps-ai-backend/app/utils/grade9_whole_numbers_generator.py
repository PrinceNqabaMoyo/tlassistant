import random
import time
from typing import Any, Dict, List, Optional


def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


def _normalize(s: str) -> str:
    return str(s).strip().replace('−', '-').replace(' ', '')


def _make_typed(*, prompt: str, correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'typed',
        'question': prompt,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_mcq(*, prompt: str, options: List[str], correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'mcq',
        'question': prompt,
        'options': options,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_scaffold(*, prompt: str, steps: List[str], checkpoints: List[Dict[str, Any]], final_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'scaffold',
        'question': prompt,
        'steps': steps,
        'checkpoints': checkpoints,
        'correct_answer': str(final_answer),
        'explanation': explanation,
        **extra,
    }


def _validate_question(q: Dict[str, Any]) -> None:
    required = {'id', 'topic', 'subskill', 'difficulty', 'question_type', 'question', 'correct_answer', 'explanation'}
    missing = [k for k in required if k not in q]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")


def _int_choices(difficulty: str) -> List[int]:
    if difficulty == 'easy':
        return [1, 2, 3, 4, 5, 6, 8, 9, 10]
    if difficulty == 'medium':
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    return [3, 4, 5, 6, 7, 8, 9, 10, 12, 15]


def _gen_closure_table(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Based on Q9: table of number systems closed under operations
    headers = ['Statement', 'Natural', 'Whole', 'Integers', 'Rational']

    rows = [
        ['Closed under addition', 'yes', 'yes', 'yes', 'yes'],
        ['Sum is always bigger than either addend', 'yes', 'no', 'no', 'no'],
        ['Closed under subtraction', 'no', 'no', 'yes', 'yes'],
        ['Difference always smaller than first number', 'no', 'no', 'no', 'no'],
        ['Closed under multiplication', 'yes', 'yes', 'yes', 'yes'],
        ['Product always bigger than either factor', 'no', 'no', 'no', 'no'],
        ['Closed under division', 'no', 'no', 'no', 'yes'],
        ['Quotient always smaller than first number', 'no', 'no', 'no', 'no'],
    ]

    prompt = 'Complete the table by writing yes/no in each cell.'
    explanation = 'Use closure and counterexamples (e.g. 5−8 is not whole; 10÷3 is not natural; 1+0 is not bigger; etc.).'

    # Ask a single cell so we can auto-mark
    r = int(rng.randrange(0, len(rows)))
    c = int(rng.randrange(1, len(headers)))
    statement = rows[r][0]
    system = headers[c]
    correct = rows[r][c]

    if qtype == 'mcq':
        return _make_mcq(
            prompt=f"In the table, what is the correct entry for '{statement}' in {system} numbers?",
            options=['yes', 'no'],
            correct_answer=correct,
            explanation=explanation,
            table={'headers': headers, 'rows': rows},
        )

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Consider '{statement}' for {system} numbers. Is it always true? (yes/no)",
                'correct_answer': correct,
                'explanation': explanation,
            }
        ]
        steps = ['Recall the definition (closure / always bigger / etc.).', 'Use an example or counterexample.', 'Answer yes or no.']
        return _make_scaffold(
            prompt=f"Answer and justify: '{statement}' for {system} numbers. (yes/no)",
            steps=steps,
            checkpoints=checkpoints,
            final_answer=correct,
            explanation=explanation,
            table={'headers': headers, 'rows': rows},
        )

    return _make_typed(
        prompt=f"In the table, what is the correct entry for '{statement}' in {system} numbers? (yes/no)",
        correct_answer=correct,
        explanation=explanation,
        table={'headers': headers, 'rows': rows},
    )


def _gen_rounding_estimation(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Estimate product by rounding (Q3 style)
    qty = int(rng.randrange(50, 250))
    price = int(rng.randrange(30, 950))

    round_to = 100 if difficulty == 'easy' else (50 if difficulty == 'medium' else 10)

    qty_r = int(round(qty / round_to) * round_to)
    price_r = int(round(price / round_to) * round_to)

    est = qty_r * price_r

    prompt = f"Estimate {qty} × {price} by rounding both numbers to the nearest {round_to}, then multiply."
    explanation = f"Round {qty}→{qty_r} and {price}→{price_r}, then multiply: {qty_r}×{price_r}={est}."

    if qtype == 'mcq':
        options = list({str(est), str(est + round_to * 100), str(max(0, est - round_to * 100)), str(est + round_to * 50)})
        while len(options) < 4:
            options.append(str(est))
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(est), explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Round {qty} to the nearest {round_to}:",
                'correct_answer': str(qty_r),
                'explanation': 'Round to the nearest given base.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Round {price} to the nearest {round_to}:",
                'correct_answer': str(price_r),
                'explanation': 'Round to the nearest given base.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now multiply {qty_r} × {price_r}:",
                'correct_answer': str(est),
                'explanation': 'Multiply the rounded numbers.',
            },
        ]
        steps = ['Round each factor.', 'Multiply the rounded values.', 'State the estimate.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(est), explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=str(est), explanation=explanation)


def _format_long_division_ascii(dividend: int, divisor: int, quotient: int, remainder: int, partials: List[Dict[str, int]]) -> str:
    # Simple monospaced layout; no bracket glyph required.
    lines = []
    lines.append(f"{dividend} ÷ {divisor}")
    lines.append(f"{divisor} ) {dividend}")
    lines.append(f"quotient = {quotient} remainder {remainder}")
    lines.append('')
    lines.append('Working (subtract partial products):')
    current = dividend
    for p in partials:
        take = p['take']
        prod = take * divisor
        current -= prod
        lines.append(f"take {take:>4} × {divisor} = {prod:>6}  -> remainder {current}")
    return "\n".join(lines)


def _gen_long_division(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Generate division with remainder and provide ASCII working.
    divisor = int(rng.choice([12, 14, 15, 18, 21, 24, 27, 28, 35, 42, 56, 63] if difficulty != 'hard' else [27, 28, 35, 42, 44, 56, 63, 72, 84, 96]))
    quotient = int(rng.randrange(120, 420) if difficulty != 'easy' else rng.randrange(80, 240))
    remainder = int(rng.randrange(0, divisor))
    dividend = divisor * quotient + remainder

    prompt = f"Calculate {dividend} ÷ {divisor}. Give your answer as 'quotient remainder r'."
    correct = f"{quotient} remainder {remainder}"

    # Greedy partials similar to the doc's approach (estimate chunks)
    partials = []
    remaining = dividend
    for take in [200, 100, 50, 30, 20, 10, 6, 5, 4, 3, 2, 1]:
        if remaining >= take * divisor and (len(partials) == 0 or take <= partials[-1]['take']):
            while remaining >= take * divisor and sum(p['take'] for p in partials) + take <= quotient:
                partials.append({'take': take})
                remaining -= take * divisor
                if sum(p['take'] for p in partials) == quotient:
                    break
        if sum(p['take'] for p in partials) == quotient:
            break

    explanation = 'Use long division: estimate how many times the divisor fits, subtract partial products, and continue.'
    ascii_working = _format_long_division_ascii(dividend, divisor, quotient, remainder, partials)

    if qtype == 'mcq':
        options = [
            correct,
            f"{quotient + 1} remainder {remainder}",
            f"{quotient} remainder {max(0, remainder - 1)}",
            f"{max(0, quotient - 1)} remainder {remainder}",
        ]
        options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, long_division=ascii_working)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the quotient (whole number part) of {dividend} ÷ {divisor}?",
                'correct_answer': str(quotient),
                'explanation': 'This is how many whole times the divisor fits.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the remainder of {dividend} ÷ {divisor}?",
                'correct_answer': str(remainder),
                'explanation': 'Remainder is what is left after subtracting divisor×quotient.',
            },
        ]
        steps = ['Estimate a chunk of the quotient.', 'Subtract divisor×chunk.', 'Repeat until remainder < divisor.', 'State quotient and remainder.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, long_division=ascii_working)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, long_division=ascii_working)


def _gen_prime_factors(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    primes = [2, 3, 5, 7, 11, 13]
    factors = []
    count = 3 if difficulty == 'easy' else (4 if difficulty == 'medium' else 5)
    for _ in range(count):
        factors.append(int(rng.choice(primes)))
    n = 1
    for f in factors:
        n *= f

    # Build prime factorization string like 2^3 × 3 × 5
    exp = {}
    for f in factors:
        exp[f] = exp.get(f, 0) + 1
    parts = []
    for p in sorted(exp.keys()):
        e = exp[p]
        parts.append(f"{p}^{e}" if e > 1 else str(p))
    pf = ' × '.join(parts)

    prompt = f"Write the prime factorisation of {n} using exponent notation."
    explanation = 'Divide by primes and group equal prime factors; write repeated primes with an exponent.'

    if qtype == 'mcq':
        wrong1 = ' × '.join([str(p) for p in sorted(exp.keys())])
        wrong2 = pf.replace('^', '')
        options = list(dict.fromkeys([pf, wrong1, wrong2, pf + ' × 1']))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=pf, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'List the prime factors (you may repeat them, separated by ×):',
                'correct_answer': ' × '.join(str(f) for f in sorted(factors)),
                'explanation': 'These primes multiply to the number.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Now write using exponent notation:',
                'correct_answer': pf,
                'explanation': 'Group identical primes and use exponents.',
            },
        ]
        steps = ['Factor the number into primes.', 'Group equal primes.', 'Use exponents for repeats.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=pf, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=pf, explanation=explanation)


def generate_grade9_whole_numbers_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    topic = 'Whole numbers'
    difficulty = (difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = (question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    subskill = (subskill or 'mixed').lower()

    generators = {
        'number_systems_table': _gen_closure_table,
        'rounding_estimation': _gen_rounding_estimation,
        'long_division': _gen_long_division,
        'prime_factorisation': _gen_prime_factors,
    }

    if subskill == 'mixed' or subskill not in generators:
        keys = list(generators.keys())
        subskill = keys[int(rng.randrange(0, len(keys)))]

    q = generators[subskill](rng, difficulty, qtype)

    q.update(
        {
            'id': _make_id('g9_whole'),
            'topic': topic,
            'subskill': subskill,
            'difficulty': difficulty,
        }
    )
    q['_normalized_correct_answer'] = _normalize(q.get('correct_answer', ''))
    _validate_question(q)
    return q
