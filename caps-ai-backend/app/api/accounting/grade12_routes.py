from flask import jsonify, request
import asyncio
import random

from . import accounting_bp
from ...utils.grade12_accounting.concepts_generator import generate_questions as generate_concepts
from ...utils.grade12_accounting.audits_governance_shareholding_generator import (
    generate_questions as generate_audits,
)
from ...utils.grade12_accounting.company_general_ledger_generator import generate_questions as generate_company_gl
from ...utils.grade12_accounting.financial_statements_notes_generator import (
    generate_questions as generate_financial_statements,
)
from ...utils.grade12_accounting.cash_flow_generator import generate_questions as generate_cash_flow
from ...utils.grade12_accounting.analysis_interpretation_generator import generate_questions as generate_analysis

# ── Term 2 generators ──
from ...utils.grade12_accounting.term2.fixed_assets_generator import generate_questions as generate_fixed_assets_t2
from ...utils.grade12_accounting.term2.inventory_systems_generator import generate_questions as generate_inventory_systems
from ...utils.grade12_accounting.term2.reconciliation_generator import generate_questions as generate_reconciliation_t2
from ...utils.grade12_accounting.term2.vat_generator import generate_questions as generate_vat_t2

from ...services.evaluation_service import grade_submission

_SUBSKILL_DISPATCH = {
    "concepts": generate_concepts,
    "audits-governance-shareholding": generate_audits,
    "company-general-ledger": generate_company_gl,
    "financial-statements-notes": generate_financial_statements,
    "cash-flow": generate_cash_flow,
    "analysis-interpretation": generate_analysis,
    # Term 2
    "fixed-assets-t2": generate_fixed_assets_t2,
    "inventory-systems": generate_inventory_systems,
    "reconciliation-t2": generate_reconciliation_t2,
    "vat-t2": generate_vat_t2,
}

@accounting_bp.route('/grade12/accounting/generate', methods=['POST'])
def generate_grade12_accounting_dispatch():
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
        if subskill_norm in ('', 'mixed'):
            r = random.Random()
            if seed is None:
                r.seed()
            else:
                r.seed(int(seed))
            subskill_norm = r.choice(list(_SUBSKILL_DISPATCH.keys()))

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

@accounting_bp.route('/grade12/accounting/mark', methods=['POST'])
def mark_grade12_accounting():
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
