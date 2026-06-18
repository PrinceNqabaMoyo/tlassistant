import random
import time
from typing import Any, Dict, List, Optional, Tuple


def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


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


def _make_scaffold(*, prompt: str, steps: List[Dict[str, str]], checkpoints: List[Dict[str, Any]], final_answer: str, explanation: str, **extra) -> Dict[str, Any]:
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

    if q['question_type'] not in {'typed', 'mcq', 'scaffold'}:
        raise ValueError('Invalid question_type')

    if q['question_type'] == 'mcq':
        if not isinstance(q.get('options'), list) or len(q.get('options', [])) < 2:
            raise ValueError('MCQ must include options list')
        if str(q['correct_answer']) not in [str(o) for o in q.get('options', [])]:
            raise ValueError('MCQ correct_answer must be one of options')

    if q['question_type'] == 'scaffold':
        if not isinstance(q.get('steps'), list) or len(q.get('steps', [])) < 1:
            raise ValueError('Scaffold must include steps')
        if not isinstance(q.get('checkpoints'), list) or len(q.get('checkpoints', [])) < 1:
            raise ValueError('Scaffold must include checkpoints')


def _format_with_spaces(n: int) -> str:
    return f"{n:,}".replace(',', ' ')


def _prime_factorization(n: int) -> Dict[int, int]:
    if n < 2:
        return {}
    factors: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _factorization_to_product_string(factors: Dict[int, int]) -> str:
    parts: List[str] = []
    for p in sorted(factors.keys()):
        parts.extend([str(p)] * int(factors[p]))
    return ' × '.join(parts) if parts else '1'


def _factorization_to_powers_string(factors: Dict[int, int]) -> str:
    parts: List[str] = []
    for p in sorted(factors.keys()):
        e = int(factors[p])
        if e == 1:
            parts.append(str(p))
        else:
            parts.append(f"{p}^{e}")
    return ' × '.join(parts) if parts else '1'


def _pick_int(rng: random.Random, low: int, high: int) -> int:
    return rng.randint(low, high)


def _digits(n: int) -> List[int]:
    return [int(ch) for ch in str(abs(n))]


def _choose_digits_for_difficulty(difficulty: str) -> int:
    if difficulty == 'easy':
        return 3
    if difficulty == 'medium':
        return 4
    return 5


def _make_number_with_digits(rng: random.Random, digits: int) -> int:
    digits = max(2, min(8, int(digits)))
    first = rng.randint(1, 9)
    rest = [rng.randint(0, 9) for _ in range(digits - 1)]
    return int(str(first) + ''.join(str(d) for d in rest))


def _gen_beads_array_choice(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    rows = rng.choice([8, 9, 10, 12]) if difficulty != 'hard' else rng.choice([9, 10, 12, 15])
    total_cols = rng.choice([10, 12]) if difficulty != 'hard' else rng.choice([12, 14, 15])
    red_cols = rng.randint(3, total_cols - 3)
    yellow_cols = total_cols - red_cols

    prompt = (
        f"A bead pattern has {rows} rows and {total_cols} columns. {red_cols} columns are red and {yellow_cols} columns are yellow. "
        "Which calculation would you choose to find the number of yellow beads? (Choose, do not calculate.)"
    )

    # Correct: yellow columns × rows
    correct = f"{yellow_cols} × {rows}"
    options = [
        correct,
        f"{red_cols} × {rows}",
        f"{rows} + {rows} + {rows} + {rows}",
        f"{yellow_cols} + {yellow_cols} + {yellow_cols}"
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(2, 12)} × {rng.randint(2, 12)}")
        options = list(dict.fromkeys(options))
    options = options[:4]
    rng.shuffle(options)
    explanation = "Yellow beads are arranged in yellow columns, each with one bead per row, so use (yellow columns) × (rows)."

    return _make_mcq(
        prompt=prompt,
        options=options,
        correct_answer=correct,
        explanation=explanation,
        parameters={'rows': rows, 'cols_total': total_cols, 'red_cols': red_cols, 'yellow_cols': yellow_cols},
    )


def _gen_commutative_or_not(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 3, 30) if difficulty != 'hard' else _pick_int(rng, 10, 90)
    b = _pick_int(rng, 3, 30) if difficulty != 'hard' else _pick_int(rng, 10, 90)
    op = rng.choice(['+', '×', '−', '÷'])
    prompt = f"Does swapping the numbers change the answer: {a} {op} {b} vs {b} {op} {a}? Answer Yes/No."
    if op in {'+', '×'}:
        correct = 'No'
        explanation = 'Addition and multiplication are commutative (swapping does not change the result).'
    else:
        correct = 'Yes'
        explanation = 'Subtraction and division are not commutative (swapping usually changes the result).'

    if qtype == 'mcq':
        options = ['Yes', 'No']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'op': op})


