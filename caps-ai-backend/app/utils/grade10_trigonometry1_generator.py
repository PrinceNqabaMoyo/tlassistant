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


def _choice(rng: random.Random, xs: List[Any]) -> Any:
    return xs[int(rng.randrange(0, len(xs)))]


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


def _round_str(x: float, places: int) -> str:
    return f"{x:.{places}f}"


def _deg_to_rad(d: float) -> float:
    return d * math.pi / 180.0


def _rad_to_deg(r: float) -> float:
    return r * 180.0 / math.pi


def _calc_button_sequence(expr: str) -> str:
    # Keep it simple and consistent; render as a single line.
    # Example: "Press \"sin\" \"3\" \"5\" \"=\""
    return f"Press {expr}"


def _special_angle_value(func: str, angle: int) -> str:
    # exact values for 30, 45, 60
    if func == 'sin':
        if angle == 30:
            return '1/2'
        if angle == 45:
            return '1/√2'
        if angle == 60:
            return '√3/2'
    if func == 'cos':
        if angle == 30:
            return '√3/2'
        if angle == 45:
            return '1/√2'
        if angle == 60:
            return '1/2'
    if func == 'tan':
        if angle == 30:
            return '1/√3'
        if angle == 45:
            return '1'
        if angle == 60:
            return '√3'
    raise ValueError('Unsupported special angle')


