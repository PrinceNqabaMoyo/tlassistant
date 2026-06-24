import json
import os
from flask import Blueprint, request, jsonify

evaluation_bp = Blueprint('evaluation', __name__)

# Read key from environment (same place llm_provider.py looks)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@evaluation_bp.route('/evaluate-typed', methods=['POST'])
def evaluate_typed_answer():
    """
    Evaluate a student's free-text answer against a sample answer using Gemini.
    Only used for 'typed' question types where deterministic marking is not possible.
    """
    try:
        data = request.get_json()
        question_prompt = data.get("question_prompt", "")
        sample_answer = data.get("sample_answer", "")
        student_answer = data.get("student_answer", "")
        subject = data.get("subject", "")
        grade = data.get("grade", "")

        if not question_prompt or not student_answer:
            return jsonify({"error": "Missing question_prompt or student_answer"}), 400

        if not GOOGLE_API_KEY:
            return jsonify({"evaluation": {
                "is_correct": False,
                "score": 0,
                "feedback": "AI evaluation is not available right now. Please review the sample answer and marking points instead.",
                "key_points_hit": [],
                "key_points_missed": [],
            }}), 200

        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
        except Exception:
            return jsonify({"evaluation": {
                "is_correct": False,
                "score": 0,
                "feedback": "AI evaluation is not available (missing LLM package). Please review the sample answer and marking points instead.",
                "key_points_hit": [],
                "key_points_missed": [],
            }}), 200

        llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            temperature=0.1,
            google_api_key=GOOGLE_API_KEY,
        )

        evaluation_prompt = f"""You are a {subject} Grade {grade} teacher marking a student's answer.

QUESTION: {question_prompt}

SAMPLE ANSWER (marking guide): {sample_answer}

STUDENT'S ANSWER: {student_answer}

Evaluate the student's answer against the sample answer. Respond in this exact JSON format:
{{
  "is_correct": true/false,
  "score": <number 0-100>,
  "feedback": "<brief, encouraging feedback explaining what was correct and what was missing or wrong. Max 3 sentences.>",
  "key_points_hit": ["<point 1>", "<point 2>"],
  "key_points_missed": ["<missed point 1>"]
}}

Rules:
- Award partial credit for partially correct answers.
- The student does not need to match the sample answer word-for-word; accept equivalent meanings.
- is_correct = true if score >= 50.
- Be encouraging but honest.
- Return ONLY valid JSON, no markdown fences."""

        response = llm.invoke(evaluation_prompt)
        raw_output = response.content.strip()

        # Try to parse as JSON; if it fails, return raw text as feedback
        try:
            parsed = json.loads(raw_output)
            return jsonify({"evaluation": parsed})
        except json.JSONDecodeError:
            return jsonify({
                "evaluation": {
                    "is_correct": False,
                    "score": 0,
                    "feedback": raw_output,
                    "key_points_hit": [],
                    "key_points_missed": [],
                }
            })

    except Exception as e:
        print(f"Error in evaluate-typed: {e}")
        return jsonify({"error": str(e)}), 500