def _gen_identity_properties(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n = _pick_int(rng, 15, 500) if difficulty != 'easy' else _pick_int(rng, 5, 200)
    kind = rng.choice(['add_zero', 'times_one'])

    if kind == 'add_zero':
        prompt = f"What is {n} + 0 ?"
        correct = str(n)
        explanation = 'Additive identity: adding 0 does not change a number.'
    else:
        prompt = f"What is {n} × 1 ?"
        correct = str(n)
        explanation = 'Multiplicative identity: multiplying by 1 does not change a number.'

    if qtype == 'mcq':
        options = [correct, str(n + 1), str(max(0, n - 1)), '0']
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n, 'kind': kind})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n, 'kind': kind})


def _gen_brackets_conventions(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Based on Q12 style: same numbers/operators but different brackets -> different results
    a = _pick_int(rng, 4, 12)
    b = _pick_int(rng, 3, 9)
    c = _pick_int(rng, 3, 9)
    d = _pick_int(rng, 1, 6)

    expr = f"{a} + {b} × {c} − {d}"
    target_kind = rng.choice(['mul_first', 'bracket_add', 'bracket_sub'])

    if target_kind == 'mul_first':
        correct_expr = expr
        correct_value = a + b * c - d
    elif target_kind == 'bracket_add':
        correct_expr = f"({a} + {b}) × {c} − {d}"
        correct_value = (a + b) * c - d
    else:
        correct_expr = f"{a} + {b} × ({c} − {d})"
        correct_value = a + b * (c - d)

    prompt = f"Insert brackets to make the expression equal {correct_value}: {expr}"
    options = [
        correct_expr,
        expr,
        f"({a} + {b} × {c}) − {d}",
        f"{a} + ({b} × {c} − {d})",
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"({a} + {b}) × ({c} − {d})")
        options = list(dict.fromkeys(options))
    options = options[:4]
    rng.shuffle(options)
    explanation = 'Brackets tell you what to do first (before multiplication/addition rules apply).'

    return _make_mcq(prompt=prompt, options=options, correct_answer=correct_expr, explanation=explanation, parameters={'expr': expr, 'target': correct_value})


def _gen_estimate_nearest_thousand_or_hundred(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    is_product = rng.random() < 0.5
    if is_product:
        a = _pick_int(rng, 20, 99)
        b = _pick_int(rng, 90, 399) if difficulty != 'easy' else _pick_int(rng, 80, 199)
        exact = a * b
        base = 1000
        prompt = f"Estimate {a} × {b} to the nearest {base}. Give your estimate."
    else:
        a = _make_number_with_digits(rng, 3 if difficulty == 'easy' else 4)
        b = _make_number_with_digits(rng, 3 if difficulty == 'easy' else 4)
        exact = a + b
        base = 100
        prompt = f"Estimate {_format_with_spaces(a)} + {_format_with_spaces(b)} to the nearest {base}. Give your estimate."

    estimate = int(base * round(exact / base))
    explanation = f"Round the result to the nearest {base}. Exact is {exact}, estimate is {estimate}."

    if qtype == 'mcq':
        options = [str(estimate), str(int(base * (exact // base))), str(int(base * (exact // base) + base)), str(estimate + base)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(estimate), explanation=explanation, parameters={'exact': exact, 'base': base})

    return _make_typed(prompt=prompt, correct_answer=str(estimate), explanation=explanation, parameters={'exact': exact, 'base': base})


def _column_addition_steps(a: int, b: int) -> Tuple[int, List[Dict[str, Any]]]:
    da = list(reversed(_digits(a)))
    db = list(reversed(_digits(b)))
    ncols = max(len(da), len(db))
    carry = 0
    checkpoints: List[Dict[str, Any]] = []
    out_digits: List[int] = []

    for i in range(ncols):
        xa = da[i] if i < len(da) else 0
        xb = db[i] if i < len(db) else 0
        s = xa + xb + carry
        digit = s % 10
        next_carry = s // 10
        out_digits.append(digit)

        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Column {i+1} from the right: {xa} + {xb} + carry {carry} = {s}. What digit do you write?",
                'correct_answer': str(digit),
                'explanation': 'Write the units digit of the column sum.',
            }
        )

        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What carry do you take to the next column from {s}?",
                'correct_answer': str(next_carry),
                'explanation': 'Carry the tens part to the next column.',
            }
        )

        carry = next_carry

    if carry:
        out_digits.append(carry)

    total = int(''.join(str(d) for d in reversed(out_digits)))
    return total, checkpoints


def _gen_column_addition(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    digits = 4 if difficulty == 'easy' else (5 if difficulty == 'medium' else 6)
    a = _make_number_with_digits(rng, digits)
    b = _make_number_with_digits(rng, digits - 1)
    total = a + b
    prompt = f"Add in columns: {_format_with_spaces(a)} + {_format_with_spaces(b)}"
    explanation = f"Align place values (units under units) and add right to left, carrying when needed. Answer: {_format_with_spaces(total)}."

    if qtype == 'scaffold':
        final, checkpoints = _column_addition_steps(a, b)
        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': _format_with_spaces(final),
                'explanation': explanation,
            }
        )
        steps = [
            'Line up digits by place value.',
            'Add from the units column to the left.',
            'Carry tens to the next column when needed.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=_format_with_spaces(final), explanation=explanation, parameters={'a': a, 'b': b})

    return _make_typed(prompt=prompt, correct_answer=_format_with_spaces(total), explanation=explanation, parameters={'a': a, 'b': b})


def _borrow_subtraction_steps(a: int, b: int) -> Tuple[int, List[Dict[str, Any]]]:
    da = list(reversed(_digits(a)))
    db = list(reversed(_digits(b)))
    ncols = max(len(da), len(db))
    borrow = 0
    out_digits: List[int] = []
    checkpoints: List[Dict[str, Any]] = []

    for i in range(ncols):
        xa = da[i] if i < len(da) else 0
        xb = db[i] if i < len(db) else 0

        xa_adj = xa - borrow
        if xa_adj < xb:
            xa_adj += 10
            next_borrow = 1
        else:
            next_borrow = 0

        digit = xa_adj - xb
        out_digits.append(digit)

        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Column {i+1} from the right: ({xa} − borrow {borrow}) compared to {xb}. What digit do you write after borrowing if needed?",
                'correct_answer': str(digit),
                'explanation': 'Borrow 10 if the top is smaller, then subtract.',
            }
        )
        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Do you borrow 1 from the next column? (0 or 1)',
                'correct_answer': str(next_borrow),
                'explanation': 'Borrow when needed to make the subtraction possible.',
            }
        )

        borrow = next_borrow

    while len(out_digits) > 1 and out_digits[-1] == 0:
        out_digits.pop()
    diff = int(''.join(str(d) for d in reversed(out_digits)))
    return diff, checkpoints


