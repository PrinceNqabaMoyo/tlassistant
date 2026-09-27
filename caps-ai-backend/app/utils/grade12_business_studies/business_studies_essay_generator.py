"""Grade 12 Business Studies — Section C 40-Mark Essay Generator (Deterministic).
Implements authentic CAPS Section C Examination benchmarks:
- LASO Rubric (Layout: 2, Analysis: 2, Synthesis: 2, Originality: 2) + 32 Content marks = 40 Marks Total.
- Full 6-Pillar Contract with atomic sub-drills for adaptive progression.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


ESSAY_ARCHETYPES = [
    {
        "id": "essay_bbbee_legislation",
        "topic": "Impact of Recent Legislation",
        "title": "Broad-Based Black Economic Empowerment (B-BBEE) Act & Business Strategies",
        "term": 1,
        "caps_weight_percent": 33,
        "suggested_duration_mins": 35,
        "scenario": "Zamani Manufacturing Ltd is a large industrial parts supplier seeking to renew government contracts.",
        "prompt": (
            "Write an in-depth essay (Section C examination standard) addressing the following aspects of the B-BBEE Act:\n\n"
            "• Outline the purpose of the Broad-Based Black Economic Empowerment Act (B-BBEE).\n"
            "• Discuss the impact (advantages and disadvantages) of B-BBEE on large businesses.\n"
            "• Explain the following FIVE pillars of the B-BBEE scorecard:\n"
            "   - Management Control\n"
            "   - Skills Development\n"
            "   - Enterprise and Supplier Development (ESD)\n"
            "   - Socio-Economic Development\n"
            "   - Ownership\n"
            "• Advise Zamani Manufacturing on ways in which they can comply with the Skills Development pillar."
        ),
        "structure_subheadings": [
            "Introduction",
            "Purpose of the B-BBEE Act",
            "Impact of B-BBEE on Large Businesses",
            "Five Pillars of the B-BBEE Scorecard",
            "Strategies for Compliance with Skills Development",
            "Conclusion"
        ],
        "content_rubric": [
            {"criterion": "Purpose of B-BBEE", "max_marks": 8, "key_concepts": ["redress historical imbalances", "broad-based economic participation", "empower women and youth", "accelerate economic growth"]},
            {"criterion": "Impact of B-BBEE (Positives & Negatives)", "max_marks": 10, "key_concepts": ["secures government tenders", "improves business image", "high compliance and administrative costs", "ownership dilution risk"]},
            {"criterion": "Five Scorecard Pillars", "max_marks": 12, "key_concepts": ["management control voting rights", "skills development learnerships", "preferential procurement from black-owned QSEs/EMEs", "supplier development grants", "socio-economic community investments"]},
            {"criterion": "Skills Development compliance advice", "max_marks": 6, "key_concepts": ["1% payroll skills development levy", "registered learnership programs", "internships for unemployed youth", "mandatory workplace skills plan WSP"]},
        ],
        "elementary_drills": {
            "pillar_match": {
                "prompt": "Match the business initiative to the correct B-BBEE scorecard pillar:",
                "pairs": [
                    ("Appointing black women as senior executive directors", "Management Control"),
                    ("Funding accredited technical learnerships for employees", "Skills Development"),
                    ("Purchasing raw materials from 51% black-owned local manufacturers", "Enterprise & Supplier Development"),
                    ("Donating computers and bursaries to a local community school", "Socio-Economic Development"),
                ]
            }
        }
    },
    {
        "id": "essay_macro_strategies",
        "topic": "Macro Environment & Strategic Responses",
        "title": "PESTLE Analysis & Strategic Management Formulation",
        "term": 1,
        "caps_weight_percent": 33,
        "suggested_duration_mins": 35,
        "scenario": "Metro Logistics operates a national transport fleet facing fuel volatility and technological disruption.",
        "prompt": (
            "Write an authentic Section C exam essay addressing strategic management in the macro environment:\n\n"
            "• Outline the strategic management process.\n"
            "• Explain how the following PESTLE factors impact modern logistics enterprises:\n"
            "   - Economic (inflation, fuel costs, interest rates)\n"
            "   - Technological (automated fleet tracking, AI route optimization)\n"
            "   - Environmental / Physical (carbon emissions, extreme weather events)\n"
            "• Discuss THREE types of integration strategies (Forward, Backward, Horizontal).\n"
            "• Recommend practical strategies Metro Logistics can implement to mitigate economic instability."
        ),
        "structure_subheadings": [
            "Introduction",
            "The Strategic Management Process",
            "PESTLE Factors and Business Impact",
            "Evaluation of Integration Strategies",
            "Recommendations for Economic Risk Mitigation",
            "Conclusion"
        ],
        "content_rubric": [
            {"criterion": "Strategic Management Process", "max_marks": 8, "key_concepts": ["vision and mission review", "environmental scanning SWOT/PESTLE", "strategy formulation", "strategy implementation", "strategy evaluation"]},
            {"criterion": "PESTLE Analysis Factors", "max_marks": 12, "key_concepts": ["interest rates increase borrowing costs", "fuel inflation erodes operating margins", "telematics improve asset turnover", "carbon taxes increase regulatory compliance"]},
            {"criterion": "Integration Strategies", "max_marks": 10, "key_concepts": ["forward integration takes over distribution", "backward integration secures supply of fuel/spares", "horizontal integration merges with competitors"]},
            {"criterion": "Mitigation Recommendations", "max_marks": 6, "key_concepts": ["bulk fuel hedging contracts", "driver eco-training", "fleet right-sizing"]},
        ],
        "elementary_drills": {
            "strategy_match": {
                "prompt": "Identify whether the strategic move is Forward, Backward, or Horizontal Integration:",
                "pairs": [
                    ("A courier company purchases an automotive maintenance workshop that services its vans", "Backward Integration"),
                    ("A furniture factory opens its own retail showroom stores in shopping malls", "Forward Integration"),
                    ("A freight logistics firm buys out a competing courier business in the same province", "Horizontal Integration"),
                ]
            }
        }
    },
    {
        "id": "essay_human_resources",
        "topic": "Human Resources Function",
        "title": "Authentic Selection Procedures & Employment Legislation",
        "term": 1,
        "caps_weight_percent": 33,
        "suggested_duration_mins": 35,
        "scenario": "Apex Financial Services is recruiting 20 regional portfolio managers.",
        "prompt": (
            "Write a comprehensive Section C essay on the Human Resources function:\n\n"
            "• Explain the difference between job analysis, job description, and job specification.\n"
            "• Critically evaluate internal vs. external recruitment.\n"
            "• Detail the selection procedure that Apex Financial Services must follow to appoint candidates ethically.\n"
            "• Highlight the legal requirements of an employment contract according to the BCEA."
        ),
        "structure_subheadings": [
            "Introduction",
            "Job Analysis, Description, and Specification",
            "Evaluation of Internal vs External Recruitment",
            "Step-by-Step Ethical Selection Procedure",
            "Legal Provisions of an Employment Contract (BCEA)",
            "Conclusion"
        ],
        "content_rubric": [
            {"criterion": "Job Analysis distinction", "max_marks": 6, "key_concepts": ["job description duties and working conditions", "job specification minimum qualifications and competencies"]},
            {"criterion": "Internal vs External recruitment evaluation", "max_marks": 10, "key_concepts": ["internal boosts staff morale and lower cost", "internal creates jealousy", "external brings fresh ideas and skills", "external recruitment is costly"]},
            {"criterion": "Selection Procedure", "max_marks": 12, "key_concepts": ["screening CVs against criteria", "shortlisting candidates", "conducting interviews", "reference and background checks", "offer letter and medical/credit vetting"]},
            {"criterion": "Employment contract provisions (BCEA)", "max_marks": 8, "key_concepts": ["working hours 45h per week", "annual leave 21 consecutive days", "overtime remuneration rates", "termination notice periods"]},
        ],
        "elementary_drills": {
            "hr_match": {
                "prompt": "Classify the statement as Job Description, Job Specification, or Contract Provision:",
                "pairs": [
                    ("Candidate must possess a BCom Honours degree and 3 years auditing experience", "Job Specification"),
                    ("Responsible for preparing monthly bank reconciliations and VAT returns", "Job Description"),
                    ("Employee entitled to 21 consecutive days paid annual leave per cycle", "Contract Provision"),
                ]
            }
        }
    }
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Essay Structure Skeleton (LASO Layout marks)
# --------------------------------------------------------------------------- #
def _build_structure_drill(r: random.Random) -> Dict[str, Any]:
    archetype = r.choice(ESSAY_ARCHETYPES)
    subheadings = archetype["structure_subheadings"]
    
    return {
        "id": f"bs_essay_struct_{r.randint(100000, 999999)}",
        "topic": archetype["topic"],
        "subskill": "elementary_structure_outline",
        "mode": "elementary_structure_outline",
        "term": archetype["term"],
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "prompt": (
            f"Under CAPS Section C guidelines, an authentic 40-mark essay requires a structured layout to earn LASO marks.\n\n"
            f"For the essay topic: **{archetype['title']}**, arrange the standard subheadings into the correct chronological order:\n"
            + "\n".join(f"- {sh}" for sh in r.sample(subheadings, len(subheadings)))
        ),
        "ideal_answer": " -> ".join(subheadings),
        "sample_answer": "\n".join(f"{i+1}. {sh}" for i, sh in enumerate(subheadings)),
        "marks": 4,
        "misconception_tags": ["omitted_introduction_conclusion", "unstructured_body_paragraphs"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Introduction at beginning", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Logical body headings sequence", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Conclusion at end", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "1_nudge": "Always begin with Introduction and end with Conclusion.",
            "2_concept": "The body headings should directly map to the bullet points of the exam question prompt.",
            "3_breakdown": "Correct order: " + " -> ".join(subheadings)
        }
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Concept Matching
# --------------------------------------------------------------------------- #
def _build_concept_match_drill(r: random.Random) -> Dict[str, Any]:
    archetype = ESSAY_ARCHETYPES[0] # B-BBEE
    drill = archetype["elementary_drills"]["pillar_match"]
    pairs = drill["pairs"]
    r.shuffle(pairs)

    return {
        "id": f"bs_pillar_match_{r.randint(100000, 999999)}",
        "topic": archetype["topic"],
        "subskill": "elementary_legislation_matching",
        "mode": "elementary_legislation_matching",
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "prompt": (
            f"{drill['prompt']}\n\n"
            + "\n".join(f"{i+1}. {p[0]} -> [{p[1]}]" for i, p in enumerate(pairs))
        ),
        "ideal_answer": "; ".join(f"{p[0]} -> {p[1]}" for p in pairs),
        "sample_answer": "; ".join(f"{p[0]} -> {p[1]}" for p in pairs),
        "marks": 4,
        "misconception_tags": ["macro_vs_market_confusion", "confused_bbbee_pillars"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Correct match for {p[1]}", "marks": 1, "editable": True}
                for i, p in enumerate(pairs)
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "1_nudge": "Look at the core focus: leadership/directors (Management Control) vs external training (Skills Development).",
            "2_concept": "B-BBEE pillars evaluate distinct operational spheres: ownership, management, skills, procurement/suppliers, and community.",
            "3_breakdown": "; ".join(f"{p[0]} = {p[1]}" for p in pairs)
        }
    }


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Authentic 40-Mark Section C Essay
# --------------------------------------------------------------------------- #
def _build_compound_essay(r: random.Random) -> Dict[str, Any]:
    archetype = r.choice(ESSAY_ARCHETYPES)

    laso_breakdown = [
        {"dimension": "Layout (L)", "marks": 2, "desc": "Introduction, body subheadings, and conclusion present (at least 2 subheadings with content)."},
        {"dimension": "Analysis (A)", "marks": 2, "desc": "Addresses all parts of the essay prompt in depth (candidate scores at least 50% in all sub-questions)."},
        {"dimension": "Synthesis (S)", "marks": 2, "desc": "Arguments are synthesized into sound business recommendations and evaluative judgments."},
        {"dimension": "Originality (O)", "marks": 2, "desc": "Cites realistic business examples, recent market dynamics, and current trends."},
    ]

    marking_points = [
        {"id": "laso_layout", "desc": "Layout (L): Intro, proper body headings, and conclusion", "marks": 2, "editable": True},
        {"id": "laso_analysis", "desc": "Analysis (A): In-depth treatment of all question facets", "marks": 2, "editable": True},
        {"id": "laso_synthesis", "desc": "Synthesis (S): Well-reasoned evaluations & recommendations", "marks": 2, "editable": True},
        {"id": "laso_originality", "desc": "Originality (O): Contemporary examples & business insight", "marks": 2, "editable": True},
    ]

    for item in archetype["content_rubric"]:
        marking_points.append({
            "id": f"content_{item['criterion'].lower().replace(' ', '_')[:16]}",
            "desc": f"Content: {item['criterion']} (Key concepts: {', '.join(item['key_concepts'])})",
            "marks": item["max_marks"],
            "editable": True
        })

    marking_schema = {
        "total_marks": 40,
        "laso_marks": 8,
        "content_marks": 32,
        "laso_breakdown": laso_breakdown,
        "marking_points": marking_points,
        "deductions": [{"rule": "omitted_subheadings", "penalty": -2}],
        "carry_forward_rule": "rubric_holistic"
    }

    sample_essay_outline = (
        f"### SAMPLE MEMORANDUM OUTLINE (40 MARKS)\n\n"
        f"**1. INTRODUCTION (2 marks)**\n"
        f"- Define the core topic and context: {archetype['scenario']}\n\n"
        f"**2. BODY SECTIONS (Max 32 Content Marks)**\n"
        + "\n".join(
            f"**{c['criterion']} (Max {c['max_marks']} marks):**\n"
            + "\n".join(f"  • {concept}" for concept in c["key_concepts"])
            for c in archetype["content_rubric"]
        )
        + f"\n\n**3. CONCLUSION (2 marks)**\n"
        f"- Meaningful summary connecting strategic compliance to sustainable competitive advantage.\n\n"
        f"**4. LASO RUBRIC ASSESSMENT (8 marks)**\n"
        f"- Layout: 2/2 | Analysis: 2/2 | Synthesis: 2/2 | Originality: 2/2."
    )

    return {
        "id": f"bs_secC_{r.randint(100000, 999999)}",
        "topic": archetype["topic"],
        "subskill": "section_c_essay_40_marks",
        "mode": "compound",
        "difficulty": "hard",
        "term": archetype["term"],
        "caps_weight_percent": 33,
        "suggested_duration_mins": 35,
        "prompt": (
            f"### SECTION C: ESSAY QUESTION (40 MARKS)\n\n"
            f"**Context / Scenario:** {archetype['scenario']}\n\n"
            f"{archetype['prompt']}\n\n"
            f"*Your essay will be evaluated using the official CAPS LASO Rubric (Layout: 2, Analysis: 2, Synthesis: 2, Originality: 2) and Content: 32 marks.*"
        ),
        "ideal_answer": sample_essay_outline,
        "sample_answer": sample_essay_outline,
        "marks": 40,
        "misconception_tags": ["omitted_subheadings_essay", "superficial_analysis_no_synthesis", "confused_legislation_principles"],
        "marking_schema": marking_schema,
        "hints": {
            "1_nudge": "Always write in full essay format with an Introduction, distinct subheadings for each question bullet, and a Conclusion.",
            "2_concept": "To maximize Content marks, provide two complete facts per bullet point (2 marks per valid statement). Address all four prompts to secure Analysis marks.",
            "3_breakdown": f"Structure: {', '.join(archetype['structure_subheadings'])}. Focus on distinct, high-impact facts for each pillar or strategy."
        }
    }


# --------------------------------------------------------------------------- #
# Public Generator Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_essay,
    "elementary_structure_outline": _build_structure_drill,
    "elementary_legislation_matching": _build_concept_match_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Business Studies 40-Mark Section C essays."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_essay)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
