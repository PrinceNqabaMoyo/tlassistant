import random
import time
from typing import Any, Dict, List, Optional


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


def _gen_basic_shapes_definition(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    items = [
        ('triangle', 'A closed figure with three straight sides and three angles.'),
        ('quadrilateral', 'A closed figure with four straight sides and four angles.'),
        ('circle', 'A round figure where every point on the edge is the same distance from the centre.'),
    ]
    name, correct = rng.choice(items)

    if qtype == 'mcq':
        distractors = {
            'triangle': [
                'A closed figure with four straight sides and four angles.',
                'A round figure where every point on the edge is the same distance from the centre.',
                'A figure with three curved sides.',
            ],
            'quadrilateral': [
                'A closed figure with three straight sides and three angles.',
                'A round figure where every point on the edge is the same distance from the centre.',
                'A figure with four curved sides.',
            ],
            'circle': [
                'A closed figure with three straight sides and three angles.',
                'A closed figure with four straight sides and four angles.',
                'A figure with straight sides and sharp corners.',
            ],
        }
        options = [correct, *distractors[name]]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"Which option best describes a {name}?",
            options=options,
            correct_answer=correct,
            explanation=correct,
            parameters={'shape': name},
        )

    return _make_typed(
        prompt=f"Describe what a {name} is.",
        correct_answer=correct,
        explanation=correct,
        parameters={'shape': name},
    )


def _gen_adjacent_opposite_sides(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Use a generic quadrilateral ABCD.
    pairs = [
        (('AB', 'BC'), 'adjacent'),
        (('BC', 'CD'), 'adjacent'),
        (('CD', 'DA'), 'adjacent'),
        (('DA', 'AB'), 'adjacent'),
        (('AB', 'CD'), 'opposite'),
        (('BC', 'DA'), 'opposite'),
    ]
    (s1, s2), correct = rng.choice(pairs)

    if qtype == 'mcq':
        options = ['adjacent', 'opposite']
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"In quadrilateral ABCD, are sides {s1} and {s2} adjacent or opposite?",
            options=options,
            correct_answer=correct,
            explanation=f"Adjacent sides share a common vertex; opposite sides do not touch.",
            parameters={'sides': [s1, s2]},
        )

    return _make_typed(
        prompt=f"In quadrilateral ABCD, are sides {s1} and {s2} adjacent or opposite?",
        correct_answer=correct,
        explanation="Adjacent sides meet at a vertex; opposite sides do not meet.",
        parameters={'sides': [s1, s2]},
    )


def _gen_triangle_types(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    types = [
        ('equilateral', 'Three equal sides (and three equal angles).'),
        ('isosceles', 'Two equal sides (and two equal base angles).'),
        ('scalene', 'All sides different (and all angles different).'),
        ('right-angled', 'One angle is exactly 90°.'),
    ]
    tri_type, definition = rng.choice(types)

    if qtype == 'mcq':
        options = [t[0] for t in types]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"A triangle has this property: {definition} What type of triangle is it?",
            options=options,
            correct_answer=tri_type,
            explanation=f"That property describes a {tri_type} triangle.",
            parameters={'definition': definition},
        )

    return _make_typed(
        prompt=f"A triangle has this property: {definition} What type of triangle is it?",
        correct_answer=tri_type,
        explanation=f"That property describes a {tri_type} triangle.",
        parameters={'definition': definition},
    )


