

import math
import random
import time
from typing import Any, Dict, List, Optional, Tuple


def _make_id(prefix: str, rng: random.Random) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{rng.randint(1000, 9999)}"


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


def _make_scaffold(
    *,
    prompt: str,
    steps: List[str],
    checkpoints: List[Dict[str, Any]],
    final_answer: str,
    explanation: str,
    **extra,
) -> Dict[str, Any]:
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


def _make_unique_options(rng: random.Random, correct: str, candidates: List[str], target: int = 4) -> List[str]:
    opts: List[str] = [str(correct)]
    for c in candidates:
        if len(opts) >= target:
            break
        c = str(c)
        if c not in opts:
            opts.append(c)

    while len(opts) < target:
        opts.append(str(correct))
        opts = list(dict.fromkeys(opts))

    opts = opts[:target]
    rng.shuffle(opts)
    return opts


def _choose_nonzero(rng: random.Random, xs: List[int]) -> int:
    v = int(rng.choice(xs))
    while v == 0:
        v = int(rng.choice(xs))
    return v


def _arith_terms(a1: int, d: int, n: int) -> List[int]:
    return [a1 + (k - 1) * d for k in range(1, n + 1)]


def _fmt_rational(num: int, den: int) -> str:
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num, den = -num, -den
    if den == 1:
        return str(num)
    return f"{num}/{den}"


def _geom_terms(a1: int, r_num: int, r_den: int, n: int) -> List[Tuple[int, int]]:
    terms: List[Tuple[int, int]] = []
    num, den = a1, 1
    for _ in range(n):
        g = math.gcd(abs(num), abs(den))
        num //= g
        den //= g
        if den < 0:
            num, den = -num, -den
        terms.append((num, den))
        num *= r_num
        den *= r_den
    return terms


def _gen_arithmetic_next_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = rng.randint(-10, 20)
        d = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
    elif difficulty == 'medium':
        a1 = rng.randint(-25, 35)
        d = _choose_nonzero(rng, [-9, -8, -7, -6, 6, 7, 8, 9])
    else:
        a1 = rng.randint(-50, 60)
        d = _choose_nonzero(rng, [-12, -10, -9, -8, 8, 9, 10, 12])

    shown = _arith_terms(a1, d, 5)
    next3 = _arith_terms(a1, d, 8)[5:]
    correct = '; '.join(str(x) for x in next3)
    prompt = f"Arithmetic sequence: {'; '.join(str(x) for x in shown)}; ... Write the next 3 terms (semicolon-separated)."
    explanation = 'Add the common difference d each time.'

    if qtype == 'mcq':
        candidates = [
            '; '.join(str(x + 1) for x in next3),
            '; '.join(str(x - 1) for x in next3),
            '; '.join(str(a1 + (k - 1) * (d + 1)) for k in range(6, 9)),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Find the common difference d = T2 − T1:',
                'correct_answer': str(d),
                'explanation': 'Subtract consecutive terms.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Next 3 terms (semicolon-separated):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find d.', 'Add d repeatedly.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d})


def _gen_geometric_next_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = _choose_nonzero(rng, [1, 2, 3, 4, 5, 6, 8, 10])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (1, 2)])
        if rng.random() < 0.2:
            r_num = -r_num
        shown_n = 5
    elif difficulty == 'medium':
        a1 = _choose_nonzero(rng, [-12, -10, -8, -6, 6, 8, 10, 12])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (4, 1), (1, 2), (3, 2)])
        if rng.random() < 0.3:
            r_num = -r_num
        shown_n = 5
    else:
        a1 = _choose_nonzero(rng, [-15, -12, -10, -8, 8, 10, 12, 15])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (5, 1), (1, 2), (3, 2)])
        if rng.random() < 0.35:
            r_num = -r_num
        shown_n = 6

    terms = _geom_terms(a1, r_num, r_den, shown_n + 3)
    shown = terms[:shown_n]
    next3 = terms[shown_n:shown_n + 3]
    shown_str = '; '.join(_fmt_rational(n, d) for n, d in shown)
    correct = '; '.join(_fmt_rational(n, d) for n, d in next3)
    prompt = f"Geometric sequence: {shown_str}; ... Write the next 3 terms (semicolon-separated)."
    explanation = 'Multiply by the constant ratio r each time.'

    if qtype == 'mcq':
        candidates = [
            '; '.join(_fmt_rational(n * r_num, d * r_den) for n, d in next3),
            '; '.join(_fmt_rational(n, d) for n, d in terms[shown_n + 1:shown_n + 4]),
            '; '.join(_fmt_rational(-n, d) for n, d in next3),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Find the constant ratio r = T2 / T1 (as a fraction):',
                'correct_answer': _fmt_rational(r_num, r_den),
                'explanation': 'Divide consecutive terms to find r.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Next 3 terms (semicolon-separated):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find r.', 'Multiply by r repeatedly.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den})


def _arith_sum(a1: int, d: int, n: int) -> int:
    # S_n = n/2 (2a + (n-1)d)
    return n * (2 * a1 + (n - 1) * d) // 2


def _gen_arithmetic_series_sum(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = rng.randint(-10, 20)
        d = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
        n = rng.randint(5, 12)
    elif difficulty == 'medium':
        a1 = rng.randint(-25, 35)
        d = _choose_nonzero(rng, [-9, -8, -7, -6, 6, 7, 8, 9])
        n = rng.randint(8, 20)
    else:
        a1 = rng.randint(-50, 60)
        d = _choose_nonzero(rng, [-12, -10, -9, -8, 8, 9, 10, 12])
        n = rng.randint(10, 30)

    sn = _arith_sum(a1, d, n)
    prompt = f"Arithmetic sequence has first term a = {a1}, common difference d = {d}. Calculate S_{n} (sum of first {n} terms)."
    correct = str(sn)
    explanation = 'Use S_n = n/2 [2a + (n − 1)d].'

    if qtype == 'mcq':
        candidates = [str(sn + d), str(sn - d), str(_arith_sum(a1, d, max(1, n - 1)))]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'n': n})

    if qtype == 'scaffold':
        tn = a1 + (n - 1) * d
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Find T_{n} = a + (n − 1)d:",
                'correct_answer': str(tn),
                'explanation': 'Compute the nth term first.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Use S_n = n/2 (a + T_n) to find S_{n}:",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find T_n.', 'Use S_n = n/2 (a + T_n) or S_n = n/2 [2a + (n−1)d].']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'n': n})


