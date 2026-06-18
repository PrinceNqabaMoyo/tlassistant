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
    required = {
        'id',
        'topic',
        'subskill',
        'difficulty',
        'question_type',
        'question',
        'correct_answer',
        'explanation',
    }
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


def _rand_int(rng: random.Random, lo: int, hi: int) -> int:
    return int(rng.randint(lo, hi))


def _rand_nonzero_int(rng: random.Random, lo: int, hi: int) -> int:
    x = _rand_int(rng, lo, hi)
    while x == 0:
        x = _rand_int(rng, lo, hi)
    return x


def _gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def _simplify_fraction(n: int, d: int) -> Tuple[int, int]:
    if d == 0:
        raise ValueError('Denominator cannot be 0')
    if d < 0:
        n, d = -n, -d
    g = _gcd(abs(n), abs(d))
    return (n // g, d // g)


def _fmt_fraction(n: int, d: int) -> str:
    n, d = _simplify_fraction(n, d)
    if d == 1:
        return str(n)
    return f"{n}/{d}"


def _fmt_signed_int(n: int) -> str:
    return f"+ {n}" if n >= 0 else f"- {abs(n)}"


def _fmt_point(x: Any, y: Any) -> str:
    return f"({x}; {y})"


def _distance_squared(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    return dx * dx + dy * dy


def _gen_distance_between_points(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
        q = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
    elif difficulty == 'medium':
        p = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
    else:
        p = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))
        q = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))

    while p == q:
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))

    dsq = _distance_squared(p, q)
    prompt = f"Determine the distance between P{_fmt_point(p[0], p[1])} and Q{_fmt_point(q[0], q[1])}. Give your answer in simplest surd form (e.g. √8 or 3√2 or 5)."

    # Keep exact surd: sqrt(dsq) simplified
    root = int(math.isqrt(dsq))
    if root * root == dsq:
        correct = str(root)
        explanation = 'Use the distance formula. Here the square root is a perfect square.'
    else:
        # simplify sqrt(dsq) = a*sqrt(b)
        a = 1
        b = dsq
        # factor out squares
        for k in range(2, int(math.isqrt(b)) + 1):
            kk = k * k
            if b % kk == 0:
                a = k
        while a > 1 and (dsq % (a * a) != 0):
            a -= 1
        if a > 1 and dsq % (a * a) == 0:
            b = dsq // (a * a)
        else:
            a = 1
            b = dsq

        correct = f"{a}√{b}" if a != 1 else f"√{b}"
        explanation = 'Use the distance formula AB = √((x₂−x₁)² + (y₂−y₁)²) and simplify the surd.'

    if qtype == 'mcq':
        candidates = [
            str(int(correct) + 1) if correct.isdigit() else f"√{dsq + 1}",
            str(int(correct) - 1) if correct.isdigit() and int(correct) > 0 else f"√{max(1, dsq - 1)}",
            f"√{dsq}",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q, 'dsq': dsq})

    if qtype == 'scaffold':
        dx = q[0] - p[0]
        dy = q[1] - p[1]
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute Δx = x₂ − x₁:',
                'correct_answer': str(dx),
                'explanation': 'Subtract x-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute Δy = y₂ − y₁:',
                'correct_answer': str(dy),
                'explanation': 'Subtract y-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute (Δx)² + (Δy)²:',
                'correct_answer': str(dsq),
                'explanation': 'Square and add.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Distance in simplest surd form:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find Δx and Δy.', 'Compute (Δx)² + (Δy)².', 'Take the square root and simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q, 'dsq': dsq})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q, 'dsq': dsq})