def _gen_subtraction_number_line(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # number line jump method (difference as distance)
    a = _make_number_with_digits(rng, 3 if difficulty == 'easy' else 4)
    b = _make_number_with_digits(rng, 3 if difficulty == 'easy' else 4)
    hi, lo = (a, b) if a >= b else (b, a)
    diff = hi - lo

    to_next_hundred = ((lo // 100) + 1) * 100
    step1 = to_next_hundred - lo
    to_base = (hi // 100) * 100
    step2 = max(0, to_base - to_next_hundred)
    step3 = hi - to_base
    prompt = f"Use a number-line jump method to find {_format_with_spaces(hi)} − {_format_with_spaces(lo)}. Give the answer."
    explanation = f"Jump: {lo}→{to_next_hundred} (+{step1}), {to_next_hundred}→{to_base} (+{step2}), {to_base}→{hi} (+{step3}). Total difference {diff}."

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"First jump: {lo} to {to_next_hundred}. What is the jump size?",
                'correct_answer': str(step1),
                'explanation': 'Count up to the next hundred.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Second jump: {to_next_hundred} to {to_base}. What is the jump size?",
                'correct_answer': str(step2),
                'explanation': 'Count in hundreds.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Last jump: {to_base} to {hi}. What is the jump size?",
                'correct_answer': str(step3),
                'explanation': 'Count up to the target number.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': str(diff),
                'explanation': explanation,
            },
        ]
        steps = [
            'Count up from the smaller number to a friendly number (e.g., next hundred).',
            'Make big jumps (hundreds or thousands).',
            'Finish with the last small jump and add the jumps.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(diff), explanation=explanation, parameters={'hi': hi, 'lo': lo})

    return _make_typed(prompt=prompt, correct_answer=str(diff), explanation=explanation, parameters={'hi': hi, 'lo': lo})


def _gen_subtraction_borrowing_columns(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    digits = 4 if difficulty == 'easy' else (5 if difficulty == 'medium' else 6)
    a = _make_number_with_digits(rng, digits)
    b = _make_number_with_digits(rng, digits)
    if b >= a:
        a, b = b + rng.randint(10, 99), a
    diff = a - b
    prompt = f"Subtract using borrowing (column method): {_format_with_spaces(a)} − {_format_with_spaces(b)}"
    explanation = f"Subtract right to left. Borrow from the next column when the top digit is smaller. Answer: {_format_with_spaces(diff)}."

    if qtype == 'scaffold':
        final, checkpoints = _borrow_subtraction_steps(a, b)
        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': _format_with_spaces(final),
                'explanation': explanation,
            }
        )
        steps = [
            'Line up digits by place value.',
            'Subtract from the units column to the left.',
            'If the top is smaller, borrow 10 from the next column.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=_format_with_spaces(final), explanation=explanation, parameters={'a': a, 'b': b})

    return _make_typed(prompt=prompt, correct_answer=_format_with_spaces(diff), explanation=explanation, parameters={'a': a, 'b': b})


def _gen_multiplication_in_parts(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Matches doc's "multiply in parts" / vertical method with carrying.
    multiplier = rng.choice([6, 7, 8, 9]) if difficulty != 'easy' else rng.choice([3, 4, 5, 6, 7])
    multiplicand = _make_number_with_digits(rng, 4 if difficulty == 'easy' else 5)
    product = multiplier * multiplicand

    parts = []
    place = 1
    n = multiplicand
    while n > 0:
        d = n % 10
        parts.append((d * place, d))
        n //= 10
        place *= 10

    prompt = f"Calculate {multiplier} × {_format_with_spaces(multiplicand)} using multiplication in parts / columns."
    explanation = f"Multiply each place-value part by {multiplier} and add the partial products. Answer: {_format_with_spaces(product)}."

    if qtype == 'scaffold':
        checkpoints: List[Dict[str, Any]] = []
        partials = []
        for value, digit in parts:
            partial = multiplier * value
            partials.append(partial)
            checkpoints.append(
                {
                    'id': _make_id('cp'),
                    'kind': 'typed',
                    'prompt': f"Compute {multiplier} × {_format_with_spaces(value)}.",
                    'correct_answer': _format_with_spaces(partial),
                    'explanation': 'Multiply the place-value part.',
                }
            )
        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Add the partial products: {' + '.join(_format_with_spaces(p) for p in partials)}",
                'correct_answer': _format_with_spaces(product),
                'explanation': explanation,
            }
        )
        steps = [
            'Split the big number into place-value parts (thousands, hundreds, tens, units).',
            'Multiply each part by the single-digit multiplier.',
            'Add the partial products to get the final answer.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=_format_with_spaces(product), explanation=explanation, parameters={'multiplier': multiplier, 'multiplicand': multiplicand})

    return _make_typed(prompt=prompt, correct_answer=_format_with_spaces(product), explanation=explanation, parameters={'multiplier': multiplier, 'multiplicand': multiplicand})


def _gen_long_division_chunking(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Chunking / partial quotients like the tree example.
    divisor = rng.randint(12, 98)
    quotient = rng.randint(120, 480) if difficulty != 'easy' else rng.randint(40, 250)
    remainder = rng.randint(0, divisor - 1)
    dividend = divisor * quotient + remainder

    prompt = f"Use long division (chunking) to calculate {_format_with_spaces(dividend)} ÷ {divisor}. Give quotient and remainder."
    correct = f"{quotient} R {remainder}"
    explanation = f"Divide by taking convenient chunks (e.g., hundreds, tens, ones) until the remainder is less than the divisor. Answer: {correct}."

    if qtype == 'scaffold':
        # Use three chunks: hundreds, tens, ones (greedy).
        remaining = dividend
        q_so_far = 0
        checkpoints: List[Dict[str, Any]] = []

        for chunk in [100, 10, 1]:
            chunk_q = (remaining // divisor) // chunk * chunk
            if chunk_q <= 0:
                continue
            chunk_value = chunk_q * divisor
            checkpoints.append(
                {
                    'id': _make_id('cp'),
                    'kind': 'typed',
                    'prompt': f"Choose a chunk for the quotient (multiple of {chunk}). What chunk do you subtract now?",
                    'correct_answer': str(chunk_q),
                    'explanation': f"Take as many groups of {divisor} as possible in steps of {chunk}.",
                }
            )
            checkpoints.append(
                {
                    'id': _make_id('cp'),
                    'kind': 'typed',
                    'prompt': f"Compute {chunk_q} × {divisor}.",
                    'correct_answer': _format_with_spaces(chunk_value),
                    'explanation': 'Multiply the chunk of the quotient by the divisor.',
                }
            )
            remaining -= chunk_value
            q_so_far += chunk_q
            checkpoints.append(
                {
                    'id': _make_id('cp'),
                    'kind': 'typed',
                    'prompt': 'New remainder after subtraction:',
                    'correct_answer': _format_with_spaces(remaining),
                    'explanation': 'Subtract to see what is left.',
                }
            )

        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': "Final answer (quotient R remainder):",
                'correct_answer': correct,
                'explanation': explanation,
            }
        )
        steps = [
            'Start with the dividend.',
            'Subtract big chunks: (hundreds of divisor), then tens, then ones.',
            'Add chunk quotients to get the quotient; what is left is the remainder.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'dividend': dividend, 'divisor': divisor})

    if qtype == 'mcq':
        options = [
            correct,
            f"{quotient + 1} R {max(0, remainder - divisor)}",
            f"{max(0, quotient - 1)} R {remainder}",
            f"{quotient} R {min(divisor - 1, remainder + 1)}",
        ]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'dividend': dividend, 'divisor': divisor})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'dividend': dividend, 'divisor': divisor})


