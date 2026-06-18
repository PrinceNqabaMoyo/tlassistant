from flask import request, jsonify

from . import math_bp
from ...utils.grade12_patterns_sequences_series_generator import generate_questions


@math_bp.route('/grade12/patterns-sequences-series/generate', methods=['POST'])
def generate_grade12_patterns_sequences_series():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')

        if not isinstance(count, int) or count < 1 or count > 20:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        questions = []
        for i in range(count):
            q_seed = None
            if seed is not None:
                try:
                    q_seed = int(seed) + i
                except Exception:
                    q_seed = None

            qs = generate_questions(
                subskill=subskill,
                difficulty=difficulty,
                question_type=question_type,
                count=1,
                seed=q_seed,
            )
            questions.append(qs[0])

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
