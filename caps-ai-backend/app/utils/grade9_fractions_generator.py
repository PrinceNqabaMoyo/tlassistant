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


def _gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def _reduce(n: int, d: int) -> Tuple[int, int]:
    if d == 0:
        raise ValueError('Denominator cannot be zero')
    if d < 0:
        n, d = -n, -d
    g = _gcd(n, d)
    return n // g, d // g


def _fmt_frac(n: int, d: int) -> str:
    n, d = _reduce(n, d)
    if d == 1:
        return str(n)
    return f"{n}/{d}"


def _to_mixed(n: int, d: int) -> str:
    n, d = _reduce(n, d)
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    whole = n_abs // d
    rem = n_abs % d
    if rem == 0:
        return str(sign * whole)
    frac = _fmt_frac(rem, d)
    if whole == 0:
        return f"-{frac}" if sign < 0 else frac
    return f"{sign * whole} {frac}" if sign > 0 else f"-{whole} {frac}".replace('--', '-')


def _pick_den(rng: random.Random, difficulty: str) -> int:
    if difficulty == 'easy':
        return rng.choice([2, 3, 4, 5, 6, 8, 10, 12])
    if difficulty == 'hard':
        return rng.choice([7, 9, 11, 13, 14, 15, 16, 18, 20])
    return rng.choice([4, 5, 6, 8, 9, 10, 12, 15, 18])