def _gen_multiples_sequence(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    k = rng.choice([6, 7, 8, 9, 12])
    n = 100 if difficulty != 'hard' else 150
    value = k * n
    prompt = f"What is the {n}th multiple of {k}?"
    explanation = f"The nth multiple of {k} is {k}×{n} = {value}."

    if qtype == 'mcq':
        options = [str(value), str(k * (n - 1)), str(k * (n + 1)), str(value + k)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(value), explanation=explanation, parameters={'k': k, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=str(value), explanation=explanation, parameters={'k': k, 'n': n})


def _gen_factors_rectangle_area(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    area = rng.choice([24, 30, 36, 48, 60, 72]) if difficulty != 'hard' else rng.choice([84, 96, 108, 120, 144])
    pairs = []
    for a in range(1, int(area ** 0.5) + 1):
        if area % a == 0:
            pairs.append((a, area // a))

    pair_str = '; '.join([f"{x}×{y}" for x, y in pairs])
    prompt = f"A rectangle has area {area} cm². List possible whole-number side-length pairs (length × width)."
    explanation = f"Side lengths must multiply to {area}. Possible pairs: {pair_str}."
    return _make_typed(prompt=prompt, correct_answer=pair_str, explanation=explanation, parameters={'area': area, 'pairs': pairs})


def _gen_common_multiple_statement(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = rng.choice([4, 6, 8, 9, 10, 12])
    b = rng.choice([5, 6, 7, 8, 9, 11])
    prod = a * b
    prompt = f"Is {a} × {b} a multiple of {a}? Is it a multiple of {b}? Answer 'Yes and Yes', 'Yes and No', 'No and Yes', or 'No and No'."
    correct = 'Yes and Yes'
    explanation = f"{a}×{b} contains {a} as a factor, so it is a multiple of {a}; and it contains {b} as a factor, so it is a multiple of {b}."

    if qtype == 'typed':
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'product': prod})

    options = ['Yes and Yes', 'Yes and No', 'No and Yes', 'No and No']
    rng.shuffle(options)
    return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'product': prod})


def _gen_rate_and_ratio_problem(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    variant = rng.choice(['trees_per_day', 'distance_time', 'money_split_ratio'])

    if variant == 'trees_per_day':
        total = rng.choice([3000000, 2400000, 1800000])
        rate = rng.choice([15000, 12000, 20000])
        days = total // rate
        prompt = f"At a rate of {rate} trees per day, how many working days are needed to cut down {total:,} trees?"
        prompt = prompt.replace(',', ' ')
        explanation = f"Days = total ÷ rate = {total} ÷ {rate} = {days}."
        correct = str(days)
    elif variant == 'distance_time':
        dist = rng.choice([180, 240, 150])
        hours = rng.choice([2, 3, 4])
        target_hours = hours + rng.choice([1, 2])
        speed = dist / hours
        new_dist = int(speed * target_hours)
        prompt = f"A car travels {dist} km in {hours} hours. How far (km) in {target_hours} hours at the same speed?"
        explanation = f"Speed = {dist}/{hours} = {speed} km/h. Distance = speed×time = {new_dist} km."
        correct = str(new_dist)
    else:
        total = 600
        ratio = (5, 4, 3)
        parts = sum(ratio)
        share = [int(total * r / parts) for r in ratio]
        prompt = "Nathi, Paul and Tim worked 5, 4 and 3 hours respectively and earned R600. Divide the money in the ratio 5:4:3. Give 'Nathi, Paul, Tim'."
        correct = f"{share[0]}, {share[1]}, {share[2]}"
        explanation = f"Total parts = {parts}. Each part = 600/{parts} = {total//parts}. Shares: 5×{total//parts}={share[0]}, 4×{total//parts}={share[1]}, 3×{total//parts}={share[2]}."

    if qtype == 'mcq':
        options = [correct]
        while len(options) < 4:
            tweak = str(int(correct.split(',')[0]) + rng.randint(-10, 10)) if ',' in correct else str(int(correct) + rng.randint(-10, 10))
            if tweak != correct:
                options.append(tweak)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'variant': variant})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'variant': variant})


