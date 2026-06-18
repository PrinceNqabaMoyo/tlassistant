"""
Unified Grade 10 Accounting dispatch route (mirrors grade11_routes / grade12_routes pattern).
Covers Term 1 + Term 2 sub-skills via a single POST endpoint.
"""
import asyncio
import random
from flask import jsonify, request

from . import accounting_bp

# ── Term 1 generators (existing, root-level) ──
from ...utils.grade10_accounting.indigenous_bookkeeping_generator import (
    generate_questions as generate_indigenous_bookkeeping,
)
from ...utils.grade10_accounting.sole_trader_generator import (
    generate_questions as generate_sole_trader,
)

# ── Term 2 generators (moved to term2/ sub-package) ──
from ...utils.grade10_accounting.term2.salaries_wages_generator import (
    generate_questions as generate_salaries_wages,
)
from ...utils.grade10_accounting.term2.final_accounts_generator import (
    generate_questions as generate_final_accounts,
)
from ...utils.grade10_accounting.term2.vat_generator import (
    generate_questions as generate_vat,
)

from ...services.evaluation_service import grade_submission


_SUBSKILL_DISPATCH = {
    # Term 1
    "indigenous-bookkeeping": generate_indigenous_bookkeeping,
    "sole-trader": generate_sole_trader,
    # Term 2
    "salaries-wages": generate_salaries_wages,
    "final-accounts": generate_final_accounts,
    "vat": generate_vat,
}

_MIXED_SUBSKILL_POOL = list(_SUBSKILL_DISPATCH.keys())


@accounting_bp.route("/grade10/accounting/generate", methods=["POST"])
def generate_grade10_accounting_dispatch():
    try:
        data = request.get_json(force=True) or {}

        mode = data.get("mode")
        topic = data.get("topic")
        subskill = data.get("subskill", "mixed")
        difficulty = data.get("difficulty", "easy")
        question_type = data.get("question_type", "mixed")
        count = data.get("count", 1)
        seed = data.get("seed")
        rotation_ordinal = data.get("rotation_ordinal", 0)

        try:
            count_int = int(count)
        except Exception:
            return jsonify({"success": False, "error": "Count must be an integer between 1 and 20"}), 400

        if count_int < 1 or count_int > 20:
            return jsonify({"success": False, "error": "Count must be an integer between 1 and 20"}), 400

        topic_norm = str(topic or "").strip().lower()
        subskill_norm = str(subskill or "").strip().lower()
        try:
            rotation_ordinal_int = max(0, int(rotation_ordinal or 0))
        except Exception:
            rotation_ordinal_int = 0

        r = random.Random()
        if seed is None:
            r.seed()
        else:
            r.seed(int(seed))

        # ── Mixed mode ──
        if not topic_norm and subskill_norm in ("", "mixed"):
            questions = []
            subskills_used = []
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
                    subskill="mixed",
                    difficulty=difficulty,
                    question_type=question_type,
                    count=1,
                    seed=q_seed,
                    mode=mode or "",
                )
                if isinstance(qs, list):
                    questions.extend(qs)
                else:
                    questions.append(qs)

            return jsonify({
                "success": True,
                "subskill": "mixed",
                "subskills_used": subskills_used,
                "questions": questions,
                "count": len(questions),
            })

        # ── Concrete subskill ──
        dispatch_key = topic_norm or subskill_norm
        gen = _SUBSKILL_DISPATCH.get(dispatch_key)
        if gen is None:
            return (
                jsonify({
                    "success": False,
                    "error": "Unknown subskill. Use one of: " + ", ".join(sorted(_SUBSKILL_DISPATCH.keys())),
                }),
                400,
            )

        if dispatch_key == "final-accounts":
            questions = gen(
                subskill=subskill_norm if topic_norm else "mixed",
                difficulty=difficulty,
                question_type=question_type,
                count=count_int,
                seed=seed,
                mode=mode or "",
                rotation_ordinal=rotation_ordinal_int,
            )
        else:
            questions = gen(
                subskill=subskill_norm if topic_norm else "mixed",
                difficulty=difficulty,
                question_type=question_type,
                count=count_int,
                seed=seed,
                mode=mode or "",
            )

        return jsonify({
            "success": True,
            "topic": dispatch_key,
            "subskill": subskill_norm if topic_norm else dispatch_key,
            "questions": questions,
            "count": len(questions),
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@accounting_bp.route("/grade10/accounting/mark", methods=["POST"])
def mark_grade10_accounting():
    try:
        data = request.get_json(force=True) or {}
        answers = data.get("answers")
        questions = data.get("questions")

        if not answers or not questions:
            return jsonify({"success": False, "error": "Missing answers or questions in payload"}), 400

        results = asyncio.run(grade_submission(questions, answers))
        return jsonify({"success": True, "results": results})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
