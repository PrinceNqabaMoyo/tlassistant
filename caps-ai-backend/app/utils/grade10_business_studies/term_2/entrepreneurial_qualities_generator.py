"""Grade 10 Business Studies - Term 2 - Topic 9: Entrepreneurial qualities.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_entrequal"
VAID = "entrepreneurial_qualities"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A person who starts a business, taking on financial risks to make a profit, is a/an …",
            options=["employee", "entrepreneur", "shareholder", "regulator"],
            correct_index=1,
            explanation="An entrepreneur starts a business and takes on financial risks in the hope of making a profit.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The quality of being able to change and adapt to different circumstances is called …",
            options=["flexibility", "commitment", "ambition", "perseverance"],
            correct_index=0,
            explanation="Flexibility is the ability to change and adapt to different circumstances.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A strong desire to achieve something describes …",
            options=["ambition", "confidence", "passion", "flexibility"],
            correct_index=0,
            explanation="Ambition is a strong desire to achieve something.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A person who introduces a new method, idea or product is a/an …",
            options=["innovator", "risk-taker", "investor", "manager"],
            correct_index=0,
            explanation="An innovator introduces a new method, idea or product.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Persistence in doing something despite difficulty or delay in achieving success is …",
            options=["confidence", "perseverance", "passion", "autonomy"],
            correct_index=1,
            explanation="Perseverance is persistence despite difficulty or delay in achieving success.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An entrepreneur who measures risks carefully and then dares to see a decision through shows the quality of being a …",
            options=["risk-taker", "follower", "spectator", "regulator"],
            correct_index=0,
            explanation="Risk-takers measure risks carefully and commit to seeing their decisions through.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Independence in one's thoughts and actions is known as …",
            options=["autonomy", "mediocrity", "passion", "stamina"],
            correct_index=0,
            explanation="Autonomy means being independent in one's thoughts and actions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An entrepreneur who can plan, lead, organise and control the activities of the business shows …",
            options=["management and leadership skills", "risk aversion", "mediocrity", "dependence"],
            correct_index=0,
            explanation="Management and leadership skills allow the entrepreneur to plan, lead, organise and control the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The activity of setting up a business and taking financial risks in the hope of making a profit is …",
            options=["entrepreneurship", "administration", "regulation", "intermediation"],
            correct_index=0,
            explanation="Entrepreneurship is the activity of setting up businesses and taking financial risks for profit.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An entrepreneur who has high standards and cannot tolerate mediocrity displays a high degree of …",
            options=["commitment", "flexibility", "risk-taking", "autonomy"],
            correct_index=0,
            explanation="A high degree of commitment means having high standards and not tolerating mediocrity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An entrepreneur who likes to be self-employed and make their own decisions shows a …",
            options=["desire for responsibility", "fear of risk", "lack of confidence", "preference for instruction"],
            correct_index=0,
            explanation="A desire for responsibility means preferring self-employment and making one's own decisions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Great physical stamina and the ability to work long hours and handle stress reflect …",
            options=["high motivation/energy levels", "flexibility", "mediocrity", "autonomy"],
            correct_index=0,
            explanation="High motivation/energy levels give the entrepreneur stamina to work long hours and handle stress.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of an entrepreneur. (4)",
            marking_points=[
                "A person who sets up a business with the aim of making a profit.",
                "Creates a new business, bearing most of the risks and enjoying most of the rewards.",
                "Seen as an innovator and source of new ideas, goods and services.",
                "Able to look at the environment and identify opportunities/new ways of making a product.",
            ],
            sample_answer="An entrepreneur is a person who sets up a business to make a profit, bearing most of the risks and enjoying most of the rewards. They are innovators and a source of new ideas, goods and services, able to look at the environment and identify opportunities.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss flexibility/the ability to adapt quickly as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs adapt quickly to changing circumstances because they are open to change.",
                "They listen to other ideas and use them to correct mistakes.",
                "They continuously update skills and knowledge for the latest technology/market trends.",
                "They are always ready to expand by seeking new opportunities.",
            ],
            sample_answer="Flexible entrepreneurs adapt quickly to changing circumstances because they are open to change. They listen to others' ideas to correct mistakes, continuously update their skills for the latest technology and trends, and are always ready to seek new opportunities to expand.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss being a risk-taker as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs are willing to take risks to achieve their goals.",
                "They measure risks carefully and dare to see a decision through.",
                "They risk by putting capital together to start their business.",
                "They are flexible in their decisions, even when one turns out to be wrong.",
            ],
            sample_answer="Risk-taking entrepreneurs are willing to take risks to achieve their goals. They measure risks carefully, commit to seeing decisions through, risk their capital to start the business, and remain flexible even when a decision turns out to be wrong.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss management and leadership skills as a quality of an entrepreneur. (4)",
            marking_points=[
                "Management skills enable them to plan, lead, organise and control the business.",
                "They are good leaders who listen to others and inspire them.",
                "They are good communicators, skilled at resolving conflict.",
                "They know their weaknesses and get others to complement their strengths.",
            ],
            sample_answer="Entrepreneurs with management and leadership skills can plan, lead, organise and control the business. They are good leaders who listen to and inspire others, are good communicators who resolve conflict, and they recognise their weaknesses, getting others to complement their strengths.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss perseverance as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs keep going even if things are difficult or failing.",
                "They do not give up easily and stay motivated.",
                "They are goal-driven and cannot tolerate failure.",
                "Their motivation keeps them going through challenges.",
            ],
            sample_answer="Perseverance means entrepreneurs keep going even when things are difficult or failing. They do not give up easily, stay motivated, are goal-driven and cannot tolerate failure, using their motivation to push through challenges.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss ambition and self-confidence as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs always strive to reach their future dreams.",
                "They are self-driven to achieve their goals.",
                "They have a high level of enthusiasm.",
                "They are willing to learn from their mistakes.",
            ],
            sample_answer="Ambitious, self-confident entrepreneurs always strive to reach their future dreams and are self-driven to achieve their goals. They have a high level of enthusiasm and are willing to learn from their mistakes.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss a high degree of commitment as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs are not afraid to make sacrifices to realise their dreams.",
                "They are open-minded towards learning about people and the future.",
                "They have high standards and cannot tolerate mediocrity.",
                "They are committed to their business idea and work hard to achieve goals.",
            ],
            sample_answer="A high degree of commitment means entrepreneurs are not afraid to make sacrifices for their dreams. They are open-minded about learning, have high standards that do not tolerate mediocrity, and work hard to achieve their goals.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss willpower to overcome obstacles as a quality of an entrepreneur. (4)",
            marking_points=[
                "Entrepreneurs can solve problems and establish a successful business.",
                "They are ambitious, set goals and work to achieve them.",
                "They are motivated to keep going even when things are not in their favour.",
                "Their hard work ensures success can be achieved.",
            ],
            sample_answer="Willpower to overcome obstacles means entrepreneurs can solve problems and build a successful business. They are ambitious, set and work towards goals, stay motivated even when things are not in their favour, and their hard work ensures success.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_entrepreneurial_qualities = build_generate(_pools)
