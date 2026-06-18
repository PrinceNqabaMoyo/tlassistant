"""Grade 10 Business Studies - Term 1 - Topic 3: The market environment.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed, pick_scenario

PREFIX = "g10bs_market"
VAID = "market_environment"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The market environment of a business is best described as the …",
            options=[
                "internal environment over which the business has full control",
                "immediate external environment that the business can influence but not fully control",
                "macro environment over which the business has no control",
                "physical resources owned by the business",
            ],
            correct_index=1,
            explanation="The market environment is the immediate external environment; the business has limited control but can influence it.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Individuals or businesses that provide a business with inputs/raw materials are called …",
            options=["consumers", "suppliers", "intermediaries", "competitors"],
            correct_index=1,
            explanation="Suppliers provide the inputs/resources a business needs to produce its goods and services.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Agents or businesses that distribute and sell the goods of other businesses, linking producer and consumer, are …",
            options=["intermediaries", "regulators", "unions", "competitors"],
            correct_index=0,
            explanation="Intermediaries (wholesalers, retailers, agents, brokers) bridge the gap between producers and consumers.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that sell more or less the same goods/services are known as …",
            options=["suppliers", "intermediaries", "competitors", "strategic allies"],
            correct_index=2,
            explanation="Competitors sell more or less the same goods/services, forcing businesses to compete on quality and price.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Government bodies that make rules and regulations to monitor businesses (e.g. SABS, ACSA) are called …",
            options=["unions", "regulators", "CBOs", "intermediaries"],
            correct_index=1,
            explanation="Regulators are government bodies that make rules and regulations to control business activities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An organised group of workers that protects the interests of its members is a/an …",
            options=["union", "NGO", "CBO", "strategic ally"],
            correct_index=0,
            explanation="A union is an organised group of workers that protects members' interests and negotiates wages and conditions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Non-profit organisations that operate separately from government to meet community needs are …",
            options=["regulators", "NGOs", "competitors", "intermediaries"],
            correct_index=1,
            explanation="NGOs are non-governmental, non-profit organisations established to fulfil community needs.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that combine their resources to undertake a project that benefits all of them are …",
            options=["competitors", "strategic allies", "regulators", "unions"],
            correct_index=1,
            explanation="Strategic allies combine resources and share expertise to benefit all members of the alliance.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is an OPPORTUNITY in the external environment?",
            options=[
                "Increase in taxes",
                "New businesses entering the market",
                "Decline in interest rates",
                "Industrial action (strikes)",
            ],
            correct_index=2,
            explanation="A decline in interest rates is an opportunity; increased taxes, new entrants and strikes are threats.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is a THREAT in the external environment?",
            options=[
                "Decrease in taxes",
                "Closing down of a competitor",
                "Increase in interest rates",
                "Favourable government legislation",
            ],
            correct_index=2,
            explanation="An increase in interest rates is a threat; the others are opportunities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A business identifies opportunities and threats in its environment by conducting a …",
            options=["SWOT analysis", "PESTLE forecast", "balance sheet", "cash budget"],
            correct_index=0,
            explanation="A SWOT analysis identifies strengths, weaknesses, opportunities and threats.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=f"{biz} buys its raw materials from another business at fixed prices via a long-term contract. That other business is its …",
            options=["competitor", "supplier", "regulator", "intermediary"],
            correct_index=1,
            explanation="The business providing inputs/raw materials is the supplier; long-term contracts build good supplier relationships.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of the market environment. (2)",
            marking_points=[
                "It is the immediate external environment of the business.",
                "The business has limited/little control over it but can influence it.",
            ],
            sample_answer="The market environment is the immediate external environment of the business. The business has limited control over it but is able to influence its components to some extent.",
            marks=2,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between CBOs and NGOs. (8)",
            marking_points=[
                "CBOs assist the community with job creation, socio-economic development and self-sufficiency.",
                "CBOs are local organisations providing social services aimed at social upliftment.",
                "NGOs are non-profit organisations that operate separately from government.",
                "NGOs are established to fulfil important community needs by addressing socio-economic issues.",
            ],
            sample_answer="CBOs are local community-based organisations that assist with job creation and socio-economic development, aiming at social upliftment. NGOs are non-profit organisations operating separately from government, established to address socio-economic issues and meet important community needs.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Describe intermediaries as a component of the market environment. (4)",
            marking_points=[
                "Individuals or businesses that distribute and sell the products/services of a business.",
                "They bridge the gap between producers and consumers.",
                "Include wholesalers, retailers, agents, brokers and transport services.",
                "Some assist businesses with packaging and advertising.",
            ],
            sample_answer="Intermediaries are individuals or businesses that distribute and sell the products of other businesses, bridging the gap between producers and consumers. They include wholesalers, retailers, agents and brokers, and some also help with packaging and advertising.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of 'opportunities' and give TWO practical examples. (4)",
            marking_points=[
                "Opportunities are external factors that contribute to the success of the business.",
                "Example: decrease in taxes / decline in interest rates.",
                "Example: closing down of a competitor / favourable legislation.",
            ],
            sample_answer="Opportunities are factors in the external environment that contribute, or are already contributing, to the success of the business. Examples include a decline in interest rates and the closing down of a competitor.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of 'threats' and give TWO practical examples. (4)",
            marking_points=[
                "Threats are external factors that prevent the business from achieving its goals.",
                "Example: increase in taxes / increase in interest rates.",
                "Example: new businesses entering the market / industrial action.",
            ],
            sample_answer="Threats are factors in the external environment that stand in the way of the business achieving its goals. Examples include an increase in taxes and new businesses entering the market.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the role of unions in the market environment. (4)",
            marking_points=[
                "Unions protect the interests of workers.",
                "They negotiate for better wages, salaries and working conditions.",
                "They may call for industrial action such as strikes or go-slows.",
                "They safeguard members against unfair dismissal and represent them at disciplinary hearings.",
            ],
            sample_answer="Unions are established bodies that protect workers' interests. They negotiate for better wages and working conditions, may call for industrial action like strikes, and safeguard members against unfair dismissal, representing them at disciplinary hearings.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain why NGOs and CBOs form part of the market environment. (4)",
            marking_points=[
                "They supply consumer goods and services.",
                "They are concerned about the welfare of others.",
                "They are local organisations providing social services aimed at social upliftment.",
            ],
            sample_answer="NGOs and CBOs form part of the market environment because they supply consumer goods and services and are concerned about the welfare of others, operating locally to provide social services aimed at social upliftment.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss strategic allies as a component of the market environment. (4)",
            marking_points=[
                "Strategic allies are businesses that combine their resources to undertake a project.",
                "The project benefits all members of the alliance.",
                "They share expertise and information.",
                "Alliances help explore new markets and gain competitive advantage.",
            ],
            sample_answer="Strategic allies are businesses that combine their resources to undertake a project that benefits all of them. They share expertise and information, which helps them explore new markets and gain a competitive advantage.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_market_environment = build_generate(_pools)