def _gen_commutative(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 6, 40) if difficulty != 'easy' else _pick_int(rng, 3, 20)
    b = _pick_int(rng, 6, 40) if difficulty == 'hard' else _pick_int(rng, 3, 20)

    op = rng.choice(['addition', 'multiplication'])
    if op == 'addition':
        correct = 'Yes'
        explanation = 'Addition is commutative: a + b = b + a.'
        prompt = f"Is {a} + {b} equal to {b} + {a}? (Yes/No)"
    else:
        correct = 'Yes'
        explanation = 'Multiplication is commutative: a × b = b × a.'
        prompt = f"Is {a} × {b} equal to {b} × {a}? (Yes/No)"

    if qtype == 'mcq':
        options = ['Yes', 'No']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'op': op})


def _gen_associative(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 2, 12)
    b = _pick_int(rng, 2, 12)
    c = _pick_int(rng, 2, 12)

    op = rng.choice(['addition', 'multiplication'])
    if op == 'addition':
        correct = 'Yes'
        explanation = 'Addition is associative: (a + b) + c = a + (b + c).'
        prompt = f"Is ({a} + {b}) + {c} equal to {a} + ({b} + {c})? (Yes/No)"
    else:
        correct = 'Yes'
        explanation = 'Multiplication is associative: (a × b) × c = a × (b × c).'
        prompt = f"Is ({a} × {b}) × {c} equal to {a} × ({b} × {c})? (Yes/No)"

    if qtype == 'mcq':
        options = ['Yes', 'No']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c, 'op': op})


