"""Grade 10 Business Studies - Term 4 - Relationships & team performance.

Deterministic generator (no LLM). Content grounded from the CAPS textbook topic
"Relationships and team performance" (curriculum_docs_auto/
BusinessStudies_Gr10/Term 4/04. Relationships & team performance.md).

Uses the shared `_bs_entropy` module to expand a compact fact base into many
deterministic archetype variants (see _bs_entropy for the combinatorics).
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_typed
from .._bs_entropy import expand_fact_base

PREFIX = "g10bs_relationships"
VAID = "relationships_team_performance"

FACTS: List[Dict[str, Any]] = [
    {"stem": "A group of two or more people who work together in a business to achieve a common goal is called a …",
     "correct": "team", "distractors": ["competitor", "supplier", "auditor", "manager", "shareholder"],
     "explanation": "A team consists of two or more people who work together in a business or organisation to achieve a common goal."},
    {"stem": "The connection between employees, colleagues, customers and suppliers is referred to as a …",
     "correct": "relationship", "distractors": ["transaction", "budget", "merger", "contract"],
     "explanation": "A relationship is the connection between employees, colleagues, customers and suppliers."},
    {"stem": "A preconceived opinion or judgement of someone, normally NOT based on reason or fact, is …",
     "correct": "prejudice", "distractors": ["equity", "diversity", "productivity", "openness"],
     "explanation": "Prejudice is a preconceived opinion or judgement, normally not based on reason or fact, and can lead to discrimination."},
    {"stem": "Treating an employee unfairly because of race, gender, religion or disability is called …",
     "correct": "discrimination", "distractors": ["equity", "collaboration", "openness", "prejudice"],
     "explanation": "Discrimination occurs when prejudice results in an employee being treated unfairly because of race, gender, sexuality, religion or disability."},
    {"stem": "The practice of being fair or impartial in the workplace, achieved when there is no discrimination, is …",
     "correct": "equity", "distractors": ["profit", "prejudice", "efficiency", "synergy"],
     "explanation": "Equity is the practice of being fair or impartial in the workplace; equity is achieved when there is no discrimination."},
    {"stem": "What makes people unique - different cultures, backgrounds, beliefs, gender, language and life experiences - is …",
     "correct": "diversity", "distractors": ["equity", "synergy", "leadership", "productivity"],
     "explanation": "Diversity is what makes people unique and includes different cultures, backgrounds, beliefs, gender, language and life experiences."},
    {"stem": "The financial advantage or benefit earned by a business is its …",
     "correct": "profit", "distractors": ["productivity", "service", "revenue", "cash flow"],
     "explanation": "Profit is the financial advantage or benefit a business earns; it is one of the key business objectives."},
    {"stem": "A way to measure how efficiently a business produces goods or services is …",
     "correct": "productivity", "distractors": ["prejudice", "diversity", "trust", "equity"],
     "explanation": "Productivity is a way to measure efficiency and is one of the core business objectives."},
    {"stem": "The beliefs, philosophies and principles that guide and drive a business are its …",
     "correct": "core values", "distractors": ["assets", "liabilities", "competitors", "products"],
     "explanation": "Values are the beliefs, philosophies and principles that drive a business - the core values that guide it."},
    {"stem": "Business objectives must be SMART. The 'M' in SMART means the objective must be …",
     "correct": "measurable", "distractors": ["managerial", "motivating", "mandatory", "memorable"],
     "explanation": "SMART objectives are Specific, Measurable, Attainable, Relevant and Timely."},
    {"stem": "The relationship between two employees working at the same place is called a/an … relationship.",
     "correct": "interpersonal", "distractors": ["international", "interdepartmental", "intergenerational", "intranet"],
     "explanation": "An interpersonal relationship is the relationship between two employees working at the same place."},
    {"stem": "When employees enjoy a culture of honesty and psychological safety, the team has …",
     "correct": "mutual trust", "distractors": ["prejudice", "conflict", "turnover", "distance"],
     "explanation": "Mutual trust exists when employees enjoy a culture of honesty and psychological safety."},
    {"stem": "An activity delivered by the business to a customer or another department is …",
     "correct": "service", "distractors": ["profit", "product", "revenue", "surplus"],
     "explanation": "Service is an activity delivered by the business to another party such as a customer or another department."},
    {"stem": "The action of working with someone to produce something is called …",
     "correct": "collaboration", "distractors": ["competition", "separation", "delegation", "outsourcing"],
     "explanation": "Collaboration is the action of working with someone to produce something together."},
    {"stem": "The quality of being relatively free from obstruction and encouraging open communication is …",
     "correct": "openness", "distractors": ["secrecy", "control", "distance", "hierarchy"],
     "explanation": "Openness is the quality of being free from obstruction, allowing information to flow between team members."},
    {"stem": "Extreme anxiety that can be created by poor relationships in a team is called …",
     "correct": "distress", "distractors": ["motivation", "satisfaction", "synergy", "profit"],
     "explanation": "Distress is extreme anxiety that can result from poor relationships and can lead to withdrawal from a team."},
    {"stem": "Stopping participation in a team because of poor relationships is best described as …",
     "correct": "withdrawal", "distractors": ["initiative", "commitment", "engagement", "consensus"],
     "explanation": "Withdrawal means to stop participating in a team - it can result from distress caused by poor relationships."},
    {"stem": "Racism, xenophobia, sexism and religious prejudice are all examples of …",
     "correct": "prejudice", "distractors": ["diversity", "equity", "productivity", "synergy"],
     "explanation": "Racism, xenophobia, sexism and religious prejudice are forms of prejudice that can lead to discrimination."},
]

PAIRS: List[Dict[str, str]] = [
    {"term": "team", "defn": "Two or more people working together towards a common goal"},
    {"term": "relationship", "defn": "The connection between employees, colleagues, customers and suppliers"},
    {"term": "prejudice", "defn": "A preconceived opinion or judgement not based on reason or fact"},
    {"term": "discrimination", "defn": "Unfair treatment because of race, gender, religion or disability"},
    {"term": "equity", "defn": "Being fair or impartial in the workplace"},
    {"term": "diversity", "defn": "What makes people unique - cultures, beliefs, gender, language, experiences"},
    {"term": "profit", "defn": "The financial advantage or benefit earned by a business"},
    {"term": "productivity", "defn": "A measure of efficiency or output"},
    {"term": "service", "defn": "An activity delivered by the business to a customer or another department"},
    {"term": "interpersonal", "defn": "The relationship between two employees working at the same place"},
    {"term": "collaboration", "defn": "The action of working with someone to produce something"},
    {"term": "openness", "defn": "The quality of being free from obstruction in communication"},
    {"term": "distress", "defn": "Extreme anxiety caused by poor relationships"},
    {"term": "withdrawal", "defn": "Stopping participation in a team"},
    {"term": "values", "defn": "The beliefs, philosophies and principles that drive a business"},
    {"term": "beliefs", "defn": "A feeling of being sure that something is true or trustworthy"},
    {"term": "synergy", "defn": "The extra energy and output created when a team works well together"},
    {"term": "trust", "defn": "A culture of honesty and psychological safety between team members"},
    {"term": "respect", "defn": "A fundamental belief in a person's right to exist, be heard and have equal opportunity"},
    {"term": "objectives", "defn": "The detailed steps a business takes to achieve a goal"},
]

TYPED_SPECS: List[Dict[str, Any]] = [
    {"base": "the meaning of business objectives",
     "marking_points": [
         "A business objective explains in detail the steps a business will take to achieve a goal.",
         "Objectives are aligned to the vision, mission and purpose of the business.",
         "Type: Profit - the financial advantage or benefit.",
         "Type: Productivity - a measure of efficiency or output.",
         "Type: Service - an activity delivered to a customer or another department.",
     ], "marks": 6, "min_ask": 3, "max_ask": 5,
     "sample_answer": "Business objectives explain in detail the steps a business plans to take to reach a goal, aligned to its vision, mission and purpose. Three types are profit (financial benefit), productivity (measure of efficiency) and service (activity delivered to a customer or another department)."},
    {"base": "the benefits of teamwork",
     "marking_points": [
         "Team members learn from each other and grow; performance improves through support.",
         "The team achieves more than the individual (synergy).",
         "Good teamwork helps the business achieve its objectives.",
         "It improves effective communication and creates strong relationships.",
         "It encourages healthy risk-taking, creativity and a wider sense of ownership.",
         "Employees feel connected to the company which builds loyalty and job satisfaction.",
         "Teamwork increases the range of skills and raises productivity.",
         "It gives employees more control over their jobs.",
         "It reduces distress and withdrawal caused by poor relationships.",
         "Teamwork creates synergy that maximises the energy levels of employees.",
     ], "marks": 10, "min_ask": 4, "max_ask": 8,
     "sample_answer": "Teamwork lets members learn from each other, achieves more than any individual (synergy), and helps the business reach its objectives. It improves communication, builds strong relationships, encourages risk-taking, creativity and ownership, and creates loyalty and job satisfaction. It also increases the range of skills, raises productivity, gives employees more control, reduces distress and withdrawal, and maximises energy levels."},
    {"base": "how personal beliefs and values influence business relationships",
     "marking_points": [
         "Beliefs are a feeling that something is true or trustworthy; values are the principles that guide behaviour.",
         "Beliefs and values shape how people relate to colleagues, customers and suppliers.",
         "Prejudice is a preconceived judgement not based on reason or fact (e.g. racism, xenophobia, sexism).",
         "Prejudice can lead to discrimination - unfair treatment because of race, gender, religion or disability.",
         "Equity is the practice of being fair and impartial; it is achieved when there is no discrimination.",
         "Diversity is what makes people unique and must be valued for strong relationships.",
     ], "marks": 6, "min_ask": 3, "max_ask": 6,
     "sample_answer": "Beliefs and values are the principles that drive behaviour and shape workplace relationships. Prejudice is a preconceived judgement not based on fact and can lead to discrimination - unfair treatment because of race, gender, religion or disability. Equity means being fair and impartial and is achieved when there is no discrimination. Diversity is what makes people unique and valuing it strengthens relationships and team performance."},
    {"base": "the ways team members can work together to accomplish business objectives",
     "marking_points": [
         "Set clear objectives and agreed goals.",
         "Communicate with openness and share information and resources.",
         "Show mutual respect for one another.",
         "Build mutual trust, honesty and psychological safety.",
         "Support each other and commit to achieving mutual goals.",
         "Maintain sound inter-team relations.",
         "Provide individual development opportunities.",
         "Regularly review the team processes.",
     ], "marks": 8, "min_ask": 4, "max_ask": 7,
     "sample_answer": "Team members accomplish objectives by setting clear objectives and agreed goals, communicating with openness, showing mutual respect and building mutual trust. They support each other, commit to mutual goals, maintain sound inter-team relations, provide individual development opportunities and regularly review the team processes."},
    {"base": "the criteria for a successful and collaborative team",
     "marking_points": [
         "The team understands and works towards clear business objectives.",
         "Members communicate frequently and openly.",
         "There is mutual respect, trust and support among members.",
         "Roles, ground rules and team values are agreed and followed.",
         "Members cooperate and share information and resources.",
         "The team reviews its processes and improves performance and productivity.",
     ], "marks": 6, "min_ask": 3, "max_ask": 6,
     "sample_answer": "A successful, collaborative team understands and works towards clear objectives, communicates frequently and openly, and shows mutual respect, trust and support. It agrees on roles, ground rules and team values, cooperates by sharing information and resources, and reviews its processes to improve performance and productivity."},
]

ESSAY_SPECS: List[Dict[str, Any]] = [
    {"topic": "'Teamwork is essential for achieving business objectives.'",
     "ask": "refer to the benefits of teamwork, the criteria for a collaborative team, and how businesses can create an environment that enables teams to work effectively",
     "rubric": [
         {"criterion": "Meaning of teamwork and business objectives", "description": "Defines teamwork and explains business objectives (profit, productivity, service) aligned to vision/mission", "marks": 4},
         {"criterion": "Benefits of teamwork", "description": "Explains synergy, improved communication, learning, creativity, loyalty and productivity", "marks": 6},
         {"criterion": "Criteria for a collaborative team", "description": "Describes clear objectives, openness, mutual respect and trust, agreed roles and process review", "marks": 5},
         {"criterion": "Enabling environment", "description": "Suggests ways to enable effective teams: understanding objectives, ground rules, sharing information, delegation, consensus", "marks": 3},
         {"criterion": "Terminology, structure and expression", "description": "Uses correct business terminology in a clear, logical structure", "marks": 2},
     ],
     "sample_answer": "Teamwork brings people together to reach a common goal, and it is central to achieving business objectives such as profit, productivity and service. Its benefits include synergy, improved communication, learning and skill growth, creativity, healthy risk-taking, a wider sense of ownership, job satisfaction and loyalty. A successful, collaborative team works towards clear objectives, communicates openly, and is built on mutual respect, trust and support, with agreed roles, ground rules and regular review of its processes. Businesses can enable effective teams by ensuring members understand the objectives, setting ground rules and team values, encouraging listening and brainstorming, sharing information and resources, delegating problem-solving, and establishing a method for reaching consensus. Poor relationships marked by prejudice and discrimination undermine this, so equity and respect for diversity are essential. In conclusion, teamwork, underpinned by positive relationships, is essential for achieving business objectives.",
     "marks": 20, "min_words": 180, "max_words": 450},
]


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Rewrite the following vague goal as a SMART business objective: 'We want better customer service.' (4)",
            marking_points=[
                "Specific: state exactly what will be done (e.g. reduce customer complaints).",
                "Measurable: attach a figure (e.g. by 25%).",
                "Attainable/Relevant: realistic and linked to the business goal.",
                "Timely: give a deadline (e.g. within the next six months).",
            ],
            sample_answer="Decrease our customer complaints by 25% within the next six months, because good customer service helps us retain customers and generate sustained revenue.",
            marks=4, visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="A manager assigns work by gender only. Name the concept this shows and state TWO ways to correct it. (3)",
            marking_points=[
                "It shows discrimination / prejudice (unfair treatment based on gender).",
                "Correct it by applying fair, objective criteria.",
                "Ensure equity and equal opportunity for all employees.",
            ],
            sample_answer="This is discrimination (unfair treatment because of gender), which breaches equity. It should be corrected by making decisions on fair, objective criteria and giving all employees equal opportunity.",
            marks=3, visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Suggest FOUR ways a business can create an environment that enables teams to work effectively. (4)",
            marking_points=[
                "Ensure the team clearly understands the business objectives.",
                "Set ground rules and establish team values and goals.",
                "Encourage trust, respect and cooperation among members.",
                "Communicate clearly and encourage listening and brainstorming.",
            ],
            sample_answer="A business can ensure the team understands the objectives, set ground rules and team values, encourage trust, respect and cooperation, and communicate clearly while encouraging listening and brainstorming.",
            marks=4, visual_aid_key=VAID,
        ),
    ]


def _pools(r) -> Dict[str, List[Callable[[], Dict[str, Any]]]]:
    pools = expand_fact_base(
        PREFIX, VAID,
        mcq_facts=FACTS, pairs=PAIRS,
        typed_specs=TYPED_SPECS, essay_specs=ESSAY_SPECS,
        mcq_variants=6,
        matching_variants=8, matching_sizes=[5, 6, 7],
        crossword_variants=5, crossword_sizes=[6, 7, 5],
        wordbank_variants=6, wordbank_sizes=[4, 5, 6],
        typed_variants=5, essay_variants=4,
    )
    pools["application"] = _application(r)
    return pools


generate_relationships = build_generate(_pools)
