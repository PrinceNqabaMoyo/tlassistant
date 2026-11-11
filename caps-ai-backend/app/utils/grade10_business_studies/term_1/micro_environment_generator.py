"""Grade 10 Business Studies - Term 1 - Topic 1: Components of the micro environment.

Deterministic generator (no LLM). Content is hand-authored from the CAPS
curriculum notes and activities for this topic. Question shapes match the
Business Studies /generate and /mark endpoints.

Subskills:
    concepts    -> MCQ recall/understanding of the micro-environment components
    discussion  -> typed (outline/explain/differentiate) questions with memos
    mixed       -> union of all pools
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import (
    build_generate,
    make_mcq,
    make_typed,
    make_wordbank,
    make_matching,
    make_crossword,
    make_essay,
    pick_scenario,
)

PREFIX = "g10bs_micro"
VAID = "micro_environment"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which ONE of the following is a component of the micro environment?",
            options=["Suppliers", "Competitors", "Vision and mission statement", "Economic factors"],
            correct_index=2,
            explanation="The vision and mission statement are internal components fully controlled by the business, so they form part of the micro environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The micro environment of a business is best described as the environment that the business has …",
            options=[
                "no control over at all",
                "full/complete control over",
                "only partial influence over",
                "control over only through government",
            ],
            correct_index=1,
            explanation="The business has full/complete control over its micro (internal) environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="What does a business's MISSION STATEMENT primarily describe?",
            options=[
                "Its long-term dream for the future",
                "What the business provides or produces, and why it exists",
                "The dress code employees must follow",
                "The steps used to advertise products",
            ],
            correct_index=1,
            explanation="The mission statement describes what the business provides or produces and why it exists.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The VISION of a business refers to …",
            options=[
                "what the business wants to achieve in the long term (its dream)",
                "the short-term steps to achieve goals",
                "the people who work in the business",
                "the money borrowed from a bank",
            ],
            correct_index=0,
            explanation="The vision is what the business wants to achieve in the long term — the dream of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which term describes the SHORT-TERM steps that explain how goals will be achieved?",
            options=["Vision", "Goals", "Objectives", "Mission"],
            correct_index=2,
            explanation="Objectives describe how goals will be achieved; they are the short-term steps.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Raw materials, buildings, machinery and vehicles are examples of which resource category?",
            options=["Human resources", "Technological resources", "Physical resources", "Financial resources"],
            correct_index=2,
            explanation="Physical resources are tangible items such as raw materials, buildings, machinery and vehicles.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Software licences, patents, websites and computer software are examples of which resource category?",
            options=["Technological resources", "Physical resources", "Human resources", "Financial resources"],
            correct_index=0,
            explanation="Technological resources are intangible resources such as software licences, patents and websites.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A bank overdraft, credit cards and long-term loans form part of a business's …",
            options=["human resources", "financial resources", "physical resources", "technological resources"],
            correct_index=1,
            explanation="Financial resources refer to the capital a business owns or borrows, including overdrafts, credit cards and loans.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which statement BEST describes 'organisational culture'?",
            options=[
                "The hierarchy of managers and subordinates",
                "The physical assets owned by the business",
                "The way things are done — the shared values, beliefs, norms and dress code",
                "The long-term plans the business wants to accomplish",
            ],
            correct_index=2,
            explanation="Organisational culture refers to how things are done, including the values, beliefs, norms and dress code shared by employees.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An organogram is another name for the …",
            options=[
                "mission statement",
                "organisational structure",
                "code of conduct",
                "marketing plan",
            ],
            correct_index=1,
            explanation="The organisational structure is also known as an organogram; it shows levels of authority, responsibility and tasks.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which business function is responsible for changing/processing raw materials into finished products?",
            options=["Purchasing function", "Production function", "Administration function", "Marketing function"],
            correct_index=1,
            explanation="The production function changes/processes raw materials into finished or semi-finished products.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which business function is responsible for buying all the resources the business needs?",
            options=["Purchasing function", "Financial function", "Public relations function", "Production function"],
            correct_index=0,
            explanation="The purchasing function buys all the resources the business needs to produce its goods and services.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which function is responsible for creating a good public image and communicating with stakeholders?",
            options=["Marketing function", "Public relations function", "Human resources function", "Administration function"],
            correct_index=1,
            explanation="The public relations function creates a good public image and ensures proper communication with stakeholders.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=f"At {biz}, the manager plans, organises, leads and controls the resources of the business. This describes …",
            options=["leadership", "management", "marketing", "administration"],
            correct_index=1,
            explanation="Management is the process of guiding and directing the business by planning, organising, leading and controlling resources.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How many business functions are there in the micro environment?",
            options=["Six", "Seven", "Eight", "Ten"],
            correct_index=2,
            explanation="There are eight business functions: general management, purchasing, production, marketing, public relations, human resources, administration and financial.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Dress code together with the shared values, beliefs and norms of employees describes a business's …",
            options=["organisational structure", "organisational culture", "mission statement", "code of conduct"],
            correct_index=1,
            explanation="Organisational culture is 'how things are done' — the shared values, beliefs, norms and dress code of employees and management.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Laptops, computer software, websites and patents are grouped under which organisational resource?",
            options=["human", "physical", "financial", "technological"],
            correct_index=3,
            explanation="Technological resources are intangible items such as software licences, patents, websites and computer equipment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A bank overdraft, credit cards and short-term loans form part of a business's … resources.",
            options=["financial", "physical", "human", "technological"],
            correct_index=0,
            explanation="Financial resources are the capital the business owns or borrows, including overdrafts, credit cards and loans.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The set of people who make up the workforce of a business are its … resources.",
            options=["human resources", "physical resources", "financial resources", "technological resources"],
            correct_index=0,
            explanation="Human resources are the people who make up the workforce of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which level of management consists of the CEO and directors and sets long-term strategy?",
            options=["Lower-level", "Middle-level", "Top-level", "Supervisory"],
            correct_index=2,
            explanation="Top-level management (CEO and directors) develops long-term strategic plans and determines the vision and mission.",
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
            prompt="The ability of an individual to inspire, influence or motivate subordinates toward business goals is …",
            options=["management", "leadership", "administration", "control"],
            correct_index=1,
            explanation="Leadership is the ability to inspire, influence or motivate subordinates to achieve the goals and objectives of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which business function undertakes market research to determine the real needs of the target market?",
            options=["production", "purchasing", "marketing", "administration"],
            correct_index=2,
            explanation="The marketing function conducts market research to determine the needs of the target market and promotes the goods and services.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A STAKEHOLDER is best defined as …",
            options=[
                "only the shareholders who own the business",
                "any party that has an interest in the business and can affect or be affected by it",
                "the government department that issues licences",
                "the manager in charge of human resources",
            ],
            correct_index=1,
            explanation="A stakeholder is any party with an interest in the company that can affect or be affected by the business, e.g. employees, customers, suppliers and shareholders.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that adopt the latest technology gain a … over rivals that struggle with it.",
            options=["monopoly", "competitive advantage", "licensing fee", "trade barrier"],
            correct_index=1,
            explanation="A competitive advantage is a factor that allows a business to produce goods or services better or cheaper than its rivals.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In the concentric-circle model of the business environment, the INNERMOST circle is the …",
            options=["macro environment", "market environment", "micro environment", "global environment"],
            correct_index=2,
            explanation="The micro (internal) environment is the innermost circle, followed by the market environment and then the outermost macro environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Objectives differ from goals because objectives are …",
            options=[
                "the long-term dreams of the business",
                "the short-term steps describing how goals will be achieved",
                "synonymous with the vision statement",
                "set only by external stakeholders",
            ],
            correct_index=1,
            explanation="Goals are long-term plans; objectives are the short-term steps that describe how those goals will be achieved.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is NOT a component of the micro environment?",
            options=["Organisational culture", "The eight business functions", "Suppliers and competitors", "Organisational resources"],
            correct_index=2,
            explanation="Suppliers and competitors belong to the MARKET environment, not the internal micro environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The human resources function is responsible for …",
            options=[
                "processing raw materials into finished goods",
                "attracting new employees and providing education and training",
                "collecting and storing data and information",
                "determining the financial needs of the business",
            ],
            correct_index=1,
            explanation="The human resources function attracts new employees into the business and manages them through education and training.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="State any THREE components of the micro environment. (3)",
            marking_points=[
                "Vision, mission statement, goals and objectives",
                "Organisational culture",
                "Organisational resources",
                "Management and leadership",
                "Organisational structure",
                "Eight business functions",
            ],
            sample_answer="Three components of the micro environment are: organisational culture; organisational resources; and the eight business functions.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the purpose of organisational culture in a business. (4)",
            marking_points=[
                "Defines the business' internal and external identity and core values.",
                "Has the power to turn employees into ambassadors of the business.",
                "Helps the business retain its employees and clients.",
                "Breaks down boundaries between teams, guides decision-making and improves productivity.",
            ],
            sample_answer="The purpose of organisational culture is to define the core values and identity of the business. A strong culture turns employees into ambassadors and helps retain staff and clients. It also guides decision-making, breaks down team boundaries and improves productivity.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the purpose of an organisational structure (organogram). (6)",
            marking_points=[
                "Helps ensure the smooth and efficient functioning of the business.",
                "Ensures work happens with precise co-ordination and minimum wastage of resources.",
                "Helps the business work towards its goals.",
                "Shows the connections between various positions and tasks.",
                "Describes the coordination between various departments in the business.",
            ],
            sample_answer="An organogram shows the connections between positions and tasks and the levels of authority. It ensures the smooth, efficient functioning of the business by coordinating departments with minimum wastage of resources, helping the business work towards its goals.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Differentiate between MANAGEMENT and LEADERSHIP. (4)",
            marking_points=[
                "Management is the process of guiding and directing the organisation to achieve goals.",
                "Managers plan, organise, lead and control resources.",
                "Leadership is the ability to inspire, influence or motivate subordinates.",
                "Leaders focus on influencing behaviour towards achieving objectives.",
            ],
            sample_answer="Management guides and directs the organisation by planning, organising, leading and controlling resources to achieve goals. Leadership, in contrast, is the ability to inspire, influence or motivate subordinates' behaviour towards achieving the business's objectives.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Name the FOUR main groups of organisational resources. (4)",
            marking_points=[
                "Human resources",
                "Physical resources",
                "Financial resources",
                "Technological resources",
            ],
            sample_answer="The four main groups of organisational resources are human resources, physical resources, financial resources and technological resources.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Briefly explain the purpose of the general management function. (4)",
            marking_points=[
                "Coordinates the other business functions to achieve the goals and objectives.",
                "Plans, organises, leads and controls resources in the business.",
                "Brings the different functions to work together.",
            ],
            sample_answer="The general management function coordinates the other seven business functions so they work together. It plans, organises, leads and controls the resources of the business to achieve its goals and objectives.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=f"Formulate a suitable VISION and MISSION statement for {biz}. (4)",
            marking_points=[
                "The vision states what the business wants to achieve in the future (long term).",
                "The mission statement explains why the business exists.",
                "The mission statement describes what the business provides/produces.",
            ],
            sample_answer=f"Vision: {biz} aims to become the most trusted provider in its market. Mission: {biz} exists to deliver high-quality products and services that meet customer needs while creating sustainable value.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the difference between GOALS and OBJECTIVES. (4)",
            marking_points=[
                "Goals are the long-term plans the business wants to accomplish.",
                "Goals serve as guidelines for what the business sets out to do.",
                "Objectives describe how goals will be achieved.",
                "Objectives are the short-term steps to achieve the goals.",
            ],
            sample_answer="Goals are the long-term plans the business wants to accomplish and act as guidelines. Objectives are the short-term steps that describe how those goals will be achieved.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    """Scenario/application questions (MCQ + short typed) based on the
    Sarah's Bakery and Mzobe Traders activities in the CAPS curriculum."""
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Sarah's Bakery took out a loan from FastBank to cover start-up costs. Which organisational resource does this represent?",
            options=["human resources", "physical resources", "financial resources", "technological resources"],
            correct_index=2,
            explanation="A loan from a bank is a financial resource — the capital the business borrows from a financial institution.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Sarah's Bakery uses an ONLINE ORDERING SYSTEM to make ordering easier for customers. This is an example of which resource?",
            options=["technological", "physical", "human", "financial"],
            correct_index=0,
            explanation="An online ordering system / website is a technological (intangible) resource.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Sarah bought a small BUILDING for baking and packaging. The building is a … resource.",
            options=["financial", "physical", "human", "technological"],
            correct_index=1,
            explanation="Buildings, machinery and vehicles are tangible physical resources.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Mzobe Traders used an effective RECRUITMENT method to attract the best candidates. Which business function did this apply?",
            options=["administration", "financial", "human resources", "public relations"],
            correct_index=2,
            explanation="Recruitment and selection of candidates is the human resources function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Mr Masina, the CEO, included the vision and mission statement in his speech. Which function does a CEO belong to?",
            options=["general management", "marketing", "purchasing", "production"],
            correct_index=0,
            explanation="The CEO is top-level general management, which sets the vision, mission and direction of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Read the Sarah's Bakery scenario and identify THREE organisational resources used by SB. Motivate each by quoting from the scenario. (9)",
            marking_points=[
                "Human resources — 'Sarah employed five employees to help her'.",
                "Physical resources — 'She bought a small building where she does all her baking and packaging'.",
                "Financial resources — 'Sarah had to take out a loan from FastBank to cover the cost of setting up her business'.",
                "Technological resources — 'She uses an online ordering system to make ordering easier for her customers'.",
                "Each resource correctly named with a supporting quote earns marks.",
            ],
            sample_answer="SB uses human resources ('Sarah employed five employees to help her'); physical resources ('She bought a small building where she does all her baking and packaging'); financial resources ('Sarah had to take out a loan from FastBank'); and technological resources ('She uses an online ordering system'). Any three of these, each quoted from the scenario, are correct.",
            marks=9,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Formulate a suitable VISION and MISSION statement for a cell-phone provider. (4)",
            marking_points=[
                "Vision states what the business wants to achieve in the future (long term).",
                "Mission explains why the business exists and what it provides/produces.",
                "Statements are realistic and relevant to a cell-phone provider.",
            ],
            sample_answer="Vision: 'To be the most loved mobile network connecting every South African home and business.' Mission: 'We provide affordable, reliable voice and data services and innovative mobile solutions that keep our customers connected.'",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Word-bank items built from the micro-environment key concepts."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Choose the correct words from the bank to complete the key-concept definitions.",
            pool=["vision", "mission", "goals", "objectives", "culture"],
            blanks=["1", "2", "3", "4"],
            correct_map={"1": "vision", "2": "mission", "3": "goals", "4": "objectives"},
            text_parts=[
                "The ",
                " is what the business wants to achieve in the long term (its dream). The ",
                " statement describes what the business provides and why it exists. The ",
                " are the long-term plans of the business, while the ",
                " describe the short-term steps to achieve them.",
            ],
            explanation="Vision = long-term dream; Mission = why the business exists; Goals = long-term plans; Objectives = short-term steps.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the sentence about the four groups of organisational resources.",
            pool=["human", "physical", "financial", "technological", "emotional"],
            blanks=["1", "2", "3", "4"],
            correct_map={"1": "human", "2": "physical", "3": "financial", "4": "technological"},
            text_parts=[
                "The four main groups of organisational resources are ",
                " resources (the workforce), ",
                " resources (tangible assets), ",
                " resources (capital and funds) and ",
                " resources (software and patents).",
            ],
            explanation="The four resource groups are human, physical, financial and technological; 'emotional' is the distractor.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Matching columns linking micro-environment terms to their descriptions."""
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each TERM in Column A with its correct DESCRIPTION in Column B.",
            column_a=["Vision", "Mission statement", "Organogram", "Organisational culture", "Stakeholder"],
            column_b=[
                "Any party that has an interest in and can affect or be affected by the business",
                "What the business wants to achieve in the long term",
                "Diagram showing levels of authority and how departments are organised",
                "Describes what the business provides and why it exists",
                "The shared values, beliefs and norms — 'how things are done'",
            ],
            correct_pairs={
                "Vision": "What the business wants to achieve in the long term",
                "Mission statement": "Describes what the business provides and why it exists",
                "Organogram": "Diagram showing levels of authority and how departments are organised",
                "Organisational culture": "The shared values, beliefs and norms — 'how things are done'",
                "Stakeholder": "Any party that has an interest in and can affect or be affected by the business",
            },
            explanation="Each internal component has a distinct definition; match by the key defining words.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each BUSINESS FUNCTION with what it is responsible for.",
            column_a=["Production", "Purchasing", "Marketing", "Public relations", "Administration"],
            column_b=[
                "Collecting, processing and storing data and information",
                "Changing/processing raw materials into finished products",
                "Creating a good public image and communicating with stakeholders",
                "Buying the resources the business needs to produce",
                "Undertaking market research and promoting goods and services",
            ],
            correct_pairs={
                "Production": "Changing/processing raw materials into finished products",
                "Purchasing": "Buying the resources the business needs to produce",
                "Marketing": "Undertaking market research and promoting goods and services",
                "Public relations": "Creating a good public image and communicating with stakeholders",
                "Administration": "Collecting, processing and storing data and information",
            },
            explanation="Each of the eight business functions has a specific role; match function to role.",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """Crossword using the key vocabulary from the micro-environment activity."""
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="Read each clue and enter the correct business term.",
            words=["VISION", "VALUES", "MANAGEMENT", "LEADERSHIP", "OBJECTIVES", "ORGANOGRAM", "CULTURE"],
            clues={
                "VISION": "What the business wants to achieve in the long term — its dream",
                "VALUES": "The morals shared by the employees in an organisation",
                "MANAGEMENT": "The process of planning, organising, leading and controlling",
                "LEADERSHIP": "The ability to inspire and motivate people to achieve goals",
                "OBJECTIVES": "Short-term steps that describe how goals will be achieved",
                "ORGANOGRAM": "The hierarchical structure diagram of the business",
                "CULTURE": "The beliefs, values and norms of a group of people",
            },
            grid_size=15,
            explanation="These terms are the key concepts of the components of the micro environment.",
            marks=7,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Long-form essay questions aligned to the topic's learning objectives."""
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt="Discuss the six components of the micro (internal) environment of a business and explain why each is important. (20)",
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Define the micro environment and state that the business has full control over it."},
                {"criterion": "Components", "marks": 10, "description": "Name and describe at least four components: vision/mission/goals/objectives, organisational culture, resources, management & leadership, structure and the eight functions."},
                {"criterion": "Importance", "marks": 4, "description": "Explain why each component contributes to business success."},
                {"criterion": "Conclusion", "marks": 3, "description": "Summarise how the components work together as the internal operating system."},
            ],
            sample_answer="The micro environment is everything inside the business over which it has full control. Its components are the vision, mission, goals and objectives (the direction of the business); organisational culture (shared values and norms that turn employees into ambassadors); organisational resources (human, physical, financial and technological); management and leadership (planning/organising and inspiring); the organisational structure/organogram (levels of authority); and the eight business functions. Each component guides decisions, coordinates work and supports productivity, so together they act as the internal operating system that determines whether the business achieves its goals.",
            marks=20,
            min_words=150,
            max_words=350,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt="'A business can only succeed if its eight functions work together as a team.' Discuss this statement with reference to the eight business functions. (20)",
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Define business functions and list the eight of them."},
                {"criterion": "Roles", "marks": 8, "description": "Describe the role of at least five functions (general management, purchasing, production, marketing, public relations, human resources, administration, financial)."},
                {"criterion": "Interrelationship", "marks": 6, "description": "Explain how general management coordinates the others and how a failure in one function (e.g. marketing) affects the whole business."},
                {"criterion": "Conclusion", "marks": 3, "description": "Conclude on the importance of coordination for achieving objectives."},
            ],
            sample_answer="The eight business functions — general management, purchasing, production, marketing, public relations, human resources, administration and financial — are interrelated and work as a team. General management coordinates the other seven. Purchasing buys resources, production transforms them, and marketing sells to the customer, while financial and administration handle funds and information. If marketing fails to attract the target market, the profit objective is not realised even if the other functions perform well, which shows that success depends on how effectively the functions are coordinated and managed.",
            marks=20,
            min_words=150,
            max_words=350,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
        "application": _application(r),
        "word_bank": _wordbank(r),
        "matching": _matching(r),
        "crossword": _crossword(r),
        "essay": _essay(r),
    }


generate = build_generate(_pools)
