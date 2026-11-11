"""Grade 10 Business Studies - Term 4 - Self management (Topic 18).

Deterministic generator (no LLM). Content hand-authored and grounded from
curriculum_source_files/Textbook_BusinessStudies_Gr10_Self-management.pdf
(the scraped curriculum_docs_auto .md for this topic is corrupt - contains
Euclidean Geometry, not Business Studies - so we ground from the PDF instead).

Uses the shared `_bs_entropy` module to expand a compact fact base into many
deterministic archetype variants so an archetype can produce semantically
different questions from the same grounded content. See _bs_entropy for the
combinatorics (MCQ distractor rotation, matching/crossword/wordbank
sub-sampling, typed verb + subset rotation, essay lead rotation).
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_typed
from .._bs_entropy import expand_fact_base

PREFIX = "g10bs_selfmanagement"
VAID = "self_management"

# ---------------------------------------------------------------------------
# 1. MCQ fact base - grounded from the topic's key concepts + memoranda.
# ---------------------------------------------------------------------------
FACTS: List[Dict[str, Any]] = [
    {
        "stem": "Using time in the most productive way in order to complete assigned tasks is called …",
        "correct": "time management",
        "distractors": ["stress management", "self-confidence", "adaptability", "professional image", "personal SWOT"],
        "explanation": "Time management is the skill of using time in the most productive way to complete assigned tasks and work towards important goals.",
    },
    {
        "stem": "The ability to take responsibility for oneself, regulate one's actions and direct one's behaviour is …",
        "correct": "self-management",
        "distractors": ["time management", "professional image", "self-compassion", "adaptability", "goal setting"],
        "explanation": "Self-management is the ability to take responsibility for oneself, regulate one's actions and direct one's behaviour.",
    },
    {
        "stem": "A natural ability to be good at something, especially without being taught, is a …",
        "correct": "talent",
        "distractors": ["skill", "goal", "value", "interest", "attitude"],
        "explanation": "A talent is a natural ability to be good at something, especially without being taught.",
    },
    {
        "stem": "An attitude about a person's skills and abilities, where one accepts and trusts oneself, is …",
        "correct": "self-confidence",
        "distractors": ["self-discipline", "adaptability", "professional image", "self-compassion", "initiative"],
        "explanation": "Self-confidence is an attitude about a person's skills and abilities; it means accepting and trusting yourself and having a sense of control.",
    },
    {
        "stem": "The ability to accept change and to adjust to new conditions successfully is …",
        "correct": "adaptability",
        "distractors": ["productivity", "self-compassion", "initiative", "tolerance", "flexibility"],
        "explanation": "Adaptability is the ability to accept change and to adjust to new conditions successfully.",
    },
    {
        "stem": "An image that one projects about oneself based on appearance and reputation is a …",
        "correct": "professional image",
        "distractors": ["personal goal", "self-analysis", "value system", "SWOT matrix", "brand equity"],
        "explanation": "A professional image is the image one projects about oneself based on appearance and reputation.",
    },
    {
        "stem": "Any physical or emotional factor that causes bodily or mental harm is …",
        "correct": "stress",
        "distractors": ["conflict", "talent", "obstacle", "anxiety", "burnout"],
        "explanation": "Stress may be considered as any physical or emotional factor that causes bodily or mental harm.",
    },
    {
        "stem": "A personal SWOT analysis examines strengths, weaknesses, opportunities and …",
        "correct": "threats",
        "distractors": ["talents", "targets", "timeframes", "traits", "team members"],
        "explanation": "A personal SWOT analysis looks at Strengths, Weaknesses, Opportunities and Threats.",
    },
    {
        "stem": "Things you want to achieve for yourself in life are your …",
        "correct": "personal goals",
        "distractors": ["obstacles", "values", "talents", "responsibilities", "regulations"],
        "explanation": "Personal goals are things you want to achieve for yourself in life.",
    },
    {
        "stem": "The ability to turn understanding, acceptance and love inward is called …",
        "correct": "self-compassion",
        "distractors": ["self-confidence", "self-discipline", "adaptability", "initiative", "self-analysis"],
        "explanation": "Self-compassion is the ability to turn understanding, acceptance and love inward.",
    },
    {
        "stem": "The ability to control yourself and your weaknesses is …",
        "correct": "self-discipline",
        "distractors": ["self-confidence", "self-esteem", "self-analysis", "self-image", "self-management"],
        "explanation": "Self-discipline is the ability to control yourself and your weaknesses; effective time management promotes it.",
    },
    {
        "stem": "A detailed plan outlining the activities that need to be performed to reach a goal is a/an …",
        "correct": "action plan",
        "distractors": ["business plan", "job description", "budget", "mission", "vision"],
        "explanation": "An action plan is a detailed plan outlining activities that need to be performed to achieve a goal.",
    },
    {
        "stem": "Change that is certain to happen or unavoidable is described as …",
        "correct": "inevitable",
        "distractors": ["optional", "temporary", "reversible", "uncommon", "improbable"],
        "explanation": "Inevitable means certain to happen / unavoidable - accepting that change is inevitable is a way to adapt.",
    },
    {
        "stem": "Things that prevent one's progress are called …",
        "correct": "obstacles",
        "distractors": ["opportunities", "strengths", "talents", "goals", "targets"],
        "explanation": "Obstacles are things that prevent one's progress; letting go of fears and obstacles builds self-confidence.",
    },
    {
        "stem": "Which of the following is NOT one of the aspects of a balanced life taught in this topic?",
        "correct": "political",
        "distractors": ["physical", "mental", "spiritual", "social", "material"],
        "explanation": "The five aspects of a balanced life are physical, mental, spiritual, social and material; 'political' is not one.",
    },
]

# ---------------------------------------------------------------------------
# 2. Term/definition pairs (drives matching, crossword, wordbank variants).
# ---------------------------------------------------------------------------
PAIRS: List[Dict[str, str]] = [
    {"term": "time management", "defn": "Using time in the most productive way to complete assigned tasks"},
    {"term": "self-management", "defn": "The ability to take responsibility for oneself and regulate one's actions"},
    {"term": "talent", "defn": "A natural ability to be good at something without being taught"},
    {"term": "self-confidence", "defn": "An attitude about a person's skills and abilities"},
    {"term": "adaptability", "defn": "The ability to accept change and adjust to new conditions"},
    {"term": "professional image", "defn": "The image one projects based on appearance and reputation"},
    {"term": "stress", "defn": "Any physical or emotional factor causing bodily or mental harm"},
    {"term": "personal goals", "defn": "Things you want to achieve for yourself in life"},
    {"term": "self-compassion", "defn": "The ability to turn understanding, acceptance and love inward"},
    {"term": "self-discipline", "defn": "The ability to control yourself and your weaknesses"},
    {"term": "action plan", "defn": "A detailed plan outlining activities that need to be performed"},
    {"term": "obstacle", "defn": "Something that prevents one's progress"},
    {"term": "inevitable", "defn": "Certain to happen; unavoidable"},
    {"term": "SWOT", "defn": "A personal analysis of strengths, weaknesses, opportunities and threats"},
    {"term": "initiative", "defn": "The ability to act independently and take charge without being told"},
    {"term": "balance", "defn": "A successful and healthy mix of physical, mental, spiritual, social and material life"},
]

# ---------------------------------------------------------------------------
# 3. Typed / discussion specs (rotated for verb + subset-count entropy).
#    `base` = the noun phrase that follows the command verb, e.g.
#    verb + " " + base + " (marks)".
# ---------------------------------------------------------------------------
TYPED_SPECS: List[Dict[str, Any]] = [
    {
        "base": "the importance of setting goals",
        "marking_points": [
            "Goal setting helps you organise your time and resources so you live a productive, satisfying life.",
            "Setting goals gives long-term vision and short-term motivation.",
            "Setting goals lets you take control of your life and gives you direction.",
            "Goals give focus - you spend time and energy achieving exactly what you want.",
            "Goals propel you to take more action and create accountability.",
            "Goals enable you to achieve your highest potential and become the best you can be.",
            "An action plan can be created and reviewed even when things go off track.",
        ],
        "marks": 7,
        "min_ask": 3,
        "max_ask": 6,
        "sample_answer": "Setting goals organises your time and resources for a productive, satisfying life, provides long-term vision and short-term motivation, gives you direction and control, focuses your effort, propels you to act, creates accountability, and enables you to reach your highest potential. An action plan can be reviewed when things go off track.",
    },
    {
        "base": "the ways in which people can manage stress",
        "marking_points": [
            "Set aside personal time and take breaks.",
            "Develop a healthy lifestyle with a well-balanced diet.",
            "Exercise regularly.",
            "Spend time with people you enjoy or love.",
            "Have a plan so that you stay in control.",
            "Listen to music and reduce caffeine intake.",
            "Be assertive, optimistic and have a sense of humour.",
        ],
        "marks": 7,
        "min_ask": 3,
        "max_ask": 6,
        "sample_answer": "Ways to manage stress include setting aside personal time and taking breaks, developing a healthy lifestyle with a balanced diet, exercising regularly, spending time with loved ones, having a plan to stay in control, listening to music, reducing caffeine and being assertive, optimistic and humorous.",
    },
    {
        "base": "the ways in which people can adapt to change",
        "marking_points": [
            "Adapt to new learning styles and skills to make the most of opportunities.",
            "Transfer and adapt skills and resources for new tasks and situations.",
            "Avoid complaining and learn to be positive about change.",
            "Find ways to meet the challenges change brings and benefit from them.",
            "Be proactive by keeping up with changes in the world.",
            "Accept that change is inevitable.",
            "Reflect on how you have handled change in the past.",
            "Take responsibility and hold yourself accountable for adapting.",
        ],
        "marks": 8,
        "min_ask": 3,
        "max_ask": 7,
        "sample_answer": "People adapt to change by adjusting learning styles and skills, transferring skills and resources to new situations, being positive about change, meeting its challenges, keeping up proactively, accepting that change is inevitable, reflecting on past handling of change, and taking responsibility and accountability.",
    },
    {
        "base": "the importance of a professional image",
        "marking_points": [
            "It creates a good impression on others.",
            "People form ideas about who you are and what you are capable of.",
            "Being aware of your image lets you influence how others see you.",
            "Being viewed positively benefits your career, work relationships and experiences.",
            "The image a business projects helps build customer confidence.",
            "Companies with a professional image and quality service attract and retain customers.",
        ],
        "marks": 6,
        "min_ask": 3,
        "max_ask": 6,
        "sample_answer": "A professional image creates a good impression, lets you influence how others see you and gives you career and relationship benefits. A business's professional image builds customer confidence, and combined with quality service, attracts and retains customers.",
    },
    {
        "base": "the ways in which you can increase your self-confidence",
        "marking_points": [
            "Focus on your strengths rather than your weaknesses.",
            "Approach new experiences as opportunities.",
            "Do not expect perfection from yourself.",
            "Do not rely on other people's approval.",
            "Let go of fears, obstacles and personal limitations.",
            "Accept and love yourself unconditionally; practise self-compassion.",
            "Confront what you find difficult to accept about yourself.",
            "Change your perception and attitude toward yourself.",
        ],
        "marks": 8,
        "min_ask": 3,
        "max_ask": 7,
        "sample_answer": "Increase self-confidence by focusing on strengths, treating new experiences as opportunities, not demanding perfection, not depending on others' approval, letting go of fears, accepting and loving yourself unconditionally, confronting hard-to-accept facts, and changing your perception of yourself.",
    },
    {
        "base": "the ways to build your strengths and manage your weaknesses",
        "marking_points": [
            "Identify your strengths before you consider your weaknesses.",
            "Take full advantage of your strengths.",
            "Develop your skills to the maximum and push your talents as far as you can.",
            "Do not ignore talent - spend time enhancing it.",
            "Break weaknesses into those you can change and those you cannot.",
            "Set goals to fix changeable weaknesses and manage unchangeable ones.",
            "Surround yourself with people who uplift you.",
        ],
        "marks": 7,
        "min_ask": 3,
        "max_ask": 6,
        "sample_answer": "Identify strengths first and take full advantage of them; develop skills to the maximum; enhance talent; split weaknesses into changeable (set goals to fix) and unchangeable (manage); and surround yourself with uplifting people.",
    },
    {
        "base": "the ways in which employees can project a professional image",
        "marking_points": [
            "Dress appropriately for the work and the workplace.",
            "Work hard and be productive.",
            "Do more than what the job description requires.",
            "Be punctual and enthusiastic.",
            "Be friendly and accepting of colleagues.",
            "Treat everyone with respect, whether or not you like them.",
            "Avoid or manage conflict.",
            "Be courteous and professional on the telephone.",
        ],
        "marks": 8,
        "min_ask": 3,
        "max_ask": 7,
        "sample_answer": "Employees project a professional image by dressing appropriately, working hard, exceeding their job description, being punctual and enthusiastic, being friendly and accepting, treating everyone with respect, managing conflict, and being courteous on the telephone.",
    },
    {
        "base": "the ways in which a business can encourage employees to live a successful and balanced life",
        "marking_points": [
            "Advise regular medical check-ups and avoid activities that lead to stress.",
            "Encourage a positive attitude and self-reflection.",
            "Take responsibility for actions and engage in self-development programmes.",
            "Ensure proper hygiene and regular physical exercise (physical).",
            "Plan the day and activities to avoid unnecessary stress (mental).",
            "Make time every day for the religion or beliefs you practise (spiritual).",
            "Do good deeds by giving, helping and guiding others (social).",
            "Get a good education to obtain a self-supporting job (material).",
        ],
        "marks": 8,
        "min_ask": 3,
        "max_ask": 7,
        "sample_answer": "A business can advise medical check-ups and stress avoidance, encourage positive attitude and self-reflection, promote responsibility and self-development, ensure hygiene and physical exercise, plan the day to reduce stress, support spiritual practice, encourage social good deeds, and enable employees to obtain education for a self-supporting job.",
    },
]

# ---------------------------------------------------------------------------
# 4. Essay specs.
# ---------------------------------------------------------------------------
ESSAY_SPECS: List[Dict[str, Any]] = [
    {
        "topic": "'Self-management is essential for personal and business success.'",
        "ask": "refer to time management, goal setting, personal SWOT, self-confidence, stress management and adaptability",
        "rubric": [
            {"criterion": "Time management and goal setting", "description": "Defines time management and explains the importance of setting SMART goals that organise time and resources", "marks": 5},
            {"criterion": "Personal SWOT / strengths and weaknesses", "description": "Explains a personal SWOT analysis and the importance of building strengths and managing weaknesses and threats", "marks": 4},
            {"criterion": "Self-management and self-confidence", "description": "Defines self-management and self-confidence and gives concrete ways to increase them, including self-compassion and self-discipline", "marks": 4},
            {"criterion": "Stress management and adaptability", "description": "Explains stress and gives ways to manage it, then describes adaptability and ways to accept and adapt to change", "marks": 4},
            {"criterion": "Terminology, structure and expression", "description": "Uses correct business terminology in a clear introduction-body-conclusion structure", "marks": 3},
        ],
        "sample_answer": "Self-management is the ability to take responsibility for oneself and control one's thoughts, feelings and actions. It begins with time management - using time in the most productive way - and with setting SMART goals that organise time and resources. A personal SWOT analysis reveals strengths to build on and weaknesses and threats to manage. Self-confidence, an attitude about one's skills and abilities, is increased by focusing on strengths, taking on new experiences and practising self-compassion. Managing stress through a healthy lifestyle, planning and support, and adapting to inevitable change through a proactive and positive attitude complete the picture. Together these skills let individuals reach their highest potential and businesses project a professional image that attracts and retains customers.",
        "marks": 20,
        "min_words": 180,
        "max_words": 450,
    },
]

# ---------------------------------------------------------------------------
# 5. Curated scenario / application questions (typed) - the entropy-generated
#    discussion items above cover general explanation; these cover applied
#    scenario work quoted from the learner's book (Activity 18.1 / 18.2 and
#    Consolidation Q2 - MAZAMO TRADERS / REGGIAN LTD).
# ---------------------------------------------------------------------------

def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="MAZAMO TRADERS told employees to accept and love themselves unconditionally and to confront what they find difficult to accept about themselves. Quote TWO ways of increasing self-confidence from the scenario. (2)",
            marking_points=[
                "Accept and love yourself unconditionally.",
                "Confront what you find difficult to accept about yourself.",
            ],
            sample_answer="(1) Accept and love yourself unconditionally. (2) Confront what you may find difficult to accept about yourself.",
            marks=2,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Reggian Ltd advises employees to conduct regular medical check-ups and to avoid activities that lead to stress. Quote TWO ways RL uses to encourage a balanced lifestyle and recommend TWO further stress-management practices. (4)",
            marking_points=[
                "Advise regular medical check-ups.",
                "Advise avoiding activities that could lead to stress.",
                "Set aside personal time / take breaks / exercise regularly.",
                "Develop a healthy lifestyle / eat a balanced diet / reduce caffeine / be optimistic.",
            ],
            sample_answer="RL quotes two ways: advising regular medical check-ups and avoiding activities that lead to stress. Two further stress-management practices could be setting aside personal time with regular exercise, and developing a healthy lifestyle with a balanced diet and reduced caffeine.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="A learner writes: 'I always procrastinate before exams.' Recommend FOUR time-management practices that will help this learner. (4)",
            marking_points=[
                "Set specific, measurable and time-bound goals for study.",
                "Prioritise work and pre-plan a study schedule.",
                "Define time limits for each task and organise study resources.",
                "Avoid distractions and delegate/reduce redundancies; keep a balanced routine.",
            ],
            sample_answer="The learner should set specific, measurable and time-bound study goals, prioritise work and pre-plan a study schedule, define time limits and organise study resources, and avoid distractions while keeping a balanced routine.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


# ---------------------------------------------------------------------------
# Wire it up: entropy pools + curated application, then hand the merged dict
# to build_generate.
# ---------------------------------------------------------------------------

def _pools(r) -> Dict[str, List[Callable[[], Dict[str, Any]]]]:
    pools = expand_fact_base(
        PREFIX, VAID,
        mcq_facts=FACTS,
        pairs=PAIRS,
        typed_specs=TYPED_SPECS,
        essay_specs=ESSAY_SPECS,
        mcq_variants=6,          # 15 facts x 6 = 90 MCQ variants
        matching_variants=8,     # sub-sample PAIRS
        crossword_variants=5,
        wordbank_variants=6,
        typed_variants=4,        # rotate verb + subset count
        essay_variants=4,
    )
    pools["application"] = _application(r)
    return pools


generate_self_management = build_generate(_pools)
