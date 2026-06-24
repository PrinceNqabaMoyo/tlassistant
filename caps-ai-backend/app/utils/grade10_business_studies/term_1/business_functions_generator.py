"""Grade 10 Business Studies - Term 1 - Topic 2: Business functions and the
activities of the business.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed, make_wordbank, make_matching, make_crossword, make_essay

PREFIX = "g10bs_bizfunc"
VAID = "business_functions"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How many business functions are there in a business?",
            options=["Five", "Six", "Eight", "Ten"],
            correct_index=2,
            explanation="There are eight business functions, with general management overseeing the other seven.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which business function oversees and coordinates all the other functions?",
            options=["Marketing function", "General management function", "Purchasing function", "Public relations function"],
            correct_index=1,
            explanation="The general management function leads, organises and controls all the other functions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The function responsible for collecting and storing information for decision-making is the …",
            options=["administration function", "financial function", "production function", "marketing function"],
            correct_index=0,
            explanation="The administration function collects and stores information used by management in decision-making.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Buying the goods and services a company needs to operate and manufacture products is the … function.",
            options=["financial", "purchasing", "marketing", "production"],
            correct_index=1,
            explanation="The purchasing function buys the goods and services the company needs.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Promoting and selling products or services is the responsibility of the … function.",
            options=["public relations", "marketing", "purchasing", "administration"],
            correct_index=1,
            explanation="The marketing function promotes and sells the products or services.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The continuous maintenance of a positive public image is the role of the … function.",
            options=["marketing", "public relations", "human resources", "financial"],
            correct_index=1,
            explanation="The public relations function maintains a positive public image of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Hiring and training of staff is handled by the … function.",
            options=["human resources", "administration", "general management", "production"],
            correct_index=0,
            explanation="The human resources function deals with the hiring and training of staff.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A function of an enterprise that directly generates income (e.g. production) is a … function.",
            options=["support", "core", "tactical", "strategic"],
            correct_index=1,
            explanation="Core business functions generate income; support functions facilitate production.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which statement describes a LEADER rather than a manager?",
            options=[
                "Understands the goals of the business",
                "Ensures tasks given to subordinates are completed",
                "Creates a vision and sets direction",
                "Is appointed to the position",
            ],
            correct_index=2,
            explanation="A leader creates a vision and sets direction; a manager understands goals and ensures tasks are completed.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which level of management consists of the CEO and directors and sets long-term strategy?",
            options=["Lower-level management", "Middle-level management", "Top-level management", "Supervisory management"],
            correct_index=2,
            explanation="Top-level management (CEO and directors) sets long-term strategic plans and policies.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Departmental managers who take medium-term tactical decisions belong to … management.",
            options=["top-level", "middle-level", "lower-level", "operational"],
            correct_index=1,
            explanation="Middle-level management (e.g. departmental managers) takes medium-term tactical decisions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Foremen, supervisors and team leaders who take short-term operational decisions are … management.",
            options=["top-level", "middle-level", "lower-level", "strategic"],
            correct_index=2,
            explanation="Lower-level management (foremen, supervisors, team leaders) takes short-term operational decisions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is NOT one of the five management tasks?",
            options=["Planning", "Organising", "Marketing", "Controlling"],
            correct_index=2,
            explanation="The five management tasks are planning, organising, leadership, controlling and risk management.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The management task that identifies, assesses and controls threats to a business is …",
            options=["planning", "organising", "risk management", "leadership"],
            correct_index=2,
            explanation="Risk management identifies, assesses and controls threats to a business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which Act protects consumers and requires information about a product's ingredients?",
            options=[
                "National Credit Act (NCA)",
                "Consumer Protection Act (CPA)",
                "Labour Relations Act (LRA)",
                "Skills Development Act (SDA)",
            ],
            correct_index=1,
            explanation="The Consumer Protection Act protects consumers and requires product information such as ingredients.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The management task of bringing materials, human and financial resources together to execute a plan is …",
            options=["planning", "organising", "controlling", "directing"],
            correct_index=1,
            explanation="Organising brings resources together and breaks the plan into delegated actions.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between leadership and management. (8)",
            marking_points=[
                "A leader creates a vision/sets direction; a manager understands the goals of the business.",
                "Leaders create the team and inspire subordinates; managers ensure tasks are completed.",
                "A leader influences human behaviour; a manager guides human behaviour.",
                "Leaders are born with natural skills; a manager is appointed to the position.",
            ],
            sample_answer="A leader creates a vision and sets direction, inspiring and building the team, and influences human behaviour, often with natural/instinctive skills. A manager understands the goals of the business, ensures tasks are completed, guides human behaviour and is appointed to the position.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the responsibilities of top-level management. (4)",
            marking_points=[
                "Oversees the activities of the other functions to achieve objectives.",
                "Comprises the CEO and directors.",
                "Develops long-term goals, strategic plans and business policies.",
                "Determines the vision, mission, objectives and strategy of the business.",
            ],
            sample_answer="Top-level management, made up of the CEO and directors, oversees the other functions to achieve objectives. It develops long-term goals, strategic plans and policies, and determines the vision, mission, objectives and strategy of the business.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Describe the responsibilities of middle-level management. (4)",
            marking_points=[
                "Responsible for specific departments within the business.",
                "Takes medium-term tactical decisions.",
                "Implements the plans and vision of top management.",
                "Acts as the link between top and lower management.",
            ],
            sample_answer="Middle-level management is responsible for specific departments and takes medium-term tactical decisions. It implements the plans and vision of top management and acts as the link between top and lower management.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the five management tasks. (10)",
            marking_points=[
                "Planning: evaluating activities and goals and scheduling activities to achieve them.",
                "Organising: bringing resources together and delegating actions to execute the plan.",
                "Leadership/directing: motivating and guiding employees to achieve goals.",
                "Controlling: setting performance standards and taking corrective measures.",
                "Risk management: identifying, assessing and controlling threats to the business.",
            ],
            sample_answer="Planning evaluates goals and schedules activities to achieve them. Organising brings resources together and delegates actions. Leadership motivates and guides employees. Controlling sets performance standards and takes corrective action. Risk management identifies, assesses and controls threats to the business.",
            marks=10,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Describe the management task of 'controlling'. (4)",
            marking_points=[
                "Establish performance standards and ensure they are met.",
                "Compare actual results with the goals set by management.",
                "Take corrective measures where there are deviations.",
                "Continuous control ensures the business runs smoothly.",
            ],
            sample_answer="Controlling establishes performance standards and ensures they are met by comparing actual results with the goals set by management. Where there are deviations, corrective measures are taken, and continuous control ensures the business runs smoothly.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the relationship between the eight business functions. (6)",
            marking_points=[
                "The eight functions are interrelated and work together as a team.",
                "General management is directly linked to all seven other functions.",
                "Financial and administration functions gather, store and process information/records.",
                "Purchasing, production and marketing are responsible for the delivery of goods.",
            ],
            sample_answer="The eight business functions are interrelated and work as a team. General management is linked to all seven other functions, the financial and administration functions handle information and records, while the purchasing, production and marketing functions deliver goods to the customer.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Describe the management task of 'planning'. (4)",
            marking_points=[
                "Evaluates existing activities and goals.",
                "Top management formulates strategic plans; middle, tactical; lower, operational.",
                "Different plans are considered and a chosen plan is implemented.",
                "Backup plans are put in place if the chosen plan becomes impossible.",
            ],
            sample_answer="Planning evaluates existing activities and goals and schedules activities to achieve them. Top management formulates strategic plans, middle management tactical plans, and lower management operational plans. Different plans are considered, the chosen one is implemented, and backup plans are kept ready.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Distinguish between core and support business functions. (4)",
            marking_points=[
                "Core functions are activities of an enterprise that generate income.",
                "Example of a core function: the production function that makes the final goods.",
                "Support functions are carried out to facilitate the production of goods/services.",
                "Example of a support function: the marketing function.",
            ],
            sample_answer="Core business functions generate income, for example the production function that makes the final goods. Support business functions facilitate production, for example the marketing function.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the importance of the administration function. (4)",
            marking_points=[
                "Collects and stores information used by management in decision-making.",
                "Processes and keeps records and data for the business.",
                "Provides information to all the other functions.",
                "Supports efficient decision-making across the business.",
            ],
            sample_answer="The administration function collects and stores the information used by management for decision-making. It processes and keeps the business's records and data, supplies information to the other functions, and supports efficient decision-making throughout the business.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Word-bank questions drawn from curriculum key concepts."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Fill in the missing words to complete the definitions of business functions.",
            pool=["General management", "Administration", "Financial", "Purchasing", "Public relations", "Human resources", "Production", "Marketing"],
            blanks=["1", "2", "3"],
            correct_map={"1": "General management", "2": "Administration", "3": "Financial"},
            text_parts=[
                "The ",
                " function sets the overall direction for the business and oversees all other functions.",
                "The ",
                " function collects and stores information used by management in decision making.",
                "The ",
                " function involves acquiring and utilising funds necessary for efficient operations."
            ],
            explanation="General management sets direction; Administration collects information; Financial acquires funds.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the sentence about management and leadership.",
            pool=["vision", "mission", "goals", "objectives", "planning", "organising", "controlling", "leadership"],
            blanks=["1", "2", "3"],
            correct_map={"1": "vision", "2": "mission", "3": "objectives"},
            text_parts=[
                "The ",
                " describes what the business wants to achieve in the long-term.",
                "The ",
                " statement describes what the business provides or produces.",
                "The ",
                " describe how goals will be achieved."
            ],
            explanation="Vision = long-term dream; Mission = what the business provides; Objectives = how goals are achieved.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Matching columns drawn from curriculum content."""
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each business function with its correct description.",
            column_a=["General management", "Administration", "Financial", "Purchasing", "Marketing"],
            column_b=["Collects and stores information for decision-making", "Sets overall direction and oversees all functions", "Buys goods and services needed to operate", "Acquires and utilises funds for operations", "Promotes and sells products or services"],
            correct_pairs={
                "General management": "Sets overall direction and oversees all functions",
                "Administration": "Collects and stores information for decision-making",
                "Financial": "Acquires and utilises funds for operations",
                "Purchasing": "Buys goods and services needed to operate",
                "Marketing": "Promotes and sells products or services"
            },
            explanation="Each business function has a specific purpose: General management oversees; Administration handles information; Financial manages funds; Purchasing buys inputs; Marketing sells products.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each level of management with its key responsibility.",
            column_a=["Top-level management", "Middle-level management", "Lower-level management"],
            column_b=["Takes short-term operational decisions", "Takes medium-term tactical decisions", "Develops long-term strategic plans"],
            correct_pairs={
                "Top-level management": "Develops long-term strategic plans",
                "Middle-level management": "Takes medium-term tactical decisions",
                "Lower-level management": "Takes short-term operational decisions"
            },
            explanation="Top-level = strategic/long-term; Middle-level = tactical/medium-term; Lower-level = operational/short-term.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """Crossword questions using key vocabulary from the curriculum."""
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="Read each clue and fill in the correct business term.",
            words=["MANAGEMENT", "LEADERSHIP", "ORGANISING", "CONTROLLING", "PLANNING"],
            clues={
                "MANAGEMENT": "The process of guiding and directing an organisation to achieve its goals",
                "LEADERSHIP": "The ability to inspire and influence subordinates",
                "ORGANISING": "Identifying and grouping work, defining responsibility and authority",
                "CONTROLLING": "Measuring progress towards goals and taking corrective action",
                "PLANNING": "Thinking about activities required to achieve a desired goal"
            },
            grid_size=15,
            explanation="These are the five key management tasks/functions.",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Essay questions drawn from curriculum learning objectives."""
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt="Discuss the differences between leadership and management in a business context. (20)",
            rubric=[
                {"criterion": "Introduction", "marks": 4, "description": "Define leadership and management and state the purpose of the essay."},
                {"criterion": "Differences", "marks": 8, "description": "Explain at least four differences between leadership and management with examples."},
                {"criterion": "Relationship", "marks": 4, "description": "Explain how leadership and management complement each other in business."},
                {"criterion": "Conclusion", "marks": 4, "description": "Summarise the key points and give a final evaluative statement."}
            ],
            sample_answer="Leadership and management are both necessary competencies in business, but they are different. A leader creates a vision and sets direction, inspiring subordinates with natural or instinctive skills. A manager understands business goals, ensures tasks are completed, and is appointed to the position. Leaders influence behaviour while managers guide behaviour. Both are essential for business success.",
            marks=20,
            min_words=150,
            max_words=300,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt="Discuss the importance of the eight business functions and how they are interrelated. (20)",
            rubric=[
                {"criterion": "Introduction", "marks": 4, "description": "Define business functions and state the purpose of the essay."},
                {"criterion": "Eight Functions", "marks": 8, "description": "Name and briefly describe at least five of the eight business functions."},
                {"criterion": "Interrelationship", "marks": 4, "description": "Explain how the functions depend on each other to achieve business goals."},
                {"criterion": "Conclusion", "marks": 4, "description": "Summarise the importance of business functions and give a final statement."}
            ],
            sample_answer="Business functions are tasks requiring specific knowledge and skills carried out by various departments to achieve business goals. There are eight functions: General Management, Administration, Financial, Purchasing, Public Relations, Human Resources, Production and Marketing. They are interrelated and work together as a team. General management oversees all functions. The financial and administration functions gather and process information. Purchasing, production and marketing deliver goods to customers. Together they ensure the survival and sustainability of the business.",
            marks=20,
            min_words=150,
            max_words=300,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
        "word_bank": _wordbank(r),
        "matching": _matching(r),
        "crossword": _crossword(r),
        "essay": _essay(r),
    }


generate_business_functions = build_generate(_pools)
