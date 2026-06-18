import os
import random
import uuid
import sys
from typing import Any, Dict, List, Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils.bs_namelist import get_random_scenario, get_random_issue
from app.utils.hints_schema import build_tiered_hints

# --- Archetype Builders ---
def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"

def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("bs_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "hints": hints or [],
        "expected_answer_type": "mcq",
    }

def _make_typed(*, prompt: str, sample_answer: str, hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Generates a text-based freeform response archetype."""
    return {
        "id": _make_id("bs_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "hints": hints or [],
        "expected_answer_type": "text",
    }

def _make_matching(*, prompt: str, term_column: List[str], definition_column: List[str], correct_pairs: Dict[str, str], hints: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Generates a matching column archetype (common in BS Control Tests)."""
    return {
        "id": _make_id("bs_matching"),
        "question_type": "matching",
        "prompt": prompt,
        "term_column": term_column,
        "definition_column": definition_column,
        "correct_pairs": correct_pairs,
        "hints": hints or [],
        "expected_answer_type": "matching",
    }

# --- Hybrid Generation Logic ---
def _fetch_random_concept_from_wiki(grade: str, topic: str) -> str:
    """Reads a random concept paragraph from the caps-wiki to serve as the question basis."""
    wiki_path = os.path.join(os.path.dirname(__file__), '..', 'caps-wiki', 'business-studies', f'grade-{grade}', f'{topic}.md')
    if not os.path.exists(wiki_path):
        return "Business Environments involve Micro, Market, and Macro factors."
        
    with open(wiki_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Very simplistic split by paragraphs for hybrid generation
    paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
    return random.choice(paragraphs) if paragraphs else "Business Environments."

def generate_macro_environment_question(grade: int = 10, assessment_type: str = "activity") -> Dict[str, Any]:
    """Generates a dynamic question based on the Macro Environment."""
    scenario = get_random_scenario()
    issue = get_random_issue("macro")
    
    prompt = f"Case Study: {scenario['business_name']} is a {scenario['business_type']} in {scenario['city']} selling {scenario['product']}. Recently, they have faced a major challenge: {issue}."
    
    # Hybrid: Read actual curriculum notes to enforce the answer standard
    concept_note = _fetch_random_concept_from_wiki(str(grade), "business-environments")
    
    if assessment_type == "activity":
        # Generate an MCQ
        question_text = f"{prompt}\n\nWhich business environment does this challenge belong to?"
        options = ["Micro Environment", "Market Environment", "Macro Environment"]
        hints = build_tiered_hints(
            nudge="Does the business have any control over this challenge?",
            concept=f"Caps Note: {concept_note[:100]}...",
            breakdown=f"{scenario['business_name']} cannot control {issue}. Therefore it is external."
        )
        return _make_mcq(prompt=question_text, options=options, correct_index=2, explanation="Macro issues are completely outside the business's control.", hints=hints)
    
    else:
        # Generate a Typed Response (Consolidation/Test)
        question_text = f"{prompt}\n\nIdentify the business environment affected by this challenge, and state whether {scenario['owner_name']} has any control over it."
        sample_answer = f"This belongs to the Macro Environment. {scenario['owner_name']} has absolutely no control over {issue}."
        hints = build_tiered_hints(
            nudge="Remember the 3 levels of control: full, partial, and no control.",
            concept="The Macro environment operates at national/global levels where individual businesses have no control.",
            breakdown="Who is causing the issue? If it's the government or global events, it's Macro."
        )
        return _make_typed(prompt=question_text, sample_answer=sample_answer, hints=hints)