def _gen_arithmetic_series_solve_for_n(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Choose (a, d, n) then compute S_n to ensure integer solution.
    if difficulty == 'easy':
        a1 = rng.randint(-5, 15)
        d = _choose_nonzero(rng, [-5, -4, -3, 3, 4, 5])
        n = rng.randint(6, 15)
    elif difficulty == 'medium':
        a1 = rng.randint(-20, 25)
        d = _choose_nonzero(rng, [-8, -7, -6, 6, 7, 8])
        n = rng.randint(8, 25)
    else:
        a1 = rng.randint(-30, 40)
        d = _choose_nonzero(rng, [-12, -10, -9, 9, 10, 12])
        n = rng.randint(10, 40)

    sn = _arith_sum(a1, d, n)
    prompt = f"For an arithmetic series with first term a = {a1} and common difference d = {d}, the sum S_n = {sn}. Find n."
    correct = str(n)
    explanation = 'Use S_n = n/2 [2a + (n − 1)d] and solve the resulting quadratic for the positive integer n.'

    if qtype == 'mcq':
        candidates = [str(n - 1), str(n + 1), str(n + 2)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'sn': sn})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the sum formula used:',
                'correct_answer': 'S_n = n/2 [2a + (n − 1)d]',
                'explanation': 'This is the arithmetic series sum formula.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Solve for n (positive integer):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Substitute into S_n = n/2 [2a + (n−1)d].', 'Solve for the positive integer n.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'sn': sn})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'd': d, 'sn': sn})


def _geom_sum(a1: int, r_num: int, r_den: int, n: int) -> Tuple[int, int]:
    # S_n = a(1-r^n)/(1-r) for r != 1, all rationals.
    # Represent r as r_num/r_den.
    if r_num == r_den:
        return (a1 * n, 1)

    # Compute r^n as (r_num^n)/(r_den^n)
    rn_num = pow(r_num, n)
    rn_den = pow(r_den, n)

    # a * (1 - rn) / (1 - r)
    # = a * ((rn_den - rn_num)/rn_den) / ((r_den - r_num)/r_den)
    num = a1 * (rn_den - rn_num) * r_den
    den = rn_den * (r_den - r_num)
    g = math.gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num, den = -num, -den
    return num, den