def _gen_distributive(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 2, 12)
    b = _pick_int(rng, 10, 90) if difficulty != 'easy' else _pick_int(rng, 10, 50)
    c = _pick_int(rng, 1, 9)

    if difficulty == 'hard':
        c = _pick_int(rng, 10, 40)

    total = a * (b + c)
    prompt = f"Use the distributive property to calculate: {a} × ({b} + {c})."
    explanation = f"Distribute: {a}×({b}+{c}) = {a}×{b} + {a}×{c} = {a*b} + {a*c} = {total}."

    if qtype == 'scaffold':
        checkpoints: List[Dict[str, Any]] = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute {a} × {b}.",
                'correct_answer': str(a * b),
                'explanation': 'Multiply the first term.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Compute {a} × {c}.",
                'correct_answer': str(a * c),
                'explanation': 'Multiply the second term.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Add the results: {a*b} + {a*c}.",
                'correct_answer': str(total),
                'explanation': 'Add the partial products.',
            },
        ]
        steps = [
            'Rewrite a × (b + c) as a×b + a×c.',
            'Calculate each product.',
            'Add the two results.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(total), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    if qtype == 'mcq':
        options = [str(total), str(a * b + c), str(a * b - a * c), str((b + c) * (a + 1))]
        options = list(dict.fromkeys(options))
        while len(options) < 4:
            options.append(str(total + rng.randint(-20, 20)))
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(total), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=str(total), explanation=explanation, parameters={'a': a, 'b': b, 'c': c})


def _gen_estimation_more_less(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 8, 60)
    b = _pick_int(rng, 60, 140) if difficulty != 'easy' else _pick_int(rng, 50, 120)

    threshold = rng.choice([2000, 3000, 4000])
    exact = a * b
    correct = 'more' if exact > threshold else 'less'

    prompt = f"Without calculating exactly, is {a} × {b} more than {threshold} or less than {threshold}? Answer 'more' or 'less'."
    explanation = f"Estimate: {a}×{b} ≈ {a}×{round(b/10)*10} = {a*round(b/10)*10}. Exact is {exact}, so it is {correct} than {threshold}."

    if qtype == 'mcq':
        options = ['more', 'less']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'threshold': threshold})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'threshold': threshold})


def _gen_rounding_compensating_add(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = _pick_int(rng, 120, 980)
    b = _pick_int(rng, 1200, 9800) if difficulty != 'easy' else _pick_int(rng, 900, 5500)

    base = 100
    a_rounded = int(base * round(a / base))
    b_rounded = int(base * round(b / base))

    rounded_sum = a_rounded + b_rounded
    exact = a + b

    prompt = f"Use rounding off and compensating to calculate: {_format_with_spaces(a)} + {_format_with_spaces(b)}."
    explanation = f"Round to nearest {base}: {a}→{a_rounded}, {b}→{b_rounded}. Rounded sum {rounded_sum}. Compensate to get exact {exact}."

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Round {_format_with_spaces(a)} to the nearest {base}.",
                'correct_answer': str(a_rounded),
                'explanation': 'Use nearest hundred.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Round {_format_with_spaces(b)} to the nearest {base}.",
                'correct_answer': str(b_rounded),
                'explanation': 'Use nearest hundred.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Add the rounded numbers: {a_rounded} + {b_rounded}.",
                'correct_answer': str(rounded_sum),
                'explanation': 'Add the rounded values.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final exact answer (after compensating):',
                'correct_answer': str(exact),
                'explanation': f"Exact sum is {exact}.",
            },
        ]
        steps = [
            'Round each number to an easy base (e.g., nearest 100).',
            'Add the rounded numbers.',
            'Adjust (compensate) for how much you rounded up or down.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(exact), explanation=explanation, parameters={'a': a, 'b': b, 'base': base})

    if qtype == 'mcq':
        options = [str(exact), str(rounded_sum), str(exact + rng.randint(-200, 200)), str(exact + rng.randint(-200, 200))]
        options = list(dict.fromkeys(options))
        while len(options) < 4:
            options.append(str(exact + rng.randint(-300, 300)))
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(exact), explanation=explanation, parameters={'a': a, 'b': b, 'base': base})

    return _make_typed(prompt=prompt, correct_answer=str(exact), explanation=explanation, parameters={'a': a, 'b': b, 'base': base})


