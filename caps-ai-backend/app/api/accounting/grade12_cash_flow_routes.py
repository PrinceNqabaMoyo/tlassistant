from flask import jsonify, request

from . import accounting_bp
from ...utils.grade12_accounting.cash_flow_generator import generate_questions


@accounting_bp.route('/grade12/accounting/cash-flow/generate', methods=['POST'])
def generate_grade12_accounting_cash_flow():
    try:
        data = request.get_json(force=True) or {}

        mode = data.get('mode')
        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')

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
            mode=mode or '',
        )

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
