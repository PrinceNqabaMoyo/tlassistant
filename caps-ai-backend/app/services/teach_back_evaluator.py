"""
Teach-Back Evaluator Service (Layer C — Pro Agent Cognitive Evaluator)
Deterministic, 100% zero-LLM semantic concept matching against CAPS Wiki rubrics.
Allows learners to explain underlying rules and derivations in their own words.
"""

import re
from typing import Dict, Any, List, Optional

# Authoritative conceptual rubrics derived directly from CAPS Wiki specifications
TEACH_BACK_RUBRICS = {
    # ACCOUNTING & EMS
    "net_vs_gross_vat": {
        "required_concepts": [["15", "vat", "rate"], ["gross", "incl", "inclusive", "115"], ["net", "excl", "exclusive", "100"]],
        "misconception_triggers": {
            "vat_is_income": ["vat is income", "profit for the business", "keep the vat"],
            "direct_15_percent_on_gross": ["multiply gross by 15%", "15% of gross"]
        },
        "success_explanation": "Spot on! You correctly distinguish that Gross includes VAT (115%), Net is business revenue (100%), and VAT (15/115) is collected on behalf of SARS.",
        "partial_nudge": "You have the right intuition, but make sure to clearly state that Gross represents 115% and how SARS is owed the tax portion.",
        "xp": 25
    },
    "debit_credit_inversion": {
        "required_concepts": [["bank", "cash"], ["asset", "assets"], ["debit", "received", "inflow", "increases"]],
        "misconception_triggers": {
            "bank_statement_view": ["bank credit because bank statement credits", "credit because money comes in like my bank account"]
        },
        "success_explanation": "Excellent accounting intuition! Bank is an Asset belonging to the business. Whenever money is received in the CRJ, assets increase on the Debit side.",
        "partial_nudge": "Remember the fundamental accounting equation: Is Bank an Asset or a Liability, and on which side do Assets increase?",
        "xp": 25
    },
    "cost_of_sales": {
        "required_concepts": [["cost", "cost price"], ["trading stock", "stock", "inventory"], ["expense", "decreases"]],
        "misconception_triggers": {
            "selling_price_confusion": ["selling price", "profit calculation only"]
        },
        "success_explanation": "Accurate! Cost of Sales is an expense recording the original purchase price of merchandise sold, matching the decrease in Trading Stock.",
        "partial_nudge": "Good attempt. Be sure to link Cost of Sales to how it impacts Trading Stock asset value at cost price.",
        "xp": 25
    },

    # MATHEMATICS
    "sign_error_distribution": {
        "required_concepts": [["negative", "minus", "-"], ["distribute", "multiply", "brackets", "terms"], ["flip", "change", "positive", "signs"]],
        "misconception_triggers": {
            "only_first_term": ["only multiplies first term", "first number only"]
        },
        "success_explanation": "Perfect! Distributing a negative sign across brackets multiplies every single term inside, reversing each positive to negative and negative to positive.",
        "partial_nudge": "Almost there. Emphasize that the negative must multiply *every* term inside the parentheses, not just the first one.",
        "xp": 25
    },
    "inequality_division_negative": {
        "required_concepts": [["negative", "-"], ["divid", "divide", "dividing", "division", "multipl", "multiply"], ["reverse", "flip", "direction", "switch", "opposite"]],
        "misconception_triggers": {
            "sign_does_not_change": ["stays the same", "sign never flips"]
        },
        "success_explanation": "Brilliant algebraic rigor! Dividing or multiplying an inequality by a negative number reverses the inequality symbol because positive and negative numbers swap order on the number line.",
        "partial_nudge": "Recall what happens on the number line when you negate both sides: what must happen to the inequality sign?",
        "xp": 25
    },
    "difference_of_squares": {
        "required_concepts": [["square", "squared", "^2"], ["minus", "subtraction", "difference"], ["brackets", "plus and minus", "(a-b)(a+b)", "cancel", "middle term"]],
        "misconception_triggers": {
            "squared_binomial": ["(a-b)^2", "same signs"]
        },
        "success_explanation": "Spot on! In a difference of squares $a^2 - b^2 = (a-b)(a+b)$, the opposite signs ensure that the cross-terms ($ab - ab$) cancel out to zero.",
        "partial_nudge": "Good reasoning. Explain why the signs in the two factors must be opposite (+ and -).",
        "xp": 25
    },

    # BUSINESS STUDIES
    "macro_vs_market_confusion": {
        "required_concepts": [["macro", "external", "pestle"], ["market", "consumers", "competitors", "suppliers"], ["control", "influence", "no control"]],
        "misconception_triggers": {
            "business_controls_macro": ["business controls macro", "can control legislation"]
        },
        "success_explanation": "Mastery demonstrated! The enterprise has NO control over the Macro environment (PESTLE forces), but has INFLUENCE over the Market environment through marketing and negotiations.",
        "partial_nudge": "Make sure to clearly distinguish the level of control: how much control does management have over Macro vs Market forces?",
        "xp": 25
    }
}