def _gen_geometric_series_sum(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        a1 = _choose_nonzero(rng, [1, 2, 3, 4, 5, 6])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (1, 2)])
        n = rng.randint(4, 8)
    elif difficulty == 'medium':
        a1 = _choose_nonzero(rng, [-8, -6, -4, 4, 6, 8])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (4, 1), (1, 2), (3, 2)])
        n = rng.randint(5, 10)
    else:
        a1 = _choose_nonzero(rng, [-10, -8, -6, 6, 8, 10])
        r_num, r_den = rng.choice([(2, 1), (3, 1), (5, 1), (1, 2), (3, 2)])
        n = rng.randint(6, 12)

    if rng.random() < 0.25:
        r_num = -r_num

    s_num, s_den = _geom_sum(a1, r_num, r_den, n)
    correct = _fmt_rational(s_num, s_den)
    r_str = _fmt_rational(r_num, r_den)
    prompt = f"Geometric series with first term a = {a1}, ratio r = {r_str}. Calculate S_{n}."
    explanation = 'Use S_n = a(1 − r^n)/(1 − r) (for r ≠ 1).'

    if qtype == 'mcq':
        candidates = [
            _fmt_rational(s_num + 1, s_den),
            _fmt_rational(s_num - 1, s_den),
            _fmt_rational(s_num, s_den + 1),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den, 'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the formula used:',
                'correct_answer': 'S_n = a(1 − r^n)/(1 − r)',
                'explanation': 'Geometric series sum formula (r ≠ 1).',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Compute S_{n}:",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Use S_n = a(1 − r^n)/(1 − r).', 'Substitute values and simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a1': a1, 'r_num': r_num, 'r_den': r_den, 'n': n})


def _gen_sigma_expand_evaluate(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Keep scope simple: sums of (c*k) and (c*2^(k-1)) style.
    if difficulty == 'easy':
        n = rng.randint(4, 7)
        kind = rng.choice(['linear', 'powers2'])
    elif difficulty == 'medium':
        n = rng.randint(5, 9)
        kind = rng.choice(['linear', 'powers2'])
    else:
        n = rng.randint(6, 10)
        kind = rng.choice(['linear', 'powers2'])

    start = 1
    if kind == 'linear':
        c = _choose_nonzero(rng, [-6, -5, -4, -3, 3, 4, 5, 6])
        # sum_{k=1..n} c*k = c*n(n+1)/2
        value = c * n * (n + 1) // 2
        prompt = f"Evaluate the sigma: Σ(k={start} to {n}) [{c}k]."
        explanation = 'This is an arithmetic series: c(1 + 2 + ... + n) = c·n(n+1)/2.'
    else:
        # sum_{k=1..n} a*2^(k-1) = a(2^n - 1)
        a = _choose_nonzero(rng, [-8, -6, -4, 4, 6, 8])
        value = a * (2 ** n - 1)
        prompt = f"Evaluate the sigma: Σ(k={start} to {n}) [{a}·2^(k-1)]."
        explanation = 'This is a geometric series with first term a and ratio 2: sum = a(2^n − 1).'

    correct = str(value)

    if qtype == 'mcq':
        candidates = [str(value + 1), str(value - 1), str(value + n)]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'n': n, 'kind': kind})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Expand the first few terms (write 3 terms, separated by commas):',
                'correct_answer': 'see expansion',
                'explanation': 'Expand by substituting k = 1, 2, 3.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final value:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Expand using k values.', 'Recognise arithmetic/geometric series.', 'Use the relevant sum formula.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'n': n, 'kind': kind})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n, 'kind': kind})


_SUBSKILLS = {
    'arithmetic_next_terms': _gen_arithmetic_next_terms,
    'geometric_next_terms': _gen_geometric_next_terms,
    'arithmetic_series_sum': _gen_arithmetic_series_sum,
    'arithmetic_series_solve_for_n': _gen_arithmetic_series_solve_for_n,
    'geometric_series_sum': _gen_geometric_series_sum,
    'sigma_evaluate': _gen_sigma_expand_evaluate,
}


def generate_questions(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'mixed',
    count: int = 5,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold', 'mixed'}:
        question_type = 'mixed'

    if count < 1:
        count = 1
    if count > 30:
        count = 30

    rng = random.Random(seed if seed is not None else int(time.time()))

    if subskill == 'mixed' or not subskill:
        subskills = list(_SUBSKILLS.keys())
    else:
        subskills = [subskill] if subskill in _SUBSKILLS else list(_SUBSKILLS.keys())

    questions: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen_subskill = rng.choice(subskills)
        gen = _SUBSKILLS[chosen_subskill]

        if question_type == 'mixed':
            chosen_qtype = rng.choice(['typed', 'mcq', 'scaffold'])
        else:
            chosen_qtype = question_type

        q = gen(rng, difficulty, chosen_qtype)
        q = {
            'id': _make_id('g12_patseqseries', rng),
            'topic': 'Patterns, sequences, series',
            'subskill': chosen_subskill,
            'difficulty': difficulty,
            **q,
        }
        _validate_question(q)
        questions.append(q)

    return questions