def _gen_equivalent_fractions(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    d = _pick_den(rng, difficulty)
    n = rng.randint(1, d - 1)
    k = rng.choice([2, 3, 4, 5] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7])

    a = _fmt_frac(n, d)
    b = _fmt_frac(n * k, d * k)

    prompt = f"Write a fraction equivalent to {a} by multiplying numerator and denominator by {k}."
    correct = b
    explanation = f"Multiply numerator and denominator by the same number: {a} = {n*k}/{d*k}."

    if qtype == 'mcq':
        opts = [
            b,
            _fmt_frac(n * k, d),
            _fmt_frac(n, d * k),
            _fmt_frac(n * (k + 1), d * (k + 1)),
        ]
        options = list(dict.fromkeys(opts))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = [
            'Choose the multiplier k.',
            'Multiply the numerator by k.',
            'Multiply the denominator by k.',
            'Write the new fraction.'
        ]
        checkpoints = [
            {
                'id': 'cp_num',
                'prompt': f"New numerator = {n} × {k} = ?",
                'kind': 'typed',
                'correct_answer': str(n * k),
                'explanation': f"{n} × {k} = {n * k}."
            },
            {
                'id': 'cp_den',
                'prompt': f"New denominator = {d} × {k} = ?",
                'kind': 'typed',
                'correct_answer': str(d * k),
                'explanation': f"{d} × {k} = {d * k}."
            },
            {
                'id': 'cp_frac',
                'prompt': 'Write the equivalent fraction.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': f"So {a} = {correct}."
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_simplify_fractions(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base_d = _pick_den(rng, difficulty)
    base_n = rng.randint(1, base_d - 1)
    mult = rng.choice([2, 3, 4, 5] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8])

    n = base_n * mult
    d = base_d * mult
    given = f"{n}/{d}"
    simp = _fmt_frac(base_n, base_d)

    prompt = f"Convert the fraction {given} to its simplest form."
    correct = simp
    explanation = f"Divide numerator and denominator by the common factor {mult}: {n}/{d} = {base_n}/{base_d} = {simp}."

    if qtype == 'mcq':
        wrong = [
            _fmt_frac(base_n, base_d * 2),
            _fmt_frac(base_n * 2, base_d),
            _fmt_frac(base_n + 1, base_d),
        ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = [
            'Find a common factor of numerator and denominator.',
            'Divide numerator and denominator by the common factor.',
            'Check that the new fraction has no common factors.'
        ]
        checkpoints = [
            {
                'id': 'cp_factor',
                'prompt': 'What common factor can we divide by?',
                'kind': 'typed',
                'correct_answer': str(mult),
                'explanation': f"Both {n} and {d} are divisible by {mult}."
            },
            {
                'id': 'cp_frac',
                'prompt': 'Write the simplest form.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_mixed_to_improper(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    d = _pick_den(rng, difficulty)
    whole = rng.randint(1, 9 if difficulty != 'hard' else 15)
    n = rng.randint(1, d - 1)

    mixed = f"{whole} {n}/{d}"
    improper_n = whole * d + n
    improper = _fmt_frac(improper_n, d)

    prompt = f"Convert the mixed number {mixed} to an improper fraction."
    correct = improper
    explanation = f"Multiply the whole number by the denominator and add the numerator: {whole}×{d}+{n}={improper_n}, so {mixed} = {improper_n}/{d}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            _fmt_frac(whole + n, d),
            _fmt_frac(whole * d - n, d),
            _fmt_frac(whole * d + n, d + 1),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = [
            'Multiply the whole number by the denominator.',
            'Add the numerator.',
            'Keep the denominator the same.'
        ]
        checkpoints = [
            {
                'id': 'cp_mul',
                'prompt': f"{whole} × {d} = ?",
                'kind': 'typed',
                'correct_answer': str(whole * d),
                'explanation': f"{whole} × {d} = {whole * d}."
            },
            {
                'id': 'cp_add',
                'prompt': f"Now add the numerator: {whole*d} + {n} = ?",
                'kind': 'typed',
                'correct_answer': str(improper_n),
                'explanation': f"{whole*d} + {n} = {improper_n}."
            },
            {
                'id': 'cp_frac',
                'prompt': 'Write the improper fraction.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_improper_to_mixed(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    d = _pick_den(rng, difficulty)
    whole = rng.randint(1, 9 if difficulty != 'hard' else 15)
    n = rng.randint(1, d - 1)
    improper_n = whole * d + n

    improper = f"{improper_n}/{d}"
    mixed = _to_mixed(improper_n, d)

    prompt = f"Convert the improper fraction {improper} to a mixed number."
    correct = mixed
    explanation = f"Divide {improper_n} by {d}: quotient {whole}, remainder {n}. So {improper} = {whole} {n}/{d}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            f"{whole + 1} {n}/{d}",
            f"{whole} {d - n}/{d}",
            f"{whole} {n}/{d + 1}",
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = [
            'Divide the numerator by the denominator.',
            'The quotient is the whole number part.',
            'The remainder is the new numerator, and the denominator stays the same.'
        ]
        checkpoints = [
            {
                'id': 'cp_whole',
                'prompt': f"Whole number part: {improper_n} ÷ {d} = ? (quotient)",
                'kind': 'typed',
                'correct_answer': str(whole),
                'explanation': f"{improper_n} ÷ {d} gives quotient {whole}."
            },
            {
                'id': 'cp_rem',
                'prompt': f"Remainder: {improper_n} − ({whole}×{d}) = ?",
                'kind': 'typed',
                'correct_answer': str(n),
                'explanation': f"{improper_n} − {whole*d} = {n}."
            },
            {
                'id': 'cp_mixed',
                'prompt': 'Write the mixed number.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_add_sub_fractions(rng: random.Random, difficulty: str, qtype: str, *, like: bool) -> Dict[str, Any]:
    if like:
        d = _pick_den(rng, difficulty)
        a = rng.randint(1, d - 1)
        b = rng.randint(1, d - 1)
        op = rng.choice(['+', '-'])
        prompt = f"Calculate: {a}/{d} {op} {b}/{d}"
        if op == '+':
            n, dd = a + b, d
        else:
            n, dd = a - b, d
        correct = _fmt_frac(n, dd)
        explanation = f"Same denominator: keep {d} and {op} the numerators. Simplify if needed: {correct}."
    else:
        d1 = _pick_den(rng, difficulty)
        d2 = _pick_den(rng, difficulty)
        while d2 == d1:
            d2 = _pick_den(rng, difficulty)
        a = rng.randint(1, d1 - 1)
        b = rng.randint(1, d2 - 1)
        op = rng.choice(['+', '-'])
        prompt = f"Calculate: {a}/{d1} {op} {b}/{d2}"
        lcm = (d1 * d2) // _gcd(d1, d2)
        m1 = lcm // d1
        m2 = lcm // d2
        nn = a * m1 + (b * m2 if op == '+' else -b * m2)
        correct = _fmt_frac(nn, lcm)
        explanation = f"Common denominator {lcm}: {a}/{d1} = {a*m1}/{lcm} and {b}/{d2} = {b*m2}/{lcm}. Then combine and simplify: {correct}."

    if qtype == 'mcq':
        wrong = [
            _fmt_frac(abs(a + b), d if like else (d1 + d2)),
            _fmt_frac(abs(a - b), d if like else (d1 + d2)),
            _fmt_frac(abs(a + b), d1 if not like else (d + 1)),
        ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Find a common denominator.', 'Convert each fraction.', 'Add/subtract numerators.', 'Simplify.']
        checkpoints = [
            {
                'id': 'cp_common',
                'prompt': 'What common denominator will you use?',
                'kind': 'typed',
                'correct_answer': str(d if like else ((d1 * d2) // _gcd(d1, d2))),
                'explanation': 'Use the same denominator for both fractions.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the final simplified answer.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_fraction_of_amount(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    denom = _pick_den(rng, difficulty)
    num = rng.randint(1, min(denom - 1, 6 if difficulty == 'easy' else denom - 1))

    base = rng.choice([50, 60, 80, 100, 120, 150, 200, 240, 300])
    amount = base * denom

    value = (amount * num) // denom
    prompt = f"Calculate {num}/{denom} of R{amount}."
    correct = str(value)
    explanation = f"Find 1/{denom} of R{amount} then multiply by {num}: R{amount} ÷ {denom} = R{amount//denom}; R{amount//denom} × {num} = R{value}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            str(value + base),
            str(max(0, value - base)),
            str((amount * (num + 1)) // denom),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Divide the amount by the denominator.', 'Multiply the result by the numerator.']
        checkpoints = [
            {
                'id': 'cp_unit',
                'prompt': f"Find 1/{denom} of R{amount}: {amount} ÷ {denom} = ?",
                'kind': 'typed',
                'correct_answer': str(amount // denom),
                'explanation': f"{amount} ÷ {denom} = {amount // denom}."
            },
            {
                'id': 'cp_final',
                'prompt': f"Now multiply by {num}: {amount//denom} × {num} = ?",
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def generate_grade9_fractions_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    rng = random.Random(seed if seed is not None else int(time.time() * 1000))

    subskill = str(subskill or 'mixed').strip().lower()

    generators = {
        'equivalent_fractions': _gen_equivalent_fractions,
        'simplify_fractions': _gen_simplify_fractions,
        'mixed_to_improper': _gen_mixed_to_improper,
        'improper_to_mixed': _gen_improper_to_mixed,
        'add_sub_like_denominators': lambda r, d, qt: _gen_add_sub_fractions(r, d, qt, like=True),
        'add_sub_unlike_denominators': lambda r, d, qt: _gen_add_sub_fractions(r, d, qt, like=False),
        'fraction_of_amount': _gen_fraction_of_amount,
    }

    if subskill == 'mixed':
        keys = list(generators.keys())
        subskill = rng.choice(keys)

    if subskill not in generators:
        subskill = 'equivalent_fractions'

    gen = generators[subskill]
    q = gen(rng, difficulty, question_type)

    q_full = {
        'id': _make_id('g9_frac'),
        'topic': 'grade9_fractions',
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(q_full)
    return q_full


def generate_grade9_fractions_questions(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if not isinstance(count, int) or count < 1:
        count = 1
    if count > 20:
        count = 20

    out: List[Dict[str, Any]] = []
    for i in range(count):
        q_seed = None
        if seed is not None:
            try:
                q_seed = int(seed) + i
            except Exception:
                q_seed = None

        out.append(
            generate_grade9_fractions_question(
                subskill=subskill,
                difficulty=difficulty,
                question_type=question_type,
                seed=q_seed,
            )
        )

    return out