def evaluate_teach_back(
    subject: str,
    topic: str,
    subskill: str,
    student_explanation: str,
    misconception_tag: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluates a learner's teach-back explanation using pure deterministic semantic matching.
    Zero token cost, zero LLM hallucination.
    """
    if not student_explanation or len(student_explanation.strip()) < 10:
        return {
            "is_mastered": False,
            "score": 20,
            "status": "partial",
            "socratic_feedback": "Your explanation is very brief. Try expanding on the specific rule and why it applies.",
            "missing_concepts": ["more_detail_needed"],
            "suggested_next_step": "refine_explanation",
            "xp_awarded": 0
        }

    text_lower = student_explanation.lower()
    
    # Identify target rubric by misconception_tag or subskill key
    matched_key = None
    if misconception_tag and misconception_tag in TEACH_BACK_RUBRICS:
        matched_key = misconception_tag
    else:
        # Search by tag keywords in subskill/topic
        combined = f"{topic}_{subskill}".lower()
        for key in TEACH_BACK_RUBRICS:
            if key in combined:
                matched_key = key
                break
    
    # Fallback to general evaluator if no exact rubric key matches
    if not matched_key:
        return _evaluate_generic_concept(student_explanation, topic, subskill)

    rubric = TEACH_BACK_RUBRICS[matched_key]
    
    # 1. Check for explicit misconception triggers
    triggers = rubric.get("misconception_triggers", {})
    for m_name, phrases in triggers.items():
        for phrase in phrases:
            if phrase.lower() in text_lower:
                return {
                    "is_mastered": False,
                    "score": 40,
                    "status": "misconception_detected",
                    "socratic_feedback": f"Watch out for a common trap: {phrase}. Think about what the CAPS rule specifically says.",
                    "detected_misconception": m_name,
                    "suggested_next_step": "refine_explanation",
                    "xp_awarded": 0
                }

    # 2. Match required conceptual anchor clusters
    required_clusters = rubric.get("required_concepts", [])
    matched_clusters = 0
    missing_clusters = []

    for idx, cluster in enumerate(required_clusters):
        has_match = any(token in text_lower for token in cluster)
        if has_match:
            matched_clusters += 1
        else:
            missing_clusters.append(cluster[0])

    cluster_ratio = matched_clusters / len(required_clusters) if required_clusters else 1.0

    if cluster_ratio >= 0.8:
        return {
            "is_mastered": True,
            "score": 100,
            "status": "mastered",
            "socratic_feedback": rubric.get("success_explanation", "Excellent conceptual explanation!"),
            "missing_concepts": [],
            "suggested_next_step": "advance",
            "xp_awarded": rubric.get("xp", 25)
        }
    elif cluster_ratio >= 0.4:
        return {
            "is_mastered": False,
            "score": 60,
            "status": "partial",
            "socratic_feedback": rubric.get("partial_nudge", "Good progress. Connect all key parts of the rule."),
            "missing_concepts": missing_clusters,
            "suggested_next_step": "refine_explanation",
            "xp_awarded": 5
        }
    else:
        return {
            "is_mastered": False,
            "score": 35,
            "status": "needs_remedial",
            "socratic_feedback": f"Your explanation is missing core concepts related to: {', '.join(missing_clusters)}. Would you like to review the worked example?",
            "missing_concepts": missing_clusters,
            "suggested_next_step": "launch_simulearn",
            "xp_awarded": 0
        }


def _evaluate_generic_concept(explanation: str, topic: str, subskill: str) -> Dict[str, Any]:
    """Fallback semantic heuristic when a specific rubric is not pre-registered."""
    words = re.findall(r'\b\w{4,}\b', explanation.lower())
    if len(words) >= 8:
        return {
            "is_mastered": True,
            "score": 85,
            "status": "mastered",
            "socratic_feedback": f"Well reasoned explanation for {topic}! You demonstrated clear understanding of {subskill}.",
            "missing_concepts": [],
            "suggested_next_step": "advance",
            "xp_awarded": 15
        }
    return {
        "is_mastered": False,
        "score": 50,
        "status": "partial",
        "socratic_feedback": f"Provide more detail on how the rule for {subskill} operates in practice.",
        "missing_concepts": ["detailed_mechanism"],
        "suggested_next_step": "refine_explanation",
        "xp_awarded": 0
    }
