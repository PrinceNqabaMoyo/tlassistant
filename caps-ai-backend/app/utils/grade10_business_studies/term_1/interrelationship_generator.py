"""Grade 10 Business Studies - Topic 5: Interrelationship of the micro, market
and macro environments.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_interrel"
VAID = "interrelationship"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which environment has the biggest control and influence over the other two?",
            options=["Micro environment", "Market environment", "Macro environment", "They are equal"],
            correct_index=2,
            explanation="The macro environment has the biggest influence; the micro and market environments can only adapt to it.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'TEBO Ltd uses the services of Malo Distributors to supply products to customers.' This shows a relationship with …",
            options=["suppliers", "intermediaries", "competitors", "consumers"],
            correct_index=1,
            explanation="A business that distributes/sells goods to customers is an intermediary.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'A supermarket discovers another grocery store has opened nearby.' The new store is a …",
            options=["supplier", "intermediary", "competitor", "regulator"],
            correct_index=2,
            explanation="A business selling more or less the same goods/services is a competitor.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'A business purchases raw materials in bulk from Birchwood Ltd.' Birchwood Ltd is a …",
            options=["supplier", "competitor", "consumer", "intermediary"],
            correct_index=0,
            explanation="A business that provides raw materials/inputs is a supplier.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An increase in the interest rate (macro) raises production costs (micro), which raises prices and lowers consumer demand (market). This best illustrates …",
            options=[
                "that the three environments are independent",
                "the interrelationship between the three environments",
                "that the micro environment controls the macro environment",
                "that the market environment is the most powerful",
            ],
            correct_index=1,
            explanation="A change in one environment flows through to the others — this is their interrelationship.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which function coordinates all the other functions to achieve the vision and mission of the business?",
            options=["Marketing function", "General management function", "Purchasing function", "Administration function"],
            correct_index=1,
            explanation="General management coordinates the other functions and seeks information/advice from departmental heads.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Reliable suppliers are those that deliver raw materials at the right quality, quantity, price and …",
            options=["colour", "time", "weight", "brand"],
            correct_index=1,
            explanation="Reliable suppliers deliver the right quality, quantity, price and at the right time.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An individual or business that sells the goods of another business for a commission is a/an …",
            options=["agent", "regulator", "union", "consumer"],
            correct_index=0,
            explanation="An agent distributes and sells the goods/services of another business for a commission.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Evaluate the interrelationships that exist WITHIN the micro environment. (6)",
            marking_points=[
                "Interrelationship between business functions: the eight functions depend on each other.",
                "Interrelationship between departments: e.g. production informs purchasing of the resources needed.",
                "Interrelationship between employer and employee: employees perform duties; employers remunerate and consult them.",
            ],
            sample_answer="Within the micro environment the eight business functions depend on one another, for example general management consults administration for information. Departments also depend on each other, such as production informing purchasing of the resources required. Finally, employers and employees are interrelated: employees perform duties and are remunerated and consulted by employers.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the reasons why competition poses a challenge to businesses. (6)",
            marking_points=[
                "Competition is not within the control of the business.",
                "Consumers buy where they get the most value for money and may choose a competitor.",
                "A business may be unable to make sufficient profit when demand is not high enough.",
                "It is hard to differentiate from competitors to gain a competitive advantage.",
                "New entrants with better products can divide the market and reduce market share.",
            ],
            sample_answer="Competition is challenging because it is outside the business's control. Consumers buy where they get the most value and may choose a competitor, so a business may struggle to make sufficient profit. It is also hard to differentiate from rivals, and new entrants with better products can reduce the business's market share.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between businesses and their consumers. (6)",
            marking_points=[
                "Consumers depend on businesses for goods/services; businesses depend on consumers for income.",
                "Without consumers a business cannot survive, so it must produce consistently high-quality goods.",
                "Public relations must maintain a positive image so customers stay loyal.",
                "Marketing must conduct market research to satisfy changing consumer needs.",
            ],
            sample_answer="Consumers depend on businesses for goods and services, while businesses depend on consumers for income. Because a business cannot survive without consumers, it must produce consistently high-quality goods, maintain a positive image through public relations, and conduct market research to satisfy changing consumer needs.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between a business and its suppliers. (6)",
            marking_points=[
                "Businesses depend on suppliers for raw materials and inputs.",
                "Without raw materials a business cannot produce its goods/services.",
                "Businesses must identify reliable suppliers (right quality, quantity, price, time).",
                "Good relationships are maintained by paying on time and signing long-term contracts.",
            ],
            sample_answer="Businesses depend on suppliers for raw materials and inputs, without which they cannot produce. They must identify reliable suppliers who deliver the right quality, quantity and price at the right time, and maintain good relationships by paying on time and signing long-term contracts at fixed prices.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how a change in the macro environment can affect the micro and market environments. (4)",
            marking_points=[
                "Changes in the macro environment may affect the micro environment, then the market environment.",
                "Example: an increase in interest rates raises production costs.",
                "Higher production costs raise the prices of goods/services.",
                "Higher prices decrease consumer spending/demand.",
            ],
            sample_answer="A change in the macro environment flows through to the micro and then the market environment. For example, an increase in interest rates raises production costs in the micro environment, which increases prices, and this in turn decreases consumer spending in the market environment.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between a business and its intermediaries. (4)",
            marking_points=[
                "Intermediaries distribute and sell the goods of the business; they link business and consumers.",
                "Businesses must maintain good relationships and monitor intermediaries' activities.",
                "Intermediaries must be reliable and efficient as they affect quality and price.",
                "Intermediaries are also customers of the business and should be treated with care.",
            ],
            sample_answer="Intermediaries distribute and sell a business's goods, linking it to consumers. The business must monitor and maintain good relationships with them because their reliability and efficiency affect the quality and price of goods. Intermediaries are also customers, so they should be treated with care.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_interrelationship = build_generate(_pools)
