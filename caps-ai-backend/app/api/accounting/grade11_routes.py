import asyncio
import random
from flask import jsonify, request

from . import accounting_bp
from ...utils.grade11_accounting.concepts_generator import generate_questions as generate_concepts
from ...utils.grade11_accounting.fixed_assets_generator import generate_questions as generate_fixed_assets
from ...utils.grade11_accounting.partnership_ledger_generator import generate_questions as generate_partnership_ledger
from ...utils.grade11_accounting.partnership_balance_sheet_generator import (
    generate_questions as generate_partnership_balance_sheet,
)
from ...utils.grade11_accounting.reconciliation_generator import generate_questions as generate_reconciliation
from ...utils.grade11_accounting.income_statement_generator import generate_questions as generate_income_statement
from ...utils.grade11_accounting.controlled_test_generator import generate_questions as generate_controlled_test

# ── Term 2 generators ──
from ...utils.grade11_accounting.term2.clubs_nonprofit_generator import generate_questions as generate_clubs_nonprofit
from ...utils.grade11_accounting.term2.analysis_interpretation_generator import generate_questions as generate_analysis_interpretation_t2

from ...services.evaluation_service import grade_submission


_SUBSKILL_DISPATCH = {
    "concepts": generate_concepts,
    "fixed-assets": generate_fixed_assets,
    "partnership-ledger": generate_partnership_ledger,
    "partnership-balance-sheet": generate_partnership_balance_sheet,
    "reconciliation": generate_reconciliation,
    "income-statement": generate_income_statement,
    "controlled-test": generate_controlled_test,
    # Term 2
    "clubs-nonprofit": generate_clubs_nonprofit,
    "analysis-interpretation-t2": generate_analysis_interpretation_t2,
}


_MIXED_SUBSKILL_POOL = [
    "concepts",
    "fixed-assets",
    "partnership-ledger",
    "partnership-balance-sheet",
    "reconciliation",
    "income-statement",
    "clubs-nonprofit",
    "analysis-interpretation-t2",
]


@accounting_bp.route('/grade11/accounting/generate', methods=['POST'])
def generate_grade11_accounting_dispatch():
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

        subskill_norm = str(subskill or '').strip().lower()

        r = random.Random()
        if seed is None:
            r.seed()
        else:
            r.seed(int(seed))

        # Mixed: rotate across actual subskills so each click yields variety.
        if subskill_norm in ('', 'mixed'):
            questions = []
            subskills_used = []

            # Prefer no repetition until we exhaust the pool.
            pool = list(_MIXED_SUBSKILL_POOL)
            for _ in range(count_int):
                if not pool:
                    pool = list(_MIXED_SUBSKILL_POOL)

                chosen = r.choice(pool)
                pool.remove(chosen)
                subskills_used.append(chosen)

                gen = _SUBSKILL_DISPATCH.get(chosen)
                if gen is None:
                    continue

                q_seed = r.randint(1, 2_147_483_647)
                qs = gen(
                    subskill='mixed',
                    difficulty=difficulty,
                    question_type=question_type,
                    count=1,
                    seed=q_seed,
                    mode=mode or '',
                )
                if isinstance(qs, list):
                    questions.extend(qs)
                else:
                    questions.append(qs)

            return jsonify(
                {
                    'success': True,
                    'subskill': 'mixed',
                    'subskills_used': subskills_used,
                    'questions': questions,
                    'count': len(questions),
                }
            )

        # Concrete subskill: restrict generation to that subskill only.
        gen = _SUBSKILL_DISPATCH.get(subskill_norm)
        if gen is None:
            return (
                jsonify(
                    {
                        'success': False,
                        'error': 'Unknown subskill. Use one of: ' + ', '.join(sorted(_SUBSKILL_DISPATCH.keys())),
                    }
                ),
                400,
            )

        questions = gen(
            subskill='mixed',
            difficulty=difficulty,
            question_type=question_type,
            count=count_int,
            seed=seed,
            mode=mode or '',
        )

        return jsonify({'success': True, 'subskill': subskill_norm, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@accounting_bp.route('/grade11/accounting/mark', methods=['POST'])
def mark_grade11_accounting():
    try:
        data = request.get_json(force=True) or {}
        answers = data.get('answers')
        questions = data.get('questions')

        if not answers or not questions:
            return jsonify({
                'success': False,
                'error': 'Missing answers or questions in payload'
            }), 400

        results = asyncio.run(grade_submission(questions, answers))
        return jsonify({
            'success': True,
            'results': results
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
