from flask import jsonify, request
 
from . import math_bp
from ...utils.grade12_functions_generator import generate_questions
 
 
@math_bp.route("/grade12/functions/generate", methods=["POST"])
def generate_grade12_functions():
    try:
        data = request.get_json(silent=True) or {}

        subskill = data.get("subskill") or "mixed"
        difficulty = data.get("difficulty", "easy")
        question_type = data.get("question_type", "typed")
        count = data.get("count", 1)
        seed = data.get("seed")

        try:
            count_int = int(count)
        except Exception:
            return jsonify({"success": False, "error": "Count must be an integer between 1 and 20"}), 400

        if count_int < 1 or count_int > 20:
            return jsonify({"success": False, "error": "Count must be an integer between 1 and 20"}), 400

        result = generate_questions(
            subskill=None if subskill == "mixed" else subskill,
            difficulty=difficulty,
            question_type=question_type,
            count=count_int,
            seed=seed,
        )

        if not result.get("ok"):
            return jsonify({"success": False, "error": result.get("error") or "Generation failed"}), 400

        questions = result.get("questions") or []
        return jsonify({"success": True, "questions": questions, "count": len(questions)})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