def _gen_prime_or_composite(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        n = rng.choice([17, 19, 21, 25, 27, 29, 31, 33])
    elif difficulty == 'medium':
        n = rng.randint(50, 200)
    else:
        n = rng.randint(200, 900)

    factors = _prime_factorization(n)
    is_prime = n >= 2 and len(factors) == 1 and list(factors.values())[0] == 1

    correct = 'prime' if is_prime else 'composite'
    explanation = 'A prime number has exactly two factors: 1 and itself.' if is_prime else f"Composite: {n} has a factorization { _factorization_to_product_string(factors) }."
    prompt = f"Is {n} prime or composite? Answer 'prime' or 'composite'."

    if qtype == 'mcq':
        options = ['prime', 'composite']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n})


def _gen_prime_factorization_powers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    candidates = [72, 84, 96, 108, 120, 144, 180, 210, 252, 360]
    if difficulty == 'hard':
        candidates += [444, 792]

    n = rng.choice(candidates)
    factors = _prime_factorization(n)
    prod = _factorization_to_product_string(factors)
    pow_str = _factorization_to_powers_string(factors)

    prompt = f"Write the prime factorization of {n} using exponents (powers of primes)."
    explanation = f"{n} = {prod} = {pow_str}."

    if qtype == 'scaffold':
        primes = sorted(factors.keys())
        checkpoints = []
        for p in primes:
            checkpoints.append(
                {
                    'id': _make_id('cp'),
                    'kind': 'typed',
                    'prompt': f"How many times does {p} divide into {n}? (its exponent)",
                    'correct_answer': str(int(factors[p])),
                    'explanation': 'Count repeated factors.',
                }
            )
        checkpoints.append(
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer (use ^ for powers, e.g., 2^3 × 3^2):',
                'correct_answer': pow_str,
                'explanation': explanation,
            }
        )
        steps = [
            'Divide by the smallest prime repeatedly (2, 3, 5, 7, ...).',
            'Count how many times each prime divides the number (the exponent).',
            'Write as a product of powers of primes.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=pow_str, explanation=explanation, parameters={'n': n, 'factors': factors})

    if qtype == 'mcq':
        distractors = set()
        while len(distractors) < 3:
            tweak_prime = rng.choice(list(factors.keys()))
            tweaked = dict(factors)
            tweaked[tweak_prime] = max(1, tweaked[tweak_prime] + rng.choice([-1, 1]))
            distractors.add(_factorization_to_powers_string(tweaked))
        options = [pow_str, *sorted(distractors)]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=pow_str, explanation=explanation, parameters={'n': n})

    return _make_typed(prompt=prompt, correct_answer=pow_str, explanation=explanation, parameters={'n': n})


def _lcm_hcf_from_factors(a: int, b: int) -> Tuple[int, int]:
    fa = _prime_factorization(a)
    fb = _prime_factorization(b)

    primes = set(fa.keys()) | set(fb.keys())

    hcf = 1
    lcm = 1
    for p in primes:
        ea = fa.get(p, 0)
        eb = fb.get(p, 0)
        hcf *= p ** min(ea, eb)
        lcm *= p ** max(ea, eb)

    return lcm, hcf