def _gen_identify_sides(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Text-only: declare which side is hypotenuse/opposite/adjacent w.r.t theta.
    # Triangle description: right angle at B, theta at A. So:
    # hypotenuse = AC, opposite = BC, adjacent = AB
    labels = _choice(rng, [
        ('AB', 'adjacent'),
        ('BC', 'opposite'),
        ('AC', 'hypotenuse'),
    ])
    side, role = labels
    prompt = (
        "In right-angled triangle ABC, ∠B = 90° and θ = ∠A. "
        f"Which side is {side} relative to θ? (hypotenuse/opposite/adjacent)"
    )
    correct = role
    explanation = "Hypotenuse is opposite 90°. Opposite is across from θ. Adjacent touches θ (but is not the hypotenuse)."

    if qtype == 'mcq':
        options = ['hypotenuse', 'opposite', 'adjacent']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'First, which side is opposite the 90° angle?',
                'correct_answer': 'AC',
                'explanation': 'The hypotenuse is always opposite the right angle.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Now classify {side} relative to θ:",
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Find the hypotenuse (opposite 90°).',
            'Find the opposite side (across from θ).',
            'The remaining non-hypotenuse side is adjacent.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_special_angles_exact(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    func = _choice(rng, ['sin', 'cos', 'tan'])
    angle = int(_choice(rng, [30, 45, 60]))
    correct = _special_angle_value(func, angle)
    prompt = f"Calculate exactly (no calculator): {func} {angle}°"
    explanation = "Use the special angles table (30°, 45°, 60°)."

    if qtype == 'mcq':
        candidates = ['1/2', '1/√2', '√3/2', '√3', '1/√3', '1']
        options = _make_unique_options(rng, correct, [c for c in candidates if c != correct], target=4)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'State the angle type (special angle / not a special angle):',
                'correct_answer': 'special angle',
                'explanation': '30°, 45°, and 60° are special angles with exact trig values.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Exact value:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Recognize the angle (30°, 45°, 60°).',
            'Use the special angles table to read off the exact value.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_evaluate_trig_decimal(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    func = _choice(rng, ['sin', 'cos', 'tan'])
    angle = int(_choice(rng, [12, 20, 23, 26, 27, 34, 35, 38, 40, 48, 49, 55, 65, 72, 74, 81]))
    power = 1
    mult_num = 1
    mult_den = 1

    if difficulty != 'easy' and bool(_choice(rng, [True, False])):
        power = 2

    if difficulty == 'hard' and bool(_choice(rng, [True, False])):
        mult_num = int(_choice(rng, [2, 3, 4, 5]))
        mult_den = int(_choice(rng, [1, 2, 3, 4, 5, 6]))

    base_val = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}[func](_deg_to_rad(angle))
    val = (base_val ** power) * (mult_num / mult_den)

    # keep consistent with doc: 2 d.p.
    correct = _round_str(val, 2)

    expr = f"{func} {angle}°"
    if power == 2:
        expr = f"({func} {angle}°)^2"
    if mult_num != 1 or mult_den != 1:
        if mult_den == 1:
            expr = f"{mult_num} {expr}"
        else:
            expr = f"({mult_num}/{mult_den}) {expr}"

    prompt = f"Use your calculator (degrees mode). Calculate (to 2 d.p.): {expr}"

    steps = [
        'Make sure the calculator is in degrees mode.',
        f"Enter the trig function: {func} and the angle: {angle}.",
    ]
    if power == 2:
        steps.append('Square the result (x²).')
    if mult_num != 1 or mult_den != 1:
        steps.append('Multiply by the fraction (or divide as needed).')

    # Calculator procedure line (per your request)
    calc_line = _calc_button_sequence(f"\"{func}\" \"{angle}\" \"=\" then round to 2 d.p.")

    explanation = f"{calc_line}. Answer ≈ {correct}."

    if qtype == 'mcq':
        x = float(correct)
        options = _make_unique_options(rng, correct, [
            _round_str(x + 0.1, 2),
            _round_str(x - 0.1, 2),
            _round_str(x + 0.2, 2),
            _round_str(x - 0.2, 2),
        ])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Calculator procedure (write a short instruction, e.g. "Press sin 35 ="): ',
                'correct_answer': f"press {func} {angle} =".lower(),
                'explanation': calc_line,
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final value (2 d.p.):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps2 = steps + [calc_line, 'Round to 2 decimal places.']
        return _make_scaffold(prompt=prompt, steps=steps2, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_solve_for_side(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Right triangle, angle given and one side, solve another side.
    # Keep to sin/cos/tan with clear selection.
    func = _choice(rng, ['sin', 'cos', 'tan'])
    angle = int(_choice(rng, [17, 22, 23, 30, 37, 49, 55]))

    if func == 'sin':
        hyp = float(_choice(rng, [20, 25, 33, 50, 62, 100]))
        opp = hyp * math.sin(_deg_to_rad(angle))
        correct = _round_str(opp, 2)
        prompt = f"In a right-angled triangle, θ = {angle}° and the hypotenuse is {hyp}. Find the opposite side (to 2 d.p.)."
        calc = _calc_button_sequence(f"\"sin\" \"{angle}\" \"=\" then \"ANS\" × \"{hyp}\"")
        explanation = f"sin θ = opposite/hypotenuse, so opposite = {hyp} × sin {angle}°. {calc}."
    elif func == 'cos':
        hyp = float(_choice(rng, [19, 20, 25, 33, 50, 62, 100]))
        adj = hyp * math.cos(_deg_to_rad(angle))
        correct = _round_str(adj, 2)
        prompt = f"In a right-angled triangle, θ = {angle}° and the hypotenuse is {hyp}. Find the adjacent side (to 2 d.p.)."
        calc = _calc_button_sequence(f"\"cos\" \"{angle}\" \"=\" then \"ANS\" × \"{hyp}\"")
        explanation = f"cos θ = adjacent/hypotenuse, so adjacent = {hyp} × cos {angle}°. {calc}."
    else:
        adj = float(_choice(rng, [6, 9, 12, 21, 31, 50, 100]))
        opp = adj * math.tan(_deg_to_rad(angle))
        correct = _round_str(opp, 2)
        prompt = f"In a right-angled triangle, θ = {angle}° and the adjacent side is {adj}. Find the opposite side (to 2 d.p.)."
        calc = _calc_button_sequence(f"\"tan\" \"{angle}\" \"=\" then \"ANS\" × \"{adj}\"")
        explanation = f"tan θ = opposite/adjacent, so opposite = {adj} × tan {angle}°. {calc}."

    if qtype == 'mcq':
        x = float(correct)
        options = _make_unique_options(rng, correct, [_round_str(x + 1.0, 2), _round_str(x - 1.0, 2), _round_str(x + 2.0, 2), _round_str(max(0.0, x - 2.0), 2)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Which ratio will you use? (sin/cos/tan)",
                'correct_answer': func,
                'explanation': 'Choose the ratio that connects the given side(s) to the required side.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Calculator procedure (short):',
                'correct_answer': calc.replace('Press ', '').strip().lower(),
                'explanation': calc,
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final answer (2 d.p.):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Identify opposite/adjacent/hypotenuse.', f"Write the {func} ratio.", 'Rearrange to make the unknown the subject.', calc, 'Round to 2 d.p.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_solve_for_angle(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    func = _choice(rng, ['sin', 'cos', 'tan'])

    if func == 'tan':
        ratio = float(_choice(rng, [1.7, 0.8, 0.5, 2.3]))
        angle = _rad_to_deg(math.atan(ratio))
        correct = _round_str(angle, 1)
        prompt = f"Determine θ (to 1 d.p.) if tan θ = {ratio}."
        calc = _calc_button_sequence(f"\"2ndF\" \"tan\" \"({ratio})\" \"=\" (degrees mode)")
        explanation = f"Use inverse tan: θ = tan⁻¹({ratio}). {calc}."
    elif func == 'sin':
        ratio = float(_choice(rng, [0.8, 2/3, 0.5]))
        ratio = min(1.0, max(-1.0, ratio))
        angle = _rad_to_deg(math.asin(ratio))
        correct = _round_str(angle, 1)
        prompt = f"Determine θ (to 1 d.p.) if sin θ = {_round_str(ratio, 2)}."
        calc = _calc_button_sequence(f"\"2ndF\" \"sin\" \"({_round_str(ratio, 2)})\" \"=\" (degrees mode)")
        explanation = f"Use inverse sin: θ = sin⁻¹({_round_str(ratio, 2)}). {calc}."
    else:
        ratio = float(_choice(rng, [0.32, 0.5, 0.8]))
        ratio = min(1.0, max(-1.0, ratio))
        angle = _rad_to_deg(math.acos(ratio))
        correct = _round_str(angle, 1)
        prompt = f"Determine θ (to 1 d.p.) if cos θ = {_round_str(ratio, 2)}."
        calc = _calc_button_sequence(f"\"2ndF\" \"cos\" \"({_round_str(ratio, 2)})\" \"=\" (degrees mode)")
        explanation = f"Use inverse cos: θ = cos⁻¹({_round_str(ratio, 2)}). {calc}."

    if qtype == 'mcq':
        x = float(correct)
        options = _make_unique_options(rng, correct, [_round_str(x + 1.0, 1), _round_str(x - 1.0, 1), _round_str(x + 2.0, 1), _round_str(max(0.0, x - 2.0), 1)])
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': f"Which inverse key do you use? (sin^-1/cos^-1/tan^-1)",
                'correct_answer': f"{func}^-1",
                'explanation': 'Use the inverse trig function for the given ratio.',
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Calculator procedure (short):',
                'correct_answer': calc.replace('Press ', '').strip().lower(),
                'explanation': calc,
            },
            {
                'id': _make_id('cp', rng),
                'kind': 'typed',
                'prompt': 'Final answer (1 d.p.):',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Ensure degrees mode.', f"Use {func}⁻¹ on the calculator.", calc, 'Round to 1 decimal place.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def generate_grade10_trigonometry1_question(
    *,
    subskill: str = 'trigonometry1',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Trigonometry 1'
    subskill = str(subskill or 'trigonometry1')
    difficulty = str(difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = str(question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    supported = [
        'identify_sides',
        'special_angles_exact',
        'evaluate_trig_decimal',
        'solve_for_side',
        'solve_for_angle',
    ]

    if subskill in {'trigonometry1', 'trigonometry', 'trig', 'mixed'}:
        subskill = _choice(rng, supported)

    generators = {
        'identify_sides': _gen_identify_sides,
        'special_angles_exact': _gen_special_angles_exact,
        'evaluate_trig_decimal': _gen_evaluate_trig_decimal,
        'solve_for_side': _gen_solve_for_side,
        'solve_for_angle': _gen_solve_for_angle,
    }

    if subskill not in generators:
        subskill = _choice(rng, supported)

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g10_trig1', rng),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