def _gen_triangle_unknown_sides(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Deterministic tick-mark style: equilateral or isosceles.
    kind = rng.choice(['equilateral', 'isosceles']) if difficulty != 'hard' else rng.choice(['equilateral', 'isosceles', 'scalene_insufficient'])

    if kind == 'equilateral':
        side = rng.randint(8, 40)
        prompt = f"Triangle ABC is equilateral. If AB = {side} mm, what is BC?"
        return _make_typed(
            prompt=prompt,
            correct_answer=str(side),
            explanation='All sides in an equilateral triangle are equal, so BC = AB.',
            parameters={'AB': side, 'BC': side, 'type': 'equilateral'},
        )

    if kind == 'isosceles':
        equal_side = rng.randint(5, 30)
        prompt = f"Triangle DEF is isosceles with DE = EF. If DE = {equal_side} cm, what is EF?"
        if qtype == 'mcq':
            options = [str(equal_side), str(equal_side + 1), str(max(1, equal_side - 1)), str(equal_side * 2)]
            options = list(dict.fromkeys(options))
            options = options[:4]
            rng.shuffle(options)
            return _make_mcq(
                prompt=prompt,
                options=options,
                correct_answer=str(equal_side),
                explanation='In an isosceles triangle, the marked equal sides have the same length.',
                parameters={'DE': equal_side, 'EF': equal_side, 'type': 'isosceles'},
            )
        return _make_typed(
            prompt=prompt,
            correct_answer=str(equal_side),
            explanation='In an isosceles triangle, the marked equal sides have the same length, so EF = DE.',
            parameters={'DE': equal_side, 'EF': equal_side, 'type': 'isosceles'},
        )

    # scalene_insufficient
    a = rng.randint(10, 60)
    b = rng.randint(10, 60)
    while b == a:
        b = rng.randint(10, 60)
    prompt = f"Triangle GHI has all sides different. If GH = {a} mm and HI = {b} mm, can you determine GI?"
    correct = 'no'
    if qtype == 'mcq':
        options = ['yes', 'no']
        rng.shuffle(options)
        return _make_mcq(
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation='Not enough information: knowing two sides does not fix the third side for a general scalene triangle.',
            parameters={'GH': a, 'HI': b},
        )
    return _make_typed(
        prompt=prompt,
        correct_answer=correct,
        explanation='Not enough information: the third side could vary as long as the triangle inequality holds.',
        parameters={'GH': a, 'HI': b},
    )


def _gen_quadrilateral_types_properties(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    items = [
        ('parallelogram', 'Both pairs of opposite sides are parallel.'),
        ('rectangle', 'All angles are right angles (90°) and opposite sides are equal and parallel.'),
        ('square', 'All sides are equal and all angles are right angles (90°).'),
        ('rhombus', 'All sides are equal; opposite sides are parallel.'),
        ('kite', 'Two pairs of adjacent sides are equal.'),
        ('trapezium', 'At least one pair of opposite sides is parallel.'),
    ]
    shape, property_text = rng.choice(items)

    if qtype == 'mcq':
        options = [s for s, _ in items]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"Which quadrilateral matches this description? {property_text}",
            options=options,
            correct_answer=shape,
            explanation=f"That description matches a {shape}.",
            parameters={'property': property_text},
        )

    return _make_typed(
        prompt=f"Name the quadrilateral: {property_text}",
        correct_answer=shape,
        explanation=f"That description matches a {shape}.",
        parameters={'property': property_text},
    )


def _gen_quadrilateral_unknown_sides(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['parallelogram', 'kite', 'trapezium'])

    if kind == 'parallelogram':
        ad = rng.randint(2, 30)
        prompt = f"Quadrilateral ABCD is a parallelogram. If AD = {ad} cm, what is BC?"
        return _make_typed(
            prompt=prompt,
            correct_answer=str(ad),
            explanation='In a parallelogram, opposite sides are equal, so BC = AD.',
            parameters={'AD': ad, 'BC': ad, 'type': 'parallelogram'},
        )

    if kind == 'kite':
        pq = rng.randint(2, 12)
        qr = rng.randint(6, 20)
        prompt = f"PQRS is a kite with PQ = {pq} cm and QR = {qr} cm. Which sides are equal to PQ and QR?"
        correct = 'PQ = PS and QR = RS'
        if qtype == 'mcq':
            options = [
                'PQ = PS and QR = RS',
                'PQ = QR and PS = RS',
                'PQ = RS and QR = PS',
                'PQ = QR and QR = RS',
            ]
            rng.shuffle(options)
            return _make_mcq(
                prompt=prompt,
                options=options,
                correct_answer=correct,
                explanation='A kite has two pairs of adjacent equal sides: PQ = PS and QR = RS.',
                parameters={'PQ': pq, 'QR': qr, 'type': 'kite'},
            )
        return _make_typed(
            prompt=prompt,
            correct_answer=correct,
            explanation='A kite has two pairs of adjacent equal sides: PQ = PS and QR = RS.',
            parameters={'PQ': pq, 'QR': qr, 'type': 'kite'},
        )

    # trapezium
    prompt = 'In a trapezium, do all opposite sides have to be parallel?' 
    correct = 'no'
    if qtype == 'mcq':
        options = ['yes', 'no']
        rng.shuffle(options)
        return _make_mcq(
            prompt=prompt,
            options=options,
            correct_answer=correct,
            explanation='A trapezium has at least one pair of opposite sides parallel, not necessarily both pairs.',
            parameters={'type': 'trapezium'},
        )
    return _make_typed(
        prompt=prompt,
        correct_answer=correct,
        explanation='A trapezium has at least one pair of opposite sides parallel, not necessarily both pairs.',
        parameters={'type': 'trapezium'},
    )


def _gen_circle_parts(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    items = [
        ('radius', 'A line segment from the centre of a circle to a point on the circle.'),
        ('diameter', 'A straight line across a circle passing through the centre.'),
        ('chord', 'A straight line joining two points on a circle.'),
        ('segment', 'The area between a chord and an arc.'),
        ('sector', 'The region between two radii and an arc.'),
        ('centre', 'The midpoint of a circle; all radii start here.'),
    ]
    term, definition = rng.choice(items)

    if qtype == 'mcq':
        options = [t for t, _ in items]
        rng.shuffle(options)
        return _make_mcq(
            prompt=f"Which circle term matches this definition? {definition}",
            options=options,
            correct_answer=term,
            explanation=f"That definition describes the {term}.",
            parameters={'definition': definition},
        )

    return _make_typed(
        prompt=f"Which circle term matches this definition? {definition}",
        correct_answer=term,
        explanation=f"That definition describes the {term}.",
        parameters={'definition': definition},
    )


def _gen_similar_congruent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    scenarios = [
        ('similar but not congruent', 'Two triangles have the same angles, but one is larger than the other.'),
        ('congruent', 'Two shapes have the same shape and the same size.'),
        ('neither', 'Two shapes have different angles and different side ratios.'),
    ]
    correct, desc = rng.choice(scenarios)

    options = ['similar and congruent', 'similar but not congruent', 'neither', 'congruent']
    # Remove impossible duplicate phrasing while keeping four options stable.
    options = ['similar but not congruent', 'congruent', 'neither', 'similar and congruent']

    if qtype == 'typed':
        return _make_typed(
            prompt=f"Classify the shapes: {desc} (answer: congruent / similar but not congruent / neither)",
            correct_answer=correct,
            explanation=f"{correct.capitalize()} is correct because: {desc}",
            parameters={'scenario': desc},
        )

    rng.shuffle(options)
    return _make_mcq(
        prompt=f"Classify the shapes: {desc}",
        options=options,
        correct_answer=correct,
        explanation=f"{correct.capitalize()} is correct because: {desc}",
        parameters={'scenario': desc},
    )


def generate_grade7_geometry_2d_shapes_question(
    *,
    subskill: str,
    difficulty: str,
    question_type: str,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    normalized_subskill = (subskill or '').strip().lower()
    normalized_difficulty = (difficulty or 'easy').strip().lower()
    normalized_qtype = (question_type or 'typed').strip().lower()

    if normalized_difficulty not in {'easy', 'medium', 'hard'}:
        normalized_difficulty = 'easy'

    if normalized_qtype not in {'typed', 'mcq', 'scaffold'}:
        normalized_qtype = 'typed'

    typed_capable = {
        'basic_shapes_definition',
        'adjacent_opposite_sides',
        'triangle_types',
        'triangle_unknown_sides',
        'quadrilateral_types_properties',
        'quadrilateral_unknown_sides',
        'circle_parts',
        'similar_congruent',
    }

    scaffold_capable = {
        'adjacent_opposite_sides',
        'triangle_unknown_sides',
        'quadrilateral_unknown_sides',
        'circle_parts',
        'similar_congruent',
    }

    if normalized_subskill in {'', 'geometry_of_2d_shapes', 'geometry of 2d shapes', 'geometry_2d_shapes'}:
        if normalized_qtype == 'scaffold':
            normalized_subskill = rng.choice(sorted(scaffold_capable))
        else:
            normalized_subskill = rng.choice(sorted(typed_capable))

    if normalized_qtype == 'scaffold' and normalized_subskill not in scaffold_capable:
        normalized_qtype = 'typed'

    generators = {
        'basic_shapes_definition': _gen_basic_shapes_definition,
        'adjacent_opposite_sides': _gen_adjacent_opposite_sides,
        'triangle_types': _gen_triangle_types,
        'triangle_unknown_sides': _gen_triangle_unknown_sides,
        'quadrilateral_types_properties': _gen_quadrilateral_types_properties,
        'quadrilateral_unknown_sides': _gen_quadrilateral_unknown_sides,
        'circle_parts': _gen_circle_parts,
        'similar_congruent': _gen_similar_congruent,
    }

    if normalized_subskill not in generators:
        normalized_subskill = 'basic_shapes_definition'

    if normalized_qtype == 'scaffold':
        if normalized_subskill == 'adjacent_opposite_sides':
            steps = [
                {'title': 'Remember the definitions', 'content': 'Adjacent sides share a vertex. Opposite sides do not touch.'},
                {'title': 'Check the letters', 'content': 'If the sides share a letter (vertex), they are adjacent.'},
            ]
            pair = generators[normalized_subskill](rng, normalized_difficulty, 'typed')
            question_text = pair['question']
            correct = pair['correct_answer']
            checkpoints = [
                {
                    'id': 'c1_share',
                    'kind': 'mcq',
                    'prompt': 'Adjacent sides share…',
                    'options': ['a vertex', 'a midpoint', 'a circle', 'a diameter'],
                    'correct_answer': 'a vertex',
                    'explanation': 'Adjacent sides meet at a vertex.',
                },
                {
                    'id': 'c2_answer',
                    'kind': 'mcq',
                    'prompt': question_text,
                    'options': ['adjacent', 'opposite'],
                    'correct_answer': correct,
                    'explanation': pair['explanation'],
                },
            ]
            base = _make_scaffold(
                prompt=question_text,
                steps=steps,
                checkpoints=checkpoints,
                final_answer=correct,
                explanation=pair['explanation'],
                parameters=pair.get('parameters') or {},
            )
        elif normalized_subskill == 'circle_parts':
            steps = [
                {'title': 'Read the definition carefully', 'content': 'Look for keywords like centre, two points, chord, arc, or radii.'},
                {'title': 'Match to the right term', 'content': 'Radius/diameter/chord/segment/sector/centre each have a specific meaning.'},
            ]
            typed = generators[normalized_subskill](rng, normalized_difficulty, 'typed')
            term = typed['correct_answer']
            definition = typed.get('parameters', {}).get('definition', '')
            checkpoints = [
                {
                    'id': 'c1_keyword',
                    'kind': 'typed',
                    'prompt': 'Write one keyword you notice in the definition (e.g., centre, chord, arc, radii).',
                    'correct_answer': 'centre',
                    'explanation': 'Any reasonable keyword helps you match definitions. (This checkpoint is self-check.)',
                },
                {
                    'id': 'c2_term',
                    'kind': 'typed',
                    'prompt': f"Definition: {definition}\nWrite the correct term.",
                    'correct_answer': term,
                    'explanation': typed['explanation'],
                },
            ]
            base = _make_scaffold(
                prompt=typed['question'],
                steps=steps,
                checkpoints=checkpoints,
                final_answer=term,
                explanation=typed['explanation'],
                parameters=typed.get('parameters') or {},
            )
        else:
            typed = generators[normalized_subskill](rng, normalized_difficulty, 'typed')
            steps = [
                {'title': 'Identify the rule', 'content': 'Use the property given in the question.'},
                {'title': 'Apply it', 'content': 'Make a direct conclusion from the rule.'},
            ]
            checkpoints = [
                {
                    'id': 'c1_answer',
                    'kind': 'typed',
                    'prompt': typed['question'],
                    'correct_answer': typed['correct_answer'],
                    'explanation': typed['explanation'],
                }
            ]
            base = _make_scaffold(
                prompt=typed['question'],
                steps=steps,
                checkpoints=checkpoints,
                final_answer=typed['correct_answer'],
                explanation=typed['explanation'],
                parameters=typed.get('parameters') or {},
            )
    else:
        base = generators[normalized_subskill](rng, normalized_difficulty, normalized_qtype)

    q = {
        'id': _make_id('g7_geo_2d'),
        'topic': 'Geometry of 2D shapes',
        'subskill': normalized_subskill,
        'difficulty': normalized_difficulty,
        **base,
    }

    _validate_question(q)
    return q