def _gen_midpoint(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
        q = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
    elif difficulty == 'medium':
        p = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
    else:
        p = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))
        q = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))

    mx_num = p[0] + q[0]
    my_num = p[1] + q[1]
    mx = _fmt_fraction(mx_num, 2)
    my = _fmt_fraction(my_num, 2)

    prompt = f"Calculate the midpoint of the line segment joining A{_fmt_point(p[0], p[1])} and B{_fmt_point(q[0], q[1])}. Give your answer as (x; y)."
    correct = f"({_fmt_fraction(mx_num, 2)}; {_fmt_fraction(my_num, 2)})"
    explanation = 'Use midpoint formula M = ((x₁+x₂)/2; (y₁+y₂)/2).'

    if qtype == 'mcq':
        candidates = [
            f"({_fmt_fraction(mx_num + 1, 2)}; {_fmt_fraction(my_num, 2)})",
            f"({_fmt_fraction(mx_num, 2)}; {_fmt_fraction(my_num + 1, 2)})",
            f"({_fmt_fraction(p[0] - q[0], 2)}; {_fmt_fraction(p[1] - q[1], 2)})",
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute (x₁ + x₂):',
                'correct_answer': str(mx_num),
                'explanation': 'Add x-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute (y₁ + y₂):',
                'correct_answer': str(my_num),
                'explanation': 'Add y-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Midpoint M(x; y):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Add the x-coordinates and divide by 2.', 'Add the y-coordinates and divide by 2.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})


def _gen_gradient_two_points(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
        q = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
    elif difficulty == 'medium':
        p = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
    else:
        p = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))
        q = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))

    while p == q or (q[0] - p[0]) == 0:
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))

    dy = q[1] - p[1]
    dx = q[0] - p[0]
    n, d = _simplify_fraction(dy, dx)
    correct = _fmt_fraction(n, d)

    prompt = f"Determine the gradient of the line through A{_fmt_point(p[0], p[1])} and B{_fmt_point(q[0], q[1])}."
    explanation = 'Gradient m = (y₂ − y₁)/(x₂ − x₁).'

    if qtype == 'mcq':
        candidates = [
            _fmt_fraction(n + 1, d),
            _fmt_fraction(n, d + 1),
            _fmt_fraction(-n, d),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute Δy = y₂ − y₁:',
                'correct_answer': str(dy),
                'explanation': 'Subtract y-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute Δx = x₂ − x₁:',
                'correct_answer': str(dx),
                'explanation': 'Subtract x-coordinates.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Gradient m in simplest form:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find Δy and Δx.', 'Compute m = Δy/Δx and simplify.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'A': p, 'B': q})


def _line_from_point_slope(m_num: int, m_den: int, x1: int, y1: int) -> Tuple[int, int, int]:
    # Return standard form: Ax + By + C = 0 with integer coefficients, gcd simplified.
    m_num, m_den = _simplify_fraction(m_num, m_den)
    # y - y1 = (m_num/m_den)(x - x1)
    # m_den*y - m_den*y1 = m_num*x - m_num*x1
    # m_num*x - m_den*y + (m_den*y1 - m_num*x1) = 0
    A = m_num
    B = -m_den
    C = m_den * y1 - m_num * x1

    g = _gcd(_gcd(abs(A), abs(B)), abs(C))
    if g != 0:
        A //= g
        B //= g
        C //= g
    if A < 0:
        A, B, C = -A, -B, -C
    return A, B, C


def _fmt_standard_line(A: int, B: int, C: int) -> str:
    # Ax + By + C = 0
    parts: List[str] = []
    parts.append(f"{A}x" if A != 1 else 'x')

    if B != 0:
        sign = '+' if B > 0 else '-'
        b_abs = abs(B)
        parts.append(f" {sign} {b_abs}y" if b_abs != 1 else f" {sign} y")

    if C != 0:
        sign = '+' if C > 0 else '-'
        parts.append(f" {sign} {abs(C)}")

    return ''.join(parts) + ' = 0'


def _gen_equation_line_two_points(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
        q = (_rand_int(rng, -6, 6), _rand_int(rng, -6, 6))
    elif difficulty == 'medium':
        p = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))
    else:
        p = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))
        q = (_rand_int(rng, -15, 15), _rand_int(rng, -15, 15))

    while p == q or (q[0] - p[0]) == 0:
        q = (_rand_int(rng, -10, 10), _rand_int(rng, -10, 10))

    dy = q[1] - p[1]
    dx = q[0] - p[0]
    A, B, C = _line_from_point_slope(dy, dx, p[0], p[1])
    correct = _fmt_standard_line(A, B, C)

    prompt = f"Determine the equation of the line passing through P{_fmt_point(p[0], p[1])} and Q{_fmt_point(q[0], q[1])}. Give your answer in standard form Ax + By + C = 0."
    explanation = 'Find the gradient m = (y₂−y₁)/(x₂−x₁), then use point-slope form and rearrange to standard form.'

    if qtype == 'mcq':
        candidates = [
            _fmt_standard_line(A, B, C + 1),
            _fmt_standard_line(A, B + 1, C),
            _fmt_standard_line(A + 1, B, C),
        ]
        options = _make_unique_options(rng, correct, candidates)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q})

    if qtype == 'scaffold':
        m = _fmt_fraction(*_simplify_fraction(dy, dx))
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Compute the gradient m:',
                'correct_answer': m,
                'explanation': 'm = (y₂−y₁)/(x₂−x₁).',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Write the equation in standard form Ax + By + C = 0:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find the gradient.', 'Use point-slope form.', 'Rearrange to Ax + By + C = 0.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'P': p, 'Q': q})


