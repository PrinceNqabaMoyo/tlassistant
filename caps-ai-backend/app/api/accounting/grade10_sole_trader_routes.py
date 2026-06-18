from flask import current_app, jsonify, request

import random

from . import accounting_bp
from ...utils.grade10_accounting.sole_trader_generator import generate_questions


@accounting_bp.route('/grade10/sole-trader/generate', methods=['POST'])
def generate_grade10_sole_trader():
    try:
        data = request.get_json() or {}

        mode = data.get('mode')
        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'mixed')
        count = data.get('count', 1)
        seed = data.get('seed')

        n = int(count) if isinstance(count, int) else 1
        if n < 1:
            n = 1
        if n > 20:
            n = 20

        r = random.Random()
        if seed is None:
            r.seed()
        else:
            r.seed(int(seed))

        questions = generate_questions(
            r=r,
            n=n,
            mode=mode or "",
            subskill=subskill,
            difficulty=difficulty,
            variant=question_type,
        )

        return jsonify({
            'success': True,
            'topic': 'grade10_accounting_sole_trader',
            'subskill': subskill,
            'difficulty': difficulty,
            'questions': questions,
        })
    except Exception as e:
        current_app.logger.exception("Grade10 sole-trader generate failed")
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