def _gen_lcm_hcf(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = rng.choice([12, 18, 24, 30, 32, 36, 40, 48])
    b = rng.choice([16, 20, 24, 28, 36, 42, 45, 60])

    if difficulty == 'hard':
        a = rng.choice([32, 48, 84])
        b = rng.choice([48, 60, 72, 84])

    lcm, hcf = _lcm_hcf_from_factors(a, b)

    prompt = f"Find the LCM and HCF of {a} and {b}. Give your answer as 'LCM = ..., HCF = ...'."
    correct = f"LCM = {lcm}, HCF = {hcf}"
    explanation = f"Use prime factors. LCM uses the highest powers; HCF uses the lowest powers."

    if qtype == 'scaffold':
        fa = _prime_factorization(a)
        fb = _prime_factorization(b)
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Prime factorization of {a} (use × and ^):",
                'correct_answer': _factorization_to_powers_string(fa),
                'explanation': 'Write as powers of primes.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Prime factorization of {b} (use × and ^):",
                'correct_answer': _factorization_to_powers_string(fb),
                'explanation': 'Write as powers of primes.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final: LCM = ?, HCF = ?',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Factor each number into primes.',
            'For HCF take common primes with the smallest exponents.',
            'For LCM take all primes with the largest exponents.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b})

    if qtype == 'mcq':
        options = [
            correct,
            f"LCM = {hcf}, HCF = {lcm}",
            f"LCM = {lcm + rng.randint(1, 10)}, HCF = {hcf}",
            f"LCM = {lcm}, HCF = {max(1, hcf - rng.randint(1, 5))}",
        ]
        options = list(dict.fromkeys(options))
        while len(options) < 4:
            options.append(f"LCM = {lcm + rng.randint(1, 25)}, HCF = {hcf + rng.randint(1, 5)}")
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b})


def generate_grade8_whole_numbers_question(
    *,
    subskill: str = 'whole_numbers',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    supported_subskills = {
        'beads_array_choice',
        'commutative',
        'commutative_or_not',
        'associative',
        'distributive',
        'identity_properties',
        'brackets_conventions',
        'estimation_more_less',
        'estimate_nearest',
        'rounding_compensating',
        'column_addition',
        'subtraction_number_line',
        'subtraction_borrowing',
        'multiplication_in_parts',
        'long_division',
        'multiples_sequence',
        'factors_rectangle_area',
        'prime_or_composite',
        'prime_factorization',
        'common_multiple_statement',
        'lcm_hcf',
        'rate_and_ratio',
    }

    if subskill not in supported_subskills:
        subskill = 'commutative'

    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    if question_type == 'scaffold' and subskill in {
        'beads_array_choice',
        'commutative',
        'commutative_or_not',
        'associative',
        'identity_properties',
        'brackets_conventions',
        'estimation_more_less',
        'estimate_nearest',
        'multiples_sequence',
        'factors_rectangle_area',
        'prime_or_composite',
        'common_multiple_statement',
        'rate_and_ratio',
    }:
        question_type = 'typed'

    if subskill == 'beads_array_choice':
        q = _gen_beads_array_choice(rng, difficulty, 'mcq')
    elif subskill == 'commutative':
        q = _gen_commutative(rng, difficulty, question_type)
    elif subskill == 'commutative_or_not':
        q = _gen_commutative_or_not(rng, difficulty, question_type)
    elif subskill == 'associative':
        q = _gen_associative(rng, difficulty, question_type)
    elif subskill == 'distributive':
        q = _gen_distributive(rng, difficulty, question_type)
    elif subskill == 'identity_properties':
        q = _gen_identity_properties(rng, difficulty, question_type)
    elif subskill == 'brackets_conventions':
        q = _gen_brackets_conventions(rng, difficulty, 'mcq')
    elif subskill == 'estimation_more_less':
        q = _gen_estimation_more_less(rng, difficulty, question_type)
    elif subskill == 'estimate_nearest':
        q = _gen_estimate_nearest_thousand_or_hundred(rng, difficulty, question_type)
    elif subskill == 'rounding_compensating':
        q = _gen_rounding_compensating_add(rng, difficulty, question_type)
    elif subskill == 'column_addition':
        q = _gen_column_addition(rng, difficulty, question_type)
    elif subskill == 'subtraction_number_line':
        q = _gen_subtraction_number_line(rng, difficulty, question_type)
    elif subskill == 'subtraction_borrowing':
        q = _gen_subtraction_borrowing_columns(rng, difficulty, question_type)
    elif subskill == 'multiplication_in_parts':
        q = _gen_multiplication_in_parts(rng, difficulty, question_type)
    elif subskill == 'long_division':
        q = _gen_long_division_chunking(rng, difficulty, question_type)
    elif subskill == 'multiples_sequence':
        q = _gen_multiples_sequence(rng, difficulty, question_type)
    elif subskill == 'factors_rectangle_area':
        q = _gen_factors_rectangle_area(rng, difficulty, question_type)
    elif subskill == 'prime_or_composite':
        q = _gen_prime_or_composite(rng, difficulty, question_type)
    elif subskill == 'prime_factorization':
        q = _gen_prime_factorization_powers(rng, difficulty, question_type)
    elif subskill == 'common_multiple_statement':
        q = _gen_common_multiple_statement(rng, difficulty, question_type)
    elif subskill == 'rate_and_ratio':
        q = _gen_rate_and_ratio_problem(rng, difficulty, question_type)
    else:
        q = _gen_lcm_hcf(rng, difficulty, question_type)

    out = {
        'id': _make_id('g8_whole'),
        'topic': 'Whole Numbers',
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