def _gen_parallel_or_perpendicular(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    mode = rng.choice(['parallel', 'perpendicular'])

    # Generate a base line in standard form by point-slope, then a second line
    if difficulty == 'easy':
        m_num = _rand_nonzero_int(rng, -4, 4)
        m_den = _rand_nonzero_int(rng, 1, 5)
        x1 = _rand_int(rng, -5, 5)
        y1 = _rand_int(rng, -5, 5)
    elif difficulty == 'medium':
        m_num = _rand_nonzero_int(rng, -7, 7)
        m_den = _rand_nonzero_int(rng, 1, 8)
        x1 = _rand_int(rng, -8, 8)
        y1 = _rand_int(rng, -8, 8)
    else:
        m_num = _rand_nonzero_int(rng, -10, 10)
        m_den = _rand_nonzero_int(rng, 1, 12)
        x1 = _rand_int(rng, -12, 12)
        y1 = _rand_int(rng, -12, 12)

    A, B, C = _line_from_point_slope(m_num, m_den, x1, y1)
    base = _fmt_standard_line(A, B, C)

    # A line in y = mx + c form for display
    m = _fmt_fraction(*_simplify_fraction(m_num, m_den))

    if mode == 'parallel':
        correct = 'yes'
        explanation = 'Parallel lines have equal gradients.'
        other_m = m
        label = 'parallel'
    else:
        correct = 'yes'
        explanation = 'Perpendicular lines satisfy m₁ × m₂ = −1.'
        # perpendicular slope = -den/num
        pm_num, pm_den = _simplify_fraction(-m_den, m_num)
        other_m = _fmt_fraction(pm_num, pm_den)
        label = 'perpendicular'

    prompt = f"Is the line {base} {label} to a line with gradient m = {other_m}? Answer yes or no."

    if qtype == 'mcq':
        options = ['yes', 'no']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm_other': other_m, 'relation': mode})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'What is the gradient of the line in standard form? (Give as a fraction)',
                'correct_answer': m,
                'explanation': 'Rewrite to y = mx + c or use m = -A/B if Ax + By + C = 0.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Are the lines {label}? (yes/no)",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Find gradient of the given line.', f'Apply the rule for {label} lines.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'base': base, 'm_other': other_m, 'relation': mode})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm_other': other_m, 'relation': mode})


_SUBSKILLS = {
    'distance_between_points': _gen_distance_between_points,
    'midpoint': _gen_midpoint,
    'gradient_two_points': _gen_gradient_two_points,
    'equation_line_two_points': _gen_equation_line_two_points,
    'parallel_or_perpendicular': _gen_parallel_or_perpendicular,
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
            'id': _make_id('g11_analgeo', rng),
            'topic': 'Analytical Geometry',
            'subskill': chosen_subskill,
            'difficulty': difficulty,
            **q,
        }
        _validate_question(q)
        questions.append(q)

    return questions
