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

from .._bs_common import build_generate, make_mcq, make_typed, pick_scenario

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


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate = build_generate(_pools)
