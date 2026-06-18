from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os
import google.generativeai as genai

# Setup Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")
genai.configure(api_key=api_key)

router = APIRouter()

class MarkingRequest(BaseModel):
    questions: List[Dict[str, Any]]
    answers: Dict[str, Any]

class MarkingResponse(BaseModel):
    total_score: float
    max_score: float
    results: Dict[str, Any]

def evaluate_mcq(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    try:
        correct_idx = int(question.get("correct_index", -1))
        user_idx = int(answer)
        is_correct = (correct_idx == user_idx)
        marks = float(question.get("marks", 1.0))
        score = marks if is_correct else 0.0
        return {
            "is_correct": is_correct,
            "score": score,
            "max_score": marks,
            "feedback": "Correct!" if is_correct else f"Incorrect. {question.get('explanation', '')}"
        }
    except (ValueError, TypeError):
        return {"is_correct": False, "score": 0.0, "max_score": float(question.get("marks", 1.0)), "feedback": "Invalid answer format."}

def evaluate_calc(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    try:
        correct_val = float(question.get("correct_value", 0.0))
        user_val = float(answer)
        # Allow small floating point tolerance
        is_correct = abs(correct_val - user_val) < 0.01
        marks = float(question.get("marks", 1.0))
        score = marks if is_correct else 0.0
        return {
            "is_correct": is_correct,
            "score": score,
            "max_score": marks,
            "feedback": "Correct!" if is_correct else f"Incorrect. The correct answer is {correct_val}."
        }
    except (ValueError, TypeError):
        return {"is_correct": False, "score": 0.0, "max_score": float(question.get("marks", 1.0)), "feedback": "Invalid number format."}

def evaluate_table(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    # Exact match for table cells
    score = 0.0
    total_cells = 0
    feedback = []
    
    if not isinstance(answer, dict):
         return {"is_correct": False, "score": 0.0, "max_score": float(question.get("marks", 1.0)), "feedback": "Invalid answer format for table."}
         
    # Table logic varies. To be perfectly generic we need the exact correct map or we rely on the frontend to pass the correct map in the evaluation prompt.
    # We will implement a basic pass-through for now, but ideally we'd evaluate it rigorously here based on question type.
    # For now, we will return a pending state and let the LLM evaluate it if it's complex, or rely on strict matching if we have correct_map.
    
    correct_map = question.get("correct_map", {})
    if not correct_map:
        return {"is_correct": False, "score": 0.0, "max_score": float(question.get("marks", 1.0)), "feedback": "Backend missing correct map."}

    max_score = float(question.get("marks", 1.0))
    # Count expected answers
    expected_answers = sum(len(cols) for cols in correct_map.values() if cols)
    if expected_answers == 0:
         return {"is_correct": True, "score": max_score, "max_score": max_score, "feedback": "No answers required."}

    points_per_cell = max_score / expected_answers
    
    for row_idx_str, cols in correct_map.items():
        user_row = answer.get(row_idx_str, {})
        for col_idx_str, expected_val in cols.items():
            if expected_val is None:
                continue
            user_val = user_row.get(col_idx_str)
            if str(user_val).strip() == str(expected_val).strip():
                score += points_per_cell
            else:
                feedback.append(f"Row {int(row_idx_str)+1}, Col {int(col_idx_str)+1}: Expected {expected_val}, got {user_val}")
                
    is_correct = score >= max_score - 0.01
    return {
        "is_correct": is_correct,
        "score": min(score, max_score),
        "max_score": max_score,
        "feedback": "All correct!" if is_correct else "; ".join(feedback)
    }

async def evaluate_typed(question: Dict[str, Any], answer: Any) -> Dict[str, Any]:
    user_answer = str(answer).strip()
    marks = float(question.get("marks", 2.0))
    rubric = question.get("grading_rubric", [])
    sample = question.get("sample_answer", "")
    prompt_text = question.get("prompt", "")

    if not user_answer:
        return {"is_correct": False, "score": 0.0, "max_score": marks, "feedback": "No answer provided."}

    model = genai.GenerativeModel('gemini-2.5-flash')
    
    eval_prompt = f"""
    You are an expert Accounting teacher grading a Grade 10 student's typed answer.
    
    Question Prompt: "{prompt_text}"
    Student's Answer: "{user_answer}"
    Teacher's Sample Answer: "{sample}"
    Key Rubric Concepts to look for: {rubric}
    Maximum Marks: {marks}
    
    Evaluate the student's answer. Give marks based on how many rubric concepts they successfully mentioned or explained. 
    It doesn't have to be identical to the sample answer, it just needs to be conceptually correct.
    
    Respond STRICTLY in the following format:
    SCORE: [number]
    FEEDBACK: [1-2 sentences explaining why they got that score]
    """

    try:
        response = model.generate_content(eval_prompt)
        text = response.text.strip()
        
        score_line = [line for line in text.split('\\n') if line.startswith('SCORE:')][0]
        feedback_line = [line for line in text.split('\\n') if line.startswith('FEEDBACK:')][0]
        
        score = float(score_line.replace('SCORE:', '').strip())
        feedback = feedback_line.replace('FEEDBACK:', '').strip()
        
        # Cap score
        score = min(score, marks)
        score = max(score, 0.0)
        
        is_correct = score >= marks - 0.01

        return {
            "is_correct": is_correct,
            "score": score,
            "max_score": marks,
            "feedback": feedback
        }

    except Exception as e:
        print(f"LLM Eval error: {e}")
        return {"is_correct": False, "score": 0.0, "max_score": marks, "feedback": "Error evaluating typed answer."}

@router.post("/")
async def mark_assessment(req: MarkingRequest):
    results = {}
    total_score = 0.0
    max_score = 0.0

    for q in req.questions:
        qid = q["id"]
        qtype = q.get("question_type")
        user_ans = req.answers.get(qid)
        
        if user_ans is None:
             results[qid] = {"is_correct": False, "score": 0.0, "max_score": float(q.get("marks", 1.0)), "feedback": "Unanswered."}
        elif qtype == "mcq":
             results[qid] = evaluate_mcq(q, user_ans)
        elif qtype == "calc":
             results[qid] = evaluate_calc(q, user_ans)
        elif qtype in ["table", "table_wordbank", "journal"]:
             results[qid] = evaluate_table(q, user_ans)
        elif qtype == "typed":
             results[qid] = await evaluate_typed(q, user_ans)
             
        else:
             results[qid] = {"is_correct": False, "score": 0.0, "max_score": float(q.get("marks", 1.0)), "feedback": f"Unsupported manual grading for type: {qtype}"}
             
        total_score += results[qid]["score"]
        max_score += results[qid]["max_score"]

    return MarkingResponse(
        total_score=total_score,
        max_score=max_score,
        results=results
    )
