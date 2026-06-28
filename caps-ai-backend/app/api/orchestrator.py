from flask import Blueprint, request, jsonify
from app.services import procedure_tracker as pt
from app.services.llm_provider import get_llm_provider
from app.services.orchestrator_service import (
    generate_study_plan,
    check_and_notify,
    initialize_orchestrator,
)

orchestrator_bp = Blueprint('orchestrator', __name__)


@orchestrator_bp.route('/study-plan', methods=['POST'])
def handle_study_plan():
    """Generates a weekly study plan for a student.
    Body: {"user_id": "..."}
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        result = generate_study_plan(user_id)
        return jsonify(result)
    except Exception as e:
        print(f"Error generating study plan: {e}")
        return jsonify({"error": str(e)}), 500


@orchestrator_bp.route('/check-notify', methods=['POST'])
def handle_check_and_notify():
    """Runs the daily check and creates notifications.
    Body: {"user_id": "..."}
    Returns the list of notifications created.
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        result = check_and_notify(user_id)
        return jsonify(result)
    except Exception as e:
        print(f"Error during check-and-notify: {e}")
        return jsonify({"error": str(e)}), 500


@orchestrator_bp.route('/run', methods=['POST'])
def handle_run_orchestrator():
    """Full orchestrator run: study plan + notifications.
    Body: {"user_id": "..."}
    Can also be called with {"all_users": true} for batch processing (admin only).
    """
    data = request.get_json() or {}
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    try:
        plan_result = generate_study_plan(user_id)
        notify_result = check_and_notify(user_id)
        return jsonify({
            "status": "ok",
            "study_plan": plan_result,
            "notifications": notify_result,
        })
    except Exception as e:
        print(f"Error during orchestrator run: {e}")
        return jsonify({"error": str(e)}), 500


@orchestrator_bp.route('/diagnose-procedure', methods=['POST'])
def handle_diagnose_procedure():
    """Diagnose a student's working against the canonical solution.

    Body: {
        "canonical_solution": {...},
        "student_steps": ["2x + 2 = 10", "2x = 8", "x = 4"],
        "marks": 3,
        "tier": "standard" | "pro"
    }

    Returns deterministic diagnosis; for Pro tier, adds a Socratic explanation.
    """
    data = request.get_json() or {}
    canonical = data.get("canonical_solution", {})
    steps = data.get("student_steps", [])
    marks = int(data.get("marks", 1))
    tier = data.get("tier", "standard")

    if not isinstance(steps, list):
        steps = str(steps or "").splitlines()

    try:
        diag = pt.diagnose(canonical, steps, marks)
    except Exception as e:
        return jsonify({"error": f"Diagnosis failed: {e}"}), 500

    # Standard tier: return deterministic diagnosis only
    if tier != "pro":
        return jsonify({"status": "ok", "diagnosis": diag})

    # Pro tier: generate Socratic explanation via LLM
    provider = get_llm_provider()
    prompt = _build_socratic_prompt(diag, canonical, steps)
    try:
        explanation = provider.invoke(messages=[{"role": "user", "content": prompt}])
    except Exception:
        explanation = "Review your working step by step to find the first error."

    return jsonify({
        "status": "ok",
        "diagnosis": diag,
        "explanation": explanation,
    })


def _build_socratic_prompt(diag, canonical, steps) -> str:
    first_error = diag.get("first_error_step")
    error_type = diag.get("error_type", "unknown")
    misconception = diag.get("misconception_tags", [])
    canon_steps = canonical.get("steps", [])
    goal = canonical.get("goal", "solve the problem")

    lines = [
        "You are a patient, Socratic maths tutor for a South African student.",
        "The student is working through a multi-step problem.",
        f"Goal: {goal}",
        "",
        "Canonical (correct) steps:",
    ]
    for i, s in enumerate(canon_steps):
        lines.append(f"  Step {i + 1}: {s.get('op', '')} — {s.get('from_latex', '')} -> {s.get('to_latex', '')}")

    lines.extend([
        "",
        "Student's steps:",
    ])
    for i, s in enumerate(steps):
        marker = "  <-- FIRST ERROR" if i == first_error else ""
        lines.append(f"  Step {i + 1}: {s}{marker}")

    lines.extend([
        "",
        f"First error at step: {first_error + 1 if first_error is not None else 'none'}",
        f"Error type: {error_type}",
        f"Misconceptions: {', '.join(misconception) if misconception else 'none'}",
        "",
        "Give a short, encouraging Socratic explanation that:",
        "1. Pinpoints the exact step where the working broke.",
        "2. Asks a guiding question (does NOT give the answer).",
        "3. References the specific rule that was violated.",
        "Keep it to 2-3 sentences max.",
    ])
    return "\n".join(lines)
