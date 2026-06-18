import os
import random
import uuid
from typing import Any, Dict, List, Optional
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils.ems_namelist import get_ems_scenario, get_random_need_and_want
from app.utils.hints_schema import build_tiered_hints

def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"

def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("ems_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "hints": hints or [],
        "expected_answer_type": "mcq",
    }

def _make_typed(*, prompt: str, sample_answer: str, hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("ems_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "hints": hints or [],
        "expected_answer_type": "text",
    }

def _make_calc(*, prompt: str, correct_value: float, unit: str = "", hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("ems_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(correct_value),
        "unit": unit,
        "hints": hints or [],
        "expected_answer_type": "number",
    }

# Example of a Grade 7 Hybrid Generator (Uses Namelist to generate a dynamic scenario)
def generate_needs_and_wants_question(difficulty: str = "easy") -> Dict[str, Any]:
    """Generates a scenario-based question about Needs vs Wants (EMS Gr 7)."""
    scenario = get_ems_scenario()
    nw = get_random_need_and_want()
    
    # Randomly test either a need or a want
    if random.choice([True, False]):
        item = nw["need"]
        is_need = True
    else:
        item = nw["want"]
        is_need = False

    prompt = f"{scenario['entrepreneur']} runs a small tuck shop in {scenario['area']}. They are considering spending their profit on {item}. Is this considered a 'Need' or a 'Want' in economic terms?"
    
    options = ["Need", "Want"]
    correct_idx = 0 if is_need else 1
    explanation = f"A {item} is a {'basic requirement for survival (Need)' if is_need else 'desire that is not essential for survival (Want)'}."
    
    hints = build_tiered_hints(
        nudge="Think about whether this item is essential to live.",
        concept="A Need is essential for survival (like food or shelter), whereas a Want is a luxury or desire.",
        breakdown=f"Can {scenario['entrepreneur']} survive without {item}?"
    )

    return _make_mcq(
        prompt=prompt,
        options=options,
        correct_index=correct_idx,
        explanation=explanation,
        hints=hints
    )
