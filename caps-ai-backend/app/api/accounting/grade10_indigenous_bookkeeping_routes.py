from flask import request, jsonify

from . import accounting_bp
from ...utils.grade10_accounting.indigenous_bookkeeping_generator_v2 import generate_questions


@accounting_bp.route('/grade10/indigenous-bookkeeping/generate', methods=['POST'])
def generate_grade10_indigenous_bookkeeping():
    try:
        data = request.get_json(force=True) or {}

        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')
        user_id = data.get('user_id')

        try:
            count_int = int(count)
        except Exception:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        if count_int < 1 or count_int > 20:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        questions = generate_questions(
            subskill=subskill,
            difficulty=difficulty,
            question_type=question_type,
            count=count_int,
            seed=seed,
        )

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
